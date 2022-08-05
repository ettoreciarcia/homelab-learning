
import boto3
import requests
import os
import json
import time
import logging
import datetime

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)
#COSTANTI 
SUBSCRIPTION_ID = 669

import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def remove_item_from_list(tableName):
   
   client = boto3.client('dynamodb')
   data = client.get_item(
      TableName = tableName,
      Key ={
         'id':{
            'S': '001'
         }
      
      }
   )

   item_to_delete = data['Item']['file_names']['L'][0]['S']

   delete_item = client.update_item(
      TableName = tableName,
      Key = {
         'id':{
            'S': '001'
         }
      },
      # ExpressionAttributeNames: {
      #   "#F": "file_names" 
      #  },

      UpdateExpression = "REMOVE file_names[0] "

   )

   logging.info("Deleted name_files = " + item_to_delete)
   return item_to_delete

def getToken(url, body, header):
    myRequest = requests.post(url, json = body, headers = header)
    if(myRequest.status_code != 200):
      logging.critical('Login FAILED')
    else:
      logging.info('/login SUCCESSFUL ')
      response = json.loads(myRequest.content)
      #  print(response)
      token = response['token']
      return token

def read_configuration_table(tableName, key):
   client = boto3.client('dynamodb')
   data = client.get_item(
      TableName = tableName,
      Key ={
         'id':{
            'S': key
         }
      }
   )
   return data

def  get_item(tableName, key):
   client = boto3.client('dynamodb')
   data = client.get_item(
      TableName = tableName,
      Key ={
         'id':{
            'S': key
         }
      }
   )
   return data

def scan_table(tableName):
   client = boto3.client('dynamodb')
   data = client.scan(
      TableName = tableName,
      Limit = 1
   )

   return data

def delete_item(tableName,key):
   client = boto3.client('dynamodb')
   data = client.delete_item(
      TableName = tableName,
      Key = {
         'id': {
            'S' : key
         }
      }
   )
   return data

def table_is_empty(tableName):
   client = boto3.client('dynamodb')
   data = client.scan(
      TableName = tableName,
      Limit = 1
   )
   if(data['Count'] > 0):
      return False
   else:
      logging.warning('Table ' + os.getenv('DynamoDB_Table') + ' is empty')
      return True

def get_item_query(tableName, indexName, indexValue):
   client = boto3.client('dynamodb')
   #file_name = 'temp/2022-07-04-11:07:40partial-test.csv'
   data = client.query(
      TableName = tableName, #tableName,
      IndexName = indexName,
      ExpressionAttributeValues={
       ':v1': {
           'S': indexValue,
         },
      },
      Limit = 1,
      KeyConditionExpression='subscriptionId = :v1'
      #https://stackoverflow.com/questions/35758924/how-do-we-query-on-a-secondary-index-of-dynamodb-using-boto3 finally
      #KeyConditionExpression =Key('file_name').eq(file_name) #from https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Query.html
   )

   return data

def remove_item_from_list(tableName):
   
   client = boto3.client('dynamodb')
   data = client.get_item(
      TableName = tableName,
      Key ={
         'id':{
            'S': '001'
         }
      
      }
   )

   item_to_delete = data['Item']['file_names']['L'][0]['S']

   delete_item = client.update_item(
      TableName = tableName,
      Key = {
         'id':{
            'S': '001'
         }
      },
      # ExpressionAttributeNames: {
      #   "#F": "file_names" 
      #  },

      UpdateExpression = "REMOVE file_names[0] "

   )

   logging.info("Deleted name_files = " + item_to_delete)
   return item_to_delete



def main():

   #LOGGING
   FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   logging.basicConfig(format=FORMAT)

   fh = logging.FileHandler(filename='/tmp/example.log', encoding='utf-8')
   fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

   logger = logging.getLogger()
   logger.setLevel(logging.INFO)
   logger.addHandler(fh)
   logger.info('Hello')


   body = {
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD')
    }

   myHeaderLogin ={
    'X-USBIM-PLATFORM-SERVICE-KEY' : os.getenv('HEADER_VALUE')
   }

   # env var e valori letti dalla tabella di configurazione di DynamoDB
   url = os.getenv('URL_TOKEN')
   

   token = getToken(url, body, myHeaderLogin)

   logging.info("Token from /login " + token)

   headerPostLogin ={
      'X-USBIM-PLATFORM-SERVICE-KEY' : os.getenv('HEADER_VALUE'),
      'X-USBIM-PLATFORM-ACCESS-TOKEN': token
   } 

   postData = {
      'subscription_id': SUBSCRIPTION_ID,
      'latitudine': '',
      'longitudine': '',
      'tagbim'     : ''
   }

   

   #Chiamata per impersonificare un altro utente
   bodyAdminRole = {
      'email': os.getenv('USERNAME_TO_IMPERSONATE')
   }

   urlGetAdminRole = os.getenv('URL_IMPERSONATE_USER')
   getAdminRole = requests.post(urlGetAdminRole, json = bodyAdminRole, headers = headerPostLogin)
   risposta = json.loads(getAdminRole.content)
   adminToken = risposta['token']
   logging.info("Token from /generateTokenJWT " + adminToken)
   #URL A CUI FARE LA RICHIESTA DOPO AVER OTTENUTO IL TOKEN //La post va fatta sul path /projects/<project_id>/edit

   ultimateLoginHeader ={
      'X-USBIM-PLATFORM-SERVICE-KEY' : os.getenv('HEADER_VALUE'),
      'X-USBIM-PLATFORM-ACCESS-TOKEN': adminToken
   } 

   url_ultimate_post = os.getenv('URL_POST')
  

   #Leggo i dati dalla tabella di configurazione DynamoDB
   response = read_configuration_table(os.getenv('Configuration_Table'), '001')
   interval = response['Item']['intervalFromRequest']['N']
   numberOfRequest = response['Item']['numberOfRequest']['N']
   
   empty = table_is_empty(os.getenv('DynamoDB_Table'))
   i = 0

   while ( i < int(numberOfRequest) and empty == False ):
      #item =scan_table(os.getenv('DynamoDB_Table'))
      item = get_item_query(os.getenv('DynamoDB_Table'), 'subscriptionId_time', '6675')
      #Prendiamo la chiave primaria per cancellare l'elemento di cui facciamo la POST
      #print(item)
      primary_key = item['Items'][0]['id']['S']

      #Popoliamo i campi della nostra post
      postData['latitudine'] = item['Items'][0]['latitudine']['S']
      postData['longitudine'] = item['Items'][0]['longitudine']['S']
      tag = item['Items'][0]['tagbim']['M']


      Properties =  ['#Property.Codice_Immobile','#Property.CAP', '#Property.Regione', '#Property.Proprieta', 
               '#Property.Codici_Edifici_SAP_Associati', '#Property.Data_Inizio_Gestione', '#Property.Provincia',
               '#Property.Area_Immobiliare', '#Property.Comune', '#Property.Tipo_Immobile', '#Property.Data_Costruzione',
               '#Property.Denominazione_Immobile', '#Property.Indirizzo', '#Property.Utilizzo_Aziendale', '#Property.Tipo_Proprieta']

      str_tagbim = ""
      for property in Properties:
         value = tag[property]["S"]
         str = property +  ' = "' + value + '"; '
         str_tagbim = str_tagbim + str

      postData['tagbim'] = str_tagbim
      postData['code'] = primary_key


      # print(postData['tagbim'])
      #print(postData)
      # print("Faccio la POST della riga che contiene la chiave primaria " + primary_key)
      post = requests.post(url_ultimate_post, json = postData, headers = ultimateLoginHeader)
      print(post.content)
      if(post.status_code == 200):
         #Se la post va a buon fine posso rimuovere l'item, altrimenti printo l'errore e passo all'item successivo
         #Attendo il numero di secondi specificato in "IntervalFromRequest" della tabella di configurazione
         time.sleep(int(interval))
         #rimuovo l'item di cui ho fatto la post
         item_deleted = delete_item(os.getenv('DynamoDB_Table'), primary_key)
         logging.info("SUCCESS! Item with primary key " + primary_key + " posted successfully")
      else:
         logging.warning("Failed post of Item with Primary Key : " + primary_key)
         logging.warning(post.content)
         logger.info('PROBLEM')
      i = i + 1
      empty = table_is_empty(os.getenv('DynamoDB_Table'))







def lambda_handler(event, context):
   try:
      main()
   except:
      logging.info('Error')
   finally:
      key_name ='6675/logs/' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
      upload_file('/tmp/example.log', os.getenv('LOG_BUCKET'), key_name)
      
