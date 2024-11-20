# fuerzabrutasimuladortermux
Un simulador de ataque de Fuerza bruta en un entorno controlado para termux creado en python uso exclusivamente para the termux sindicate

---
## **Instrucciones de Uso de la Herramienta Fuerza Bruta Simulador en Termux**
---

### Requisitos Previos:
- **Termux instalado** en tu dispositivo Android.
- **Python 3** y **pip** deben estar instalados en Termux.
- **Conexión a internet** para descargar dependencias desde el repositorio de GitHub.

---

### **1. Clonar el Repositorio en Termux**

Primero, clona el repositorio desde GitHub para obtener el código:

```bash
git clone https://github.com/danissj45/fuerzabrutasimuladortermux.git
```

Luego, navega al directorio del repositorio:

```bash
cd fuerzabrutasimuladortermux
```

---

### **2. Instalar Dependencias**

Si prefieres no usar el archivo `requirements.txt`, puedes instalar las dependencias de forma manual. Ejecuta los siguientes comandos para instalar las librerías necesarias:

1. **Para instalar `requests`**:

```bash
pip install requests
```

2. **Para instalar `termcolor`**:

```bash
pip install termcolor
```

3. **Para instalar `Flask`**:

```bash
pip install Flask
```

Si prefieres usar `requirements.txt`, puedes instalar todas las dependencias de una vez ejecutando:

```bash
pip install -r requirements.txt
```

---

Aquí tienes la sección modificada con la opción **`-p`** para cambiar la contraseña:

---

### **3. Ejecutar el Servidor Web con `montarpagina.py`**

Este script monta una página web básica que será atacada por el **`bruteforce.py`**.

#### **Ejecutar el servidor con la contraseña predeterminada:**

Para ejecutar el servidor con la contraseña predeterminada (sin cambios), simplemente usa el siguiente comando:

```bash
python montarpagina.py
```

El script generará una página web simulada que estará disponible en **`http://localhost:8080/`** (por defecto). Asegúrate de que el servidor esté corriendo antes de ejecutar el ataque de fuerza bruta.

#### **Ejecutar el servidor y cambiar la contraseña:**

Si deseas establecer una contraseña personalizada para la página web, puedes hacerlo utilizando el parámetro **`-p`** seguido de la nueva contraseña que deseas usar. Por ejemplo, para cambiar la contraseña a **"nueva_contraseña"**, ejecuta:

```bash
python montarpagina.py -p nueva_contraseña
```

Esto generará una página web en **`http://localhost:8080/`** con la nueva contraseña que has configurado. Recuerda que el ataque de fuerza bruta deberá ser dirigido a esta contraseña si decides cambiarla.

De esta forma, ahora puedes modificar la contraseña de la página web antes de ejecutar el ataque de fuerza bruta.

---

### **4. Configuración y Ejecución del Ataque de Fuerza Bruta con `bruteforce.py`**

Una vez que el servidor esté corriendo, puedes iniciar el ataque de fuerza bruta.

#### **Configuración de Ataque:**

1. **Seleccionar Diccionario:**
   El ataque utiliza un diccionario de contraseñas. Asegúrate de tener tus diccionarios `.txt` en la carpeta `dic/`. Si no existe, créala y coloca los archivos de diccionario dentro de ella.

2. **Velocidad del Ataque:**
   Puedes configurar la velocidad del ataque seleccionando entre las siguientes opciones:
   - **Lento (2 segundos entre intentos)**
   - **Medio (1 segundo entre intentos)**
   - **Rápido (0.5 segundos entre intentos)**

3. **Método HTTP:**
   El ataque puede ser realizado usando los métodos **GET** o **POST**. Selecciona el método adecuado dependiendo de la configuración de la página.

#### **Ejecutar el Ataque:**

Para iniciar el ataque, ejecuta el siguiente comando en Termux:

```bash
python bruteforce.py
```

El programa te guiará a través de las siguientes opciones interactivas:

1. **Iniciar el Ataque**: Selecciona la URL (en este caso, **http://localhost:8080/**) y los parámetros de usuario/contraseña para atacar.
2. **Configurar Velocidad**: Elige entre las opciones de velocidad para el ataque.
3. **Seleccionar Diccionario**: Escoge el archivo de diccionario que deseas utilizar (asegúrate de tener los archivos en la carpeta `dic/`).
4. **Elegir Método de Ataque**: Selecciona entre **GET** o **POST** según el método que soporte la página web.

El script intentará diferentes combinaciones de contraseñas hasta que encuentre una que sea exitosa, o hasta que termine con todas las posibles combinaciones.

---

### **5. Instrucciones Adicionales:**

- **Para Detener el Ataque**: Si necesitas detener el ataque, simplemente presiona `CTRL+C` en Termux.
- **Resultados**: Si el ataque tiene éxito, se mostrará un mensaje indicando que se ha encontrado la contraseña. De lo contrario, se indicará que no se encontró ninguna coincidencia en el diccionario.
- **Usar Ngrok**: Si deseas realizar un ataque sobre una página que esté en una red pública (por ejemplo, usando Ngrok), puedes configurar la URL de Ngrok en el menú de **`bruteforce.py`**.

---

### **6. Consideraciones Importantes:**

- **Uso Legal**: Esta herramienta está destinada para ser utilizada **solo en pruebas de penetración autorizadas**. No se debe utilizar en sistemas o páginas web sin el consentimiento explícito del propietario.
- **Precauciones de Seguridad**: Asegúrate de usar esta herramienta en un entorno controlado y de no vulnerar ninguna ley local.

---

### **Enlaces Útiles:**

- Repositorio en GitHub: [https://github.com/danissj45/fuerzabrutasimuladortermux](https://github.com/danissj45/fuerzabrutasimuladortermux)
