"""
Inference function.
"""

def predict(model, image_path: str) -> float:
    """
    Tries to detect trucks in the image located at 'image_path'.
    Returns the highest detection score among all detections if a truck is 
    found, and -1 otherwise.
    """
    truck_label = 7
    results = model(image_path)
    
    trucks_detected = []
    for detection in results.xywh[0]:
        if detection[-1] == truck_label:
            trucks_detected.append(float(detection[-2]))
    
    if trucks_detected:
        return max(trucks_detected)
    
    return -1