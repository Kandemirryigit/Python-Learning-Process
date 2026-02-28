import requests

GENDER="male"
WEİGHT_KG="82"
HEİGHT_CM="185"
AGE="18"

app_id="c5e574bd"
api_key="e3a06618d8365167c598d421cdd4fc04—"

exercise_endpoint="'https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text=input("Tell me which exercises you did: ")

headers={
    "x-app-id":app_id,
    "x-app-key":api_key,
}

parameters={
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEİGHT_KG,
    "height_cm":HEİGHT_CM,
    "age":AGE
}

response=requests.post(exercise_endpoint,json=parameters,headers=headers)
result=response.json()
print(result)