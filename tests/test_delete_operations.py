import unittest
from unittest.mock import patch, MagicMock
from your_module import delete_records, update_spreadsheet

"""
Purpose: Validate deleting data from Salesforce.
Test Cases:
Delete records by Id or external identifier.
Update the spreadsheet after deletion (e.g., mark rows as "Deleted").
Handle errors when deleting data.
"""
class TestDeleteOperations(unittest.TestCase):

  @patch('your_module.salesforce_api')
  def test_delete_records_by_id(self, mock_salesforce_api):
    mock_salesforce_api.delete.return_value = {'success': True}
    result = delete_records(['001xx000003DGbYAAW'])
    self.assertTrue(result)
    mock_salesforce_api.delete.assert_called_with(['001xx000003DGbYAAW'])

  @patch('your_module.salesforce_api')
  def test_delete_records_by_external_id(self, mock_salesforce_api):
    mock_salesforce_api.delete_by_external_id.return_value = {'success': True}
    result = delete_records(['external_id_123'], use_external_id=True)
    self.assertTrue(result)
    mock_salesforce_api.delete_by_external_id.assert_called_with(['external_id_123'])

  @patch('your_module.spreadsheet')
  def test_update_spreadsheet_after_deletion(self, mock_spreadsheet):
    mock_spreadsheet.update.return_value = True
    result = update_spreadsheet(['001xx000003DGbYAAW'], status='Deleted')
    self.assertTrue(result)
    mock_spreadsheet.update.assert_called_with(['001xx000003DGbYAAW'], status='Deleted')

  @patch('your_module.salesforce_api')
  def test_handle_errors_when_deleting_data(self, mock_salesforce_api):
    mock_salesforce_api.delete.side_effect = Exception('Deletion error')
    with self.assertRaises(Exception) as context:
      delete_records(['001xx000003DGbYAAW'])
    self.assertEqual(str(context.exception), 'Deletion error')

if __name__ == '__main__':
  unittest.main()
