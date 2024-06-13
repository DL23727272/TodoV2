import mysql.connector
from mysql.connector import Error
import hashlib

class Database:
    def __init__(self, host, user, password, database):
        try:
            self.con = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.con.cursor()
            self.create_task_table()
            self.create_user_table()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def create_task_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task VARCHAR(50) NOT NULL,
            due_date VARCHAR(50),
            completed BOOLEAN NOT NULL
        )
        '''
        self.cursor.execute(create_table_query)
        self.con.commit()

    def create_user_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        '''
        self.cursor.execute(create_table_query)
        self.con.commit()

    def create_task(self, task, due_date=None):
        try:
            insert_task_query = "INSERT INTO tasks(task, due_date, completed) VALUES(%s, %s, %s)"
            self.cursor.execute(insert_task_query, (task, due_date, 0))
            self.con.commit()

            last_inserted_id = self.cursor.lastrowid

            created_task_query = "SELECT id, task, due_date FROM tasks WHERE id = %s"
            self.cursor.execute(created_task_query, (last_inserted_id,))
            created_task = self.cursor.fetchone()

            return created_task
        except Error as e:
            print(f"Error creating task: {e}")
            return None

    def get_tasks(self):
        try:
            complete_tasks_query = "SELECT id, task, due_date FROM tasks WHERE completed = 0"
            incomplete_tasks_query = "SELECT id, task, due_date FROM tasks WHERE completed = 1"

            self.cursor.execute(complete_tasks_query)
            complete_tasks = self.cursor.fetchall()

            self.cursor.execute(incomplete_tasks_query)
            incomplete_tasks = self.cursor.fetchall()

            return incomplete_tasks, complete_tasks
        except Error as e:
            print(f"Error retrieving tasks: {e}")
            return None, None

    def mark_task_as_complete(self, task_id):
        try:
            update_query = "UPDATE tasks SET completed = 1 WHERE id = %s"
            self.cursor.execute(update_query, (task_id,))
            self.con.commit()
        except Error as e:
            print(f"Error marking task as complete: {e}")

    def mark_task_as_incomplete(self, task_id):
        try:
            update_query = "UPDATE tasks SET completed = 0 WHERE id = %s"
            self.cursor.execute(update_query, (task_id,))
            self.con.commit()

            task_text_query = "SELECT task FROM tasks WHERE id = %s"
            self.cursor.execute(task_text_query, (task_id,))
            task_text = self.cursor.fetchone()
            return task_text[0] if task_text else None
        except Error as e:
            print(f"Error marking task as incomplete: {e}")
            return None

    def delete_task(self, task_id):
        try:
            delete_query = "DELETE FROM tasks WHERE id = %s"
            self.cursor.execute(delete_query, (task_id,))
            self.con.commit()
        except Error as e:
            print(f"Error deleting task: {e}")

    def signup(self, username, password):
        try:
            insert_user_query = "INSERT INTO users(username, password) VALUES(%s, %s)"
            self.cursor.execute(insert_user_query, (username, password))
            self.con.commit()
            return True
        except mysql.connector.IntegrityError:
            return False
        
    def check_user(self, username, password):
        check_user_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(check_user_query, (username, password))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False

    def close_db_connection(self):
        try:
            if self.con.is_connected():
                self.cursor.close()
                self.con.close()
        except Error as e:
            print(f"Error closing the database connection: {e}")

    def get_task(self):
        try:
            get_tasks_query = "SELECT * FROM tasks"
            self.cursor.execute(get_tasks_query)
            tasks = self.cursor.fetchall()
            return tasks
        except Error as e:
            print(f"Error retrieving tasks: {e}")
            return []
