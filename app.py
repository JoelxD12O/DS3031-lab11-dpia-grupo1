# app.py  —  pip install -r requirements.txt ; flask --app app run
# Backend mínimo del Lab 11 (DS3031). SIN protecciones de privacidad a propósito:
# sus problemas son el objeto de la DPIA (ver DPIA.md). Lo único no negociable:
# consultas parametrizadas (?).
import sqlite3
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")
db = sqlite3.connect("lab.db", check_same_thread=False)
db.execute("""CREATE TABLE IF NOT EXISTS registro (
    id         INTEGER PRIMARY KEY,
    nombres    TEXT NOT NULL,
    apellidos  TEXT NOT NULL,
    correo     TEXT NOT NULL,
    telefono   TEXT,
    creado_en  TEXT DEFAULT CURRENT_TIMESTAMP)""")


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.post("/registro")
def registrar():
    d = request.get_json()
    db.execute("INSERT INTO registro (nombres, apellidos, correo, telefono) "
               "VALUES (?, ?, ?, ?)",
               (d["nombres"], d["apellidos"], d["correo"], d.get("telefono")))
    db.commit()
    return {"ok": True}, 201


@app.get("/registros")
def listar():
    cur = db.execute("SELECT * FROM registro")
    cols = [c[0] for c in cur.description]
    return jsonify([dict(zip(cols, row)) for row in cur.fetchall()])
