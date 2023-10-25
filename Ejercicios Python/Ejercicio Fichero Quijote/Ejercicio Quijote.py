#!/usr/bin/env python
# coding: utf-8

# In[13]:


f = open('el_quijote.txt')


# In[12]:


# Ejercicio 1
# numero de palabras

with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    contenido = f.read()

    palabras = contenido.split()
    numWords = len(palabras)

print(f'El quijote tiene {numWords} palabras.')


# In[13]:


# Ejercicio 2
# Encontrar el numero de lineas
with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    num_lineas = sum(1 for _ in f)
    
print(f"El quijote tiene {num_lineas} líneas.")   


# In[14]:


# Ejercicio 3
# Crear una tabla de traducción para reemplazar los signos por espacios
# Encontrar la palabra más larga en el archivo:
import string

with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    
signos = string.punctuation    
tradTable = str.maketrans(signos, ' ' * len(signos))
    
    
content = content.translate(tradTable)
words = content.split()

longWord = max(words, key=len)
maxLetters = len(longWord)

shortWord = min(words, key=len)
minLetters = len(shortWord)

print(f'La palabra más larga en el Quijote es: "{longWord}", con {maxLetters} letras.\nLa palabra más corta en el Quijote es: "{shortWord}", con {minLetters} letra.')
    
    
    


# In[15]:


# Ejercicio 4
# Encontrar las líneas que contienen la palabra:

with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    content = f.read()

word1 = 'Dulcinea'
word2 = 'Sancho'
word3 = 'Rocinante'

line1 = []
line2 = []
line3 = []

lines = content.splitlines()
for i in lines:
    i = i.strip()
    if word1 in i:
        line1.append(i)
    if word2 in i:
        line2.append(i)
    if word3 in i:
        line3.append(i)

        
print(f'Se encontraron {len(line1)} líneas que contienen la palabra {word1}.')
print(f'Se encontraron {len(line2)} líneas que contienen la palabra {word2}.')
print(f'Se encontraron {len(line3)} líneas que contienen la palabra {word3}.')


# In[16]:


# Ejercicio 5
# Contar el número de palabras distintas en el archivo:

# El archivo contiene 15601 palabras distintas.

import string

sign = string.punctuation
tradTable = str.maketrans(sign, ' ' * len(sign))

with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.translate(tradTable)
    words = content.split()
    new = set(words)
    
print(f'El quijote tiene {len(new)} palabras distintas.')


# In[17]:


# Ejercicio 6
#Encontrar las palabras que aparecen con mayor frecuencia en el archivo:
import string
from collections import Counter

with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    content = f.read()

sign = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
text = content.translate(sign)
word = text.split()
wordCount = Counter(word)
mostUsed = wordCount.most_common(30)
    

print('Las palabras mas frecuentes son: \n')
for word, count in mostUsed:
    print(f'- {word}: {count} veces\n')


# In[18]:


# Ejercicio 7
#Contar el número de apariciones de cada letra en el archivo:
import string
from collections import Counter

with open('el_quijote.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.lower()
    content = content.replace(' ', '')
    
    total = Counter(content)
    order = sorted(total.items())
    
    
print('Número de apariciones de cada letra en el quijote:')
for i, x in order:
    print(f'- {i}: {x} veces.')


# In[19]:


# Ejercicio 8
# Escribir los resultados en un nuevo archivo

with open('resultados.txt', 'w', encoding='utf-8') as f:
    f.write(f'RESULTADOS Ejercicio Fichero Quijote!!!!\n')
    f.write(f'\nEl quijote tiene {numWords} palabras.\n')
    f.write(f'\nEl quijote tiene {num_lineas} líneas.\n')
    f.write(f'\nEl quijote tiene {len(words)} palabras distintas.\n')
    f.write(f'\nLa palabra más larga en el Quijote es: "{longWord}", con {maxLetters} letras.\nLa palabra más corta en el Quijote es: "{shortWord}", con {minLetters} letra.\n')
    f.write(f'\nSe encontraron {len(line1)} líneas que contienen la palabra {word1}.\n')
    f.write(f'Se encontraron {len(line2)} líneas que contienen la palabra {word2}.\n')
    f.write(f'Se encontraron {len(line3)} líneas que contienen la palabra {word3}.\n')
    f.write(f'\nLas palabras más frecuentes son:')
    for word, count in mostUsed:
        f.write(f'- {word}: {count} veces\n')
        
    f.write(f'\nNúmero de apariciones de cada letra en el quijote:\n')
    for i, x in order:
        f.write(f'- {i}: {x} veces.\n')

    


# In[ ]:




