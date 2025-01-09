import pytest
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

@patch('org_management.fetch_orgs')
def test_fetch_and_display_connected_orgs(mock_fetch_orgs):
  mock_fetch_orgs.return_value = [{'name': 'Org1'}, {'name': 'Org2'}]
  orgs = org_management.fetch_orgs()
  assert len(orgs) == 2
  assert orgs[0]['name'] == 'Org1'
  assert orgs[1]['name'] == 'Org2'

@patch('org_management.set_working_org')
def test_set_working_org(mock_set_working_org):
  mock_set_working_org.return_value = {'name': 'Org1'}
  org = org_management.set_working_org('Org1')
  assert org['name'] == 'Org1'

@patch('org_management.get_working_org_details')
def test_retrieve_working_org_details_and_limits(mock_get_working_org_details):
  mock_get_working_org_details.return_value = {'name': 'Org1', 'limits': {'api_calls': 100}}
  details = org_management.get_working_org_details()
  assert details['name'] == 'Org1'
  assert details['limits']['api_calls'] == 100

@patch('org_management.authenticate_org')
def test_authenticate_new_salesforce_org(mock_authenticate_org):
  mock_authenticate_org.return_value = {'name': 'Org1', 'status': 'Authenticated'}
  org = org_management.authenticate_org('Org1')
  assert org['name'] == 'Org1'
  assert org['status'] == 'Authenticated'

@patch('org_management.fetch_orgs')
def test_handle_errors_when_fetching_orgs(mock_fetch_orgs):
  mock_fetch_orgs.side_effect = Exception('Error fetching orgs')
  with pytest.raises(Exception) as excinfo:
    org_management.fetch_orgs()
  assert 'Error fetching orgs' in str(excinfo.value)
