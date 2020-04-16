import os
import asana
import json

from argparse import ArgumentParser

def pprint(s):
    return json.dumps(s, indent=4, separators=(',',':'))


###########
# Main
###########
parser = ArgumentParser("Add task to 1on1 projects.")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

# create a client with a Personal Access Token
client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
me = client.users.me()


project_id = '1165398058700585'
REACH_GID = '1165398058700602'
IMPACT_GID = '1165398058700616'
CONFIDENCE_GID = '1165398058700597'
EFFORT_GID = '1165398058700624'

# project = client.projects.find_by_id(project_id)
# print(json.dumps(project, indent=4, separators=(',',':')))

reach_field = client.custom_fields.find_by_id(REACH_GID)
reach_options = {}
reach_map = {
    'S': 1,
    'M': 2, 
    'L': 8, 
    'XL': 16
}
for option in reach_field['enum_options']:
    reach_options[option['gid']] = reach_map[option['name']]

print(reach_options)
print(pprint(reach_field))

impact_field = client.custom_fields.find_by_id(IMPACT_GID)
impact_options = {}
impact_map = {
    'Massive 3x': 3,
    'High 2x': 2,
    'Medium 1x': 1, 
    'Low 0.5x': 0.5,
    'Minimal 0.25x': 0.25
}
for option in impact_field['enum_options']:
    impact_options[option['gid']] = impact_map[option['name']]

print(impact_options)
print(pprint(impact_field))

confidence_field = client.custom_fields.find_by_id(CONFIDENCE_GID)
confidence_options = {}
confidence_map = {
    '100%': 1.00,
    '80%': 0.80, 
    '50%': 0.50,
    '20%': 0.20, 
    'Needs Definition': 0
}
for option in confidence_field['enum_options']:
    confidence_options[option['gid']] = confidence_map[option['name']]

print(confidence_options)
print(pprint(confidence_field))

effort_field = client.custom_fields.find_by_id(EFFORT_GID)
effort_options = {}
effort_map = {
    'XS': 0.5,
    'S': 1,
    'M': 2, 
    'L': 3, 
    'XL': 4
}
for option in effort_field['enum_options']:
    effort_options[option['gid']] = effort_map[option['name']]

print(effort_options)
print(pprint(effort_field))

tasks = client.tasks.find_by_project(project_id, opt_fields=['name', 'custom_fields.enum_value'])

SCORE_GID = '1166544034612362'
for task in tasks:
    print(pprint(task))
    score = 1
    for field in task['custom_fields']:
        if field['gid'] == REACH_GID:
            if field['enum_value']:
                print('reach', reach_map[field['enum_value']['name']])
                score *= reach_map[field['enum_value']['name']]
            else:
                score *= 0
        elif field['gid'] == IMPACT_GID:
            if field['enum_value']:
                print('impact', impact_map[field['enum_value']['name']])
                score *= impact_map[field['enum_value']['name']]
            else:
                score *= 0

        elif field['gid'] == CONFIDENCE_GID:
            if field['enum_value']:
                print('confidence', confidence_map[field['enum_value']['name']])
                score *= confidence_map[field['enum_value']['name']]
            else:
                score *= 0
        elif field['gid'] == EFFORT_GID:
            if field['enum_value']:
                print('effort', effort_map[field['enum_value']['name']])
                score *= effort_map[field['enum_value']['name']]
            else:
                score *= 0
        print(score)
    client.tasks.update(task['gid'], {'custom_fields': {'1166544034612362': score}})



