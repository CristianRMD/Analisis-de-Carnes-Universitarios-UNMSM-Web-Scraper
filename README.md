# 🎓 Análisis de Carnés Universitarios – UNMSM Web Scraper 🕸️

## 📖 Descripción  
Este proyecto implementa **web scraping con Selenium en Python** para extraer información de carnés universitarios desde la página oficial de la **Universidad Nacional Mayor de San Marcos (UNMSM)**:  
🔗 [websecgen.unmsm.edu.pe/carne/carne.aspx](http://websecgen.unmsm.edu.pe/carne/carne.aspx)  
![image](https://github.com/user-attachments/assets/7980fcf4-bcb1-4dd8-a2dc-e9f6ae8ff3ee)

El script automatiza la extracción de datos de estudiantes de la **Facultad de Ingeniería de Sistemas e Informática (Base 22)**, obteniendo información como:  
- ✔ **Código de alumno**  
- ✔ **Nombre completo**  
- ✔ **Facultad y escuela profesional**  
- ✔ **Estado del carné universitario** (Tramitado / No Tramitado)  

Los datos extraídos se convierten en **CSV** y posteriormente se analizan en **Power BI**.  

---

## 🎯 Objetivo  
✅ **Automatizar** la recopilación de datos sobre el estado de los carnés universitarios.  
✅ **Almacenar** los datos en **CSV** para su posterior análisis.  
✅ **Visualizar** patrones y estadísticas en **Power BI** según la escuela profesional.  

---

## 🚀 Instalación y Ejecución  

### 1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/CristianRMD/unmsm-carne-webscraper.git
cd unmsm-carne-webscraper
