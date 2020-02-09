
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd

def scrape():
    mars_results = {}

    url = 'https://mars.nasa.gov/news/'



    response = requests.get(url)




    soup = bs(response.text, 'html.parser')






    title = soup.find('div', class_="content_title").text
    p_text = soup.find('div', class_="rollover_description_inner").text

    print(title)
    print(p_text)
    mars_results['title'] = title
    mars_results['p_text'] = p_text

    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    get_ipython().system('which chromedriver')
    executable_path = {'executable_path': '/Users/mc/CU-NYC-DATA-PT-10-2019-U-C-master2/Homework/12-Web-Scraping-and-Document-Databases/web-scraping-challenge/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)



    html = browser.html
    soup = bs(html, 'html.parser')
    image_url = soup.find('article')['style']

    image_url
    image_url_slice = image_url[23:-3]


    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url= main_url+image_url_slice
    featured_image_url

    mars_results['featured_image_url'] = featured_image_ur

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    response_w = requests.get(weather_url)
    soup2 = bs(response_w.text, 'html.parser')






    tweets = soup2.find("div", class_="stream").find("ol").find_all("li", class_="js-stream-item")
    for tweet in tweets:
        tweet_text = tweet.find("div", class_="js-tweet-text-container").text
        if "Sol " in tweet_text:
            mars_weather = tweet_text.strip()
            break

    weather = mars_weather[81:145]
    weather




    fact_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(fact_url)
    tables



    fact_df = tables[0]
    fact_df.columns=['Fact','Value']
    fact_df["Fact"] = fact_df["Fact"].str[:-1]
    fact_df

    mars_results['fact_df'] = fact_df


    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    html_hemispheres = browser.html

    soup3 = bs(html_hemispheres, 'html.parser')

    items = soup3.find_all('div', class_='item')

    hemisphere_image_urls = []

    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    for i in items: 

        title = i.find('h3').text
        
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        
        browser.visit(hemispheres_main_url + partial_img_url)
        
        partial_img_html = browser.html
        
        soup4 = bs( partial_img_html, 'html.parser')
        
        img_url = hemispheres_main_url + soup4.find('img', class_='wide-image')['src']
        
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        

    hemisphere_image_urls

    mars_results['hemisphere_image_urls'] =hemisphere_image_urls

    return mars_results
