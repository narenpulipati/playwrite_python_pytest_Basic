import os
import pytest
import allure
from playwright.sync_api import Browser


# ==================================================
# Capture test result (shared by pytest-html & Allure)
# ==================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ==================================================
# Browser Context (video + trace for Allure)
# ==================================================

@pytest.fixture(scope="function")
def context(browser: Browser):
    os.makedirs("reports/videos", exist_ok=True)
    os.makedirs("reports/traces", exist_ok=True)

    context = browser.new_context(
        record_video_dir="reports/videos",
        record_video_size={"width": 1280, "height": 720}
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context
    context.close()


# ==================================================
# Page fixture
# ==================================================

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ==================================================
# Attach artifacts AFTER test
# ==================================================

@pytest.fixture(autouse=True)
def attach_artifacts(request, context):
    yield

    if not hasattr(request.node, "rep_call") or not request.node.rep_call.failed:
        return

    os.makedirs("reports/screenshots", exist_ok=True)

    # ---------- Screenshot (pytest-html + Allure) ----------
    for page in context.pages:
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path)

        # Allure attachment
        with open(screenshot_path, "rb") as f:
            allure.attach(
                f.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        # pytest-html attachment
        html = request.config.pluginmanager.getplugin("html")
        if html:
            extra = getattr(request.node.rep_call, "extra", [])
            extra.append(html.extras.image(screenshot_path))
            request.node.rep_call.extra = extra

    # ---------- Video (Allure only) ----------
    for page in context.pages:
        if page.video:
            video_path = page.video.path()
            with open(video_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name="Failure Video",
                    attachment_type=allure.attachment_type.WEBM
                )

    # ---------- Trace (Allure only) ----------
    trace_path = f"reports/traces/{request.node.name}.zip"
    context.tracing.stop(path=trace_path)

    with open(trace_path, "rb") as f:
        allure.attach(
            f.read(),
            name="Playwright Trace",
            attachment_type=allure.attachment_type.ZIP
        )
