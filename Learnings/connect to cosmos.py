import json
import azure.cosmos.cosmos_client as cosmos_client1


## Config Load
with open(r'config.json') as config_file:
	config = json.load(config_file)

cosmosdb_endpoint1 = 'https://dev01ssgai01meta01cosmos02.documents.azure.com:443/'
cosmosdb_key1 = '5qyCUAmmBkICmksyMICh1973XifQC5r1CAOwNfUNEYHOI2SxCbFhAVBNjClYvhjTQMaVCnpqzErLNR1LXAv7kQ=='
cosmosdb_database1 = 'apicontentdb'
cosmosdb_container1 = 'youtube'

# Initialize the Cosmos client
client1 = cosmos_client1.CosmosClient(url_connection=cosmosdb_endpoint1, auth={
                                    'masterKey': cosmosdb_key1})

database_link1 = 'dbs/' + cosmosdb_database1
collection_link1 = database_link1 + '/colls/{0}'.format(cosmosdb_container1)
container1 = client1.ReadContainer(collection_link1) 
##########################################################################################

# print(client)
# print(client1)
# print(container)
# print(container1)

# Query these items in SQL
query = {'query': 'SELECT * FROM c'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client1.QueryItems(container1['_self'], query, options)

for item in iter(result_iterable):
	#Prints documents record by record. Item corresponds to a document
	print(item)	  	
    
	#To append create or overwrite documents back in collection
    	upsert = client1.UpsertItem(collection_link1, item, options=None)
