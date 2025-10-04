import pygame
import random
pygame.init()
s=pygame.display.set_mode((1200,700))
run=True
game=True
image=pygame.image.load("6.PNG")
image=pygame.transform.scale(image,(400,400))
font=pygame. font.SysFont("monospace",23)
font2=pygame. font.SysFont("monospace",50)
intro=font.render("BRO: HELP! , FIND SECERET NAME TO SAVE ME",1,(0,0,0))
l=["sathasin","karthick","sriram","ashawath","venkatesh","arun","asarsiddiq","dinesh","yogesh","gokul","muthusankar","muthukrishnan","hari","harisivabalan","panchali","pappuraj","ramkumar",
   "saktivel","sanjay","sivabalan","thirumoorthi","thiruramkumar","vignesh","avinash","sankar","sinivasabalan","janarthan","priyadharshan","karthikeayan","enbashankar","jeffrin","sivabalan","aravind"]
name=random.choice(l)
health=6
glist=[]
j=""
guess=""
q=""
for i in name:
        j=j+"*"
p=font2.render(j,1,(0,0,0))
p1=font.render("",1,(0,0,0))
p2=font.render("",1,(0,0,0))
p3=font.render("",1,(0,0,0))
while run:
    while game:
        s.fill((255,255,255))
        s.blit(image,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                game=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    q="a"
                if event.key==pygame.K_b:
                    q="b"
                if event.key==pygame.K_c:
                    q="c"
                if event.key==pygame.K_d:
                    q="d"             
                if event.key==pygame.K_e:
                    q="e"
                if event.key==pygame.K_f:
                    q="f"
                if event.key==pygame.K_g:
                    q="g"
                if event.key==pygame.K_h:
                    q="h"
                if event.key==pygame.K_i:
                    q="i"
                if event.key==pygame.K_j:
                    q="j"
                if event.key==pygame.K_k:
                    q="k"
                if event.key==pygame.K_l:
                    q="l"
                if event.key==pygame.K_m:
                    q="m"
                if event.key==pygame.K_n:
                    q="n"
                if event.key==pygame.K_o:
                    q="o"
                if event.key==pygame.K_p:
                    q="p"
                if event.key==pygame.K_q:
                    q="q"
                if event.key==pygame.K_r:
                    q="r"
                if event.key==pygame.K_s:
                    q="s"
                if event.key==pygame.K_t:
                    q="t"
                if event.key==pygame.K_u:
                    q="u"
                if event.key==pygame.K_v:
                    q="v"
                if event.key==pygame.K_w:
                    q="w"
                if event.key==pygame.K_x:
                    q="x"
                if event.key==pygame.K_y:
                    q="y"
                if event.key==pygame.K_z:
                    q="z"
                if event.key==pygame.K_UP:
                    guess=q
        a=font.render("enter guess : "+q,1,(0,0,0))
        if guess!="" and guess not in glist and health>0  and "*" in j :
                glist.append(guess)
                if guess in name:
                    temp=""
                    for i in name:
                        if i in glist:
                            temp=temp+i
                        else:
                            temp=temp+"*"
                    j=temp
                    p=font2.render(j,1,(0,0,0))
                    if "*" in j:
                        k=str(health)
                        o=str(glist)
                        p1=font.render("your guess is right and only"+k+"lives you have",1,(0,0,0))
                        p2=font.render("your guesses : "+o,1,(0,0,0))
                        p3=font.render("BRO:YES,RIGHT YOU CAN DO IT ",1,(0,0,0))
                    else:
                        p1=font.render("",1,(0,0,0))
                        p2=font.render("",1,(0,0,0))
                        p3=font.render("WE WON",1,(0,0,0))
                        image=pygame.image.load("7.PNG")
                        image=pygame.transform.scale(image,(400,400))
                        break
                else:
                     health=health-1
                     k=str(health)
                     o=str(glist)
                     image=pygame.image.load(k+".PNG")
                     image=pygame.transform.scale(image,(400,400))
                     if health!=0:
                        p1=font.render("BRO:PLS!, DON'T MAKE MISTAKE YOU HAVE ONLY "+k+"  CHANCE TO SAVE ME ",1,(0,0,0))
                        p2=font.render("your guesses : "+o,1,(0,0,0))   
                        image=pygame.transform.scale(image,(500,500))
                     else:
                        p1=font.render("BRO:OH NOOOO, I AM DEATH ",1,(0,0,0))
                        p2=font.render("you lose and the real word is "+name,1,(0,0,0))
                        p3=font.render("sorry bro",1,(0,0,0))
                        break
        s.blit(intro,(420,30))
        s.blit(p,(420,70))
        s.blit(a,(420,140))
        s.blit(p1,(420,180))
        s.blit(p2,(420,230))
        s.blit(p3,(420,270))
        pygame.display.update()
pygame.quit()
