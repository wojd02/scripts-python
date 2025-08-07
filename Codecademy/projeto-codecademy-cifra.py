alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def message_encoder(message, offset=10):
    encoded_msg = ''
    for index_msg, letter_msg in enumerate(message.lower()):
        for index_alphabet, letter_alphabet in enumerate(alphabet):
            if letter_msg == letter_alphabet:
                real_index = (index_alphabet - offset) % list_size
                encoded_msg += alphabet[real_index]
                break
            elif letter_msg not in alphabet:
                encoded_msg += letter_msg
                break
            else:
                pass
    return encoded_msg

def message_decoder(message, offset=10):
    decoded_msg = ''
    for index_msg, letter_msg in enumerate(message.lower()):
        for index_alphabet, letter_alphabet in enumerate(alphabet):
            if letter_msg == letter_alphabet:
                real_index = (index_alphabet + offset) % list_size
                decoded_msg += alphabet[real_index]
                break
            elif letter_msg not in alphabet:
                decoded_msg += letter_msg
                break
            else:
                pass
    return decoded_msg

list_size = len(alphabet)

msg = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
scn_msg = """ O poeta é um fingidor.
Finge tão completamente
Que chega a fingir que é dor
A dor que deveras sente.

E os que lêem o que escreve,
Na dor lida sentem bem,
Não as duas que ele teve,
Mas só a que eles não têm.

E assim nas calhas da roda
Gira, a entreter a razão,
Esse comboio de corda
Que se chama o coração.
"""

my_msg = message_encoder(msg)
print(my_msg)


