from utilities.readconfig import ReadConfig
from utilities.custom_logging import LogGen


class TestCasesForLogin:
    home_page = ReadConfig.get_home_page()
    logger = LogGen.log_gen()

    def test_login(self, setup):
        self.logger.info("Executing 'test_login'")
        self.driver = setup
        self.logger.info("Opening home page of website")
        self.driver.get(self.home_page)
        self.logger.info("Extraced title of the webpage")
        login_title = self.driver.title
        assert "nopCommerce demo store" == login_title, 'Verifying webpage title'
        self.driver.save_screenshot(".\\Screenshots\\" + 'test_homepageTitle.png')
