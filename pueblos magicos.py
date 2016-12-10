import json
import csv

class Profeco_json:
    data = []

    def __init__(self):
        pass

    def data_read(self,file_name):
        with open(file_name,"r") as file:
            self.data = json.load(file)

    def data_write(self):
        with open('data.csv','w') as file:
           data = csv.writer(file, delimiter=",")
           for row in self.data['results']:
               data.writerow([row['cadenaComercial'],row['latitud'],row['longitud']])
