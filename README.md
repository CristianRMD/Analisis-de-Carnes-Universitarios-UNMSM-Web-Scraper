🎓 Análisis de Carnés Universitarios – UNMSM Web Scraper 🕸️
📖 Descripción
Este proyecto implementa web scraping con Selenium en Python para extraer información de carnés universitarios desde la página oficial de la Universidad Nacional Mayor de San Marcos (UNMSM):
🔗 websecgen.unmsm.edu.pe/carne/carne.aspx

El script automatiza la extracción de datos de estudiantes de la Facultad de Ingeniería de Sistemas e Informática (Base 22), obteniendo información como:
✔ Código de alumno
✔ Nombre completo
✔ Facultad y escuela profesional
✔ Estado del carné universitario (Tramitado / No Tramitado)

Los datos extraídos se convierten en CSV y posteriormente se analizan en Power BI.

🎯 Objetivo
✅ Automatizar la recopilación de datos sobre el estado de los carnés universitarios.
✅ Almacenar los datos en CSV para su posterior análisis.
✅ Visualizar patrones y estadísticas en Power BI según la escuela profesional.

🚀 Instalación y Ejecución
1️⃣ Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/tu-usuario/unmsm-carne-webscraper.git
cd unmsm-carne-webscraper
2️⃣ Instalar dependencias
Asegúrate de tener pip instalado y luego ejecuta:

bash
Copiar
Editar
pip install -r requirements.txt
3️⃣ Configurar Selenium 🛠️
Este script usa Selenium, por lo que necesitas el WebDriver de tu navegador.
🔹 Si usas Chrome, descarga Chromedriver desde: https://chromedriver.chromium.org/downloads
🔹 Guarda el chromedriver.exe en la carpeta del proyecto o en una ruta accesible.

4️⃣ Ejecutar el Script 🖥️
Para iniciar la extracción de datos:

bash
Copiar
Editar
python scripts/scraper.py
Esto generará un archivo CSV con los datos recolectados.

📋 Funcionalidades
🔹 Automatización con Selenium: Simula la interacción con la web ingresando códigos de alumnos.
🔹 Extracción de datos: Obtiene el nombre, facultad, escuela y estado del carné universitario.
🔹 Filtrado de datos: Se almacenan solo registros de la Facultad de Ingeniería de Sistemas e Informática - Base 22.
🔹 Almacenamiento en CSV: Los datos extraídos se guardan en carnes_unmsm.csv.
🔹 Visualización en Power BI: Se importan los datos en Power BI para el análisis gráfico.

🔨 Tecnologías Utilizadas
🐍 Python – Para la automatización del scraping
🌐 Selenium – Para interactuar con la web
📄 Pandas – Para el procesamiento y almacenamiento en CSV
📊 Power BI – Para la visualización de los datos
