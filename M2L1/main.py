# Y así es como podemos reescribir la totalidad de un archivo de texto
f = open('tarea.txt', 'w', encoding='utf-8')
text = 'Yo (el original)'
f.write(text)
f.close()