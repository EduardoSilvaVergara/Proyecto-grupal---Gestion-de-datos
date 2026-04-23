
# 📊 Pipeline de Datos – Virtual Reality Experiences

## 📌 Descripción del Proyecto
Este proyecto implementa un pipeline de datos que realiza las etapas de **ingesta, limpieza y transformación** sobre un dataset de experiencias de realidad virtual.

El objetivo es obtener un dataset limpio, consistente y listo para análisis, aplicando buenas prácticas de procesamiento de datos, modularidad y trazabilidad.

---

## 📥 Fuente de Datos
El dataset fue obtenido desde Kaggle:

https://www.kaggle.com/datasets/aakashjoshi123/virtual-reality-experiences

Contiene información relacionada con experiencias de realidad virtual, incluyendo características descriptivas que permiten su análisis posterior.

---

## ⚙️ Tecnologías Utilizadas

- Python 3
- Pandas
- NumPy
- Google Colab
- Kaggle API

---

## 🏗️ Estructura del Proyecto
project/
│
├── data/
│ ├── raw/ # Datos originales descargados desde Kaggle
│ └── processed/ # Dataset limpio y transformado
│ └── vr_clean.csv
│
├── notebooks/
│ └── pipeline_colab.ipynb # Notebook con el pipeline completo
│
├── README.md
└── requirements.txt


---

## 🔄 Pipeline de Datos

### 1️⃣ Ingesta de Datos
- Descarga del dataset desde Kaggle utilizando la API (`kaggle.json`)
- Descompresión automática del archivo `.zip`
- Carga del archivo CSV en un DataFrame de Pandas

---

### 2️⃣ Limpieza de Datos
Se aplicaron las siguientes operaciones:

- Eliminación de registros duplicados
- Eliminación de valores nulos
- Eliminación de filas vacías o irrelevantes
- Validación básica de consistencia de datos

---

### 3️⃣ Transformación de Datos
Se realizaron las siguientes transformaciones:

- Estandarización de texto:
  - Conversión a minúsculas
  - Eliminación de espacios innecesarios
- Conversión de tipos de datos:
  - Variables numéricas
  - Variables categóricas
- Creación de columnas derivadas (cuando aplica)
- Preparación de los datos para análisis posterior

---

### 4️⃣ Almacenamiento (Output)
El dataset limpio se guarda en:


data/processed/vr_clean.csv

Este archivo representa la versión final lista para análisis.

---

## ▶️ Ejecución del Proyecto

### Requisitos previos
- Cuenta en Kaggle
- Archivo `kaggle.json` (API Key)

### Pasos en Google Colab

1. Subir archivo `kaggle.json`
2. Ejecutar instalación de dependencias:

!pip install kaggle pandas numpy

3. Descargar dataset desde Kaggle
4. Ejecutar pipeline completo
5. Descargar archivo limpio generado

---

## 🧪 Buenas Prácticas Aplicadas

- Separación de datos crudos y procesados
- Código reproducible en entorno Colab
- Uso de control de versiones (Git)
- Mensajes de commit descriptivos
- Documentación clara del proceso

---

## 📌 Control de Versiones (Ejemplo de Commits)

- `feat: ingesta de dataset desde kaggle`
- `feat: limpieza inicial de datos`
- `feat: transformación de variables`
- `feat: generación de dataset limpio`

---

## ⚠️ Consideraciones

- El archivo `kaggle.json` contiene credenciales y no debe compartirse
- El dataset original no debe modificarse directamente
- Todas las transformaciones se aplican sobre copias del dataset

---

## 📊 Resultado

Se obtiene un dataset limpio, consistente y estructurado, listo para análisis exploratorio o modelamiento.

---

## 👨‍💻 Autor

Proyecto desarrollado como parte de actividad académica de pipeline de datos.
