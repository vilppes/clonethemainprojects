from gitactions import GitActionsForMains
gafm = GitActionsForMains([],"https://github.com/vilppes/")
gafm.load_project_gits_from_a_prespecified_file()
gafm.set_project_names_without_having_to_insert_list()
def defined_actions(i) -> None:
    if i == 1:
        gafm.git_clone_all_projects()
    elif i == 2:
        gafm.git_pull_all_projects()
    elif i == 3:
        exit()
def input_by_loop() -> None:
    while True:
        i = int(input("what would you like to do? (1 = clone all, 2 = pull all, 3 = exit): "))
        defined_actions(i)
def input_by_list(li: list) -> None:
    for item in li:
        defined_actions(item)