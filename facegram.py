from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import back
import pygame
import random
import sys
from tkinter import *
from time import strftime
#login _______________________________________________________________________
def login():
#login cheek___________________________________________________________________
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
#close windos____________________________________________
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
              if i==9:
                     global post
                     post.destroy()
#login __________________________________________________________________________ 
def login():
#delete line for old password user______________________________________________
       global dell
       def dell(i):  
                  l1 = []
                  with open(r"data/profiles.txt", 'r') as fp:
                       l1 = fp.readlines()
                  with open(r"data/profiles.txt", 'w') as fp:
                      for number, line in enumerate(l1):
                             if number not in [i]:     
                                  fp.write(line)  
#frpgot pasword __________________________________________________________    
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
                       global mail_
                       #username_______________
                       name_get=name_forg.get()
                       neme_frog=name_get
                       #password____________
                       pas_get=new_pas.get()
                       new_pas=pas_get
                       #mali________________________
                       mail_get=mail_.get()
                       mail=mail_get
                       id_true(name_get,new_pas,mail)
               close(3)
               global forg
               global new_pas
               global mail_
               forg= Tk()
               forg.geometry("450x450")
               name_label=ttk.Label(forg,font=('Century 11'),text="Ονομα ")
               new_pas=ttk.Entry(forg,font=('Century 12'))  
               entre=ttk.Button(forg, text="Ολοκληροση", command=lambda:[get(),close(5),login()])
               pas_label=ttk.Label(forg,font=('Century 11'),text="   Νεος"+"\n"+"Κοδικως ",background="#404040",foreground="cyan")
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
               frog.configure(bg='#404040')
               forg.mainloop()
#login tsek______________________________________________________________________________________
       def id_porfile(user,pas) :
               f=open("data/profiles.txt","r")
               for i in f:
                      i=i.strip()   
                      cre=i.split('==')
                      if len(cre)<2:
                          continue
                      if cre[0]==user:
                             if cre[1]==pas:      
                                    return True                  
               f.close() 
               return False 
#get valye απο τα input του χρηστι______________________________________________________________     
       def get_value():
           name_profile=name_entry.get()
           ps_profile=pas_entry.get()
           mail_profile=mail_entry.get()
           null_t_f=save_profile(name_profile,ps_profile,mail_profile)
           if null_t_f ==  False:
                  text_erro=ttk.Label(new_sub,font=('Century 12'),text="συμπληροστε ολα τα στοιχια σας",background="#404040",foreground="cyan")
                  text_erro.place(x = 50,y = 160)
           else :
                  close(4)
                  login()
#save porfiles_________________________________________________________________________________
       global save_profile
       def save_profile(user,pas,mail):
              if user!="":
                     if pas!="":
                            if mail !="":
                                   f=open("data/profiles.txt","a")
                                   f.write(str(user)+"=="+str(pas)+"=="+str(mail) +"\n")    
                                   f.closed
                                   return True
              else:
                      return False
#check user name and pasword __________________________________________________________________           
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
                  text_false=ttk.Label(register,font=('Century 11'),text="λαθος ονομα ή κωδικος ξανα δοκημαστε ",background="#404040",foreground="cyan")
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
               #label_________________________________________________________________________
               text_title=ttk.Label(new_sub,font=('Century 18'),text="ΔΗΜΙΟΥΡΓΙΑ ΛΟΓΑΡΙΑΣΜΟΥ",background="#404040",foreground="cyan")
               text_neme=ttk.Label(new_sub,font=('Century 12'),text="οναμα ",background="#404040",foreground="cyan")
               text_ps=ttk.Label(new_sub,font=('Century 12'),text="κωδικος ",background="#404040",foreground="cyan")
               text_mail=ttk.Label(new_sub,font=('Century 12'),text="mail ",background="#404040",foreground="cyan")
               #inpyt____________________________________________
               name_entry= ttk.Entry(new_sub,font=('Century 12'))
               pas_entry= ttk.Entry(new_sub,font=('Century 12'))
               mail_entry= ttk.Entry(new_sub,font=('Century 12')) 
               # bytton____________________________________________________________________
               Enter= ttk.Button(new_sub, text="ολοκληροση", command=lambda:[get_value(),])
               back=ttk.Button(new_sub, text="αρχικη", command=lambda:[close(4),home()])
         #input style__________________________________
               #text_label_____________________
               text_title.place(x = 20,y = 10) 
               text_neme.place(x = 20,y = 50) 
               text_ps.place(x = 20, y = 90)
               text_mail.place(x = 20, y = 120)
               #entry__________________________
               name_entry.place(x = 90, y = 50)
               pas_entry.place(x = 90, y = 90)
               mail_entry.place(x = 90, y = 120)
               #button style_________________________
               Enter.place(x = 190, y = 190)
               back.place(x = 100, y = 190)
               new_sub.title("ΔΗΜΙΟΥΡΓΙΑ ΛΟΓΑΡΙΑΣΜΟΥ")
               new_sub.configure(bg='#404040')
               new_sub.mainloop()
       def login():             
                global register
                global name_entry
                global pas_entry            
                register= Tk()
                register.geometry("450x450")
                # label___________________________________________________________
                text_title=ttk.Label(register,font=('Century 20'),text="εισοδος ",background="#404040",foreground="cyan")
                text_neme=ttk.Label(register,font=('Century 12'),text="οναμα ",background="#404040",foreground="cyan")
                text_ps=ttk.Label(register,font=('Century 12'),text="κωδικος ",background="#404040",foreground="cyan")
                # input____________________________________________
                name_entry= ttk.Entry(register,font=('Century 12'))
                pas_entry= ttk.Entry(register,font=('Century 12'))
                # button_____________________________________________________________________________________
                Enter= ttk.Button(register, text="Enter", command= check)
                back= ttk.Button(register, text="home", command=lambda:[close(3),home()])
                new= ttk.Button(register, text="δημηοθργια λογαριασμο", command= lambda:[close(3),new_sub_()])
                # input style____________________
                text_title.place(x = 150,y = 10) 
                text_neme.place(x = 20,y = 50) 
                text_ps.place(x = 20, y = 90) 
                name_entry.place(x = 90, y = 50)
                pas_entry.place(x = 90, y = 90)
                # button style_______________
                new.place(x = 300, y = 10) 
                Enter.place(x = 190, y = 150)
                back.place(x = 100, y = 150)
                register.title("εισοδος")
                register.configure(bg='#404040')
                register.mainloop()     
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
           #text____________________________________________
           text_song=ttk.Label(root,font=('Century 15'),text="Tο Tραγουδι Eιναι:"+str(key)+".mp3",background="#404040",foreground="cyan")
           text_song.place(x=120,y=200)
       def music_():
              global key
              global root
              key=0
              music_list()
              root = Tk()
              #text__________________________________________________________________________________
              text_title=ttk.Label(font=('Century 20'),text="μουσικη ",background="#404040",foreground="cyan")
             #button_____________________________________
              b_play = Button(text = "play",command=play)
              b_stop = Button(text = "stop",command=stop)
              b_next = Button(text = "next",command=next)
              b_back = Button(text = "back",command=back)
              b_random = Button(text = "random",command=random_)
              b_home = Button(text = "facegram",command=lambda:[close(2),facegram(user)])
              #button style___________________
              b_play.place(x = 200,y = 250) 
              b_stop.place(x = 200,y = 280)
              b_next.place(x = 240, y = 250) 
              b_back.place(x = 160, y = 250)
              b_random.place(x = 280, y = 250)
              b_home.place(x =280, y = 280)
              text_title.place(x=170,y=10)              
              root.geometry("450x450")
              root.title("μουσσικη")
              root.configure(bg='#404040')
              root.mainloop()             
       music_()    
def facegram(user):
       #clock______________________________________________________________________
       def clock():
              def time():
                  string=strftime("%H:%M:%S  %p")
                  label_clock.config(text=string)
                  label_clock.after(1000,time)
              label_clock= ttk.Label(index, font=("DS-DIGI.TTF",20),background="#404040",foreground="cyan")
              label_clock.place(x=100,y=330) 
              time()
       def profile(user):
               def data_change(user):
                      #get input entry__________________
                       def get_change(user):
                               global name
                               global password
                               global mail
                               name=name_change.get()
                               password=pas_change.get()
                               mail=mail_change.get()
                               change_save(user)
                      #get_change____________________________        
                      #save the new username and password and mail______________         
                       def change_save(user):
                             global name
                             global password
                             global mail
                             global save_profile
                             global dell
                             f=open("data/profiles.txt","r")
                             a=0
                             for i in f:
                                    i=i.strip()   
                                    cre=i.split('==')
                                    if cre[0]==user:    
                                           null_t_f=save_profile(name,password,mail)
                                           if null_t_f==True:
                                                  dell(a)
                                                  close(8)
                                    a+=1                                         
                             f.close()
                       #change_save__________________________    
                       global change_profile     
                       change_profile= Tk()
                       change_profile.geometry("450x450")
                       #button____________________________________________________________________________________
                       save=ttk.Button(change_profile,text="ολοκληροση",command=lambda:[get_change(user),login()])
                       back=ttk.Button(change_profile,text="back",command=lambda:[close(8),facegram(user)])
                       #text___________________________________________________________
                       name=ttk.Label(change_profile,font=('Century 15'),text="ονομα:",background="#404040",foreground="cyan")
                       pas=ttk.Label(change_profile,font=('Century 15'),text="κωδικος:",background="#404040",foreground="cyan")
                       mail=ttk.Label(change_profile,font=('Century 15'),text="mail :",background="#404040",foreground="cyan")  
                       #input____________________________________________________
                       name_change= ttk.Entry(change_profile,font=('Century 12'))
                       pas_change= ttk.Entry(change_profile,font=('Century 12'))
                       mail_change= ttk.Entry(change_profile,font=('Century 12'))
                       #style_________________________
                       name.place(x=100,y=60)
                       name_change.place(x=170,y=60)
                       pas.place(x=100,y=90)
                       pas_change.place(x=180,y=90)
                       mail.place(x=100,y=120)
                       mail_change.place(x=150,y=120)
                       save.place(x=200,y=200)
                       back.place(x=100,y=200)
                       change_profile.configure(bg='#404040')
                       change_profile.mainloop()
                       #data_change________________
               def data_user(user):
                      f=open("data/profiles.txt","r")
                      for i in f:
                             i=i.strip()   
                             cre=i.split('==')
                             if cre[0]==user:
                                    return cre
                      f.close()
               global prof               
               data=data_user(user)
               prof= Tk()
               prof.geometry("450x450")
               #button____________________________________________________________________________________
               button_change=ttk.Button(prof,text="change",command=lambda:[close(7),data_change(data[0])])
               back=ttk.Button(prof,text="back",command=lambda:[close(7),facegram(user)])
               #text______________________________________________________________________________________
               prof_label=ttk.Label(prof,font=('Century 15'),text="Τα στοιχια του λογαριασμου σου",background="#404040",foreground="cyan")
               name=ttk.Label(prof,font=('Century 15'),text="ονομα:",background="#404040",foreground="cyan")
               name_=ttk.Label(prof,font=('Century 15'),text=data[0],background="#404040",foreground="cyan")
               pas=ttk.Label(prof,font=('Century 15'),text="κωδικος:",background="#404040",foreground="cyan")
               pas_=ttk.Label(prof,font=('Century 15'),text=data[1],background="#404040",foreground="cyan")
               mail=ttk.Label(prof,font=('Century 15'),text="mail:",background="#404040",foreground="cyan")
               mail_=ttk.Label(prof,font=('Century 15'),text=data[2],background="#404040",foreground="cyan")
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
               prof.configure(bg='#404040')
               prof.mainloop()
               #porfile____________________________
       #Publication post _______________________________        
       def Publication(user):
              def get_text():
                     global post_text
                     text_get=post_text.get("1.0","end-1c")
                     save_post(text_get)
              def save_post(text):
                     f=open("data/post.txt","a")
                     f.write(str(user)+"=="+str(text)+"\n")    
                     f.closed        
              global post
              post=Tk()
              post.geometry("450x450")
              post.title("Δημοσίευση")
              global post_text
              #label_______________________________________
              text=ttk.Label(font=('Century 15'),text="Δημοσίευση",background="#404040",foreground="cyan")
              #input_______________________________________
              post_text=Text(post,height=10, width=30)
              #bytton____________________________________________________________________
              back=Button(post,text="back",command=lambda:[close(9),facegram(user)])
              enter=Button(post,text="sharing",command=lambda:[get_text(),close(9),facegram(user)])
              #style____________________
              text.place(x=170,y=0)
              back.place(x=100,y=200)
              enter.place(x=270,y=200)
              post_text.place(x=100,y=30)
              post.configure(bg='#404040')
              post.mainloop()
             
       #code_view_text_post_________________
       def view(i):
              read_post_list=i.split('==')
              print(read_post_list)
              text_post_user=ttk.Label(index,font=('Century 15'),text="ο/η χρητης   "+read_post_list[0],background="#404040",foreground="cyan")
              text_user_post=ttk.Label(index,font=('Century 15'),text=read_post_list[1],background="#404040",foreground="cyan")
              text_post_user.place(x = 20, y = 320)
              text_user_post.place(x = 20, y = 350)
       def file_is_not_null():
                 p=0
                 f=open("data/post.txt","r")
                 while p!="1":
                        i=f.read()
                        if i=="":
                               p=1
                               return False
                        else:
                               view(i)
                               p=1
                 f.closed
       #finish===============================
       #facegram_______________________________________________________________________________________        
       global index
       index= Tk()
       index.geometry("450x550")
       #text_______________________________________________________________________________________________________________________
       text_user=ttk.Label(font=('Century 15'),text="   Καλως Ηρθες"+"\n"+"|_-_-_|  "+user+"  |_-_-_|",background="#404040",foreground="cyan")
       #button________________________________________________________________________________________
       exitt=ttk.Button(index,text="exit",command=lambda:[close(6),home()])
       index.music_=ttk.Button(index,text="παιξε μουσικη",command=lambda:[close(6),music_play(user)])
       index.profile_=ttk.Button(index,text="ο λογαριασμο σου",command=lambda:[close(6),profile(user)])
       post=ttk.Button(index,text="Δημοσίευση",command=lambda:[close(6),Publication(user)])
       post_view=ttk.Button(index,text="εμφανιση Δημοσίευση ",command=lambda:[file_is_not_null()])
       #clock_______________________________________________________________________________________
       clock()
       #imag_______________________________________________________________________________________
       canvas = Canvas(index, width = 450, height = 200)            
       img = PhotoImage(file="image/facegram_home.png")      
       canvas.create_image(10,10, anchor=NW, image=img)
       #style_______________________________________________________________________________________
       text_user.place(x=150,y=200)
       index.profile_.place(x = 10, y = 200)
       index.music_.place(x = 10, y = 230)
       exitt.place(x=360,y=200)
       canvas.place(x = 0, y = 0)
       post.place(x = 360, y = 230)
       post_view.place(x = 10, y = 260)
       index.title("Facegram")
       index.configure(bg='#404040')
       index.mainloop()      
def home():
       global main
       main= Tk()
       main.geometry("450x450")
       text_title=ttk.Label(font=('Century 20'),text="καλως ηρθες"+"\n"+"στο Facegram",background="#404040",foreground="cyan")
       main.title("Facegram")
       #button_________________________________________________________________________
       main.login_=ttk.Button(main,text="εισοδος  ",command=lambda:[close(1),login()])
       quitt=ttk.Button(main,text="quit",command=lambda:[close(1)])      
       #image__________________________________________
       canvas = Canvas(main, width = 400, height = 150)            
       img = PhotoImage(file="image/facegram_logo.png")      
       canvas.create_image(0,0, anchor=NW, image=img)
       #stely___________________________________________
       text_title.place(x=50,y=300) 
       main.login_.place(x = 290, y = 320)
       quitt.place(x = 290, y = 200)
       canvas.place(x = 20, y = 0)
       #color___
       main.configure(bg='#404040')
       main.mainloop()      
home()
