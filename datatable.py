from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from database import Database

db = Database(host='localhost', user='root', password='', database='todo')
 
class DataTableApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        layout = AnchorLayout()
        data_table = MDDataTable(
            size_hint=(0.9, 0.6), 
            pos_hint={"center_x": 0.5, "center_y": 0.5},  
            check=True,
            rows_num=10,
            column_data=[
                ("ID", dp(30)),
                ("Task", dp(120)),
                ("Status", dp(100)),
            ],
            row_data=self.get_tasks(),
        )
        layout.add_widget(data_table)
        return layout

    def get_tasks(self):
        tasks = db.get_task() #cinall ko yung function from database.py
        db.close_db_connection()
        return [(task[0], task[1], "Complete" if task[3] == 1 else "Incomplete") for task in tasks]

if __name__ == "__main__":
    DataTableApp().run()
