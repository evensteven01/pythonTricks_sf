from time import sleep, time

def play(words):
    veces = 0
    tiempo_total = 0
    numero_correcto = 0
    for i in range(25):
        letter = words[random.randint(0,len(words)-1)]
        challenge = f'Encuentra la letra: {letter}\n'
        start = time()
        answer = input(challenge)
        veces += 1
        end = time()
        tiempo_de_ronda = end-start
        tiempo_total += tiempo_de_ronda
        if letter == answer:
            numero_correcto += 1
        print(f'Te tardastes {int(tiempo_de_ronda)} segundos para encontrar {letter} y respondistes {answer}')

    print(f'Respondieron {numero_correcto} de {veces} en {tiempo_total} con un promedio de {tiempo_total/veces}')

questions = [
    {
        'question': 'Que queres comer de cena?',
        'expected_answer': 'pizza',
        'match_answer': 'Esa es la comida favorita de tu tio!',
        'wrong_answer': 'A nu, mejor pizza!',
    },
    {
        'question': 'Cual es tu deporte favorito?',
        'expected_answer': 'futbol',
        'match_answer': 'Yo sabia que tu deporte favorita era futobl. Y tu jugador favorito es Messi!',
        'wrong_answer': 'Mentiroso! Yo se que es futbol',
    },
]

questions = []
for question in questions:
    q_text = question['question'] + '\n'
    q_text = q_text.lower()
    answer = input(q_text)
    expected_answer = question['expected_answer']
    match_answer = question['match_answer']
    wrong_answer = question['wrong_answer']
    if answer.lower() == expected_answer.lower():
        print(match_answer)
    else:
        print(wrong_answer)

import random
from threading import Timer

out_of_time = False
def time_ran_out():
    print('Se te acabo el tiempo!')
    out_of_time = True


t = Timer(5, time_ran_out)


type = 'word'
if type == 'letter':
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    play(alph)
elif type == 'word':
    words = 'Esto es una prueba de palabras Jimmy un chico inteligente Michel es una chica bella Nos gusta ir al rio zapatos verdes oscuro banano computadora kayla yanci chela yanci steven pua televisor'
    words = words.split()
    play(words)


