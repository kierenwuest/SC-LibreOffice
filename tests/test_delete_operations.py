import pytest
from unittest.mock import patch, MagicMock
from your_module import delete_records, update_spreadsheet

"""
Purpose: Validate deleting data from Salesforce.
Test Cases:
Delete records by Id or external identifier.
Update the spreadsheet after deletion (e.g., mark rows as "Deleted").
Handle errors when deleting data.
"""

@patch('your_module.salesforce_api')
def test_delete_records_by_id(mock_salesforce_api):
  mock_salesforce_api.delete.return_value = {'success': True}
  result = delete_records(['001xx000003DGbYAAW'])
  assert result
  mock_salesforce_api.delete.assert_called_with(['001xx000003DGbYAAW'])

@patch('your_module.salesforce_api')
def test_delete_records_by_external_id(mock_salesforce_api):
  mock_salesforce_api.delete_by_external_id.return_value = {'success': True}
  result = delete_records(['external_id_123'], use_external_id=True)
  assert result
  mock_salesforce_api.delete_by_external_id.assert_called_with(['external_id_123'])

@patch('your_module.spreadsheet')
def test_update_spreadsheet_after_deletion(mock_spreadsheet):
  mock_spreadsheet.update.return_value = True
  result = update_spreadsheet(['001xx000003DGbYAAW'], status='Deleted')
  assert result
  mock_spreadsheet.update.assert_called_with(['001xx000003DGbYAAW'], status='Deleted')

@patch('your_module.salesforce_api')
def test_handle_errors_when_deleting_data(mock_salesforce_api):
  mock_salesforce_api.delete.side_effect = Exception('Deletion error')
  with pytest.raises(Exception) as excinfo:
    delete_records(['001xx000003DGbYAAW'])
  assert str(excinfo.value) == 'Deletion error'
