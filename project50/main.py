import requests
from datetime import datetime


url_to_site="https://pixe.la/v1/users/yigitkandemir/graphs/graph1.html"

USERNAME="yigitkandemir"
TOKEN="fdsmk42kmldcslk42lkdcskv4k"
ID="graph1"




# To preapare web site

pixela_endpoint="https://pixe.la/v1/users"
user_params= {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}



# To preapare web sites css

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params= {
    "id":ID,
    "name":"coding",
    "unit":"time",
    "type":"float",
    "color":"shibafu"

}


headers={
    "X-USER-TOKEN":TOKEN
}




# To give your daily information


today=datetime.now()

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how much time did you study? : "),
}


response=requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
print(response)





# To update anyday's value
# To make update uncomment two lines at the bottom of the code

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{20250212}"
update_params={
    "quantity":"4.5"
}


# response=requests.put(url=update_endpoint,json=update_params,headers=headers)
# print(response)





# To delete any day's pixel
# To make delete operation uncomment two lines at the bottom of the code


delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{20250212}"


# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response)