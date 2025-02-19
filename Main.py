

try:
    text_file = open("dna_raw.txt", "r")
    print(text_file.read())  # Skriver ut innehållet i filen
    text_file.close()
except FileNotFoundError:
    print("Filen dna_raw.txt hittades inte!")