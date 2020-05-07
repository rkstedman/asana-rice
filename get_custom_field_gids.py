import os
import asana
import json

# create a client with a Personal Access Token
client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
me = client.users.me()

# PUT YOUR PROJECT ID HERE - find in the project url! https://app.asana.com/0/PROJECT_ID/list
PROJECT_ID = ""
project = client.projects.find_by_id(PROJECT_ID)
print(json.dumps(project['custom_field_settings'], indent=4, separators=(',',':')))

# TODO
# pull out reach, impact, confidence and effort custom field gids automatically!