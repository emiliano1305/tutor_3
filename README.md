# Tutor guiado de Python (sin API)

Aplicación sencilla de Streamlit para ayudar a estudiantes que comienzan con Python. El contenido está escrito dentro del proyecto; no descarga un PDF, no busca en Internet y no llama a OpenAI ni a otros servicios. Por eso no necesita claves API ni una sección de Secrets.

## Qué incluye

- Ruta de 12 lecciones: desde “¿Qué es Python?” hasta una introducción a clases y objetos.
- Consulta rápida por palabras clave sobre los temas incluidos.
- Ejemplos de código listos para descargar como archivos `.py`.
- Ejercicios de autoevaluación con corrección inmediata.

## Alcance

No es un chatbot generativo. Las respuestas se limitan deliberadamente al material preparado en `core.py`. Si una consulta no coincide con esos temas, la app indica que aún no tiene esa explicación. Para agregar contenido, editá las lecciones, los ejemplos o las preguntas de práctica de `core.py`.

La app no ejecuta código escrito por los alumnos ni transmite sus consultas a servicios externos.

## Ejecutar en tu computadora

Se necesita Python 3.10 o posterior. En PowerShell, dentro de la carpeta del proyecto:

```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Publicar en Streamlit Community Cloud

1. Subí estos archivos a un repositorio nuevo de GitHub.
2. En Streamlit Community Cloud elegí ese repositorio, rama `main` y archivo principal `app.py`.
3. Usá Python 3.12.
4. No hace falta configurar Secrets ni variables de API.

> En este flujo, GitHub aloja el código para que Streamlit Community Cloud lo despliegue. La app no requiere Git instalado para funcionar; sí necesitás una fuente de código conectada para alojarla en Streamlit Cloud.
