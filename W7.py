def symbol1(row):
    s=[
    '**0000*',
    '*0***00',
    '*0***00',
    '*0**0*0',
    '*0*00*0',
    '*0*0**0',
    '*00***0',
    '*00***0',
    '*00000*',
    ]
    return s[row]
 
def symbol2(row):
    s=[
    '*00000*',
    '*0****0',
    '******0',
    '******0',
    '**00000',
    '*0*****',
    '*0*****',
    '*0*****',
    '*000000',
    ]
    return s[row]
 
def symbol3(row):
    s=[
    '*00000*',
    '******0',
    '******0',
    '******0',
    '*00000*',
    '******0',
    '******0',
    '******0',
    '*00000*',
    ]
    return s[row]
 
def symbol4(row):
    s=[
    '*****0*',
    '****00*',
    '***0*0*',
    '**0**0*',
    '*0***0*',
    '*000000',
    '*****0*',
    '*****0*',
    '*****0*',
    ]
    return s[row]
 
def symbol5(row):
    s=[
    '*00000*',
    '*0*****',
    '*0*****',
    '*0*****',
    '*00000*',
    '******0',
    '******0',
    '******0',
    '*00000*',
    ]
    return s[row]
 
def symbol6(row):
    s=[
    '******0',
    '******0',
    '******0',
    '******0',
    '******0',
    '******0',
    '*0****0',
    '*0****0',
    '**0000*',
    ]
    return s[row]
 
def symbol7(row):
    s=[
    '*000000',
    '*0*****',
    '*0*****',
    '*0*****',
    '*00000*',
    '*0*****',
    '*0*****',
    '*0*****',
    '*000000',
    ]
    return s[row]
 
def symbol8(row):
    s=[
    '**0000*',
    '*0****0',
    '*0*****',
    '*0*****',
    '**0000*',
    '******0',
    '******0',
    '*0****0',
    '**0000*',
    ]
    return s[row]
 
def symbol9(row):
    s=[
    '*000000',
    '***0***',
    '***0***',
    '***0***',
    '***0***',
    '***0***',
    '***0***',
    '***0***',
    '*000000',
    ]
    return s[row]

def symbol10(row):
    s = [
    '**0000*',
    '*0****0',
    '*0*****',
    '*0*****',
    '*0*****',
    '*0*****',
    '*0*****',
    '*0****0',
    '**0000*',
    ]
    return s[row]
 
 
def symbol11(row):
    s = [
    '*0****0',
    '*0****0',
    '*0****0',
    '*0****0',
    '*000000',
    '*0****0',
    '*0****0',
    '*0****0',
    '*0****0',
    ]
    return s[row]
 
 
def symbol12(row):
    s = [
    '*0****0',
    '*00***0',
    '*000**0',
    '*0*0**0',
    '*0*00*0',
    '*0**0*0',
    '*0**000',
    '*0***00',
    '*0****0',
    ]
    return s[row]

def symbol13(row):
    s = [
    '*000000',
    '******0',
    '*****00',
    '****00*',
    '***00**',
    '**00***',
    '*00****',
    '*0*****',
    '*000000',
    ]
    return s[row]

symbolDict={"0":symbol1, "2":symbol2, "3":symbol3, "4":symbol4,
"5":symbol5, "J":symbol6, "E":symbol7, "S":symbol8, "I":symbol9,
"C":symbol10, "H":symbol11, "N":symbol12 ,"Z":symbol13}
 
row=9
 
while True:
    inp=input("enter a string to display or 'exit' to end program:")
    if inp=='exit':
        break
    for r in range(row):
        for c in inp:
            print(symbolDict[c](r),end=' ')
        print()
print('game over')