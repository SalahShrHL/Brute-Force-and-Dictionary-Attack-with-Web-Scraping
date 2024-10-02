from time import time
import time


###############
# ###########     ATTAQUE PAR DICTIONNAIRE  CAS1      ##################################################################################################### 
#Les Testes  


 start = time.process_time()

 def Dictionnaire(mdp):
     myFile = open(r"C:\Users\SALAH PC\Documents\SAAD\Attaques\Dictionnaire.txt","r")
     for line in myFile:
         if line.startswith(mdp):
             print("Votre mot de passe est "+line)
             myFile.close()
             break


 Dictionnaire("111")

 end = time.process_time()
 print(f"Le temps d'execution est: {end-start} secondes")


##########################     ATTAQUE PAR FORCE BRUTE  CAS 2+3    ##################################################################################################### 
def ForceBrute(ensemble,k,mdp):
 
    n = len(ensemble)
    ForceBruteRec(ensemble, "", n, k,mdp)

 
cout=0
def ForceBruteRec(ensemble,guess, n, k,mdp):
    if (k == 0) :
        global cout
        cout =cout+1
        print("le cas numéro "+str(cout))
        print(guess)
        if(guess==mdp):
            print("your code is "+guess)
            end = time.time()
            print(f"Le temps d'execution est: {end - start} secondes")
            exit()
            
        return
 
    for i in range(n):
        newguess = guess + ensemble[i]
        ForceBruteRec(ensemble, newguess, n, k - 1,mdp)



print("\n Test2")

# ensemble2 = ['0', '1', '2', '3','4','5', '6', '7','8','9']
# k = 5
# start = time.process_time()
# ForceBrute(ensemble2, k,"99999")


    






#Test3

symbols = [' ','~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
nembers = ['0', '1', '2', '3','4','5', '6', '7','8','9']
letters=  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w','x','y', 'z']
lm=  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W','X','Y', 'Z']

all= symbols + nembers +letters + lm
 
ensemble3 = all
k=5

start = time.time()
ForceBrute(ensemble3, k,"~~~~Z")




