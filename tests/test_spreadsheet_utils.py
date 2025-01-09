import unittest
from spreadsheet_utils import create_tab, append_metadata, overwrite_data, format_ods

"""
Purpose: Test spreadsheet-specific manipulations and integrations.
Test Cases:
Create and manage Calc tabs for different Salesforce objects.
Append additional metadata to columns (e.g., ReadOnly, Required, API Response).
Handle overwriting data in existing tabs.
Ensure proper formatting of generated .ods files.
"""
class TestSpreadsheetUtils(unittest.TestCase):

  def test_create_tab(self):
    result = create_tab('SalesforceObject')
    self.assertTrue(result)
    self.assertIn('SalesforceObject', result)

  def test_append_metadata(self):
    columns = ['Name', 'Email']
    metadata = {'ReadOnly': True, 'Required': True}
    result = append_metadata(columns, metadata)
    self.assertEqual(result['Name']['ReadOnly'], True)
    self.assertEqual(result['Email']['Required'], True)

  def test_overwrite_data(self):
    tab_data = {'Name': 'John Doe', 'Email': 'john.doe@example.com'}
    new_data = {'Name': 'Jane Doe'}
    result = overwrite_data(tab_data, new_data)
    self.assertEqual(result['Name'], 'Jane Doe')
    self.assertEqual(result['Email'], 'john.doe@example.com')

  def test_format_ods(self):
    file_path = '/path/to/generated.ods'
    result = format_ods(file_path)
    self.assertTrue(result)
    self.assertTrue(file_path.endswith('.ods'))

if __name__ == '__main__':
  unittest.main()
