# src/lib/config_management.py

import json
import os

def load_config(file_path):
    """
    Load configuration from the specified JSON file.
    :param file_path: Path to the configuration file.
    :return: Configuration data as a dictionary.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_config_file(config):
    """
    Validate the configuration file structure.
    :param config: The configuration dictionary to validate.
    :return: True if the configuration is valid, False otherwise.
    """
    required_keys = ["database", "queries"]
    database_keys = ["host", "port", "user", "password"]
    queries_keys = ["fetch_data"]

    # Check top-level keys
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key: {key}")

    # Check database keys
    for key in database_keys:
        if key not in config["database"]:
            raise ValueError(f"Missing required database key: {key}")

    # Check queries keys
    for key in queries_keys:
        if key not in config["queries"]:
            raise ValueError(f"Missing required query key: {key}")

    return True

def save_config(file_path, config_data):
    """
    Save configuration data to the specified JSON file.
    :param file_path: Path to the configuration file.
    :param config_data: Configuration data as a dictionary.
    """
    with open(file_path, 'w') as file:
        json.dump(config_data, file, indent=4)
