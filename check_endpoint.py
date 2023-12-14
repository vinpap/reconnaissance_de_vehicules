import requests

request_data = {"img_path": 'https://www.udtrucks.com/sites/default/files/styles/image_text_component/public/2022-11/Croner.png?itok=5sKgKamc'}
print(requests.get("reconnaissance-de-vehicules.azurewebsites.net", params=request_data))