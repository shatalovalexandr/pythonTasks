import math


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        A = list(zip(self.key * math.ceil(len(text) / len(self.key)), text))
        key1 = "".join(i[0] for i in A)

        ciph = ''
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                ciph += text[i]
                continue
            ciph += self.alphabet[(self.alphabet.find(text[i]) + self.alphabet.find(key1[i])) % len(self.alphabet)]

        return ciph

    def decode(self, text):
        A = list(zip(self.key * math.ceil(len(text) / len(self.key)), text))
        key1 = "".join(i[0] for i in A)
        ciph = ''
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                ciph += text[i]
                continue
            ciph += self.alphabet[(self.alphabet.find(text[i]) - self.alphabet.find(key1[i]) + len(self.alphabet)) % len(self.alphabet)]
        return ciph


# abc = "abcdefghijklmnopqrstuvwxyz"
# key = "password"

abc = 'ンワラヤマハナタサカアリミヒニチシキイルユムフヌツスクウレメヘネテセケエヲロヨモホノトソコオ'
key = 'カタカナ'
c = VigenereCipher(key, abc)

# print(c.encode('CODEWARS'))
print(c.encode('カタカナ'))
# print(c.decode('rovwsoiv'))