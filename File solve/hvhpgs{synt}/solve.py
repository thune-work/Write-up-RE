def generate():
    list_2495 = [2]
    i = 1
    v3 = 3
    while i <= 1337:
        a = 1
        for j in range (i):
            if not (v3 % list_2495[j]):
                a = 0
        if a:
            list_2495.append(v3)
            i = i + 1
        v3 = v3 + 2
    return list_2495

def rot(a1, a2):
    for i in range(len(a1)):
        v3 = a1[i]
        if v3 != 95:
            v3 = (v3 - 97 + a2) % 26 + 97
        a1[i] = v3
        
def shift(a3, a4):
    for i in range(len(a3)):
        v11 = (i + a4) % len(a3)
        a3[i] = a3[v11]


res = generate()
v18 = "azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o"

for i in range(1337):
    a = ""
    for j in range(len(v18)):
        v11 = ((j - res[1336 - i]) % len(v18) + len(v18)) % len(v18)
        a += v18[v11]
    v18 = a    
    
    a = ""
    for j in range(len(v18)):
        if ord(v18[j]) != 95:
            v3 = (((ord(v18[j]) - 97 - res[1336 - i]) % 26) + 26) % 26 + 97 
            a += chr(v3)
        else:
            a += v18[j]
    v18 = a          
        

print(v18)

