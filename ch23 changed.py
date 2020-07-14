# extra challenge
import sys
script, decoding, errors = sys.argv


def main(file, input_decoding, errors):
    variable = file.readline()
    newline = variable.strip(" b' \n ")
    newline = newline.encode('raw_unicode_escape')
    if variable:
        print_line(newline, input_decoding, errors)
        return main(file, input_decoding, errors)


def print_line(newline, input_decoding, errors):
    # decoding process
    abc = newline.decode(input_decoding, errors=errors)
    bytes_file = abc.encode(input_decoding, errors=errors)
    print(bytes_file, "<===>", abc)


scriptread = open("languages in utf-8 encoded.txt", 'rt', encoding='unicode_escape')
main(scriptread, decoding, errors)
