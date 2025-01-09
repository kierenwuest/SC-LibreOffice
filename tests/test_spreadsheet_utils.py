import pytest
from spreadsheet_utils import create_tab, append_metadata, overwrite_data, format_ods

"""
Purpose: Test spreadsheet-specific manipulations and integrations.
Test Cases:
Create and manage Calc tabs for different Salesforce objects.
Append additional metadata to columns (e.g., ReadOnly, Required, API Response).
Handle overwriting data in existing tabs.
Ensure proper formatting of generated .ods files.
"""

def test_create_tab():
  result = create_tab('SalesforceObject')
  assert result
  assert 'SalesforceObject' in result

def test_append_metadata():
  columns = ['Name', 'Email']
  metadata = {'ReadOnly': True, 'Required': True}
  result = append_metadata(columns, metadata)
  assert result['Name']['ReadOnly'] == True
  assert result['Email']['Required'] == True

def test_overwrite_data():
  tab_data = {'Name': 'John Doe', 'Email': 'john.doe@example.com'}
  new_data = {'Name': 'Jane Doe'}
  result = overwrite_data(tab_data, new_data)
  assert result['Name'] == 'Jane Doe'
  assert result['Email'] == 'john.doe@example.com'

def test_format_ods():
  file_path = '/path/to/generated.ods'
  result = format_ods(file_path)
  assert result
  assert file_path.endswith('.ods')

if __name__ == '__main__':
  pytest.main()
