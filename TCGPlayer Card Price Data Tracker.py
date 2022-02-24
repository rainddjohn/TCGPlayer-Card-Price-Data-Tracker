import requests;cardnames=[];normalprices=[];foilprices=[];import datetime

set="Innistrad: Crimson Vow"
write_to='crimson_vow'

def findcardprices(cardnames,normalprices,foilprices,set):
    ##this part searches for the productIDs'
    token='OMITTED FOR PRIVACY'

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
    assert r.status_code == 200
    search_response_data = r.json()
    #print('Search complete:');#print(search_response_data)
    productIDs=list(search_response_data.values());productIDs=productIDs[3];backupproductIDs=list(productIDs)

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
    #print('Search complete:');print(search_response_data)

    ###prices input to lists
    priceresults=list(search_response_data['results']);normalprices=[];foilprices=[]
    for i in priceresults:
        if i['subTypeName']=='Normal':
            normalprices.append(i['marketPrice'])
        if i['subTypeName']=='Foil':
            foilprices.append(i['marketPrice'])

    #this part turns productIDs into names
    r = requests.get(
        f'https://api.tcgplayer.com/v1.39.0/catalog/products/{productIDs}',
        headers={
            'Authorization': f"bearer {token}"
        }
    )
    search_response_data = r.json()
    #print('Search complete:');print(search_response_data)
    nameresults=search_response_data['results'];cardnames=[]
    for j in backupproductIDs:
        for i in nameresults:
            if j==i['productId']:
                cardnames.append(i['name'])
    #for i in range(len(cardnames)): print(cardnames[i], normalprices[i])
    return cardnames,normalprices,foilprices
def token(): ## you need this if your token expires
    import requests
    payload = {
        'OMITTED FOR PRIVACY'
        }
    r = requests.post('https://api.tcgplayer.com'
             + '/token',
            data=payload,
        )
    token_response_data = r.json()
    print('Token Received:')
    print(token_response_data)
def writetotxt(cardnames,normalprices,foilprices):
    filternames = [];filterprices = []
    # takes out cards we don't want in this list
    for i in range(len(cardnames)):
        if normalprices[i] is None: continue
        if not '(' in cardnames[i] and not ' - ' in cardnames[i] and int(normalprices[i] > 2):
            filternames.append(cardnames[i]);filterprices.append(normalprices[i])

    # for i in range(len(cardnames)):print(cardnames[i],foilprices[i])
    for i in range(len(filternames)): print(filternames[i], filterprices[i])

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
#token()
cardnames,normalprices,foilprices=findcardprices(cardnames,normalprices,foilprices,set);writetotxt(cardnames,normalprices,foilprices,write_to)

