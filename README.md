# 1 Title: TCG Player Card Price Data Tool 

by John Sileo 

## 2 Description: 

There are two parts to this program. The first part connects to the TCG Player API, and retrieves prices of cards in one specific set of “Magic: The Gathering”, and stores them into a text file along with the date. The second part displays the prices according to their date. Prices of cards fluctuate much like stocks in the stock market. This price data can be used to figure out how price data will move in the future. 

## 3 Installation: 

In order to install this program, you need python 3, and the requests and pygame libraries for python. 

Command to download pygame:

<code> python3 -m pip install -U pygame --user </code>

Command to download requests:

<code> python -m pip install requests </code>

You also need an API developer key from TCGplayer.com to retrieve data from their API. The link for that is [here:](https://docs.tcgplayer.com/docs/getting-started). 


### 3.1 Price Finder Inputs: 

The first two inputs are ‘private_key’ and ‘public_key’. These are both given to you by TCGPlayer when you apply to be a developer. These two inputs are a requirement to receive a token, which is the third input. Copy and paste the token you receive from the API into the ‘token’ variable. The fourth variable is the set that you want to get price of. Note that the words in this field are case and punctuation sensitive. The last variable is the variable ‘write_to’. This is just the text file where the prices are going to be written. 

### 3.2 Price Display Input: 

The only input here is the variable ‘open_file’, which simply is the file you want to open. 

## 4 How the program works 

### 4.1 API Call Section: 

The first thing the program does is find the product numbers of the cards I want to find. In this code, the program first searches the set “Innistrad: Crimson Vow” for rares and mythic rares and get all of their product IDs for later use. After finding the product IDs, the program searches for the market prices and card names of all of those cards and adds them to their respective lists. The program will then omit any cards that are less than $2. This is because cards that are valued at less than $2 are just not very interesting or useful for this data. Finally, the date/time, the list of product names, and list of card prices are written to a text file.  


### 4.2 Display Section:

For each card in the data, the program will show a card name with a price next to it. Using the buttons, you can go back to different dates of cards and see the differences in price. 


### 4.3 Text File:

If you look at the example “crimson_vow.txt”, you will see an example of the data that is made by the program. Each item is separated by a “@” character, the reason for this is that “Magic: The Gathering” cards sometimes have commas or periods in their name which will throw off your data. The solution was to use a character to separate items that will never be used in a name of a card.


## 5 Why I used the technologies I used 

I really wanted to use excel for this program. The problem was, that I did not have excel easily accessible so I made due with using a text file to store data and pygame to display the data. I used pygame because I was very familiar with it from a previous project and it was very easy to use. I used the TCG player API because a bunch of friends that are software developers told me that I should make a project that uses and connects to an API. TCG Player’s API made sense to try out because I use the website frequently and they allowed me a key to make this program. They also had a nice walkthrough on how to get data from their API and a discord that you can ask questions on. Shoutout to user ‘CptSpaceToaster’ on the discord for helping me out with this project. 

## 6 Screenshots 

6.1 Prices of cards from 2/21/22 

6.2 Price of cards from 12/27/21 

