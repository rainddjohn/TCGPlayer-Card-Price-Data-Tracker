import pygame;pygame.init()
set='Crimson Vow'
(width,height)=(300,700);background_color= (0,0,0);screen=pygame.display.set_mode((width,height));screen.fill(background_color);pygame.display.set_caption(f'{set}')
f= open('crimson_vow.txt', 'r')
list1=[];list2=[]
#takes txt file and converts it into a list of strings
for i in f:
    if i=='\n':continue
    lastchar=i[-1:]
    i=i[:-1]
    list1.append(i)
list1[-1]=list1[-1]+lastchar
#takes the comma'ed string and turns it into a list seperated by commas
for i in list1:
    i=i.split(',')
    list2.append(i)
#accounts for cards that have a comma in the name
x=1;y=0;list1=[]
while x < len(list2):
    while y != len(list2[x]):
        if y+1==len(list2[x]):list1.append(list2[x][y]);break
        if list2[x][y]=='Umbris' or  list2[x][y]=='Toxrill' or list2[x][y]=='Olivia'or list2[x][y]=='Chandra'or list2[x][y]=='Kaya' or list2[x][y]=='Thalia':
            #print('list2[x][y] is',list2[x][y],y,len(list2[x]),list1)
            list2[x][y]=list2[x][y]+','+str(list2[x][y+1]);list1.append(list2[x][y]);y+=2
        else: list1.append(list2[x][y]);y+=1
    list2[x]= list(list1);list1=[];x+=3;y=0
adjuster=int(len(list2)/3)
baseadjuster=int(adjuster)

def display(list2,adjuster,baseadjuster):
    #resets screen
    screen.fill(background_color)
    # sets font for header (set/date)
    font = pygame.font.Font('freesansbold.ttf', 20);text = font.render('', True, (0, 0, 0), (0, 0, 0))
    text=font.render(f'{list2[adjuster*3-3][0]}', True, (255,255,255),(0,0,0))
    screen.blit(text, (10, 10))
    if adjuster>1:
        text=font.render('Back', True, (255,255,255),(0,0,0)); screen.blit(text, (135, 10))
    if adjuster!=baseadjuster:
        text = font.render('Forward', True, (255, 255, 255), (0, 0, 0));screen.blit(text, (195, 10))
    #sets font for body/prices
    font = pygame.font.Font('freesansbold.ttf', 15);text = font.render('', True, (0, 0, 0), (0, 0, 0))
    for i in range(len(list2[adjuster*3-2])):
        text = font.render (f'{list2[adjuster*3-2][i]}' + '  ' + f'{list2[adjuster*3-1][i]}', True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (10, 40+i*20))
    pygame.display.update()

def button(mouse,adjuster,baseadjuster):
    print('adjuster is',adjuster)
    #back button
    if 135 <=mouse[0]<=181 and 10<=mouse[1]<=25 and adjuster !=1:
        adjuster-=1;display(list2,adjuster,baseadjuster)
    #forward button
    if 195 <= mouse[0] <= 275 and 10 <= mouse[1] <= 25 and adjuster != baseadjuster:
        adjuster+=1;display(list2,adjuster,baseadjuster)
    return adjuster
display(list2,adjuster,baseadjuster)
pygame.display.flip();running= True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False;pygame.quit();exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            adjuster=button(mouse,adjuster,baseadjuster)
            print(mouse)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()