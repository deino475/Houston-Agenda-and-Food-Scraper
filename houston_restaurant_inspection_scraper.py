
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime

class HoustonFoodInspectionScraper:
	def __init__(self):
		self.driver = webdriver.Firefox(executable_path = r"C:\\Users\\Owner\\Desktop\\WebDrivers\\geckodriver.exe")
		self.base_url = "https://houston-tx.healthinspections.us/media/search.cfm"
		self.restaurants_data = []
		self.inspections_data = []
		self.inspection_links = []
		self.month_day_tracker = [31,28,31,30,31,30,31,31,30,31,30,31]

	def make_search(self, year, month, day):
		time.sleep(5)
		start_month = self.driver.find_element_by_name("sd_month")
		for option in start_month.find_elements_by_tag_name("option"):
			print(option.text)
			if option.text == month:
				print("Hello")
				option.click()

		time.sleep(2)

		start_day = self.driver.find_element_by_name("sd_day")
		for option in start_day.find_elements_by_tag_name("option"):
			if option.text == day:
				option.click()

		time.sleep(2)

		start_year = self.driver.find_element_by_name("sd_year")
		for option in start_year.find_elements_by_tag_name("option"):
			if option.text == year:
				option.click()

		time.sleep(2)

		end_month = self.driver.find_element_by_name("ed_month")
		for option in end_month.find_elements_by_tag_name("option"):
			if option.text == month:
				option.click()

		time.sleep(2)

		end_day = self.driver.find_element_by_name("ed_day")
		for option in end_day.find_elements_by_tag_name("option"):
			if option.text == day:
				option.click()

		time.sleep(2)

		end_year = self.driver.find_element_by_name("ed_year")
		for option in end_year.find_elements_by_tag_name("option"):
			if option.text == year:
				option.click()

		time.sleep(2)

		search_button = self.driver.find_element_by_name("Submit")
		search_button.click()
		return

	def run(self):
		self.driver.get(self.base_url)
		self.make_search("2019","January","03")

		today = datetime.today()



hou = HoustonFoodInspectionScraper()
hou.run()
