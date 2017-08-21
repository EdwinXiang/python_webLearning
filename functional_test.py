#! /usr/bin/en python3
#coding:utf-8
from selenium import webdriver
import unittest

class NewVisitTest(unittest.TestCase):
	"""docstring for NewVisitTest"""
	def setUp(self):
		self.browser = webdriver.Firefox()
		# 隐士等待3秒
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retreve(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('welcome',self.browser.title)
		self.fail('finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')