# Proyecto Grupal --- NPCs con personalidad dinamica basada en IA en videojuegos

##Introduccion

Este documento tiene como fin implementar en NPCs de videjuegos, un modelo de IA entrenado con personalidad dinamica que puedan interactuar con el personaje y cambiar en funcion de los eventos que provoque el jugador.

## Componentes del sistema

- **Scripts de procesamiento**: ingesta, limpieza, transformación y validación de datos.
- **Base de datos PostgreSQL**: para la carga y consulta estructurada de los datasets.
- **Modelo de IA (LLM)**: Entendimiento .
- **Documentación**: diseño técnico completo + planificación.

## Tecnologías utilizad
- Visual Studio Code
- Python 3.0
- Base de datos PostgreSQL
- Git Hub
- Github Actions
- Docker
- Render

## Pipeline implementado
1. Simulación: Registro de las interacciones jugador-NPC mediante scripts de simulación.
   
3. Procesamiento: Limpieza de datos nulos y transformación de variables de comportamiento.

4. Adaptación de IA: Procesamiento de datos por el modelo para modificar rasgos de personalidad del NPC.

5. Persistencia: Carga de los nuevos estados y el historial de comportamiento en la base de datos PostgreSQL.

6. Evaluación: Simulación visual o demo de los resultados para validar la coherencia del comportamiento adaptativo


## Estructura del repositorio
--/scripts: Contiene archivos .py de ingesta, limpieza y entrenamiento de IA.
--/data: Almacena los datasets generados (reales o sintéticos).
-/database: Archivos de configuración y scripts SQL para PostgreSQL.
-/docs: Documentación técnica, diagramas y planificación PMBOK.
-.github/workflows: Configuración de GitHub Actions para integración continua.

agotamiento-stock/
├── README.md
├── docs/
│   └── diseño_tecnico.docs
│   └── Planificacion_PEMBOK.
│   └── Diagramas
├── scripts/
│   ├── ingesta.py
│   ├── limpieza.py
│   ├── transformacion.py
│   └── entrenamiento.py
├── data/
│   └── dialogo.csv
│   └── context.md
├── docker-compose.yml

## Cómo ejecutar el sistema (entorno ya instalado)

1. Clonar el repositorio: git clone [URL_del_repositorio].

2. Activar entorno virtual: source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows).

3. Levantar Base de Datos: Ejecutar el contenedor de PostgreSQL con docker run.

4. Instalar dependencias: pip install -r requirements.txt.

5. Ejecutar Pipeline: Correr manualmente scripts de simulación y entrenamiento: python scripts/[nombre_script].py

## Documentación técnica

El sistema cuenta con un diagrama técnico de la solución que ilustra el flujo de datos y la relación entre componentes, así como un diccionario de datos que define los atributos de personalidad y estados almacenados.
El README.md en GitHub actúa como punto de entrada para comprender el funcionamiento y la ejecución

## Equipo

- Integrante 1 - Arquitectura de Datos e infraestructura
-Diseño y gestión de la base de datos PostgreSQL.
-Scripts de ingesta, limpieza y validación de datos de comportamiento.
-Configuración de Docker, CI/CD y despliegue en Render.

- Integrante 2 - Inteligencia Artificial y Documentación.
  
-Modelado de la lógica de personalidad y entrenamiento con LangChain/ML.
-Desarrollo de la simulación de interacción y demo visual.
-Liderazgo de la documentación técnica (Diseño y Planificación PMBOK)
