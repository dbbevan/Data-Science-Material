import logging
import json
from IPython.display import HTML
import azure.functions as func
from azure.storage.blob import BlockBlobService 


def main(myblob: func.InputStream):
    ## Config Load
    with open(r'config.json') as config_file:
        config = json.load(config_file)

    blob_account_name = <enter blob storage account name>
    blob_account_key = <Enter storage account key>
    your_container = <Enter container name>
  
    jsonfile = os.path.split(myblob.uri)[1]
    blob_service = BlockBlobService(account_name=blob_account_name, account_key=blob_account_key)
    blob_service.get_blob_to_path(mycontainer, jsonfile, jsonfile)

    with open(os.path.split(myblob.uri)[1]) as json_file:
        data = json.load(json_file)