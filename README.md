# ClashRoyale-unit-data-CSV
A Python script for extracting unit data stats from http://clashroyale.wikia.com/ and saving them to CSV

The script is free to use for everyone. The only request I make is:  <br />
Please share your tools with the community and include a reference to this project. <br />

This script was written in Python 2.7 on Windows. It has the C:\ drive location hard coded and must be changed to run on other systems.

Dependencies: <br />
<a href="https://www.crummy.com/software/BeautifulSoup">BeautifulSoup 3 library</a> <br />
<a href="http://docs.python-requests.org/en/master">Requests: HTTP for Humans v2.11.1</a>

Credit goes to <a href="http://stackoverflow.com/questions/259091/how-can-i-scrape-an-html-table-to-csv/29276277#29276277">Aviad</a>
for providing the code for the <a href="http://stackoverflow.com/questions/259091/how-can-i-scrape-an-html-table-to-csv/29276277#29276277">Table parse</a>. <br />




The scipt creates two output files. One for unit attributes, and one for statistics (HP, DMG, etc)

An example output is below:

"Knight","Level","Hitpoints","Damage","Damage per second", <br />
"Knight","1","660","75","68", <br />
"Knight","2","726","82","74", <br />
"Knight","3","798","90","81", <br />
"Knight","4","877","99","90", <br />
"Knight","5","963","109","99", <br />
"Knight","6","1,056","120","109", <br />
"Knight","7","1,161","132","120", <br />
"Knight","8","1,273","144","130", <br />
"Knight","9","1,399","159","144", <br />
"Knight","10","1,537","174","158", <br />
"Knight","11","1,689","192","174", <br />
"Knight","12","1,854","210","190", <br />
"Knight","13","2,039","231","210", <br />
-----------------------------------

"Knight","Hit Speed","Speed","Deploy Time","Range","Target","Cost","Count","Type","Rarity", <br />
"Knight","1.1 sec","Medium","1 sec","Melee","Ground","3","x1","Troop","Common",
