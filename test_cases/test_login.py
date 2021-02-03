from selenium import webdriver


class TestCasesForLogin:

    def test_login(self, setup):
        self.driver = setup
        self.driver.get("https://frontend.nopcommerce.com/")
        login_title = self.driver.title
        # self.driver.close()
        assert "nopCommerce demo store" == login_title
