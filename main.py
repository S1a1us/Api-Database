import json
import os

# Function to create a new API
def create_api():
    name = input("System >> Enter the name of the API: ")
    key = input("System >> Enter the API key: ")

    if not os.path.exists("api_database.json"):
        with open("api_database.json", "w") as f:
            f.write("{}")

    with open("api_database.json", "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}

    if name in data:
        print(f"System >> API with name '{name}' already exists. Please choose another name.")
        return

    data[name] = key

    with open("api_database.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"System >> API '{name}' created successfully!")


# Function to read an API key
def read_api():
    name = input("System >> Enter the name of the API to read: ")
    
    with open("api_database.json", "r") as f:
        apis = json.load(f)
        
        if name in apis:
            print(f"System >> API Key for '{name}': {apis[name]}")
        else:
            print(f"System >> No API with name '{name}' found.")

# Function to list all APIs
def list_apis():
    with open("api_database.json", "r") as f:
        apis = []
        for line in f:
            data = json.loads(line)
            apis.extend(data.keys())
        print("System >> APIs in the database:\n" + "\n".join(apis))

# Function to delete an API
def delete_api():
    name = input("System >> Enter the name of the API to delete: ")
    
    with open("api_database.json", "r") as f:
        apis = json.load(f)
        
        if name in apis:
            del apis[name]
            with open("api_database.json", "w") as f:
                json.dump(apis, f, indent=4)
            print(f"System >> API '{name}' deleted successfully!")
        else:
            print(f"System >> No API with name '{name}' found.")

# Main function
def main():
    while True:
        print("System >> Select an option:")
        print("1. Create API")
        print("2. Read API Key")
        print("3. List APIs")
        print("4. Delete API")
        print("5. Exit")

        choice = input("System >> ")

        if choice == "1":
            create_api()
        elif choice == "2":
            read_api()
        elif choice == "3":
            list_apis()
        elif choice == "4":
            delete_api()
        elif choice == "5":
            print("System >> Goodbye!")
            break
        else:
            print("System >> Invalid choice. Try again.")

if __name__ == "__main__":
    main()
