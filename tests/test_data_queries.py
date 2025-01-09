import unittest
from unittest.mock import patch, MagicMock
from your_module import query_salesforce_data, populate_spreadsheet

"""
Purpose: Validate querying Salesforce data and populating spreadsheets.
Test Cases:
Query data using SOQL.
Populate multiple tabs with data for different objects.
Handle errors when querying data.
Append API responses to data rows in the spreadsheet.
"""
class TestDataQueries(unittest.TestCase):

  @patch('your_module.salesforce_api.query')
  def test_query_data_using_soql(self, mock_query):
    mock_query.return_value = {'records': [{'Id': '001', 'Name': 'Test Account'}]}
    result = query_salesforce_data('SELECT Id, Name FROM Account')
    self.assertEqual(result, [{'Id': '001', 'Name': 'Test Account'}])
    mock_query.assert_called_once_with('SELECT Id, Name FROM Account')

  @patch('your_module.salesforce_api.query')
  def test_handle_errors_when_querying_data(self, mock_query):
    mock_query.side_effect = Exception('API Error')
    with self.assertRaises(Exception) as context:
      query_salesforce_data('SELECT Id, Name FROM Account')
    self.assertTrue('API Error' in str(context.exception))
    mock_query.assert_called_once_with('SELECT Id, Name FROM Account')

  @patch('your_module.populate_spreadsheet')
  def test_populate_multiple_tabs_with_data(self, mock_populate):
    data = {
      'Account': [{'Id': '001', 'Name': 'Test Account'}],
      'Contact': [{'Id': '002', 'Name': 'Test Contact'}]
    }
    populate_spreadsheet(data)
    self.assertEqual(mock_populate.call_count, 1)
    mock_populate.assert_called_once_with(data)

  @patch('your_module.salesforce_api.query')
  @patch('your_module.append_to_spreadsheet')
  def test_append_api_responses_to_data_rows(self, mock_append, mock_query):
    mock_query.return_value = {'records': [{'Id': '001', 'Name': 'Test Account'}]}
    data = query_salesforce_data('SELECT Id, Name FROM Account')
    append_to_spreadsheet(data)
    mock_append.assert_called_once_with(data)

if __name__ == '__main__':
  unittest.main()
