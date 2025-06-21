import requests

# === ✅ STEP 1: Replace these two lines ===
prediction_key = "1OIDhuJKwQZbBZEmrg3PJ9WKuXCp0DybLcusfhy5w6hh4Z19JMrSJQQJ99BFACYeBjFXJ3w3AAAIACOGZrsb"  
endpoint = "https://visionapphanan01-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/21c1f6d0-a281-44f2-b8f6-17578d93bf1e/classify/iterations/Iteration1/image"        

# === ✅ STEP 2: Make sure the published name is correct ===
published_name = "Iteration1"                # This usually stays as 'Iteration1'

# === ✅ STEP 3: Make sure your image file is correct ===
image_path = "apple.jpeg"                     # Must match the exact file name


with open(image_path, "rb") as image_data:
    headers = {
        "Prediction-Key": prediction_key,
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(
        url=endpoint,
        headers=headers,
        data=image_data
    )

if response.status_code == 200:
    results = response.json()
    print("\nPrediction Results:")
    for prediction in results["predictions"]:
        tag = prediction["tagName"]
        probability = prediction["probability"] * 100
        print(f"  {tag}: {probability:.2f}%")
else:
    print(f"Error: {response.status_code} - {response.text}")
