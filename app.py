import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar clave de API desde .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializar cliente OpenAI
client = OpenAI(api_key=api_key)

# Configuración de la app
st.set_page_config(page_title="ExploraJugando", page_icon="🎲")

# Título y descripción
st.title("🎲 ExploraJugando")
st.markdown("Generador de actividades creativas para niños y niñas, según su edad e intereses.")

# Inputs del usuario
edad = st.number_input("Edad del niño/a:", min_value=1, max_value=12, step=1)
intereses = st.text_input("Intereses (por ejemplo: dinosaurios, dibujo, aventuras):")

# Botón para generar actividad
if st.button("🎯 Generar actividad"):
    with st.spinner("Pensando una idea divertida..."):

        # Construir el prompt
        prompt = (
            f"Generá una actividad divertida y educativa para un niño de {edad} años "
            f"interesado en {intereses}. La actividad debe ser clara, creativa, y fácil de hacer en casa. "
            f"Incluí materiales necesarios (si los hay), duración estimada y una breve explicación."
        )

        # Solicitud a la API de OpenAI
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Sos un asistente creativo que diseña actividades educativas y divertidas para niños."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8
            )

            actividad_generada = response.choices[0].message.content
            st.success("¡Actividad generada!")
            st.markdown("### 📌 Actividad sugerida:")
            st.write(actividad_generada)

        except Exception as e:
            st.error(f"Ocurrió un error al generar la actividad: {str(e)}")

# Sección: Cómo funciona
with st.expander("🛠️ ¿Cómo funciona esta app?"):
    st.markdown("""
Esta aplicación utiliza la inteligencia artificial de OpenAI para crear actividades personalizadas para niños/as.
1. Ingresás la edad y los intereses del niño/a.
2. La IA genera una actividad creativa y educativa en base a esa información.
3. ¡Listo! Tenés una idea para jugar y aprender juntos/as.

Las ideas generadas están pensadas para ser seguras, creativas y adecuadas a la edad que indiques.
""")
