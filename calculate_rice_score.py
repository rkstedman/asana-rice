import os
import asana

from argparse import ArgumentParser

# projects is an array of objects in the following format

# projects = [
#     { 'name': 'KateTest',         #user-friendly name
#       'id': '<projectId>',        # string, project id
#       'userid': '<userEmail>',    # string, email address of the other user who should be assigned tasks in this project
#       'group': 'self'},            # group name. matches list of groups
# ]

def get_user_selected_group(groups):
    """Prompt user to select project group."""

    for i, group in enumerate(groups):
        print i, ': ' + group
    print i + 1, ': all'
    print i + 2, ': choose'

    return raw_input('Select (name) which projects or groups to add task to: ')


def get_user_task_title():
    "Prompt user for task title, and return result."

    return raw_input("Enter task title: ")

def get_user_task_description():
    """Prompt user for task description. return as a string."""

    print("Enter task description: (Ctrl-D to finish)")
    contents = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        contents.append(line)
    return '\n'.join(contents)


def get_projects_by_user_select(projects):
    """Prompts the user for each project to determine whether to add task to that project.

    :param projects: (list) all projects for the user to select from
    :return: (list) all projects selected by the user
    """

    selected_projects = []
    for project in projects:
        add_to_project = raw_input('Add to ' + project['name'] + ' [y/n]? ')
        if(add_to_project == 'y'):
            selected_projects.append(project)
    return selected_projects


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
project = client.projects.find_by_id(project_id, opt_fields=['effort', 'confidence', '1165398058700602'])
print(project)
tasks = client.tasks.find_by_project(project_id)

for task in tasks:
    print(task)
    print(task['name'])




