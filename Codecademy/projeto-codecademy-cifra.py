alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_size = len(alphabet)

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

def phrase_conversion(message, keyword):
    keyword_len = len(keyword)
    conv_msg = ''
    keyword_index = 0
    for letter in message.lower():
        if letter in alphabet:
            real_index = keyword_index % keyword_len
            conv_msg += keyword[real_index]
            keyword_index += 1
        else:
            conv_msg += letter
    return conv_msg

def vignere_cipher_encoder(phrase, keyword):
    coded_string = ''
    converted_phrase = phrase_conversion(phrase, keyword)
    for index_phrase, phrase_letter in enumerate(phrase.lower()):
        converted_phrase_letter = converted_phrase[index_phrase]
        if phrase_letter in alphabet or converted_phrase_letter in alphabet:
            for index_alphabet, letter_alphabet in enumerate(alphabet):
                if phrase_letter == letter_alphabet:
                    index_letter_phrase = int(index_alphabet)
                elif converted_phrase_letter == letter_alphabet:
                    index_letter_converted_phrase = int(index_alphabet)
                else:
                    pass
            index_run = index_letter_phrase - index_letter_converted_phrase
            index_run = list_size - index_run
            index_map = (list_size - index_run) % list_size
            coded_string += alphabet[index_map]
        else:
            coded_string += phrase_letter
    return coded_string

def vignere_cipher_decoder(phrase, keyword):
    coded_string = ''
    converted_phrase = phrase_conversion(phrase, keyword)
    for index_phrase, phrase_letter in enumerate(phrase.lower()):
        converted_phrase_letter = converted_phrase[index_phrase]
        if phrase_letter in alphabet or converted_phrase_letter in alphabet:
            for index_alphabet, letter_alphabet in enumerate(alphabet):
                if phrase_letter == letter_alphabet:
                    index_letter_phrase = int(index_alphabet)
                elif converted_phrase_letter == letter_alphabet:
                    index_letter_converted_phrase = int(index_alphabet)
                else:
                    pass
            index_run = index_letter_phrase + index_letter_converted_phrase
            index_run = list_size + index_run
            index_map = (list_size + index_run) % list_size
            coded_string += alphabet[index_map]
        else:
            coded_string += phrase_letter
    return coded_string
mes = 'barry is the spy'
keyy = 'dog'
#teste = phrase_conversion(mes, keyy)
teste_2 = vignere_cipher_encoder(mes, keyy)
print(mes)
#print(teste)
print(teste_2)




        
