Esta aplicación realiza el scraping de las opciones sobre el MINI IBEX desde la página oficial de MEFF, calcula su volatilidad implícita mediante el modelo de Black-Scholes y permite visualizar el skew de volatilidad usando Streamlit.

## Estructura del proyecto

PRACTICA_ENTORNO_CLOUD  
├── scraping.py          # Extrae datos de opciones y futuros  
├── volatilidad.py       # Calcula la volatilidad implícita  
├── graficos.py          # Dibuja el skew de volatilidad  
├── streamlit_app.py     # Aplicación web en Streamlit  
├── requirements.txt     # Dependencias del proyecto  
└── README.md            # Documentación


---

###  USO: Cómo lanzar la aplicación

```markdown
## Cómo ejecutar la aplicación

1. Asegurarse de tener instalado `streamlit`.

2. Ejecutar:
```bash
python -m streamlit run streamlit_app.py


---

### 6. FUNCIONALIDAD

```markdown
## Funcionamiento de la aplicación

- Obtiene automáticamente datos de opciones y futuros del MINI IBEX desde MEFF.
- Calcula la volatilidad implícita de cada opción usando Black-Scholes.
- Muestra gráficamente el skew de volatilidad (Volatilidad vs Strike) para cada fecha de vencimiento.
- Permite seleccionar el vencimiento de forma interactiva.
## Requisitos

- Navegador actualizado (Google Chrome, etc.)
- Tener instalado Python 3.12
- Tener instalado el driver de Selenium (se instala automáticamente con WebDriver Manager)
- Librerías del requirements.txt
## Notas importantes

- La tasa de interés utilizada en Black-Scholes es 0%.
- El precio del subyacente es el precio del futuro más cercano al día actual.
- Los precios de opciones y futuros son obtenidos en tiempo real cada vez que se accede a la aplicación.
