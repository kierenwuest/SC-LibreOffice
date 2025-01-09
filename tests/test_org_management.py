import unittest
from unittest.mock import patch, MagicMock

""" 
Purpose: Test viewing, setting, and managing Salesforce orgs.
Test Cases:
Fetch and display connected orgs (sf org list).
Set a working org (sf org display).
Retrieve working org details and limits.
Authenticate a new Salesforce org (sf org login web).
Handle errors when fetching orgs.
"""
class TestOrgManagement(unittest.TestCase):

  @patch('org_management.fetch_orgs')
  def test_fetch_and_display_connected_orgs(self, mock_fetch_orgs):
    mock_fetch_orgs.return_value = [{'name': 'Org1'}, {'name': 'Org2'}]
    orgs = org_management.fetch_orgs()
    self.assertEqual(len(orgs), 2)
    self.assertEqual(orgs[0]['name'], 'Org1')
    self.assertEqual(orgs[1]['name'], 'Org2')

  @patch('org_management.set_working_org')
  def test_set_working_org(self, mock_set_working_org):
    mock_set_working_org.return_value = {'name': 'Org1'}
    org = org_management.set_working_org('Org1')
    self.assertEqual(org['name'], 'Org1')

  @patch('org_management.get_working_org_details')
  def test_retrieve_working_org_details_and_limits(self, mock_get_working_org_details):
    mock_get_working_org_details.return_value = {'name': 'Org1', 'limits': {'api_calls': 100}}
    details = org_management.get_working_org_details()
    self.assertEqual(details['name'], 'Org1')
    self.assertEqual(details['limits']['api_calls'], 100)

  @patch('org_management.authenticate_org')
  def test_authenticate_new_salesforce_org(self, mock_authenticate_org):
    mock_authenticate_org.return_value = {'name': 'Org1', 'status': 'Authenticated'}
    org = org_management.authenticate_org('Org1')
    self.assertEqual(org['name'], 'Org1')
    self.assertEqual(org['status'], 'Authenticated')

  @patch('org_management.fetch_orgs')
  def test_handle_errors_when_fetching_orgs(self, mock_fetch_orgs):
    mock_fetch_orgs.side_effect = Exception('Error fetching orgs')
    with self.assertRaises(Exception) as context:
      org_management.fetch_orgs()
    self.assertTrue('Error fetching orgs' in str(context.exception))

if __name__ == '__main__':
  unittest.main()
