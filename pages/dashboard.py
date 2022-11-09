from pages.base_page import BasePage


class Dashboard(BasePage):
    logo_scouts_panel = '//div[@class="MuiCardMedia-root jss38"]'
    sign_out_element = '//span[contains(text(),"Sign out")]'
    print_button = '//button[@aria-label="menu"]'
    view_columns_button = '//button[@title="View Columns"]'
    search_bar_field = '//input[@class="MuiInputBase-input jss54"]'
    add_player_link = '//a[@href="/en/players/add"]'
    language_choosing_button = '//div[@role="button"]'
    age_field = '//input[@name="age"]'
    dev_team_contact_button = '//span[contains(text(), "contact")]'
    main_page_button = '//span[contains(text(),"Main page")]'
    main_page_button = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    player_match_and_report_management_panel = '//p[contains(@class, MuiTypography-root)]'

    pass





