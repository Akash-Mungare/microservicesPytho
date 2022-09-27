from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
# from config.config import testData
import pytest
import allure
from allure_commons.types import AttachmentType

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()

# class test_microservices():
    # @pytest.fixture()
    # def __init__(self):
    #     self.setup(self);
        
@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestCase:    
    # def test_homePageTitle(self):
    #     time.sleep(2)
    #     self.driver.get("http://20.219.249.1/login")
    #     assert self.driver.title == "Asset Tracking"


    @pytest.mark.usefixtures("setup")
    def test_login(self):
        self.driver.get("http://20.219.249.1/login")
        self.driver.find_element(By.ID,"mat-input-0").send_keys("akashmungare112@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID,"mat-input-1").send_keys("Akash@123")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,"mat-button-wrapper").click()
        time.sleep(8)
        assert self.driver.title == "Asset Tracking"
        allure.attach(driver.get_screenshot_as_png(),name="DoLogin",attachment_type=AttachmentType.PNG)
        
        """   Created Find   """ 
        self.driver.find_element(By.XPATH,'//button[@class="mat-focus-indicator mat-raised-button mat-button-base"]').click() #Click on Add_Find
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@formcontrolname="deviceId"]').send_keys("6001") # Entering the text
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//button[ @class="mat-focus-indicator mat-raised-button mat-button-base mat-primary"]').click() #submit button
        time.sleep(2)
        add_find = self.driver.find_element(By.XPATH,"//*[@class='mat-simple-snackbar ng-star-inserted']/span").text #getting success text
        time.sleep(2)
        assert  add_find == "Asset registered successfully" #checking add_find is matching with the context
        allure.attach(driver.get_screenshot_as_png(),name="addFind",attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator float-right mat-button mat-button-base']").click() #Add_ find close button
        
        """   Delete created Find  """
        time.sleep(2)
        del_asset = "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/app-manage-asset/mat-tab-group/div/mat-tab-body[1]/div/app-manage-device/div[2]/table/tbody/tr[10]"
        self.driver.find_element(By.XPATH,del_asset).click()
        time.sleep(2)
        for i in range(1,25):
            # print(("==========================>>>>>>>>>>>>>>>> i:",i).encode('utf8'))
            find_col = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/app-manage-asset/mat-tab-group/div/mat-tab-body[1]/div/app-manage-device/div[2]/table/tbody/tr['+str(i)+']/td[2]'
            # print("==================================>>>>>>>>>>>>>>>>>>>",find_col)
            del_find = self.driver.find_element(By.XPATH,find_col).text
            # print(("==========================>>>>>>>>>>>>>>>> del find:",del_find).encode('utf8'))
            time.sleep(2)
            # driver.execute_script("window.scrollBy(0,6000)","")
            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
            if del_find == "6001":
                time.sleep(2)
                del_find = self.driver.find_element(By.XPATH,'//div[@class="mat-paginator-page-size-label"]').click()
                time.sleep(4)
                del_Assset1 = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/app-manage-asset/mat-tab-group/div/mat-tab-body[1]/div/app-manage-device/div[2]/table/tbody/tr['+str(i)+']/td[9]/mat-icon'
                # driver.execute_script("window.scrollTo(0, del_Assset1.scrollHeight);")
                time.sleep(4)
                # print("=========================>>>>>>>>>>>> del_Asset: ", del_Assset1)
                self.driver.find_element(By.XPATH,del_Assset1).click()
                time.sleep(4)
                alert = Alert(driver)
                time.sleep(2)
                alert.accept()
                time.sleep(4)
                del_find_text = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/snack-bar-container/div/div/simple-snack-bar/span').text
                assert del_find_text == "Asset deleted successfully"
                allure.attach(driver.get_screenshot_as_png(),name="deleteFind",attachment_type=AttachmentType.PNG)
                break
            else:
                # print(('==============>>>>>>>>>>>>>>>>>> else:',i).encode('utf8'))
                # print(null)
                continue
        
        """   Delete created Find  """
        time.sleep(2)


        # time.sleep(2)
        # self.driver.find_element(By.XPATH,'//div[@aria-posinset="2"]').click() #Click on Manage Coins
        # time.sleep(2)
        
# add_Asset = test_microservices()
# add_Asset.setup()
