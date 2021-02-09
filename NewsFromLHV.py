from urllib.request import urlopen as u_open
from bs4 import BeautifulSoup as Soup


# Function for grabbing news titles from different news pages through LHV site
def news_from_lhv(news_page_name, page_url, pages, textfile):  # pages stands for 20 titles per page starting from the latest
    
    # opening up textfile
    with open(textfile, "w", encoding="UTF-8") as f:
    
        heading = (news_page_name + "\n\n")
        f.write(heading)

        # loop for checking titles on multiple pages
        for page in range(pages):
            if page != 0:
                page_url = page_url[:-1]+str(page)

            # opening up connection, grabbing the page
            url_client = u_open(page_url)
            page_html = url_client.read()
            url_client.close()

            # html parsing
            page_soup = Soup(page_html, "html.parser")

            # grab each title, link and date of publishing on news page
            containers = page_soup.findAll("a", {"class": "title"})
            dates = page_soup.findAll("td", {"class": "date right"})

            for container, date in zip(containers, dates):
                link = container["href"]  # reference for full article
                title = container.text.strip()  # title of article
                date = date.text.strip().split("\r\n   ")
                print(date)
                f.writelines(date)
                news = ("\n", title, "\n", link, "\n\n")
                f.writelines(news)


# variable for the amount of pages scraped
my_pages = 1

# different url-s from LHV site
aripaev_url = "https://fp.lhv.ee/news/aripaevnews/0"
ERR_url = "https://fp.lhv.ee/news/err/0"
rahageenius_url = "https://fp.lhv.ee/news/rahageeniusnews/0"
postimees_url = "https://fp.lhv.ee/news/e24news/0"
arileht_url = "https://fp.lhv.ee/news/delfinews/0"
balti_borsid_url = "https://fp.lhv.ee/news/omx/0"

# Using the functions to extract information
news_from_lhv("Äripäev", aripaev_url, my_pages, "Aripaev.txt")
news_from_lhv("Eesti Rahvus Ringhääling", ERR_url, my_pages, "ERR.txt")
news_from_lhv("Rahageenius", rahageenius_url, my_pages, "Rahageenius.txt")
news_from_lhv("Postimees", postimees_url, my_pages, "Postimees.txt")
news_from_lhv("Ärileht", arileht_url, my_pages, "Arileht.txt")
news_from_lhv("Balti Börsid", balti_borsid_url, my_pages, "Balti_Borsid.txt")
