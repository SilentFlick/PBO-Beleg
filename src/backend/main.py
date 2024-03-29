import json
import os
import re

from flask import Flask, jsonify, request
from flask_cors import CORS

import hashtable
import server

app = Flask(__name__)
CORS(app)


@app.route("/posts", methods=["GET", "POST"])
def get_posts():
    data = json.loads(request.data, strict=False)
    pl_id = data["pl_id"]
    posts = server.get_posts_and_comments_from_db(pl_id)
    if posts == None:
        return "", 511
    return jsonify(posts)


@app.route("/post/<int:id>", methods=["GET"])
def get_posts_by_id(id):
    post = server.get_posts_by_id_from_db(id)
    return jsonify(post)


@app.route("/post", methods=["POST"])
def insert_posts():
    data = json.loads(request.data, strict=False)
    from_user = data["from_user"]
    to_user = data["to_user"]
    title = data["title"]
    content = data["content"]
    faculty = data["faculty"]
    hash = data["hash"]
    result = None
    print(hash)
    print(ht.get(hash))
    if ht.get(hash):
        result = server.insert_post_to_db(from_user, to_user, faculty, title, content)
        return jsonify(result)
    return "", 511


@app.route("/post/<int:id>", methods=["PUT"])
def update_posts(id):
    data = json.loads(request.data, strict=False)
    id = data["post_id"]
    from_user = data["from_user"]
    to_user = data["to_user"]
    title = data["title"]
    content = data["content"]
    hash = data["hash"]
    result = None
    if ht.get(hash):
        result = server.update_post_to_db(id, from_user, to_user, title, content)
        return jsonify(result)
    return "", 511


@app.route("/post/<int:id>", methods=["DELETE"])
def delete_post(id):
    data = json.loads(request.data, strict=False)
    id = data["id"]
    hash = data["hash"]
    result = None
    if ht.get(hash):
        result = server.delete_post_from_db(id)
        return jsonify(result)
    return "", 511


@app.route("/comments", methods=["GET"])
def get_comments():
    comments = server.get_comments_from_db()
    return jsonify(comments)


@app.route("/comments", methods=["POST"])
def insert_comment():
    data = json.loads(request.data, strict=False)
    post_id = data["post_id"]
    from_user = data["from_user"]
    comment = data["comment"]
    hash = data["hash"]
    result = None
    if ht.get(hash):
        result = server.insert_comment_to_db(post_id, from_user, comment)
        return jsonify(result)
    return "", 511


@app.route("/profs", methods=["POST"])
def get_profs():
    data = json.loads(request.data, strict=False)
    faculty = data["faculty"]
    profs = server.get_prof_from_db(faculty)
    return jsonify(profs)


@app.route("/logout", methods=["POST"])
def logout():
    data = json.loads(request.get_data(), strict=False)
    res = ht.delete(data)
    return jsonify(res)


@app.route("/login", methods=["POST"])
def login():
    data = json.loads(request.get_data(), strict=False)
    username = data["username"]
    password = data["password"]
    randomString = None
    profs = server.check_prof_from_db(username)
    if profs != None and password == "123":
        randomString = "".join("%02x" % x for x in os.urandom(16))
        ht.put(randomString)
        return jsonify(hash=randomString, pl_id=profs)
    elif re.findall(r"s\d{5}", username):
        result = server.authenticate(username, password)
        if result != None:
            randomString = "".join("%02x" % x for x in os.urandom(16))
            ht.put(randomString)
            return jsonify(hash=randomString)
    return "", 511


if __name__ == "__main__":
    server.create_db()
    ht = hashtable.HashTable()
    app.run(host="0.0.0.0", port=8000, debug=False)
