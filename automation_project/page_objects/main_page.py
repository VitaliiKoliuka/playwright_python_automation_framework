from playwright.sync_api import Page
from automation_project.page_objects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)