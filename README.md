# Pre-Entrega Automation Testing - SauceDemo

Proyecto de automatización web realizado con Selenium WebDriver, Python y Pytest.

---

# Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Visual Studio Code
- Git & GitHub

---

# Funcionalidades automatizadas

## Login exitoso
- Validación de acceso con credenciales válidas.
- Verificación de URL.
- Verificación de título "Products".

## Catálogo de productos
- Validación de productos visibles.
- Validación de menú lateral.
- Validación de filtro de productos.

## Carrito de compras
- Agregar producto al carrito.
- Validación del contador del carrito.
- Verificación del producto agregado.

---

# Estructura del proyecto

```bash
tests/
utils/
reports/
datos/
```

---

# Instalación

## Crear entorno virtual

```bash
python -m venv venv
```

## Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar pruebas

```bash
pytest -v
```

---

# Generar reporte HTML

```bash
pytest -v --html=reports/reporte.html
```

---

# Evidencias

## Screenshots automáticos
Se generan automáticamente en caso de error:

```bash
reports/screenshots/
```

## Logs
Los logs de ejecución se almacenan en:

```bash
reports/logs/
```

---

# Autor

Angel Garcia