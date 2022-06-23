import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def greeting(name):
  print("Hello, " + name)


def hello(name='jackie'):
    print('Salut'+name)
    

    




def pie_types_variable(d,name=''):
    """
    Renvoie en sortie un pie plot des distributions des types de variable dans le DataFrame donné en entrée.
    """
    (d.dtypes.value_counts()).plot.pie(autopct='%1.1f%%',startangle=0)
    plt.title('Pieplot des types de variables dans la bdd',name)
    plt.ylabel('')
    plt.show()
    
def desc_df(df,name=''):
    """
    Renvoie en sortie une description du df en entrée
    """
    val_manq=df.notna().mean().mean()
    dupli=df.duplicated().sum()
    nbligne=len(df.index)
    nbcolonne=len(df.columns)
    print("Dans la base de données",name ,"on a {} lignes avec {} variables. Elle est remplie à {} % et il y a {} lignes dupliquées".format(nbligne,nbcolonne,str(val_manq*100)[:5],dupli))
    
def pie_remplissage(d,name=''):
    """
    Renvoie en sortie un pie plot du pourcentage de remplissage du df
    """
    notna=d.notna().mean().mean()*100
    na=100-notna
    labels = 'valeurs manquantes','valeurs présentes'
    sizes = [na, notna]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    plt.figure(facecolor=None)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Pie Plot Valeurs présentes/manquantes '+name)
    plt.show()
    
def piebar_categorie(ser,angle=180,rot_bar=90,rot_lab=False,name=''):
    """
    Renvoie en sortie un pie plot et un barplot de la variable qualitative de catégorie en entrée
    """
    labels = ser.value_counts().index.values
    sizes = ser.value_counts().values


    fig, (ax1, ax2) = plt.subplots(1, 2)
    plt.figure(facecolor=None)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=angle,labeldistance=1.2,rotatelabels=rot_lab)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   

    #ax1.legend(loc='lower left')
    x_pos=np.arange(len(labels))
    ax2.bar(labels,sizes)
    fig.suptitle('Affichage catégorie: pie et bar plot'+name,fontsize=15)
    ax2.set_xlabel('categories')
    ax2.grid()
    ax2.set_xticklabels(labels=labels,rotation=rot_bar)

    plt.show()

def comparaison_columns(d1,d2):
    dif1_2=list(set(d1.columns)-set(d2.columns)) 
    dif2_1=list(set(d2.columns)-set(d1.columns))
    commun=list(set(d1.columns)-set(dif1_2))
    exte=dif1_2+dif2_1
    return dif1_2,dif2_1,commun,exte



