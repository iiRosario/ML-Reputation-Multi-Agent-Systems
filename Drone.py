from Identification import Identification
import csv

# Drone.py
# Authors: Diogo Rosário, João Raposo
# Description: This file defines the Drone object utilized in main.py. The objective is to simulate a drone with the following attributes:
# - Name: A or B or C
# - Confidence: Initial reputation
# - Json: JSON file containing predictions/identifications from corresponding models
# - Identifications: List of predictions/identifications from each model
class Drone():    
    def __init__(self,name, confidence, json):
        self.name = name
        self.confidence = confidence
        self.json = json
        self.identifications = self.createObjects()

    
    # Generates the identification list for each Drone object by utilizing the JSON file created during the model's prediction process.
    def createObjects(self):
        objects = []
        
        for iteration in self.json.get("predictions"):
            x = int(iteration.get("x"))    
            y = int(iteration.get("y"))
            width = int(iteration.get("width"))
            height = int(iteration.get("height"))
            ident_confidence = iteration.get("confidence")
            class_type = iteration.get("class")
            
            x = int(x - round(width / 2))
            y = int(y - round(height / 2))
            obj = Identification(x,y,width,height,ident_confidence,class_type, self.name, self.confidence)
            objects.append(obj)

        return objects


    # Saves the identifications in the corresponding csv file
    def saveInCsv(self):

        if self.name == "A":
            csv_filename = 'droneA_Identification.csv'
            with open(csv_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Identification', 'x', 'y', 'width', 'height', 'confidence', 'class_type'])

                for i, identification in enumerate(self.identifications, start=1):
                    writer.writerow([f'identification {i}', identification.x, identification.y, identification.width,
                                     identification.height, identification.confidence, identification.class_type])

            print(f"CSV file '{csv_filename}' has been created.")

        elif self.name == "B":
            csv_filename = 'droneB_Identification.csv'
            with open(csv_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Identification', 'x', 'y', 'width', 'height', 'confidence', 'class_type'])

                for i, identification in enumerate(self.identifications, start=1):
                    writer.writerow([f'identification {i}', identification.x, identification.y, identification.width,
                                     identification.height, identification.confidence, identification.class_type])

            print(f"CSV file '{csv_filename}' has been created.")

        elif self.name == "C":
            csv_filename = 'droneC_Identification.csv'
            with open(csv_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Identification', 'x', 'y', 'width', 'height', 'confidence', 'class_type'])

                for i, identification in enumerate(self.identifications, start=1):
                    writer.writerow([f'identification {i}', identification.x, identification.y, identification.width,
                                     identification.height, identification.confidence, identification.class_type])

            print(f"CSV file '{csv_filename}' has been created.")
        
        
        
        
    
    
    