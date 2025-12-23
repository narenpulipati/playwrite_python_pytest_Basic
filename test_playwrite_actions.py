#this program contains max types of locators and assertions w.r to input-box check box

from playwright.sync_api import Page, expect

def test_page_actions(page:Page):
    #opem the website
    page.goto("https://testautomationpractice.blogspot.com/")

#click on a element (button element)
    #page.get_by_role("button", name="Simple Alert").click()---by role of the element
    #page.get_by_text("Simple Alert").click() ---- by text
    #page.locator('div button[id="alertBtn"]').click() ----by CSS
    #page.locator('//div//button[@id="alertBtn"]').click() #---by xpath
    #page.locator("id=alertBtn").click() ---by id
#button element validations
    #button1=page.locator("button").nth(0)
    #button1.click()
    #expect(button1).to_be_visible()
    #expect(button1).to_be_enabled()
    #expect(button1).to_have_count(1)

#check the checkbox and asser whether it is checked or not
    #page.locator('id=monday').check()---by locator id
    #page.locator("//div//input[@id='monday']").check()#-----by Xpath
    #page.locator('#monday').check()---by css
    #page.locator('input[type="checkbox"][id="monday"]').check()--5. By combination of attributes
    #page.locator('div input[class="form-check-input"][type="checkbox"]').nth(1).check()-- By index nth-of-type / nth-child
    #page.locator('div input[class="form-check-input"][id="monday"]').check()# -- by using css 2 elements
    #page.get_by_text('monday').check()#---by id
    page.get_by_role('checkbox',name='monday').check()
    #page.get_by_label('Monday').check()
#assrtions on checkbox
    expect(page.locator('id=monday')).to_be_checked()
    expect(page.locator('id=monday')).to_be_visible()
    #expect(page.locator('id=monday')).to_be_enabled()
    expect(page.locator('id=monday')).to_have_id('monday')
    expect(page.locator('id=monday')).to_have_attribute("type", "checkbox")
    expect(page.locator('id=monday')).to_have_attribute("value", "monday")
    expect(page.locator('#monday')).to_have_class("form-check-input")
    expect(page.locator('#monday')).to_be_editable()
    expect(page.locator('#monday')).to_have_count(1)
    page.wait_for_timeout(2000)

    # uncheck the checkbox and asser whether it is checked or not
    page.locator('id=monday').uncheck()
    expect(page.locator('id=monday')).not_to_be_checked()


    #click in input box, Enter the text
    #page.get_by_placeholder("Enter Name").fill("Narendrapulipati")---by placeholder
    page.locator('id=name').fill('Narendrapulipati')
    page.wait_for_timeout(3000)









