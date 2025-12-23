from playwright.sync_api import Page,expect

def test_css(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    title=page.get_by_title('Automation Testing Practice')

#input boxes
    page.locator('#textarea').fill('Hyderabad')
    page.locator('#name').fill('Narendra Pulipati')
    page.locator('#email').fill('pulipati@123.com')

#button element
    button=page.locator("div input[id='female']")
    button1=page.locator("id=male")
    button.click()
    button1.click()
    page.wait_for_timeout(3000)
    #expect(button).to_be_enabled()

#check box
    checkbox=page.locator("input#sunday")
    checkbox1=page.locator("div input[class='form-check-input'][id='saturday']")
    checkbox.check()
    checkbox1.click()
    expect(checkbox).to_be_checked()
    print("\n The day clicked :", page.locator("label[for='sunday']").text_content())
    total_days=page.locator("label[for*='day']")
    total_days_count=total_days.count()
    print('Total number of days : ',total_days_count)

#printing all days
    page.locator("label[for *= 'day']")
    all_days=page.locator("label[for*='day']").all_text_contents()
    for day in all_days:
        print(day)

#click on one or two days using nth
    page.locator("label[for *= 'day']").nth(5).click()
    page.locator("label[for *= 'day']").nth(3).click()
    page.wait_for_timeout(3000)
