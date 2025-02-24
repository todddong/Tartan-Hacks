from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image
import random

##########################################################################################
############################ All Helper Functions ########################################
##########################################################################################

def loadPilImage(url):
    # Loads a PIL image from a url
    return Image.open(urlopen(url)) 

def distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2) ** 0.5


##########################################################################################
############################ All Helper Functions ########################################
##########################################################################################

# Overall model shared between all screens
def onAppStart(app):

##########################################################################################
#################### All lists with the respective quotes ################################
##########################################################################################

    app.factHIS = ["Antarctica Had a rainforest 90 million years ago",
"A woman was elected to Congress \nbefore women had the right to vote",
"Four U.S. presidents were cheerleaders",
"Woodrow Wilson was the only president with a Ph.D.",
"Emperor Hirohito was buried wearing a Mickey Mouse watch",
"Roman ships used flamethrowers as far back as the 7th century",
"Vikings didn’t actually wear horned helmets",
"The Third Punic War didn’t officially end until 1985 –\n 2,000 years after it started.",
"It took the Oxford English Dictionary editors \nfive years just to reach the word ant",
"Ducklings were used for medical therapy in the 1950s."]

    app.factCEL = ["Tom Hanks is related to Abraham Lincoln",
"Harry Styles has four nipples",
"President Obama, President George Bush,\n and Brad Pitt are all distant cousins",
"Jennifer Lawrence has six toes on her left foot",
"Daniel Radcliffe is allergic to horses",
"Frank Oz was the voice for Yoda,\n Miss Piggy, and the Cookie Monster.",
"Liam Payne has a fear of spoons",
"Elvis Presley was a natural blonde",
"Tom Hanks had an asteroid named after him\n which was called ‘12818 tomhanks’",
"Ryan Gosling was asked to audition for the Backstreet Boys\n but he turned it down."]

    app.factGEO = ["Antarctica is the largest desert",
"Canada has the longest coastline",
"Russia spans 11 timezones",
"90% of Earth’s population lives in the Northern Hemisphere.",
"Australia is wider than the moon",
'''In the Philippines, there’s an island that’s within a lake,
 on an island, that’s within a lake, on an island.''',
"Russia and the United States,\n at their closest points, are about 2.4 miles apart.",
"Antarctica holds about 70% of the world’s freshwater,\n stored in its massive ice sheets.",
"Iceland is growing 5 centimeters each year.",
"Africa is the only continent \nsituated in all four hemispheres."
"The Caspian Sea is the largest lake by surface area",
"Mawsynram, India, is the wettest place on Earth,\n with the most rainfall",
"Angel Falls in Venezuela\n is the world’s tallest waterfall",
"Tokyo, Japan, is the most populous city",
"The longest highway runs from Alaska to Argentina",
"La Paz, Bolivia, is the highest capital city",
"Lake Baikal in Russia is the deepest lake",
"Ethiopia uses a unique calendar system",
"Mammoth Cave in Kentucky\n is the longest cave system in the world",
"The deepest known cave is Krubera Cave in Georgia",
"When Krakatau erupted,\n it released the energy of 15,000 nuclear bombs",
"Thirty of the world’s highest mountains are in the Himalayas",]


    app.factSPO = ["Wrestling is considered mankind’s oldest sport,\nwith traces of its origins \nback to the dawn of civilization.",
"The Cleveland Browns are the only NFL franchise\n to neither play in a Super Bowl or host one.",
"NFL home teams must provide \n36 regulation footballs for each game",
"Around 42,000 tennis balls \nare used in the 650 tennis matches in Wimbledon",
"Before lacrosse, the Maryland State sport was jousting",
"Olympic gold medals are \n93% silver, 6% copper, and 1% actual gold",
"NFL Super Bowl referees also get Super Bowl rings.",
"Baseballs last an average of seven pitches.",
"The ‘G’ on the Green Bay Packers helmet \nstands for “greatness” not Green Bay",
"Golf and Javelin toss are the only two games\n to have been played on the moon.",
"The YoYo started out as a weapon in the Philippines",
"During WWII, the Steelers and Eagles \nlost so many players, they combined into the Steagles",
"The Buffalo Bills appeared in 4 consecutive Super Bowls,\n and lost them all",
"Major League Umpires are required to wear black underwear,\n in the case of a disaster",
"Babe Ruth used to keep a cabbage leaf\n on his head to keep him cool",
"At one point, the tallest and shortest \nplayers played on the Washington Bullets at the same time",
"Shaq has made 1 of 22 three point attempts in his career",
"Only 6 of all World Cups were won by the host country",
"On average, each player runs 7 miles per game",
"Most NASCAR teams use nitrogen\n instead of oxygen in their tires"]


    app.factANI = ["Dolphins use toxic pufferfish to ‘get high’",
"There are more than 1.4 billion insects\n for each human on the planet.",
"A Mayfly’s total lifespan is just 24 hours",
"Koalas can sleep for up to 22 hours a day.",
"A group of parrots is known as a pandemonium",
"Cows poo up to 15 times a day,\n which can be as much as 115 pounds of poo per day",
"A common garden snail has 14,000 teeth",
"Baby elephants suck their trunks for comfort",
"The Giant Pacific Octopus has \n3 hearts, 9 brains, and blue blood",
"More than half of all pigs in the world\n are kept by farmers in China",
"There’s a species of frog that can fly",
"Flamingos are born white\n but turn pink from the algae they eat",
"A chicken once lived for 18 months without a head",
"Hippos can’t actually swim,\n they just run across the river bottom",
"Cuttlefish can change colour in 200 milliseconds\n, aka, the blink of an eye",
"Orangutans self-medicate",
"Chimpanzees and monkeys are known to\n steal and consume alcoholic drinks",
"The hairiest animal in the world is the sea otter",
"An elephant’s trunk has\n tens of thousands of individual muscles",
"Hummingbirds are the\n only bird that can fly backwards",
"Male seahorses give birth",
"Elephants hold funerals for each other",
"The Costasiella Sea Slug\n is part animal, part vegetable",
"Tardigrades can pretty much survive anywhere",
"Some animals can regrow lost limbs",
"An electric eel can produce up to 600V of \nelectricity at once, enough to kill a human",
"Birds don’t pee",
"The largest butterfly was so big\n it was killed by a shotgun"]

    app.factNAT =["More people die from falling coconuts\n than from shark attacks",
"There have been 5 mass extinctions\n which killed off half of species",
"Some species of fungi\n can turn ants into ‘zombies’",
"There are more than 200 different viruses\n which cause colds in humans",
"Despite what many believe,\n viruses are not living things",
"There are more species of microbe\n on Earth than stars in the galaxy",
"Crocodiles and Alligators are color blind",
"Trees can ‘talk’ to each other\n using a network of fungi in the soil",
"There are lakes under the Ocean",
"Mount Everest is still growing",
"The Sahara Desert was once green",
"Snow can be pink",
"Snow has been recorded in the\n Sahara Desert multiple times in recent years"]

    app.factRAN = ["President Kennedy was the fastest random speaker in the world \nwith upwards of 350 words per minute.",
"In the average lifetime, a person will walk\n the equivalent of 5 times around the equator.",
"Odontophobia is the fear of teeth.",
"The 57 on Heinz ketchup bottles represents\n the number of varieties of pickles the company once had.",
"The surface area of an average-sized brick\n is 79 cm squared.",
"According to suicide statistics,\n Monday is the favored day for self-destruction.",
"Cats sleep 16 to 18 hours per day.",
"The most common name in the world is Mohammed.",
"Karoke means empty orchestra in Japanese.",
"There are two credit cards\n for every person in the United States"
"When you die \nyour hair still grows for a couple of months.",
"There are two credit cards\n for every person in the United States.",
"Isaac Asimov is the only author\n to have a book in every Dewey-decimal category.",
"The first person selected as\n the Time Magazine Man of the Year\n - Charles Lindbergh in 1927.",
"The most money ever paid for a cow\n in an auction was $1.3 million.",
"It took Leo Tolstoy six years\n to write War & Peace.",
"The Neanderthal's brain was bigger than yours is.",
"On the new hundred dollar bill\n the time on the clock tower of Independence Hall is 4:10.",
"The sound of E.T. walking was made \nby someone squishing her hands in jelly.",
"The pancreas produces Insulin.",
"1 in 5,000 north Atlantic lobsters are born bright blue.",
"There are 10 human body parts that are only 3 letters long\n (eye hip arm leg ear toe jaw rib lip gum).",
"A skunk's smell can be detected by a human a mile away.",
"The word lethologica describes the state\n of not being able to remember the word you want.",
"The king of hearts is the only\n king without a moustache.",
"Every year about 98% of the atoms\n in your body are replaced.",
"Elephants are the only mammals that can't jump.",
"The international telephone dialing code\n for Antarctica is 672.",
"World Tourist day is observed on September 27.",
"Women are 37% more likely to go to a psychiatrist\n than men are."]

    app.quoteFAM = ["Audrey Hepburn:\n Nothing is impossible, the word itself says Im possible" ,
"Fran Lebowitz:\n In real life, I assure you, there is no such thing as Algebra",
"Albert Einstein:\n The only source of knowledge is experience.",
"Albert Einstein:\n I have no special talent. I am only passionately curious.",
'''John F. Kennedy:\n Ask not what your country can do for you 
-- ask what you can do for your country''',
"Winston Churchill:\n If youre going through hell, keep going",
"Theodore Roosevelt:\n Believe you can and youre halfway there ",
'''Dr. Seuss:\n You have brains in your head.\n 
You have feet in your shoes. \n
You can steer yourself any direction you choose''',
"Oprah Winfrey:\n You can have it all, you just cant have it all at ",
'''Steve Jobs:\n Have the courage to follow your heart and intuition. 
They somehow know what you truly want to become. ''']
    
##########################################################################################
########################## End of lists with quotes ######################################
##########################################################################################

    # Introscreen Variables
    reset_introScreen(app)

    # Feed screen Variables
    app.user = None
    app.factLikes = 0
    app.quoteLikes = 0

    app.topic = None
    app.likeUrl = 'https://uxwing.com/wp-content/themes/uxwing/download/hand-gestures/thumbs-up-black-icon.png'
    app.dislikeUrl = 'https://uxwing.com/wp-content/themes/uxwing/download/hand-gestures/thumbs-down-black-icon.png'
    app.likes = 0
    app.dislikes = 0

    app.feed1List, app.feed2List = None, None
    app.feed1Indx, app.feed2Indx = 0, 0
    app.text1, app.text2 = None, None

    app.topicKeys = ['HIS', 'CEL', 'GEO', 'SPO', 'ANI', 'NAT', 'RAN', 'FAM']
    app.topics = [app.factHIS, app.factCEL, app.factGEO, app.factSPO, 
                  app.factANI, app.factNAT, app.factRAN, app.quoteFAM]
    app.topicLikeDict = {'HIS': 0, 'CEL': 0, 'GEO': 0, 'SPO': 0,
                         'ANI': 0, 'NAT':0, 'RAN':0, 'FAM': 0}
    app.topicDislikeDict = {'HIS': 0, 'CEL': 0, 'GEO': 0, 'SPO': 0,
                            'ANI': 0, 'NAT':0, 'RAN':0, 'FAM': 0}

    app.feed1Low, app.feed2Low = 0, 0
    app.feed1X, app.feed2X = 0, 0
    app.fd1H, app.fd2H = 800, 800
    app.fd1W, app.fd2W = 500, 500
    app.feed1Pos = 150
    app.feed2Pos = 950
    app.fd1LabelX, app.fd1LabelY = (app.feed1X+app.fd1W)//2, (app.feed1Pos+app.fd1H)//2
    app.fd2LabelX, app.fd2LabelY = (app.feed2X+app.fd2W)//2, app.fd1LabelY+800
    
    app.likeUrl = 'https://raw.githubusercontent.com/alanpham06/exceed-TH2025/refs/heads/main/thumbs-up-black-icon.webp'
    app.dislikeUrl = 'https://raw.githubusercontent.com/alanpham06/exceed-TH2025/refs/heads/main/thumbs-down-black-icon.webp'
    app.likeImgW, app.likeImgH = getImageSize(app.likeUrl)
    app.dislikeImgW, app.dislikeImgH = getImageSize(app.dislikeUrl)
    likePIL = loadPilImage(app.likeUrl)
    dislikePIL = loadPilImage(app.dislikeUrl)
    app.likeImg = CMUImage(likePIL)
    app.dislikeImg = CMUImage(dislikePIL)

    app.likecx, app.likecy = app.width - 45, app.height/2 + 45
    app.dislikecx, app.dislikecy = app.width -45 , app.height/2 + 115
    app.buttonr = 30
    app.topic1 = app.topicKeys[app.feed1Indx]
    app.topic2 = app.topicKeys[app.feed2Indx]
    app.currentTopic = app.topic1


##########################################################################################
########################## Intro Screen Starts Here ######################################
##########################################################################################

# Reset helper function
def reset_introScreen(app):
    # Variables for intro screen
    app.username = None
    app.sigma = 'https://github.com/alanpham06/exceed-TH2025/blob/main/Note_Feb_7__2025__3_-removebg-preview.png?raw=true'
    app.buttonCx = app.width//2
    app.buttonCy = app.height-(app.height//3)
    app.buttonW = 380
    app.buttonH = 75
    app.xW = 150
    app.xH = 50
    app.colors = ['ghostWhite','azure','ivory','floralWhite','aliceBlue','lavenderBlush', 
                  'seashell', 'honeydew', 'whiteSmoke', 'oldLace', 'linen', 'beige', 'antiqueWhite']
    app.screenColor = app.colors[random.randrange(len(app.colors))]
    app.fsize = 20


def intro_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill=app.screenColor)
    drawLabel('Exceed', app.width//2, app.height//8, fill='black',
                size=50, font='monospace', bold=True)
    drawImage(app.sigma, app.width//2, app.height//2.25, width=300, height=400, align='center')

    if (app.username == None):
        drawRect(app.buttonCx, app.buttonCy, app.buttonW, app.buttonH, fill='snow', border=None, 
             opacity=80, align='center')
        drawLabel('Login to your account', app.buttonCx, app.buttonCy, fill='black',
                size=20, font='monospace', bold=True)
    else:
        drawRect(app.buttonCx, app.buttonCy, app.buttonW, app.buttonH, fill='mintCream', 
                 border=None, opacity=80, align='center')
        drawLabel(f"Welcome to Exceed, {app.username}!", app.buttonCx, app.buttonCy, 
                  fill='black', size=app.fsize, font='monospace', bold=True)
        drawRect(app.buttonCx, app.buttonCy+100, app.xW, app.xH, fill='mintCream', 
                 border='black', opacity=80, align='center')
        drawLabel('->', app.buttonCx, app.buttonCy+100, fill='black',
                size=40, font='monospace', bold=True)
        drawRect(app.buttonCx, app.buttonCy+175, app.xW, app.xH, fill='mistyRose', 
                 border='black', opacity=80, align='center')
        drawLabel('x', app.buttonCx, app.buttonCy+175, fill='black',
                size=40, font='monospace', bold=True)


def intro_onMousePress(app, mouseX, mouseY):
    # Checks if user wants to log in
    if ((mouseX > (app.buttonCx-(app.buttonW//2))) and (mouseX < (app.buttonCx+(app.buttonW//2))) 
        and (mouseY < (app.buttonCy+(app.buttonH//2))) and (mouseY > (app.buttonCy-(app.buttonH//2)))):
        app.username = app.getTextInput('Please Enter Your Username:')
        app.user = app.username
        if len(app.username) >= 20:
            app.fsize = 14
        elif len(app.username) >= 30:
            app.fsize = 10
            

    # Checks if user wants to redo login
    if ((mouseX > (app.buttonCx-(app.xW//2))) and (mouseX < (app.buttonCx+(app.xW//2))) 
        and (mouseY < (app.buttonCy+100+(app.xH//2))) and (mouseY > (app.buttonCy+100-(app.xH//2)))):
        app.feed1List = app.topics[random.randint(0, len(app.topics)-1)]
        app.feed2List = app.topics[random.randint(0, len(app.topics)-1)]
        app.text1 = app.feed1List[random.randint(0, len(app.feed1List)-1)]
        app.text2 = app.feed2List[random.randint(0, len(app.feed2List)-1)]
        setActiveScreen('feed')
    if ((mouseX > (app.buttonCx-(app.xW//2))) and (mouseX < (app.buttonCx+(app.xW//2))) 
        and (mouseY < (app.buttonCy+175+(app.xH//2))) and (mouseY > (app.buttonCy+175-(app.xH//2)))):
        reset_introScreen(app)


##########################################################################################
########################### Intro Screen Ends Here #######################################
##########################################################################################

##########################################################################################
########################### Feed Screen Starts Here ######################################
##########################################################################################

def feed_redrawAll(app):

    # Feed Scrolling
    drawRect(app.feed1X, app.feed1Pos, app.fd1W, app.fd1H, fill='white', opacity=75)
    i = 0
    for substr1 in app.text1.split('\n'):
        drawLabel(substr1, app.fd1LabelX, app.fd1LabelY+i, size=18)
        i += 20
    drawRect(app.feed2X, app.feed2Pos, app.fd2W, app.fd2H, fill='gainsboro', opacity=70)
    j = 0
    for substr2 in app.text2.split('\n'):
        drawLabel(substr2, app.fd2LabelX, app.fd2LabelY+j, size=18)
        j += 20

    # Feed Screen Labels
    drawRect(app.width//2, 0, 500, 250, fill='skyBlue', align='center')
    drawLabel(f'{app.user}', app.width/2, 20, size = 30, bold=True)
    if app.currentTopic == app.topic1:
        drawLabel(f'{app.topic1} likes: {app.topicLikeDict[app.topic1]}', app.width/2, 50, size = 20) 
        drawLabel(f'{app.topic1} dislikes: {app.topicDislikeDict[app.topic1]}', app.width/2, 70, size = 20)
    else:
        drawLabel(f'{app.topic2} likes: {app.topicLikeDict[app.topic2]}', app.width/2, 50, size = 20) 
        drawLabel(f'{app.topic2} dislikes: {app.topicDislikeDict[app.topic2]}', app.width/2, 70, size = 20)

    # Draw like/dislike button
    drawCircle(app.likecx, app.likecy, app.buttonr, border = "black", fill = 'green')
    drawCircle(app.dislikecx, app.dislikecy, app.buttonr, border = "black", fill = 'red')
    drawImage(app.likeImg, app.likecx, app.likecy, width = app.likeImgW/15, 
              height = app.likeImgH/15, align='center')
    drawImage(app.dislikeImg, app.dislikecx, app.dislikecy, width = app.dislikeImgW/15, 
              height = app.dislikeImgH/15, align='center')
    

def feed_onKeyHold(app, keys):
    if ('up' in keys):
        app.feed1Pos -= 30
        app.feed2Pos -= 30
        app.fd1LabelY -= 30
        app.fd2LabelY -= 30

    app.feed1Low = app.feed1Pos+app.fd1H
    app.feed2Low = app.feed2Pos+app.fd2H
    if (app.feed1Low <= 150):
        app.feed1Pos = (950 - (150-(app.feed1Low)))
        app.fd1LabelY = app.fd2LabelY + app.fd1H
        app.feed1List = app.topics[app.feed1Indx]
        app.text1 = app.feed1List[random.randint(0, len(app.feed1List)-1)]
    elif (app.feed2Low <= 150):
        app.feed2Pos = (950 - (150-app.feed2Low))
        app.fd2LabelY = app.fd1LabelY + app.fd2H
        app.feed2List = app.topics[app.feed2Indx]
        app.text2 = app.feed2List[random.randint(0, len(app.feed2List)-1)]

    if (app.fd1LabelY <= 50):
        app.feed1Indx = (random.randint(0, len(app.topics)-1))
    elif (app.fd2LabelY <= 50):
        app.feed2Indx = (random.randint(0, len(app.topics)-1))

    
def feed_onMousePress(app, mouseX, mouseY):
    # check if user pressed like button 
    if (distance(mouseX, mouseY, app.likecx, app.likecy) < app.buttonr):
        app.likes += 1
        if (app.fd1LabelY > 150 and app.fd1LabelY < 800):
            app.topic1 = app.topicKeys[app.feed1Indx]
            app.topicLikeDict[app.topic1] += 1
            app.currentTopic = app.topic1
        elif (app.fd2LabelY > 150 and app.fd2LabelY < 800):
            app.topic2 = app.topicKeys[app.feed2Indx]
            app.topicLikeDict[app.topic2] += 1
            app.currentTopic = app.topic2

    if (distance(mouseX, mouseY, app.dislikecx, app.dislikecy) < app.buttonr):
        app.dislikes += 1
        if (app.fd1LabelY > 200 and app.fd1LabelY < 600):
            app.topic1 = app.topicKeys[app.feed1Indx]
            app.topicDislikeDict[app.topic1] += 1
            app.currentTopic = app.topic1
        elif (app.fd2LabelY > 200 and app.fd2LabelY < 600):
            app.topic2 = app.topicKeys[app.feed2Indx]
            app.topicDislikeDict[app.topic2] += 1
            app.currentTopic = app.topic2


##########################################################################################
############################ Feed Screen Ends Here #######################################
##########################################################################################


def main():
    runAppWithScreens(initialScreen='intro', width=500, height=800)

main()
