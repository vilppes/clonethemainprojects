import os
#TODO: create this for linux terminals too
class GitActionsForMains:
    def __init__(self,projects: list,base_git: str) -> None:
        self.project_gits = projects
        self.project_names = []
        self.base_git = base_git
    def set_project_names(self,project_gits: list) -> list:
        for pgit in project_gits:
            pgit1 = pgit.split(self.base_git)[1]
            pgit2 = pgit1.split(",")
            self.project_names.append(pgit2[0]+"-"+pgit2[1])
    def get_project_names(self) -> list:
        return self.project_names
    def get_project_gits(self) -> list:
        return self.project_gits
    def set_project_names_without_having_to_insert_list(self) -> None:
        self.set_project_names(self.project_gits)
    def get_project_names_without_having_to_call_set_function_separately(self) -> list:
        self.set_project_names_without_having_to_insert_list()
        return self.get_project_names()
    def git_pull_all_projects(self):
        for project_name in self.project_names:
            command = "cd .. & cd "+project_name+" & "+"git pull"
            command2 = 'cmd /c "{}"'.format(command)
            os.system(command2)
    