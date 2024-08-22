```markdown
# HubSpot List Creation Script

This script allows you to create multiple lists in HubSpot by reading filter definitions from a JSON file. Each list in the JSON file will be created dynamically using the provided access token.

## Features

- Read list definitions from a JSON file.
- Automatically create lists in HubSpot using the HubSpot API.
- Supports dynamic list creation with custom filters.
- Loops through all the lists defined in the JSON file and creates them one by one.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

### Command-Line Arguments

- `--access-token`: Your HubSpot access token (required).
- `--file`: Path to the JSON file containing the list definitions (required).

### Running the Script

```bash
python your_script.py --access-token your_access_token_here --file path_to_your_json_file.json
```

Replace `your_script.py` with the name of your Python script file, `your_access_token_here` with your actual HubSpot access token, and `path_to_your_json_file.json` with the path to your JSON file.

### Example

```bash
python create_hubspot_lists.py --access-token xxx-xxx-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --file plz.json
```

## JSON File Structure

The JSON file should have a structure similar to the following:

```json
{
  "lists": [
    {
      "listVersion": 2,
      "name": "Companies PLZ Brandenburg",
      "filterBranch": {
        "filterBranchType": "AND",
        "filters": {
          "property": "zip",
          "operation": {
            "operator": "IS_EQUAL_TO",
            "values": ["14467", "14469", "14471"]
          }
        }
      }
    },
    {
      "listVersion": 1,
      "name": "Companies PLZ Berlin",
      "filterBranch": {
        "filterBranchType": "AND",
        "filters": {
          "property": "zip",
          "operation": {
            "operator": "IS_EQUAL_TO",
            "values": ["10115", "10117", "10119"]
          }
        }
      }
    }
  ]
}
```

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Explanation:

- **Prerequisites**: Lists the requirements to run the script.
- **Usage**: Explains how to use the script, including the command-line arguments.
- **JSON File Structure**: Provides an example of the expected JSON file format.
- **Contributing**: Encourages contributions and provides guidelines.
- **License**: Indicates the license for the project.

This `README.md` should provide a clear and concise overview of how to use the script and what it does.
