import cv2


class Utils():

    def addLabel(img, x, y, width, height, class_id, confidence, drone):
        # Add labels or shapes
        color = (255,255,255) 
        width = int(width)
        height = int(height)
                
                
        label_text = class_id +" : "+ str(round(confidence,2))
        if(drone.__eq__("A")):
            color = (0,0,255)
        elif(drone.__eq__("B")):
            color = (255,0,0)
        elif(drone.__eq__("C")):
            color = (0,255,0)
        
        
        img  = cv2.rectangle(img, (x, y), (x + width, y + height), color, 2)
        
        cv2.putText(img , label_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        