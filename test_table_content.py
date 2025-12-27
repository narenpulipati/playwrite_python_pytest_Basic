import pytest
from playwright.sync_api import Page,expect

def test_table_static(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table=page.locator("table[name='BookTable']")
    expect(table).to_be_visible()

    #count number of rows in table and assert
    #rows=page.locator("table[name='BookTable'] tr")  #actuall navigation
    rows=table.locator("tr")        #shortcut where as we already have table element located

    row_count = rows.count()
    print("\n Number of rows: ", row_count)
    expect(rows).to_have_count(row_count)  #asserting rows count


    # count number of column in table and assert
    column=table.locator('th')
    column_count=column.count()
    print("\n Number of column: ",column_count)
    expect(column).to_have_count(column_count)    #asserting column count


    print("\n Printing second row data: ")
    #read the second row data
    #using for loop
    read_row_data=rows.nth(2)
    for text in read_row_data.all_text_contents():
        print(text)
    #using inner text method
    read_row_data1 = rows.nth(1).locator('td')
    read_row_text=read_row_data1.all_inner_texts()
    print(read_row_text)
    expect(read_row_data1).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])


    print("\n Printing All rows data :")
    #getting all the rows and columns data
    all_row_data = rows.all()                   # all method will get all rows data
    for rows in all_row_data:                   #navigating each row in all_row_data
        col=rows.locator('td').all_inner_texts() # getting row inner text
        print(col)                                  # printing the row text and it will repeat


    print("\n Below are the Books Authored by Amit: ")
    # Get the book names by author Amit
    for rows in all_row_data[1:]:                   #navigating each row in all_row_data and header row skiped
        author_name=rows.locator('td').nth(1).inner_text() # getting authors column inner text
        #print(author) #printing author names
        if author_name=='Amit':
            book_name = rows.locator('td').nth(0).inner_text()
            print(author_name, ":",book_name)

    #caluculate total prices
    total_price=0
    for rows in all_row_data[1:]:                   #navigating each row in all_row_data and header row skiped
        prices=rows.locator('td').nth(3).inner_text()
        total_price+=int(prices)  # prices we got the string covert it into int to add prices
    print(total_price)

