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


mes = 'Barry is the spy'
keyy = 'dog'
teste = phrase_conversion(mes, keyy)
print(mes)
print(teste)

coded_string = ''
for index_mes, let_1 in enumerate(mes.lower()):
    let_2 = teste[index_mes]
    for index_alphabet, letter_alphabet in enumerate(alphabet):
        if let_1 == letter_alphabet:
            count = int(index_alphabet)
        elif let_2 == letter_alphabet:
            count_2 = int(index_alphabet)
        else:
            pass
    final_count = (count - count_2) % list_size
    final_count = list_size - final_count
    print(final_count)
    coded_string += alphabet[final_count]
print(coded_string)
        
