
from playwright.sync_api import Page, expect

def test_css_locator(page:Page):
    page.goto('https://demowebshop.tricentis.com/',wait_until="load")
#verfiy logo and make some assertions
    logo=page.locator('img[alt="Tricentis Demo Web Shop"]')
    logo.get_by_title('Demo Web Shop')
    expect(logo).to_be_visible()
    expect(logo).to_have_attribute( "alt","Tricentis Demo Web Shop")
    expect(logo).to_have_attribute( "src","/Themes/DefaultClean/Content/images/logo.png")
    expect(logo).to_have_count(1)
#capture all computer related elements and capture the count
    products = page.locator('//a[contains(text(),"computer")]')
    products.first.wait_for(state="visible")
    total = products.count()
    print(f"Total computer products found: {total}\n")


    page.goto('https://demowebshop.tricentis.com/')
    products = page.locator("//a[contains(text(), 'computer')]")
    products_count = products.count()
    print("products count : ", products_count)
    expect(products).to_have_count(products_count)
#printing the product names individually
    '''print(products.first.text_content())
    print(products.last.text_content())
    print(products.nth(1).text_content())
    print(products.nth(0).text_content())'''
#using for loop to print the products list
    print("\n Below are the products list:\n")
    for product in range(products_count):
        print(products.nth(product).text_content())
#Below is the play-write inbuilt
    '''product_names=products.all_text_contents()
    
        print(i)'''






