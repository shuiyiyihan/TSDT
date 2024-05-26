from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        #executable_path=r'D:\anaconda\envs\yyy\chromedriver.exe'  
        #https://blog.csdn.net/weixin_60535956/article/details/131660133救命文章
        
    def tearDown(self):
        self.browser.quit() 
        
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页里面包含'To-Do'这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do', header_text)
        
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item')
        
        inputbox.send_keys('Buy flowers')
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy flowers')
        
        #他按了回车键后，页面更新了
        #代办事项表格中显示了"1: Buy flowers"
        
        #页面中又显示了一个文本框，可以输入其他待办事项
        #他输入了“gift to girlfriend”
        inputbox= self.browser.find_element(By.ID,'id_new_item')
        inputbox.send_keys('Give a gift ti Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # table = self.browser.find_element(By.ID,'id_list_table')
        # rows = table.find_elements(By.TAG_NAME,'tr')
        # self.assertIn('1: Buy flowers',[row.text for row in rows])
        # self.assertIn('2: Give a gift ti Lisi',[row.text for row in rows])
        self.check_for_row_in_list_table('1: Buy flowers')
        self.check_for_row_in_list_table
        
        self.fail('Finish the test!')
        
        #页面再次更新，她的清单中显示了这两个待办事项
        
if __name__ == '__main__':
    unittest.main()

