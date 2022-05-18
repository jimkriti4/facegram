from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import back
import pygame
import random
import sys
from tkinter import *     
#login _________________________________________________________________________________________________________________
def login():
#login cheek____________________________________________________________________________________________________________
       def id_porfile(user,pas) :
               f=open("data/profiles.txt","r")
               for i in f:
                      i=i.strip()   
                      cre=i.split('==')
                      if cre[0]==user:
                             if cre[1]==pas:      
                                    return True
               f.close() 
               return False 
#close windos__________________________________________________________________________________________________________________
def close(i):
              if i==1:
                  global main
                  main.destroy()
              if i==2:
                  global root
                  root.destroy()
              if i==3:
                  global register  
                  register.destroy()
              if i==4:
                  global new_sub
                  new_sub.destroy()
              if i==5:
                  global forg
                  forg.destroy()
              if i==6:
                  global index
                  index.destroy()
              if i==7:
                  global prof
                  prof.destroy()     
              if i==8:
                  global change_profile
                  change_profile.destroy()    
#login ________________________________________________________________________________________________________ 
def login():
#delete line for old password user
       def dell(i):  
                  l1 = []
                  with open(r"data/profiles.txt", 'r') as fp:
                       l1 = fp.readlines()
                  with open(r"data/profiles.txt", 'w') as fp:
                      for number, line in enumerate(l1):
                             if number not in [i]:     
                                  fp.write(line)  
#frpgot pasword __________________________________________________________________________________________________    
       def forgot():   
               def id_true(user,pas):
                     def save_frogot():
                            global dell
                            fout = open("data/profiles.txt", "a")
                            fout.write(replacement) 
                            fout.close 
                     f=open("data/profiles.txt","r")
                     replacement = ""
                     a=0
                     for i in f:
                             i=i.strip()   
                             cre=i.split('==')
                             if len(cre)<2:
                                 continue
                             if cre[0]==user:      
                                    dell(a)
                                    save_profile(user,pas,mail)
                             a+=1                             
                     f.close()
               def get():
                       global neme_frog
                       global new_pas
                       #username_________________
                       name_get=name_forg.get()
                       neme_frog=name_get
                       #password________________
                       pas_get=new_pas.get()
                       new_pas=pas_get
                       id_true(name_get,new_pas)
               close(3)
               global forg
               global new_pas
               forg= Tk()
               forg.geometry("450x450")
               name_label=ttk.Label(forg,font=('Century 11'),text="Ονομα ")
               new_pas=ttk.Entry(forg,font=('Century 12'))  
               entre=ttk.Button(forg, text="Ολοκληροση", command=lambda:[get(),close(5),login()])
               pas_label=ttk.Label(forg,font=('Century 11'),text="   Νεος"+"\n"+"Κοδικως ")
               back_frog=ttk.Button(forg, text="home", command=lambda:[close(5),home()])
               name_forg=ttk.Entry(forg,font=('Century 12'))     
#style_______________________________________________________________________________________
               pas_label.place(x = 30, y =85 )
               new_pas.place(x = 110, y =100 )     
               entre.place(x = 270, y = 200)
               name_label.place(x = 30, y = 60)
               name_forg.place(x = 110, y = 60)              
               back_frog.place(x = 80, y = 200)
               forg.title("Ξεχασες των κοδικω ")
               forg.mainloop()
#login tsek____________________________________________________________________________________________________________
       def id_porfile(user,pas) :
               f=open("data/profiles.txt","r")
               for i in f:
                      i=i.strip()   
                      cre=i.split('==')
                      if len(cre
                             )<2:
                          continue
                      if cre[0]==user:
                             if cre[1]==pas:      
                                    return True                  
               f.close() 
               return False 
#get valye απο τα input του χρηστι______________________________________________________________________________________________     
       def get_value():
           name_profile=name_entry.get()
           ps_profile=pas_entry.get()
           mail_profile=mail_entry.get()
           save_profile(name_profile,ps_profile,mail_profile)
#save porfiles________________________________________________________________________________________________________
       def save_profile(user,pas,mail):
              if user!="":
                     if pas!="":
                            if mail !="":
                                   f=open("data/profiles.txt","a")
                                   f.write(str(user)+"=="+str(pas)+"=="+str(mail) +"\n")    
                                   f.closed     
              else:
                      return False
#check user name and pasword ______________________________________________________________________________________           
       def check():
              global name_profile
              global ps_profile
              global name_entry
              global pas_entry
              name_profile=name_entry.get()
              ps_profile=pas_entry.get()
              connected=id_porfile(name_profile,ps_profile)
              if connected==True:
                  close(3)
                  facegram(name_profile)
              if connected==False:
                  text_false=ttk.Label(register,font=('Century 11'),text="λαθος ονομα ή κωδικος ξανα δοκημαστε ")
                  Forgot_pas= ttk.Button(register, text="Forgot password", command=lambda:[forgot(),])
                  Forgot_pas.place(x = 280, y = 150)  
                  text_false.place(x = 100, y = 120)     
#new sub  νεα εγγραφη_________________________________________________________________________________________________________               
       def new_sub_():
               global new_sub
               global register
               global name_entry
               global pas_entry
               global mail_entry
               new_sub= Tk()
               new_sub.geometry("450x450")
               #label______________________________________________________________________________
               text_title=ttk.Label(new_sub,font=('Century 18'),text="ΔΗΜΙΟΥΡΓΙΑ ΛΟΓΑΡΙΑΣΜΟΥ")
               text_neme=ttk.Label(new_sub,font=('Century 12'),text="οναμα ")
               text_ps=ttk.Label(new_sub,font=('Century 12'),text="κωδικος ")
               text_mail=ttk.Label(new_sub,font=('Century 12'),text="mail ")
               #inpyt___________________________________________________________________________________
               name_entry= ttk.Entry(new_sub,font=('Century 12'))
               pas_entry= ttk.Entry(new_sub,font=('Century 12'))
               mail_entry= ttk.Entry(new_sub,font=('Century 12')) 
               # bytton_______________________________________________________________________________________
               Enter= ttk.Button(new_sub, text="ολοκληροση", command=lambda:[get_value(),close(4),login(),])
               back=ttk.Button(new_sub, text="αρχικη", command=lambda:[close(4),home()])
         #input style_______________________________________________________________________________________________________
               #text_label_____________________
               text_title.place(x = 20,y = 10) 
               text_neme.place(x = 20,y = 50) 
               text_ps.place(x = 20, y = 90)
               text_mail.place(x = 20, y = 120)
               #entry__________________________
               name_entry.place(x = 90, y = 50)
               pas_entry.place(x = 90, y = 90)
               mail_entry.place(x = 90, y = 120)
               #button style_______________________ 
               Enter.place(x = 190, y = 190)
               back.place(x = 100, y = 190)
               new_sub.title("ΔΗΜΙΟΥΡΓΙΑ ΛΟΓΑΡΙΑΣΜΟΥ")
               new_sub.mainloop()
       def login():             
                global register
                global name_entry
                global pas_entry            
                register= Tk()
                register.geometry("450x450")
                # label_____________________________________________________________________________________
                text_title=ttk.Label(register,font=('Century 20'),text="εισοδος ")
                text_neme=ttk.Label(register,font=('Century 12'),text="οναμα ")
                text_ps=ttk.Label(register,font=('Century 12'),text="κωδικος ")
                # input_____________________________________________________________________________________
                name_entry= ttk.Entry(register,font=('Century 12'))
                pas_entry= ttk.Entry(register,font=('Century 12'))
                # button_____________________________________________________________________________________
                Enter= ttk.Button(register, text="Enter", command= check)
                back= ttk.Button(register, text="home", command=lambda:[close(3),home()])
                new= ttk.Button(register, text="δημηοθργια λογαριασμο", command= lambda:[close(3),new_sub_()])
                # input style_____________________
                text_title.place(x = 150,y = 10) 
                text_neme.place(x = 20,y = 50) 
                text_ps.place(x = 20, y = 90) 
                name_entry.place(x = 90, y = 50)
                pas_entry.place(x = 90, y = 90)
                # button style____________________
                new.place(x = 300, y = 10) 
                Enter.place(x = 190, y = 150)
                back.place(x = 100, y = 150)
                register.title("εισοδος")
                register.mainloop() 
       close(1)     
       login()                                            
#_play music_________________________________________________________________________________________
music=[ ]
def music_play (user):
       def music_list():
              global music
              for i in range(1,19):
                  music.append(i)  
       def play():
              global music
              global key
              if key<=0:
                  key=music[0]
              pygame.mixer.init()
              pygame.mixer.music.load('music/'+str(key)+'.mp3')
              pygame.mixer.music.play()
              viow_song()
       def stop():
              global key
              global music
              pygame.mixer.init()
              pygame.mixer.music.load('music/'+str(key)+'.mp3')
              pygame.mixer.music.stop()  
       def next():
              global key
              global music
              max_song=18
              key=key+1
              if key >max_song:
                  key=music[0]     
              pygame.mixer.init()
              pygame.mixer.music.load('music/'+str(key)+'.mp3')
              pygame.mixer.music.play()
              viow_song()
       def back():
              global key
              global music
              key=key-1
              if key<=0:
                     key=18
              pygame.mixer.init()
              pygame.mixer.music.load('music/'+str(key)+'.mp3')
              pygame.mixer.music.play()
              viow_song()
       def random_():
              global music
              global key
              key= random.randint(1,18)
              pygame.mixer.init()
              pygame.mixer.music.load('music/'+str(key)+'.mp3')
              pygame.mixer.music.play()
              viow_song()
       def viow_song():
           global key
           text_song=ttk.Label(root,font=('Century 15'),text="Tο Tραγουδι Eιναι:"+str(key)+".mp3")
           text_song.place(x=120,y=200)
       def music_():
              global key
              global root
              key=0
              music_list()
              root = Tk()
              text_title=ttk.Label(font=('Century 20'),text="μουσικη ")
             #button
              b_play = Button(text = "play",command=play)
              b_stop = Button(text = "stop",command=stop)
              b_next = Button(text = "next",command=next)
              b_back = Button(text = "back",command=back)
              b_random = Button(text = "random",command=random_)
              b_home = Button(text = "facegram",command=lambda:[close(2),facegram(user)])
              #button style
              b_play.place(x = 200,y = 250) 
              b_stop.place(x = 200,y = 280)
              b_next.place(x = 240, y = 250) 
              b_back.place(x = 160, y = 250)
              b_random.place(x = 280, y = 250)
              b_home.place(x = 120, y = 250)
              text_title.place(x=170,y=10)              
              root.geometry("450x450")
              root.title("μουσσικη")
              root.mainloop()             
       music_()
def facegram(user):
#delete line for old password user____________________________________________________________________________________
       def dell(i):  
                  l1 = []
                  with open(r"data/profiles.txt", 'r') as fp:
                       l1 = fp.readlines()
                  with open(r"data/profiles.txt", 'w') as fp:
                      for number, line in enumerate(l1):
                             if number not in [i]:     
                                  fp.write(line)
#save porfiles________________________________________________________________________________________________________
       def save_profile(user,pas,mail):
               if user!="":
                     if pas!="":
                            if mail !="":
                                   f=open("data/profiles.txt","a")
                                   f.write(str(user)+"=="+str(pas)+"=="+str(mail) +"\n")    
                                   f.closed     
               else:
                      return False                          
       def profile(user):
               def data_change(user):
                      #get input entry___________________
                       def get_change():
                               global name
                               global password
                               global mail
                               name=name_change.get()
                               password=pas_change.get()
                               mail=mail_change.get()
                      #save the new username and password and mail______________         
                       def change_save(user):
                             get_change()
                             global name
                             global password
                             global mail
                             f=open("data/profiles.txt","r")
                             a=0
                             for i in f:
                                    i=i.strip()   
                                    cre=i.split('==')
                                    if cre[0]==user:    
                                           dell(a)
                                           save_profile(name,password,mail)
                                    a+=1                                         
                             f.close()                 
                       global change_profile     
                       change_profile= Tk()
                       change_profile.geometry("450x450")
              #button__________________________________________________________________________
                       save=ttk.Button(change_profile,text="ολοκληροση",command=lambda:[change_save(user),close(8),facegram(user)])
                       back=ttk.Button(change_profile,text="back",command=lambda:[close(8),facegram(user)])
              #text________________________________________________________________
                       name=ttk.Label(change_profile,font=('Century 15'),text="ονομα:")
                       pas=ttk.Label(change_profile,font=('Century 15'),text="κωδικος:")
                       mail=ttk.Label(change_profile,font=('Century 15'),text="mail :")  
              #input______________________________________________________________
                       name_change= ttk.Entry(change_profile,font=('Century 12'))
                       pas_change= ttk.Entry(change_profile,font=('Century 12'))
                       mail_change= ttk.Entry(change_profile,font=('Century 12'))
              #style______________________________________________________________
                       name.place(x=100,y=60)
                       name_change.place(x=170,y=60)
                       pas.place(x=100,y=90)
                       pas_change.place(x=180,y=90)
                       mail.place(x=100,y=120)
                       mail_change.place(x=150,y=120)
                       save.place(x=200,y=200)
                       back.place(x=100,y=200)                            
                       change_profile.mainloop()     
               def data_user(user):
                      f=open("data/profiles.txt","r")
                      for i in f:
                             i=i.strip()   
                             cre=i.split('==')
                             if cre[0]==user:
                                    return cre
                      f.close()
               global prof     
               prof= Tk()
               prof.geometry("450x450")
               data=data_user(user)
               #button_______________________________________________________________________________________________
               button_change=ttk.Button(prof,text="change",command=lambda:[close(7),data_change(data[0])])
               back=ttk.Button(prof,text="back",command=lambda:[close(7),facegram(user)])
               #text___________________________________________________________________________________________________
               prof_label=ttk.Label(prof,font=('Century 15'),text="Τα στοιχια του λογαριασμου σου")
               name=ttk.Label(prof,font=('Century 15'),text="ονομα:")
               name_=ttk.Label(prof,font=('Century 15'),text=data[0])
               pas=ttk.Label(prof,font=('Century 15'),text="κωδικος:")
               pas_=ttk.Label(prof,font=('Century 15'),text=data[1])
               mail=ttk.Label(prof,font=('Century 15'),text="mail:")
               mail_=ttk.Label(prof,font=('Century 15'),text=data[2])
               #style________________________________________________________________________
               prof_label.place(x=100,y=10)
               name.place(x=100,y=60)
               name_.place(x=170,y=60)
               button_change.place(x=200,y=200)
               pas.place(x=100,y=90)
               pas_.place(x=180,y=90)
               mail.place(x=100,y=120)
               mail_.place(x=150,y=120)
               back.place(x=100,y=200)
               prof.mainloop()              
       global index
       index= Tk()
       index.geometry("450x450")
       text_user=ttk.Label(font=('Century 15'),text="Καλως Ηρθες"+"\n"+"|_-_-_|  "+user+"  |_-_-_|")
       index.music_=ttk.Button(index,text="παιξε μουσικη",command=lambda:[close(6),music_play(user)])

       index.profile_=ttk.Button(index,text="ο λογαριασμο σου",command=lambda:[close(6),profile(user)])
#______imag_________________________________________________________________________________________
       canvas = Canvas(index, width = 450, height = 200)            
       img = PhotoImage(file="image/facegram_home.png")      
       canvas.create_image(10,10, anchor=NW, image=img)
#______style____________________________________________________________________________________________
       text_user.place(x=270,y=200)
       index.profile_.place(x = 10, y = 200)
       index.music_.place(x = 10, y = 300)
       canvas.place(x = 0, y = 0)
       index.title("Facegram")
       index.mainloop()      
def home():
       global main
       main= Tk()
       main.geometry("450x450")
       text_title=ttk.Label(font=('Century 20'),text="καλως ηρθες"+"\n"+"στο Facegram")
       main.login_=ttk.Button(main,text="εισοδος  ",command=login)
       main.title("Facegram")
#_______image___________________________________________________________________________________
       canvas = Canvas(main, width = 450, height = 200)            
       img = PhotoImage(file="image/facegram_logo.png")      
       canvas.create_image(10,10, anchor=NW, image=img)
#______stely____________________________________________________________________________________
       text_title.place(x=50,y=300) 
       main.login_.place(x = 290, y = 320)
       canvas.place(x = 0, y = 0)
       main.mainloop()
home()
