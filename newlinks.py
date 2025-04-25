import requests  # For sending HTTP requests to websites
from bs4 import BeautifulSoup  # For parsing HTML content
import openpyxl  # For creating and working with Excel files

# First, let’s define the website we want to scrape — Hacker News front page
url = "https://news.ycombinator.com/news"

# Send a request to the site and store the response
response = requests.get(url)

# If something went wrong (like no internet or page not found), this will stop the program with an error
response.raise_for_status()

# Now we parse the page content using BeautifulSoup so we can work with it more easily
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the article titles and their links — they're in <a> tags inside elements with the class "titleline"
articles = soup.select('.titleline > a')

# Grab the text (title) and the link (href) for each article
titles_and_links = [(article.text, article['href']) for article in articles]

# Let’s print what we found, just to see it in the console
for title, link in titles_and_links:
    print(title)
    print(link)
    print()  # Just adding a blank line for better readability

# Now, let’s save this information into an Excel spreadsheet

# Create a new Excel workbook
wb = openpyxl.Workbook()

# Select the default worksheet and give it a name
ws = wb.active
ws.title = "Hacker News Links"

# Add headers to the first row
ws.append(["Title", "URL"])

# Write each title and its corresponding link to a new row
for title, link in titles_and_links:
    ws.append([title, link])

# Finally, save the workbook to a file
wb.save("hacker_news_links.xlsx")

# Let the user know that the data has been saved
print("Data saved to hacker_news_links.xlsx")
