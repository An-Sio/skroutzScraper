This is a scraping script made by An-Sio: https://github.com/an-sio
The script automates the collection of the characteristics of all washing machines sold on the greek site Skroutz (https://www.skroutz.gr/), then saves the output in an .xlsx file.

The script uses both selenium module and a combination of requests + BeautifulSoup modules, in order to showcase familiarity with all of these modules.

The script waits for a random small amount of time between scrapes, in order to avoid being detected as a bot and complete the scraping process smoothly.

Although the script is used for washing machines only, you can change it in order to look for anything if you change line 30: search.send_keys("plynthrio") to search.send_keys(key), where key is the name used to save the excel output file.

Thank you!