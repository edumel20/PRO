from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'


def create_db(db_path: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """CREATE TABLE tasks(
        id INTEGER PRIMARY KEY,
        name TEXT,
        done BOOLEAN   
        )"""

    cur.execute(sql)
    con.commit()


class Task:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, done: bool = False, id: int = -1):
        self.name = name
        self.done = done
        self.id = id

    def save(self) -> None:
        sql = 'INSERT INTO tasks (name, done) VALUES (?, ?);'
        con = Task.con
        cur = Task.cur
        cur.execute(sql, (self.name, self.done))
        con.commit()
        self.id = cur.lastrowid

    def update(self) -> None:
        sql = f'UPDATE tasks SET name = ?, done = ? WHERE id = {self.id}'
        con = Task.con
        cur = Task.cur
        cur.execute(
            sql,
            (
                self.name,
                self.done,
            ),
        )
        con.commit()

    def check(self) -> None:
        self.done = True
        self.update()

    def uncheck(self) -> None:
        self.done = False
        self.update()

    def __repr__(self):
        return f'[X] {self.name} (id={self.id})' if self.done else f'[ ] {self.name} (id={self.id})'

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        new_id = row[0]
        new_name = row[1]
        new_done = row[2]

        return cls(new_id, new_name, new_done)

    @classmethod
    def get(cls, task_id: int) -> Task:
        sql = 'SELECT * from tasks WHERE id = ?'
        cur = cls.cur
        cur.execute(sql, (task_id,))
        row = cur.fetchone()
        return cls.from_db_row(row)


class ToDo:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def get_tasks(self, done: int = -1):
        cur = ToDo.cur
        sql1 = 'SELECT * FROM tasks'
        sql2 = 'SELECT * FROM tasks WHERE done = False'
        sql3 = 'SELECT * FROM tasks WHERE done = True'

        if done == 0:
            result = cur.execute(sql2)
        elif done == 1:
            result = cur.execute(sql3)
        else:
            result = cur.execute(sql1)

        for row in result:
            yield Task(row[0], row[1], row[2])

    def add_task(self, name: str) -> None:
        Task(name).save()

    def complete_task(self, task_id: int) -> None:
        Task.get(task_id).check()

    def reopen_task(self, task_id: int) -> None:
        Task.get(task_id).uncheck()
