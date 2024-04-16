meme_dict = {
            'LOL': 'una respuesta a algo gracioso',
            'CRINGE':'algo raro o embarazoso',
            'ROFL': 'una respuesta a una broma',
            'SHEESH': 'ligera desaprobación',
            'CREEPY':'aterrador, siniestro',
            'AGGRO': 'ponerse agresivo/enojado',
            'LMAO': 'Algo te acaba de dar mucha risa',
            'BRUH': 'Algo te parecio aburrido o normalito',
            'STFU': 'Es una manera amable "guiño" de pedirle silencio a alguien que ha colmado tu paciencia',
            }

for i in range (5):
    word = input('Escribe la palabra que no entiendes, (En mayusculas)')
    if word in meme_dict:
        print('El significado de', word, 'es:', meme_dict[word])
    else:
        print('Ingresa una palabra valida o verifica que estes usando mayúsculas')
