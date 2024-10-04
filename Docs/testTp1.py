def _sommeImpair(n,res):
    if n==1:
        return res
    else: 
        return _sommeImpair(n-2, res+n)
        
def _sommePair(n,res):
    if n==1:
        return res
    else:
        return _sommePair(n-2,res+n)

def sommes2(n):
    if n %2==0:
        return _sommePair(n-1,0)
    else:
        return _sommeImpair(n, 0)
    


def sommes(n):
    n= n-1 if n %2==0 else n
    return range(1,n+1,2)

'''def sommes(n):
    if n % 2 == 0:
        return sum(range(1, n, 2))  # For even n, stop at n-1
    else:
        return sum(range(1, n+1, 2))  # For odd n, include n'''


#print(sommes(5)) 


def repeat(ch, effective):
    return ch*effective

#Write a function that returns the index of the max element in a list and if it's a duplicqte it returns a list of the indexes
def predict_class(z):
    res=[]
    max_value = max(z)
    for i in range(len(z)):
        if z[i] == max_value:
            res.append(i)
    return res



def merge(t1, t2):
    res = []
    for i in range(len(t1)):
        res.append(t2[i])
        res.append(t1[i])
    return res

def pair(a):
    return [x for x in a if x % 2 == 0]

def fibonacci(n):
    a, b = 0, 1
    res = []
    for i in range(n):
        # Append the current value of 'a' to the result list
        res.append(a)
        # Update 'a' and 'b' by swapping their values
        a, b = b, a+b
    return res

#print(fibonacci(5))


'''Écrire un programme en Python occurrence(s) qui prendre une chaine de caractère s, et de lui renvoyer un dictionnaire dont les clés sont les caractères de la chaine saisie et les valeurs sont les nombres d’occurrences des caractères dans la chaine. Exemple pour la chaine s = "langage" , le programme renvoie le dictionnaire:

{'l':1, 'a':2, 'n':1, 'g':2, 'e':1}'''
def occurrence(s):
    d = {}
    for letter in s:
        res=s.count(letter)
        d[letter]= res
    return d


'''def occurrence(s):
    a={}
    for letter in s:
        res=s.count(letter)
        a[0]= letter
        a[1]= res
    return a'''
print(occurrence("hello"))