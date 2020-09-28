import os

#FUNCIÓN

#Esta funcion permite sacar los archivos de las carpetas y sub carpetas en las que se encuentre a un directorio específico.
#Para sacar todas las fotos y o videos de una carpeta de iCloud exportada y lograr encontrar los archivos dentro de esa carpeta de
#gran tamaño para eliminar lo más pesado. 


#variables para los directorios de destino y fuente
target_folder = r'xxx'
source_folder = r'yyy'

def move_files(source_folder, target_folder):
    try:
        for path, dir, files in os.walk(source_folder):
            if os.path.ismount():
                if files:
                  for file in files:
                       if not os.path.isfile(target_folder + file):
                            os.rename(path + '\\' + file, target_folder + file)
        print('Los archivos se movieron...')
    except Exception as e:
        print (e)

move_files(source_folder, target_folder)

