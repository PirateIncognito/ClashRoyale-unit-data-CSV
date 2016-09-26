
from BeautifulSoup import BeautifulSoup
import requests
import sys

def table2csv(html_txt, card_name):
   csvs = []
   soup = BeautifulSoup(html_txt)
   tables = soup.findAll('table')

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
    
print "\n" * 100 #Clear Python Shell buffer

url = "http://clashroyale.wikia.com/wiki/"

troops = [
    "Knight",
    "Giant",
    "Bomber",
    "Archers",
    "Musketeer",
    "Mini P.E.K.K.A.",
    "Baby Dragon",
    "Prince",
    "Witch",
    "Skeleton Army",
    "Spear Goblins",
    "Goblins",
    "Valkyrie",
    "Skeletons",
    "Minions",
    "Giant Skeleton",
    "Balloon",
    "Barbarians",
    "Minion Horde",
    "Hog Rider",
    "P.E.K.K.A.",
    "Inferno Dragon",
    "Lava Hound",
    "Fire Spirits",
    "Wizard",
    "Ice Wizard",
    "Golem",
    "Sparky",
    "Miner",
    "Royal Giant",
    "Mega Minion",
    "Three Musketeers",
    "Dark Prince",
    "Guards",
    "Princess",
    "Ice Spirit",
    "Bowler",
    "Lumberjack"
    ]


spells = [
    "Arrows",
    "Fireball",
    "Lightning",
    "Goblin Barrel",
    #"Rage",
    "Rocket",
    #"Freeze",
    "Zap",
    #"Mirror",
    "Poison",
    "The Log",
    ]

buildings = [
    "Goblin Hut",
    "Tombstone",
    "Bomb Tower",
    "Cannon",
    "Barbarian Hut",
    "X-Bow",
    "Tesla",
    "Inferno Tower",
    "Furnace",
    "Mortar",
    "Elixir Collector"
    ]

def get_card_info(card):
    print "Getting " + card

    s = url + card.replace(" ","_") #Replace spaces with _ for valid URL
    r = requests.get(s)
    if r.status_code != requests.codes.ok: #If page 404 not found, terminate program
        print s
        r.raise_for_status()
        sys.exit()
    soup = BeautifulSoup(r.content)    
    tua = soup.find('table', id='unit-attributes-table')
    tua = table2csv(str(tua), card)
    #tua = tua.split('\n')[0] + '\n' #Only keep the header line. This was used for testing only to compare the difference in headers between all the units. They aren't uniform.
    print tua
    text_file = open("C:\\tua.txt", "a")
    text_file.write("%s" % tua)
    text_file.close()

    tus = soup.find('table', id='unit-statistics-table')
    tus = table2csv(str(tus), card)
    #tus = tus.split('\n')[0] + '\n' #Only keep the header line. This was used for testing only to compare the difference in headers between all the units. They aren't uniform.
    print tus
    text_file = open("C:\\tus.txt", "a")
    text_file.write("%s" % tus)
    text_file.close()

    #soup.find('table', id='unit-attributes-table').prettify() #testing
    #[img.decompose() for img in soup.findAll('img')] #Remove all <img> tags
    #[a.decompose() for a in soup.findAll('a')] #Remove all <a> tags; disabled because it removed table values

    #s = tua.split('\n')[1] #Only keep the 2nd line
    #s = s.rstrip(',') #Remove the last comma
    #s = s.split(',')[1:len(s)] #Remove the card name from the first element in the list
    #s = ','.join(s)
    #print s

#Initialize files
text_file = open("C:\\tua.txt", "w") 
text_file.close()
text_file = open("C:\\tus.txt", "w")
text_file.close()

#testing purposes
#for card in troops[0:2]:
#    get_card_info(card)
#sys.exit()

for card in troops:
    get_card_info(card)

for card in spells:
    get_card_info(card)

for card in buildings:
    get_card_info(card)

print "Done"
