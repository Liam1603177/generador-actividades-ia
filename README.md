
# ExploraJugando: Generador de actividades para niños con IA

ExploraJugando es una aplicación web que utiliza Inteligencia Artificial para generar actividades creativas y educativas personalizadas para niños, basada en su edad e intereses. Fue desarrollada con Streamlit y la API de OpenAI como proyecto para la materia "Inteligencia Artificial: Prompt Engineering para programadores".

## 👤 Autor

- Ignacio Luis Daddario  
- Usuario de GitHub: [Liam1603177](https://github.com/Liam1603177)

## 🌟 Objetivo

Crear una solución práctica que ayude a padres, docentes y cuidadores a encontrar ideas de juegos y actividades personalizadas para fomentar el desarrollo cognitivo, emocional y social de los niños.

## 🧩 Problemática

Muchos padres y docentes se enfrentan a la dificultad de encontrar actividades originales, educativas y adaptadas a la edad de los niños. Las ideas suelen repetirse y no siempre son adecuadas a los intereses específicos o al contexto del niño (clima, espacio disponible, materiales, etc.).

## 💡 Solución Propuesta

ExploraJugando genera actividades únicas e interactivas para niños, basándose en:

- Edad
- Intereses específicos (como ciencia, arte, movimiento, etc.)
- Materiales disponibles
- Lugar de la actividad (interior/exterior)

Esto permite que las propuestas estén mejor adaptadas a cada situación. Utiliza modelos de lenguaje avanzados (GPT-3.5-turbo) para generar textos creativos, educativos y seguros.

## 🖥️ Funcionalidad de la App

- 🎨 Título y descripción de la app
- 📋 Campos para ingresar edad, intereses y contexto
- 🔁 Botón para generar actividad personalizada
- 📚 Sección “¿Cómo funciona?” que explica el propósito y la mecánica de la app

## 🚀 Acceso a la aplicación

- Aplicación en línea:  
  👉 https://generador-actividades-ia-fpkbsxrrfpghggh2ocnp37.streamlit.app/

- Código fuente en GitHub:  
  👉 https://github.com/Liam1603177/generador-actividades-ia

## 🔐 Prompt Inicial

A continuación, el prompt utilizado como base para interactuar con la API de OpenAI:

```
Actúa como un generador de actividades para niños. Según la edad y los intereses que te indique, proponé una actividad educativa, creativa y divertida. Indicá los materiales necesarios, el paso a paso para desarrollarla y los beneficios que tiene para el desarrollo del niño. Usá un lenguaje claro y adecuado a la edad.
```

Este prompt fue elegido por su claridad, tono amigable y por pedir una respuesta estructurada que cubra los elementos clave (actividad + materiales + beneficios).

## 💵 Factibilidad económica

Se utilizó la API de OpenAI con el modelo GPT-3.5-turbo, que ofrece un bajo costo por token. Las consultas son breves, por lo que el costo por uso es bajo y escalable. En una implementación básica, puede utilizarse gratuitamente bajo los límites de uso de la API.

## 📦 Instalación local

1. Clonar el repositorio:
   git clone https://github.com/Liam1603177/generador-actividades-ia

2. Instalar dependencias:
   pip install -r requirements.txt

3. Crear un archivo .env con tu clave de OpenAI:
   OPENAI_API_KEY=tu_clave_aquí

4. Ejecutar la app:
   streamlit run app.py

## ✅ Conclusión

ExploraJugando permite aprovechar el poder de la IA para resolver una necesidad real en familias y ámbitos educativos. Es una herramienta flexible, divertida y útil para fomentar el juego creativo y el aprendizaje en los niños.
