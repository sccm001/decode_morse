def decodeMorse(morse_code):
    #increase dectionary of MORSE_CODE '':' '
    MORSE_CODE['']=' '
    #拆分字符串为数组
    string=morse_code.split(' ')
    k=0
    while True:
       
        for k in range(len(string)):
            if string[k]==string[k+1] and string[k]=='':
                del string[k]
            elif k==len(string) and string[k]=='':
                del string[k]
            elif k==len(string):
                break
            else:
                k=0
            
    print(string)
    
    
    english_letter=[]
    while k < len(string):
        # print(string[k])
        # print(MORSE_CODE[string[k]])
        if not(MORSE_CODE[string[k]]==' ' and MORSE_CODE[string[k-1]]==' '):
            english_letter.append(MORSE_CODE[string[k]])
        k=k+1
        print(english_letter)
    english=''.join(english_letter)
    
    
    return english
