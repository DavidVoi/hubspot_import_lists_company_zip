import json
import requests
import argparse

def load_filters_from_json(file_path):
    """
    Load all filter definitions from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data.get('lists', [])

def create_hubspot_list(access_token, filter_branch, name, object_type_id="COMPANY"):
    """
    Create a list in HubSpot using the provided access token, filter branch, and name.
    """
    url = "https://api.hubapi.com/crm/v3/lists/"
    headers = {
        "authorization": f"Bearer {access_token}",
        "content-type": "application/json"
    }
    
    payload = {
        "listFolderId": 0,
        "filterBranch": filter_branch,
        "objectTypeId": object_type_id,
        "processingType": "DYNAMIC",  # or "STATIC" depending on your needs
        "name": name
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        print(f"List '{name}' created successfully.")
        print("Response data:", response.json())
    else:
        print(f"Failed to create list '{name}'. Status code: {response.status_code}")
        print("Response data:", response.text)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='HubSpot List Creation Script')
    parser.add_argument('--access-token', required=True, help='Your HubSpot access token')
    parser.add_argument('--file', required=True, help='Path to the JSON file containing the list definitions')

    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Load all filter data from the provided JSON file
    lists = load_filters_from_json(args.file)

    # Loop through each list in the JSON and create it in HubSpot
    for item in lists:
        filter_branch = item.get('filterBranch')
        name = item.get('name')
        create_hubspot_list(args.access_token, filter_branch, name)
