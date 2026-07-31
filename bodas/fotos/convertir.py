from PIL import Image
import glob
import os

print("Iniciando conversión a WebP...")

# Busca todos los archivos JPG en la carpeta actual y en las subcarpetas (miniaturas y alta-resolucion)
archivos = glob.glob('**/*.jpg', recursive=True)

for archivo in archivos:
    try:
        # Abrir la imagen original
        img = Image.open(archivo)
        
        # Crear el nuevo nombre de archivo cambiando .jpg a .webp
        nuevo_nombre = os.path.splitext(archivo)[0] + '.webp'
        
        # Guardar como WebP optimizado
        # quality=80 es un balance excelente entre peso y calidad
        # method=6 exprime al máximo la compresión
        img.save(nuevo_nombre, 'webp', quality=80, method=6)
        
        print(f"✅ Convertido: {nuevo_nombre}")
    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")

print("¡Proceso terminado con éxito!")