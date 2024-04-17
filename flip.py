def flipString(str):
    strLen = len(str)
    flip = ""
    for i in range(strLen - 1, -1, -1):
        flip += str[i]
    return flip

msg = input("Digite uma string para ser invertida: ")
print("String invertida: ", flipString(msg))