import os
import asana
import json

def pprint(s):
    return json.dumps(s, indent=4, separators=(',',':'))

with open("project_values.json", "r") as read_file:
    project_values = json.load(read_file)

PROJECT_ID = project_values['project_id']
SCORE_GID = project_values['score_gid']

scored_field_maps = {
    project_values['reach_gid']: project_values['reach_map'],
    project_values['impact_gid']: project_values['impact_map'],
    project_values['confidence_gid']: project_values['confidence_map'],
    project_values['effort_gid']: project_values['effort_map'],
}

###########
# Main
###########

# create a client with a Personal Access Token
client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
me = client.users.me()

tasks = client.tasks.find_by_project(PROJECT_ID, opt_fields=['name', 'custom_fields.enum_value'])

print(f'calculating scores...')
scores_calculated = 0
for task in tasks:
    score = 1
    for field in task['custom_fields']:
        gid = field['gid']
    
        if gid in scored_field_maps:
            scored_field = scored_field_maps[gid]
            value = field['enum_value']
            if value:
                score *= scored_field[value['name']]
            else:
                score *= 0

    client.tasks.update(task['gid'], {'custom_fields': {SCORE_GID: score}})
    scores_calculated += 1
    if scores_calculated % 5 == 0:
        print(f"{scores_calculated} scores have been calculated...")

print('Complete!')
