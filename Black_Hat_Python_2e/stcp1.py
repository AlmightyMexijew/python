#practicing with requests api
import requests
target_host = input("Where are we looking?")
target_port = input("http or https?")

response = requests.get(f"{target_port}://{target_host}")
print(response.text)