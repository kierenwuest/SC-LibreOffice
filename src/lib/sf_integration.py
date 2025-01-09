# Implement Salesforce CLI integration.

import subprocess
import json

def get_org_list():
    try:
        result = subprocess.run(
            ["sf", "org", "list", "--json"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output = json.loads(result.stdout)
        return output.get("result", [])
    except Exception as e:
        print(f"Error fetching orgs: {e}")
        return []