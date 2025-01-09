import unittest
from unittest.mock import patch
from your_module import upsert_to_salesforce

"""
Purpose: Validate upserting data into Salesforce.
Test Cases:
Upsert using Salesforce Id.
Upsert using an external identifier (ExternalKey-API-Name).
Log success or failure in the "API Response" column.
"""
class TestUpsertOperations(unittest.TestCase):

  @patch('your_module.salesforce_api')
  def test_upsert_with_salesforce_id(self, mock_salesforce_api):
    mock_salesforce_api.upsert.return_value = {'success': True, 'id': '001xx000003DGbYAAW'}
    result = upsert_to_salesforce({'Id': '001xx000003DGbYAAW', 'Name': 'Test Account'})
    self.assertTrue(result['success'])
    self.assertEqual(result['id'], '001xx000003DGbYAAW')

  @patch('your_module.salesforce_api')
  def test_upsert_with_external_id(self, mock_salesforce_api):
    mock_salesforce_api.upsert.return_value = {'success': True, 'id': '001xx000003DGbYAAW'}
    result = upsert_to_salesforce({'ExternalKey__c': 'EXT123', 'Name': 'Test Account'})
    self.assertTrue(result['success'])
    self.assertEqual(result['id'], '001xx000003DGbYAAW')

  @patch('your_module.salesforce_api')
  def test_upsert_failure(self, mock_salesforce_api):
    mock_salesforce_api.upsert.return_value = {'success': False, 'errors': ['Invalid data']}
    result = upsert_to_salesforce({'ExternalKey__c': 'EXT123', 'Name': ''})
    self.assertFalse(result['success'])
    self.assertIn('Invalid data', result['errors'])

  @patch('your_module.salesforce_api')
  def test_log_success(self, mock_salesforce_api):
    mock_salesforce_api.upsert.return_value = {'success': True, 'id': '001xx000003DGbYAAW'}
    result = upsert_to_salesforce({'Id': '001xx000003DGbYAAW', 'Name': 'Test Account'})
    self.assertEqual(result['api_response'], 'Success')

  @patch('your_module.salesforce_api')
  def test_log_failure(self, mock_salesforce_api):
    mock_salesforce_api.upsert.return_value = {'success': False, 'errors': ['Invalid data']}
    result = upsert_to_salesforce({'ExternalKey__c': 'EXT123', 'Name': ''})
    self.assertEqual(result['api_response'], 'Failure: Invalid data')

if __name__ == '__main__':
  unittest.main()
