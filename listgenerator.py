def countdown():
    word=""
    for ch in "spam":
        word+=ch
        yield word
        
        
print(list(countdown()))