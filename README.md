# ClashRoyale-unit-data-CSV
A Python script for extracting unit data stats from http://clashroyale.wikia.com/ and saving them to CSV

This script was written in Python 2.7 on Windows. It has the C:\ drive location hard coded and must be changed to run on other systems.

This file uses the BeautifulSoup 3 library https://www.crummy.com/software/BeautifulSoup/

Credit goes to this Aviad (http://stackoverflow.com/questions/259091/how-can-i-scrape-an-html-table-to-csv/29276277#29276277)
for providing the code for the Table parse.
http://stackoverflow.com/questions/259091/how-can-i-scrape-an-html-table-to-csv/29276277#29276277

Please use this python for your own uses. The only request I make is: Please share your tools with the community and include a reference to this project.

The output of this program creates two output files. One for unit attributes, and one for statistics (HP, DMG, etc)

An example output is below:

"Knight","Level","Hitpoints","Damage","Damage per second",
"Knight","1","660","75","68",

"Knight","2","726","82","74",

"Knight","3","798","90","81",

"Knight","4","877","99","90",

"Knight","5","963","109","99",

"Knight","6","1,056","120","109",

"Knight","7","1,161","132","120",

"Knight","8","1,273","144","130",

"Knight","9","1,399","159","144",

"Knight","10","1,537","174","158",

"Knight","11","1,689","192","174",

"Knight","12","1,854","210","190",

"Knight","13","2,039","231","210",

-----------------------------------

"Knight","Hit Speed","Speed","Deploy Time","Range","Target","Cost","Count","Type","Rarity",

"Knight","1.1 sec","Medium","1 sec","Melee","Ground","3","x1","Troop","Common",
