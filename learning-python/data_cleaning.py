import re

data = ' "#Property.Codice_Immobile = ""I_LEX00400""";"#Property.Area_Immobiliare = ""SUD""";"#Property.Codici_Edifici_SAP_Associati = ""LEX00400""";"#Property.Denominazione_Immobile = ""LECCE 2""";"#Property.Indirizzo = ""PIAZZALE STAZIONE""";"#Property.CAP = ""73100""";"#Property.Comune = ""LECCE""";"#Property.Provincia = ""LECCE""";"#Property.Regione = ""PUGLIA""";"#Property.Tipo_Immobile = ""FABBRICATO""";"#Property.Tipo_Proprieta = ""Cielo terra""";"#Property.Proprieta = ""Poste italiane""";"#Property.Utilizzo_Aziendale = ""UFFICIO APERTO AL PUBBLICO CON UFFICI DIREZIONALI""";"#Property.Data_Costruzione = ""1848-01-01""";"#Property.Data_Inizio_Gestione = ""1848-01-01""";"#ProjectInfo.Latitudine=""40.3456783""";"#ProjectInfo.Longitudine=""18.1665539"""'

# print(data.replace(\'"', ''))
# print(data.strip('"'))
# print(re.sub('["]', '', data))

# data1 = (data.replace('["""]', '"' ))
# print(data1.replace())


# NewStr = data.replace("\"\"\"", "\"")
# NewStr = data.replace("\"", "")
# NewStr = data.replace(["\""], "")
# NewStr = NewStr.replace("\"\"", "\"")

# print(NewStr)

# CAP = 12
# MyStr = "#Property.CAP = " + str(CAP) + ";"
# print(MyStr)


tagbim = {
    "#Property.CAP":{
       "S":"73100"
    },
    "#Property.Regione":{
       "S":"PUGLIA"
    },
    "#ProjectInfo.Latitudine":{
       "S":"40.3456783"
    },
    "#Property.Tipo_Proprieta":{
       "S":"Cielo terra"
    },
    "#Property.Provincia":{
       "S":"LECCE"
    },
    "#ProjectInfo.Longitudine":{
       "S":"18.1665539"
    },
    "#Property.Area_Immobiliare":{
       "S":"SUD"
    },
    "#Property.Comune":{
       "S":"LECCE"
    },
    "#Property.Tipo_Immobile":{
       "S":"FABBRICATO"
    },
    "#Property.Data_Costruzione":{
       "S":"1848-01-01"
    },
    "#Property.Denominazione_Immobile":{
       "S":"LECCE 2"
    },
    "#Property.Indirizzo":{
       "S":"PIAZZALE STAZIONE"
    },
    "#Property.Proprieta":{
       "S":"Poste italiane"
    },
    "#Property.Utilizzo_Aziendale":{
       "S":"UFFICIO APERTO AL PUBBLICO CON UFFICI DIREZIONALI"
    },
    "#Property.Data_Inizio_Gestione":{
       "S":"1848-01-01"
    },
    "#Property.Codici_Edifici_SAP_Associati":{
       "S":"LEX00400"
    },
    "#Property.Codice_Immobile":{
       "S":"I_LEX00400"
    }
}

MyStr = ""
Properties =  ['#Property.Codice_Immobile','#Property.CAP', '#Property.Regione', '#Property.Proprieta', 
                '#Property.Codici_Edifici_SAP_Associati', '#Property.Data_Inizio_Gestione', '#Property.Provincia',
                '#Property.Area_Immobiliare', '#Property.Comune', '#Property.Tipo_Immobile', '#Property.Data_Costruzione',
                '#Property.Denominazione_Immobile', '#Property.Indirizzo', '#Property.Utilizzo_Aziendale', '#Property.Tipo_Proprieta']

for property in Properties:
    value = tagbim[property]["S"]
    str = property +  ' = ' + value + '"; '
    MyStr = MyStr + str

print(MyStr)

print(len(Properties))