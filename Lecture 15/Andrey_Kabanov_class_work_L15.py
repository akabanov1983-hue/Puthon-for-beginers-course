import sqlite3

with sqlite3.connect("test_todolist.db") as c:

    cur = c.cursor()
    q_text = '''CREATE TABLE "user" (
    "u_id" INTEGER NOT NULL UNIQUE,
    "u_name" TEXT NOT NULL,
    "u_email" TEXT NOT NULL,
    "u_phone" TEXT NOT NULL,
    PRIMARY KEY("u_id" AUTOINCREMENT)
    );'''

    cur.execute(q_text)

    q_text = """
    CREATE TABLE "task" (
    "t_id" INTEGER NOT NULL UNIQUE,
    "t_name" TEXT NOT NULL,
    "u_id_fk" INTEGER NOT NULL,
    PRIMARY KEY("t_id" AUTOINCREMENT),
    FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
    );
    """
    cur.execute(q_text)

    c.commit()