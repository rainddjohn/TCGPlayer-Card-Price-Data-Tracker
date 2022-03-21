#user inputs
public_key='Paste Public Key Here'
private_key='Paste Private Key Here'
token='Paste Token Here'
set="Type the exact case sensitive name of the set you want here "
write_to='Type the name of the file you want to save the data to here'

import requests
import datetime

class data():
    cardnames=[]
    normalprices=[]
    foilprices=[]
data=data()

def findcardprices(data,set,token):
    ##this part searches for the productIDs'

    r = requests.post(
        'https://api.tcgplayer.com/v1.39.0/catalog/categories/1/search',
        headers={'Authorization':f"bearer {token}"
        },
        json={
            "sort": "MinPrice DESC",
            "limit": 1000,
            "offset": 0,
            "filters": [
                {
                    "name": "SetName",
                    "values": [f"{set}"]
                },{ "name": "Rarity","values": ["Mythic", "Rare"]}

            ]
        }
    )
    search_response_data = r.json()


    if r.status_code != 200:
        gettoken(public_key,private_key)
        return data

    productIDs=list(search_response_data.values())
    productIDs=productIDs[3]
    backupproductIDs=list(productIDs)


    #this part searches pricing
    backup_productIDs=[]
    if len(productIDs)>250:
        backup_productIDs= productIDs[250:]
        productIDs= productIDs[:250]

    productIDs= ','.join(str(y) for y in productIDs)
    r = requests.get(
        f'https://api.tcgplayer.com/v1.39.0/pricing/product/{productIDs}',
        headers={
            'Authorization': f"bearer {token}"
        }
    )
    search_response_data = r.json()


    ###prices input to lists
    priceresults=list(search_response_data['results'])
    for i in priceresults:
        if i['subTypeName']=='Normal':
            data.normalprices.append(i['marketPrice'])
        if i['subTypeName']=='Foil':
            data.foilprices.append(i['marketPrice'])

    #this part turns productIDs into names
    r = requests.get(
        f'https://api.tcgplayer.com/v1.39.0/catalog/products/{productIDs}',
        headers={
            'Authorization': f"bearer {token}"
        }
    )
    search_response_data = r.json()
    nameresults=search_response_data['results']
    
    for j in backupproductIDs:
        for i in nameresults:
            if j==i['productId']:
                data.cardnames.append(i['name'])
    return data

def gettoken(public_key,private_key): ## you need this if your token expires
    import requests
    payload = {
        'grant_type': 'client_credentials',
        'client_id': f'{public_key}',
         'client_secret': f'{private_key}',
        }
    r = requests.post('https://api.tcgplayer.com'
             + '/token',
            data=payload,
        )
    token_response_data = r.json()
    print('Paste this into the token input:')
    print(token_response_data['access_token'])

def writetotxt(data,write_to):
    filternames = []
    filterprices = []
    
    # takes out cards we don't want in this list
    for i in range(len(data.cardnames)):
        if data.normalprices[i] is None: 
            continue
            
        if not '(' in data.cardnames[i] and not ' - ' in data.cardnames[i] and int(data.normalprices[i] > 2):
            filternames.append(data.cardnames[i])
            filterprices.append(data.normalprices[i])

    # for i in range(len(cardnames)):print(cardnames[i],foilprices[i])
    for i in range(len(filternames)): 
        print(filternames[i], filterprices[i])
        
    # turns data into strings to write to txt
    
    filternames = '@'.join(str(y) for y in filternames)
    filterprices = '@'.join(str(y) for y in filterprices)
    
    # writes data to txt file
    f = open(f'{write_to}.txt', 'a')
    f.write('\n')
    f.write(str(datetime.date.today()))
    f.write('\n')
    f.write(filternames)
    f.write('\n')
    f.write(filterprices)
    f.close()

data=findcardprices(data,set,token)
writetotxt(data,write_to)
