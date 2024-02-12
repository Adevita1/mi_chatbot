import re 
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    responce = check_all_messages(split_message)
    return responce

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hola', ['hola', 'Buen dia', 'Buenas tardes'], single_response=True)
    response('Estoy bien y vos?', ['como', 'estas','como', 'te va', 'como', 'te sientes'], required_words=['como'])
    response('Estamos ubicados en la Ciudad de Buenos Aires, Argentina', ['Donde te encuentras?', 'Cual es tu ubicacion?', 'De donde eres?', 'Ubicacion', 'Direccion', 'localidad', 'domicilio'])
    response('Cualquier otra consulta, estoy para ayudarte', ['Muchas gracias', 'Hasta la proxima', 'Chau', 'Gracias'])
    response('Eso suena interesante, ¿puedes contarme más?', ['Cuéntame más', 'Dime más', '¿Qué más?'])
    response('Lo siento, no puedo hacer eso', ['¿Puedes hacer esto por mí?', '¿Me harías un favor?', '¿Podrías ayudarme con esto?'])
    response('Creo que sí', ['¿Puedes hacer esto?', '¿Crees que podrías hacerlo?', '¿Es posible?'])
    response('Me alegra escuchar eso', ['Eso es genial', 'Me alegra', 'Qué bueno'])
    response('¿Qué opinas?', ['¿Cuál es tu opinión?', '¿Tienes alguna opinión sobre esto?', '¿Qué piensas sobre eso?'])
    response('No estoy seguro de entender', ['No entiendo', '¿Puedes explicar eso?', '¿Puedes ser más claro?'])
    response('Eso no suena bien', ['Eso es malo', 'Oh no', 'Qué pena'])
    response('¿Qué tal si lo intentas?', ['¿Por qué no lo intentas?', '¿Has intentado eso?', 'Podrías intentarlo'])
    response('Eso es interesante', ['Interesante', 'Me gusta eso', 'Qué interesante'])
    response('¿Qué tal si lo pensamos un poco más?', ['Deberíamos pensarlo más', '¿Has pensado en eso?', 'Quizás deberíamos pensar en esto'])
    response('¿Qué quieres decir con eso?', ['¿Puedes explicar eso?', '¿Qué quieres decir?', 'No entiendo lo que quieres decir'])
    response('Entiendo lo que dices', ['Te entiendo', 'Entiendo', 'Lo veo'])
    response('Lo siento, no puedo hacer eso', ['No puedo hacer eso', 'No puedo ayudarte con eso', 'Lo siento, no puedo'])
    response('¿Qué pasa?', ['¿Algo anda mal?', '¿Puedo ayudarte?', '¿Qué sucede?'])
    response('Me parece bien', ['Está bien', 'Me parece bien', 'De acuerdo'])
    response('¿Qué te parece?', ['¿Qué piensas?', '¿Cuál es tu opinión?', '¿Qué crees?'])
    response('Vamos a ver', ['Vamos a ver', 'Veremos', 'Esperemos'])
    response('¿Podrías repetir eso?', ['¿Puedes repetir?', 'No entendí eso', '¿Puedes decirlo de nuevo?'])
    response('No estoy seguro', ['No estoy seguro', 'No lo sé', 'No tengo idea'])
    response('¿Puedo ayudarte con algo más?', ['¿Hay algo más en lo que pueda ayudarte?', '¿Necesitas algo más?', '¿Puedo hacer algo más por ti?'])
    response('Lo siento, no puedo hacer eso', ['No puedo hacer eso', 'Lo siento, no puedo', 'No puedo ayudarte con eso'])
    response('¿Cómo te sientes hoy?', ['¿Cómo estás hoy?', '¿Te sientes bien?', '¿Cómo va tu día?'])
    response('¿Puedes explicar eso en más detalle?', ['¿Puedes detallarlo más?', 'Necesito más información', '¿Puedes expandir eso?'])
    response('¿Qué tienes en mente?', ['¿Qué estás pensando?', '¿Tienes alguna idea?', '¿Qué tienes en mente?'])
    response('¿Cómo ha sido tu día?', ['¿Cómo ha sido tu día?', '¿Qué has hecho hoy?', '¿Qué tal ha ido tu día?'])

    best_match = max(highest_prob, key=highest_prob.get)

    return unknown() if highest_prob[best_match] < 1 else best_match
    
def unknown():
    response = ['me repetis la pregunta?', 'no entiendo la pregunta', 'me podrias repetir la consulta?', 'googlealo a ver que encontras'][random.randrange(3)]
    return response

while True:
    user_input = input('you: ')
    response = get_response(user_input)
    print('Bot: ' + str(response))