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

class EditText(unittest.TestCase, BasicFunctions):
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

	# self.windowSize = self.driver.get_window_size()
	# self.windowWidth = self.windowSize['width']
	# self.windowHeight = self.windowSize['height']

	def test_01_addTitle(self):
		#self.driver.find_element_by_id("edit").click()
		self.driver.find_element_by_id("cover_title").send_keys("test_03_addTitle: %s" % self.random_str(46))
		self.driver.back()

	def test_02_editBody(self):
		text = self.readFile("text.txt")
		self.driver.find_element_by_name(u"正文").send_keys(text)
		self.driver.back()

	def test_03_addGuide(self):
		self.driver.find_element_by_name(u"正文").click()
		self.driver.find_element_by_id("act_editor_more").click()
		self.driver.find_element_by_id("act_editor_summary").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=self.getScreenWidth()/2,y=self.getScreenHeight()/2-100).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("dialog_summary").send_keys("EditText.test_03_addGuide")
		self.driver.find_element_by_id("buttonDefaultPositive").click()
		self.driver.back()
		#修改导语
		while True:
			try:
				self.driver.find_element_by_id("cover_summary").click()
				TouchAction(self.driver).press(x=self.getScreenWidth()/2,y=self.getScreenHeight()/2-100).release().perform()
				time.sleep(2)
				self.driver.find_element_by_id("dialog_summary").send_keys("I have changed the guide.")
				break
			except:
				TouchAction(self.driver).press(x=500,y=300).move_to(x=0,y=800).wait(1000).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("buttonDefaultNegative").click()
		while True:
			try:
				self.driver.find_element_by_id("cover_summary").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=300).move_to(x=0,y=800).wait(1000).release().perform()
		try:
			self.driver.find_element_by_name("EditText.test_03_addGuide").click()
		except:
			self.fail("The guide should be 'EditText.test_03_addGuide'.")
		time.sleep(2)
		TouchAction(self.driver).press(x=self.getScreenWidth()/2,y=self.getScreenHeight()/2-100).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("dialog_summary").send_keys("I have changed the guide again.")
		self.driver.find_element_by_id("buttonDefaultPositive").click()
		while True:
			try:
				self.driver.find_element_by_id("cover_summary").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=300).move_to(x=0,y=800).wait(1000).release().perform()
		try:
			self.driver.find_element_by_name("I have changed the guide again.")
		except:
			self.fail("The change of the guide should be 'I have changed the guide again'.")

	def test_04_setType(self):
		#self.driver.find_element_by_id("draft_layout").click()
		text = ['headline1','quote','list']
		Type = ['act_editor_paragraph_type','act_editor_blockquote','act_editor_ul']
		for i in range(0,len(text)):
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys(text[i])
			print Type[i]
			self.driver.find_element_by_id(Type[i]).click()
			self.driver.find_element_by_id("act_back").click()
			self.driver.find_element_by_id("edit").click()
			time.sleep(2)
		
	def test_05_H2(self):
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys("headline2")
		self.driver.find_element_by_id("act_editor_paragraph_type").click()
		self.driver.find_element_by_id("act_editor_paragraph_type").click()
		self.driver.find_element_by_id("act_back").click()


	def test_06_link(self):
		#self.driver.find_element_by_id("edit").click()
		self.driver.find_element_by_name(u"正文").click()
		self.driver.find_element_by_id("act_editor_link").click()
		TouchAction(self.driver).press(x=self.getScreenWidth()/2,y=self.getScreenHeight()/2-100).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("dialog_link_address").send_keys("www.baidu.com")
		self.driver.find_element_by_id("dialog_link_title").send_keys("baidu")
		self.driver.find_element_by_id("buttonDefaultPositive").click()
		time.sleep(2)
		self.driver.find_element_by_id("act_editor_link").click()
		TouchAction(self.driver).press(x=self.getScreenWidth()/2,y=self.getScreenHeight()/2-100).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("dialog_link_address").send_keys("www.baidu.com")
		self.driver.find_element_by_id("buttonDefaultPositive").click()

	def test_07_insertPreviousArticle(self):
		#self.driver.find_element_by_id("edit").click()
		self.driver.find_element_by_name(u"正文").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").click()
		time.sleep(2)
		self.driver.find_element_by_id("act_editor_more").click()
		self.driver.find_element_by_id("act_editor_pre_article").click()
		time.sleep(2)
		articleNum = self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[","]")
		for i in random.sample(range(1,articleNum),3):
			preArticle = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
			preArticle.click()
		self.driver.find_element_by_id("finish").click()
		self.driver.find_element_by_id("act_back").click()

	def test_08_setStyle(self):
		style = ["act_editor_style_bold_btn","act_editor_style_italic_btn","act_editor_style_strike_btn"]
		string = ["Bold_this_sentence.","Italic_this_sentence.","Strickthrough_this_sentence."]

		for i in range(0,len(style)):
			line = self.driver.find_element_by_name(u"正文")
			line.send_keys(string[i])
			TouchAction(self.driver).long_press(x=10,y=600).release().perform()
			self.driver.find_element_by_id(style[i]).click()
			self.driver.find_element_by_id("act_back").click()
			self.driver.find_element_by_id("edit").click()

	def test_11_setWordsTolink(self):
		#self.driver.find_element_by_id("edit").click()
		line = self.driver.find_element_by_name(u"正文")
		line.send_keys("Add_url_to_this_sentence.")
		TouchAction(self.driver).long_press(x=10,y=600).release().perform()
		self.driver.find_element_by_id("act_editor_style_link_btn").click()
		time.sleep(2)
		size = self.driver.get_window_size()
		TouchAction(self.driver).press(x=size['width']/2,y=size['height']/2-100).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("dialog_link_address").send_keys("www.baidu.com")
		self.driver.find_element_by_id("buttonDefaultPositive").click()
		self.driver.find_element_by_id("act_editor_finish").click()

	def test_12_changeColor(self):
		#self.driver.find_element_by_id("edit").click()
		line = self.driver.find_element_by_name(u"正文")
		line.send_keys("Change_the_color_of_this_sentence.")
		TouchAction(self.driver).long_press(x=10,y=600).release().perform()
		self.driver.find_element_by_id("act_editor_style_color_btn").click()
		time.sleep(2)
		index = random.randint(2,7)
		print index
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.ImageView["+str(index)+"]").click()
		self.driver.find_element_by_id("act_editor_finish").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EditText)
    unittest.TextTestRunner(verbosity=2).run(suite)