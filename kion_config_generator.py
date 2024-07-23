import csv
import yaml
import os

def get_user_input():
    url = input("Enter the Kion URL: ")
    api_key = input("Enter the API key: ")
    return url, api_key

def parse_csv(file_path):
    favorites = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            favorite = {
                'name': row['Account Alias'],
                'account': row['Account Number'],
                'cloud_access_role': row['CAR'],
                'access_type': row.get('Access Type', 'cli'),  # default to 'cli' if not provided
                'region': row.get('Region', '')  # optional field
            }
            # Remove 'access_type' and 'region' if they are empty or default
            if favorite['access_type'] == 'cli':
                del favorite['access_type']
            if not favorite['region']:
                del favorite['region']
            favorites.append(favorite)
    return favorites

def create_yaml(url, api_key, favorites, output_path):
    data = {
        'kion': {
            'url': url,
            'api_key': api_key
        },
        'favorites': favorites
    }

    with open(output_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False, sort_keys=False)

def main():
    url, api_key = get_user_input()

    csv_path = os.path.join('data', 'input.csv')
    if not os.path.exists(csv_path):
        print(f"CSV file not found at {csv_path}. Please make sure the file exists.")
        return

    favorites = parse_csv(csv_path)
    output_path = os.path.join('data', 'kion.yml')
    create_yaml(url, api_key, favorites, output_path)
    print(f"YAML file created at {output_path}")

if __name__ == "__main__":
    main()
