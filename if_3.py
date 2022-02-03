pocket = ['paper', 'cellphone']
card = False

### 주머니에 돈이 있다면 
if 'money' in pocket : 
    print("택시를 타고 가라")

### 주머니에 돈이 없고 카드가 있다면
elif card :   
    print("택시를 타고 가라")

### 주머니에 돈도 없고 카드도 없다면 
else :   
    print("걸어 가라")
