from utilities.readconfig import ReadConfig


class TestCasesForLogin:
    home_page = ReadConfig.get_home_page()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.home_page)
        login_title = self.driver.title
        assert "nopCommerce demo store" == login_title
