from playwright.sync_api import Page
from pages.base_page import BasePage



class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.get_in_touch = page.get_by_role("heading", name="Get In Touch")
        self.name_input = page.get_by_test_id("name")
        self.email_input = page.get_by_test_id("email")
        self.subject_input = page.get_by_test_id("subject")
        self.message_input = page.get_by_test_id("message")
        self.upload_file_button = page.locator("//input[@type='file']")
        self.submit_button  = page.get_by_test_id("submit-button")

    # one element (single) methods
    def get_in_touch_heading(self):
        return self.get_in_touch.inner_text()

    def enter_name(self, name):
        self.name_input.fill(name)

    def enter_email(self, email):
        self.email_input.fill(email)

    def enter_subject(self, subject):
        self.subject_input.fill(subject)

    def enter_message(self, message):
        self.message_input.fill(message)

    def submit_form(self, dialog_expected):
        self.handle_dialog(trigger_action=lambda: self.submit_button.click(),
                           expected_text="Press OK to proceed!", dialog_expected=dialog_expected)



    # wrapper method
    def fill_contact_form(self, name, email, subject, message, filepath=None):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)

        ## file upload is optional
        if filepath:
            self.upload_file(trigger_action=lambda: self.upload_file_button.click(), filepath=filepath)


