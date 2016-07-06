#coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, unittest, sys, os, random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from basicFunction import BasicFunctions

class EditImage(unittest.TestCase, BasicFunctions):
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
		# try:
		# 	self.driver.find_element_by_id("edit").click()
		# 	time.sleep(2)
		# except:
			time.sleep(2)

	def tearDown(self):
		# while True:
		# 	try:
		# 		self.driver.find_element_by_id("edit")
		# 		break
		# 	except:
		# 		self.driver.back()
		time.sleep(2)

	# def test_01_addCoverFromAlbum(self):
	# 	self.driver.find_element_by_id("edit").click()
	# 	self.driver.find_element_by_id("cover_add").click()
	# 	#获取图片数
	# 	j = random.randint(1,self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[","]/android.widget.ImageView[1]"))
	# 	print "The number %d image is selected as cover."% j
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(j)+"]/android.widget.ImageView[1]").click()
	# 	self.driver.find_element_by_id("act_crop_finish").click()#剪切页面点击完成


	# def test_02_addCoverFromCamera(self):
	# 	try:
	# 		self.driver.find_element_by_id("cover_add").click()
	# 	except:
	# 		self.driver.find_element_by_id("cover_image").click()
	# 	self.driver.find_element_by_id("act_pp_camera").click()
	# 	time.sleep(2)
	# 	#self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()#快门
	# 	self.driver.find_element_by_name(u"快门").click()
	# 	time.sleep(2)
	# 	self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]").click()#返回
	# 	time.sleep(2)
	# 	#选项
	# 	self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]").click()
	# 	time.sleep(2)
	# 	#切换前后摄像头
	# 	self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageButton[4]").click()
	# 	time.sleep(2)
	# 	self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()#快门
	# 	time.sleep(2)
	# 	#确认
	# 	self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageButton[1]").click()
 # 		time.sleep(2)
	# 	self.driver.find_element_by_id("act_crop_finish").click()#剪切页面点击完成

	# def test_03_addTitle(self):
	# 	self.driver.find_element_by_id("cover_title").send_keys("test_03_addTitle: %s" % self.random_str(46))
	# 	self.driver.back()

	# def test_04_editBody(self):
	# 	text = self.readFile("text.txt")
	# 	self.driver.find_element_by_name(u"正文").send_keys(text)
	# 	self.driver.back()


	# # def test_06_addImageToLib(self):
	# # 	try:
	# # 		self.driver.find_element_by_id("note_image").click()
	# # 		time.sleep(5)
	# # 		self.driver.find_element_by_id("note_image_source").click()
	# # 	except:
	# # 		self.fail("Cannot add image to image library.")

	# # def test_07_setImageInArticleAsCover(self):
	# # 	while True:
	# # 		try:
	# # 			self.driver.find_element_by_id("cover_add").click()
	# # 			break
	# # 		except:
	# # 			TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=200).wait(1000).release().perform()
	# # 	self.driver.find_element_by_id("act_pp_cover").click()
	# # 	j = random.randint(1,self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[","]/android.widget.ImageView[1]"))
	# # 	print "The number %d image is selected as cover."% j
	# # 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(j)+"]/android.widget.ImageView[1]").click()
	# # 	self.driver.find_element_by_id("act_crop_finish").click()#剪切页面点击完成


	# def test_05_addImage(self):
	# 	self.driver.find_element_by_id("act_editor_album").click()
	# 	#选择相册
	# 	self.driver.find_element_by_id("album_name").click()
	# 	time.sleep(2)
	# 	album_num = self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[","]")
	# 	album_index = random.randint(1,album_num)
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout["+str(album_index)+"]").click()
	# 	print "The number %d album is selected."% album_index
	# 	#选择图片
	# 	if album_index==1:#如果相册为“全部相片”，应考虑第一位为相机
	# 		image_num = self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[","]")
	# 		if image_num < 11:
	# 			for i in range(2,image_num+1):
	# 				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.ImageView[1]").click()
	# 		else:
	# 			for j in random.sample(range(2,image_num+1),9):
	# 				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(j)+"]/android.widget.ImageView[1]").click()
	# 	else:
	# 		image_num = self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[","]")
	# 		if image_num < 9:
	# 			for p in range(1,image_num+1):
	# 				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(p)+"]/android.widget.ImageView[1]").click()
	# 		else:
	# 			for q in random.sample(range(1,image_num+1),9):
	# 				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(q)+"]/android.widget.ImageView[1]").click()
	# 	self.driver.find_element_by_id("act_photo_finish").click()#选择完成		

	def test_07_addCoverFromCoverLib(self):
		self.driver.find_element_by_id("edit").click()
		while True:
			try:
				self.driver.find_element_by_id("cover_add").click()
				break
			except:
				try:
					self.driver.find_element_by_id("cover_image").click()
					break
				except:
					TouchAction(self.driver).press(x=500,y=300).move_to(x=0,y=900).wait(1000).release().perform()
		self.driver.find_element_by_id("act_pp_cover").click()
		try:
			self.driver.find_element_by_name(u"封面库")
		except:
			self.driver.find_element_by_id("act_back").click()
			self.skipTest("There's no image in cover library.")
		self.driver.find_element_by_id("albumPreview").click()
		self.driver.find_element_by_id("act_crop_finish").click()

	def test_08_addImageDescription(self):
		while True:
			try:
				self.driver.find_element_by_id("note_image").click()
				time.sleep(2)
				self.driver.find_element_by_id("note_image_edit_description").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-500).wait(1000).release().perform()
			time.sleep(2)
		self.driver.find_element_by_id("note_image_description").send_keys("test_08_addImageDescription: %s \n" % self.random_str(40))
		self.driver.find_element_by_id("note_image").click()

	def test_09_cropImage(self):
		while True:
			try:
				self.driver.find_element_by_id("note_image").click()
				time.sleep(3)
				self.driver.find_element_by_id("note_image_crop").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-500).wait(1000).release().perform()
		cropStyle1 = random.randint(1,5)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout["+str(cropStyle1)+"]").click()
		self.driver.find_element_by_id("act_crop_reset").click()
		cropStyle2 = random.randint(1,5)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout["+str(cropStyle2)+"]").click()
		self.driver.find_element_by_id("act_crop_cancel").click()
		self.driver.find_element_by_id("note_image").click()
		self.driver.find_element_by_id("note_image_crop").click()
		cropStyle3 = random.randint(1,5)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout["+str(cropStyle3)+"]").click()
		self.driver.find_element_by_id("act_crop_finish").click()

	def test_10_deleteImage(self):
		while True:
			try:
				self.driver.find_element_by_id("note_image").click()
				time.sleep(3)
				self.driver.find_element_by_id("note_image_del").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-500).wait(1000).release().perform()
		self.driver.find_element_by_id("buttonDefaultNegative").click()
		self.driver.find_element_by_id("note_image").click()
		self.driver.find_element_by_id("note_image_del").click()
		self.driver.find_element_by_id("buttonDefaultPositive").click()

	def test_11_addMaxNumOfImages(self):
		self.driver.find_element_by_id("act_editor_album").click()
		self.driver.find_element_by_id("album_name").click()
		self.driver.find_element_by_name(u"全部图片").click()	
		for j in range(1,5):
			for i in random.sample(range(2,16),9):
				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.ImageView[1]").click()
			self.driver.find_element_by_id("act_photo_finish").click()
			self.driver.find_element_by_id("act_editor_album").click()
			try:
				self.driver.find_element_by_id("album_name")
			except:
				print "Cannot add image any more."
				break	




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EditImage)
    unittest.TextTestRunner(verbosity=2).run(suite)