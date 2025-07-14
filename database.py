import sqlite3
from typing import List, Dict, Any
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS todos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  category TEXT NOT NULL,
                  date_added TEXT NOT NULL,
                  date_completed TEXT,
                  status INTEGER NOT NULL,
                  position INTEGER)''')
    
create_table()

def insert_todo(todo: Todo):
    c.execute('select count(*) from todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    # Always set status=0 for new todos (pending)
    with conn:
        c.execute('INSERT INTO todos (task, category, date_added, date_completed, status, position) VALUES (:task, :category, :date_added, :date_completed, :status, :position)', {
            'task': todo.task,
            'category': todo.category,
            'date_added': todo.date_added,
            'date_completed': todo.date_completed,
            'status': 0,
            'position': todo.position
        })

def get_all_todos() -> List[Todo]:
    c.execute('SELECT * FROM todos ORDER BY position')
    rows = c.fetchall()
    todos  = []
    for result in rows:
        todos.append(Todo(*result))
    return todos

def delete_todo(position: int):
    c.execute('select count(*) from todos')
    count = c.fetchone()[0]
    with conn:
        c.execute("DELETE FROM todos WHERE position=:position", {'position': position})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1,False)

def change_position(old_position: int, new_position: int, commit: bool = True):
    if old_position == new_position:
        return
    with conn:
        c.execute("UPDATE todos SET position=:new_position WHERE position=:old_position", {'new_position': new_position, 'old_position': old_position})
        if commit:
            conn.commit()      

def update_todo(position: int, task: str = None, category: str = None):
    with conn:
        if task is not None:
            c.execute("UPDATE todos SET task = :task WHERE position = :position", {'task': task, 'position': position})
        elif task is not None:
            c.execute("UPDATE todos SET task = :task WHERE position = :position", {'task': task, 'position': position})
        elif category is not None:
            c.execute("UPDATE todos SET category = :category WHERE position = :position", {'category': category, 'position': position})

# Mark a todo as complete by setting status=1 and updating date_completed
def complete_todo(position: int):
    date_completed = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with conn:
        c.execute(
            "UPDATE todos SET status = 1, date_completed = :date_completed WHERE position = :position",
            {'date_completed': date_completed, 'position': position}
        )
