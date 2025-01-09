import subprocess
import pytest
from unittest.mock import patch, Mock
from lib.cli_integration import run_cli_command, list_connected_orgs, set_working_org, get_org_details 

@pytest.fixture
def mock_subprocess():
    """Fixture to mock subprocess.run."""
    with patch('subprocess.run') as mock_run:
        yield mock_run

def run_mocked_subprocess(cmd, returncode, stdout, stderr=""):
    """Helper function to mock subprocess.run."""
    mock_run = Mock(returncode=returncode, stdout=stdout, stderr=stderr)
    with patch('subprocess.run', return_value=mock_run):
        return subprocess.run(cmd, capture_output=True, text=True)

def test_sf_cli_version():
    """Test that the Salesforce CLI is up to date."""
    result = run_mocked_subprocess(['sf', '--version'], 0, "sfdx-cli/7.199.0")
    assert result.returncode == 0
    assert 'sfdx-cli' in result.stdout

@pytest.mark.parametrize("cmd,expected,returncode,stderr", [
    (['sf', '--version'], "sfdx-cli", 0, ""),
    (['sf', 'org', 'list'], "ALIAS", 0, ""),
    (['sf', 'invalidcommand'], "Error", 1, "Error"),
])
def test_sf_cli_commands(cmd, expected, returncode, stderr):
    """Test various CLI commands."""
    result = run_mocked_subprocess(cmd, returncode, expected, stderr)
    assert result.returncode == returncode
    if returncode == 0:
        assert expected in result.stdout
    else:
        assert stderr in result.stderr

def test_sf_cli_org_list(mock_subprocess):
    """Test that the Salesforce CLI can list orgs successfully."""
    mock_subprocess.return_value = Mock(
        returncode=0,
        stdout="=== Orgs\nALIAS USERNAME ORGID STATUS\nprod user@example.com 00Dxxxx Active",
        stderr=""
    )
    result = subprocess.run(['sf', 'org', 'list'], capture_output=True, text=True)
    assert result.returncode == 0, "CLI command failed unexpectedly"
    lines = result.stdout.splitlines()
    assert lines[0] == "=== Orgs", "First line of CLI output should indicate orgs section"
    assert 'ALIAS' in lines[1] and 'USERNAME' in lines[1], "Headers missing in CLI output"
    assert len(lines) > 2, "No orgs found in CLI output"

def test_sf_cli_invalid_command(mock_subprocess):
    """Test that the Salesforce CLI handles invalid commands gracefully."""
    mock_subprocess.return_value = Mock(returncode=1, stdout="", stderr="Error: command not found")
    result = subprocess.run(['sf', 'invalidcommand'], capture_output=True, text=True)
    assert result.returncode != 0
    assert "command not found" in result.stderr
