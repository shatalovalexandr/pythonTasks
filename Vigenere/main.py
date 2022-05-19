import math


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.v_table = {}
        for i in range(len(alphabet)):
            v_str = self.alphabet[i:] + self.alphabet[:i]
            self.v_table[self.alphabet[i]] = v_str

    def encode(self, text):
        if not text.islower():
            return text
        A = list(zip(self.key * math.ceil(len(text) / len(self.key)), text))
        key1 = "".join(i[0] for i in A)

        ciph = ''
        i = 0
        for j in text:
            if j not in self.alphabet:
                ciph += j
                i += 1
                continue
            str1 = self.v_table[j]
            num1 = self.alphabet.find(key1[i])
            i += 1
            ciph += str1[num1]
        return ciph

    def decode(self, text):
        if not text.islower():
            return text
        A = list(zip(self.key * math.ceil(len(text) / len(self.key)), text))
        key1 = "".join(i[0] for i in A)
        ciph = ''
        i = 0
        for j in key1:
            if j not in self.alphabet:
                ciph += j
                i += 1
                continue
            str1 = self.v_table[j]
            num1 = str1.find(text[i])
            i += 1
            ciph += self.alphabet[num1]
        return ciph


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

# print(c.encode('CODEWARS'))
print(c.encode('codewars'))
print(c.decode('rovwsoiv'))