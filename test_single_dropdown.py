from playwright.sync_api import Page,expect

def test_single_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    drop_down=page.locator('#country')
    print("\n Default selected:", drop_down.input_value())

    #validations on dropdown
    expect(drop_down).to_be_visible()
    expect(drop_down).to_be_enabled()

    #page.get_by_label("Country:").click()
    #drop_down.select_option("India")#---- without label
#below code is changed
    drop_down.select_option(label="India") #---by label
    expect(drop_down).to_have_value("india") #validating dropdown selected value


    drop_down.select_option("uk") #---by value
    #drop_down.select_option(index=4) ----by index
    page.wait_for_timeout(5000)

    #counting the dropdown elements
    drop_down_options=page.locator("#country>option") # using css locator

    print("drop down count: ",drop_down_options.count())
    expect(drop_down_options).to_have_count(10)

    print("\n Below are the countries list: ")

    for text in drop_down_options.all_text_contents():  #all_text_contents() will get all text data
        print(text.strip())#-----strip is used to remove spaces


