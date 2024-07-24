import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

import init
from kivy.uix.label import Label

kivy_version = kivy.version
print("Kivy version:", kivy_version)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup

import oracledb

class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''
    def printo(self, t):
        print(t)

class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def on_press(self):
        popup = TextInputPopup(self)
        popup.open()

    def update_changes(self, txt):
        self.text = txt
        try:
            print("hi bro")
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            con.commit()

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle ROOT", e)


class Prim1Button(Button):
    pass
class Prim2Button(Button):
    pass

class MBranch(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(MBranch, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.get_users()
        self.current_id = '0'
        self.Header = Button(text = 'BRANCH DATABASE', size_hint = (1, 0.1))
        self.add_widget(self.Header)
        self.Scroll = ScrollView()
        self.add_widget(self.Scroll)
        self.View = GridLayout()
        self.View.cols = 6
        self.Scroll.add_widget(self.View)

        self.get_users()

        self.temp1 = 0
        for i in self.data_items:
            if (self.temp1%6 == 0):
                temp1 = Prim1Button(text = str(i))
            else:
                temp1 = Label(text = str(i))
            self.View.add_widget(temp1)
            self.temp1 += 1

    def get_users(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()

            cursor.execute("SELECT * FROM branch ORDER BY branch_id ASC")
            rows = cursor.fetchall()

            # create data_items
            for row in rows:
                for col in row:
                    self.data_items.append(col)
        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle", e)

class MEmployee(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(MEmployee, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.get_users()
        self.current_id = '0'
        self.Header = Button(text = 'EMPLOYEE DATABASE', size_hint = (1, 0.1))
        self.add_widget(self.Header)
        self.Scroll = ScrollView()
        self.add_widget(self.Scroll)
        self.View = GridLayout()
        self.View.cols = 6
        self.Scroll.add_widget(self.View)

        self.get_users()

        self.temp1 = 0
        for i in self.data_items:
            if (self.temp1%6 == 0):
                temp1 = Prim1Button(text = str(i))
            else:
                temp1 = Label(text = str(i))
            self.View.add_widget(temp1)
            self.temp1 += 1

    def get_users(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()

            cursor.execute("SELECT * FROM employee ORDER BY emp_id ASC")
            rows = cursor.fetchall()

            # create data_items
            for row in rows:
                for col in row:
                    self.data_items.append(col)
        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle", e)


class MyApp(App):
    title = 'Storage Company Database'
    def build(self):
        return RootLayout()

    def on_submit(self, instance):
        text = instance.manager.get('text_input').text
        print("Text input value:", text)

class TableListLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (0.2, 1)
        self.padding = 5

class IP(TextInput):
    pass

class CommitButton(Button):
    pass

class EmployeeInfoView(BoxLayout):
    recordData = []
    id : str
    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.id =  id
        self.orientation = 'vertical'
        self.size_hint = (0.5,1)
        self.padding = 1

        self.rowCount = 0
        self.getRowCount()

        self.widgets = []
        self.widgets.append(Button(text = f'EMPLOYEE', size_hint = (1,0.1)))
        self.widgets.append(Button(text = f'Record Count : {self.rowCount}', size_hint = (1, 0.1)))

        self.record_select()

        self.sublayouts = []

        for i in range(0,6):
            self.sublayouts.append(BoxLayout(size_hint = (1,0.5)))

        self.sublayouts[0].add_widget(Button(text = 'ID', size_hint = (0.5, 1)))
        self.sublayouts[0].add_widget(Button(text = self.recordData[0], size_hint = (0.5, 1)))
        self.sublayouts[1].add_widget(Button(text = 'NAME', size_hint = (0.5, 1)))
        self.sublayouts[1].add_widget(IP(text = self.recordData[1], size_hint = (0.5, 1)))
        self.sublayouts[2].add_widget(Button(text = 'DEPT', size_hint = (0.5, 1)))
        self.sublayouts[2].add_widget(IP(text = self.recordData[2], size_hint = (0.5, 1)))
        self.sublayouts[3].add_widget(Button(text = 'SALARY', size_hint = (0.5, 1)))
        self.sublayouts[3].add_widget(IP(text = self.recordData[3], size_hint = (0.5, 1)))
        self.sublayouts[4].add_widget(Button(text = 'ADDRESS', size_hint = (0.5, 1)))
        self.sublayouts[4].add_widget(IP(text = self.recordData[4], size_hint = (0.5, 1)))
        self.sublayouts[5].add_widget(Button(text = 'BRANCH', size_hint = (0.5, 1)))
        self.sublayouts[5].add_widget(IP(text = self.recordData[5], size_hint = (0.5, 1)))

        for i in range(0,6):
            self.widgets.append(self.sublayouts[i])

        #self.widgets.append(CommitButton(text='COMMIT', size_hint = (1, 0.5)))

        for w in self.widgets:
            self.add_widget(w)

    def updateRecordData(self, id):
        pass

    def record_select(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            self.record = cursor.execute(f'select * from employee where emp_id = {self.id}')
            for row in self.record:
                for col in row:
                    self.recordData.append(str(col))

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)

    def record_commit(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            print(self.recordData[1])
            #cursor.execute(f'update employee set emp_name = {str(self.recordData[1])} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_dept = {self.recordData[2]} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_sal = {self.recordData[3]} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_add = {self.recordData[4]} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_branch = {self.recordData[5]} where emp_id = {self.recordData[0]}')

            con.commit()
        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)

    def getRowCount(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            val = cursor.execute('select COUNT(distinct emp_id) from employee')
            for col in val:
                self.rowCount = col[0]

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)
            self.rowCount = 0

class BranchInfoView(BoxLayout):
    recordData = []
    id : str
    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.id =  id
        self.orientation = 'vertical'
        self.size_hint = (0.5,1)
        self.padding = 1

        self.rowCount = 0
        self.getRowCount()

        self.widgets = []
        self.widgets.append(Button(text = f'BRANCH', size_hint = (1,0.1)))
        self.widgets.append(Button(text = f'Record Count : {self.rowCount}', size_hint = (1, 0.1)))

        self.record_select()

        self.sublayouts = []

        for i in range(0,6):
            self.sublayouts.append(BoxLayout(size_hint = (1,0.5)))

        self.sublayouts[0].add_widget(Button(text = 'ID', size_hint = (0.5, 1)))
        self.sublayouts[0].add_widget(Button(text = self.recordData[0], size_hint = (0.5, 1)))
        self.sublayouts[1].add_widget(Button(text = 'ADDRESS', size_hint = (0.5, 1)))
        self.sublayouts[1].add_widget(IP(text = self.recordData[1], size_hint = (0.5, 1)))
        self.sublayouts[2].add_widget(Button(text = 'BUDGET', size_hint = (0.5, 1)))
        self.sublayouts[2].add_widget(IP(text = self.recordData[2], size_hint = (0.5, 1)))

        for i in range(0,6):
            self.widgets.append(self.sublayouts[i])

        #self.widgets.append(CommitButton(text='COMMIT', size_hint = (1, 0.5)))

        for w in self.widgets:
            self.add_widget(w)

    def updateRecordData(self, id):
        pass

    def record_select(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            self.record = cursor.execute(f'select * from branch where branch_id = {self.id}')
            for row in self.record:
                for col in row:
                    self.recordData.append(str(col))

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)

    def record_commit(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            print(self.recordData[1])
            #cursor.execute(f'update employee set emp_name = {str(self.recordData[1])} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_dept = {self.recordData[2]} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_sal = {self.recordData[3]} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_add = {self.recordData[4]} where emp_id = {self.recordData[0]}')
            #cursor.execute(f'update employee set emp_branch = {self.recordData[5]} where emp_id = {self.recordData[0]}')

            con.commit()
        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)

    def getRowCount(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            val = cursor.execute('select COUNT(distinct emp_id) from employee')
            for col in val:
                self.rowCount = col[0]

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)
            self.rowCount = 0



class RootLayout(BoxLayout):
    pk1 : str = ''
    pk2 : str = ''
    new_layout = BoxLayout()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.currentTable = 0 # 0-emp 1-branch 2-clicomp 3-trans 4-shipment 5-ware 6-invoice 7-emphier 8-doc
        self.offset = 0

        self.rightLayouts = []
        self.rightLayouts.append(BoxLayout())
        self.middleLayouts = []
        self.middleLayouts.append(MEmployee())
        self.middleLayouts.append(MBranch())

        self.LeftLayout = TableListLayout()
        self.MiddleLayout = self.middleLayouts[0]
        self.RightLayout = self.rightLayouts[0]

        self.add_widget(self.LeftLayout)
        self.add_widget(self.MiddleLayout)
        self.add_widget(self.RightLayout)

    testext = StringProperty('123')
    def updateChanges(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)

    def rootRecordSelected(self, id):
        self.new_layout = None
        self.new_layout = EmployeeInfoView(id)
        self.remove_widget(self.RightLayout)
        self.RightLayout = self.new_layout
        self.add_widget((self.RightLayout))
        print(123)

    def consoleProcedure(self):
        try:
            con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
            cursor = con.cursor()
            cursor.execute('declare begin low_wage(100000); end;/')

        except oracledb.DatabaseError as e:
            print("There is a problem with Oracle emp", e)


if __name__ == "__main__":
    init.createTables()
    init.insertRecords()
    app = MyApp()
    app.run()
