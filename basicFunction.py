#coding=utf-8
import random, string, time
from appium import webdriver

class BasicFunctions():
	def random_str(self,length):
		chars = string.ascii_letters+string.digits+string.punctuation
		s = [random.choice(chars) for i in range(length)]
		return ''.join(s)

	def B2Q(self,bstring): #半角转全角
		qstring = []
		for bchar in bstring:  
		    inside_code=ord(bchar)  
		    if inside_code<0x0020 or inside_code>0x7e: #不是半角字符就返回原来的字符  
		        pass
		    elif inside_code==0x0020: #除了空格其他的全角半角的公式为:半角=全角-0xfee0  
		        inside_code=0x3000  
		    else:  
		        inside_code+=0xfee0
		    qchar = unichr(inside_code)
		    qstring.append(qchar)
		return ''.join(qstring)

	# def readFile(self,filename):
	# 	f = open(filename,"r")
	# 	lines = []
	# 	while True:
	# 		line = f.readline().decode("utf8")
	# 		if not line: break
	# 		lines.append(line)
	# 	f.close()
	# 	return "".join(lines).encode('ascii','ignore')

	def readFile(self,filename):
		f = open(filename,"r")
		str = f.read().decode("utf8")
		f.close()
		return str.encode('ascii','ignore')

	def getElementNum(self,prefix_xpath,postfix_xpath):
		i = 1
		while True:
			xpath = prefix_xpath+str(i)+postfix_xpath
			try:
				self.driver.find_element_by_xpath(xpath)
			except:
				break
			i+=1
		return i-1

	def login(self):
		self.driver.find_element_by_id("act_login_btn").click()
		time.sleep(5)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]").send_keys("jhwhale@163.com")
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.widget.EditText[2]").send_keys("testweico")
		self.driver.find_element_by_name(u"登录").click()

	def getScreenWidth(self):
		size = self.driver.get_window_size()
		return size['width']

	def getScreenHeight(self):
		size = self.driver.get_window_size()
		return size['height']

	def createArticles(self, articleAccount = 10):
		articleNum = 0
		while articleNum<articleAccount:
			#添加封面
			self.driver.find_element_by_id("cover_add").click()
			#获取图片数
			j = random.randint(1,self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[","]/android.widget.ImageView[1]"))

			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(j)+"]/android.widget.ImageView[1]").click()
		 	self.driver.find_element_by_id("act_crop_finish").click()#剪切页面点击完成

			#添加标题
			self.driver.find_element_by_id("cover_title").send_keys("No.%s" % articleNum)
			#self.driver.back()
			time.sleep(2)
			
			#添加正文
			self.driver.find_element_by_name(u"正文").send_keys(self.random_str(100))
			self.driver.find_element_by_id("act_back").click()

			articleNum+=1
			self.driver.find_element_by_id("edit").click()
