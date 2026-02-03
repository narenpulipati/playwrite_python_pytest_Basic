import pytest
from playwright.sync_api import Page,expect

#mouse hover actions
def test_mouse_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator(".dropbtn").hover()
    page.locator(".dropdown-content a:nth-child(2)").hover()

#right click functionality

def test_mouse_right_click(page:Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    right_click=page.locator(".context-menu-one")
    right_click.click(button="right")


#double click functionality

def test_mouse_double_click(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    button=page.get_by_text("Copy Text")
    button.dblclick()
    text=page.locator("id=field2")
#    expect(text).to_have_value("Hello World!")

#drag and drop the elements
def test_drag_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    element1=page.locator("id=draggable")
    element2=page.locator("id=droppable")
    element1.drag_to(element2)


