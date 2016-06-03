from pages.internal_page import InternalPage
from pages.blocks.user_form import UserForm


class UserProfilePage(InternalPage):

    def __init__(self, driver, base_url):
        super(UserProfilePage, self).__init__(driver,base_url)
        self.user_form = UserForm(self.driver, self.base_url)

