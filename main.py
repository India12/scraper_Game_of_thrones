from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Game_of_Thrones#cite_note-S1avgS2ratings-276"
response = urlopen(url).read()
wiki = BeautifulSoup(response)

viewer_numbers_file = open("viewer_numbers.csv", "w")
viewer_numbers_file.write("The number of viewers of first-airing episodes of Game of Thrones in the US is: \n\n")

print "The number of viewers of first-airing episodes of Game of Thrones in the US is:  \n"

table = wiki.findAll("table", attrs={"class": "wikitable"})

all_views = 0

for table_row in table[1].findAll("tr"):
    for table_data in table_row.findAll("td"):
        all_table_data = table_data.string
        odvec = "N/A"
        if all_table_data is not None and all_table_data != odvec:
            views = float(all_table_data)
            all_views += views

print str(all_views) + " millions."

viewer_numbers_file.write(str(all_views) + " millions. \n")

viewer_numbers_file.close()
