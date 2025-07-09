import requests
from bs4 import BeautifulSoup
import csv

url = "https://toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    with open('toscrape_full_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Tag', 'Content'])

        for tag in soup.find_all(['h1', 'h2', 'h3']):
            writer.writerow(['Heading', tag.name, tag.get_text(strip=True)])

        for p in soup.find_all('p'):
            writer.writerow(['Paragraph', 'p', p.get_text(strip=True)])

        for link in soup.find_all('a', href=True):
            text = link.get_text(strip=True)
            href = link['href']
            writer.writerow(['Link', 'a', f'Text: {text} | URL: {href}'])

        title_tag = soup.find('title')
        if title_tag:
            writer.writerow(['Meta', 'title', title_tag.get_text(strip=True)])

        description_tag = soup.find('meta', attrs={'name': 'description'})
        if description_tag and description_tag.get('content'):
            writer.writerow(['Meta', 'description', description_tag['content']])

    print(" Data scraped and saved to 'toscrape_full_data.csv' successfully.")

except requests.exceptions.RequestException as e:
    print(f" Request failed: {e}")
except Exception as e:
    print(f" An error occurred: {e}")
