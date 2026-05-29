import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users():
    try:
        response = requests.get(API_URL)

        # Check request status
        response.raise_for_status()

        # Convert JSON to Python
        users = response.json()

        return users

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def search_user(users, keyword):

    found = False

    for user in users:

        if keyword.lower() in user['name'].lower():

            print("\nUser Found")
            print("-" * 30)

            print("Name :", user['name'])
            print("Email:", user['email'])
            print("City :", user['address']['city'])

            found = True

    if not found:
        print("No user found.")

# Main Program
print("===== API Data Fetcher =====")

users = fetch_users()

if users:

    print(f"\nTotal Users Fetched: {len(users)}")

    keyword = input("\nEnter name to search: ")

    search_user(users, keyword)