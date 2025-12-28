from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

#To rescrape if the site is changed add "view-source:(INSERT URL)" and reexamine html
# ^^ Will eventually go in a rescraping file

# As of 2025-12-28 the current html hierarchy of the factions is as follows:
#                                            <NavColumns2 div>
#                                                 V V V
#                                          <BreakInsideAvoid div>
#                                                 V V V
# <FactionHeader div>Faction Name 1</div> <a href="">Subfaction Name 1</a> <a href="">Subfaction Name 2</a> ...
# <FactionHeader div>Faction Name 2</div> <a href="">Subfaction Name 1</a> <a href="">Subfaction Name 2</a> ...
#                                                  ...
#                                                 </div>
#                                                 </div>

load_dotenv()
raw_init_html = requests.get(os.getenv("SITE_INIT"))
clean_init_html = BeautifulSoup(raw_init_html.text, "lxml")
main_div = clean_init_html.find("div", class_="NavColumns2")
faction_types = main_div.findChildren("div", class_= "BreakInsideAvoid")

#Making a list of all the factions that we will need to scrape with links (currently href)
# to them
factions = []
for faction_type in faction_types:
    subfactions = faction_type.find_all("a", recursive = False)
    faction_name = faction_type.find("div", class_="FactionHeader").get_text()
    for subfaction in subfactions:
        name = subfaction.getText()
        href = subfaction.get("href")
        factions.append({"Faction" : faction_name, "Subfaction" : name, "href" : href})

print(factions)

#Endgoal : list containing every weapon profile for every unit of every faction with ways to identify:
#   - Superfaction
#   - Faction
#   - Model

#Then from each faction page we need to make a list of all model pages to scrape

#Finally we need to scrape each of these pages