from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


class TestCase:
    def login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("http://20.219.249.1/login")
        driver.find_element(By.ID,"mat-input-0").send_keys("akashmungare112@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID,"mat-input-1").send_keys("Akash@123")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,"mat-button-wrapper").click()
        time.sleep(8)
        assert driver.title == "Asset Tracking"

        """   Created Find  """
        # driver.find_element(By.XPATH,'//button[@class="mat-focus-indicator mat-raised-button mat-button-base"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH,'//*[@formcontrolname="deviceId"]').send_keys("6001")
        # time.sleep(2)
        # driver.find_element(By.XPATH,'//button[ @class="mat-focus-indicator mat-raised-button mat-button-base mat-primary"]').click()
        # time.sleep(2)
        # pass1 = driver.find_element(By.XPATH,"//*[@class='mat-simple-snackbar ng-star-inserted']/span").text
        # time.sleep(2)
        # print(pass1)
        # time.sleep(4)
        # # assert  pass1 == "Asset registered successfully"
        # driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-add-assets/button/span[1]/mat-icon').click() #Add_ find close button

        """   Delete created Find  """

        time.sleep(2)
        del_asset = "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/app-manage-asset/mat-tab-group/div/mat-tab-body[1]/div/app-manage-device/div[2]/table/tbody/tr[10]"
        driver.find_element(By.XPATH,del_asset).click()
        time.sleep(2)
        for i in range(1,25):
            print("==========================>>>>>>>>>>>>>>>> i:",i)
            find_col = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/app-manage-asset/mat-tab-group/div/mat-tab-body[1]/div/app-manage-device/div[2]/table/tbody/tr['+str(i)+']/td[2]'
            # print("==================================>>>>>>>>>>>>>>>>>>>",find_col)
            del_find = driver.find_element(By.XPATH,find_col).text
            print("==========================>>>>>>>>>>>>>>>> del find:",del_find)
            time.sleep(2)
            # driver.execute_script("window.scrollBy(0,6000)","")
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
            if del_find == "6001":
                time.sleep(2)
                del_find = driver.find_element(By.XPATH,'//div[@class="mat-paginator-page-size-label"]').click()
                time.sleep(4)
                del_Assset1 = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/app-manage-asset/mat-tab-group/div/mat-tab-body[1]/div/app-manage-device/div[2]/table/tbody/tr['+str(i)+']/td[9]/mat-icon'
                # driver.execute_script("window.scrollTo(0, del_Assset1.scrollHeight);")
                time.sleep(4)
                # print("=========================>>>>>>>>>>>> del_Asset: ", del_Assset1)
                driver.find_element(By.XPATH,del_Assset1).click()
                time.sleep(4)
                alert = Alert(driver)
                time.sleep(2)
                alert.accept()
                time.sleep(4)
                break
            else:
                print('==============>>>>>>>>>>>>>>>>>> else:',i)
                continue
        
        """   Delete created Find  """
        

        time.sleep(4)
        driver.close()

        

# add_Asset = TestCase()
# add_Asset.login()