from pages.base_page import BasePage


class AddPage(BasePage):
    add_player_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button'
    name_field_xpath = '//input[@nam="name"]'
    surname_field_xpath = '//input[@name="surname"]'
    phone_field_xpath = '//input[@name="phone"]'
    weight_field_xpath = '//input[@name="weight"]'
    email_field_xpath = '//input[@name="email"]'
    leg_select_xpath = '//*[@id="mui-component-select-leg"]'
    age_select_xpath = '//input[@name="age"]'
    submit_button_xpath = '//span[contains(text(),"Submit")]'
    add_url_xpath = '//button[@aria-label="Add link to Youtube"]'
    clear_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]'
    expected_title = "Add player"
    adding_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        pass

    def type_in_name(self, param):
        pass

    def type_in_surname(self, param):
        pass

    def type_in_phone(self, param):
        pass

    def type_in_weight(self, param):
        pass

    def type_in_email(self, param):
        pass

    def type_in_click_the_submit_button(self):
        pass

    def type_in_level(self, param):
        pass


def type_in_email(self, email):
    self.field_send_keys(self.login_field_xpath, email)


def click_the_add_player_button(self):
    self.click_on_the_element(self.sign_in_button_xpath)



def type_in_name(self, name):
    self.field_send_keys(self.name_field_xpath)


def type_in_surname(self, surname):
    self.field_send_keys(self.surname_field_xpath)


def type_in_phone(self, phone):
    self.field_send_keys(self.phone_field_xpath)


def type_in_weight(self, weight):
    self.field_send_keys(self.phone_field_xpath)
