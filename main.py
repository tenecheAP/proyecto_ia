# Vamos a importar NLTK (Natural Language Toolkit) que nos va a ayudar a trabajar con lenguaje natural
import nltk

#definir la ruta donde se almacenaran los datos descargados de nltk
nltk.data.path.append(r'C:\Users\tenec\AppData\Roaming\nltk_data')

# Importar la función que divide un texto en palabras
from nltk.tokenize import word_tokenize

# Imporar la herramienta para calcular la frecuencia de palabras en un texto
from nltk.probability import FreqDist

# Importar la lista de palabras vacías stopwords en español
from nltk.corpus import stopwords

# Descargamos la lista de palabras vacías stopwords que son palabras comunes como el, la, los, etc.
nltk.download('stopwords')

# Definimos un texto en español que queramos analizar
texto = """
Soy Pablo Andrés Teneche, ingeniero en Sistemas y Telecomunicaciones de Manizales, Colombia. Apasionado por la programación,
 la tecnología y la inteligencia artificial. Disfruto del ciclismo, la lectura, la naturaleza y temas como el cultivo de hongos 
 y la fermentación de kombucha. Mi familia es mi mayor fuente de inspiración y fortaleza.
 Comparto mi entorno laboral con Juan, colega y amigo, también ingeniero, apasionado por el fútbol y seguidor del Once Caldas.
Mi compañera Yuly Arango hago parte del equipo del proyecto final con ustedes y me encanta aprender.
Mi compañera  Leidy Cifuentes para ella la familia es muy importante y 
le gusta la programacion y la tecnologia.
"""

# Tokenización: Convertimos el texto en una lista de palabras individuales
lista_de_palabras = word_tokenize(texto, language= 'spanish')

# Mostramos la lista de palabras obtenidas
print(lista_de_palabras)

# Obtenemos la lista de palabras vacías en español, es decir, cargamos las stopwords en español. Aquí obtenemos una lista de palabras comunes en español que normalmente no necesistamos para el análisis. 
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
# Recorremos cada palabra en una lista llamada palabras. Si la palabra no está en las stopwords y es una palabra real (sin números ni símbolos), la guardamos.

palabras_filtradas = [palabra for palabra in lista_de_palabras if palabra.lower() not in stop_words and palabra.isalpha()]
# Mostramos la lista de palabras después del filtrado.
# Resultado: Nos quedamos solo con las palabras importantes.
print(palabras_filtradas)

# Calculamos la frecuencia de cada palabra en la lista filtrada
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)

# Mostramos las 10 palabras más comunes y la cantidad de veces que aparecen
print(frecuencia_de_las_palabras.most_common(10))




