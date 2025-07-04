from flask import Flask, request, redirect, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "usuarios.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Hash de la password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registro de usuario 
def registrar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
    if not c.fetchone():  
        c.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, hash_password(password)))
        conn.commit()
    conn.close()

# Validar usuario
def validar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (nombre,))
    resultado = c.fetchone()
    conn.close()
    if resultado:
        return hash_password(password) == resultado[0]
    return False

# HTML simple
html = '''
<!DOCTYPE html>
<html>
<head><title>Examen DRY7122</title></head>
<body>
    <h2>Iniciar sesion</h2>
    <form method="post">
        Usuario: <input type="text" name="usuario"><br>
        Password: <input type="password" name="clave"><br>
        <input type="submit" value="Ingresar">
    </form>
    <p>{{ mensaje }}</p>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]
        if validar_usuario(usuario, clave):
            mensaje = "Bienvenido, " + usuario
        else:
            mensaje = "Usuario o password incorrecta"
    return render_template_string(html, mensaje=mensaje)

if __name__ == "__main__":
    init_db()
    registrar_usuario("Macarena Comen", "clave123")  

    app.run(port=7500)