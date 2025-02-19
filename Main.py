
dna_sequences = {} #Ett dictionary för att lagra DNA-sekvenserna (sekvens-ID som nyckel och sekvens som värde).


with open("dna_raw.txt", "r") as text_file: # Öppnar filen i läsläge ("r").
    current_sequence_id = None #Variabel som håller koll på sekvens-ID.
    current_sequence = "" #Variabel som lagrar den aktuella sekvensens innehåll.

    for line in text_file: #Läser textfilen, rad för rad. 
        line = line.strip() #Tar bort eventuella mellanslag eller nya rader.

        if line.startswith(">"): #Om raden börjar med ">", är det en sekvens-ID-rad. 
            if current_sequence_id: #Om det redan finns en pågående sekvens:
                dna_sequences[current_sequence_id] = current_sequence #Spara raden i dictionaryn (ID = key, sekvens = value).
            
            current_sequence_id = line[1:] #Ta bort ">"-tecknet för att få sekvens-ID.
            current_sequence = "" #Nollställer den aktuella sekvensen (för att börja på ny sekvens).
        else:
            current_sequence += line.lower() #Lägger till raden till den aktuella sekvensen, konverterar texten till gemener.
    
    if current_sequence_id: #Sparar sista sekvensen efter att loopen är klar
        dna_sequences[current_sequence_id] = current_sequence

# Skriver ut dictionaryn i form av "sekvens-ID: sekvens"
for seq_id, sequence in dna_sequences.items():
    print(f"{seq_id}: {sequence}")




#     for unique_char in text_file:
#         if unique_char.isalpha():
#             lower_char = unique_char.lower()
#             if lower_char not in text_file:
#                 dna_sequences[lower_char] = 1
#             else:
#                 dna_sequences[lower_char] += 1

# for char, count in dna_sequences.items():
#     print(f"{count}, {char}")













