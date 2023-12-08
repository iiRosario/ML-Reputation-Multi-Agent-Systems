from tkinter import *  
import csv
import cv2
from roboflow import Roboflow
from Drone import Drone

from Master import Master
from utils.Utils import Utils



#image_path = "mastersTests/test-8.jpg"
#image_path = "mastersTests/test-21.jpeg"
#image_path = "mastersTests/test-17.jpg"
image_path = "mastersTests/test-10.jpg"
predicitonA_path = "predictions/predicitonA.jpg"
predicitonB_path = "predictions/predicitonB.jpg"
predicitonC_path = "predictions/predicitonC.jpg"
predictionM_path = "predictions/predictionM.jpg"
confidence = 51
overlap = 0


rfA = Roboflow(api_key="usQXRh13NGjn2HK6BwFP")
project1 = rfA.workspace().project("drone-a-tb89u")
modelA = project1.version(2).model

rfB = Roboflow(api_key="usQXRh13NGjn2HK6BwFP")
project2 = rfB.workspace().project("drone-b-xkvry")
modelB = project2.version(1).model

rfC = Roboflow(api_key="usQXRh13NGjn2HK6BwFP")
project3 = rfC.workspace().project("drone-c-hytyd")
modelC = project3.version(5).model

values = [0.0, 0.25, 0.50, 0.75, 1]
drone_A_confidence = 0.1
drone_B_confidence = 0.5
drone_C_confidence = 0.5




csv_filename = 'masterResults.csv'
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['A - Cars', 'A - Houses', 'A - Trees', 
                    'B - Cars', 'B - Houses', 'B - Trees',
                    'C - Cars', 'C - Houses', 'C - Trees',
                    'A Reputation','B Reputation','C Reputation'])
  
    # for permA in values:
    #     for permB in values:
    #         for permC in values:
                
    drone_A_confidence = drone_A_confidence
    drone_B_confidence = drone_B_confidence
    drone_C_confidence = drone_A_confidence
    #print(f'{permA} , {permB}, {permC}')
    ################################################################
    #################### DRONE A ###################################

    
    predictA = modelA.predict(image_path, confidence=confidence, overlap=overlap)
    drone_A = Drone("A", drone_A_confidence, predictA.json())
    predictA.save(predicitonA_path)
    drone_A.saveInCsv()

    #plot_model(modelA, to_file='cnns/a.png', show_shapes=True, show_layer_names=True)
    ################################################################
    #################### DRONE B ###################################

    predictB = modelB.predict(image_path, confidence=confidence, overlap=overlap)
    drone_B =  Drone("B", drone_B_confidence, predictB.json())
    predictB.save(predicitonB_path)
    drone_B.saveInCsv()

    ################################################################
    #################### DRONE C ###################################

    
    predictC = modelC.predict(image_path, confidence=confidence, overlap=overlap) 
    drone_C = Drone("C", drone_C_confidence, predictC.json())
    predictC.save(predicitonC_path)
    drone_C.saveInCsv()

    ################################################################
    ####################### CALCULATION ############################
    ################################################################

    master = Master(drone_A,drone_B , drone_C)

    ## PLOT THE SUM OF THE BEST CONFIDENCES
    clone_img = cv2.imread(image_path)
    masterImage = clone_img.copy()  

    for box in master.identifications:
        Utils.addLabel(masterImage, box.x, box.y, box.width, box.height, box.class_type, box.confidence, box.drone)

    cv2.imwrite(predictionM_path, masterImage) 
    print(str(len(master.identifications)))
    # writer.writerow([str(master.count_A_cars), str(master.count_A_Houses), str(master.count_A_trees),
    #                 str(master.count_B_cars), str(master.count_B_Houses), str(master.count_B_trees),
    #                 str(master.count_C_cars), str(master.count_C_Houses), str(master.count_C_trees),
    #                 str(master.drone_A.confidence * 100),str(master.drone_B.confidence* 100),str(master.drone_C.confidence* 100)])

    # print(f"CSV file '{csv_filename}' has been created.")
