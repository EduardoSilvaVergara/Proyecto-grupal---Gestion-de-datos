# 📊 Pipeline de Datos – Virtual Reality Experiences

## 📌 Descripción del Proyecto
Este proyecto implementa un pipeline de procesamiento de datos orientado a mejorar la calidad de un dataset de experiencias de realidad virtual. El flujo abarca desde la obtención de los datos hasta su validación y generación de resultados finales, asegurando que la información sea confiable para análisis posteriores.

El proceso fue desarrollado en un entorno de **Google Colab**, utilizando herramientas de análisis de datos en Python.

---

## 📂 Dataset
Se utilizó un dataset proveniente de Kaggle, el cual contiene información sobre usuarios y su interacción con experiencias de realidad virtual.

Las principales variables incluyen:

- Identificación del usuario  
- Edad  
- Género  
- Dispositivo de realidad virtual utilizado  
- Duración de la experiencia  
- Nivel de mareo (Motion Sickness)  
- Nivel de inmersión  

---

## ⚙️ Enfoque de la Implementación

El pipeline fue diseñado bajo un enfoque estructurado de calidad de datos, separando claramente las etapas de procesamiento para facilitar su comprensión, mantenimiento y reutilización.

---

## 🔄 Etapas del Pipeline

### 1. Ingesta de Datos
Los datos son obtenidos desde Kaggle mediante su API, permitiendo automatizar la descarga e incorporación del dataset al entorno de trabajo.

---

### 2. Limpieza y Transformación
En esta etapa se preparan los datos para su validación:

- Se eliminan espacios innecesarios en variables de texto  
- Se normalizan formatos (por ejemplo, valores en minúsculas)  
- Se convierten los datos a sus tipos correspondientes (numéricos)  
- Se manejan valores inválidos transformándolos en valores nulos  

Esto permite estandarizar el dataset y evitar errores en etapas posteriores.

---

### 3. Validación Estructural
Se verifica que los datos cumplan con la estructura esperada:

- Campos numéricos correctamente definidos  
- Variables obligatorias no vacías  
- Integridad básica de cada registro  

Los registros que no cumplen con estos criterios son clasificados como errores estructurales.

---

### 4. Validación Semántica
Se evalúa la coherencia lógica de los datos:

- Rangos válidos para edad  
- Valores positivos para la duración  
- Escalas definidas para indicadores como mareo e inmersión  
- Validación de categorías permitidas (por ejemplo, género)  

Esta etapa permite detectar datos que, aunque estructuralmente correctos, no tienen sentido en el contexto del negocio.

---

### 5. Generación de Resultados
Finalmente, los datos se separan en dos conjuntos:

- **Datos válidos**: cumplen con todas las validaciones  
- **Datos con errores**: contienen inconsistencias estructurales o semánticas  

Ambos conjuntos se exportan como archivos independientes, facilitando su análisis y tratamiento posterior.

---

## 📊 Resultados Esperados

El pipeline produce:

- Un dataset limpio y validado listo para análisis  
- Un dataset con errores identificado para revisión  

Esto permite mejorar la toma de decisiones basada en datos confiables.

---

## 💡 Consideraciones

- Se diferencia claramente entre errores estructurales y semánticos  
- El pipeline es escalable y adaptable a otros datasets  
- Se prioriza la calidad de los datos antes del análisis  

---

## 📈 Posibles Mejoras

- Incorporar validaciones adicionales específicas del dominio  
- Integrar visualizaciones para análisis exploratorio  
- Automatizar completamente el flujo de procesamiento  
- Conectar el pipeline a sistemas de almacenamiento o bases de datos  

---
