# Create a simple modal to manage Salesforce orgs.

from src.lib.sf_integration import get_org_list

def show_config_modal(doc):
    orgs = get_org_list()
    print("Connected Orgs:")
    for org in orgs:
        print(f"- {org['Alias']} ({org['Username']})")