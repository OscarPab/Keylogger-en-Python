# Keylogger en Python

Este proyecto contiene un script de Python que implementa un keylogger utilizando la biblioteca `pynput`. El script realiza las siguientes funciones:

1. **Registrar las teclas presionadas:** Utiliza la biblioteca `pynput` para detectar y registrar las teclas presionadas por el usuario.
2. **Guardar las teclas en un archivo:** Guarda las teclas registradas en un archivo de texto con una marca de tiempo en el nombre del archivo.
3. **Manejo de teclas especiales:** Registra de manera especial las teclas `Enter`, `Space` y `Backspace`.

## Requisitos

- Python 3.x
- pynput

Puedes instalar la dependencia necesaria usando pip:

```sh
pip install pynput
