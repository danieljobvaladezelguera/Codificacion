text = str(input("Coloca tu texto: "))
text_change = list(text)
text_len = len(text)
new_text_len = str(text_len)

first_abc = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m', 'n','ñ' ,'o','p','q','r','s','t', 'u', 'v', 'w','x','y','z', ' ', '1','2','3','4','5','6','7','8','9','0']
numeros = ['0','1','2','3','4','5','6','7','8','9']
acento = ['á','é','í', 'ó','ú']

last_abc = ['s','t', 'u', 'v', 'w','x','y','z', 'a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m', 'n','ñ', 'o','p','q','r', ' ', '1','2','3','4','5','6','7','8','9','0']

final_abc = []


for i in range(text_len):
    for j in range(len(last_abc)):
        text_change_lower = text_change[i].lower()
        if(last_abc[j] == text_change_lower):
            final_abc.append([first_abc[j]])
            
print(*final_abc)

