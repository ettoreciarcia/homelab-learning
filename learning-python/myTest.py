import json

myJson =  {'Items': [{'subject': {'S': 'test_subject'}, 'end_date': {'S': 'test_end_date'}, 'external_data': {'S': 'test_external_data'}, 'time': {'N': '1656083339731'}, 'name': {'S': 'test_name'}, 'state': {'S': 'test_state'}, 'tagbim': {'M': {'Property.Indirizzo': {'S': 'PIAZZA GIUSEPPE GARIBALDI 1'}, 'Property.Data_Inizio_Gestione': {'S': '1926-01-01'}, 'ProjectInfo.Latitudine': {'S': '44.417113'}, 'Property.Codici_Edifici_SAP_Associati': {'S': 'RAX00100'}, 'Property.CAP': {'S': '48121'}, 'Property.Tipo_Proprieta': {'S': 'Cielo terra'}, 'Property.Data_Costruzione': {'S': '1928-04-21'}, 'Property.Proprieta': {'S': 'Poste italiane'}, 'Property.Denominazione_Immobile': {'S': 'RAVENNA CENTRO'}, 'Property.Utilizzo_Aziendale': {'S': 'UFFICI DIREZIONALI'}, 'ProjectInfo.Longitudine': {'S': '12.2005103'}, 'Property.Regione': {'S': 'EMILIA-ROMAGNA'}, 'Property.Area_Immobiliare': {'S': 'CENTRO NORD'}, 'Property.Comune': {'S': 'RAVENNA'}, 'Property.Provincia': {'S': 'RAVENNA'}, 'Property.Codice_Immobile': {'S': 'I_RAX00100'}, 'Property.Tipo_Immobile': {'S': 'FABBRICATO'}}}, 'image': {'S': 'test_image'}, 'start_date': {'S': 'test_start_date'}, 'extension': {'S': 'test_extension'}, 'file_name': {'S': 'temp/2022-06-24-15:08:56testing-events.csv'}, 'id': {'S': 'I_RAX00100'}}], 'Count': 1, 'ScannedCount': 1, 'LastEvaluatedKey': {'id': {'S': 'I_RAX00100'}}, 'ResponseMetadata': {'RequestId': 'VIL1DLJBK3H60ES59EUOQU3DFBVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sun, 26 Jun 2022 10:07:22 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '1260', 'connection': 'keep-alive', 'x-amzn-requestid': 'VIL1DLJBK3H60ES59EUOQU3DFBVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3525181751'}, 'RetryAttempts': 0}}

item = myJson['Items']
print(item)
print(type(item))

for i in myJson['Items']:
    value = i['subject']['S']

print(value)