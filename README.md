
# Kion Config Generator

This script generates a YAML configuration file for Kion based on user input and a CSV file.

## Kion Prerequisites

- Kion Installed
- Accounts added to Kion
- CARs added to Accounts
- API Key set up.

## System Prerequisites

- Python 3.x
- PyYAML library

Install the required library using pip:

```sh
pip install -r requirements.txt
```

## Preparing the Input CSV

Create an `input.csv` file with the following structure and place it in the `data` directory. The CSV should have the following columns:

```csv
Account Alias,Account Number,CAR,Access Type,Region
```

### Example `input.csv`

```csv
Account Alias,Account Number,CAR,Access Type,Region
sandbox,111122223333,Admin,web,us-gov-west-1
sandbox,111122223333,Admin,,  # Access Type defaults to 'cli' and Region is optional
```

- `Account Alias`: The name or alias for the account.
- `Account Number`: The 12-digit AWS account number.
- `CAR`: The cloud access role the user will use to access the account.
- `Access Type` (optional): Either `cli` or `web`. Defaults to `cli` if not provided.
- `Region` (optional): The region for the account. If not provided, this field will be omitted.

## Running the Script

CD into the directory where this Python script is located and ensure the `input.csv` file with account information is in the `data` directory.

Run the script:

```sh
python kion_config_generator.py
```

### User Input

When you run the script, you will be prompted to enter the following:

- **Kion URL**: The URL for your Kion instance.
- **API Key**: The API key for accessing Kion.

The script will then generate a `kion.yml` file in the `data` directory with the provided information and the contents of the `input.csv` file.

### Output

The generated `kion.yml` file will be in the following format:

```yaml
kion:
  url: https://mykion.example
  api_key: [api key]
favorites:
  - name: sandbox
    account: "111122223333"
    cloud_access_role: Admin
    access_type: web               # optional (defaults to cli)
    region: us-gov-west-1          # optional
```

Ensure that the provided URL and API key are accurate and valid for your Kion instance.
