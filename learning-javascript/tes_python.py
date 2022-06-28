import json

# Json = {
#     "Records": [
#         {
#             "eventID": "7de3041dd709b024af6f29e4fa13d34c",
#             "eventName": "INSERT",
#             "eventVersion": "1.1",
#             "eventSource": "aws:dynamodb",
#             "awsRegion": "region",
#             "dynamodb": {
#                     "ApproximateCreationDateTime": 1655462718,
#                     "Keys": {
#                         "id": {
#                             "S": "I_LEX00400"
#                         }
#                     },
#                     "NewImage": {
#                         "end_date": {
#                             "S": "test_end_date"
#                         },
#                         "image": {
#                             "S": "test_image"
#                         },
#                         "extension": {
#                             "S": "test_extension"
#                         },
#                         "external_data": {
#                             "S": "test_external_data"
#                         },
#                         "tagbim": {
#                             "M": {
#                                 "Property.Indirizzo": {
#                                     "S": "PIAZZALE STAZIONE"
#                                 },
#                                 "Property.Data_Inizio_Gestione": {
#                                     "S": "1848-01-01"
#                                 },
#                                 "ProjectInfo.Latitudine": {
#                                     "S": "40.3456783"
#                                 },
#                                 "Property.Codici_Edifici_SAP_Associati": {
#                                     "S": "LEX00400"
#                                 },
#                                 "Property.CAP": {
#                                     "S": "73100"
#                                 },
#                                 "Property.Tipo_Proprieta": {
#                                     "S": "Cielo terra"
#                                 },
#                                 "Property.Data_Costruzione": {
#                                     "S": "1848-01-01"
#                                 },
#                                 "Property.Proprieta": {
#                                     "S": "Poste italiane"
#                                 },
#                                 "Property.Denominazione_Immobile": {
#                                     "S": "LECCE 2"
#                                 },
#                                 "Property.Utilizzo_Aziendale": {
#                                     "S": "UFFICIO APERTO AL PUBBLICO CON UFFICI DIREZIONALI"
#                                 },
#                                 "ProjectInfo.Longitudine": {
#                                     "S": "18.1665539"
#                                 },
#                                 "Property.Regione": {
#                                     "S": "PUGLIA"
#                                 },
#                                 "Property.Area_Immobiliare": {
#                                     "S": "SUD"
#                                 },
#                                 "Property.Comune": {
#                                     "S": "LECCE"
#                                 },
#                                 "Property.Provincia": {
#                                     "S": "LECCE"
#                                 },
#                                 "Property.Codice_Immobile": {
#                                     "S": "I_LEX00400"
#                                 },
#                                 "Property.Tipo_Immobile": {
#                                     "S": "FABBRICATO"
#                                 }
#                             }
#                         },
#                         "subject": {
#                             "S": "test_subject"
#                         },
#                         "name": {
#                             "S": "test_name"
#                         },
#                         "id": {
#                             "S": "I_LEX00400"
#                         },
#                         "state": {
#                             "S": "test_state"
#                         },
#                         "start_date": {
#                             "S": "test_start_date"
#                         }
#                     },
#                     "SequenceNumber": "17945400000000005893275605",
#                     "SizeBytes": 787,
#                     "StreamViewType": "NEW_AND_OLD_IMAGES"
                
#             },
#             "eventSourceARN": "arn:aws:dynamodb:region:123456789012:table/BarkTable/stream/2016-11-16T20:42:48.104"
#         }
#     ]
# }

# example = {
#     "Records":
#     [
        
#         {
#             'color': "red",
#             'value': "#f00"
#         },
#         {
#             'color': "green",
#             'value': "#0f0"
#         },
#         {
#             'color': "blue",
#             'value': "#00f"
#         },
#         {
#             'color': "cyan",
#             'value': "#0ff"
#         },
#         {
#             'color': "magenta",
#             'value': "#f0f"
#         },
#         {
#             'color': "yellow",
#             'value': "#ff0"
#         },
#         {
#             'color': "black",
#             'value': "#000"
#         }
#     ]

    
# }

# test = len(example["Records"])
# # print(test)
# mynewlength = 2
# for i  in range(mynewlength):
#     print(example["Records"][i]['color'])

myMap = [{'subject': {'S': 'test_subject'}, 'end_date': {'S': 'test_end_date'}, 'external_data': {'S': 'test_external_data'}, 'time': {'N': '1656083339731'}, 'name': {'S': 'test_name'}, 'state': {'S': 'test_state'}, 'tagbim': {'M': {'Property.Indirizzo': {'S': 'PIAZZA GIUSEPPE GARIBALDI 1'}, 'Property.Data_Inizio_Gestione': {'S': '1926-01-01'}, 'ProjectInfo.Latitudine': {'S': '44.417113'}, 'Property.Codici_Edifici_SAP_Associati': {'S': 'RAX00100'}, 'Property.CAP': {'S': '48121'}, 'Property.Tipo_Proprieta': {'S': 'Cielo terra'}, 'Property.Data_Costruzione': {'S': '1928-04-21'}, 'Property.Proprieta': {'S': 'Poste italiane'}, 'Property.Denominazione_Immobile': {'S': 'RAVENNA CENTRO'}, 'Property.Utilizzo_Aziendale': {'S': 'UFFICI DIREZIONALI'}, 'ProjectInfo.Longitudine': {'S': '12.2005103'}, 'Property.Regione': {'S': 'EMILIA-ROMAGNA'}, 'Property.Area_Immobiliare': {'S': 'CENTRO NORD'}, 'Property.Comune': {'S': 'RAVENNA'}, 'Property.Provincia': {'S': 'RAVENNA'}, 'Property.Codice_Immobile': {'S': 'I_RAX00100'}, 'Property.Tipo_Immobile': {'S': 'FABBRICATO'}}}, 'image': {'S': 'test_image'}, 'start_date': {'S': 'test_start_date'}, 'extension': {'S': 'test_extension'}, 'file_name': {'S': 'temp/2022-06-24-15:08:56testing-events.csv'}, 'id': {'S': 'I_RAX00100'}}]
json = json.dumps(myMap)

print(json['subject'])