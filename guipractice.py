import PySimpleGUI as sg
import random

#code for the art prompt generator

job = """
actress
actor
architect
singer
dentist 
detective 
writer
farmer
nurse
pilot
engineer
accountant
butcher
cashier
barber
carpenter
lifeguard
baker
electrician
flight attendant
plumber
receptionist
researcher
scientist
lawyer
bus driver
designer
journalist
photographer
musician
painter
florist
sales-assistant
mechanic
model
shop-assistant 
politician
translator
postman
hairdresser
taxi driver
pharmacist
nanny
travel agent
cleaner
biologist
businesswoman
businessman 
dancer 
gardener
meteorologist
programmer
travel guide 
saleswoman 
salesman
superhero
supervillain
chef
"""
jobList = job.split()
jobIndex = len(jobList)


settings = """ABANDONED-MINE

AIRPLANE

AIRPORT

ALLEY

AMBULANCE

AMUSEMENT-PARK

ANCIENT-RUINS

ANTIQUES-SHOP

ARCHERY-RANGE

ARCTIC-TUNDRA 

ART-GALLERY

ART-STUDIO

ATTIC

BACKYARD

BADLANDS

BAKERY

BALLROOM

BANK

BAR 

BARN

BASEMENT

BAZAAR

BEACH

BEACH-PARTY

BIG-CITY-STREET

BIRTHDAY-PARTY

BLACK-TIE-EVENT

BLOCK-PARTY

BOARDING-SCHOOL

BOARDROOM

BOMB-SHELTER

BOOKSTORE

BOWLING-ALLEY

BREAKROOM

BREWERY

BRIDGE

CAMPSITE

CANYON


CAR-WASH

CARNIVAL-FUNHOUSE

CASINO

CASUAL-DINING-RESTAURANT

CAVE

CHEAP-MOTEL

CHICKEN-COOP

CHILD'S-BEDROOM

CHURCH

CIRCUS

CITY-BUS

COFFEEHOUSE

COMMUNITY-CENTER

CONDEMNED-APARTMENT-BUILDING

CONSTRUCTION-SITE

CONVENIENCE-STORE

COUNTRY-ROAD

COUNTY-FAIR

COURTROOM

CREEK

CRUISE-SHIP

CUSTODIAL-SUPPLY-ROOM

DELI

DESERT

DINER

DORM-ROOM

DUNGEON 

ELEMENTARY-SCHOOL-CLASSROOM

ELEVATOR

EMERGENCY-ROOM

EMPTY-LOT

EXECUTIVE'S-OFFICE

FACTORY

FARM

FARMER'S-MARKET

FAST-FOOD-RESTAURANT

FIRE-STATION

FISHING-BOAT

FITNESS-CENTER

FLOWER-GARDEN

FLOWER-SHOP

FOREST

FUNERAL-HOME

GALLOWS 

GARAGE

GARAGE-SALE

GAS-STATION

GHOST-TOWN 

GOLF-COURSE

GRAVEYARD 

GREEN-ROOM

GREENHOUSE

GROCERY-STORE

GROTTO

GROUP-FOSTER-HOME

GYMNASIUM

HAIR-SALON

HALLOWEEN-PARTY

HARDWARE-STORE

HAUNTED-HOUSE 

HERBALIST'S-SHOP 

HIGH-SCHOOL-CAFETERIA

HIGH-SCHOOL-HALLWAY

HIKING-TRAIL

HOME-OFFICE

HOMELESS-SHELTER

HOSPITAL 

HOT SPRINGS

HOTEL-ROOM

HOUSE-FIRE

HOUSE-PARTY

HUNTING-CABIN

ICE-CREAM-PARLOR

INDOOR-SHOOTING-RANGE

JEWELRY-STORE

JUDGE'S-CHAMBERS

JUVENILE-DETENTION-CENTER

KITCHEN

LAKE

LANDFILL

LAUNDROMAT

LIBRARY

LIGHTHOUSE

LIMOUSINE

LIQUOR-STORE

LIVING-ROOM

MAN-CAVE

MANSION

MARINA

MARSH

MAUSOLEUM

MEADOW

MECHANIC'S-SHOP

MEDIEVAL-CASTLE 

MEDIEVAL-CASTLE-ARMORY 

MEDIEVAL-TAVERN 

MEDIEVAL-VILLAGE 

MILITARY-BASE

MILITARY-HELICOPTER

MOORS

MORGUE

MOTOR-HOME

MOUNTAINS

MOVIE-SET

MOVIE-THEATER

MUSEUM

NEWSROOM

NIGHTCLUB

NURSERY

NURSING-HOME

OCEAN

OFFICE-CUBICLE

OLD-PICK-UP-TRUCK

ORCHARD

OUTDOOR-POOL

OUTDOOR-SKATING-RINK

OUTHOUSE

PARADE

PARK

PARKING-GARAGE

PARKING-LOT

PASTURE

PATIO-DECK

PAWN-SHOP

PENTHOUSE-SUITE

PERFORMING-ARTS-THEATER

PET-STORE

PHARMACY

PHOTOGRAPHY-STUDIO

PIRATE-SHIP

PLAYGROUND

POLICE-CAR

POLICE-STATION

POND

POOL

PRESCHOOL

PRINCIPAL'S-OFFICE

PRISON-CELL 

PROM

PSYCHIATRIC-WARD

PSYCHIC'S-SHOP

PUB

PUBLIC-RESTROOM

QUARRY

RACE TRACK 

RAINFOREST

RANCH

RAZED-CITY-STREET

REC-CENTER

RECORDING-STUDIO

REFUGEE-CAMP

RESIDENTIAL-BATHROOM

RIVER

ROCK-CONCERT

RODEO

ROOT-CELLAR

RUN-DOWN-APARTMENT

SALVAGE-YARD

SCHOOL-BUS

SCHOOL-LOCKER-ROOM

SCIENCE-LAB

SECRET-PASSAGEWAY

SEWERS

SHOPPING-MALL

SKATE-PARK

SKI-RESORT

SLAUGHTERHOUSE

SMALL-TOWN-STREET

SPA

SPORTING-EVENT-STANDS

SUBMARINE

SUBWAY-TRAIN

SUBWAY-TUNNEL

SUMMER-CAMP

SWAMP

TANK

TATTOO-PARLOR

TAXI

TAXIDERMIST

TEACHER'S-LOUNGE

TEENAGER'S-BEDROOM


THERAPIST'S-OFFICE

THRIFT-STORE

TOOL-SHED

TRADE-SHOW

TRAILER-PARK

TRAIN-STATION

TREE-HOUSE

TRENDY-STORE

TROPICAL-ISLAND

TROPICAL-RESORT

TRUCK-STOP

UNDERGROUND-STORM-SHELTER

UNDERPASS

UNIVERSITY-LECTURE-HALL

UNIVERSITY-QUAD

UPSCALE-HOTEL-LOBBY

URBAN-ROOFTOP

USED-CAR-DEALERSHIP

VEGAS-STAGE-SHOW

VEGETABLE-PATCH

VET-CLINIC

VIDEO-ARCADE

WAITING-ROOM

WAKE

WATERPARK

WATERFALL

WEDDING-RECEPTION

WINE-CELLAR

WINERY

WORKSHOP

YACHT

ZOO"""

settingsList = settings.split()
settingsIndex = len(settingsList)



emotes = """
pleasure
joy
happiness
amusement
pride
awe
excitement
ecstasy
lonely
unhappy
hopeless
gloomy
miserable
worried
nervous
anxious
scared
panicked 
stressed
annoyed
frustrated
bitter
infuriated
mad
insulted
vengeful
dislike
revulsion
nauseated
aversion
offended
horrified
pleased
content
relaxed
calm
acceptance
admiration
adoration
affection
afraid
agitation
agony
aggressive
alarm
alarmed
alienation
amazement
ambivalence
amusement
anger
anguish
annoyed
anticipating
anxious
apathy
apprehension
arrogant
assertive
astonished
attentiveness
attraction
aversion
awe
baffled
bewildered
bitter
bitter-sweetness
bliss
bored
brazen
brooding
calm
carefree
careless
caring
charity
cheeky
cheerfulness
claustrophobic
coercive
comfortable
confident
confusion
contempt
content
courage
cowardly
cruelty
curiosity
cynicism
dazed
dejection
delighted
demoralized
depressed
desire
despair
determined
disappointment
disbelief
discombobulated
discomfort
discontentment
disgruntled
disgust
disheartened
dislike
dismay
disoriented
dispirited
displeasure
distraction
distress
disturbed
dominant
doubt
dread
driven
dumbstruck
eagerness
ecstasy
elation
embarrassment
empathy
enchanted
enjoyment
enlightened
ennui
enthusiasm
envy
epiphany
euphoria
exasperated
excitement
expectancy
fascination
fear
flakey
focused
fondness
friendliness
fright
frustrated
fury
glee
gloomy
glumness
gratitude
greed
grief
grouchiness
grumpiness
guilt
happiness
hate
hatred
helpless
homesickness
hope
hopeless
horrified
hospitable
humiliation
humility
hurt
hysteria
idleness
impatient
indifference
indignant
infatuation
infuriated
insecurity
insightful
insulted
interest
intrigued
irritated
isolated
jealousy
joviality
joy
jubilation
kind
lazy
liking
loathing
lonely
longing
loopy
love
lust
mad
melancholy
miserable
miserliness
mixed up
modesty
moody
mortified
mystified
nasty
nauseated
negative
neglect
nervous
nostalgic
numb
obstinate
offended
optimistic
outrage
overwhelmed
panicked
paranoid
passion
patience
pensiveness
perplexed
persevering
pessimism
pity
pleased
pleasure
politeness
positive
possessive
powerless
pride
puzzled
rage
rash
rattled
regret
rejected
relaxed
relieved
reluctant
remorse
resentment
resignation
restlessness
revulsion
ruthless
sadness
satisfaction
scared
schadenfreude
scorn
self-caring
self-compassionate
self-confident
self-conscious
self-critical
self-loathing
self-motivated
self-pity
self-respecting
self-understanding
sentimentality
serenity
shame
shameless
shocked
smug
sorrow
spite
stressed
strong
stubborn
stuck
submissive
suffering
sullenness
surprise
suspense
suspicious
sympathy
tenderness
tension
terror
thankfulness
thrilled
tired
tolerance
torment
triumphant
troubled
trust
uncertainty
undermined
uneasiness
unhappy
unnerved
unsettled
unsure
upset
vengeful
vicious
vigilance
vulnerable
weak
woe
worried
worthy
wrath"""

job = """
actress
actor
architect
singer
dentist 
detective 
writer
farmer
nurse
pilot
engineer
accountant
butcher
cashier
barber
carpenter
lifeguard
baker
electrician
flight attendant
plumber
receptionist
researcher
scientist
lawyer
bus driver
designer
journalist
photographer
musician
painter
florist
sales-assistant
mechanic
model
shop-assistant 
politician
translator
postman
hairdresser
taxi driver
pharmacist
nanny
travel agent
cleaner
biologist
businesswoman
businessman 
dancer 
gardener
meteorologist
programmer
travel guide 
saleswoman 
salesman
superhero
supervillain
chef
"""

emotesList = emotes.split()
emotesIndex = len(emotesList)



animals = """
Dog
Puppy
Turtle
Rabbit
Parrot
Cat
Kitten
Goldfish
Mouse
Tropical-fish
Hamster
Cow
Rabbit
Ducks
Shrimp
Pig
Goat
Crab
Deer
Bee
Sheep
Fish
Turkey
Dove
Chicken
Horse
Crow
Peacock
Dove
Sparrow
Goose
Stork
Pigeon
Turkey
Hawk
Bald-eagle
Raven
Parrot
Flamingo
Seagull
Ostrich
Swallow
Black-bird
Penguin
Robin
Swan
Owl
Woodpecker
Giraffe
Woodpecker
Camel
Starfish
Koala
Alligator
Owl
Tiger
Bear
Blue whale
Coyote
Chimpanzee
Raccoon
Lion
Arctic wolf
Crocodile
Dolphin
Elephant
Squirrel
Snake
Kangaroo
Hippopotamus
Elk
Fox
Gorilla
Bat
Hare
Toad
Frog
Deer
Rat
Badger
Lizard
Mole
Hedgehog
Otter
Reindeer
Crab
Fish
Seal
Octopus
Shark
Seahorse
Walrus
Starfish
Whale
Penguin
Jellyfish
Squid
Lobster
Pelican
Clams
Seagull
Dolphin"""

animalsList = animals.split()
animalsIndex = len(animalsList)


#start of PySimpleGUI Code

# Define the window's contents
layout = [[sg.Text("Welcome to Art Prompt Generator. Please choose an option name:")],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button("Occupation"), sg.Button("Setting"), sg.Button("Expression"), sg.Button("Animal")],
          [sg.Button('Quit')]]

# Create the window
window = sg.Window('Art Prompt Generator', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == "Occupation":
        jobRand = random.randint(0, jobIndex-1) 
        window["-OUTPUT-"].update("Your job is: " + jobList[jobRand], text_color = "blue")
    elif event == "Setting":
        settingRand = random.randint(0, settingsIndex-1) 
        window["-OUTPUT-"].update("Your setting is: " + settingsList[settingRand].lower(), text_color = "pink")
    elif event == "Expression":
        emotesRand = random.randint(0,emotesIndex-1)
        window["-OUTPUT-"].update("Your expression is: " + emotesList[emotesRand], text_color = "orange")
    elif event == "Animal":
       animalRand = random.randint(0, animalsIndex-1)
       window["-OUTPUT-"].update("Your animal is: " + animalsList[animalRand].lower(), text_color = "purple") 

# Finish up by removing from the screen
window.close()