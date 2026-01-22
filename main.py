# Ejemplo sencillo de conexión a la API de Gemini con Python
# ----------------------------------------------------------
# Requisitos previos:
# 1. Instalar la librería oficial: pip install google-generativeai
# 2. Tener tu API key de Gemini (Google AI Studio)
# https://aistudio.google.com/api-keys

import google.generativeai as genai

# Aquí escribimos la API key de manera explícita
API_KEY = "TU_API_KEY_AQUI"   # <-- reemplaza con tu clave real

# Configuramos la librería con la API key
genai.configure(api_key=API_KEY)

# Creamos un modelo de texto (Gemini-2-5-flash)
model = genai.GenerativeModel("gemini-2.5-flash")

# Enviamos un prompt sencillo al modelo
prompt = "Escribe un poema corto sobre el amanecer en la playa."

# Generamos la respuesta
response = model.generate_content(prompt)

# Mostramos el resultado en pantalla
print("Respuesta del modelo:")
print(response.text)
