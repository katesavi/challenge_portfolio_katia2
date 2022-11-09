from pages.base_page import BasePage


class Dashboard(BasePage):
    age_field = '//input[@name="age"]'
    name_field = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input'
    main_page_button = '//span[contains(text(),"Main page")]'
    sign_out_button = '//span[contains(text(),"Sign out")]'
    matches_button = '//span[contains(text(),"Matches")]'
    remove_language_button = '//button[@aria-label="Remove language"]'
    player_name_button = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]'
    clear_button_label = '//span[@class="MuiButton-label"][contains(text(),"Clear")]'
    clear_button = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary"]'
    add_match_button = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss34"]'






    pass

