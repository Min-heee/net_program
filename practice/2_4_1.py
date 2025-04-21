word = input("Your word: ")  

a_index = word.find('a')  

if a_index != -1:  
    
    print(word[:a_index+1])
    
    
    print(word[a_index+1:])
else:
    print("입력한 단어에 'a'가 포함되어 있지 않습니다.")