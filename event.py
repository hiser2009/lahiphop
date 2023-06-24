import pytest
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import datetime
import pytz





app = Flask(__name__)

# Send a GET request to the website
# url = "https://lahiphopevents.com/calendar/"
# response = requests.get(url)

# Use Beautiful Soup to parse the HTML content of the page
# soup = BeautifulSoup(response.content, "html.parser")

# Find all the events on the page
# events = soup.find_all("div", class_="tribe-events-calendar-list__event-description tribe-common-b2 tribe-common-a11y-hidden")
# images = soup.find_all("div", class_="tribe-events-calendar-list__event-featured-image-wrapper tribe-common-g-col")

# for event in events:
# #   Get the event title

#     for p_tag in event.find_all('p'):
#         print(p_tag.text)
#         print('<>'*79)
#         print()
@app.route('/')
def index():
    # URL of the web page to scrape
    
    # render the template with the object list
    # return render_template('index.html' , events=events)
    url = "https://lahiphopevents.com/calendar/"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    events = soup.find_all("div", class_="tribe-events-calendar-list__event-description tribe-common-b2 tribe-common-a11y-hidden")
    utc_dt = datetime.datetime.utcnow()
    pst_timezone = pytz.timezone('US/Pacific')
    pst_dt=utc_dt.replace(tzinfo=pytz.utc).astimezone(pst_timezone)
    return render_template('index.html' , events=events , pst_formatted=pst_dt.strftime('%Y-%m-%d %H:%M:%S') )

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')