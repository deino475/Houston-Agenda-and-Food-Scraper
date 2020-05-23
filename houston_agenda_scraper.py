import requests
from bs4 import BeautifulSoup
import json

class HoustonAgendaScraper:
	def __init__(self):
		self.agenda_items = []
		self.base_url = "https://houston.novusagenda.com/agendapublic/MeetingView.aspx?MeetingID={}&doctype=Agenda"

	def get_agenda_date(self, website_text):
		list_of_months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		soup = BeautifulSoup(website_text, "html.parser")
		for span in soup.find_all("span"):
			for month in list_of_months:
				if span.get_text().find(month) >= 0:
					return span.get_text()
		return "No Date Found"

	def get_agenda_items(self, website_text):
		soup = BeautifulSoup(website_text, "html.parser")
		for table_rows in soup.find_all("tr"):
			table_data_items = table_rows.find_all('td')
			if len(table_data_items) >= 3:
				if table_data_items[0].get_text() == "VIDEO":
					agenda_item_text = table_data_items[2].get_text()
					self.agenda_items.append(agenda_item_text.encode('utf-8'))
	
	def scrape_url(self, meeting_id):
		#GET WEBSITE HTML
		r = requests.get(self.base_url.format(meeting_id))
		page_html = r.text

		#CHECK TO SEE IF AGENDA 
		if page_html.find("This Agenda is not available.") >= 0:
			print("No agenda available")
			return

		agenda_date = self.get_agenda_date(page_html)
		self.get_agenda_items(page_html)

		print(agenda_date)
		print(str(self.agenda_items))

		with file("agenda_items.json","w") as file_to_write:
			json.dump(file_to_write, self.agenda_items)
		

has = HoustonAgendaScraper()
has.scrape_url("389")
print(has.agenda_items)
