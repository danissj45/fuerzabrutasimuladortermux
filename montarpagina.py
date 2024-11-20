from flask import Flask, render_template_string, request, redirect, url_for, flash
import argparse

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar flash mensajes

# Contraseña predeterminada
password_value = "root"

# Función para manejar el argumento -p
def parse_arguments():
    global password_value
    parser = argparse.ArgumentParser(description="Cambiar la contraseña")
    parser.add_argument('-p', '--password', type=str, help="Establecer una nueva contraseña")
    args = parser.parse_args()
    
    # Si el argumento -p es proporcionado, cambiar la contraseña
    if args.password:
        password_value = args.password
        print(f"Contraseña cambiada a: {password_value}")

# Plantilla de la página web
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio de Sesión</title>
    <style>
        body {
            background-color: #222;
            color: #0f0;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
        }
        .container {
            width: 300px;
            margin: auto;
        }
        h1 {
            color: #0f0;
        }
        input[type="password"], button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #0f0;
            background-color: #111;
            color: #0f0;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            cursor: pointer;
        }
        button:hover {
            background-color: #0f0;
            color: #111;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Inicio de Sesión</h1>
        <form action="{{ url_for('login') }}" method="post">
            <input type="password" name="password" placeholder="Ingrese su contraseña" required>
            <button type="submit">Ingresar</button>
        </form>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
            <p style="color: #f00;">{{ messages[0] }}</p>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
"""

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def login():
    global password_value
    if request.method == 'POST':
        # Obtener contraseña ingresada
        password = request.form.get('password')

        # Validar contraseña
        if password == password_value:
            return redirect(url_for('success'))
        else:
            flash("Contraseña incorrecta. Intenta nuevamente.")
            return redirect(url_for('login'))
    return render_template_string(html_template)

# Ruta para mostrar el éxito
@app.route('/success', methods=['GET'])
def success():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inicio Exitoso</title>
        <style>
            body {
                background-color: #222;
                color: #0f0;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
            }
            h1 {
                color: #0f0;
            }
            p {
                color: #0f0;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>¡Inicio Exitoso!</h1>
        <p>Bienvenido al sistema.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    parse_arguments()  # Llamada para procesar el parámetro -p
    app.run(host='0.0.0.0', port=8080)
