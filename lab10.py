# Programmers: Tim Hunt, Emily Catanzariti, Angel Scott
# Course: CS151, Dr. Rajeev
# Date: 12/2/2021
# Lab Number: 10
# Program Inputs: Name of file containing Morse Code
# Program Outputs: Decoded file contents

ENGLISH = 0
MORSE = 1
def load_morse_dictionary():
    try:
        morse_code_file = open("morsecode.txt", "r")
        morse_codes = []
        for line in morse_code_file:
            code = line.split("\t").split("\n")
            #code[ENGLISH] = str(code[ENGLISH])
            #code[MORSE] = str(code[MORSE])
            morse_codes.append(code)
        morse_code_file.close()
    except FileNotFoundError:
        print("Error. File not found.")
    return morse_codes

print(load_morse_dictionary())
