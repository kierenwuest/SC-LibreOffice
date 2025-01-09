import subprocess
import unittest

""" 
Purpose: Validate interactions with the Salesforce CLI.
Test Cases:
SF CLI is up to date (sf --version).
SF CLI commands execute successfully (e.g., sf org list).
Handle errors in CLI commands (e.g., invalid command).
"""

class TestSalesforceCLI(unittest.TestCase):
  
  def test_sf_cli_version(self):
    """Test that the Salesforce CLI is up to date."""
    result = subprocess.run(['sf', '--version'], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0)
    self.assertIn('sfdx-cli', result.stdout)

  def test_sf_cli_org_list(self):
    """Test that the Salesforce CLI can list orgs successfully."""
    result = subprocess.run(['sf', 'org', 'list'], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0)
    self.assertIn('No results found', result.stdout)  # Adjust based on expected output

  def test_sf_cli_invalid_command(self):
    """Test that the Salesforce CLI handles invalid commands gracefully."""
    result = subprocess.run(['sf', 'invalidcommand'], capture_output=True, text=True)
    self.assertNotEqual(result.returncode, 0)
    self.assertIn('Unknown command', result.stderr)  # Adjust based on expected error message

  def test_sf_cli_help(self):
    """Test that the Salesforce CLI help command works."""
    result = subprocess.run(['sf', '--help'], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0)
    self.assertIn('Usage:', result.stdout)

  def test_sf_cli_org_display(self):
    """Test that the Salesforce CLI can display org details."""
    result = subprocess.run(['sf', 'org', 'display', '--targetusername', 'my-org'], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0)
    self.assertIn('Access Token', result.stdout)  # Adjust based on expected output

if __name__ == '__main__':
  unittest.main()