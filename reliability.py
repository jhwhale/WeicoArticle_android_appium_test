#coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, unittest, sys, os, random, string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from basicFunction import BasicFunctions
#import codecs

class ReliabilityTest(unittest.TestCase, BasicFunctions):
	@classmethod
	def setUpClass(cls):
		desired_caps = {}
		desired_caps['appium-version'] = '1.0'
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'OnePlus'
		#desired_caps['app'] = os.path.abspath('/Users/eico/Downloads/Weico-weico-release.apk')
		desired_caps['appPackage'] = 'com.weico.weiconotepro'
		desired_caps['appActivity'] = 'com.weico.weiconotepro.MainTabActivity'

		cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def setUp(self):
		while True:
			try:
				self.driver.find_element_by_id("edit").click()
				break
			except:
				self.driver.back()
		time.sleep(2)

	def tearDown(self):
		while True:
			try:
				self.driver.find_element_by_id("avatar")
				break
			except:
				self.driver.back()
		time.sleep(2)


	def test_01_longArticle(self):
		file_object = open('log.txt', 'rb')
		try:
			while True:
				chunk = file_object.read().decode("utf8")
				if not chunk:
					break
				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys(chunk.encode("ascii","ignore"))
		finally:
			file_object.close() 

		for t in range(0,3):
			TouchAction(self.driver).long_press(x=540,y=800).release().perform()
			time.sleep(2)
			self.driver.find_element_by_id("selectAll").click()
			time.sleep(2)
			self.driver.find_element_by_id("copy").click()
			time.sleep(2)
			TouchAction(self.driver).long_press(x=540,y=800).release().perform()
			time.sleep(2)
			self.driver.find_element_by_id("paste").click()
			time.sleep(2)

	# def test_02_createMultiArticles(self):
	# 	self.createArticles()#参数为创建文章篇数，默认为10篇


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ReliabilityTest)
    unittest.TextTestRunner(verbosity=2).run(suite)