# importar la libreria nltk
import nltk

# descargar el paquete de stopwords
nltk.download('stopwords')

# importar las stopwords
from nltk.corpus import stopwords

#se crea una lista de stopwords
list_stopwords = stopwords.words('english')

# imprimir las stopwords
# print(list_stopwords)

#se crea una lista de palabras
print(list_stopwords)








