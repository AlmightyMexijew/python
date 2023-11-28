import requests

target_host = input("Enter host: ")
target_protocol = input("Enter protocol: ")
subdomain_yesno = input("Is there a sub domain? y/n: ")
if subdomain_yesno == "y":
    subdomain = input("Input subdomain") + "."
else:
    print("No subdomain")
    subdomain = ""

response = requests.get(f'{target_protocol}://{subdomain}{target_host}')
print(response.text)