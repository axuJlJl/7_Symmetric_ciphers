GLOBAL_STR = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцшщъыьэюя0123456789 .,;...?:!()-|\"«»'"

class CesarClass:
    def __init__(self, key, string):

        out = ""
        for char in string:
            out += self.encrypter(char, key)
        self.encrypted = out

        s = ""
        for char in out:
            s += self.decrypter(char, key)
        self.decrypted = s

    def encrypter(self, char, k):
        """
        Метод для шифрования данных по шифру Цезаря
        """
        s = GLOBAL_STR
        index = s.find(char)

        # Если длина ключа больше самой строки
        if k > len(s):
            k = k - len(s)

        if index + k >= len(s):
            return s[index + k - len(s)]
        else:
            return s[index + k]

    def decrypter(self, char, k):
        """
        Метод для расшифровки данных по шифру Цезаря
        """
        s = GLOBAL_STR
        index = s.find(char)

        if k > len(s):
            k = k - len(s)

        if index - k >= len(s):
            return s[index - k + len(s)]
        else:
            return s[index - k]


def main():
    try:
        k = int(input("Введите сдвиг=  "))
        s = str(input("Введите строку=  "))
    except:
        print("Что-то пошло не так при вводе данных")
        return

    obj = CesarClass(k, s)
    print("Зашифрованный ключ: " + obj.encrypted)
    print("Расшифрованный ключ: " + obj.decrypted)

if __name__ == "__main__":
    main()
