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
Soy pablo andres teneche y soy ingeniero de sistemas y telecomunicaciones 
soy de la ciudad de manizales, colombia, me gusta la programacion y la tecnologia
ademas me gussta el ciclismo y la naturaleza
las peliculas de aventura y accion, me gusta la inteligencia artificial.
"""

# Tokenización: Convertimos el texto en una lista de palabras individuales
palabras = word_tokenize(texto, language= 'spanish')

# Mostramos la lista de palabras obtenidas
print(palabras)

# Obtenemos la lista de palabras vacías en español, es decir, cargamos las stopwords en español. Aquí obtenemos una lista de palabras comunes en español que normalmente no necesistamos para el análisis. 
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
# Recorremos cada palabra en una lista llamada palabras. Si la palabra no está en las stopwords y es una palabra real (sin números ni símbolos), la guardamos.

palabras_filtradas = [palabras for palabras in palabras if palabras.lower() not in stop_words and palabras.isalpha()]

# Mostramos la lista de palabras después del filtrado.
# Resultado: Nos quedamos solo con las palabras importantes.
print(palabras_filtradas)

# Calculamos la frecuencia de cada palabra en la lista filtrada
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)

# Mostramos las 10 palabras más comunes y la cantidad de veces que aparecen
print(frecuencia_de_las_palabras.most_common(10))




