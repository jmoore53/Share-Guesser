#Gets all the values from nasdaq website and stores them all in csv file
import urllib2

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def scrape_nasdaq():
	with open('namesAndInfo.csv', 'w') as myfile:
		for i in alphabet:
			download_link = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=" + i + "&render=download"
			response = urllib2.urlopen(download_link)
			html = response.read()
			myfile.write(html)
	return 0;

scrape_nasdaq()