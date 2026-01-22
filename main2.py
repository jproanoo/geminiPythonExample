# Ejemplo: conexión a Gemini 2.5 Flash con Python
# -----------------------------------------------
# Este programa pide al usuario un producto por teclado
# y genera un JSON con la misma estructura del ejemplo dado.
#
# Requisitos:
# 1. Instalar la librería: pip install google-generativeai
# 2. Tener tu API key de Gemini (Google AI Studio)

import google.generativeai as genai

# API key explícita (reemplaza con tu clave real)
API_KEY = ""

# Configuramos la librería con la API key
genai.configure(api_key=API_KEY)

# Seleccionamos el modelo Gemini 2.5 Flash
model = genai.GenerativeModel("gemini-2.5-flash")

# Pedimos al usuario un producto por teclado
producto = input("Ingrese el nombre de un producto: ")

# Prompt para que Gemini genere un JSON con la misma estructura del ejemplo
prompt = f"""
Genera un JSON en formato válido que simule una lista de productos,
con la misma estructura del siguiente ejemplo:

const listaProductos = [
    {{
        id: 1,
        nombre: "{producto}",
        precio: (precio aproximado en dólares para Ecuador),
        categoria: (categoría del producto),
        imagen: "https://dummyimage.com/200x200/000/fff&text={producto.replace(" ", "+")}",
        detalles: "Breve descripción del producto"
    }}
];

No repitas el ejemplo, usa únicamente el producto ingresado por el usuario.
"""

# Generamos la respuesta
response = model.generate_content(prompt)

# Mostramos el resultado en pantalla
print("Respuesta generada por Gemini:")
print(response.text)
