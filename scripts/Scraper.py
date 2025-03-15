import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pd.set_option('display.max_colwidth', None)

def extraer_datos(codigo_inicial, codigo_final=None):
    """
    Función que extrae información de estudiantes en un rango de códigos y la guarda en un DataFrame.

    Parámetros:
    - codigo_inicial (int): Primer código de matrícula a consultar.
    - codigo_final (int): Último código de matrícula a consultar.

    Retorna:
    - DataFrame con los datos extraídos.
    """

    # Configuración del WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    datos = []

    
    if codigo_final is None:
        codigo_final = codigo_inicial
    try:
        for codigo in range(codigo_inicial, codigo_final + 1):
            print(f"Consultando código: {codigo}")

            driver.get("http://websecgen.unmsm.edu.pe/carne/carne.aspx")
            wait = WebDriverWait(driver, 10)

            # Ingresar número de matrícula
            input_matricula = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtUsuario")))
            driver.execute_script("arguments[0].value = arguments[1];", input_matricula, str(codigo))
            driver.execute_script("arguments[0].blur();", input_matricula)

            # Click en botón Consultar
            boton_consultar = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_cmdConsultar")))
            boton_consultar.click()

            # Esperar a que se carguen los datos básicos (o validar si no existen)
            try:
                wait.until(lambda d: d.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFacultad").get_attribute("value") != "")
                facultad = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFacultad").get_attribute("value")
                programa = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPrograma").get_attribute("value")
                alumno = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAlumno").get_attribute("value")

                # Extraer estado y fecha
                try:
                    estado = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_gvEstadoCarne"]/tbody/tr[2]/td[2]').text
                    fecha = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_gvEstadoCarne"]/tbody/tr[2]/td[3]').text
                except:
                    estado = "No tramitado"
                    fecha = None  

                # Extraer URL de la imagen
                try:
                    img_element = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_imgAlumno")))
                    img_src = img_element.get_attribute("src")
                except:
                    img_src = None  

            except:
                # Si no se encuentra el código, guardar valores vacíos
                alumno, facultad, programa, estado, fecha, img_src = None, None, None, None, None, None

            datos.append([codigo, alumno, facultad, programa, estado, fecha, img_src])
            time.sleep(1)

    except Exception as e:
        print(f"Ocurrió un error: {e}")

    finally:
        driver.quit()

    # Convertir lista en DataFrame
    df = pd.DataFrame(datos, columns=["Código", "Alumno", "Facultad", "Programa", "Estado", "Fecha", "Imagen"])
    return df


df_resultado = extraer_datos(22200001,22200340)


df_resultado.to_csv("EstudiantesFISI.csv", index=False)  # Guardar como CSV