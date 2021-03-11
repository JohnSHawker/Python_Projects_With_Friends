#v0.8 Pinterdale. 

#Time is imported to delay repeated text from looping automatically.
import time


print('')
print ('"Pinterdale" was written and created by Kameron Squire\nSome branches of the story are not yet complete, but hopefully you can enjoy the early access version before you.')
print('')

#Although it is not used more than once or twice the character is written so that they can be anybody. 
user_name = input("Please type your character's name: ").capitalize()


#Title and Instructions
#Each definition has both available choices in it so you can easily track what decisions go where. The pairing is determined based off the choices in the stories text.
print('''Welcome to "Pinterdale"''',user_name,'''!

This is a "Choose Your Own Adventure" Thriller/Horror game where you just type one of the CAPITALIZED words to choose how your story unfurls.
You may type QUIT at any time to close the game. There may be a secret ending not given with capitalized letters, if you learn the mystery surrounding "Pinterdale 
type out what you learn and you might find all might not be locked between two choices.
Good Luck!''')
print ('''
''')

#the .lower().strip() at the end of each input makes sure that all answers are automatically lowercase as well as being correct even if you accidently add spaces to the word.
def gas_drive():
    decision = str(input('You have been driving for what seems an eternity when you finally enter into a small town called Pinterdale. \
Your car has about a quarter tank of gas and even though you feel like you have a lot of traveling left to do before the night is through. \
You are trying to decide if you should get GAS now or DRIVE to the next town before deciding to fill up.\n').lower().strip())

    if decision == 'gas':
        print('You pull up to the gas station. The light above the fuel pump blinks rhythmically on and off giving the place an eerie vibe \
as it repeatedly casts your surroundings in darkness before briefly illuminating your surroundings once again. \
Do you pay at the PUMP or do you go in the gas station and pay the CASHIER?')
        pump_cashier()

    elif  decision == 'drive':
        print('The gas station seems to have a broken light that blinks on and off. \
It hurts your eyes looking at it, beside you decide that a quarter of a tank is still plenty, and you rush on through down the road. \
You continue to drive but realize that you have become lost. The gas gauge slowly hovers over empty before your car putters to the side of the road. \
There is a sign for the next TOWN just a few miles away, but you can also see a LIGHT not too far from the road.')
        town_light()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    elif decision == 'quit':
        quit()

#sleep timer added to each else statement so that the user doesn't lose the command to type one word or another before the previously displayed text repeats itself
# else statements paired with definition to create loops. This stops the program from crashing when spelling errors or unavailable choices are submitted.      
    else:
        print('Please type either GAS or DRIVE')
        time.sleep (2)
        gas_drive()

        
        
def pump_cashier():
    decision = input('').lower().strip()
    if decision == 'pump':
        print('You ignore the flashing light as you start pumping your car. An old pickup pulls up to the pump next to you. \
A slightly balding man with greasy food stains smattered across his flannel shirt rolls out and start filling up his vehicle. \
He smiles at you. His mouth dripping darkened tobacco filled saliva down his chin. \
He seems friendly enough you could TALK to him or just get in your CAR now that it is done filling up.')
        talk_car()

    elif  decision == 'cashier':
        print('You hurry into the gas station to find a young girl in her teens hunched behind the counter. \
The phone in her hands casting its blue light off the many freckles covering her skin. “Excuse me,” you say. \n    Startled, the girl jumps up and faces you. “Wha-, oh. \
You startled me. We don’t normally get customers after dinnertime. What can I do for?” \
Her words tumble quickly from her lips as she brushes her clothes nervously.\n    “Just some gas on pump…” \
you glance out the window to check the number and see an old pickup pull up under the strobing fluorescent lighting. \
“Pump 1 please.”\n    “Sure thing. Anything else?”\n    “I’m ok. \
Thanks.”\n    You head back out to see the owner of the pickup has rolled out of his car, a hairy stomach poking out of his stained flannel shirt. \
You can feel his eyes on you and think he wants to SAY something, but you are in a hurry to just fill up and GO.')
        say_go()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()
  
    else:
        print('Please type either PUMP or CASHIER')
        time.sleep (2)
        pump_cashier()



def town_light():
    decision = input('').lower().strip()
    if decision == 'town':
        print('You decide not to risk an encounter out in the middle of nowhere and would feel much safer just bucking up and walking to town. \
As you start the walk you hope that the gas station sells gas cans because \
you don’t have anything on hand to bring the gas back.\n    It is pitch black, and you don’t have anything to light your way. \
You hear a noise off the road but think you can see a flickering light in the distance. \
Do you want to INVESTIGATE the noise, or continue down the ROAD to what you hope is the next town over?')
        investigate_road()
    
    elif decision == 'light':
        print('The light seems much closer, and you don’t have a gas can. You walk up a dusty trail when you come upon a cozy looking cabin. \
You knock softly on the white painted door. It was left slightly ajar, so your knocking causes the door to swing quietly open. \
“Hello…?” you call out, but nobody responds. You walk in the cabin. The main room seems bare except for a stool placed near the fireplace. \
A chandelier of antlers hangs from the ceiling, and a large fur rug is sprawled out across the creaky floor.\n    “Excuse me…. Your door sort of came open. Anybody home?” \
you head to the back of the cabin where you find a wardrobe, and a bed covered in blankets. \
The whole place smells a little like old people. There is nobody home. \
Do you want to LOOK for someone out back or SEARCH the cabin for something you can use to hold gas?')
        look_search()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either TOWN or LIGHT')
        time.sleep (2)
        town_light()


def talk_car():
    decision = input('').lower().strip()
    if decision == 'talk':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'car':
        print('(What a slob,) you think to yourself as you get in the car. \
His greasy demeanor makes you want to take a shower. You feel his eyes on you as you pull out of the flashing canopy and on to the street. \
You take off down the winding mountain highway at speeds that are probably a little unsafe, but at least you are away from the dirty local. \
You  have only been driving about fifteen minutes when you see a dark plume of smoke behind you in the last of the evening’s light. \
Not long after you notice the smoke you see the old pickup barreling toward you. You glance down at the speedometer, \
at the speed you’re going there is no way that beat up junker could be gaining on you but it is. \
Do you STOP and confront the persistent man or crank up the SPEED and try to lose him?')
        stop_speed()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either TALK or CAR')
        time.sleep (2)
        talk_car()



def stop_speed():
    decision = input('').lower().strip()
    if decision == 'stop':
        print ('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'speed':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either STOP or SPEED')
        time.sleep (2)
        stop_speed()



def say_go():
    decision = input('').lower().strip()
    if decision == 'say':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'go':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either SAY or GO')
        time.sleep (2)
        say_go()



def look_break():
    decision = input('').lower().strip()
    if decision == 'look':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'break':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either LOOK or BREAK')
        time.sleep (2)
        look_break()



def investigate_road():
    decision = input('').lower().strip()
    if decision == 'investigate':
        print('You go towards the noise hoping it is someone that can light your way. \
You hear growling and snorting. Maybe you made a mistake. \
You begin running away from the noise back to where you think the road is, but you get turned around. \
The area around you goes silent. All you can hear now is the wind whistling through the trees. \
You head towards what you hope is the road when you hear a loud Snap. \
You cry out in anguish when you feel the teeth of a bear trap as it snaps closed around your leg. \
You try ripping your leg out but it only makes the gashes in your leg deeper. Blood is steadily gushing down your leg. \
You hear the growling again, and it is closer. You are stuck. A giant bear comes toward you. It doesn’t look happy to see you. \
It stands on its hind legs and roars menacingly at you. All you can really make out is it’s outline as the sky darkens more.\n    You try to wrench the trap open, \
but you are stuck. You try to pull the trap from the ground so you can at least try to get away, but your strength is quickly failing. \
The bear sinks it’s teeth into your shoulder as it shakes you back and forth like a rag doll before tossing you to the side. \
The shaking rips you free from the trap. A bloody stump is all that remains. You can barely breathe as blood pools beneath you from your multiple cuts. \
Tears leak from your eyes as you PASS out.')
        Pass()

    elif decision == 'road':
        print('Of course you don’t want to investigate the noise. \
You didn’t want to investigate the light either. No need to have a run in with a bear tonight. \
You pick up your pace and start briskly walking, almost jogging towards the light. \
The road curves until you finally see the next town in view. The flickering light you have been following comes from a gas station. \
Does every gas station out in the middle of nowhere have to have a broken light? You wonder as you get closer. \
You notice four guys and a girl leaning up against some motorcycles, smoking in the parking lot and talking loudly to each other. \
It looks like they have a gas can sitting next to their bikes that you can ask to BORROW, or do you feel more comfortable ENTERING the gas station to ask the cashier?')
        borrow_entering()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either INVESTIGATE or ROAD')
        time.sleep (2)
        investigate_road()



def borrow_entering():
    decision = input('').lower().strip()
    if decision == 'borrow':
        print('You figure there is no harm in asking, but as soon as you approach all five of the smokers faces darken. \
“Hey! I was passing through when I ran out of gas. My car is back that way a couple miles. \
Do you mind letting me borrow your gas can so that I can get it back up and running?”\n    Five sets of eyes just stare at you. \
The silence is awkward. You are close enough that you could just GRAB the gas can or you can ASK again. \
You might be better off just ENTERING the gas station to ask the cashier.')
        grab_ask()

    elif decision == 'entering':
        print ('You don’t know what you are interrupting when you stumbled across the gang outside, \
so you choose to just walk into the gas station in hopes that there is a more welcoming person inside. \
You look around the register but don’t see anyone. Perhaps the person working here is stocking or something. \
You look around the gas station, but it seems deserted. You figure that you can at least look to see if they sell gas cans. \
You find them and walk back up to the cash register. Revving engines make you glance outside in time to see the bikers shoot off down the road. \
No one is appearing, you could just TAKE the gas can and fill it up at the pump outside, \
or you could PEEK behind the ‘Employees only’ door to see if someone is around.')
        take_peek()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either BORROW or ENTERING')
        time.sleep (2)
        borrow_entering()



def take_peek():
    decision = input('').lower().strip()
    if decision == 'take':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'peek':
        print ('You peek inside the ‘Employees only’ door and find a young woman with light red hair pulling keys out of a locker. \
Her back is turned and she doesn’t see you. You open your mouth, “Excuse me,” you say.\n    She flips around to face you. \
You can see her jump as she hears your voice. Wide eyes stare at you. \
Silent she looks at you as if trying to figure out what is going on, how had you invaded her domain? \
When the silence has dragged on long enough to get awkward you open your mouth to break it, \
but she seems to have composed herself enough for a torrent to pour out of her.\n    “Gave me a fright you did. How did you get in here? \
I swear I locked the door. Didn’t you know we are closed? Only the pumps are 24 hours. Were you spying on me? \
I can see outside from here, where is your car? Did you walk here? Don’t you know it isn’t polite to just come to the back room. \
I…..” she realizes she is ranting, and needs to give you time to answer before she bombards you with more question, \
“What is it?”\n    “I just wanted to buy a gas can. My car ran out of gas just out of town and I was hoping to carry some back \
to my car so that I had enough to drive here and fill up the rest of the way.”\n    “I’m sorry. \
The inside is already closed. The register has been shut down. I can’t ring you up for the can. \
I could give you a RIDE if you need, or there is a HOTEL just one street away that Mr. Stowers runs. \
It isn’t the nicest place, but he doesn’t charge much and you can get all sorted out in the morning.”')
        ride_hotel()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either TAKE or PEEK')
        time.sleep (2)
        take_peek()



def ride_hotel():
    decision = input ('').lower().strip()
    if decision == 'ride':
        print ('You smile at her. “I could use a ride back to my car if you don’t mind. You can call me', user_name,'. I really appreciate it.”\n    “I’m \
sorry I can’t get gas in your car, and I am forcing you to wait until tomorrow (user_name). I am Marci by the way. I am parked out back, \
I am actually a little glad for the company. Not long ago there was a bit of an ordeal here in Pinterdale and even though that all seems to be \
cleared up it just doesn’t feel safe anymore.”\n    You nod your head, not really knowing how to respond to Marci, \
and follow her to a silver car in the back. She pulls off down the road and with your guidance starts heading toward where you car broke down. \
It isn’t long before she pulls up behind your car. You thank her for the ride and you fumble with your keys so that you can just get \
in and sleep in your car until morning. Your keys fall from your hand and bounce down the mountainous hill to the side of your car. \
Grumbling, you strategically slide down after your keys. When you head back up the road Marci’s silver car is still parked behind your car, \
but she is no longer inside it. The car idles softly, no Marci in sight. You shout her name, but it is as if she vanished into thin air. \
You hear a noise back down where you drop your keys. Maybe Marci followed you when you dropped them. \
Do you want to check to see if the noise is MARCI or do you take advantage of her empty vehicle and help yourself, \
because it isn’t really STEALING if she left it for you right?')
        stealing_marci()

    elif decision == 'hotel':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either RIDE or HOTEL')
        time.sleep (2)
        ride_hotel()



def stealing_marci():
    decision = input ('').lower().strip()
    if decision == 'stealing':
        print ('You climb in the car and take off down the highway. You are pleasantly surprised to see that the gas gauge is near full. \
You drive for while when you pass a sign that reads, “Welcome to Pinterdale”. Confused you keep driving for a bit until you see a gas station. \
The broken lighting flickering on and off above the pumps. You pull over the car. Did you get turned around after stealing the car? \
There were no other roads to turn off of. Your tank is a little over half full, so you don’t need gas, \
but do you want to drive BACK the way you came from in your silver car or continue in the SAME direction you have been traveling?')
        back_same()
        
    elif decision == 'marci':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either STEALING or MARCI')
        time.sleep (2)
        stealing_marci()



def grab_ask():
    decision = input('').lower().strip()
    if decision == 'grab':
        print ('You grab the gas can and you dash off. \
The quick glance you get of the astounded faces was almost worth it. \
As you run you notice that the can is full so you don’t even need to figure out how you are going to fill it up.\n    The shock \
must have worn off the bikers because you can hear the rev of their motorcycles turning on. You shoot off into the trees. \
Zigzagging to try to be unpredictable. It isn’t long until you hear the sound of running water. \
The humming of the motorcycles has been drowned out by the insects. You almost cross into the river; \
it appears so suddenly before you. Do you follow the RIVER or try to make your way back to the STREET?')
        river_street()

    elif decision == 'ask':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'entering':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either GRAB or ASK')
        time.sleep (2)
        grab_ask()



def river_street():
    decision = input('').lower().strip()
    if decision == 'river':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued()

    elif decision == 'street':
        print ('You try to find your way back to the street so you can take the gas can to your car. \
With all the zigzagging you did you are a little confused as to what direction you took. \
The gas can is heavy against your sweating palm. You keep switching hands to keep your shoulders from cramping under the weight. \
You strain your senses to try and hear or see anything in the pines that almost seem to loom menacingly over you. \
You might hear a soft sound to your LEFT but at the same time you feel like you can almost see headlights to the RIGHT.')
        left_right()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either RIVER or STREET')
        time.sleep (2)
        river_street()



def left_right():
    decision = input('').lower().strip()
    if decision == 'left':
        print ('As you head left you can once again hear the faint sound of vehicles in the distance. \
You come out of the trees onto the road. You were so lost you can actually see your car in the distance. \
You have almost made it! The gas sloshes in the can as you pick up your pace. \
When you arrive at your car you waste no time opening the gas cap and feeding the car your prize. \
You toss the gas can aside and fumble for your keys. In your excitement you drop them. \
That is when you see the large gashes running up and down your tires. \
You start to glance around when something HARD hits you in the back of the head and your vision goes dark. ')
        hard()

    elif decision == 'right':
        print ('It wasn’t headlights at all. There is a light on in what appears to be a solitary cabin. \
You approach it quietly and set the gas can down near the front entrance. You lightly knock on the peeling white door. \
Chips of paint float lazily down as you try knocking again. “Anyone home?” you speak, \
not wanting to shout but still wanting to be heard.\n    When nobody answers you try the doorknob. \
It’s locked. You think you can BREAK the window on the door to let yourself in. You could also LOOK to see if anyone is around back.')
        look_break()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either LEFT or RIGHT')
        time.sleep (2)
        left_right()



def hard():
    decision = input('').lower().strip()
    if decision == 'hard':
        print('THIS PATH TO BE CONTINUED....THANK YOU FOR PLAYING AND TRY OTHER CHOICES TO SEE WHERE THE STORY MIGHT GO!')
        to_be_continued() 

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('That is what you get for not checking your car! Now type HARD!')



def look_search():
    decision = input('').lower().strip()
    if decision == 'look':
        print ('')

    elif decision == 'search':
        print('You look around, starting with the wardrobe. \
A dark flash darts past you as you open the door. A startled squeal escapes your lips. \
Your heart is pounding with adrenaline as you frantically look to see what almost had you. \
Then you see the largest rat you have ever laid eyes upon as it scampers out from under the bed. \
You run to the main room only to trip on the massive fur rug in your rush to escape. \
The mouse shoots past you and out the open front door. As you get back up you notice there is a door that had been covered by the rug. \
Do you want to OPEN it? There is no telling what could be down there. \
You could try looking in the WARDROBE now that it is safe.')
        open_wardrobe()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type LOOK or SEARCH')
        time.sleep (2)
        look_search()



def open_wardrobe():
    decision = input('').lower().strip()
    if decision == 'open':
        print ('You lift the door. It is heavy! There are some stone steps carved down into the cellar. \
The nostalgic smell of your grandparents is washed away by something nasty smelling. Is it just stale air? Mold? \
You don’t know what the smell is, but it is putrid. You gradually descend the steps. \
Old incandescent lighting is strung on the walls leading down. Down.  Like the cellar was carved into the mountains itself. \
You reach the bottom and let out a gasp. \
The walls of what can best be described as a chamber are desecrated with the remains of what appear to be young women. \
Nailed to the stone in a variety of poses and states of decay. \
You can’t hold the vomit back as you tear your eyes from the horrific sight. \
When what after feels like ages finally get your stomach under some control you sprint up the stairs. \
You pant as you desperately reach for the top. The opening appears to shrink. \
The door is closing! You use every last bit of energy to make it to the door. \
It is at that moment that it slams closed banging against your HEAD. The world goes black as you tumble down the stairs, back into the abyss. ')
        head()

    elif decision == 'wardrobe':
        print ('You decide to come back to the door. You might as well check everything upstairs first. \
You head back to the open wardrobe and find tons of dresses. \
Apart from the few places nibbled on by your rodent friend they look nearly new. \
They all seem to be for formal attire and a little out of place for a cabin. \
In the bottom of the wardrobe there are more blankets. \
You try to close the door to the wardrobe finding nothing of interest but the blankets keep getting in your way. \
You try to push the blankets in so you can get the wardrobe as you found it, well, minus the rat, \
when you feel something hard wrapped in one of the blankets. Upon closer inspection you find a photo album titled, \
“My Collection”. You open it out of curiosity and nearly drop the book in disgust. \
You see photos of young girls all in formal attire captured in silent screams. \
Bruises cover one girl, and cuts another. It is all different, apart from their hopeless screams.\n     You quickly \
shove the book back into blanket and leave the room. Let the crazy person think the mouse opened the door. \
Do you dare OPEN the door in the floor or do you just want to LEAVE?')
        open_leave()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or  decision =='wake up':
        dream()

    else:
        print ('Please type either OPEN or WARDROBE')
        time.sleep (2)
        open_wardrobe()



def open_leave():
    decision = input('').lower().strip()
    if decision == 'open':
        print ('You lift the door. It is heavy! There are some stone steps carved down into the cellar. \
The nostalgic smell of your grandparents is washed away by something nasty smelling. Is it just stale air? Mold? \
You don’t know what the smell is, but it is putrid. You gradually descend the steps. \
Old incandescent lighting is strung on the walls leading down. Down.  Like the cellar was carved into the mountains itself. \
You reach the bottom and let out a gasp. \
The walls of what can best be described as a chamber are desecrated with the remains of what appear to be young women. \
Nailed to the stone in a variety of poses and states of decay. \
You can’t hold the vomit back as you tear your eyes from the horrific sight. \
When what after feels like ages finally get your stomach under some control you sprint up the stairs. \
You pant as you desperately reach for the top. The opening appears to shrink. \
The door is closing! You use every last bit of energy to make it to the door. \
It is at that moment that it slams closed banging against your HEAD. The world goes black as you tumble down the stairs, back into the abyss. ')
        head()

    elif decision == 'leave':
        print ('You don’t want to push your luck. You are fairly certain that you don’t want to meet whoever owns the cabin. \
You head back down the trail and see that a silver car has parked next to your car. \
When you get closer you see that the other car has it’s engine running but no one is inside. \
When you look around your car you still don’t see anybody around. It is as if the car just appeared out of nowhere. \
For a split second you entertain the idea of either STEALING the other vehicle or CALLING out for the owner.')
        stealing_calling()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either OPEN or LEAVE')
        time.sleep (2)
        open_leave()



def stealing_calling():
    decision = input('').lower().strip()
    if decision == 'stealing':
        print ('You climb in the car and take off down the highway. You are pleasantly surprised to see that the gas gauge is near full. \
You drive for while when you pass a sign that reads, “Welcome to Pinterdale”. Confused you keep driving for a bit until you see a gas station. \
The broken lighting flickering on and off above the pumps. You pull over the car. Did you get turned around after stealing the car? \
There were no other roads to turn off of. Your tank is a little over half full, so you don’t need gas, \
but do you want to drive BACK the way you came from in your silver car or continue in the SAME direction you have been traveling?')
        back_same()

    elif decision == 'calling':
        print ('You call out. The owner must be close. No one should be anywhere near that cabin. \
You think you can hear a girl’s voice off the side of the road. When you get closer you call out again. \
“I’m here,” comes the response.\n    You see teenage girl climbing back up to the road. \
Freckles cover her face. She looks you up and down. “When I found the car I got worried that you got lost. \
It isn’t safe around these parts. The mountains can be a dangerous place, what with all the wolves and the cold. \
It is easy to get lost here. Why did you stop here anyway?” \
She seems genuinely concerned for you which makes you want to be honest and friendly back to her.\n    “My car ran out of gas. \
I thought that I could make it to the next town, but I didn’t quite make it. \
I took a walk around to see if I could find anyone to help but all I found was a creepy cabin with photos of a ton of dead girls. \
You should be the one getting out of here, there is a crazy person around here,” you respond.\n    “Oh, you went up to the cabin? \
There was an accident not long ago where a ton of girls died on prom night. \
The police were involved, just a big ordeal all around. The coroner stayed at that cabin, \
but after everything he went sort of batty and disappeared. No one has been there for a while now. \
The lights are left on as a landmark, because these mountains get rather dark at night.\n    I’m sorry you saw that. \
Do you want me to go up THERE with you? There is usually a can of gas behind the cabin or would you like a LIFT somewhere?”')
        there_lift()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either STEALING or CALLING')
        time.sleep(2)
        stealing_calling()



def back_same():
    decision = input('').lower().strip()
    if decision == 'back':
        print ('You head back the way you came regretting the lost time. \
You feel like you have been driving for hours but when you go to check the time the dashboard just blinks 12:00 at you. \
You feel like you are getting close to where you ditched your car in exchange for the one you stole but there is no sign of your vehicle anywhere. \
You are so focused on finding your vehicle you don’t have time to react when a giant elk jumps across the road. \
You hit the animal full speed. Glass breaks, airbags bang, and the car veers off the road. \
It tilts down the side of the mountain and soon you are accelerating again. \
It isn’t until your car smacks into a large tree that it comes to a stop. \
You smack your head against the steering wheel, cutting a gash across your forehead.\n    You are still alive. \
The elk it appears got part of its lower half wedged in the windshield. It appeared to be dead. \
After a closer inspection of yourself you notice that you also have cuts up and down your arms from the elk and the broken windshield. \
Your leg got twisted in the crash. You can try making your way back UP to the road, or you can continue going DOWN the mountain.')
        up_down()

    elif decision == 'same':
        print ('You figure there is nothing you can do but to keep pressing on. \
You drive down the road leaving behind the empty streets of Pinterdale. You follow the winding mountain road. \
It is so dark. You try to check the dashboard clock to see what time it is, but it just blinks 12:00 back at you. \
You look up to see a person trying to wave at you. Your car sends them flying through the air. \
When they finally hit the ground you see their head twist backwards and they continue sliding on their face down the road. \
You skid to a stop. Your first thought is that you are glad that it isn’t your car that you hit the person with. \
Then it really hits you that you just killed someone. You get out of your car and rush towards them. Their face is lying flat. \
You try to flip them over to get a good look at their face, but the skidding across the ground ripped their skin and nose off leaving a bloody, pulpy mess. \
You let the body fall back to the earth. You hurry back to the car and you start driving. You see town coming up in the distance. \
Do you REPORT the accident to the police of the town or DENY the accident? ')
        report_deny()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either BACK or SAME')
        time.sleep (2)
        back_same()



def report_deny():
    decision = input('').lower().strip()
    if decision == 'report':
        print ('You arrive at the town. A sign reads “Welcome to Pinterdale”. You slam on your breaks. \
In the distance you can see the gas station with a broken strobing light. There is no way that you are back here. \
You head to the police station ignoring the gas station. When you arrive you see that the door is locked. No one seems to be around. \
You call out to see if anyone is around but the area seems devoid of life. You turn to go back to the car and a sheriff is standing directly behind you. \
You jump because you could have sworn no one was there a moment ago. \
He just stares at you, his sunglasses hiding his eyes.\n    He scratches his mustache before finally asking, \
“What seems to be the problem?”\n    “I was driving through the mountains when a person ran out in front of me. \
I hit him. I don’t have a phone so I came to report the accident. I left him where he was hit. When I checked on him, \
he was definitely dead Sir,” you confess.\n    The sheriff reaches for his radio, \
“Hey Bill, it seems there has been an accident. Some poor fellow committed suicide. \
I just found him.  Can you come pick him up?” Static is all you hear in response.\n    Baffled you start to ask, \
“What do you mean you found a--.” The sheriff releases the gun from his holster before there is a loud bang. You feel yourself PASS away.')
        Pass()

    elif decision == 'deny':
        print ('You are in a stolen vehicle and you just killed someone. Going to the local authorities seems like the worst thing you could do. \
You decide to just drive through the town and get as far away from the accident as possible. \
As you enter the town a familiar sign greets you, “Welcome to Pinterdale”. You shoot past the sign and the strobing gas station, \
leaving as fast as you came. Nothing seems real anymore. You continue down the road when your car putters to a stop. \
You have been driving so long you ran out of fuel. \
You smack the steering wheel in frustration.\n    Just ahead you notice something in the middle of the road. \
You get out of the car to get a closer look. It’s a body, the neck snapped, and the face scraped off. \
No. No, this can’t be real. It can’t be the same person you hit hours ago. You sob when the body starts to tremble. \
It peels itself off the road, lumps of gravel imbedded in the skin give it the appearance of some demon with spikes. \
It shuffles backwards toward you. The blank spots where the eyes should be seem to pierce into your being.\n    You run for it. \
Taking off down the road trying to escape this apparition. The remains drop down on it’s hands and it starts scuttling towards you on all fours. \
The gaping hole where the mouth had been opening wider to create an empty void. It catches you. \
You feel the void devour you. Your sins weigh you down. Dragging you down, down into hell. Your silent screams disappearing as you PASS into nothing.')
        Pass()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either REPORT or DENY')
        time.sleep (2)
        report_deny()



def up_down():
    decision = input('').lower().strip()
    if decision == 'up':
        print ('You limp and crawl back up the path your car has torn down the mountain. \
You came down a lot further than you thought. You take frequent breaks but finally make it to the road again. \
You start limping down it as fast as you can manage. Your head is throbbing so bad you feel like you are going to die. \
Your sweat is mixing with your cuts causing them to burn, and walking is agony. You see the headlights of a car approaching you. \
You say a prayer of thanks that someone has found you. You are going to get help. You try to wave as the car approaches. \
The headlights blind you. Then you feel it. It feels as though you are flying. For a moment all of your pain is gone. \
You watch almost indifferently as the ground soars under you. Then it all comes crashing back as you flip head over tail. \
Your neck snaps when you hit the ground. You feel empty as you PASS from this realm.')
        Pass()

    elif decision == 'down':
        print ('You figure going down is easier than going up, so you continue down the mountain. \
You slide-walk down the mountain. It is cloudy and cold. The night feels heavy and you can hear rocks sliding down the mountain that you didn’t kick. \
It is creepy and you have no light. The further down you get the darker it seems to become. Your head is throbbing, and your leg is on fire. \
All the cuts on your face and arms are making it hard to concentrate. Should you WAIT until morning or keep HEADING down?')
        wait_heading()

    elif decision == 'quit':
            quit()

    elif decision == 'dream' or decision == 'wake up':
            dream()

    else:
        print('Please type either UP or DOWN')
        time.sleep(2)
        up_down



def wait_heading():
    decision = input('').lower().strip()
    if decision == 'wait':
        print ('You know it is getting way to dangerous to go fumbling around in the dark. \
You collapse under a tree and try to get some sleep. Now that you aren’t moving your body shivers and shakes. \
The wind goes right through you. You wish you had the time. You just wanted to get away. Get away from everything. \
Now you find yourself in the middle of nowhere. Perhaps you got your wish. \
Now if only you could stop shaking.\n    Almost as you thought it you start to feel warm. \
The breeze coming down the mountain feels like a hot breath. \
Then it starts to get hot. You feel like you are burning up. \
You would almost welcome the cold back. You start stripping off some of your crusted clothes to get some relief from the intense heat. \
You start to wonder if something is wrong as you quietly PASS out.')
        Pass()

    elif decision == 'heading':
        print ('You keep heading down. You feel like if you stop the wind will freeze you. \
You feel sick to your stomach and you can barely see. You take every step with care. You feel like you are near the bottom of the mountain. \
Darkness dominates your vision. You step on loose gravel and feel yourself fall. You roll into the darkness. \
The cuts and tears bringing a crescendo of pain as more join them. Your breathing becomes difficult. \
Your ribs are cracked. You cough up blood before laying your head against the earth in defeat. \
The pain is the only existence you know until you PASS out.')
        Pass()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either WAIT or HEADING')
        time.sleep (2)
        wait_heading()



def there_lift():
    decision = input('').lower().strip()
    if decision == 'there':
        print ('You thank her for her generosity but would prefer to use your own car. You brave the trail and go back to the coroner’s cabin. \
She walks next you. “My name is Marci, by the way. What’s yours?” She asks as you arrive back at the cabin.\n    You go around to the back of the cabin \
where a small shed is kept. “What happened to all those girls? What killed them all?” You ask. \
She doesn’t seem to mind that you didn’t answer her.\n    “I would rather not talk about it if you don’t mind. \
A lot of those girls were my friends. The gas is just kept in that shed.” \
You try the shed door when you see a large padlock over it. It is a little rusted with age, so you try pulling on it but to no avail. \
“I think there is a key inside. Come on.” Marci says after you failed to open the door.\n    You follow Marci inside, \
the rug is still kicked over revealing the door, but you can’t imagine where the key for the shed would be. \
There wasn’t much inside this place that you hadn’t explored originally. She sees the trapdoor and stops. \
“Did you go down there? I didn’t know about that door.”\n    “It gave me the creeps, so I didn’t open it. \
I was afraid the owner of the cabin wouldn’t like me poking around in his basement for a gas can,” you respond.\n    “Do you want to \
CHECK it out? The key might be in the BEDROOM we can just find the key if you are too scared of the door.” ')
        check_bedroom()

    elif decision == 'lift':
        print ('You tell her you can’t bring yourself to go back there and are grateful that she doesn’t mind giving you a ride. \
You ask to just be taken to the next town so you can find a hotel and maybe wait until morning to get your car. \
She happily agrees and you are off.\n    “My name is Marci by the way what is yours?” \
she asks.\n    “Nice to meet you Marci, thanks for saving me. \
You can call me ',user_name,'.” You look out the window and glance at the scenery rush by. \
The darkness reminds you of a child’s nightmare with the trees reaching their branches out \
to grab the unsuspecting traveler.\n    Marci remains quiet and just lets you think. \
You relax into the chair and close your eyes. Before you drift off however you decide to see how far away the next town is. \
You turn to Marci to ask and the thing that is driving looks like a person with no skin. \
Bare muscles cover her body, the flaming red hair from her head now completely gone. \
She looks at you, the lack of lips feels like she is clenching her teeth as she glares at you.\n    You cry out in shock when she starts speaking. \
“Do you remember the night you killed me', user_name,'? I begged for you to turn the car around. \
To take me home. You didn’t!” It spat. The muscles start melting from the body congealing around her. \
Her skeleton is visible, wrapped in veins and blood. \
It seems to be smiling as the skeleton decays into dust.\n    You reach over to the now empty driver side to control the steering as the car \
veers out of control. The steering wheel burns your flesh as if it was super-heated by the touch of the spirit \
that was driving you to the pits of hell. You shriek in pain and terror as the car barrels through a sign, \
“Welcome to Pinterdale”, before shooting towards the flickering lights of the gas station. \
You try to wrench the door open. The handle melts your flesh. You scream again. The car crashes into the gas pumps. \
They belch flames, the explosion tearing the world around you as you PASS into the inferno.')
        Pass()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either THERE or LIFT')
        time.sleep(2)
        there_lift()



def check_bedroom():
    decision = input('').lower().strip()
    if decision == 'check':
        print ('You start pulling on the door. It is made of some very thick wood that weighs a ton. You slowly pull it open. \
There are some stone steps carved down into the cellar. Old incandescent lighting is strung on the walls leading down. Down. \
Like the cellar was carved into the mountains itself. You try to make out the bottom when you feel a hard shove from behind. \
Marci pushes you down the stairs and your feel yourself falling, tumbling, crashing to the bottom. You sob. \
A bone sticking out of your arm.\n    Marci descends the steps after you. When she reaches the bottom she screams. \
It echoes around the stone walls of the chamber. You look up to see her staring at the walls, terror painted across her face. \
You glance to the walls and see the same screams of terror reflected in the remains of all the girls from the photos you had found upstairs. \
They had been arranged in various poses of greeting, or dance. Screaming corpses. Screaming Marci. \
Screaming you.\n    Marci, still bellowing in rage and fear charge at you. \
She kicks at your face, your belly, anywhere she can find. Her kicking drives the remaining air from your lungs. \
She keeps going until you are overloaded by the pain. You hear her ranting about her revenge on you as she stomps on your face until you finally PASS out.')
        Pass()

    elif decision == 'bedroom':
        print ('You lead her away from the trapdoor to the bedroom. You don’t want to spend any more time in that place than you have to. \
You see that the key you are probably looking for is hanging on a hook on the side of the wardrobe. \
You hadn’t noticed it the first time you had come. \
You are about to point it out to Marci when you feel a sharp pain in the back of your shoulder.\n    “DIE YOU FREAK! THOSE WERE MY FRIENDS! \
MY SISTER WAS ONE OF THOSE GIRLS YOU SICK PERVERT!!” Marci is screaming at you. \
Your shoulder spasms where you see she has stabbed you with a kitchen knife. \
You push her away, but she has you backed into the bedroom. Her eyes are filled with hatred as tears run down her freckled face.\n    “Agh,” you cry. \
“I just found this place. It wasn’t me. I don’t know what you are talking about…..you freaking stabbed me!” \
Your words have no effect on Marci as she starts charging you again with the knife. \
She slashes your arm as you try to protect your face.\n    With a cry of pain you shove at the redheaded ball of fury and get lucky. \
She falls to the ground, the knife clattering to the floor. Do you grab the KNIFE or try to run down the TRAIL back to the car she left running?')
        knife_trail()


    elif decision == 'quit':
            quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either CHECK or BEDROOM')
        time.sleep (2)
        check_bedroom()



def knife_trail():
    decision = input('').lower().strip()
    if decision == 'knife':
        print ('You grab the knife. Holding it out towards her. She starts crying. Anger twists your face. \
“Now it’s your turn Marci! Ready to join my collection?” You shout. Spittle covers the floor. You stalk toward her. \
(Wait, what? I didn’t hurt anyone…..) You lift Marci up by the hair. She is screaming and flailing about trying to break your grasp. \
Your shoulder throbs with each excited heartbeat. (No, this is wrong.) You slide the knife into her open mouth and start cutting the inside of her throat. \
She bites down on the knife, trying to get you to stop. Her pleading eyes stare at you as you as she starts to choke on the blood pooling in the back of her throat. \
Her flailing weakens, and the light dims from Marci’s eyes. (No. No. No. Why don’t I have control over my body? I am not doing that!) \
You fling her corpse over your good should and open the trapdoor. You finally have something new to add to your collection. You smile as you PASS into darkness.')
        Pass()

    elif decision == 'trail':
        print ('You run passed her. You take off out the door, crimson blood dripping down your arm and back. \
You hear a wild scream come from the house. You nearly trip as you run back down the trail. You make it to her car. \
No harm in STEALING from a crazy teen right? You could also try using her car as a WEAPON to fend her off.')
        stealing_weapon()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type either KNIFE or TRAIL')
        time.sleep (2)
        knife_trail()



def stealing_weapon():
    decision = input('').lower().strip()
    if decision == 'stealing':
        print ('You climb in the car and take off down the highway. You are pleasantly surprised to see that the gas gauge is near full. \
You drive for while when you pass a sign that reads, “Welcome to Pinterdale”. Confused you keep driving for a bit until you see a gas station. \
The broken lighting flickering on and off above the pumps. You pull over the car. Did you get turned around after stealing the car? \
There were no other roads to turn off of. Your tank is a little over half full, so you don’t need gas, \
but do you want to drive BACK the way you came from in your silver car or continue in the SAME direction you have been traveling?')
        back_same()

    elif decision == 'weapon':
        print ('You climb into her car and lock the door. She smashes into the car almost immediately after. \
The knife smashes against the driver side window. You drive away. She starts chasing after the vehicle. \
You put the car in reverse and shoot backwards to meet her. She jumps the car, both hands holding the knife over her head for a downward plunge. \
You smack her, the knife shatters the window, and she goes sprawling into the street.\n    “DIE!!” you hear her angry voice crack as she starts getting back up. \
You smash into her again. You feel the tires bounce over her. \
She doesn’t appear to be getting up so you hesitantly get out of the car to see if she survived.\n    Her back looks broken, black tire marks staining her clothes. \
You flip her over. Her eyes are closed. She looks almost peaceful. You hold her wondering what possessed to attack you. \
Why did she think you were the cause of the morbid collection of girls?\n    Her eyes shoot open and she buries the knife through the bottom of your chin. \
You try to scream but the knife has cut into the roof of your mouth effectively pinning your jaw shut. \
She coughs and weakly lets the knife go, leaving it impaled in your head. \
The last of her strength used to extract her vengeance. You choke on the blood that fills your mouth and collapse next to Marci. You both PASS into the abyss.')
        Pass()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('Please type either STEALING or WEAPON')
        time.sleep (2)
        stealing_weapon()



def head():
    decision = input ('').lower().strip()
    if decision == 'head':
        print ('You groggily wake up. You blink your eyes. Where are you? You blink again. \
Nothing changes. Everything is dark around you. You can’t see in the blackness that surrounds you. \
The smell is overpowering. You begin to remember, and you frantically feel around the floor looking for the steps. \
Your hand slips through the remains of your last meal causing you to fall the rest of the way to the floor. \
You reach out again and grab a shoe. You recoil as you remember the rotting bodies splayed across the walls. \
You start to cry. What sort of place did you stumble across? You were only looking for gas. \
You edge yourself along the wall letting out a new whimper each time you come across a foot. \
You go around, and start counting the walls. One wall without the stairs. Two. Three. \
You feel revolted that you took the long way around. That you had unwittingly started so close to the steps and went the wrong way. \
Four. Wait what? You are now sure you have gone around the entire room but the steps seem to have vanished. \
You start going around the room again, the thought of all those bodies staring at you, \
welcoming you to stay with them is causing you to panic. When you hear a voice.\n    “What did you think of my collection?” \
it whispers. \n    You sob and your body starts shaking uncontrollably.\n     “They were all so pretty before…..\
but they disgust me now. Why couldn’t they just stay perfect? Why?”\n    You think you can tell \
where the voice is coming from. You realize that the steps were being sat on by the owner, \
and you skipped across them like all the other pairs of feet. Do you want to try to RUN up the stairs or SPEAK to the voice?')
        run_speak()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('1 little monkey falls off the bed. Where the monkey hits its HEAD!')
        time.sleep (2)
        head()



def run_speak():
    decision = input('').lower().strip()
    if decision == 'run':
        print ('You muster your courage, and you charge the voice. You stumble over someone as you start ascending the stairs. \
You think you hear movement behind you. You hit your head again on the top of the door, \
lights of pain blind you for a moment before casting you back into the dark reality. \
You push against the door. You heave. It starts lifting. The lights are still on in the cabin above. \
You break for freedom when something grabs your leg, ripping you out of the light. \
You glance back before the trapdoor closes only to see a wide smile before the world is plunged back into darkness. \
You fall again, this time remaining conscious as every step smacks you on your roll back to the bottom. \
Your assailant flies down the stairs after you.\n    Dizzy and disoriented you struggle to stand when your assailant smashes you against the wall. \
The remains behind you break as you go through them, cutting you across your back. \
You scream as you hear a loud pound. Another scream when it comes again. \
It isn’t until the third pound that you realize you have a large spike going through your arm and pinning you to the wall. \
You try to rip yourself free, but only tear a few muscles before the pain becomes unbearable. You PASS out.')
        Pass()

    elif decision == 'speak':
        print ('You decide to say something. “I just got lost. I’m sorry. I didn’t mean to see your collection. \
I just wanted to borrow a gas can….” You trail off because you realized you \
were trying to ask to borrow a question from a serial killer.\n    “Gas? Yes. That would make it all better. \
Just a little gas and you will be on your way to paradise. I can give you gas.”\n    “Thank you….uh….thanks.” \
you respond stupidly.\n    Footsteps fade away. \
You chase after the noise and realize that the person talking must have been sitting on the steps and you went over their feet \
just as you did over all the feet in the room. You hurry up the stairs. But, the door won’t budge. \
Soon there is something leaking through all the cracks around the door. It sprays from the sides as if to fill up the basement cave with liquid. \
Then just as soon as in started. It stops. You start pushing against the door again when it explodes apart. \
You are blasted back down the stairs. Slivers of wood embedded in your skin. \
A river of fire follows you down the stairs as it ignites the gas. \
The facial features of the corpses around you light up in the bright flickering light, \
making it seem like the women have woken from some deep sleep and are screaming in silent terror. \
You cough as you start choking on the black smoke around you. The flames have covered most of the basement floor. \
You stand in a small, elevated spot in the back of the room where the gas couldn’t reach. \
You feel like you will hack up a lung as the black smoke gets lower and lower to the ground. \
The heat is intolerable as it climbs up the figures around you. You lay in your corner as your coughing become more violent. \
Your skin closest to the flames starts to bubble. You try to scream but the hacking continues, until you PASS out.')
        Pass()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print ('Please type RUN or SPEAK')
        time.sleep (2)
        run_speak()



def dream():
    decision = 'dream'
    if decision == 'dream':
        print ('You realize this whole thing is some sort of dream. A nightmare. You try to blink as fast as you can and start shouting for help. \
Whatever you can do to wake yourself up.\n    It works! You wake with a start. \
The sunlight is peaking through the window. You let out a sigh of relief. It worked! \
Your heart is racing as you recall all that happened to you.\n    Congratulation!!! You Win! ')



def Pass():
    decision = input('').lower().strip()
    if decision == 'pass':
        decision2 = input ('You wake up covered in sweat. It was all a dream. A terrible nightmare. \
You need out of your bed. Out of your house. You quickly get some clothes on as you run from your dreams. \
You get into your car and you take off down the highway. It isn’t long until you go through a town called Pinterdale. \
You have about a quarter tank of gas left and even though you feel like you have a lot of driving left you are trying to decide if you want to get GAS now, \
or DRIVE to the next town before deciding to fill up. \
You feel an odd sense of déjà vu, it is almost as if you have been here before.\n')

        if decision2 == 'gas':
            print('You pull up to the gas station. The light above the fuel pump blinks rhythmically on and off giving the place an eerie vibe \
as it repeatedly casts your surroundings in darkness before briefly illuminating your surroundings once again. \
Do you pay at the PUMP or do you go in the gas station and pay the CASHIER?')
            pump_cashier()
        
        elif decision2 == 'drive':
            print('The gas station seems to have a broken light that blinks on and off. \
It hurts your eyes looking at it, beside you decide that a quarter of a tank is still plenty, and you rush on through down the road. \
You continue to drive but realize that you have become lost. The gas gauge slowly hovers over empty before your car putters to the side of the road. \
There is a sign for the next TOWN just a few miles away, but you can also see a LIGHT not too far from the road.')
            town_light()

        else:
            print('Please type either GAS or DRIVE')
            time.sleep (2)
            gas_drive()

    elif decision == 'quit':
        quit()

    elif decision == 'dream' or decision == 'wake up':
        dream()

    else:
        print('You have no control. You must type PASS!')
        time.sleep (2)
        Pass()



def quit():
    decision = 'quit'
    if decision == 'quit':
        print ('Thank You for Playing!')



def to_be_continued():
    decision = input('Would you like to START over? Or would you like to QUIT? \n').lower().strip()
    if decision == 'start':
        gas_drive()
    
    elif decision == 'quit':
        quit()

    else:
        print('Please type either START or QUIT')
        time.sleep (2)
        to_be_continued()


#This starts the adventure!
gas_drive ()