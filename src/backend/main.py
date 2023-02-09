import json
import os
import re

from flask import Flask, jsonify, request
from flask_cors import CORS

import hashtable
import server

app = Flask(__name__)
CORS(app)


@app.route("/posts", methods=["GET"])
def get_posts():
    posts = server.get_posts_from_db()
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
    result = None
    if ht.get(hash):
        result = server.insert_post_to_db(from_user, to_user, faculty, title, content)
    return jsonify(result)


@app.route("/post/<int:id>", methods=["PUT"])
def update_posts(id):
    data = json.loads(request.data, strict=False)
    id = data["post_id"]
    from_user = data["from_user"]
    to_user = data["to_user"]
    title = data["title"]
    content = data["content"]
    result = server.update_post_to_db(id, from_user, to_user, title, content)
    return jsonify(result)


@app.route("/post/<int:id>", methods=["DELETE"])
def delete_post(id):
    data = json.loads(request.data, strict=False)
    id = data["id"]
    result = server.delete_post_from_db(id)
    return jsonify(result)


@app.route("/comments", methods=["GET"])
def get_comments():
    comments = server.get_comments_from_db()
    return jsonify(comments)


@app.route("/comments", methods=["POST"])
def insert_comment():
    data = json.loads(request.data, strict=False)
    post_id = data["post_id"]
    comment = data["comment"]
    hash = data["hash"]
    result = None
    if ht.get(hash):
        result = server.insert_comment_to_db(post_id, comment)
    return jsonify(result)


@app.route("/profs", methods=["GET"])
def get_profs():
    profs = server.get_prof_from_db()
    return jsonify(profs)


@app.route("/logout", methods=["POST"])
def logout():
    data = json.loads(request.get_data(), strict=False)
    ht.delete(data)
    return jsonify(True)


@app.route("/login", methods=["POST"])
def login():
    data = json.loads(request.get_data(), strict=False)
    username = data["username"]
    password = data["password"]
    randomString = None
    if server.check_prof_from_db(username) != None and password == "123":
        randomString = "".join("%02x" % x for x in os.urandom(16))
        ht.put(randomString)
    elif re.findall(r"s\d{5}", username):
        result = server.authenticate(username, password)
        if result != None:
            randomString = "".join("%02x" % x for x in os.urandom(16))
            ht.put(randomString)
    return jsonify(randomString)


if __name__ == "__main__":
    server.create_db()
    ht = hashtable.HashTable()
    app.run(host="0.0.0.0", port=8000, debug=False)
