import matplotlib.pyplot as plt

dna_sequences = {} #Ett dictionary för att lagra DNA-sekvenserna (sekvens-ID som nyckel och sekvens som värde).


with open("dna_raw.txt", "r") as text_file: # Öppnar filen i läsläge ("r").
    current_sequence_id = None #Variabel som håller koll på sekvens-ID.
    current_sequence = "" #Variabel som lagrar den aktuella sekvensens innehåll.

    for line in text_file: #Läser textfilen, rad för rad. 
        line = line.strip() #Tar bort eventuella mellanslag eller nya rader.

        if line.startswith(">"): #Om raden börjar med ">", är det en sekvens-ID-rad. 
            if current_sequence_id: #Om det redan finns en pågående sekvens:
                dna_sequences[current_sequence_id] = current_sequence #Sparar raden i dictionaryn (ID = key, sekvens = value).
            
            current_sequence_id = line[1:] #Ta bort ">"-tecknet för att få sekvens-ID.
            current_sequence = "" #Nollställer den aktuella sekvensen (för att börja på ny sekvens).
        else:
            current_sequence += line.lower() #Lägger till raden till den aktuella sekvensen, konverterar texten till gemener.
    
    if current_sequence_id: #Sparar sista sekvensen efter att loopen är klar.
        dna_sequences[current_sequence_id] = current_sequence
    

for seq_id, sequence in dna_sequences.items():  # Loopar igenom dictionaryn.
    sequence_length = len(sequence)  # Beräknar antal tecken i sekvensen.
    unique_letters = set(sequence)  # Skapar ett set med unika bokstäver, som används för att identifiera de unika tecknen i varje sekvens. 
    
    print(f"{seq_id}: (Längd: {sequence_length}) Unika bokstäver: {', '.join(sorted(unique_letters))}")


    letter_count = {"a": 0, "c": 0, "g": 0, "t": 0} #Skapar en dictionary för att beräkna antal av respektive bokstav i DNA-sekvenserna

    for letter in sequence:
        if letter in letter_count:
            letter_count[letter] += 1


    print(f"{seq_id}: (Längd: {sequence_length})")
    print(f"A: {letter_count['a']}, C: {letter_count['c']}, G: {letter_count['g']}, T: {letter_count['t']}\n")



plt.bar(letter_count.keys(), letter_count.values)
plt.xlabel("DNA-sekvens - bokstäver")
plt.ylabel("Förekomster")
plt.title(f"Bostäver och antal i {seq_id}")
plt.show()













