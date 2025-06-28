from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import time

def scrape_google_local(page_content, csv_writer):
    soup = BeautifulSoup(page_content, 'html.parser')
    results = soup.find_all('div', class_='VkpGBb')

    for result in results:
        name_elem = result.find('a', class_='vwVdIc wzN8Ac rllt__link a-no-hover-decoration')
        name_elem = name_elem.find('span', class_='OSrXXb') if name_elem else None
        name = name_elem.text.strip() if name_elem else "N/A"

        rating_elem = result.find('div', class_='rllt__details')
        rating_elem = rating_elem.find('span', class_='yi40Hd YrbPuc') if rating_elem else None
        rating = rating_elem.text.strip() if rating_elem else "N/A"

        address_elem = result.find('div', class_='rllt__details')
        address = address_elem.text.strip() if address_elem else "N/A"

        website_elem = result.find('a', class_='yYlJEf Q7PwXb L48Cpd brKmxb')
        website = website_elem['href'] if website_elem and website_elem.has_attr('href') else "N/A"

        map_elem = result.find('a', class_='yYlJEf Q7PwXb VDgVie brKmxb')
        map = map_elem['href'] if map_elem and map_elem.has_attr('href') else "N/A"

        csv_writer.writerow([name, rating, address, website, map])
        print(f"Name: {name}")
        print(f"Rating: {rating}")
        print(f"Address: {address}")
        print(f"Website: {website}")
        print(f"Map: {map}")
        print("-" * 40)

def main():
    with open('GoogleLocal_data.csv', mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Rating', 'Address', 'Website', 'Map'])

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            url = "https://www.google.com/search?q=psychologist+in+ludhiana&tbm=lcl"
            page.goto(url)
            page.wait_for_timeout(4000)

            while True:
                print("Scraping current page...")
                scrape_google_local(page.content(), csv_writer)
                try:
                    next_button = page.locator('a.oeN89d')
                    if next_button.is_visible():
                        next_button.click()
                        page.wait_for_timeout(4000)
                    else:
                        print("No more pages.")
                        break
                except:
                    print("Next button not found. Stopping.")
                    break

            browser.close()

if __name__ == "__main__":
    main()
