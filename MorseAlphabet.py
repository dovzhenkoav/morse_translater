from flask import flash


class Interpreter:

    def inter(self, text):
        lower_text = text.lower()
        a = lower_text.replace("\r\n", " ")
        morse_text = [" "]
        for i in a:

            if i == " " and morse_text[-1] == " ":
                pass
            elif i == " " and morse_text[-1] == " ":
                pass
            else:
                morse_text.append(i)

        try:
            if morse_text[-1] == " ":
                del morse_text[-1]
        except:
            pass
        try:
            if morse_text[0] == " ":
                del morse_text[0]
        except:
            pass

        final_text = ""
        for i in morse_text:
            final_text += i
        return self.decide(final_text)


    def decide(self, text):
        if text == "":
            return text
        elif text[0] != "." and text[0] != "-":
            Translater = ToMorse()
            return Translater.translate(text)
        else:
            Translater = FromMorse()
            return Translater.translate(text)



class ToMorse:

    def __init__(self):
        self.alphabet = {
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
    " ": "/ ",
    ",": "--..-- ",
    ".": ".-.-.- ",
    "!": "",
    "?": "",
    "-": "-....- ",
    "/": "-..-. ",
    " / ": " / "
}

    def translate(self,text):
        error_keys = ""
        morse_text = ''

        for i in text:
            try:
                morse_text += self.alphabet[i]
            except KeyError as err:

                error_keys += str(err)
                morse_text += ''

        error_keys_to_output = error_keys.replace("''", ',')
        if len(error_keys) > 100:
            flash("Can't read too many symbols. We removed them. Check your input")
        elif len(error_keys) < 1:
            pass
        else:
            flash(f"Can't read the next symbols: {error_keys_to_output}. We removed them")


        return morse_text







class FromMorse:

    def __init__(self):
        self.alphabet = {
    ".- ": "a",
    "-... ": "b",
    "-.-. ": "c",
    "-.. ": "d",
    ". ": "e",
    "..-. ": "f",
    "--. ": "g",
    ".... ": "h",
    ".. ": "i",
    ".--- ": "j",
    "-.- ": "k",
    ".-.. ": "l",
    "-- ": "m",
    "-. ": "n",
    "--- ": "o",
    ".--. ": "p",
    "--.- ": "q",
    ".-. ": "r",
    "... ": "s",
    "- ": "t",
    "..- ": "u",
    "...- ": "v",
    ".-- ": "w",
    "-..- ": "x",
    "-.-- ": "y",
    "--.. ": "z",
    ".---- ": "1",
    "..--- ": "2",
    "...-- ": "3",
    "....- ": "4",
    "..... ": "5",
    "-.... ": "6",
    "--... ": "7",
    "---.. ": "8",
    "----. ": "9",
    "----- ": "0",
    "/ ": " ",
    "--..-- ": ",",
    ".-.-.- ": ".",
    "-.-.-- ": "!",
    "..--.. ": "?",
    "-....- ": "-",
    "-..-. ": "/",
    " / ": " "
}
    def translate(self,text):
        error_keys = []
        morse_text = ''
        row = ""
        for i in text:
            if i != " ":
                row += i
            elif i == " ":
                row += i
                try:
                    morse_text += self.alphabet[row]
                except KeyError as err:
                    error_keys.append(str(err))
                row = ""
        row += " "
        try:
            morse_text += self.alphabet[row]
        except KeyError as err:
            error_keys.append(str(err))



        error_keys_to_output = error_keys
        if len(error_keys) > 100:
            flash("Can't read too many symbols. We removed them. Check your input")
        elif len(error_keys) < 1:
            pass
        else:
            flash(f"Can't read the next symbols: {error_keys_to_output}. We removed them")


        return morse_text




















