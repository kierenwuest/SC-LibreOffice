import pytest
from unittest.mock import patch
from your_module import upsert_to_salesforce

"""
Purpose: Validate upserting data into Salesforce.
Test Cases:
Upsert using Salesforce Id.
Upsert using an external identifier (ExternalKey-API-Name).
Log success or failure in the "API Response" column.
"""

@patch('your_module.salesforce_api')
def test_upsert_with_salesforce_id(mock_salesforce_api):
  mock_salesforce_api.upsert.return_value = {'success': True, 'id': '001xx000003DGbYAAW'}
  result = upsert_to_salesforce({'Id': '001xx000003DGbYAAW', 'Name': 'Test Account'})
  assert result['success'] is True
  assert result['id'] == '001xx000003DGbYAAW'

@patch('your_module.salesforce_api')
def test_upsert_with_external_id(mock_salesforce_api):
  mock_salesforce_api.upsert.return_value = {'success': True, 'id': '001xx000003DGbYAAW'}
  result = upsert_to_salesforce({'ExternalKey__c': 'EXT123', 'Name': 'Test Account'})
  assert result['success'] is True
  assert result['id'] == '001xx000003DGbYAAW'

@patch('your_module.salesforce_api')
def test_upsert_failure(mock_salesforce_api):
  mock_salesforce_api.upsert.return_value = {'success': False, 'errors': ['Invalid data']}
  result = upsert_to_salesforce({'ExternalKey__c': 'EXT123', 'Name': ''})
  assert result['success'] is False
  assert 'Invalid data' in result['errors']

@patch('your_module.salesforce_api')
def test_log_success(mock_salesforce_api):
  mock_salesforce_api.upsert.return_value = {'success': True, 'id': '001xx000003DGbYAAW'}
  result = upsert_to_salesforce({'Id': '001xx000003DGbYAAW', 'Name': 'Test Account'})
  assert result['api_response'] == 'Success'

@patch('your_module.salesforce_api')
def test_log_failure(mock_salesforce_api):
  mock_salesforce_api.upsert.return_value = {'success': False, 'errors': ['Invalid data']}
  result = upsert_to_salesforce({'ExternalKey__c': 'EXT123', 'Name': ''})
  assert result['api_response'] == 'Failure: Invalid data'
