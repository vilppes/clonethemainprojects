import os
#TODO: create this for linux terminals too
class GitActionsForMains:
    def __init__(self,projects: list,base_git: str) -> None:
        self.project_gits = projects
        self.project_names = []
        self.base_git = base_git
    def set_project_names(self,project_gits: list) -> list:
        for pgit in project_gits:
            self.project_names.append(self.make_a_project_name(pgit)[0]+"-"+self.make_a_project_name(pgit)[1])
    def make_a_project_name(self,project_git: str) -> str:
        pgit1 = project_git.split(self.base_git)[1]
        pgit2 = pgit1.split(",")
        return pgit2
    def get_project_names(self) -> list:
        return self.project_names
    def get_project_gits(self) -> list:
        return self.project_gits
    def set_project_names_without_having_to_insert_list(self) -> None:
        self.set_project_names(self.project_gits)
    def get_project_names_without_having_to_call_set_function_separately(self) -> list:
        self.set_project_names_without_having_to_insert_list()
        return self.get_project_names()
    def git_pull_all_projects(self) -> None:
        for project_name in self.project_names:
            self.format_and_run_command("cd .. & cd "+project_name+" & "+"git pull")
    def format_command(self,command):
        return 'cmd /c "{}"'.format(command)
    def run_command(self,command):
        os.system(command)
    def format_and_run_command(self,command):
        self.run_command(self.format_command(command))
    def git_clone_all_projects(self) -> None:
        for project in self.project_gits:
            self.git_clone_a_project(self.make_a_project_name(project))
    def git_clone_a_project(self,pgit2):
        command = "cd .. & git clone "
        if int(pgit2[2]) == 1:
            command += "--recursive "
        command += self.base_git + pgit2[0] + " "
        if pgit2[1] != "main" and pgit2[1] != "master":
            command += "--branch "+pgit2[1]+" "
        command += pgit2[0]+"-"+pgit2[1]
        self.format_and_run_command(command)
    def load_project_gits_from_file(self,file: str) -> None:
        for line in self.open_file(file):
            self.project_gits.append(line)
    def open_file(self,file) -> list[str]:
        with open(file,"r") as f:
            lines = f.readlines()
            return lines
    def write_file(self,file,lines) -> None:
        with open(file,"a") as f:
            f.writelines(lines)
    def add_line_to_file(self,file,line) -> None:
        self.write_file(file,"\n"+line)
    def load_project_gits_from_a_prespecified_file(self):
        self.load_project_gits_from_file("projectlist.txt")