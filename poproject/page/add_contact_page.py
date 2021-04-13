from page.base_func import BaseFunc


class AddContactPage(BaseFunc):
    upfile = '#js_upload_file_input'
    def add_contact(self):
        self.find(self.upfile).click()