
words = []
with open("Z:\Programming Stuff\Projects\Python-Exercises\Hangman\worliste.txt", "r", encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    for line in lines:
        words.append(line)

spcial_char_map = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss', ord("Ö"):"Oe", ord("Ä"):"Ae", ord("Ü"):"Ue"}

for i in range(len(words)):
    words[i] = words[i].translate(spcial_char_map)
    
with open("Z:\Programming Stuff\Projects\Python-Exercises\Hangman\worliste2.txt", "w", encoding='utf-8', errors='ignore') as f:
    for word in words:
        f.write(word)