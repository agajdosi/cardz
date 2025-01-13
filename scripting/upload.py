from pocketbase import PocketBase
from dotenv import load_dotenv
import os

load_dotenv(".env")

username = os.environ.get("PB_USERNAME", "")
password = os.environ.get("PB_PASSWORD", "")


client = PocketBase('https://pb1.lab.gajdosik.org')

# authenticate as regular user
user_data = client.collection("users").auth_with_password(username, password) # check if user token is valid
print(f"User {username} succeffsully logged in: {user_data.is_valid}")


# list and filter "example" collection records
#result = client.collection("Posts").get_list(1, 20, {"filter": 'created > "2022-08-01 10:00:00"'})
#for item in result.items:
#    print(item.title, item.post)


result = client.collection("Posts").create({"Title":"Hello from Python", "Post": "I have just created this using the python."})
print(result)



