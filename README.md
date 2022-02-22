1 Title: TCG Player Card Price Data Tracker by John Sileo 

2 Description: There are two parts to this program. The first part connects to the TCG Player API, and retrieves prices of cards in one specific set of “Magic: the Gathering”, and stores them into a text file along with the date. The second part displays the prices according to their date. Prices of cards fluctuate much like stocks in the stock market. This price data can be used to figure out how price data will move in the future. 

3 Installation: In order to install this program, you need python 3, as well as the community edition of pycharm and the requests library. You also need an API key from TCGplayer.com to retrieve data from their API. You also need a text file to write to which should be made in pycharm.   

3.1 Changing Sets: In the API call part of the program, if you want to change the data to a different set, you would need to change this part of the code:  

"values": ["Innistrad: Crimson Vow"], 

to the exact name of the set that you want. The data will be stored to a text file that is named in this line of code:  

f = open('crimson_vow.txt', 'a') 

If you change the set you are searching, be sure to rename this line of code so that you do not mix up your data. You also need to change the file that the display section reads from which is this line of code:  

f= open('crimson_vow.txt', 'r') 

 
For clarification, the only words that change when you change the set are “Innistrad: Crimson Vow” and “crimson_vow” in this example (keeping the quotation marks in the code and all other characters). The last thing that needs to be done is filtering exceptions. When the names of cards are added to a list, they are added to a list as a string with a comma. A bug will occur if a name of a card has a comma inside of it, therefore, in this line of code:  

if list2[x][y]=='Umbris' or  list2[x][y]=='Toxrill' or list2[x][y]=='Olivia'or list2[x][y]=='Chandra'or list2[x][y]=='Kaya' or list2[x][y]=='Thalia':

you would need to change this list to represent the set you are changing. You would have to go through the set you are changing to and add each rare and mythic rare that has a comma inside its name. Luckily, there are not many rares and mythic rares that have a comma in their name in each set. Unfortunately, there is no other way around this problem for this project. 

4 How the program works 

4.1 API Call Section: The first thing the program does is find the product numbers of the cards I want to find. In this code, the program first searches the set “Innistrad: Crimson Vow” for rares and mythic rares and get all of their product IDs for later use. After finding the product IDs, the program searches for the market prices and card names of all of those cards and adds them to their respective lists. The program will then omit any cards that are less than $2. This is because cards that are valued at less than $2 are just not very interesting or useful for this data. Finally, the date/time, the list of product names, and list of card prices are written to a text file.  

4.2 Display Section: For each card in the data, the program will show a card name with a price next to it. Using the buttons, you can go back to different dates of cards and see the differences in price. 

5 Why I used the technologies I used 

I really wanted to use excel for this program. The problem was, that I did not have excel easily accessible so I made due with using a text file to store data and pygame to display the data. I used pygame because I was very familiar with it from a previous project and it was very easy to use. I used the TCG player API because a bunch of friends that are software developers told me that I should make a project that uses and connects to an API. TCG Player’s API made sense to try out because I use the website frequently and they allowed me a key to make this program. They also had a nice walkthrough on how to get data from their API and a discord that you can ask questions on. Shoutout to user ‘CptSpaceToaster’ on the discord for helping me out with this project. 

6 Screenshots 

6.1 Prices of cards from 2/21/22 

6.2 Price of cards from 12/27/21
