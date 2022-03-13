import datetime
import pygame
import random

pygame.init()
pygame.font.init()

WIDTH,HEIGHT = 700,500
FONT = pygame.font.SysFont("comicsans",50)
PURPLE = (60,25,60)
WHITE = (255,255,255)
DARK = (100,100,100)
LIGHT = (170,170,170)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BENZ MATH QUIZ")

FPS = 60

SYMBOL = ["+","-","*","/"]
random.shuffle(SYMBOL)


class game:
    def __init__(self,rangex,rangey,choicerangey):
        self.rangex,self.rangey = rangex,rangey
        self.choicerangey = choicerangey
        self.symbol = SYMBOL
        self.numbers = []
        self.eval = []
        self.choices = []
        self.sum = 0
        self.qn = ""
        random.shuffle(self.choices)
        self.randomchoices = self.choices

    def question(self):
        for i in range(4):
            self.eval.append(self.numbers[i])
            self.eval.append(self.symbol[i])
        self.eval.append(self.numbers[-1])    
        for i in self.eval :
            self.qn += str(i)   
    def answer(self):
        for i in range(5):
            x = random.randint(self.rangex,self.rangey)
            self.numbers.append(x)
    def sumfunc(self):
        if self.symbol[0] == "+" or "-":
            self.sum = 0
        elif self.symbol[0] == "*" or "/":
            self.sum = 1 
        j = 0
        s = 0
        while s<4:
            if j == 0:
                if self.symbol[s] == "+":
                    self.sum += self.numbers[j]+self.numbers[j+1]  
                    j+=2
                    s+=1
                elif self.symbol[s] == "-":
                    self.sum += self.numbers[j]-self.numbers[j+1] 
                    j+=2
                    s+=1
                elif self.symbol[s] == "*":
                    self.sum += self.numbers[j]*self.numbers[j+1]
                    j+=2 
                    s+=1 
                elif self.symbol[s] == "/":
                    self.sum += self.numbers[j]//self.numbers[j+1]
                    j+=2
                    s+=1
            elif j!=0:
                if self.symbol[s] == "+":
                    self.sum +=self.numbers[j]
                    s+=1
                    j+=1
                elif self.symbol[s] == "-":
                    self.sum -= self.numbers[j]
                    s+=1
                    j+=1
                elif self.symbol[s] == "*":
                    self.sum*=self.numbers[j]
                    s+=1
                    j+=1
                elif self.symbol[s] == "/":
                    self.sum//=self.numbers[j]
                    s+=1
                    j+=1 
    def choice(self):
        x = random.sample(range(self.rangex,self.choicerangey),3)
        self.choices+=x
        self.choices.append(self.sum)  
        random.shuffle(self.choices)         
    def run(self):
        self.answer()
        self.question()
        self.sumfunc()
        self.choice()


class buttons(game) :
    def __init__(self,lenght,breadth,text,cordinates,win,textcor,endcor,textsize):
        self.lenght = lenght
        self.breadth = breadth
        self.text = text
        self.win = win
        self.cor = cordinates
        self.text_cor = textcor
        self.start_cor = cordinates
        self.end_cor = endcor
        self.textsize = textsize
    def writes(self):
        font = pygame.font.SysFont('Corbel',self.textsize)
        text = font.render(self.text,True,WHITE)
        self.win.blit(text ,(self.text_cor[0],self.text_cor[1])) 
    def writeonly(self):
        pygame.draw.rect(self.win,DARK,[self.cor[0],self.cor[1],self.lenght,self.breadth])
        font = pygame.font.SysFont('Corbel',33)
        text = font.render(self.text, True , WHITE)
        self.win.blit(text ,(self.text_cor[0],self.text_cor[1])) 
    def click(self,mouse):
        if self.start_cor[0] <= mouse[0] <= self.end_cor[0] and self.start_cor[1] <= mouse[1] <= self.end_cor[1]:
            pygame.draw.rect(self.win,LIGHT,[self.cor[0],self.cor[1],self.lenght,self.breadth])
            
        else:
            pygame.draw.rect(self.win,DARK,[self.cor[0],self.cor[1],self.lenght,self.breadth])
    def button(self,mouse):
        self.click(mouse)    
        self.writes()
    def write(self):
        font = pygame.font.SysFont('Corbel',self.textsize)
        text = font.render(self.text,True,WHITE,DARK)
        self.win.blit(text ,(self.text_cor[0],self.text_cor[1])) 


def drawstart(win,mouse):  
    win.fill(PURPLE)
    start.button(mouse)
    exit.button(mouse)
    difficulty.button(mouse)
    instructions.button(mouse)
    pygame.display.update()

def drawdiff(win,mouse):  
    win.fill(PURPLE)
    easy.button(mouse)
    medium.button(mouse)
    hard.button(mouse)
    pygame.display.update()


def drawgame(win,mouse,choice1,choice2,choice3,choice4,question,pts,duration,lifee):
    win.fill(PURPLE)
    choice1.button(mouse)
    choice2.button(mouse)
    choice3.button(mouse)
    choice4.button(mouse)
    question.writeonly()
    pts.write()
    lifee.write()
    duration.write()
    pygame.display.update() 

def drawexit(win):
    win.fill(PURPLE)
    font = pygame.font.SysFont('Corbel',100)
    text = font.render("GAME OVER!!!",True,WHITE)
    win.blit(text ,(100,200)) 
    pygame.display.update()

def drawinst(win):
    win.fill(PURPLE)
    font = pygame.font.SysFont('Corbel',70)
    text = font.render("DONT USE BODMAS!!!",True,WHITE)
    win.blit(text ,(100,200)) 
    pygame.display.update()    

medium = buttons(140,40,"MEDIUM",[280,230],WIN,[306,240],[420,270],33)
easy = buttons(140,40,"EASY",[280,160],WIN,[319,170],[420,200],33) 
hard = buttons(140,40,"HARD",[280,300],WIN,[319,310],[420,340],33)


difficulty = buttons(140,40,"DIFFICULTY",[280,230],WIN,[289,240],[420,270],33)
start = buttons(140,40,"START",[280,160],WIN,[314,170],[420,200],33) 
exit = buttons(140,40,"EXIT",[280,300],WIN,[319,310],[420,340],33)
instructions = buttons(140,40,"ADVICEUU",[280,370],WIN,[290,380],[420,400],33)

#back = buttons(140,40,"BACK",[])
def main():
    run = True
    clock = pygame.time.Clock()
    main = "start"
    difficulty = "easy"
    choose = ""
    points = 0
    time = 0
    life = 4
    then = datetime.datetime.now()
    now = datetime.datetime.now()
    print(then)
    while run :
        while time == 0 :
            then = datetime.datetime.now()
            now = datetime.datetime.now()
            dur = now - then
            drtn = dur.total_seconds()
            time = 1
        if main == "start":
            clock.tick(FPS)
            mouse = pygame.mouse.get_pos() 
            drawstart(WIN,mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <= 420 and 160 <= mouse[1] <= 200:
                    main = "next"
                    time =0 
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <= 420 and 230 <= mouse[1] <= 270:
                    main = "difficulty"
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <= 420 and 300 <= mouse[1] <= 340:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <=420  and 370 <= mouse[1] <= 410:    
                    main = "instructions"
        elif main == "difficulty":
            clock.tick(FPS)
            mouse = pygame.mouse.get_pos() 
            drawdiff(WIN,mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <= 420 and 160 <= mouse[1] <= 200:
                    difficulty = "easy"
                    main = "start"
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <= 420 and 230 <= mouse[1] <= 270:
                    difficulty = "medium"
                    main = "start"
                elif event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse[0] <= 420 and 310 <= mouse[1] <= 340:
                    difficulty = "hard"  
                    main = "start"  
        elif main == "game":
            clock.tick(FPS)
            mouse = pygame.mouse.get_pos() 
            drawgame(WIN,mouse,choice1,choice2,choice3,choice4,question,pts,duration,lifee)
            if life < 0 :
                main = "gameover"
            else :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        run = False
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN and 175 <= mouse[0]<=325 and 250<=mouse[1]<=280 :
                        main = "next"
                        choose = 1
                    elif event.type == pygame.MOUSEBUTTONDOWN and 175 <= mouse[0]<=325 and 330<=mouse[1]<=450 :
                        main = "next"
                        choose = 2
                    elif event.type == pygame.MOUSEBUTTONDOWN and 365 <= mouse[0]<=505 and 250<=mouse[1]<=290 :
                        main = "next"
                        choose = 3
                    elif event.type == pygame.MOUSEBUTTONDOWN and 365 <= mouse[0]<=495 and 330<=mouse[1]<=370 :
                        main = "next"
                        choose = 4
        elif main == "exit":
            clock.tick(FPS)
            mouse = pygame.mouse.get_pos() 
            drawstart(WIN,mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                    break  
        elif main == "next":       
            if choose == 1 :
                temp = int(x["c1"])
                if choicelist[2]==temp:
                    points+=1
                else:
                    life-=1    
                time=0
                choose = ""    
            elif choose == 2 :
                temp = int(x["c2"])
                if choicelist[2]==temp:
                    points+=1
                else:
                    life-=1    
                time=0
                choose = ""   
            elif choose == 3 :
                temp = int(x["c3"])
                if choicelist[2]==temp:
                    points+=1
                else:
                    life-=1    
                time=0
                choose = ""   
            elif choose == 4 :
                temp = int(x["c4"])
                if choicelist[2]==temp:
                    points+=1
                else:
                    life-=1
                time=0
                choose = ""
            elif choose == "":
                life-=1           
                
            if difficulty == "easy":
                choiceback = game(1,10,70)
            elif difficulty == "medium":
                choiceback = game(1,50,500)
            elif difficulty == "hard":
                choiceback = game(1,100,1000)    
            choiceback.answer()
            choiceback.question()
            choiceback.sumfunc()
            choiceback.choice()
            def loop():
                question = choiceback.qn
                answer = choiceback.sum
                choice = choiceback.choices
                return choice,question,answer
            choicelist = loop()
            x = {"c1":str(choicelist[0][0]),
            "c2":str(choicelist[0][1]),
            "c3":str(choicelist[0][2]),
             "c4":str(choicelist[0][3]),
            "qn":str(choicelist[1]),
            "pts":str(points),
            "life":str(life)}

            choice1 = buttons(140,40,x["c1"],[175,250],WIN,[210,260],[325,280],33)
            choice2 = buttons(140,40,x["c2"],[175,330],WIN,[210,340],[325,450],33) 
            choice3 = buttons(140,40,x["c3"],[365,250],WIN,[400,260],[505,290],33)
            choice4 = buttons(140,40,x["c4"],[365,330],WIN,[400,340],[495,370],33)
            question = buttons(330,80,x["qn"],[175,130],WIN,[175+82,250-80-40+30],[None,None],33) 
            pts = buttons(140,40,"  POINTS:"+x["pts"]+"  ",[700-140,0],WIN,[180,0],[None,None],33)
            lifee = buttons(140,40," "+"LIFE:"+x["life"],[700-280],WIN,[305,0],[None,None],33)
            main = "game"
            drtm = 0
            time = 0  
        elif main == "gameover":
            drawexit(WIN)     
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    main = "start"
                    life = 4
                    points = 0
        elif main == "instructions":
            drawinst(WIN)     
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    main = "start" 
        now = datetime.datetime.now() 
        dur = now - then
        drtn = int(dur.total_seconds())
        k = {"duration":str(drtn)}
        duration =  buttons(140,40,"COUNTDOWN:"+k["duration"]+"  ",[0,0],WIN,[0,0],[None,None],33)
        duration.write()
        if drtn>10 and main == "game":
            main = "next"   
if __name__ == "__main__":
    main()
