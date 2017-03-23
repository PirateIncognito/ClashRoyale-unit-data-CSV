# cr-get-unit-data.py
# 
# The purpose of this program is to generate a CSV file of Clash Royale unit stats & attributues.
# The data is scraped from a the internet and and output as a CSV file.
# The CSV file can then be fed into another program (not yet created) which can output useful
# information like unit efficiency (HP/elixir, DPS/elixir)
# This program will scraped 2 websites
# 1) http://clashroyaledeckbuilder.com/cards - this website is scraped to build the card list
# 2) http://clashroyale.wikia.com/wiki/ - this website is scraped to build the unit stats
# 
# This program was written in Python 2.7 and uses 2 custom libraries
# 1) BeautifulSoup v3 - HTML parser - https://www.crummy.com/software/BeautifulSoup/
# 2) requests v2 - HTTP protocol - docs.python-requests.org
#
# Functions:
# 1. get_card_data() -
#    Using lists of cards scrapes http://clashroyale.wikia.com/wiki/ for card data
#    This function finds the relevant HTML data and sends it to table2csv
#
# 2. table2csv - convert HTML table to CSV
#
# main: builds the lists of cards (troops, spells, buildings) by scraping http://clashroyaledeckbuilder.com/cards

############################################################################################

try:
    from bs4 import BeautifulSoup #BeautifulSoup v4
except ImportError:
    from BeautifulSoup import BeautifulSoup #BeautifulSoup v3
    
import requests #for URL requests
import sys

############################################################################################

#Converts HTML <table> to CSV format
#Inputs:
#   html_text (string): HTML <table> data containing stats OR attributes
#   card_name (string): card name
#Process:
#   Create beutifulsoup object 
#   Find relevant tables
#   Send table to table2csv

def table2csv(html_txt, card_name):
   csvs = []
   soup = BeautifulSoup(html_txt)
   tables = soup.findAll('table') #This line could be cleaned up, since we're already only passing a table. No need for findAll()
  
   for table in tables:
       csv = ''
       rows = table.findAll('tr')
       row_spans = []
       do_ident = False
       
       for tr in rows:
           cols = tr.findAll(['th','td'])
           csv += '"{text}"'.format(text=card_name)+ ','

           for cell in cols:
               colspan = int(cell.get('colspan',1))
               rowspan = int(cell.get('rowspan',1))

               if do_ident:
                   do_ident = False
                   csv += ','*(len(row_spans))

               if rowspan > 1: row_spans.append(rowspan)

               csv += '"{text}"'.format(text=cell.text) + ','*(colspan)

           if row_spans:
               for i in xrange(len(row_spans)-1,-1,-1):
                   row_spans[i] -= 1
                   if row_spans[i] < 1: row_spans.pop()

           do_ident = True if row_spans else False

           csv += '\n'

       csvs.append(csv)
       #print csv

   return '\n\n'.join(csvs)

############################################################################################

#Gets Clash Royale unit data from CR Wiki via HTTP
#Input: card (string): card name
#Output: csvs (string): CSV formatted string written to text file

def get_card_info(card):
    print "Getting " + card
    url = "http://clashroyale.wikia.com/wiki/"
    url += card.replace(" ","_") #Replace spaces with _ for valid URL (does not work for X_bow)
    r = requests.get(url)
    if r.status_code != requests.codes.ok: #If page 404 not found, terminate program
        print url
        r.raise_for_status()
        sys.exit()
    soup = BeautifulSoup(r.content)
    
    #Get unit attritubtes (these do not change with unit level: speed, range, elixir cost, etc)
    tua = soup.find('table', id='unit-attributes-table') #tua = Temp Unit Attribute
    tua = table2csv(str(tua), card)
    #tua = tua.split('\n')[0] + '\n' #Only keep the header line. This was used for testing only to compare the difference in headers between all the units. They aren't uniform.
    print tua
    #Append our data in CSV format to text file.
    text_file = open('cr-unit-attributes.csv', 'a')
    text_file.write("%s" % tua)
    text_file.close()

    #Get unit stats (these change with unit level: HP, DPS, etc)
    tus = soup.find('table', id='unit-statistics-table') #tus = Temp Unit Statistic
    tus = table2csv(str(tus), card)
    tus_header = tus.split('\n')[0] + '\n' #Only keep the header line. This was used for testing only to compare the difference in headers between all the units. They aren't uniform.
    #Append our data in CSV format to text file.
    print tus
    text_file = open("cr-unit-satistics.csv", "a")
    text_file.write("%s" % tus)
    text_file.close()
    text_file = open("cr-unit-satistics-header.csv", "a")
    text_file.write("%s" % tus_header)
    text_file.close()
    
############################################################################################

# Main func
# Build card list by scraping names from internet

print "\n" * 100 #Clear Python Shell buffer

#Declare vars
troops = []
spells = []
buildings = []

url = "http://clashroyaledeckbuilder.com/cards" # This URL will build the card list
r = requests.get(url)
if r.status_code != requests.codes.ok: #If page 404 not found, terminate program
    print url
    r.raise_for_status()
    sys.exit()

soup = BeautifulSoup(r.content)

s = soup.findAll('div', 'cardBackground')
for i in s:
    name = i.find('div','name').text
    type = i.find('div','vitals').findAll('div')[1].find('span').text
    if(type == 'Troop'):
        troops.append(name)
    elif(type == 'Spell'):
        spells.append(name)
    elif(type == 'Building'):
        if(name == 'X Bow'):#This card does not translate directly between website. In downstream function we replace as spaces with underscore. This needs a dash
           name = 'X-Bow'
        buildings.append(name)
        
troops.sort()
spells.sort()
buildings.sort()
#Card list is now complete, we will submit these lists to the get_card_info() func below

#Print card lists
for i in troops:
    print i
print '\n'
for i in spells:
    print i
print '\n'
for i in buildings:
    print i
    
#Initialize files
text_file = open("cr-unit-attributes.csv", "w") 
text_file.close()
text_file = open("cr-unit-satistics.csv", "w")
text_file.close()

#Meat n Potatoes
#Scroll through each list (troops, spells, buildings) and get unit data

###testing purposes: Only runs first 3 Troop cards then quits
##for card in troops[0:2]:
##    get_card_info(card)
##print "Quitting..."
##sys.exit()
###end testing purposes

for card in troops:
    get_card_info(card)

for card in spells:
    get_card_info(card)

for card in buildings:
    get_card_info(card)

print "Done"

#Things to do



#Convert create_card_list to a separate function
#Replace 'Area Damage' with 'Damage'
#Replace 'Damage Per Second' with 'DPS
#Replace &amp; with & (found in Unit attributes: Ground &amp; Air)
#Average Inferno Dragon damage
#Combine Shield+HP
#Remove 'Golem' from 'Golem Damage'
#Combine damamge data from units that split into a single number (i.e. Golem, Lava Hound)
#Confirm the numbers for units with Count >1x are correct (i.e. if the card plays 3 units, do we need to multiply the numbers by 3?)
