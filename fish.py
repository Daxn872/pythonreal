# import pickle
import pickle

# declareert de data variabele
dataObject = []
# looped 5 seconden lang
for num in range(10,15):
   dataObject.append(num)

# Opent een file om de data op te slaan
file_handler = open('languages', 'wb')
# dumpt de data in de file
pickle.dump(dataObject, file_handler)
# sluit de file
file_handler.close()

# Open een file om de data te lezen
file_handler = open('languages', 'rb')
# laat de data van de file
dataObject = pickle.load(file_handler)
# loops print de data
for val in dataObject:
  print('The data value : ', val)
# sluit file
file_handler.close()