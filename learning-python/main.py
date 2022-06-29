# import re

# Come vogliamo la nostra stringa < "#Property.Codice_Immobile = ""I_RMX1320A"""; >


# with open('CodiciAbbonati.csv') as f:
#     linee = f.readlines()

# MyStr = '"#Property.Codice_Immobile = '



# print(lines)

# for line in lines:
#     Stringa = MyStr +' "'+ line + ' perche vai a capo?!?!'
#     # Test.append(Stringa)
#     f = open("test.csv","a")
#     f.write(Stringa + "\n")
#     f.close()



# print(Test)

# for i in Test:
#     f = open("NewCsv.csv", "a")
#     f.write(i)
#     f.close()


# Properties =  ['#Property.Codice_Immobile','#Property.CAP', '#Property.Regione', '#Property.Proprieta', 
#                 '#Property.Codici_Edifici_SAP_Associati', '#Property.Data_Inizio_Gestione', '#Property.Provincia',
#                 '#Property.Area_Immobiliare', '#Property.Comune', '#Property.Tipo_Immobile', '#Property.Data_Costruzione',
#                 '#Property.Denominazione_Immobile', '#Property.Indirizzo', '#Property.Utilizzo_Aziendale', '#Property.Tipo_Proprieta']



#Inseriamo tutti i codici in una lista
lines = ""
f = open("CodiciAbbonati.csv", "r")
lines = f.read()
f.close

#print(lines)

list = lines.split('\n')

print(len(list))

MyStr = '"#Property.Codice_Immobile = '
other_property = '"#Property.Area_Immobiliare = ""SEDE CENTRALE""";"#Property.Codici_Edifici_SAP_Associati = ""RMX13200""";"#Property.Denominazione_Immobile = ""TORRE""";"#Property.Indirizzo = ""VIALE EUROPA 175""";"#Property.CAP = ""00144""";"#Property.Comune = ""ROMA""";"#Property.Provincia = ""ROMA""";"#Property.Regione = ""LAZIO""";"#Property.Tipo_Immobile = ""FABBRICATO""";"#Property.Tipo_Proprieta = ""Cielo terra""";"#Property.Proprieta = ""Poste italiane""";"#Property.Utilizzo_Aziendale = ""UFFICI DIREZIONALI""";"#Property.Data_Costruzione = ""1975-01-01""";"#Property.Data_Inizio_Gestione = ""1975-01-01""";"#ProjectInfo.Latitudine=""41.8312995""";"#ProjectInfo.Longitudine=""12.4680393"""\n'

for line in list:
    row = (MyStr + '"' + line + '"";' + other_property)
    f = open("test.csv",'a')
    f.write(row)
    f.close()
