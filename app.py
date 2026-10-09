from __future__ import annotations

import streamlit as st

from core import LESSONS, QUIZZES, RECIPES, find_lesson

st.set_page_config(page_title="Tutor guiado de Python", page_icon="🐍", layout="centered")

st.title("Tutor guiado de Python")
st.caption("Un recorrido interactivo para aprender desde cero. Sin claves API, PDF ni consultas externas.")

section = st.sidebar.radio(
    "Elegí una sección",
    ["Inicio", "Lecciones", "Consultar un tema", "Armar un ejemplo", "Practicar"],
)
st.sidebar.divider()
st.sidebar.caption("Este tutor ofrece contenido didáctico preparado en la app; no es un chatbot generativo.")
st.sidebar.caption("No se envían tus preguntas a servicios externos.")

if section == "Inicio":
    st.subheader("Empezá por lo básico y avanzá a tu ritmo")
    st.write(
        "La app explica conceptos de Python con ejemplos cortos, muestra soluciones de código "
        "preparadas y propone preguntas de práctica. Está pensada para estudiantes que recién comienzan."
    )
    st.markdown("### Ruta sugerida")
    for lesson in LESSONS:
        st.markdown(f"- {lesson['title']}")
    st.info("Para comenzar, abrí **Lecciones** y elegí **1. ¿Qué es Python?**.")
    st.markdown("### Qué puede y qué no puede hacer")
    st.write(
        "Puede explicar los temas incluidos, encontrar una explicación por palabras clave, "
        "mostrar ejemplos de una lista y corregir las respuestas de los ejercicios. "
        "No inventa respuestas a preguntas abiertas ni consulta Internet. "
        "Si el tema todavía no está incluido, te lo va a indicar."
    )

elif section == "Lecciones":
    selected_title = st.selectbox("Elegí una lección", [lesson["title"] for lesson in LESSONS])
    lesson = next(item for item in LESSONS if item["title"] == selected_title)
    st.subheader(lesson["title"])
    st.markdown(f"**Objetivo:** {lesson['objective']}")
    st.markdown("### Explicación")
    st.write(lesson["explanation"])
    st.markdown("### Ejemplo")
    st.code(lesson["code"], language="python")
    st.markdown("### Cómo leerlo")
    st.write(lesson["walkthrough"])
    st.markdown("### Probá vos")
    st.info(lesson["exercise"])

elif section == "Consultar un tema":
    st.subheader("Consulta rápida sobre Python")
    st.write("Escribí una palabra o pregunta breve. La app buscará entre los temas preparados.")
    query = st.text_input("Tu consulta", placeholder="Por ejemplo: ¿cómo funcionan las variables?")
    if st.button("Buscar tema", type="primary"):
        lesson = find_lesson(query)
        if lesson:
            st.success(f"Tema encontrado: {lesson['title']}")
            st.markdown(f"**Objetivo:** {lesson['objective']}")
            st.write(lesson["explanation"])
            st.code(lesson["code"], language="python")
            st.caption(lesson["walkthrough"])
            st.info(f"Para practicar: {lesson['exercise']}")
        else:
            st.warning(
                "Todavía no tengo una explicación preparada para esa consulta. "
                "Este tutor responde solo sobre los temas de Python incluidos en **Lecciones**. "
                "Probá con: variables, input, suma, if, bucles, listas, funciones, diccionarios, errores, archivos o clases."
            )

elif section == "Armar un ejemplo":
    st.subheader("Armar un ejemplo de código")
    st.write("Elegí un objetivo y la app te muestra un programa de ejemplo que podés descargar.")
    recipe_name = st.selectbox("¿Qué querés hacer?", list(RECIPES))
    recipe = RECIPES[recipe_name]
    st.code(recipe["code"], language="python")
    st.write(recipe["explanation"])
    st.download_button(
        "Descargar este ejemplo .py",
        data=recipe["code"],
        file_name=recipe["filename"],
        mime="text/x-python",
    )
    st.caption("El código es una plantilla educativa; revisalo y adaptalo antes de usarlo.")

elif section == "Practicar":
    st.subheader("Autoevaluación")
    quiz = st.selectbox(
        "Elegí una pregunta",
        QUIZZES,
        format_func=lambda item: item["question"],
    )
    answer = st.radio("Tu respuesta", quiz["options"], index=None)
    if st.button("Revisar respuesta", type="primary"):
        if answer is None:
            st.warning("Elegí una respuesta antes de revisar.")
        elif answer == quiz["answer"]:
            st.success("¡Correcto!")
            st.write(quiz["explanation"])
        else:
            st.error("Todavía no. Volvé a leer la lección relacionada e intentá otra vez.")
            st.write(quiz["explanation"])
