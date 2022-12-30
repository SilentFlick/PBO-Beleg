import ldap
import sqlite3

LDAP_SERVER = "ldaps://rlux40.rz.htw-dresden.de:636"
DATABASE_NAME = "pbo"


def authenticate(username, password):
    try:
        ldapLogin = "uid=" + username + ",ou=people,dc=htw-dresden,dc=de"
        server = ldap.initialize(LDAP_SERVER)
        result = server.simple_bind_s(ldapLogin, password)
        server.unbind_s()
        return result
    except Exception as e:
        print("Failed to authenticate. Invalid credential:", e)


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_db():
    with open("pbo.sql", "r") as sql_file:
        sql_script = sql_file.read()

    db = get_db()
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()
    return True


def insert_prof_to_db(name, faculty):
    db = get_db()
    cursor = db.cursor()
    statement = "insert into professor_lecturer values (null, ?, ?)"
    cursor.execute(statement, [name, faculty])
    db.commit()
    db.close()
    return True


def insert_post_to_db(from_user, to_user, title, content):
    db = get_db()
    cursor = db.cursor()
    statement = "insert into posts values (null, ?, ?, ?, ?)"
    cursor.execute(statement, [from_user, to_user, title, content])
    db.commit()
    db.close()
    return True


def update_post_to_db(id, from_user, to_user, title, content):
    db = get_db()
    cursor = db.cursor()
    statement = "update posts set from_user = ?, to_user = ?, title = ?, content = ? where post_id = ?"
    cursor.execute(statement, [from_user, to_user, title, content, id])
    db.commit()
    db.close()
    return True


def delete_post_from_db(id):
    db = get_db()
    cursor = db.cursor()
    statement = "delete from posts where post_id = ?"
    cursor.execute(statement, [id])
    db.commit()
    db.close()
    return True


def get_posts_from_db():
    db = get_db()
    cursor = db.cursor()
    statement = "select post_id, from_user, to_user, p.faculty, title, content, created_at, name from posts p left join professor_lecturer l on from_user=pl_id"
    cursor.execute(statement)
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r if r else None


def get_posts_by_id_from_db(id):
    db = get_db()
    cursor = db.cursor()
    statement = "select post_id, from_user, to_user,  title, content from posts where post_id = ?"
    cursor.execute(statement, [id])
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r[0] if r else None
