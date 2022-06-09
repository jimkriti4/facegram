import os
def windus_instal(x):
    if x=="yes":
        os.system('py -m pip install pygame')
    if x=="no":
        os.system('py -m pip --version')
        os.system('py -m ensurepip --default-pip')
        os.system('py -m pip install --upgrade pip setuptools wheel')
x=input("εχεεις κατεβαση το pip(yes/no)")
windus_instal(x)
 
