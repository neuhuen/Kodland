meme_dicc = {
    "LOL" : "una respuesta a algo gracioso",
    "CRINGE" : "algo raro o embarazoso",
    "ROFL" : "una respuesta a una broma",
    "SHEESH" : "ligera desaprobación",
    "CREEPY" : "aterrador, siniestro",
    "AGGRO" : "ponerse agresivo/enojado",
}

word = input("Escribe una palabra que no entiendas (En mayusculas)")

for i in range(5):
    if word in meme_dicc:
        print("La abreviacion" , word , "es:" , meme_dicc[word])
        print(" ")
        word = input("Escribe una palabra que no entiendas (En mayusculas)")
    else:
        print("La abreviacion" , word , "aun no esta añadida.")
        print(" ")
        word = input("Escribe una palabra que no entiendas (En mayusculas)")
