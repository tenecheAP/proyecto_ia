# importar la libreria nltk
import nltk

# descargar el paquete de stopwords
nltk.download('stopwords')

# importar las stopwords
from nltk.corpus import stopwords

#se crea una lista de stopwords
list_stopwords = stopwords.words('spanish')

# imprimir las stopwords
# print(list_stopwords)

#se crea una lista de palabras
list_words = input('Ingrese una frase: ')



#se crea una lista de palabras que no son stopwords
list_words_no_stopwords = [word for word in list_words if word not in list_stopwords]

#se imprime la lista de palabras que no son stopwords
print(list_words_no_stopwords)

