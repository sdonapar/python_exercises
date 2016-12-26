#!/usr/bin/env python

"""In cryptography, a Caesar cipher is a very simple encryption techniques
in which each letter in the plain text is replaced by a letter some fixed
number of positions down the alphabet. For example, with a shift of 3,
A would be replaced by D, B would become E, and so on. The method is named
after Julius Caesar, who used it to communicate with his generals.
ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher
where the shift is 13."""

def get_alphabets():
        return [chr(num) for num in range(97,97+26)]

def gen_dict(rotation,encode=True):
    letters = get_alphabets()
    length = len(letters)
    start_pos = length*-1 + rotation
    end_pos =  start_pos + length
    pos = 0
    encode_dict = {}
    decode_dict = {}
    for x in range(start_pos,end_pos,1):
        encode_dict[letters[pos]] = letters[x]
        encode_dict[letters[pos].upper()] = letters[x].upper()
        decode_dict[letters[x]] = letters[pos]
        decode_dict[letters[x].upper()] = letters[pos].upper()
        pos += 1
    if encode:
        return encode_dict
    else:
        return decode_dict

def cipher_encode(inp_str):
    encode_dict = gen_dict(13)
    encoded_string = ''
    for letter in inp_str:
        encoded_string += encode_dict.get(letter,letter)
    return encoded_string

def cipher_decode(inp_str):
    decode_dict = gen_dict(13,encode=False)
    decoded_string = ''
    for letter in inp_str:
        decoded_string += decode_dict.get(letter,letter)
    return decoded_string

if __name__ == '__main__':
    enc_string = cipher_encode("This is a test.")
    print(enc_string)
    print(cipher_decode(enc_string))
    print(cipher_decode("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))
    




