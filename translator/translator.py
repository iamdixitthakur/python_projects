from englisttohindi.englisttohindi import EngtoHindi

print("This is an english to hindi translator")
input_text=input(" enter the text in english :")

trans = EngtoHindi(message=input_text)
text_in_hindi=trans.convert
print(text_in_hindi)

with open('search_history.txt',mode='a') as search_file:

    text=input_text
    search_file.write(text)