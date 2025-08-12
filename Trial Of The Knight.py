from pygame import *

init()
font.init()
size=width,height=1200,800 #size of the display
screen=display.set_mode(size) 

BLACK=(0,0,0) #colors
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

GROUND=height#Ground is equal to 

jumpSpeed=-30 #jumping used by the playering to go into the air
gravity=1.5     #gravity, pushing the player down in air
bottom=GROUND #bottom = GROUND
dash_count=0 #dash count means if dash count is 0 the player is not able to dash and if dash count is 1 the player can dash
timer=0 #used to meaure time and how long something will take
level_1_rect=Rect(850,150,240,80) #level 1 rect used to add a button to the menu making it possible to access level 1
level_2_rect=Rect(850,300,240,80) #level 2 rect used to add a button to the menu making it possible to access level 2
instructions_rect=Rect(850,450,240,80) #If clicked it's purpose is to indicate the player wants to go to the instructions screen
quit_rect=Rect(850,600,240,80) #if clicked it'll quit the program

restart_rect=Rect(430,580,100,100) #used to indicate the player wants to restart
menu_rect=Rect(545,580,100,100) #used to indicate the player want to go back to the menu
next_level_rect=Rect(660,580,100,100) #used to indicate the player wants to the next level

X=0 #the x axis 
Y=1 #the y axis
W=2 #the width
H=3 #the height
BOT=2 #used to access the third element in the v list
one=1 #used to change the color of the title
one_scroll=1 #used to add a scrolling animation to the menu
side_chose=1
r=0 #r value of title color
b=0 # b value of title color
g=0 #g value of title color
action='menu' #action means what screen the player is currently on, the menu is the default and starting screen
myClock=time.Clock() #used to set up the framerate later on
death=0 #used to count the number of death
level=0 #what level the player is on
restart_level_1=0 #if the player want to restart to level 1
restart_level_2=0 #if the player want to restart to level 2
next_stage=0 #if the player want to go to the next stage
help_box=0 #what help box is the player on, 0 means the player isn't accessing any

  #X #Y BOT
v=[0,0,bottom] #used in some parts of where the player needs to move
        #X   Y  W  H
p=Rect(250,150,40,80) #player hit box

#word sizes
Stgotic_font=font.SysFont('Stgotic',150) 
Stgotic_font_2=font.SysFont('Stgotic',155)
Stgotic_font_3=font.SysFont('Stgotic',80)
Stgotic_font_4=font.SysFont('Stgotic',84)
Stgotic_font_5=font.SysFont('Stgotic',40)
Stgotic_font_6=font.SysFont('Stgotic',200)
Stgotic_font_7=font.SysFont('Stgotic',210)

#Texts used in program 
word=Stgotic_font.render("Level Complete",True,(255,235,140))
word_2=Stgotic_font_2.render("Level Complete",True,(180,170,150))
run_word=Stgotic_font_3.render("RUN",True,RED)
run_word_2=Stgotic_font_4.render("RUN",True,BLUE)
jump_word=Stgotic_font_3.render("JUMP",True,RED)
jump_word_2=Stgotic_font_4.render("JUMP",True,BLUE)
dash_word=Stgotic_font_3.render("DASH",True,RED)
dash_word_2=Stgotic_font_4.render("DASH",True,BLUE)
run_text=Stgotic_font_5.render("Press the left arrow to move left",True,(80,60,5))
run_text_2=Stgotic_font_5.render("and the right arrow to move right",True,(80,60,5))
jump_text=Stgotic_font_5.render("Press the space bar or the ",True,(80,60,5))
jump_text_2=Stgotic_font_5.render('up arrow to jump into the air',True,(80,60,5))
dash_text=Stgotic_font_5.render("Press the down arrow to dash, you can't dash",True,(80,60,5))
dash_text_2=Stgotic_font_5.render('multiple times and to recharge the dash you',True,(80,60,5))
dash_text_3=Stgotic_font_5.render("must first jump. You can control the distance",True,(80,60,5))
dash_text_4=Stgotic_font_5.render("of the dash depending on how long you press",True,(80,60,5))
quit_word=Stgotic_font_3.render("Quit",True,(30,200,230))
quit_word_2=Stgotic_font_4.render("Quit",True,(25,95,110))
level_1_word=Stgotic_font_3.render("Level 1",True,(205,105,240))
level_1_word_2=Stgotic_font_4.render("Level 1",True,(100,30,125))
level_2_word=Stgotic_font_3.render("Level 2",True,(205,105,240))
level_2_word_2=Stgotic_font_4.render("Level 2",True,(100,30,125))

#help boxes text
help_text_1=Stgotic_font_5.render("Use up arrow to jump",True,(150,115,5))
help_text_2=Stgotic_font_5.render("Use down arrow to dash",True,(150,115,5))
help_text_3=Stgotic_font_5.render("The Green blocks can propel,",True,(150,115,5))
help_text_4=Stgotic_font_5.render("you up when ever you hit it",True,(150,115,5))
help_text_5=Stgotic_font_5.render("In the next section, you must move",True,(150,115,5))
help_text_6=Stgotic_font_5.render('in the air to get past the obstacles',True,(150,115,5))

#pictures
arrow_2=image.load('Pics/pixel_arrow.png')
arrow=transform.scale(arrow_2,(55,40))
arrow_diagonal_2=image.load('Pics/pixel_arrow_diagonal.png')
arrow_diagonal=transform.scale(arrow_diagonal_2,(46,40))
down_arrow_2=image.load('Pics/pixel_down_arrow_diagonal.png')
down_arrow=transform.scale(down_arrow_2,(46,40))
level_complete_pic_2=image.load('Pics/level_complete.png')
level_complete_pic=transform.scale(level_complete_pic_2,(900,605))
pixel_star_2=image.load('Pics/pixel_star.png')
pixel_star=transform.scale(pixel_star_2,(200,200))
pixel_grey_star_2=image.load('Pics/pixel_grey_star.png')
pixel_grey_star=transform.scale(pixel_grey_star_2,(200,200))
restart_level_2=image.load('Pics/restart.png')
restart_level=transform.scale(restart_level_2,(100,100))
home_button_2=image.load('Pics/home_button.png')
home_button=transform.scale(home_button_2,(100,100))
next_button_2=image.load('Pics/next_button.png')
next_button=transform.scale(next_button_2,(100,100))
scroll_2=image.load('Pics/scroll.png')
scroll=transform.scale(scroll_2,(750,300))
death_2=image.load('Pics/death_pixel.png')
death_pic=transform.scale(death_2,(80,80))
old_paper_2=image.load('Pics/old_paper.png')
old_paper=transform.scale(old_paper_2,(1200,900))
button_2=image.load('Pics/button.png')
button=transform.scale(button_2,(300,120))
question_2=image.load('Pics/question_pixel.png')
question=transform.scale(question_2,(44,60))
death_box_2=image.load("Pics/death_box.png")
death_box=transform.scale(death_box_2,(240,120))
pilar_2=image.load("Pics/pilar_pixel.png")
pilar=transform.scale(pilar_2,(180,810))

#music
mixer.music.load('Sounds/ByteSoundtrackLoopv2.ogg')

#other lists for player movement animation
idle_pics=[]
run_pics=[]
jump_pics=[]
dash_pics=[]
bw_idle_pics=[]
bw_run_pics=[]
bw_jump_pics=[]
bw_dash_pics=[]
background=[]
idle_frame=0
run_frame=0
jump_frame=0
dash_frame=0
bw_idle_frame=0
bw_run_frame=0
bw_jump_frame=0
bw_dash_frame=0
block_pics=[]

#For loops used to add pictures to the lists above
for i in range (4): 
    idle_pics.append(image.load("Pics/sized_player_idle_" + str(i) + ".png"))
for i in range (6):
    run_pics.append(image.load("Pics/sized_player_run_" + str(i) + ".png"))
for i in range (7):
    jump_pics.append(image.load("Pics/sized_player_jump_" + str(i) + ".png"))
for i in range (1):
    dash_pics.append(image.load("Pics/sized_player_dash_" + str(i) + ".png"))
for i in range (4):
    bw_idle_pics.append(image.load("Pics/bw_player_idle_" + str(i) + ".png"))
for i in range (6):
    bw_run_pics.append(image.load("Pics/bw_player_run_" + str(i) + ".png"))
for i in range (7):
    bw_jump_pics.append(image.load("Pics/bw_player_jump_" + str(i) + ".png"))
for i in range (1):
    bw_dash_pics.append(image.load("Pics/bw_player_jump_" + str(i) + ".png").convert_alpha())
for a in range(5):
    background.append(image.load('Pics/background_image_'+str(a)+'.png'))

background_cord=[-500,2500,3900,6400,7625,9500,12500,13900,16400,17650] #cordinates of backgrounds
pilar_cord=[2400,3780,6265,7525,9400,12400,16300,17550] #cordinates of pilar pictures

#used to play the music
mixer.music.play(-1)

blocks=[[Rect(0,500,122,118),0],[Rect(104,495,122,118),1],[Rect(226,495,122,118),1],[Rect(348,495,122,118),1], #Platfrom 1
        [Rect(470,495,122,118),1],[Rect(592,502,122,118),2],[Rect(592,600,122,118),5],[Rect(592,698,122,118),5], #Platfrom 1
        [Rect(223,595,122,118),4],[Rect(223,720,122,118),4],[Rect(345,595,122,118),4],[Rect(345,720,122,118),4], #Platfrom 1
        [Rect(5,595,122,118),3],[Rect(5,717,122,118),3], #Platfrom 1
        [Rect(1000,400,122,118),0],[Rect(1104,395,122,118),1],[Rect(1226,395,122,118),1],[Rect(1348,395,122,118),1], #Platfrom 2
        [Rect(1470,402,122,118),2],[Rect(1470,500,122,118),5],[Rect(1470,598,122,118),5],[Rect(1470,696,122,118),5], #Platfrom 2
        [Rect(1223,497,122,118),4],[Rect(1223,621,122,118),4],[Rect(1223,746,122,118),4],[Rect(1004,495,122,118),3], #Platfrom 2
        [Rect(1004,590,122,118),3],[Rect(1004,685,122,118),3], #Platfrom 2
        [Rect(1900,313,122,118),1],[Rect(1898,413,122,118),4],[Rect(1898,538,122,118),4],[Rect(1898,663,122,118),4], #Platfrom 3
        [Rect(2398,221,122,118),0],[Rect(2502,216,122,118),1],[Rect(2624,222,122,118),2],[Rect(2402,316,122,118),3], #Platfrom 4
        [Rect(2402,443,122,118),3],[Rect(2402,570,122,118),3],[Rect(2402,697,122,118),3],[Rect(2624,320,122,118),5], #Platfrom 4
        [Rect(2624,418,122,118),5],[Rect(2624,516,122,118),5],[Rect(2624,616,122,118),5],[Rect(2624,714,122,118),5], #Platfrom 4
        [Rect(3201,596,122,118),1],[Rect(3322,596,122,118),1],[Rect(3444,596,122,118),1],[Rect(3198,694,122,118),4], #Platfrom 5
        [Rect(3441,694,122,118),4], #Platfrom 5
        [Rect(4901,701,122,118),0],[Rect(5005,696,122,118),1],[Rect(5109,696,122,118),1],[Rect(5213,696,122,118),1], #Platfrom 7
        [Rect(5337,703,122,118),2], #Paltfrom 7
        [Rect(6501,394,122,118),1],[Rect(6499,494,122,118),4],[Rect(6499,619,122,118),4],[Rect(6499,744,122,118),4], #Platfrom 9
        [Rect(6623,394,122,118),1],[Rect(6623,494,122,118),4],[Rect(6623,619,122,118),4],[Rect(6623,744,122,118),4], #Platfrom 9
        [Rect(7401,751,122,118),0],[Rect(7505,746,122,118),1],[Rect(7628,751,122,118),2], #Platfrom 11
        [Rect(8401,601,122,118),0],[Rect(8505,596,122,118),1],[Rect(8627,603,122,118),2],[Rect(8406,696,122,118),3], #Paltfrom 14
        [Rect(8502,694,122,118),4],[Rect(8627,699,122,118),5], #Platfrom 14
        [Rect(10501,596,122,118),1],[Rect(10498,694,122,118),4], #Platfrom 20
        [Rect(11501,496,122,118),1],[Rect(11626,496,122,118),1],[Rect(11499,594,122,118),4],[Rect(11624,594,122,118),4], #Platfrom 22
        [Rect(11499,719,122,118),4],[Rect(11624,719,122,118),4], #Platfrom 22
        [Rect(12001,296,122,118),1],[Rect(12123,296,122,118),1],[Rect(11999,394,122,118),4],[Rect(11999,519,122,118),4], #Paltfrom 23
        [Rect(11999,644,122,118),4],[Rect(11999,769,122,118),4],[Rect(12121,394,122,118),4],[Rect(12121,519,122,118),4], #Paltfrom 23
        [Rect(12121,643,122,118),4],[Rect(12121,768,122,118),4], #Platfrom 23
        [Rect(4201,601,122,118),7],[Rect(4328,601,122,118),7],[Rect(4328,700,122,118),10],[Rect(4201,700,122,118),10], #Platfrom 6
        [Rect(6100,600,122,118),7],[Rect(6227,600,122,118),7],[Rect(6100,699,122,118),10],[Rect(6227,699,122,118),10], #Platfrom 8
        [Rect(6800,301,122,118),12],[Rect(6905,300,122,118),13],[Rect(7033,300,122,118),13],[Rect(7159,300,122,118),14], #Platfrom 10
        [Rect(6809,400,122,118),15],[Rect(6809,527,122,118),15],[Rect(6809,654,122,118),15],[Rect(6809,781,122,118),15], #Platfrom 10
        [Rect(7159,400,122,118),17],[Rect(7159,530,122,118),17],[Rect(7159,660,122,118),17],[Rect(7159,790,122,118),17], #Platfrom 10
        [Rect(8200,600,122,118),13],[Rect(8200,698,122,118),16], #Platfrom 12
        [Rect(9001,601,122,118),7],[Rect(9128,601,122,118),7],[Rect(9001,700,122,118),10],[Rect(9128,700,122,118),10], #Platfrom 14
        [Rect(9500,300,122,118),13],[Rect(9500,398,122,118),16],[Rect(9500,525,122,118),16],[Rect(9500,652,122,118),16], #Platfrom 15
        [Rect(9500,679,122,118),16], #Platfrom 15
        [Rect(9701,401,122,118),7],[Rect(9828,401,122,118),7],[Rect(9828,500,122,118),10],[Rect(9828,599,122,118),10], #Platfrom 16
        [Rect(9828,698,122,118),10],[Rect(9701,500,122,118),10],[Rect(9701,599,122,118),10],[Rect(9701,698,122,118),10], #Platfrom 16
        [Rect(10150,200,122,118),13],[Rect(10150,298,122,118),16],[Rect(10150,396,122,118),16],[Rect(10150,494,122,118),16], #Platfrom 17
        [Rect(10150,592,122,118),16],[Rect(10150,690,122,118),16], #Platfrom 17
        [Rect(11001,601,122,118),7],[Rect(11001,699,122,118),10], #Platfrom 19
        [Rect(12400,300,122,118),13],[Rect(12528,300,122,118),13],[Rect(12400,398,122,118),16],[Rect(12400,525,122,118),16], #Platfrom 22
        [Rect(12400,652,122,118),16],[Rect(12400,779,122,118),16],[Rect(12528,398,122,118),16],[Rect(12528,525,122,118),16], #Platfrom 22
        [Rect(12528,652,122,118),16],[Rect(12528,779,122,118),16], #Platfrom 22
        [Rect(13000,750,122,118),18],[Rect(13105,750,122,118),19],[Rect(13231,750,122,118),20]] #Winning Platfrom

blocks_2=[[Rect(150,600,122,188),0],[Rect(254,595,122,188),1],[Rect(376,595,122,188),1],[Rect(500,600,122,188),2], #Platfrom 1
          [Rect(155,695,122,188),3],[Rect(500,698,122,188),5], #Platfrom 1
          [Rect(900,595,122,188),1],[Rect(897,695,122,188),4], #Platfrom 2
          [Rect(1600,395,122,188),1],[Rect(1597,495,122,188),4],[Rect(1597,620,122,188),4],[Rect(1597,745,122,188),4], #Platfrom 3
          [Rect(2400,750,122,188),7],[Rect(2527,750,122,188),7], #Platfrom 4
          [Rect(2900,440,122,188),13],[Rect(3028,440,122,188),13],[Rect(3028,538,122,188),16],[Rect(3028,664,122,188),16], #Platfrom 5
          [Rect(3028,790,122,188),16],[Rect(2900,538,122,188),16],[Rect(2900,664,122,188),16],[Rect(2900,790,122,188),16], #Platfrom 5
          [Rect(3300,750,122,188),7],[Rect(3427,750,122,188),7],[Rect(3552,750,122,188),7], #Platfrom 6
          [Rect(4000,300,122,188),0],[Rect(4104,295,122,188),1],[Rect(4226,295,122,188),1],[Rect(4350,300,122,188),2], #Platfrom 7
          [Rect(4005,395,122,188),3],[Rect(4005,490,122,188),3],[Rect(4005,585,122,188),3],[Rect(4005,680,122,188),3], #Platfrom 7
          [Rect(4350,395,122,188),5],[Rect(4350,490,122,188),5],[Rect(4350,585,122,188),5],[Rect(4350,680,122,188),5], #Platfrom 7
          [Rect(5400,750,122,188),7],[Rect(5527,750,122,188),7],[Rect(5652,750,122,188),7], #Platfrom 8
          [Rect(6000,350,122,188),0],[Rect(6104,345,122,188),1],[Rect(6226,345,122,188),1],[Rect(6350,350,122,188),2], #Platfrom 9
          [Rect(6005,445,122,188),3],[Rect(6005,540,122,188),3],[Rect(6005,635,122,188),3],[Rect(6005,730,122,188),3], #Platfrom 9
          [Rect(6350,445,122,188),5],[Rect(6350,540,122,188),5],[Rect(6350,635,122,188),5],[Rect(6350,730,122,188),5],
          [Rect(6600,250,122,188),12],[Rect(6701,250,122,188),13],[Rect(6826,250,122,188),13],[Rect(6952,250,122,188),13], #Platfrom 10
          [Rect(7078,250,122,188),14],[Rect(6609,349,122,188),15],[Rect(6609,478,122,188),15],[Rect(6609,589,122,188),15], #Platfrom 10
          [Rect(6609,718,122,188),15],[Rect(7078,349,122,188),17],[Rect(7078,478,122,188),17],[Rect(7078,589,122,188),17], #Platfrom 10
          [Rect(7078,718,122,188),17], #Platfrom 10
          [Rect(7250,750,122,188),7],[Rect(7377,750,122,188),7], #Platfrom 11
          [Rect(7700,450,122,188),13],[Rect(7700,549,122,188),16],[Rect(7700,678,122,188),16], #Platfrom 12
          [Rect(7950,500,122,188),13],[Rect(7950,599,122,188),16],[Rect(7950,728,122,188),16], #Platfrom 13
          [Rect(8100,750,122,188),0],[Rect(8204,745,122,188),1],[Rect(8326,745,122,188),1],[Rect(8448,745,122,188),1], #Platfrom 14
          [Rect(8570,750,122,188),2], #Platfrom 14
          [Rect(8801,566,122,188),1],[Rect(8799,666,122,188),4],[Rect(8799,781,122,188),4], #Platfrom 15
          [Rect(9101,346,122,188),1],[Rect(9099,446,122,188),4],[Rect(9099,571,122,188),4],[Rect(9099,696,122,188),4], #Platfrom 16
          [Rect(9400,250,122,188),13],[Rect(9400,349,122,188),16],[Rect(9400,474,122,188),16],[Rect(9400,599,122,188),16], #Platfrom 17
          [Rect(9400,724,122,188),16], #Platfrom 17
          [Rect(10100,600,122,188),7],[Rect(10227,600,122,188),7],[Rect(10227,699,122,188),10],[Rect(10100,699,122,188),10], #Platfrom 18
          [Rect(10701,546,122,188),1],[Rect(10699,646,122,188),4],[Rect(10699,771,122,188),4], #Platfrom 19
          [Rect(11101,346,122,188),1],[Rect(11099,446,122,188),4],[Rect(11099,571,122,188),4],[Rect(11099,696,122,188),4], #Platfrom 20
          [Rect(11300,250,122,188),13],[Rect(11300,348,122,188),16],[Rect(11300,348,122,188),16],[Rect(11300,474,122,188),16], #Platfrom 21
          [Rect(11300,600,122,188),16],[Rect(11300,726,122,188),16], #Platfrom 21
          [Rect(11600,650,122,188),13],[Rect(11600,749,122,188),16], #Platfrom 22
          [Rect(11800,750,122,188),19],[Rect(11928,750,122,188),19]] #Winning Platfrom

def menu(action): #the menu
    'Preforms and shows the menu'
    while action=="menu":
        for evnt in event.get():            
            if evnt.type==QUIT: 
                return "menu"
            
        global platform
        global walls
        global bounce_plat
        global bounce_plat_2
        global walls_2
        global platform_2
        global restart_level_1
        global restart_level_2
        global next_stage
        global death
        global one
        global r
        global b
        global g
        global pilar_cord
        global background_cord
        global one_scroll
        #used to change variables

        draw.rect(screen,GREEN,level_1_rect) #menu buttons
        draw.rect(screen,GREEN,level_2_rect) 
        draw.rect(screen,GREEN,instructions_rect)
        draw.rect(screen,GREEN,quit_rect)

        #add the images to the menu
        for a in range(5):
            screen.blit(background[a],(background_cord[a],-100))
        for a in range(5):
            screen.blit(background[a],(background_cord[a+5],-100))

        #add the pilar images to the menu
        for a in range(len(pilar_cord)):
            screen.blit(pilar,(pilar_cord[a],0))
        
        r+=one #used to change the color of tittle
        b+=one
        g+=one
        
        for a in range(len(pilar_cord)): #for loop used to add scrolling animation to the background of the menu
            pilar_cord[a]+=one_scroll
        for a in range(len(background_cord)):
            background_cord[a]+=one_scroll
        
        if r==255 or r==0:
            one=-one # is r is 255 or r is 0 one is now the negative of it self 
        if background_cord[1]==3000 or background_cord[1]==-16400:
            one_scroll=-one_scroll #if background[1] is 3000 or -16400 one_scroll becomes negative of it self

        Stgotic_font_6=font.SysFont('Stgotic',200) #knight font
        Stgotic_font_7=font.SysFont('Stgotic',210)
        knight=Stgotic_font_6.render("Knight",True,(r,b,g)) #screen blits the title
        knight_2=Stgotic_font_7.render("Knight",True,(255,30,160))
        title=Stgotic_font.render("Trial of the",True,(r,b,g))
        title_2=Stgotic_font_2.render("Trial of the",True,(255,230,160))

        screen.blit(button,(825,130))
        screen.blit(button,(825,280))
        screen.blit(button,(825,430)) #blits images
        screen.blit(button,(825,580))
        screen.blit(level_1_word_2,(875,165))
        screen.blit(level_1_word,(875,163))
        screen.blit(level_2_word_2,(875,316))
        screen.blit(level_2_word,(875,314))
        screen.blit(quit_word_2,(910,615))
        screen.blit(quit_word,(910,615))
        screen.blit(question,(875,460))
        screen.blit(question,(950,460))
        screen.blit(question,(1025,460))

        screen.blit(title_2,(148,142))
        screen.blit(title,(150,140))
        screen.blit(knight_2,(172,282))
        screen.blit(knight,(180,280))

        mx,my=mouse.get_pos() #locating of mouse is
        mb=mouse.get_pressed() #if mouse clicks and used to make the player click stuff
        #establishes mx, my and mb to use later on

        death=0 #if player returns to menu, death is 0
        
        if restart_level_1==1: #if the player presse restart in the complete screen menu, the program will go to the menu and go to the level 1 or 2 automatics this is prevent it so the level complete screen pops up when the player presses exit
            p=Rect(250,150,40,80)
            
            platform=[Rect(0,500,698,20),Rect(1000,400,480,20),Rect(1900,320,130,20),
                              Rect(2400,220,327,20),Rect(3200,600,375,20),Rect(4900,700,554,20),
                              Rect(6500,400,257,20),Rect(7400,750,345,20),Rect(8400,600,340,20),
                              Rect(10500,600,135,20),Rect(11500,500,254,20),
                              Rect(12000,300,257,20),Rect(13000,750,350,200)]

            bounce_plat=[Rect(4200,600,255,20),Rect(6100,600,255,20),Rect(9000,600,260,20),
                                 Rect(9700,400,255,20),Rect(11000,600,125,20)]

            walls=[Rect(1,521,698,300),Rect(1001,401,578,400),
                           Rect(1901,321,128,500),Rect(2401,221,325,600),Rect(3201,601,373,400),
                           Rect(4201,601,253,400),Rect(4901,701,550,200),Rect(6101,601,253,400),
                           Rect(6501,401,255,500),Rect(6800,300,470,600),Rect(7401,751,343,200),
                           Rect(8200,600,125,300),Rect(8401,601,338,400),
                           Rect(9001,601,258,400),Rect(9500,300,130,500),Rect(9701,401,253,600),
                           Rect(10150,200,127,700),Rect(10501,601,133,400),
                           Rect(11001,601,123,400),Rect(11501,501,252,400),Rect(12001,301,255,600),
                           Rect(12400,300,260,600),Rect(13001,752,698,200),
                           Rect(-500,775,16000,100)]
                
            blocks=[[Rect(0,500,122,118),0],[Rect(104,495,122,118),1],[Rect(226,495,122,118),1],[Rect(348,495,122,118),1], #Platfrom 1
            [Rect(470,495,122,118),1],[Rect(592,502,122,118),2],[Rect(592,600,122,118),5],[Rect(592,698,122,118),5], #Platfrom 1
            [Rect(223,595,122,118),4],[Rect(223,720,122,118),4],[Rect(345,595,122,118),4],[Rect(345,720,122,118),4], #Platfrom 1
            [Rect(5,595,122,118),3],[Rect(5,717,122,118),3], #Platfrom 1
            [Rect(1000,400,122,118),0],[Rect(1104,395,122,118),1],[Rect(1226,395,122,118),1],[Rect(1348,395,122,118),1], #Platfrom 2
            [Rect(1470,402,122,118),2],[Rect(1470,500,122,118),5],[Rect(1470,598,122,118),5],[Rect(1470,696,122,118),5], #Platfrom 2
            [Rect(1223,497,122,118),4],[Rect(1223,621,122,118),4],[Rect(1223,746,122,118),4],[Rect(1004,495,122,118),3], #Platfrom 2
            [Rect(1004,590,122,118),3],[Rect(1004,685,122,118),3], #Platfrom 2
            [Rect(1900,313,122,118),1],[Rect(1898,413,122,118),4],[Rect(1898,538,122,118),4],[Rect(1898,663,122,118),4], #Platfrom 3
            [Rect(2398,221,122,118),0],[Rect(2502,216,122,118),1],[Rect(2624,222,122,118),2],[Rect(2402,316,122,118),3], #Platfrom 4
            [Rect(2402,443,122,118),3],[Rect(2402,570,122,118),3],[Rect(2402,697,122,118),3],[Rect(2624,320,122,118),5], #Platfrom 4
            [Rect(2624,418,122,118),5],[Rect(2624,516,122,118),5],[Rect(2624,616,122,118),5],[Rect(2624,714,122,118),5], #Platfrom 4
            [Rect(3201,596,122,118),1],[Rect(3322,596,122,118),1],[Rect(3444,596,122,118),1],[Rect(3198,694,122,118),4], #Platfrom 5
            [Rect(3441,694,122,118),4], #Platfrom 5
            [Rect(4901,701,122,118),0],[Rect(5005,696,122,118),1],[Rect(5109,696,122,118),1],[Rect(5213,696,122,118),1], #Platfrom 7
            [Rect(5337,703,122,118),2], #Paltfrom 7
            [Rect(6501,394,122,118),1],[Rect(6499,494,122,118),4],[Rect(6499,619,122,118),4],[Rect(6499,744,122,118),4], #Platfrom 9
            [Rect(6623,394,122,118),1],[Rect(6623,494,122,118),4],[Rect(6623,619,122,118),4],[Rect(6623,744,122,118),4], #Platfrom 9
            [Rect(7401,751,122,118),0],[Rect(7505,746,122,118),1],[Rect(7628,751,122,118),2], #Platfrom 11
            [Rect(8401,601,122,118),0],[Rect(8505,596,122,118),1],[Rect(8627,603,122,118),2],[Rect(8406,696,122,118),3], #Paltfrom 14
            [Rect(8502,694,122,118),4],[Rect(8627,699,122,118),5], #Platfrom 14
            [Rect(10501,596,122,118),1],[Rect(10498,694,122,118),4], #Platfrom 20
            [Rect(11501,496,122,118),1],[Rect(11626,496,122,118),1],[Rect(11499,594,122,118),4],[Rect(11624,594,122,118),4], #Platfrom 22
            [Rect(11499,719,122,118),4],[Rect(11624,719,122,118),4], #Platfrom 22
            [Rect(12001,296,122,118),1],[Rect(12123,296,122,118),1],[Rect(11999,394,122,118),4],[Rect(11999,519,122,118),4], #Paltfrom 23
            [Rect(11999,644,122,118),4],[Rect(11999,769,122,118),4],[Rect(12121,394,122,118),4],[Rect(12121,519,122,118),4], #Paltfrom 23
            [Rect(12121,643,122,118),4],[Rect(12121,768,122,118),4], #Platfrom 23
            [Rect(4201,601,122,118),7],[Rect(4328,601,122,118),7],[Rect(4328,700,122,118),10],[Rect(4201,700,122,118),10], #Platfrom 6
            [Rect(6100,600,122,118),7],[Rect(6227,600,122,118),7],[Rect(6100,699,122,118),10],[Rect(6227,699,122,118),10], #Platfrom 8
            [Rect(6800,301,122,118),12],[Rect(6905,300,122,118),13],[Rect(7033,300,122,118),13],[Rect(7159,300,122,118),14], #Platfrom 10
            [Rect(6809,400,122,118),15],[Rect(6809,527,122,118),15],[Rect(6809,654,122,118),15],[Rect(6809,781,122,118),15], #Platfrom 10
            [Rect(7159,400,122,118),17],[Rect(7159,530,122,118),17],[Rect(7159,660,122,118),17],[Rect(7159,790,122,118),17], #Platfrom 10
            [Rect(8200,600,122,118),13],[Rect(8200,698,122,118),16], #Platfrom 12
            [Rect(9001,601,122,118),7],[Rect(9128,601,122,118),7],[Rect(9001,700,122,118),10],[Rect(9128,700,122,118),10], #Platfrom 14
            [Rect(9500,300,122,118),13],[Rect(9500,398,122,118),16],[Rect(9500,525,122,118),16],[Rect(9500,652,122,118),16], #Platfrom 15
            [Rect(9500,679,122,118),16], #Platfrom 15
            [Rect(9701,401,122,118),7],[Rect(9828,401,122,118),7],[Rect(9828,500,122,118),10],[Rect(9828,599,122,118),10], #Platfrom 16
            [Rect(9828,698,122,118),10],[Rect(9701,500,122,118),10],[Rect(9701,599,122,118),10],[Rect(9701,698,122,118),10], #Platfrom 16
            [Rect(10150,200,122,118),13],[Rect(10150,298,122,118),16],[Rect(10150,396,122,118),16],[Rect(10150,494,122,118),16], #Platfrom 17
            [Rect(10150,592,122,118),16],[Rect(10150,690,122,118),16], #Platfrom 17
            [Rect(11001,601,122,118),7],[Rect(11001,699,122,118),10], #Platfrom 19
            [Rect(12400,300,122,118),13],[Rect(12528,300,122,118),13],[Rect(12400,398,122,118),16],[Rect(12400,525,122,118),16], #Platfrom 22
            [Rect(12400,652,122,118),16],[Rect(12400,779,122,118),16],[Rect(12528,398,122,118),16],[Rect(12528,525,122,118),16], #Platfrom 22
            [Rect(12528,652,122,118),16],[Rect(12528,779,122,118),16], #Platfrom 22
            [Rect(13000,750,122,118),18],[Rect(13105,750,122,118),19],[Rect(13231,750,122,118),20]] #Winning Platfrom
        
            restart_level_1=0
            action=('level_1')
            level_1('level_1')

        if restart_level_2==1 or next_stage==1:

                p=Rect(250,150,40,80)

                walls_2=[Rect(2900,440,263,500),Rect(6600,250,593,700),Rect(7700,450,130,700),Rect(7950,500,130,700),Rect(9400,250,130,600),
                         Rect(11300,250,130,600),Rect(11600,650,130,300),Rect(151,602,463,400),
                         Rect(901,602,133,200),Rect(1601,402,128,500),Rect(4001,301,458,500),
                         Rect(6001,351,468,500),Rect(8101,751,598,250),Rect(8801,571,130,300),
                         Rect(9101,351,130,500),Rect(10701,551,130,300),Rect(11101,351,130,500),
                         Rect(11801,751,298,300),Rect(2401,751,298,50),Rect(3301,751,398,500),
                         Rect(5401,751,398,50),Rect(7251,751,298,50),Rect(10101,601,260,300),
                         Rect(-500,770,15000,300),Rect(-2000,0,1500,1000)]

                bounce_plat_2=[Rect(2400,750,260,50),Rect(3300,750,380,100),Rect(5400,750,380,100),
                                   Rect(7250,750,260,100),Rect(10100,600,260,100)]

                platform_2=[Rect(150,600,465,20),Rect(900,600,137,20),Rect(1600,400,130,20),
                                Rect(4000,300,460,20),Rect(6000,350,470,20),Rect(8100,750,585,25),
                                Rect(8800,570,130,20),Rect(9100,350,130,20),Rect(10700,550,130,20),
                                Rect(11100,350,130,20),Rect(11800,750,300,20)]
                
                blocks_2=[[Rect(150,600,122,188),0],[Rect(254,595,122,188),1],[Rect(376,595,122,188),1],[Rect(500,600,122,188),2], #Platfrom 1
                  [Rect(155,695,122,188),3],[Rect(500,698,122,188),5], #Platfrom 1
                  [Rect(900,595,122,188),1],[Rect(897,695,122,188),4], #Platfrom 2
                  [Rect(1600,395,122,188),1],[Rect(1597,495,122,188),4],[Rect(1597,620,122,188),4],[Rect(1597,745,122,188),4], #Platfrom 3
                  [Rect(2400,750,122,188),7],[Rect(2527,750,122,188),7], #Platfrom 4
                  [Rect(2900,440,122,188),13],[Rect(3028,440,122,188),13],[Rect(3028,538,122,188),16],[Rect(3028,664,122,188),16], #Platfrom 5
                  [Rect(3028,790,122,188),16],[Rect(2900,538,122,188),16],[Rect(2900,664,122,188),16],[Rect(2900,790,122,188),16], #Platfrom 5
                  [Rect(3300,750,122,188),7],[Rect(3427,750,122,188),7],[Rect(3552,750,122,188),7], #Platfrom 6
                  [Rect(4000,300,122,188),0],[Rect(4104,295,122,188),1],[Rect(4226,295,122,188),1],[Rect(4350,300,122,188),2], #Platfrom 7
                  [Rect(4005,395,122,188),3],[Rect(4005,490,122,188),3],[Rect(4005,585,122,188),3],[Rect(4005,680,122,188),3], #Platfrom 7
                  [Rect(4350,395,122,188),5],[Rect(4350,490,122,188),5],[Rect(4350,585,122,188),5],[Rect(4350,680,122,188),5], #Platfrom 7
                  [Rect(5400,750,122,188),7],[Rect(5527,750,122,188),7],[Rect(5652,750,122,188),7], #Platfrom 8
                  [Rect(6000,350,122,188),0],[Rect(6104,345,122,188),1],[Rect(6226,345,122,188),1],[Rect(6350,350,122,188),2], #Platfrom 9
                  [Rect(6005,445,122,188),3],[Rect(6005,540,122,188),3],[Rect(6005,635,122,188),3],[Rect(6005,730,122,188),3], #Platfrom 9
                  [Rect(6350,445,122,188),5],[Rect(6350,540,122,188),5],[Rect(6350,635,122,188),5],[Rect(6350,730,122,188),5],
                  [Rect(6600,250,122,188),12],[Rect(6701,250,122,188),13],[Rect(6826,250,122,188),13],[Rect(6952,250,122,188),13], #Platfrom 10
                  [Rect(7078,250,122,188),14],[Rect(6609,349,122,188),15],[Rect(6609,478,122,188),15],[Rect(6609,589,122,188),15], #Platfrom 10
                  [Rect(6609,718,122,188),15],[Rect(7078,349,122,188),17],[Rect(7078,478,122,188),17],[Rect(7078,589,122,188),17], #Platfrom 10
                  [Rect(7078,718,122,188),17], #Platfrom 10
                  [Rect(7250,750,122,188),7],[Rect(7377,750,122,188),7], #Platfrom 11
                  [Rect(7700,450,122,188),13],[Rect(7700,549,122,188),16],[Rect(7700,678,122,188),16], #Platfrom 12
                  [Rect(7950,500,122,188),13],[Rect(7950,599,122,188),16],[Rect(7950,728,122,188),16], #Platfrom 13
                  [Rect(8100,750,122,188),0],[Rect(8204,745,122,188),1],[Rect(8326,745,122,188),1],[Rect(8448,745,122,188),1], #Platfrom 14
                  [Rect(8570,750,122,188),2], #Platfrom 14
                  [Rect(8801,566,122,188),1],[Rect(8799,666,122,188),4],[Rect(8799,781,122,188),4], #Platfrom 15
                  [Rect(9101,346,122,188),1],[Rect(9099,446,122,188),4],[Rect(9099,571,122,188),4],[Rect(9099,696,122,188),4], #Platfrom 16
                  [Rect(9400,250,122,188),13],[Rect(9400,349,122,188),16],[Rect(9400,474,122,188),16],[Rect(9400,599,122,188),16], #Platfrom 17
                  [Rect(9400,724,122,188),16], #Platfrom 17
                  [Rect(10100,600,122,188),7],[Rect(10227,600,122,188),7],[Rect(10227,699,122,188),10],[Rect(10100,699,122,188),10], #Platfrom 18
                  [Rect(10701,546,122,188),1],[Rect(10699,646,122,188),4],[Rect(10699,771,122,188),4], #Platfrom 19
                  [Rect(11101,346,122,188),1],[Rect(11099,446,122,188),4],[Rect(11099,571,122,188),4],[Rect(11099,696,122,188),4], #Platfrom 20
                  [Rect(11300,250,122,188),13],[Rect(11300,348,122,188),16],[Rect(11300,348,122,188),16],[Rect(11300,474,122,188),16], #Platfrom 21
                  [Rect(11300,600,122,188),16],[Rect(11300,726,122,188),16], #Platfrom 21
                  [Rect(11600,650,122,188),13],[Rect(11600,749,122,188),16], #Platfrom 22
                  [Rect(11800,750,122,188),19],[Rect(11928,750,122,188),19]] #Winning Platfrom
                
                restart_level_2=0
                next_stage=0
                action=='level_2'
                level_2('level_2')

        if mb[0]==1: #if the player left clicks on level 1, reset all the blocks and the player
            if level_1_rect.collidepoint(mx,my):
                p=Rect(250,150,40,80)
        
                platform=[Rect(0,500,698,20),Rect(1000,400,480,20),Rect(1900,320,130,20),
                              Rect(2400,220,327,20),Rect(3200,600,375,20),Rect(4900,700,554,20),
                              Rect(6500,400,257,20),Rect(7400,750,345,20),Rect(8400,600,340,20),
                              Rect(10500,600,135,20),Rect(11500,500,254,20),
                              Rect(12000,300,257,20),Rect(13000,750,350,200)]

                bounce_plat=[Rect(4200,600,255,20),Rect(6100,600,255,20),Rect(9000,600,260,20),
                                 Rect(9700,400,255,20),Rect(11000,600,125,20)]

                walls=[Rect(1,521,698,300),Rect(1001,401,578,400),
                           Rect(1901,321,128,500),Rect(2401,221,325,600),Rect(3201,601,373,400),
                           Rect(4201,601,253,400),Rect(4901,701,550,200),Rect(6101,601,253,400),
                           Rect(6501,401,255,500),Rect(6800,300,470,600),Rect(7401,751,343,200),
                           Rect(8200,600,125,300),Rect(8401,601,338,400),
                           Rect(9001,601,258,400),Rect(9500,300,130,500),Rect(9701,401,253,600),
                           Rect(10150,200,127,700),Rect(10501,601,133,400),
                           Rect(11001,601,123,400),Rect(11501,501,252,400),Rect(12001,301,255,600),
                           Rect(12400,300,260,600),Rect(13001,752,698,200),
                           Rect(-500,775,16000,100)]
                
                blocks=[[Rect(0,500,122,118),0],[Rect(104,495,122,118),1],[Rect(226,495,122,118),1],[Rect(348,495,122,118),1], #Platfrom 1
                [Rect(470,495,122,118),1],[Rect(592,502,122,118),2],[Rect(592,600,122,118),5],[Rect(592,698,122,118),5], #Platfrom 1
                [Rect(223,595,122,118),4],[Rect(223,720,122,118),4],[Rect(345,595,122,118),4],[Rect(345,720,122,118),4], #Platfrom 1
                [Rect(5,595,122,118),3],[Rect(5,717,122,118),3], #Platfrom 1
                [Rect(1000,400,122,118),0],[Rect(1104,395,122,118),1],[Rect(1226,395,122,118),1],[Rect(1348,395,122,118),1], #Platfrom 2
                [Rect(1470,402,122,118),2],[Rect(1470,500,122,118),5],[Rect(1470,598,122,118),5],[Rect(1470,696,122,118),5], #Platfrom 2
                [Rect(1223,497,122,118),4],[Rect(1223,621,122,118),4],[Rect(1223,746,122,118),4],[Rect(1004,495,122,118),3], #Platfrom 2
                [Rect(1004,590,122,118),3],[Rect(1004,685,122,118),3], #Platfrom 2
                [Rect(1900,313,122,118),1],[Rect(1898,413,122,118),4],[Rect(1898,538,122,118),4],[Rect(1898,663,122,118),4], #Platfrom 3
                [Rect(2398,221,122,118),0],[Rect(2502,216,122,118),1],[Rect(2624,222,122,118),2],[Rect(2402,316,122,118),3], #Platfrom 4
                [Rect(2402,443,122,118),3],[Rect(2402,570,122,118),3],[Rect(2402,697,122,118),3],[Rect(2624,320,122,118),5], #Platfrom 4
                [Rect(2624,418,122,118),5],[Rect(2624,516,122,118),5],[Rect(2624,616,122,118),5],[Rect(2624,714,122,118),5], #Platfrom 4
                [Rect(3201,596,122,118),1],[Rect(3322,596,122,118),1],[Rect(3444,596,122,118),1],[Rect(3198,694,122,118),4], #Platfrom 5
                [Rect(3441,694,122,118),4], #Platfrom 5
                [Rect(4901,701,122,118),0],[Rect(5005,696,122,118),1],[Rect(5109,696,122,118),1],[Rect(5213,696,122,118),1], #Platfrom 7
                [Rect(5337,703,122,118),2], #Paltfrom 7
                [Rect(6501,394,122,118),1],[Rect(6499,494,122,118),4],[Rect(6499,619,122,118),4],[Rect(6499,744,122,118),4], #Platfrom 9
                [Rect(6623,394,122,118),1],[Rect(6623,494,122,118),4],[Rect(6623,619,122,118),4],[Rect(6623,744,122,118),4], #Platfrom 9
                [Rect(7401,751,122,118),0],[Rect(7505,746,122,118),1],[Rect(7628,751,122,118),2], #Platfrom 11
                [Rect(8401,601,122,118),0],[Rect(8505,596,122,118),1],[Rect(8627,603,122,118),2],[Rect(8406,696,122,118),3], #Paltfrom 14
                [Rect(8502,694,122,118),4],[Rect(8627,699,122,118),5], #Platfrom 14
                [Rect(10501,596,122,118),1],[Rect(10498,694,122,118),4], #Platfrom 20
                [Rect(11501,496,122,118),1],[Rect(11626,496,122,118),1],[Rect(11499,594,122,118),4],[Rect(11624,594,122,118),4], #Platfrom 22
                [Rect(11499,719,122,118),4],[Rect(11624,719,122,118),4], #Platfrom 22
                [Rect(12001,296,122,118),1],[Rect(12123,296,122,118),1],[Rect(11999,394,122,118),4],[Rect(11999,519,122,118),4], #Paltfrom 23
                [Rect(11999,644,122,118),4],[Rect(11999,769,122,118),4],[Rect(12121,394,122,118),4],[Rect(12121,519,122,118),4], #Paltfrom 23
                [Rect(12121,643,122,118),4],[Rect(12121,768,122,118),4], #Platfrom 23
                [Rect(4201,601,122,118),7],[Rect(4328,601,122,118),7],[Rect(4328,700,122,118),10],[Rect(4201,700,122,118),10], #Platfrom 6
                [Rect(6100,600,122,118),7],[Rect(6227,600,122,118),7],[Rect(6100,699,122,118),10],[Rect(6227,699,122,118),10], #Platfrom 8
                [Rect(6800,301,122,118),12],[Rect(6905,300,122,118),13],[Rect(7033,300,122,118),13],[Rect(7159,300,122,118),14], #Platfrom 10
                [Rect(6809,400,122,118),15],[Rect(6809,527,122,118),15],[Rect(6809,654,122,118),15],[Rect(6809,781,122,118),15], #Platfrom 10
                [Rect(7159,400,122,118),17],[Rect(7159,530,122,118),17],[Rect(7159,660,122,118),17],[Rect(7159,790,122,118),17], #Platfrom 10
                [Rect(8200,600,122,118),13],[Rect(8200,698,122,118),16], #Platfrom 12
                [Rect(9001,601,122,118),7],[Rect(9128,601,122,118),7],[Rect(9001,700,122,118),10],[Rect(9128,700,122,118),10], #Platfrom 14
                [Rect(9500,300,122,118),13],[Rect(9500,398,122,118),16],[Rect(9500,525,122,118),16],[Rect(9500,652,122,118),16], #Platfrom 15
                [Rect(9500,679,122,118),16], #Platfrom 15
                [Rect(9701,401,122,118),7],[Rect(9828,401,122,118),7],[Rect(9828,500,122,118),10],[Rect(9828,599,122,118),10], #Platfrom 16
                [Rect(9828,698,122,118),10],[Rect(9701,500,122,118),10],[Rect(9701,599,122,118),10],[Rect(9701,698,122,118),10], #Platfrom 16
                [Rect(10150,200,122,118),13],[Rect(10150,298,122,118),16],[Rect(10150,396,122,118),16],[Rect(10150,494,122,118),16], #Platfrom 17
                [Rect(10150,592,122,118),16],[Rect(10150,690,122,118),16], #Platfrom 17
                [Rect(11001,601,122,118),7],[Rect(11001,699,122,118),10], #Platfrom 19
                [Rect(12400,300,122,118),13],[Rect(12528,300,122,118),13],[Rect(12400,398,122,118),16],[Rect(12400,525,122,118),16], #Platfrom 22
                [Rect(12400,652,122,118),16],[Rect(12400,779,122,118),16],[Rect(12528,398,122,118),16],[Rect(12528,525,122,118),16], #Platfrom 22
                [Rect(12528,652,122,118),16],[Rect(12528,779,122,118),16], #Platfrom 22
                [Rect(13000,750,122,118),18],[Rect(13105,750,122,118),19],[Rect(13231,750,122,118),20]] #Winning Platfrom

                
                level_1('level_1') #preforms level 1 
            
            if level_2_rect.collidepoint(mx,my): #if the player left clicks on level 2, reset all the blocks and the player
                p=Rect(250,150,40,80)

                walls_2=[Rect(2900,440,263,500),Rect(6600,250,593,700),Rect(7700,450,130,700),Rect(7950,500,130,700),Rect(9400,250,130,600),
                         Rect(11300,250,130,600),Rect(11600,650,130,300),Rect(151,602,463,400),
                         Rect(901,602,133,200),Rect(1601,402,128,500),Rect(4001,301,458,500),
                         Rect(6001,351,468,500),Rect(8101,751,598,250),Rect(8801,571,130,300),
                         Rect(9101,351,130,500),Rect(10701,551,130,300),Rect(11101,351,130,500),
                         Rect(11801,751,298,300),Rect(2401,751,298,50),Rect(3301,751,398,500),
                         Rect(5401,751,398,50),Rect(7251,751,298,50),Rect(10101,601,260,300),
                         Rect(-500,770,15000,300),Rect(-2000,0,1500,1000)]

                bounce_plat_2=[Rect(2400,750,260,50),Rect(3300,750,380,100),Rect(5400,750,380,100),
                                   Rect(7250,750,260,100),Rect(10100,600,260,100)]

                platform_2=[Rect(150,600,465,20),Rect(900,600,137,20),Rect(1600,400,130,20),
                                Rect(4000,300,460,20),Rect(6000,350,470,20),Rect(8100,750,585,25),
                                Rect(8800,570,130,20),Rect(9100,350,130,20),Rect(10700,550,130,20),
                                Rect(11100,350,130,20),Rect(11800,750,300,20)]
                
                blocks_2=[[Rect(150,600,122,188),0],[Rect(254,595,122,188),1],[Rect(376,595,122,188),1],[Rect(500,600,122,188),2], #Platfrom 1
                  [Rect(155,695,122,188),3],[Rect(500,698,122,188),5], #Platfrom 1
                  [Rect(900,595,122,188),1],[Rect(897,695,122,188),4], #Platfrom 2
                  [Rect(1600,395,122,188),1],[Rect(1597,495,122,188),4],[Rect(1597,620,122,188),4],[Rect(1597,745,122,188),4], #Platfrom 3
                  [Rect(2400,750,122,188),7],[Rect(2527,750,122,188),7], #Platfrom 4
                  [Rect(2900,440,122,188),13],[Rect(3028,440,122,188),13],[Rect(3028,538,122,188),16],[Rect(3028,664,122,188),16], #Platfrom 5
                  [Rect(3028,790,122,188),16],[Rect(2900,538,122,188),16],[Rect(2900,664,122,188),16],[Rect(2900,790,122,188),16], #Platfrom 5
                  [Rect(3300,750,122,188),7],[Rect(3427,750,122,188),7],[Rect(3552,750,122,188),7], #Platfrom 6
                  [Rect(4000,300,122,188),0],[Rect(4104,295,122,188),1],[Rect(4226,295,122,188),1],[Rect(4350,300,122,188),2], #Platfrom 7
                  [Rect(4005,395,122,188),3],[Rect(4005,490,122,188),3],[Rect(4005,585,122,188),3],[Rect(4005,680,122,188),3], #Platfrom 7
                  [Rect(4350,395,122,188),5],[Rect(4350,490,122,188),5],[Rect(4350,585,122,188),5],[Rect(4350,680,122,188),5], #Platfrom 7
                  [Rect(5400,750,122,188),7],[Rect(5527,750,122,188),7],[Rect(5652,750,122,188),7], #Platfrom 8
                  [Rect(6000,350,122,188),0],[Rect(6104,345,122,188),1],[Rect(6226,345,122,188),1],[Rect(6350,350,122,188),2], #Platfrom 9
                  [Rect(6005,445,122,188),3],[Rect(6005,540,122,188),3],[Rect(6005,635,122,188),3],[Rect(6005,730,122,188),3], #Platfrom 9
                  [Rect(6350,445,122,188),5],[Rect(6350,540,122,188),5],[Rect(6350,635,122,188),5],[Rect(6350,730,122,188),5],
                  [Rect(6600,250,122,188),12],[Rect(6701,250,122,188),13],[Rect(6826,250,122,188),13],[Rect(6952,250,122,188),13], #Platfrom 10
                  [Rect(7078,250,122,188),14],[Rect(6609,349,122,188),15],[Rect(6609,478,122,188),15],[Rect(6609,589,122,188),15], #Platfrom 10
                  [Rect(6609,718,122,188),15],[Rect(7078,349,122,188),17],[Rect(7078,478,122,188),17],[Rect(7078,589,122,188),17], #Platfrom 10
                  [Rect(7078,718,122,188),17], #Platfrom 10
                  [Rect(7250,750,122,188),7],[Rect(7377,750,122,188),7], #Platfrom 11
                  [Rect(7700,450,122,188),13],[Rect(7700,549,122,188),16],[Rect(7700,678,122,188),16], #Platfrom 12
                  [Rect(7950,500,122,188),13],[Rect(7950,599,122,188),16],[Rect(7950,728,122,188),16], #Platfrom 13
                  [Rect(8100,750,122,188),0],[Rect(8204,745,122,188),1],[Rect(8326,745,122,188),1],[Rect(8448,745,122,188),1], #Platfrom 14
                  [Rect(8570,750,122,188),2], #Platfrom 14
                  [Rect(8801,566,122,188),1],[Rect(8799,666,122,188),4],[Rect(8799,781,122,188),4], #Platfrom 15
                  [Rect(9101,346,122,188),1],[Rect(9099,446,122,188),4],[Rect(9099,571,122,188),4],[Rect(9099,696,122,188),4], #Platfrom 16
                  [Rect(9400,250,122,188),13],[Rect(9400,349,122,188),16],[Rect(9400,474,122,188),16],[Rect(9400,599,122,188),16], #Platfrom 17
                  [Rect(9400,724,122,188),16], #Platfrom 17
                  [Rect(10100,600,122,188),7],[Rect(10227,600,122,188),7],[Rect(10227,699,122,188),10],[Rect(10100,699,122,188),10], #Platfrom 18
                  [Rect(10701,546,122,188),1],[Rect(10699,646,122,188),4],[Rect(10699,771,122,188),4], #Platfrom 19
                  [Rect(11101,346,122,188),1],[Rect(11099,446,122,188),4],[Rect(11099,571,122,188),4],[Rect(11099,696,122,188),4], #Platfrom 20
                  [Rect(11300,250,122,188),13],[Rect(11300,348,122,188),16],[Rect(11300,348,122,188),16],[Rect(11300,474,122,188),16], #Platfrom 21
                  [Rect(11300,600,122,188),16],[Rect(11300,726,122,188),16], #Platfrom 21
                  [Rect(11600,650,122,188),13],[Rect(11600,749,122,188),16], #Platfrom 22
                  [Rect(11800,750,122,188),19],[Rect(11928,750,122,188),19]] #Winning Platfrom
                
                level_2('level_2') # preforms level 2

            if instructions_rect.collidepoint(mx,my):
                instructions('instructions') #if the player clicks on the instruction button the instruction function is preformed
            if quit_rect.collidepoint(mx,my):
                quit_action('quit') #quits program
            
        display.flip()
        myClock.tick(60)

def draw_scene_lev1(screen,player,wall): #draws level 1
    'drawing the player and the platform for level 1'

    global idle_frame
    global run_frame
    global jump_frame
    global dash_frame
    global bw_idle_frame
    global bw_run_frame
    global bw_jump_frame
    global bw_dash_frame
    global side_chose
    #variables used later on

    death_text=Stgotic_font_3.render(str(death),True,(255,255,255)) #death count text
    death_text_2=Stgotic_font_4.render(str(death),True,(80,60,5))
    
    draw.rect(screen,RED,p,1) #draws player
    keys=key.get_pressed()

        
    for a in range(len(walls)): #draws obstacles 
        draw.rect(screen,BLUE,walls[a])
    for a in range(len(platform)): #draws platforms
        draw.rect(screen,WHITE,platform[a])
    for a in range(len(bounce_plat)): #draws bounce_plat
        draw.rect(screen,GREEN,bounce_plat[a])
    for a in range(5): #draws background
        screen.blit(background[a],(background_cord[a],-100))
    for a in range(5):
        screen.blit(background[a],(background_cord[a+5],-100))
    for a in range(len(pilar_cord)):
        screen.blit(pilar,(pilar_cord[a],0))
    for a in range(len(blocks)):
        if blocks[a][1]==0:
            screen.blit(Block0,(blocks[a][0]))
        elif blocks[a][1]==1:
            screen.blit(Block1,(blocks[a][0]))
        elif blocks[a][1]==2:
            screen.blit(Block2,(blocks[a][0]))
        elif blocks[a][1]==3:
            screen.blit(Block3,(blocks[a][0]))
        elif blocks[a][1]==4:
            screen.blit(Block4,(blocks[a][0]))
        elif blocks[a][1]==5:
            screen.blit(Block5,(blocks[a][0]))
        elif blocks[a][1]==6:
            screen.blit(G_Block0,(blocks[a][0]))
        elif blocks[a][1]==7:
            screen.blit(G_Block1,(blocks[a][0]))
        elif blocks[a][1]==8:
            screen.blit(G_Block2,(blocks[a][0]))
        elif blocks[a][1]==9:
            screen.blit(G_Block3,(blocks[a][0]))
        elif blocks[a][1]==10:
            screen.blit(G_Block4,(blocks[a][0]))
        elif blocks[a][1]==11:
            screen.blit(G_Block5,(blocks[a][0]))
        elif blocks[a][1]==12:
            screen.blit(R_Block0,(blocks[a][0]))
        elif blocks[a][1]==13:
            screen.blit(R_Block1,(blocks[a][0]))
        elif blocks[a][1]==14:
            screen.blit(R_Block2,(blocks[a][0]))
        elif blocks[a][1]==15:
            screen.blit(R_Block3,(blocks[a][0]))
        elif blocks[a][1]==16:
            screen.blit(R_Block4,(blocks[a][0]))
        elif blocks[a][1]==17:
            screen.blit(R_Block5,(blocks[a][0]))
        elif blocks[a][1]==18:
            screen.blit(Go_Block0,(blocks[a][0]))
        elif blocks[a][1]==19:
            screen.blit(Go_Block1,(blocks[a][0]))
        elif blocks[a][1]==20:
            screen.blit(Go_Block2,(blocks[a][0]))
    
    if keys[K_RIGHT]:
        side_chose=1
    elif keys[K_LEFT]:
        side_chose=0

    #player animation to indicate when to use ceratin frames and how long
    if keys[K_RIGHT]==0 and keys [K_LEFT]==0 and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0 and side_chose==1:
        screen.blit(idle_pics[int(idle_frame)],(p[X],p[Y]))
        idle_frame+=0.08
        if idle_frame>4:
            idle_frame=0 #resets frame to 0
    
    elif keys[K_RIGHT]==0 and keys [K_LEFT]==0 and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0 and side_chose==0:
        screen.blit(bw_idle_pics[int(bw_idle_frame)],(p[X],p[Y]))
        bw_idle_frame+=0.08
        if bw_idle_frame>4:
            bw_idle_frame=0 #resets frame to 0
    
    if keys[K_RIGHT] and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0:
        screen.blit(run_pics[int(run_frame)],(p[X],p[Y]))
        run_frame+=0.15
        if run_frame>6:
            run_frame=0 #resets frame to 0

    elif keys[K_LEFT] and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0:
        screen.blit(bw_run_pics[int(bw_run_frame)],(p[X],p[Y]))
        bw_run_frame+=0.15
        if bw_run_frame>6:
            bw_run_frame=0 #resets frame to 0
    
    if keys[K_SPACE] or keys[K_UP] and side_chose==1:
        screen.blit(jump_pics[int(jump_frame)],(p[X],p[Y]))
        jump_frame+=0.1
        if jump_frame>7:
            jump_frame=0 #resets frame to 0
    
    elif keys[K_SPACE] or keys[K_UP] and side_chose==0:
        screen.blit(bw_jump_pics[int(bw_jump_frame)],(p[X],p[Y]))
        bw_jump_frame+=0.1
        if bw_jump_frame>7:
            bw_jump_frame=0 #resets frame to 0
    
    if keys[K_DOWN] and keys[K_SPACE]==0 and keys[K_UP]==0 and side_chose==1:
        screen.blit(dash_pics[int(dash_frame)],(p[X],p[Y]))
        dash_frame+=0.1
        if dash_frame>1:
            dash_frame=0 #resets frame to 0

    elif keys[K_DOWN] and keys[K_SPACE]==0 and keys[K_UP]==0 and side_chose==0:
        screen.blit(bw_dash_pics[int(bw_dash_frame)],(p[X],p[Y]))
        bw_dash_frame+=0.1
        if bw_dash_frame>1:
            bw_dash_frame=0

    #shows the help boxes 
    if help_box==1:
        screen.blit(scroll,(-50,-80))
        screen.blit(help_text_1,(180,55))
    if help_box==2:
        screen.blit(scroll,(-50,-80))
        screen.blit(help_text_2,(160,55))
    if help_box==3:
        screen.blit(scroll,(-50,-80))
        screen.blit(help_text_3,(110,35))
        screen.blit(help_text_4,(110,70))
    if help_box==4:
        screen.blit(scroll,(-50,-80))
        screen.blit(help_text_5,(100,35))
        screen.blit(help_text_6,(100,70))

    #prints the text and images related to the death counter
    screen.blit(death_box,(950,10))
    screen.blit(death_text_2,(1102,50))
    screen.blit(death_text,(1100,45))
    screen.blit(death_pic,(1000,30))
            
    display.flip()

def move_lev1(player): #moves player for level 1
    'moving the player for level 1'
    global background_cord
    global pilar_cord
    
    keys=key.get_pressed()
    if keys[K_SPACE] or keys[K_UP]:
        if p[Y]+p[H]==v[BOT] and v[Y]==0:    
            v[Y]=jumpSpeed #if player is on platform, the player is allowed to jump
            
    if keys[K_LEFT]: #move left
        v[X]=15
    elif keys[K_RIGHT]: #move right
        v[X]=-15
    else:
        v[X]=0
        
    # move player, but really just moves the background
    for a in range(len(platform)):
        platform[a][X]+=v[X] #moving left/right
    for a in range(len(bounce_plat)):
        bounce_plat[a][X]+=v[X]
    for a in range(len(walls)):
        walls[a][X]+=v[X]
    for a in range(len(background_cord)):
        background_cord[a]+=v[X]
    for a in range(len(pilar_cord)):
        pilar_cord[a]+=v[X]
    for i in range(len(blocks)):
        blocks[i][0].left+=v[X]
         
    v[Y]+=gravity #acceleration

def check_lev1(player,wall):
    'check if the player lands on a platform or bounce pads for level 1'
    for a in range(len(platform)): 
        if p[X]+p[W]>platform[a][X] and p[X]<platform[a][X]+platform[a][W] and p[Y]+p[H]<=platform[a][Y] and p[Y]+p[H]+v[Y]>platform[a][Y]:
            v[BOT]=platform[a][Y]
            p[Y]=v[BOT]-p[H]
            v[Y]=0
   
    for a in range(len(bounce_plat)):
        if p[X]+p[W]>bounce_plat[a][X] and p[X]<bounce_plat[a][X]+bounce_plat[a][W] and p[Y]+p[H]<=bounce_plat[a][Y] and p[Y]+p[H]+v[Y]>bounce_plat[a][Y]:
            v[Y]=1.25*jumpSpeed #if it in on bounce pad the player is imediatly forced up
            
    p[Y]+=v[Y]#falling down

def dash_lev1(player):
    'if player is allowed to dash or not'
    global p
    global platform
    global walls
    global bounce_plat
    global death
    global dash_count
    global level
    global restart
    global timer 
    global help_box
    global background_cord
    global pilar_cord
    global dash_count
    global blocks

    keys=key.get_pressed()
    
    if keys[K_UP] or keys[K_SPACE]: #if the player jumps then the dash is reset, the player has to jump to activate it or else the player can abuse this ability
        dash_count=1
        timer=0
  
    if keys[K_DOWN]: 
        if dash_count==1: #the actually dashing, by moving everything
            timer+=1
            if keys[K_LEFT]: #if the player is going left
                for a in range(len(platform)):
                    if timer%2==0:
                        platform[a][X]+=80
                for a in range(len(bounce_plat)):
                    if timer%2==0:
                        bounce_plat[a][X]+=80
                for a in range(len(walls)):
                    if timer%2==0:
                        walls[a][X]+=80
                for a in range(len(background_cord)):
                    if timer%2==0:
                        background_cord[a]+=80
                for a in range(len(pilar_cord)):
                    if timer%2==0:
                        pilar_cord[a]+=80
                for a in range(len(blocks)):
                    if timer%2==0:
                        blocks[a][0].left+=80
                    
                if timer>10: #once timer is greater than 20 dash_count is reset
                    dash_count=0
                    
            elif keys[K_RIGHT]: #else the dash will go to the right
                for a in range(len(platform)):
                    if timer%2==0:
                        platform[a][X]-=80
                for a in range(len(bounce_plat)):
                    if timer%2==0:
                        bounce_plat[a][X]-=80
                for a in range(len(walls)):
                    if timer%2==0:
                        walls[a][X]-=80
                for a in range(len(background_cord)):
                    if timer%2==0:
                        background_cord[a]-=80
                for a in range(len(pilar_cord)):
                    if timer%2==0:
                        pilar_cord[a]-=80
                for a in range(len(blocks)):
                    if timer%2==0:
                        blocks[a][0].left-=80
                            
                if timer>10: #once timer is greater than 20 dash_count is reset
                    dash_count=0

def death_lev1(player): # death for level 1
    'death function for level 1'
    global p
    global platform
    global walls
    global bounce_plat
    global death
    global dash_count
    global level
    global restart
    global timer 
    global help_box
    global background_cord
    global pilar_cord
    global dash_count
    global blocks
    
    for a in range(len(walls)): # if the player it's the walls then the level is reset
        if p.colliderect(walls[a]):
            p=Rect(250,200,40,80)

            platform=[Rect(0,500,698,20),Rect(1000,400,480,20),Rect(1900,320,130,20),
                              Rect(2400,220,327,20),Rect(3200,600,375,20),Rect(4900,700,554,20),
                              Rect(6500,400,257,20),Rect(7400,750,345,20),Rect(8400,600,340,20),
                              Rect(10500,600,135,20),Rect(11500,500,254,20),
                              Rect(12000,300,257,20),Rect(13000,750,350,200)]

            bounce_plat=[Rect(4200,600,255,20),Rect(6100,600,255,20),Rect(9000,600,260,20),
                                 Rect(9700,400,255,20),Rect(11000,600,125,20)]

            walls=[Rect(1,521,698,300),Rect(1001,401,578,400),
                           Rect(1901,321,128,500),Rect(2401,221,325,600),Rect(3201,601,373,400),
                           Rect(4201,601,253,400),Rect(4901,701,550,200),Rect(6101,601,253,400),
                           Rect(6501,401,255,500),Rect(6800,300,470,600),Rect(7401,751,343,200),
                           Rect(8200,600,125,300),Rect(8401,601,338,400),
                           Rect(9001,601,258,400),Rect(9500,300,130,500),Rect(9701,401,253,600),
                           Rect(10150,200,127,700),Rect(10501,601,133,400),
                           Rect(11001,601,123,400),Rect(11501,501,252,400),Rect(12001,301,255,600),
                           Rect(12400,300,260,600),Rect(13001,752,698,200),
                           Rect(-500,775,16000,100)]
            
            background_cord=[-500,2500,3900,6400,7625,9500,12500,13900,16400,17650]
            pilar_cord=[2400,3780,6265,7525,9400,12400,16300,17550]
            death+=1
                
            blocks=[[Rect(0,500,122,118),0],[Rect(104,495,122,118),1],[Rect(226,495,122,118),1],[Rect(348,495,122,118),1], #Platfrom 1
            [Rect(470,495,122,118),1],[Rect(592,502,122,118),2],[Rect(592,600,122,118),5],[Rect(592,698,122,118),5], #Platfrom 1
            [Rect(223,595,122,118),4],[Rect(223,720,122,118),4],[Rect(345,595,122,118),4],[Rect(345,720,122,118),4], #Platfrom 1
            [Rect(5,595,122,118),3],[Rect(5,717,122,118),3], #Platfrom 1
            [Rect(1000,400,122,118),0],[Rect(1104,395,122,118),1],[Rect(1226,395,122,118),1],[Rect(1348,395,122,118),1], #Platfrom 2
            [Rect(1470,402,122,118),2],[Rect(1470,500,122,118),5],[Rect(1470,598,122,118),5],[Rect(1470,696,122,118),5], #Platfrom 2
            [Rect(1223,497,122,118),4],[Rect(1223,621,122,118),4],[Rect(1223,746,122,118),4],[Rect(1004,495,122,118),3], #Platfrom 2
            [Rect(1004,590,122,118),3],[Rect(1004,685,122,118),3], #Platfrom 2
            [Rect(1900,313,122,118),1],[Rect(1898,413,122,118),4],[Rect(1898,538,122,118),4],[Rect(1898,663,122,118),4], #Platfrom 3
            [Rect(2398,221,122,118),0],[Rect(2502,216,122,118),1],[Rect(2624,222,122,118),2],[Rect(2402,316,122,118),3], #Platfrom 4
            [Rect(2402,443,122,118),3],[Rect(2402,570,122,118),3],[Rect(2402,697,122,118),3],[Rect(2624,320,122,118),5], #Platfrom 4
            [Rect(2624,418,122,118),5],[Rect(2624,516,122,118),5],[Rect(2624,616,122,118),5],[Rect(2624,714,122,118),5], #Platfrom 4
            [Rect(3201,596,122,118),1],[Rect(3322,596,122,118),1],[Rect(3444,596,122,118),1],[Rect(3198,694,122,118),4], #Platfrom 5
            [Rect(3441,694,122,118),4], #Platfrom 5
            [Rect(4901,701,122,118),0],[Rect(5005,696,122,118),1],[Rect(5109,696,122,118),1],[Rect(5213,696,122,118),1], #Platfrom 7
            [Rect(5337,703,122,118),2], #Paltfrom 7
            [Rect(6501,394,122,118),1],[Rect(6499,494,122,118),4],[Rect(6499,619,122,118),4],[Rect(6499,744,122,118),4], #Platfrom 9
            [Rect(6623,394,122,118),1],[Rect(6623,494,122,118),4],[Rect(6623,619,122,118),4],[Rect(6623,744,122,118),4], #Platfrom 9
            [Rect(7401,751,122,118),0],[Rect(7505,746,122,118),1],[Rect(7628,751,122,118),2], #Platfrom 11
            [Rect(8401,601,122,118),0],[Rect(8505,596,122,118),1],[Rect(8627,603,122,118),2],[Rect(8406,696,122,118),3], #Paltfrom 14
            [Rect(8502,694,122,118),4],[Rect(8627,699,122,118),5], #Platfrom 14
            [Rect(10501,596,122,118),1],[Rect(10498,694,122,118),4], #Platfrom 20
            [Rect(11501,496,122,118),1],[Rect(11626,496,122,118),1],[Rect(11499,594,122,118),4],[Rect(11624,594,122,118),4], #Platfrom 22
            [Rect(11499,719,122,118),4],[Rect(11624,719,122,118),4], #Platfrom 22
            [Rect(12001,296,122,118),1],[Rect(12123,296,122,118),1],[Rect(11999,394,122,118),4],[Rect(11999,519,122,118),4], #Paltfrom 23
            [Rect(11999,644,122,118),4],[Rect(11999,769,122,118),4],[Rect(12121,394,122,118),4],[Rect(12121,519,122,118),4], #Paltfrom 23
            [Rect(12121,643,122,118),4],[Rect(12121,768,122,118),4], #Platfrom 23
            [Rect(4201,601,122,118),7],[Rect(4328,601,122,118),7],[Rect(4328,700,122,118),10],[Rect(4201,700,122,118),10], #Platfrom 6
            [Rect(6100,600,122,118),7],[Rect(6227,600,122,118),7],[Rect(6100,699,122,118),10],[Rect(6227,699,122,118),10], #Platfrom 8
            [Rect(6800,301,122,118),12],[Rect(6905,300,122,118),13],[Rect(7033,300,122,118),13],[Rect(7159,300,122,118),14], #Platfrom 10
            [Rect(6809,400,122,118),15],[Rect(6809,527,122,118),15],[Rect(6809,654,122,118),15],[Rect(6809,781,122,118),15], #Platfrom 10
            [Rect(7159,400,122,118),17],[Rect(7159,530,122,118),17],[Rect(7159,660,122,118),17],[Rect(7159,790,122,118),17], #Platfrom 10
            [Rect(8200,600,122,118),13],[Rect(8200,698,122,118),16], #Platfrom 12
            [Rect(9001,601,122,118),7],[Rect(9128,601,122,118),7],[Rect(9001,700,122,118),10],[Rect(9128,700,122,118),10], #Platfrom 14
            [Rect(9500,300,122,118),13],[Rect(9500,398,122,118),16],[Rect(9500,525,122,118),16],[Rect(9500,652,122,118),16], #Platfrom 15
            [Rect(9500,679,122,118),16], #Platfrom 15
            [Rect(9701,401,122,118),7],[Rect(9828,401,122,118),7],[Rect(9828,500,122,118),10],[Rect(9828,599,122,118),10], #Platfrom 16
            [Rect(9828,698,122,118),10],[Rect(9701,500,122,118),10],[Rect(9701,599,122,118),10],[Rect(9701,698,122,118),10], #Platfrom 16
            [Rect(10150,200,122,118),13],[Rect(10150,298,122,118),16],[Rect(10150,396,122,118),16],[Rect(10150,494,122,118),16], #Platfrom 17
            [Rect(10150,592,122,118),16],[Rect(10150,690,122,118),16], #Platfrom 17
            [Rect(11001,601,122,118),7],[Rect(11001,699,122,118),10], #Platfrom 19
            [Rect(12400,300,122,118),13],[Rect(12528,300,122,118),13],[Rect(12400,398,122,118),16],[Rect(12400,525,122,118),16], #Platfrom 22
            [Rect(12400,652,122,118),16],[Rect(12400,779,122,118),16],[Rect(12528,398,122,118),16],[Rect(12528,525,122,118),16], #Platfrom 22
            [Rect(12528,652,122,118),16],[Rect(12528,779,122,118),16], #Platfrom 22
            [Rect(13000,750,122,118),18],[Rect(13105,750,122,118),19],[Rect(13231,750,122,118),20]] #Winning Platfrom



def level_1(action): #level 1
    'preform all actions for level 1'
    global p
    global platform
    global walls
    global bounce_plat
    global death
    global dash_count
    global level
    global restart
    global timer 
    global help_box
    global background_cord
    global pilar_cord
    global blocks

    level=1
    
    while action=='level_1':
        for evnt in event.get():            
            if evnt.type == QUIT:
                action=='menu'
                return "menu" #if the player exits, they'll go back to menu
            
        keys=key.get_pressed()

        #preform the fuctions of level 1
        move_lev1(p)
        draw_scene_lev1(screen,p,platform)
        check_lev1(p,platform)
        dash_lev1(p)
        death_lev1(p)

        #indicates when to show help boxes
        if Rect(p[X],p[Y]+1,p[W],p[H]).colliderect(platform[0]):
            help_box=1
        elif Rect(p[X],p[Y]+1,p[W],p[H]).colliderect(platform[4]):
            help_box=2
        elif Rect(p[X],p[Y]+1,p[W],p[H]).colliderect(platform[5]):
            help_box=3
        elif Rect(p[X],p[Y]+1,p[W],p[H]).colliderect(platform[8]):
            help_box=4
        else:
            help_box=0

        #if the player has reached the final block go to the level complete screen
        if p[X]+p[W]>platform[12][X] and p[X]<platform[12][X]+platform[12][W] and p[Y]+p[H]<=platform[12][Y] and p[Y]+p[H]+v[Y]>platform[12][Y]:
            action='level_complete'
            level_complete('level_complete')


        if keys[K_UP] or keys[K_SPACE]:
            dash_count=1
            timer=0
            
        if keys[K_DOWN]:
            if dash_count==1:
                timer+=1
                if keys[K_LEFT]:
                    for a in range(len(platform)):
                        if timer%2==0:
                            platform[a][X]+=80
                    for a in range(len(bounce_plat)):
                        if timer%2==0:
                            bounce_plat[a][X]+=80
                    for a in range(len(walls)):
                        if timer%2==0:
                            walls[a][X]+=80
                    for a in range(len(background_cord)):
                        if timer%2==0:
                            background_cord[a]+=80
                    for a in range(len(pilar_cord)):
                        if timer%2==0:
                            pilar_cord[a]+=80
                    for a in range(len(blocks)):
                        if timer%2==0:
                            blocks[a][0].left+=80
                    
                    if timer>20:
                        dash_count=0
                else:
                    for a in range(len(platform)):
                        if timer%2==0:
                            platform[a][X]-=80
                    for a in range(len(bounce_plat)):
                        if timer%2==0:
                            bounce_plat[a][X]-=80
                    for a in range(len(walls)):
                        if timer%2==0:
                            walls[a][X]-=80
                    for a in range(len(background_cord)):
                        if timer%2==0:
                            background_cord[a]-=80
                    for a in range(len(pilar_cord)):
                        if timer%2==0:
                            pilar_cord[a]-=80
                    for a in range(len(blocks)):
                        if timer%2==0:
                            blocks[a][0].left-=80
                            
                    if timer>10:
                        dash_count=0

        for a in range(len(walls)):
            if p.colliderect(walls[a]):
                p=Rect(250,200,40,80)

                platform=[Rect(0,500,698,20),Rect(1000,400,480,20),Rect(1900,320,130,20),
                              Rect(2400,220,327,20),Rect(3200,600,375,20),Rect(4900,700,554,20),
                              Rect(6500,400,257,20),Rect(7400,750,345,20),Rect(8400,600,340,20),
                              Rect(10500,600,135,20),Rect(11500,500,254,20),
                              Rect(12000,300,257,20),Rect(13000,750,350,200)]

                bounce_plat=[Rect(4200,600,255,20),Rect(6100,600,255,20),Rect(9000,600,260,20),
                                 Rect(9700,400,255,20),Rect(11000,600,125,20)]

                walls=[Rect(1,521,698,300),Rect(1001,401,578,400),
                           Rect(1901,321,128,500),Rect(2401,221,325,600),Rect(3201,601,373,400),
                           Rect(4201,601,253,400),Rect(4901,701,550,200),Rect(6101,601,253,400),
                           Rect(6501,401,255,500),Rect(6800,300,470,600),Rect(7401,751,343,200),
                           Rect(8200,600,125,300),Rect(8401,601,338,400),
                           Rect(9001,601,258,400),Rect(9500,300,130,500),Rect(9701,401,253,600),
                           Rect(10150,200,127,700),Rect(10501,601,133,400),
                           Rect(11001,601,123,400),Rect(11501,501,252,400),Rect(12001,301,255,600),
                           Rect(12400,300,260,600),Rect(13001,752,698,200),
                           Rect(-500,775,16000,100)]
                
                blocks=[[Rect(0,500,122,118),0],[Rect(104,495,122,118),1],[Rect(226,495,122,118),1],[Rect(348,495,122,118),1], #Platfrom 1
                [Rect(470,495,122,118),1],[Rect(592,502,122,118),2],[Rect(592,600,122,118),5],[Rect(592,698,122,118),5], #Platfrom 1
                [Rect(223,595,122,118),4],[Rect(223,720,122,118),4],[Rect(345,595,122,118),4],[Rect(345,720,122,118),4], #Platfrom 1
                [Rect(5,595,122,118),3],[Rect(5,717,122,118),3], #Platfrom 1
                [Rect(1000,400,122,118),0],[Rect(1104,395,122,118),1],[Rect(1226,395,122,118),1],[Rect(1348,395,122,118),1], #Platfrom 2
                [Rect(1470,402,122,118),2],[Rect(1470,500,122,118),5],[Rect(1470,598,122,118),5],[Rect(1470,696,122,118),5], #Platfrom 2
                [Rect(1223,497,122,118),4],[Rect(1223,621,122,118),4],[Rect(1223,746,122,118),4],[Rect(1004,495,122,118),3], #Platfrom 2
                [Rect(1004,590,122,118),3],[Rect(1004,685,122,118),3], #Platfrom 2
                [Rect(1900,313,122,118),1],[Rect(1898,413,122,118),4],[Rect(1898,538,122,118),4],[Rect(1898,663,122,118),4], #Platfrom 3
                [Rect(2398,221,122,118),0],[Rect(2502,216,122,118),1],[Rect(2624,222,122,118),2],[Rect(2402,316,122,118),3], #Platfrom 4
                [Rect(2402,443,122,118),3],[Rect(2402,570,122,118),3],[Rect(2402,697,122,118),3],[Rect(2624,320,122,118),5], #Platfrom 4
                [Rect(2624,418,122,118),5],[Rect(2624,516,122,118),5],[Rect(2624,616,122,118),5],[Rect(2624,714,122,118),5], #Platfrom 4
                [Rect(3201,596,122,118),1],[Rect(3322,596,122,118),1],[Rect(3444,596,122,118),1],[Rect(3198,694,122,118),4], #Platfrom 5
                [Rect(3441,694,122,118),4], #Platfrom 5
                [Rect(4901,701,122,118),0],[Rect(5005,696,122,118),1],[Rect(5109,696,122,118),1],[Rect(5213,696,122,118),1], #Platfrom 7
                [Rect(5337,703,122,118),2], #Paltfrom 7
                [Rect(6501,394,122,118),1],[Rect(6499,494,122,118),4],[Rect(6499,619,122,118),4],[Rect(6499,744,122,118),4], #Platfrom 9
                [Rect(6623,394,122,118),1],[Rect(6623,494,122,118),4],[Rect(6623,619,122,118),4],[Rect(6623,744,122,118),4], #Platfrom 9
                [Rect(7401,751,122,118),0],[Rect(7505,746,122,118),1],[Rect(7628,751,122,118),2], #Platfrom 11
                [Rect(8401,601,122,118),0],[Rect(8505,596,122,118),1],[Rect(8627,603,122,118),2],[Rect(8406,696,122,118),3], #Paltfrom 14
                [Rect(8502,694,122,118),4],[Rect(8627,699,122,118),5], #Platfrom 14
                [Rect(10501,596,122,118),1],[Rect(10498,694,122,118),4], #Platfrom 20
                [Rect(11501,496,122,118),1],[Rect(11626,496,122,118),1],[Rect(11499,594,122,118),4],[Rect(11624,594,122,118),4], #Platfrom 22
                [Rect(11499,719,122,118),4],[Rect(11624,719,122,118),4], #Platfrom 22
                [Rect(12001,296,122,118),1],[Rect(12123,296,122,118),1],[Rect(11999,394,122,118),4],[Rect(11999,519,122,118),4], #Paltfrom 23
                [Rect(11999,644,122,118),4],[Rect(11999,769,122,118),4],[Rect(12121,394,122,118),4],[Rect(12121,519,122,118),4], #Paltfrom 23
                [Rect(12121,643,122,118),4],[Rect(12121,768,122,118),4], #Platfrom 23
                [Rect(4201,601,122,118),7],[Rect(4328,601,122,118),7],[Rect(4328,700,122,118),10],[Rect(4201,700,122,118),10], #Platfrom 6
                [Rect(6100,600,122,118),7],[Rect(6227,600,122,118),7],[Rect(6100,699,122,118),10],[Rect(6227,699,122,118),10], #Platfrom 8
                [Rect(6800,301,122,118),12],[Rect(6905,300,122,118),13],[Rect(7033,300,122,118),13],[Rect(7159,300,122,118),14], #Platfrom 10
                [Rect(6809,400,122,118),15],[Rect(6809,527,122,118),15],[Rect(6809,654,122,118),15],[Rect(6809,781,122,118),15], #Platfrom 10
                [Rect(7159,400,122,118),17],[Rect(7159,530,122,118),17],[Rect(7159,660,122,118),17],[Rect(7159,790,122,118),17], #Platfrom 10
                [Rect(8200,600,122,118),13],[Rect(8200,698,122,118),16], #Platfrom 12
                [Rect(9001,601,122,118),7],[Rect(9128,601,122,118),7],[Rect(9001,700,122,118),10],[Rect(9128,700,122,118),10], #Platfrom 14
                [Rect(9500,300,122,118),13],[Rect(9500,398,122,118),16],[Rect(9500,525,122,118),16],[Rect(9500,652,122,118),16], #Platfrom 15
                [Rect(9500,679,122,118),16], #Platfrom 15
                [Rect(9701,401,122,118),7],[Rect(9828,401,122,118),7],[Rect(9828,500,122,118),10],[Rect(9828,599,122,118),10], #Platfrom 16
                [Rect(9828,698,122,118),10],[Rect(9701,500,122,118),10],[Rect(9701,599,122,118),10],[Rect(9701,698,122,118),10], #Platfrom 16
                [Rect(10150,200,122,118),13],[Rect(10150,298,122,118),16],[Rect(10150,396,122,118),16],[Rect(10150,494,122,118),16], #Platfrom 17
                [Rect(10150,592,122,118),16],[Rect(10150,690,122,118),16], #Platfrom 17
                [Rect(11001,601,122,118),7],[Rect(11001,699,122,118),10], #Platfrom 19
                [Rect(12400,300,122,118),13],[Rect(12528,300,122,118),13],[Rect(12400,398,122,118),16],[Rect(12400,525,122,118),16], #Platfrom 22
                [Rect(12400,652,122,118),16],[Rect(12400,779,122,118),16],[Rect(12528,398,122,118),16],[Rect(12528,525,122,118),16], #Platfrom 22
                [Rect(12528,652,122,118),16],[Rect(12528,779,122,118),16], #Platfrom 22
                [Rect(13000,750,122,118),18],[Rect(13105,750,122,118),19],[Rect(13231,750,122,118),20]] #Winning Platfrom

                background_cord=[-500,2500,3900,6400,7625,9500,12500,13900,16400,17650]
                pilar_cord=[2400,3780,6265,7525,9400,12400,16300,17550]
                death+=1
        
        display.flip()
        myClock.tick(60)

def draw_scene_lev2(screen,player,wall): # level 2 draw
    'drawing the player and the platform for level 1'

    global idle_frame
    global run_frame
    global jump_frame
    global dash_frame
    global bw_idle_frame
    global bw_run_frame
    global bw_jump_frame
    global bw_dash_frame
    global side_chose

    draw.rect(screen,RED,p,1)
    keys=key.get_pressed()

    death_text=Stgotic_font_3.render(str(death),True,(255,255,255)) #death text for level 2
    death_text_2=Stgotic_font_4.render(str(death),True,(80,60,5))

    for a in range(len(walls_2)):
        draw.rect(screen,BLUE,walls_2[a])
    for a in range(len(platform_2)):
        draw.rect(screen,WHITE,platform_2[a])
    for a in range(len(bounce_plat_2)):
        draw.rect(screen,GREEN,bounce_plat_2[a])
    for a in range(5): #adds the background to the level
        screen.blit(background[a],(background_cord[a],-100))
    for a in range(5):
        screen.blit(background[a],(background_cord[a+5],-100))
    for a in range(len(pilar_cord)):
        screen.blit(pilar,(pilar_cord[a],0))
    for a in range(len(blocks_2)):
        if blocks_2[a][1]==0:
            screen.blit(Block0,(blocks_2[a][0]))
        elif blocks_2[a][1]==1:
            screen.blit(Block1,(blocks_2[a][0]))
        elif blocks_2[a][1]==2:
            screen.blit(Block2,(blocks_2[a][0]))
        elif blocks_2[a][1]==3:
            screen.blit(Block3,(blocks_2[a][0]))
        elif blocks_2[a][1]==4:
            screen.blit(Block4,(blocks_2[a][0]))
        elif blocks_2[a][1]==5:
            screen.blit(Block5,(blocks_2[a][0]))
        elif blocks_2[a][1]==6:
            screen.blit(G_Block0,(blocks_2[a][0]))
        elif blocks_2[a][1]==7:
            screen.blit(G_Block1,(blocks_2[a][0]))
        elif blocks_2[a][1]==8:
            screen.blit(G_Block2,(blocks_2[a][0]))
        elif blocks_2[a][1]==9:
            screen.blit(G_Block3,(blocks_2[a][0]))
        elif blocks_2[a][1]==10:
            screen.blit(G_Block4,(blocks_2[a][0]))
        elif blocks_2[a][1]==11:
            screen.blit(G_Block5,(blocks_2[a][0]))
        elif blocks_2[a][1]==12:
            screen.blit(R_Block0,(blocks_2[a][0]))
        elif blocks_2[a][1]==13:
            screen.blit(R_Block1,(blocks_2[a][0]))
        elif blocks_2[a][1]==14:
            screen.blit(R_Block2,(blocks_2[a][0]))
        elif blocks_2[a][1]==15:
            screen.blit(R_Block3,(blocks_2[a][0]))
        elif blocks_2[a][1]==16:
            screen.blit(R_Block4,(blocks_2[a][0]))
        elif blocks_2[a][1]==17:
            screen.blit(R_Block5,(blocks_2[a][0]))
        elif blocks_2[a][1]==18:
            screen.blit(Go_Block0,(blocks_2[a][0]))
        elif blocks_2[a][1]==19:
            screen.blit(Go_Block1,(blocks_2[a][0]))
        elif blocks_2[a][1]==20:
            screen.blit(Go_Block2,(blocks_2[a][0]))
    
    if keys[K_RIGHT]:
        side_chose=1
    elif keys[K_LEFT]:
        side_chose=0

    #player animation to indicate when to use ceratin frames and how long
    if keys[K_RIGHT]==0 and keys [K_LEFT]==0 and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0 and side_chose==1:
        screen.blit(idle_pics[int(idle_frame)],(p[X],p[Y]))
        idle_frame+=0.08
        if idle_frame>4:
            idle_frame=0 #resets frame to 0
    
    elif keys[K_RIGHT]==0 and keys [K_LEFT]==0 and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0 and side_chose==0:
        screen.blit(bw_idle_pics[int(bw_idle_frame)],(p[X],p[Y]))
        bw_idle_frame+=0.08
        if bw_idle_frame>4:
            bw_idle_frame=0 #resets frame to 0
    
    if keys[K_RIGHT] and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0:
        screen.blit(run_pics[int(run_frame)],(p[X],p[Y]))
        run_frame+=0.15
        if run_frame>6:
            run_frame=0 #resets frame to 0

    elif keys[K_LEFT] and keys[K_SPACE]==0 and keys[K_UP]==0 and keys[K_DOWN]==0:
        screen.blit(bw_run_pics[int(bw_run_frame)],(p[X],p[Y]))
        bw_run_frame+=0.15
        if bw_run_frame>6:
            bw_run_frame=0 #resets frame to 0
    
    if keys[K_SPACE] or keys[K_UP] and side_chose==1:
        screen.blit(jump_pics[int(jump_frame)],(p[X],p[Y]))
        jump_frame+=0.1
        if jump_frame>7:
            jump_frame=0 #resets frame to 0
    
    elif keys[K_SPACE] or keys[K_UP] and side_chose==0:
        screen.blit(bw_jump_pics[int(bw_jump_frame)],(p[X],p[Y]))
        bw_jump_frame+=0.1
        if bw_jump_frame>7:
            bw_jump_frame=0 #resets frame to 0
    
    if keys[K_DOWN] and keys[K_SPACE]==0 and keys[K_UP]==0 and side_chose==1:
        screen.blit(dash_pics[int(dash_frame)],(p[X],p[Y]))
        dash_frame+=0.1
        if dash_frame>1:
            dash_frame=0 #resets frame to 0

    elif keys[K_DOWN] and keys[K_SPACE]==0 and keys[K_UP]==0 and side_chose==0:
        screen.blit(bw_dash_pics[int(bw_dash_frame)],(p[X],p[Y]))
        bw_dash_frame+=0.1
        if bw_dash_frame>1:
            bw_dash_frame=0 #resets frame to 0
            
    screen.blit(death_box,(950,10)) #adds images and text to death boxes
    screen.blit(death_text_2,(1102,50))
    screen.blit(death_text,(1100,45))
    screen.blit(death_pic,(1000,30))
            
    display.flip()

def move_lev2(player): #player movement for level 2
    'moving the player for level 2'
    keys=key.get_pressed()
    if keys[K_SPACE] or keys[K_UP]: 
        if p[Y]+p[H]==v[BOT] and v[Y]==0: #if the player is on the ground, the player is forced up appearing to be a jump
            v[Y]=jumpSpeed
            
    if keys[K_LEFT]: #move left
        v[X]=15
    elif keys[K_RIGHT]: #move right
        v[X]=-15
    else:
        v[X]=0 #stays still
    for a in range(len(platform_2)): #moves all the blocks one way if the player presses left or right 
        platform_2[a][X]+=v[X] 
    for a in range(len(bounce_plat_2)):
        bounce_plat_2[a][X]+=v[X]
    for a in range(len(walls_2)):
        walls_2[a][X]+=v[X]
    for a in range(len(background_cord)):
        background_cord[a]+=v[X]
    for a in range(len(pilar_cord)):
        pilar_cord[a]+=v[X]
    for i in range(len(blocks_2)):
        blocks_2[i][0].left+=v[X]
    
         
    v[Y]+=gravity #acceleration

def check_lev2(player,wall):
    'check if the player "lands" on a platform for level 2'
    for a in range(len(platform_2)): 
        if p[X]+p[W]>platform_2[a][X] and p[X]<platform_2[a][X]+platform_2[a][W] and p[Y]+p[H]<=platform_2[a][Y] and p[Y]+p[H]+v[Y]>platform_2[a][Y]:
            v[BOT]=platform_2[a][Y] #checks if player is on ground
            p[Y]=v[BOT]-p[H]
            v[Y]=0
            
    for a in range(len(bounce_plat_2)): #checks if player is on a bounce pad
        if p[X]+p[W]>bounce_plat_2[a][X] and p[X]<bounce_plat_2[a][X]+bounce_plat_2[a][W] and p[Y]+p[H]<=bounce_plat_2[a][Y] and p[Y]+p[H]+v[Y]>bounce_plat_2[a][Y]:
            v[Y]=1.25*jumpSpeed #if so the player is forced up when on the bounce pad
            
    p[Y]+=v[Y]#falling down

def dash_lev2(player): #dash for level 2
    'dashing for level 2'
    global p
    global platform_2
    global walls_2
    global bounce_plat_2
    global death
    global dash_count
    global level
    global death
    global background_cord
    global pilar_cord
    global timer
    global dash_count
    global blocks_2

    keys=key.get_pressed() 
            
    if keys[K_UP] or keys[K_SPACE]: # if the player it's the walls then the level is reset
        dash_count=1
        timer=0
            
    if keys[K_DOWN]:
         if dash_count==1: #dashing the big mechanic 
            timer+=1
            if keys[K_LEFT]:
                for a in range(len(platform_2)):
                    if timer%2==0:
                        platform_2[a][X]+=80
                for a in range(len(bounce_plat_2)):
                    if timer%2==0:
                        bounce_plat_2[a][X]+=80
                for a in range(len(walls_2)):
                    if timer%2==0:
                        walls_2[a][X]+=80
                for a in range(len(background_cord)):
                    if timer%2==0:
                        background_cord[a]+=80
                for a in range(len(pilar_cord)):
                    if timer%2==0:
                        pilar_cord[a]+=80
                for a in range(len(blocks_2)):
                    if timer%2==0:
                        blocks_2[a][0].left+=80
                            
                if timer>20: #if timer is above 20 dash count is 0 making the dash stop
                    dash_count=0 
            else:
                for a in range(len(platform_2)):
                    if timer%2==0:
                        platform_2[a][X]-=80
                for a in range(len(bounce_plat_2)):
                    if timer%2==0:
                        bounce_plat_2[a][X]-=80
                for a in range(len(walls_2)):
                    if timer%2==0:
                        walls_2[a][X]-=80
                for a in range(len(background_cord)):
                    if timer%2==0:
                        background_cord[a]-=80
                for a in range(len(pilar_cord)):
                    if timer%2==0:
                        pilar_cord[a]-=80
                for a in range(len(blocks_2)):
                    if timer%2==0:
                        blocks_2[a][0].left-=80
                            
                if timer>10:
                    dash_count=0 #if timer is above 20 dash count is 0 making the dash stop
                    
def death_lev2(player): #death for level 2
    'death for level 2'
    global p
    global platform_2
    global walls_2
    global bounce_plat_2
    global death
    global dash_count
    global level
    global death
    global background_cord
    global pilar_cord
    global blocks_2
    
    for a in range(len(walls_2)): #resets the level if the player hits a wall
        if p.colliderect(walls_2[a]):
            p=Rect(250,150,40,80)
                                
            walls_2=[Rect(2900,440,263,500),Rect(6600,250,593,700),Rect(7700,450,130,700),Rect(7950,500,130,700),Rect(9400,250,130,600),
                         Rect(11300,250,130,600),Rect(11600,650,130,300),Rect(151,602,463,400),
                         Rect(901,602,133,200),Rect(1601,402,128,500),Rect(4001,301,458,500),
                         Rect(6001,351,468,500),Rect(8101,751,598,250),Rect(8801,571,130,300),
                         Rect(9101,351,130,500),Rect(10701,551,130,300),Rect(11101,351,130,500),
                         Rect(11801,751,298,300),Rect(2401,751,298,50),Rect(3301,751,398,500),
                         Rect(5401,751,398,50),Rect(7251,751,298,50),Rect(10101,601,260,300),
                         Rect(-500,770,15000,300),Rect(-2000,0,1500,1000)]

            bounce_plat_2=[Rect(2400,750,260,50),Rect(3300,750,380,100),Rect(5400,750,380,100),
                                   Rect(7250,750,260,100),Rect(10100,600,260,100)]

            platform_2=[Rect(150,600,465,20),Rect(900,600,137,20),Rect(1600,400,130,20),
                                Rect(4000,300,460,20),Rect(6000,350,470,20),Rect(8100,750,585,25),
                                Rect(8800,570,130,20),Rect(9100,350,130,20),Rect(10700,550,130,20),
                                Rect(11100,350,130,20),Rect(11800,750,300,20)]
                
            blocks_2=[[Rect(150,600,122,188),0],[Rect(254,595,122,188),1],[Rect(376,595,122,188),1],[Rect(500,600,122,188),2], #Platfrom 1
                    [Rect(155,695,122,188),3],[Rect(500,698,122,188),5], #Platfrom 1
                    [Rect(900,595,122,188),1],[Rect(897,695,122,188),4], #Platfrom 2
                    [Rect(1600,395,122,188),1],[Rect(1597,495,122,188),4],[Rect(1597,620,122,188),4],[Rect(1597,745,122,188),4], #Platfrom 3
                    [Rect(2400,750,122,188),7],[Rect(2527,750,122,188),7], #Platfrom 4
                    [Rect(2900,440,122,188),13],[Rect(3028,440,122,188),13],[Rect(3028,538,122,188),16],[Rect(3028,664,122,188),16], #Platfrom 5
                    [Rect(3028,790,122,188),16],[Rect(2900,538,122,188),16],[Rect(2900,664,122,188),16],[Rect(2900,790,122,188),16], #Platfrom 5
                    [Rect(3300,750,122,188),7],[Rect(3427,750,122,188),7],[Rect(3552,750,122,188),7], #Platfrom 6
                    [Rect(4000,300,122,188),0],[Rect(4104,295,122,188),1],[Rect(4226,295,122,188),1],[Rect(4350,300,122,188),2], #Platfrom 7
                    [Rect(4005,395,122,188),3],[Rect(4005,490,122,188),3],[Rect(4005,585,122,188),3],[Rect(4005,680,122,188),3], #Platfrom 7
                    [Rect(4350,395,122,188),5],[Rect(4350,490,122,188),5],[Rect(4350,585,122,188),5],[Rect(4350,680,122,188),5], #Platfrom 7
                    [Rect(5400,750,122,188),7],[Rect(5527,750,122,188),7],[Rect(5652,750,122,188),7], #Platfrom 8
                    [Rect(6000,350,122,188),0],[Rect(6104,345,122,188),1],[Rect(6226,345,122,188),1],[Rect(6350,350,122,188),2], #Platfrom 9
                    [Rect(6005,445,122,188),3],[Rect(6005,540,122,188),3],[Rect(6005,635,122,188),3],[Rect(6005,730,122,188),3], #Platfrom 9
                    [Rect(6350,445,122,188),5],[Rect(6350,540,122,188),5],[Rect(6350,635,122,188),5],[Rect(6350,730,122,188),5],
                    [Rect(6600,250,122,188),12],[Rect(6701,250,122,188),13],[Rect(6826,250,122,188),13],[Rect(6952,250,122,188),13], #Platfrom 10
                    [Rect(7078,250,122,188),14],[Rect(6609,349,122,188),15],[Rect(6609,478,122,188),15],[Rect(6609,589,122,188),15], #Platfrom 10
                    [Rect(6609,718,122,188),15],[Rect(7078,349,122,188),17],[Rect(7078,478,122,188),17],[Rect(7078,589,122,188),17], #Platfrom 10
                    [Rect(7078,718,122,188),17], #Platfrom 10
                    [Rect(7250,750,122,188),7],[Rect(7377,750,122,188),7], #Platfrom 11
                    [Rect(7700,450,122,188),13],[Rect(7700,549,122,188),16],[Rect(7700,678,122,188),16], #Platfrom 12
                    [Rect(7950,500,122,188),13],[Rect(7950,599,122,188),16],[Rect(7950,728,122,188),16], #Platfrom 13
                    [Rect(8100,750,122,188),0],[Rect(8204,745,122,188),1],[Rect(8326,745,122,188),1],[Rect(8448,745,122,188),1], #Platfrom 14
                    [Rect(8570,750,122,188),2], #Platfrom 14
                    [Rect(8801,566,122,188),1],[Rect(8799,666,122,188),4],[Rect(8799,781,122,188),4], #Platfrom 15
                    [Rect(9101,346,122,188),1],[Rect(9099,446,122,188),4],[Rect(9099,571,122,188),4],[Rect(9099,696,122,188),4], #Platfrom 16
                    [Rect(9400,250,122,188),13],[Rect(9400,349,122,188),16],[Rect(9400,474,122,188),16],[Rect(9400,599,122,188),16], #Platfrom 17
                    [Rect(9400,724,122,188),16], #Platfrom 17
                    [Rect(10100,600,122,188),7],[Rect(10227,600,122,188),7],[Rect(10227,699,122,188),10],[Rect(10100,699,122,188),10], #Platfrom 18
                    [Rect(10701,546,122,188),1],[Rect(10699,646,122,188),4],[Rect(10699,771,122,188),4], #Platfrom 19
                    [Rect(11101,346,122,188),1],[Rect(11099,446,122,188),4],[Rect(11099,571,122,188),4],[Rect(11099,696,122,188),4], #Platfrom 20
                    [Rect(11300,250,122,188),13],[Rect(11300,348,122,188),16],[Rect(11300,348,122,188),16],[Rect(11300,474,122,188),16], #Platfrom 21
                    [Rect(11300,600,122,188),16],[Rect(11300,726,122,188),16], #Platfrom 21
                    [Rect(11600,650,122,188),13],[Rect(11600,749,122,188),16], #Platfrom 22
                    [Rect(11800,750,122,188),19],[Rect(11928,750,122,188),19]] #Winning Platfrom
            
            background_cord=[-500,2500,3900,6400,7625,9500,12500,13900,16400,17650]
            pilar_cord=[2400,3780,6265,7525,9400,12400,16300,17550]
            death+=1 #death count is added upon 
                
def level_2(action): #preforms level 2
    'preforms level 2'
    global p
    global platform_2
    global walls_2
    global bounce_plat_2
    global death
    global dash_count
    global level
    global death
    global background_cord
    global pilar_cord
    global blocks_2

    level=2 #level equals 2
    
    while action=='level_2':
        for evnt in event.get():            
            if evnt.type == QUIT: #if the player exits the player goes back to level 1
                action=='menu'
                return "menu"
            
        keys=key.get_pressed()

        #preforms the functions that are in level 2
        move_lev2(p)
        draw_scene_lev2(screen,p,platform_2)
        check_lev2(p,platform_2)
        dash_lev2(p)
        death_lev2(p)

        #if the player hits the final platform, the screen goes to the level complete screen
        if p[X]+p[W]>platform_2[10][X] and p[X]<platform_2[10][X]+platform_2[10][W] and p[Y]+p[H]<=platform_2[10][Y] and p[Y]+p[H]+v[Y]>platform_2[10][Y]:
            action='level_complete'
            level_complete('level_complete')
        
            
        if keys[K_UP] or keys[K_SPACE]:
            dash_count=1
            timer=0
            
        if keys[K_DOWN]:
            if dash_count==1:
                timer+=1
                if keys[K_LEFT]:
                    for a in range(len(platform_2)):
                        if timer%2==0:
                            platform_2[a][X]+=80
                    for a in range(len(bounce_plat_2)):
                        if timer%2==0:
                            bounce_plat_2[a][X]+=80
                    for a in range(len(walls_2)):
                        if timer%2==0:
                            walls_2[a][X]+=80
                    for a in range(len(background_cord)):
                        if timer%2==0:
                            background_cord[a]+=80
                    for a in range(len(pilar_cord)):
                        if timer%2==0:
                            pilar_cord[a]+=80
                    for a in range(len(blocks_2)):
                        if timer%2==0:
                            blocks_2[a][0].left+=80
                            
                    if timer>20:
                        dash_count=0
                else:
                    for a in range(len(platform_2)):
                        if timer%2==0:
                            platform_2[a][X]-=80
                    for a in range(len(bounce_plat_2)):
                        if timer%2==0:
                            bounce_plat_2[a][X]-=80
                    for a in range(len(walls_2)):
                        if timer%2==0:
                            walls_2[a][X]-=80
                    for a in range(len(background_cord)):
                        if timer%2==0:
                            background_cord[a]-=80
                    for a in range(len(pilar_cord)):
                        if timer%2==0:
                            pilar_cord[a]-=80
                    for a in range(len(blocks_2)):
                        if timer%2==0:
                            blocks_2[a][0].left-=80
                            
                    if timer>10:
                        dash_count=0

        for a in range(len(walls_2)):
            if p.colliderect(walls_2[a]):
                p=Rect(250,150,40,80)
                                
                walls_2=[Rect(2900,440,263,500),Rect(6600,250,593,700),Rect(7700,450,130,700),Rect(7950,500,130,700),Rect(9400,250,130,600),
                         Rect(11300,250,130,600),Rect(11600,650,130,300),Rect(151,602,463,400),
                         Rect(901,602,133,200),Rect(1601,402,128,500),Rect(4001,301,458,500),
                         Rect(6001,351,468,500),Rect(8101,751,598,250),Rect(8801,571,130,300),
                         Rect(9101,351,130,500),Rect(10701,551,130,300),Rect(11101,351,130,500),
                         Rect(11801,751,298,300),Rect(2401,751,298,50),Rect(3301,751,398,500),
                         Rect(5401,751,398,50),Rect(7251,751,298,50),Rect(10101,601,260,300),
                         Rect(-500,770,15000,300),Rect(-2000,0,1500,1000)]

                bounce_plat_2=[Rect(2400,750,260,50),Rect(3300,750,380,100),Rect(5400,750,380,100),
                                   Rect(7250,750,260,100),Rect(10100,600,260,100)]

                platform_2=[Rect(150,600,465,20),Rect(900,600,137,20),Rect(1600,400,130,20),
                                Rect(4000,300,460,20),Rect(6000,350,470,20),Rect(8100,750,585,25),
                                Rect(8800,570,130,20),Rect(9100,350,130,20),Rect(10700,550,130,20),
                                Rect(11100,350,130,20),Rect(11800,750,300,20)]
                
                blocks_2=[[Rect(150,600,122,188),0],[Rect(254,595,122,188),1],[Rect(376,595,122,188),1],[Rect(500,600,122,188),2], #Platfrom 1
                  [Rect(155,695,122,188),3],[Rect(500,698,122,188),5], #Platfrom 1
                  [Rect(900,595,122,188),1],[Rect(897,695,122,188),4], #Platfrom 2
                  [Rect(1600,395,122,188),1],[Rect(1597,495,122,188),4],[Rect(1597,620,122,188),4],[Rect(1597,745,122,188),4], #Platfrom 3
                  [Rect(2400,750,122,188),7],[Rect(2527,750,122,188),7], #Platfrom 4
                  [Rect(2900,440,122,188),13],[Rect(3028,440,122,188),13],[Rect(3028,538,122,188),16],[Rect(3028,664,122,188),16], #Platfrom 5
                  [Rect(3028,790,122,188),16],[Rect(2900,538,122,188),16],[Rect(2900,664,122,188),16],[Rect(2900,790,122,188),16], #Platfrom 5
                  [Rect(3300,750,122,188),7],[Rect(3427,750,122,188),7],[Rect(3552,750,122,188),7], #Platfrom 6
                  [Rect(4000,300,122,188),0],[Rect(4104,295,122,188),1],[Rect(4226,295,122,188),1],[Rect(4350,300,122,188),2], #Platfrom 7
                  [Rect(4005,395,122,188),3],[Rect(4005,490,122,188),3],[Rect(4005,585,122,188),3],[Rect(4005,680,122,188),3], #Platfrom 7
                  [Rect(4350,395,122,188),5],[Rect(4350,490,122,188),5],[Rect(4350,585,122,188),5],[Rect(4350,680,122,188),5], #Platfrom 7
                  [Rect(5400,750,122,188),7],[Rect(5527,750,122,188),7],[Rect(5652,750,122,188),7], #Platfrom 8
                  [Rect(6000,350,122,188),0],[Rect(6104,345,122,188),1],[Rect(6226,345,122,188),1],[Rect(6350,350,122,188),2], #Platfrom 9
                  [Rect(6005,445,122,188),3],[Rect(6005,540,122,188),3],[Rect(6005,635,122,188),3],[Rect(6005,730,122,188),3], #Platfrom 9
                  [Rect(6350,445,122,188),5],[Rect(6350,540,122,188),5],[Rect(6350,635,122,188),5],[Rect(6350,730,122,188),5],
                  [Rect(6600,250,122,188),12],[Rect(6701,250,122,188),13],[Rect(6826,250,122,188),13],[Rect(6952,250,122,188),13], #Platfrom 10
                  [Rect(7078,250,122,188),14],[Rect(6609,349,122,188),15],[Rect(6609,478,122,188),15],[Rect(6609,589,122,188),15], #Platfrom 10
                  [Rect(6609,718,122,188),15],[Rect(7078,349,122,188),17],[Rect(7078,478,122,188),17],[Rect(7078,589,122,188),17], #Platfrom 10
                  [Rect(7078,718,122,188),17], #Platfrom 10
                  [Rect(7250,750,122,188),7],[Rect(7377,750,122,188),7], #Platfrom 11
                  [Rect(7700,450,122,188),13],[Rect(7700,549,122,188),16],[Rect(7700,678,122,188),16], #Platfrom 12
                  [Rect(7950,500,122,188),13],[Rect(7950,599,122,188),16],[Rect(7950,728,122,188),16], #Platfrom 13
                  [Rect(8100,750,122,188),0],[Rect(8204,745,122,188),1],[Rect(8326,745,122,188),1],[Rect(8448,745,122,188),1], #Platfrom 14
                  [Rect(8570,750,122,188),2], #Platfrom 14
                  [Rect(8801,566,122,188),1],[Rect(8799,666,122,188),4],[Rect(8799,781,122,188),4], #Platfrom 15
                  [Rect(9101,346,122,188),1],[Rect(9099,446,122,188),4],[Rect(9099,571,122,188),4],[Rect(9099,696,122,188),4], #Platfrom 16
                  [Rect(9400,250,122,188),13],[Rect(9400,349,122,188),16],[Rect(9400,474,122,188),16],[Rect(9400,599,122,188),16], #Platfrom 17
                  [Rect(9400,724,122,188),16], #Platfrom 17
                  [Rect(10100,600,122,188),7],[Rect(10227,600,122,188),7],[Rect(10227,699,122,188),10],[Rect(10100,699,122,188),10], #Platfrom 18
                  [Rect(10701,546,122,188),1],[Rect(10699,646,122,188),4],[Rect(10699,771,122,188),4], #Platfrom 19
                  [Rect(11101,346,122,188),1],[Rect(11099,446,122,188),4],[Rect(11099,571,122,188),4],[Rect(11099,696,122,188),4], #Platfrom 20
                  [Rect(11300,250,122,188),13],[Rect(11300,348,122,188),16],[Rect(11300,348,122,188),16],[Rect(11300,474,122,188),16], #Platfrom 21
                  [Rect(11300,600,122,188),16],[Rect(11300,726,122,188),16], #Platfrom 21
                  [Rect(11600,650,122,188),13],[Rect(11600,749,122,188),16], #Platfrom 22
                  [Rect(11800,750,122,188),19],[Rect(11928,750,122,188),19]] #Winning Platfrom
                
                background_cord=[-500,2500,3900,6400,7625,9500,12500,13900,16400,17650]
                pilar_cord=[2400,3780,6265,7525,9400,12400,16300,17550]
                death+=1
                
        display.flip()
        myClock.tick(60)

def level_complete(action): #level complete screen
    'shows the level complete screen'
    global restart_level_1
    global restart_level_2
    global next_stage
    
    while action=='level_complete':
        for evnt in event.get():            
            if evnt.type==QUIT:
                return "menu"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        death=0
        
        #draws and adds the pictures to level 1
        draw.rect(screen,BLACK,(145,95,10,610))
        draw.rect(screen,(110,110,100),(147,97,906,606))
        draw.rect(screen,RED,restart_rect) #restart
        draw.rect(screen,RED,menu_rect) #menu
        draw.rect(screen,RED,next_level_rect) #next level
        screen.blit(level_complete_pic,(150,95))
        screen.blit(word_2,(210,175))
        screen.blit(word,(220,170))

        #depending on how many times the player dies, once the player beats the level the player is given golden stars on how they preformed
        if death>10: 
            screen.blit(pixel_grey_star,(230,350))
            screen.blit(pixel_grey_star,(490,300))
            screen.blit(pixel_grey_star,(750,350))
        elif death>5:
            screen.blit(pixel_star,(230,350))
            screen.blit(pixel_grey_star,(490,300))
            screen.blit(pixel_grey_star,(750,350))
        elif death>3:
            screen.blit(pixel_star,(230,350))
            screen.blit(pixel_star,(490,300))
            screen.blit(pixel_grey_star,(750,350))
        elif death>=0:
            screen.blit(pixel_star,(230,350))
            screen.blit(pixel_star,(490,300))
            screen.blit(pixel_star,(750,350))
        
        screen.blit(restart_level,(430,580))
        screen.blit(home_button,(545,580))
        screen.blit(next_button,(660,580))

        if mb[0]==1:
            if restart_rect.collidepoint(mx,my): #if the player hits the restart button, they go back to the menu, but level_restart = 1 meaning it'll imediatly go to level 1
                if level==1:
                    restart_level_1=1
                    action='menu'
                    return 'menu'
                    
                else:
                    restart_level_2=1
                    return 'menu'
                    
            if menu_rect.collidepoint(mx,my): #the player goes back to menu if he clicks the home button
                action='menu'
                return 'menu'
            
            if next_level_rect.collidepoint(mx,my): #if the player hits the next stage button he goes to the next level, unless he is on level 1 then he goes back to home
                if level==1:
                    next_stage=1
                    action='menu'
                    return 'menu'
                else:
                    action='menu'
                    return 'menu' 

        display.flip()
        myClock.tick(60)

def instructions(action):
    while action=='instructions':
        for evnt in event.get():            
            if evnt.type == QUIT:
                return "menu" #returns home if the player exits
            
        #adds images and text to the instruction page, as this screen is not meant for anything less
        screen.blit(old_paper,(0,0))
        screen.blit(idle_pics[1],(60,100))
        screen.blit(run_pics[2],(210,100))
        screen.blit(run_pics[4],(360,100))
        screen.blit(arrow,(130,110))
        screen.blit(arrow,(280,110))
            
        screen.blit(idle_pics[1],(60,400))
        screen.blit(jump_pics[3],(260,280))
        screen.blit(jump_pics[5],(460,340))
        screen.blit(arrow_diagonal,(120,370))
        screen.blit(arrow_diagonal,(190,320))
        screen.blit(down_arrow,(320,300))
        screen.blit(down_arrow,(390,350))

        screen.blit(idle_pics[1],(60,700))
        screen.blit(jump_pics[2],(160,640))
        screen.blit(jump_pics[3],(460,640))
        screen.blit(arrow_diagonal,(105,670))
        screen.blit(arrow,(220,650))
        screen.blit(arrow,(300,650))
        screen.blit(arrow,(380,650))

        screen.blit(run_word_2,(540,80))
        screen.blit(run_word,(540,80))
        screen.blit(jump_word_2,(540,300))
        screen.blit(jump_word,(540,300))
        screen.blit(dash_word_2,(540,500))
        screen.blit(dash_word,(540,500))

        screen.blit(run_text,(540,150))
        screen.blit(run_text_2,(540,190))
        screen.blit(jump_text,(540,360))
        screen.blit(jump_text_2,(540,400))
        screen.blit(dash_text,(540,560))
        screen.blit(dash_text_2,(540,600))
        screen.blit(dash_text_3,(540,640))
        screen.blit(dash_text_4,(540,680))
        
        display.flip()
        myClock.tick(60)

def quit_action(action):
    while action=="quit": #if the player hits the quit button the program quits
        quit()


Block0=image.load("Pics/Block0.png")
Block1=image.load("Pics/Block1.png")
Block2=image.load("Pics/Block2.png")
Block3=image.load("Pics/Block3.png")
Block4=image.load("Pics/Block4.png")
Block5=image.load("Pics/Block5.png")
G_Block0=image.load("Pics/G_Block0.png")
G_Block1=image.load("Pics/G_Block1.png")
G_Block2=image.load("Pics/G_Block2.png")
G_Block3=image.load("Pics/G_Block3.png")
G_Block4=image.load("Pics/G_Block4.png")
G_Block5=image.load("Pics/G_Block5.png")
R_Block0=image.load("Pics/R_Block0.png")
R_Block1=image.load("Pics/R_Block1.png")
R_Block2=image.load("Pics/R_Block2.png")
R_Block3=image.load("Pics/R_Block3.png")
R_Block4=image.load("Pics/R_Block4.png")
R_Block5=image.load("Pics/R_Block5.png")
Go_Block0=image.load("Pics/Go_Block0.png")
Go_Block1=image.load("Pics/Go_Block1.png")
Go_Block2=image.load("Pics/Go_Block2.png")

menu("menu") #preforms menu function

quit()
