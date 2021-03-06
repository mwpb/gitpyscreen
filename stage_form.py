import npyscreen
import sqlite_utils
import git_utils
import curses

class stage_multiselect(npyscreen.MultiSelect):
    def set_up_handlers(self):
        super(stage_multiselect,self).set_up_handlers()
        self.handlers.update({curses.ascii.SP:self.toggle_then_down})
    def toggle_then_down(self,input):
        self.h_select_toggle(self)
        self.h_cursor_line_down(self)
    pass

class StageForm(npyscreen.ActionForm):
    def create(self,*args,**keywords):
        self.name = "Staging Area"
        self.repo_name = ''
        self.repo_path = ''
        self.stage_multiselect = self.add(stage_multiselect,name='stage',value=0)
    def set_up_handlers(self):
        super(StageForm,self).set_up_handlers()
        self.handlers.update({"q": self.previous_form})
    def previous_form(self,input):
        self.parentApp.switchFormPrevious()
    def on_cancel(self):
        self.parentApp.setNextFormPrevious()
    def on_ok(self):
        file_list = [self.repo_path+i for i in self.stage_multiselect.get_selected_objects()]
        self.parentApp.getForm('COMMIT').repo_path = self.repo_path
        self.parentApp.getForm('COMMIT').repo_name = self.repo_name
        self.parentApp.getForm('COMMIT').file_list = file_list
        self.parentApp.getForm('COMMIT').commit_message.value = ''
        self.parentApp.setNextForm('COMMIT')
