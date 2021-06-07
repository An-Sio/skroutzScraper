# Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import random
import xlsxwriter

def scraper(key):
    # change path accordingly (keep double slashes)
    PATH = "C:\\Users\\Whatever\\Downloads\\chromedriver.exe"

    # choose chrome as your webdriver and give the path it is installed as input
    driver = webdriver.Chrome(PATH)

    # choose the site you wish to open and navigate
    driver.get("https://www.skroutz.gr/")

    # print the opened tab's name
    print(driver.title)

    # select keyphrase to search products
    search = driver.find_element_by_name("keyphrase")

    # type selected keyphrase to search box
    search.send_keys("plynthrio")

    # hit enter to search
    search.send_keys(Keys.RETURN)

    # wait until categories_show element id appears
    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "categories_show")))

        # find search results and
        results = main.find_elements_by_class_name("sku-link")

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(key + '.xlsx')
        worksheet = workbook.add_worksheet(key)

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # for each result, scrape title, link and characteristics
        for result in results:
            title = result.get_attribute("title")
            print("Scraping for " + title + "...")

            link = result.get_attribute("href")
            print(link)
            print()

            # write in worksheet
            worksheet.write(row*2, col, "Description")
            worksheet.write(row*2+1, col, title)

            col += 1
            worksheet.write(row*2, col, "Link")
            worksheet.write(row*2+1, col, link)

            # get link of each result to start scraping characteristics
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            dts = soup.find_all("dt")
            dds = soup.find_all("dd")

            for element in range(len(dts)):
                col += 1
                worksheet.write(row*2, col, dts[element].text.strip())
                worksheet.write(row*2+1, col, dds[element].text.strip())

            # wait random seconds in order to avoid getting ip banned
            time.sleep(random.randint(3, 7))
            row += 1
            col = 0

    # When finished all processes, close the browser window
    finally:
        driver.quit()

    workbook.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome. This is a scraping script made by An-Sio: https://github.com/an-sio")
    print("The script automates the collection of the characteristics of all washing machines sold on the greek site Skroutz (https://www.skroutz.gr/), then saves the output in an .xlsx file.")
    print()

    key = input("Enter name of the xlsx file you want to be created: ")

    # Make sure user hasn't accidentally hit the enter button with no name filled in
    if key == "":
        key = "plynthrio"

    scraper(key)
