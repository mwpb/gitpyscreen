import npyscreen
import sqlite_utils
import git_utils

class merge_selectone(npyscreen.SelectOne):
    pass

class merge_fixedText(npyscreen.FixedText):
    pass

class MergeForm(npyscreen.ActionForm):
    def create(self,*args,**keywords):
        self.repo_path = ''
        self.current_branch = ''
        self.repo_name = ''
        self.branch_list = []
        self.merge_fixedText = self.add(merge_fixedText,value='')
        self.merge_selectone = self.add(merge_selectone,name='merge',values=[])
    def beforeEditing(self):
        self.merge_fixedText.value = 'Current branch is %s. Please select branch to merge with:' % self.current_branch
    def on_cancel(self):
        self.parentApp.switchFormPrevious()
    def on_ok(self):
        git_utils.merge_current(self.repo_path,self.merge_selectone.values[self.merge_selectone.cursor_line])
        self.parentApp.switchFormPrevious()
 
