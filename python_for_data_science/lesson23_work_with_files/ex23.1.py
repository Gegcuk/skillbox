import os


def print_dirs(project):
    print('\nContent of folder: ', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('    ', path)


projects_list = ['skillbox', 'probe', 'testProject1']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', '..', i_project))
    print_dirs(path_to_project)