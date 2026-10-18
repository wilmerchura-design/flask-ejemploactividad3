from flask import Flask, render_template, request

app = Flask(__name__)

ESTUDIANTES = [
    {"id": 1, "nombre": "Ana Mamani", "carrera": "Secretariado Ejecutivo", "curso": "3ro A"},
    {"id": 2, "nombre": "Luis Quispe", "carrera": "Contabilidad", "curso": "2do B"},
    {"id": 3, "nombre": "María Condori", "carrera": "Sistemas Informáticos", "curso": "3ro A"},
    {"id": 4, "nombre": "Carlos Flores", "carrera": "Secretariado Ejecutivo", "curso": "1ro C"},
]


@app.route("/")
def inicio():
    return render_template("inicio.html", titulo="Inicio")


@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html", titulo="Estudiantes", estudiantes=ESTUDIANTES)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    mensaje_enviado = None
    if request.method == "POST":
        mensaje_enviado = request.form.get("nombre", "").strip() or "visitante"
    return render_template("contacto.html", titulo="Contacto", enviado=mensaje_enviado)


if __name__ == "__main__":
    app.run(debug=True)
