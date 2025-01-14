# tests/test_config_management.py

import pytest
import json
import os
from lib.config_management import load_config, validate_config_file, save_config

"""
Purpose: Test the creation, validation, and handling of configuration files.
Test Cases:
- Load a custom configuration file.
- Validate the structure of a configuration file.
- Test SOQL queries in the configuration file.
- Handle missing or invalid parameters in the configuration.
"""

@pytest.fixture
def setup_and_teardown():
    """
    Create temporary configuration files for testing and clean them up after the test.
    """
    config_path = 'test_config.json'
    invalid_config_path = 'test_invalid_config.json'
    missing_config_path = 'test_missing_config.json'
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "password"
        },
        "queries": {
            "fetch_data": "SELECT * FROM table"
        }
    }
    with open(config_path, 'w') as f:
        json.dump(sample_config, f)

    yield config_path, invalid_config_path, missing_config_path, sample_config

    # Cleanup temporary files
    if os.path.exists(config_path):
        os.remove(config_path)
    if os.path.exists(invalid_config_path):
        os.remove(invalid_config_path)
    if os.path.exists(missing_config_path):
        os.remove(missing_config_path)

def test_load_custom_config_file(setup_and_teardown):
    """Test loading a valid custom configuration file."""
    config_path, _, _, sample_config = setup_and_teardown
    config = load_config(config_path)
    assert config == sample_config

def test_validate_config_structure(setup_and_teardown):
    """Test validating the structure of a configuration file."""
    config_path, _, _, _ = setup_and_teardown
    config = load_config(config_path)
    assert validate_config_file(config) is True

def test_handle_missing_config_file(setup_and_teardown):
    """Test handling a missing configuration file."""
    _, _, missing_config_path, _ = setup_and_teardown
    with pytest.raises(FileNotFoundError):
        load_config(missing_config_path)

def test_handle_invalid_config_file(setup_and_teardown):
    """Test handling an invalid configuration file."""
    _, invalid_config_path, _, _ = setup_and_teardown
    with open(invalid_config_path, 'w') as f:
        f.write("invalid json")
    with pytest.raises(json.JSONDecodeError):
        load_config(invalid_config_path)

def test_handle_missing_parameters_in_config(setup_and_teardown):
    """Test handling missing parameters in the configuration file."""
    _, invalid_config_path, _, _ = setup_and_teardown
    incomplete_config = {
        "database": {
            "host": "localhost",
            "port": 3306
        }
    }
    with open(invalid_config_path, 'w') as f:
        json.dump(incomplete_config, f)

    config = load_config(invalid_config_path)
    with pytest.raises(ValueError):
        validate_config_file(config)
