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


def insert_post_to_db(from_user, to_user, faculty, title, content):
    db = get_db()
    cursor = db.cursor()
    statement = "insert into posts(post_id, from_user, to_user, faculty, title, content) values (null, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [from_user, to_user, faculty, title, content])
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
    statement = "select post_id, from_user, to_user, p.faculty, title, content, created_at, name from posts p left join professor_lecturer l on from_user=pl_id where post_id = ?"
    cursor.execute(statement, [id])
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r[0] if r else None


def get_comments_from_db():
    db = get_db()
    cursor = db.cursor()
    statement = "select post_id,json_group_array(json_object('comment_id',comment_id, 'comment',comment, 'created_at', created_at, 'from_user' , (select name from comments ci left join professor_lecturer on from_user=pl_id where ci.comment_id=co.comment_id ))) as comments from comments co group by post_id"
    cursor.execute(statement)
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r if r else None


def get_posts_and_comments_from_db(pl_id=None):
    db = get_db()
    cursor = db.cursor()
    statement = "select p.*, pl.name, com.comments from posts p left join professor_lecturer pl on p.from_user = pl.pl_id left join ( select post_id,json_group_array(json_object('comment_id',comment_id, 'comment',comment, 'created_at', created_at, 'from_user' , (select name from comments ci left join professor_lecturer on from_user=pl_id where ci.comment_id=co.comment_id ))) as comments from comments co group by co.post_id) as com on p.post_id=com.post_id "
    if pl_id != None:
        statement += "where to_user = ?"
        cursor.execute(statement, [pl_id])
    else:
        cursor.execute(statement)
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r if r else None


def insert_comment_to_db(post_id, from_user, comment):
    db = get_db()
    cursor = db.cursor()
    statement = "insert into comments(comment_id, post_id, from_user, comment) values (null, ?, ?, ?)"
    cursor.execute(statement, [post_id, from_user, comment])
    db.commit()
    db.close()
    return True


def get_prof_from_db(faculty):
    db = get_db()
    cursor = db.cursor()
    statement = "select * from professor_lecturer where faculty = ?"
    cursor.execute(statement, [faculty])
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r if r else None


def check_prof_from_db(prof_name):
    db = get_db()
    cursor = db.cursor()
    statement = "select pl_id from professor_lecturer where name = ?"
    cursor.execute(statement, [prof_name])
    db.commit()
    r = [
        dict((cursor.description[i][0], value) for i, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    db.close()
    return r[0].get("pl_id") if r else None
