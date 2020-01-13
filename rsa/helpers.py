jadval = [
    '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '.', '?', ',', '-'
]


class Helpers:
    """
    Helpers is a set of string and int operation which helps us to transform given string as input to an integer number
    and to transform an integer number to a string 
    """
    @classmethod
    def str_to_number(cls, text: str, separate_length: int = 6):
        """
        transform given string to number by first of all splitting given string to smaller strings and then using pre defined charachter table provided
        in project defenition converting each charachter to a double digit int number, concat each part of split together and then join them with a simple dash
        """
        if separate_length % 2 == 1:
            raise ValueError
        text = text.upper()
        text = text.replace(' ', '')
        new_number = str()
        for char in text:
            if char in jadval:
                temp = jadval.index(char)
                if temp < 10:
                    new_number = new_number + "0" + str(temp)
                else:
                    new_number = new_number + str(temp)
            else:
                raise ValueError
        out = list()
        while True:
            if len(new_number) > separate_length:
                out.append(int(new_number[:separate_length]))
                new_number = new_number[separate_length:]
            else:
                if len(new_number) != 0:
                    out.append(int(new_number))
                break
        return out

    @classmethod
    def number_to_str(cls, number):
        """
            splits given input using dash as a delimiter and then split each part to two digit numbers and retrieve correct character from predefined table
            and finally concat all charachters together
        """
        if len(str(number)) % 2 == 1:
            decrypted = "0" + str(number)
        else:
            decrypted = str(number)
        sinp = [decrypted[i:i + 2] for i in range(0, len(decrypted), 2)]
        out = str()
        for i in sinp:
            out = out + jadval[int(i)]

        return out
