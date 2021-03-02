#!/usr/bin/env python
# coding: utf-8

# In[605]:


#Author : SAAL Fatma
import pandas as pd


# In[606]:


#Ouverture du fichier csv et récupération de son contenu dans un tableau
import csv
with open('data_contest_answers.csv',newline='') as f:   
    nbLignes=0
    tableau=[]
    lire=csv.reader(f)                            
    print('',end='\n')
    for ligne in lire:                            
        print(ligne, end='\n')                    
        tableau.append(ligne)  
        nbLignes+=1
    print(nbLignes)
    print(len(tableau))


# In[608]:


#Le nombre total de réponse

#J'ai parcouru les colonne à partir de l'indice 3 à l'indice 8 , je vérifie qu'à chaque fois la réponse n'est pas une chaine vide 
#puis j'incrémente le nombre de réponses qui est initialis& à 0 et j'imprise le nombre total de réponses à la fin
nbReponses=0
for i in range(1,len(tableau)):
    for j in range(3,len(tableau[i])):
        if(len(tableau[i][j])!=0):
            nbReponses+=1
print("Le nombre de réponses est : ",nbReponses)


# In[609]:


#Fonction qui calcule le nombre réponses avec le numéro du groupe en paramètres 
def donneesEnFonctionNumeroDeGroupe(numeroGroupe):
    nbReponses=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])):
            if(tableau[i][1]==numeroGroupe):
                if(len(tableau[i][j])!=0):
                    nbReponses+=1
    return nbReponses


# In[610]:


#Le nombre de réponses libres
nb=0
for i in range(1,len(tableau)):
    if(len(tableau[i][9])!=0):
        nb+=1
print("Le nombre de réponses libres est :" , nb)


# In[611]:


#affichage des réponses libres
for i in range(1,len(tableau)):
    if(len(tableau[i][9])!=0):
        print("Groupe : ",tableau[i][1],"Passage : ",tableau[i][1], tableau[i][9])


# In[612]:


#Affichage du nombre total de réponse par groupe
print({"Groupe 1":donneesEnFonctionNumeroDeGroupe('1'),"Groupe 2":donneesEnFonctionNumeroDeGroupe('2'),"Groupe 3":donneesEnFonctionNumeroDeGroupe('3'),
       "Groupe 4":donneesEnFonctionNumeroDeGroupe('4'),"Groupe 5":donneesEnFonctionNumeroDeGroupe('5'),"Groupe 6":donneesEnFonctionNumeroDeGroupe('6'),
       "Groupe 7":donneesEnFonctionNumeroDeGroupe('7'),"Groupe 8":donneesEnFonctionNumeroDeGroupe('8'),"Groupe 9":donneesEnFonctionNumeroDeGroupe('9')})


# In[613]:


plotdata = pd.DataFrame({
    "Nombre de réponses":[donneesEnFonctionNumeroDeGroupe('1'),donneesEnFonctionNumeroDeGroupe('2'), donneesEnFonctionNumeroDeGroupe('3'), donneesEnFonctionNumeroDeGroupe('4'), donneesEnFonctionNumeroDeGroupe('5'),donneesEnFonctionNumeroDeGroupe('6'),donneesEnFonctionNumeroDeGroupe('7'),donneesEnFonctionNumeroDeGroupe('8'),donneesEnFonctionNumeroDeGroupe('9')],
    }, 
    index=["Groupe 1", "Groupe 2", "Groupe 3", "Groupe 4", "Groupe 5" , "Groupe 6" , "Groupe 7" , "Groupe 8" , "Groupe 9"]
)
plotdata


# In[614]:


#Barplot pour représenter le nombre de réponses de chaque groupe graphiquement
df = pd.DataFrame({'Groupe':['1','2','3','4','5','6','7','8','9'],"Nombre de réponses":[donneesEnFonctionNumeroDeGroupe('1'),donneesEnFonctionNumeroDeGroupe('2'), donneesEnFonctionNumeroDeGroupe('3'), donneesEnFonctionNumeroDeGroupe('4'), donneesEnFonctionNumeroDeGroupe('5'),donneesEnFonctionNumeroDeGroupe('6'),donneesEnFonctionNumeroDeGroupe('7'),donneesEnFonctionNumeroDeGroupe('8'),donneesEnFonctionNumeroDeGroupe('9')]})
ax = df.plot.bar(x="Groupe", y="Nombre de réponses", rot=0 )


# In[615]:


#Fonction qui calcule le nombre réponses avec le numéro du groupe en paramètres 
def donneesEnFonctionDuPassage(numeroPassage):
    nbReponses=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])):
            if(tableau[i][2]==numeroPassage):
                
                if(len(tableau[i][j])!=0):
                    nbReponses+=1
    return nbReponses


# In[616]:


#Affichage du nombre de réponses en fonction du passage ,sachant qu'il y a deux passages
print({"Passage 1":donneesEnFonctionDuPassage('1'),"Passage 2":donneesEnFonctionDuPassage('2')})


# In[617]:


#Barplot pour représenter le nombre de réponses du passage graphiquement
df = pd.DataFrame({'Passage':['1','2'],"Nombre de réponses":[donneesEnFonctionDuPassage('1'),donneesEnFonctionDuPassage('2')]})
ax = df.plot.bar(x="Passage", y="Nombre de réponses", rot=0 )


# In[618]:


plotdata = pd.DataFrame({
    "Nombre de réponses":[donneesEnFonctionDuPassage('1'),donneesEnFonctionDuPassage('2')]
    }, 
    index=["Passage 1", "Passage 2"]
)
plotdata


# In[623]:


import pandas as pd 
my_dict={
'Réponses':[donneesEnFonctionDuPassage('1'),donneesEnFonctionDuPassage('2')]
}
my_labels=['Passage 1','Passage 2']

df = pd.DataFrame(data=my_dict)
df.plot.pie(title="Répartition des réponses en fonction du passsage",y='Réponses',
            fontsize=20,labels=my_labels)


# In[595]:


#caclul de la moyenne de chaque groupe
def moyenne(numeroGroupe):
    nbReponses=donneesEnFonctionNumeroDeGroupe(numeroGroupe)
    somme=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])-1):
            if(tableau[i][1]==numeroGroupe):
                if(len(tableau[i][j])!=0):
                    somme+=int(tableau[i][j])
    return (somme/nbReponses)


# In[477]:


print({"Moyenne groupe 1":moyenne('1'),"Moyenne groupe 2":moyenne('2'),"Moyenne groupe 3":moyenne('3'),
       "Moyenne groupe 4":moyenne('4'),"Moyenne groupe 5":moyenne('5'),"Moyenne groupe 6":moyenne('6'),
       "Moyenne groupe 7":moyenne('7'),"Moyenne groupe 8":moyenne('8'),"Moyenne groupe 9":moyenne('9')})


# In[497]:


#caclul de la moyenne de chaque groupe par passage
def moyenne2(numeroGroupe,numeroPassage):
    assert numeroPassage=='1' or numeroPassage=='2',"Le numero de passage est soir 1 ou 2"
    nbReponses=donneesEnFonctionNumeroDeGroupe(numeroGroupe)
    somme=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])-1):
            if(tableau[i][1]==numeroGroupe and tableau[i][2]==numeroPassage):
                if(len(tableau[i][j])!=0):
                    somme+=int(tableau[i][j])
    return (somme/nbReponses)


# In[499]:


print({"Moyenne groupe 1 passage 1":moyenne2('1','1')},end='\n')
print({"Moyenne groupe 1 passage 2":moyenne2('1','2')},end="\n\n")
print({"Moyenne groupe 2 passage 1":moyenne2('2','1')},end='\n')
print({"Moyenne groupe 2 passage 2":moyenne2('2','2')},end="\n\n")
print({"Moyenne groupe 3 passage 1":moyenne2('3','1')},end='\n')
print({"Moyenne groupe 3 passage 2":moyenne2('3','2')},end="\n\n")
print({"Moyenne groupe 4 passage 1":moyenne2('4','1')},end='\n')
print({"Moyenne groupe 4 passage 2":moyenne2('4','2')},end="\n\n")
print({"Moyenne groupe 5 passage 1":moyenne2('5','1')},end='\n')
print({"Moyenne groupe 5 passage 2":moyenne2('5','2')},end="\n\n")
print({"Moyenne groupe 6 passage 1":moyenne2('6','1')},end='\n')
print({"Moyenne groupe 6 passage 2":moyenne2('6','2')},end="\n\n")
print({"Moyenne groupe 7 passage 1":moyenne2('7','1')},end='\n')
print({"Moyenne groupe 7 passage 2":moyenne2('7','2')},end="\n\n")
print({"Moyenne groupe 8 passage 1":moyenne2('8','1')},end='\n')
print({"Moyenne groupe 8 passage 2":moyenne2('8','2')},end="\n\n")
print({"Moyenne groupe 9 passage 1":moyenne2('9','1')},end='\n')
print({"Moyenne groupe 9 passage 2":moyenne2('9','2')})


# In[500]:


#Classement des présentation par ordre d'appréciation
monDico={"Moyenne groupe 1 passage 1":moyenne2('1','1'),
         "Moyenne groupe 1 passage 2":moyenne2('1','2'),
         "Moyenne groupe 2 passage 1":moyenne2('2','1'),
         "Moyenne groupe 2 passage 2":moyenne2('2','2'),
         "Moyenne groupe 3 passage 1":moyenne2('3','1'),
         "Moyenne groupe 3 passage 2":moyenne2('3','2'),
         "Moyenne groupe 4 passage 1":moyenne2('4','1'),
         "Moyenne groupe 4 passage 2":moyenne2('4','2'),
         "Moyenne groupe 5 passage 1":moyenne2('5','1'),
         "Moyenne groupe 5 passage 2":moyenne2('5','2'),
         "Moyenne groupe 6 passage 1":moyenne2('6','1'),
         "Moyenne groupe 6 passage 2":moyenne2('6','2'),
         "Moyenne groupe 7 passage 1":moyenne2('7','1'),
         "Moyenne groupe 7 passage 2":moyenne2('7','2'),
         "Moyenne groupe 8 passage 1":moyenne2('8','1'),
         "Moyenne groupe 8 passage 2":moyenne2('8','2'),
         "Moyenne groupe 9 passage 1":moyenne2('9','1'),
         "Moyenne groupe 9 passage 2":moyenne2('9','2')}
sorted(monDico.items(), key=lambda t: t[1])


# In[590]:


#Barplot pour représenter la moyenne de chaque groupe graphiquement
df = pd.DataFrame({'Groupe':['1','2','3','4','5','6','7','8','9'], 'Moyenne':[moyenne('1'),moyenne('2'),moyenne('3'),moyenne('4'),moyenne('5'),moyenne('6'),moyenne('7'),moyenne('8'),moyenne('9')]})
ax = df.plot.bar(x="Groupe", y="Moyenne", rot=0 )


# In[494]:


#Dataframe pour représenter la moyenne de chaque groupe
plotdata = pd.DataFrame({
    "Moyenne":[moyenne('1'),moyenne('2'),moyenne('3'),moyenne('4'),moyenne('5'),moyenne('6'),moyenne('7'),moyenne('8'),moyenne('9')],
    
    }, 
    index=["Groupe 1", "Groupe 2", "Groupe 3", "Groupe 4", "Groupe 5" , "Groupe 6" , "Groupe 7" , "Groupe 8" , "Groupe 9"]
)
plotdata


# In[510]:


from matplotlib import pyplot as plt
plotdata = pd.DataFrame({
    "Moyenne passage 1":[moyenne2('1','1'), moyenne2('2','1'), moyenne2('3','1'), moyenne2('4','1'), moyenne2('5','1'),moyenne2('6','1'),moyenne2('7','1'),moyenne2('8','1'),moyenne2('9','1')],
    "Moyenne passage 2":[moyenne2('1','2'), moyenne2('2','2'), moyenne2('3','2'), moyenne2('4','2'), moyenne2('5','2'),moyenne2('6','2'),moyenne2('7','2'),moyenne2('8','2'),moyenne2('9','2')]
    }, 
    index=["Groupe 1", "Groupe 2", "Groupe 3", "Groupe 4", "Groupe 5" , "Groupe 6" , "Groupe 7" , "Groupe 8" , "Groupe 9"]
)
plotdata.plot(kind="bar")
plt.title("Moyenne par groupe/passage")
plt.xlabel("Groupe")
plt.ylabel("Moyenne")


# In[502]:


plotdata = pd.DataFrame({
    "Moyenne passage 1":[moyenne2('1','1'), moyenne2('2','1'), moyenne2('3','1'), moyenne2('4','1'), moyenne2('5','1'),moyenne2('6','1'),moyenne2('7','1'),moyenne2('8','1'),moyenne2('9','1')],
    "Moyenne passage 2":[moyenne2('1','2'), moyenne2('2','2'), moyenne2('3','2'), moyenne2('4','2'), moyenne2('5','2'),moyenne2('6','2'),moyenne2('7','2'),moyenne2('8','2'),moyenne2('9','2')]
    }, 
    index=["Groupe 1", "Groupe 2", "Groupe 3", "Groupe 4", "Groupe 5" , "Groupe 6" , "Groupe 7" , "Groupe 8" , "Groupe 9"]
)
plotdata


# In[656]:


#Detection de fraude 
#Ma réflexion pour le cas de détection de fraude , c'est que pour chaque évaluation si les notes attribues 
#sont tous des 6 ou des 1 , je le considère comme un fraude possible

    
def casDeFraude():
    somme1=0
    somme2=0
    cpt=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])-1): 
            if(tableau[i][j]=='6'):
                somme1+=1
            if(tableau[i][j]=='1'):
                somme2+=1
        if(somme1==6 or somme2==6):
            cpt+=1
           # print("groupe :", tableau[i][1],"Passage : ",tableau[i][2],"Numéro de ligne:",i," fraude possible")
            print(tableau[i],end='\n')
        somme1=0
        somme2=0
        
    return cpt
    


# In[657]:


casDeFraude()


# In[665]:


def TauxDeFraude():
    somme1=0
    somme2=0
    cpt=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])-1): 
            if(tableau[i][j]=='6'):
                somme1+=1
            if(tableau[i][j]=='1'):
                somme2+=1
        if(somme1==6 or somme2==6):
            cpt+=1
        somme1=0
        somme2=0
    return cpt
    


# In[668]:


def NonFraude():
    somme1=0
    somme2=0
    cpt=0
    for i in range(1,len(tableau)):
        for j in range(3,len(tableau[i])-1): 
            if(tableau[i][j]=='6'):
                somme1+=1
            if(tableau[i][j]=='1'):
                somme2+=1
        if(somme1!=6 or somme2!=6):
            cpt+=1
        somme1=0
        somme2=0
    return cpt
    


# In[670]:


#Barplot pour représenter le taux de fraude 
df = pd.DataFrame({'Taux de fraude':['Cas de fraude','Cas de non fraude'],"Taux":[TauxDeFraude(),NonFraude()]})
ax = df.plot.bar(x="Taux de fraude", y="Taux", rot=0 )


# In[671]:


import pandas as pd 
my_dict={
'Résultat':[TauxDeFraude(),NonFraude()]
}
infos=['Fraude','Pas de fraude']

df = pd.DataFrame(data=my_dict)
df.plot.pie(title="Représentation du taux de fraude",y='Résultat',
            fontsize=15,labels=infos)

