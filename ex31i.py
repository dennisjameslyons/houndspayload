print ("You found the guy who stole 'needle', door #1 to get him or #2 to run away")

door = input("> ")

if door == ("1"):
    print ("You brave girl, get in there and be a bad bitch.")
    print ("1. Sit & wait for your moment.")
    print ("2. Act a crazy revenge-fueled fool.")
    
    choice = input("> ")
    
    if choice == ("1"):
        print ("Patience pays off, you slayed like a bad bitch! Good job!")
    elif choice == ("2"):
        print ("Shoulda been more patient, you died. Good job!")
    else: 
        print ("Well, doing %s is probably better. Lannister men run away.") % choice

elif door == ("2"):
    print ("You are not Arya, imposter asss. She'd never run!")
    print ("1. You'll be hanged for this, imposter!")
    print ("2. Your head will be on a spike before dusk, imposter!")
    print ("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == ("1") or insanity == ("3"):
        print ("You've got a rope around your neck for lying. Good job.")
    else: 
        print ("The Lannisters will enjoy your newly spiked head! Good job!")
    
else: 
    print ("You stumble around and fall on a knife and die. Good job!")

print ("You got a pony! You could try wiping Hound off now (1) or later (2)? ")

which = input("> ")

if which == ("1"):
    print ("Well you didn't think it over - he has armor, duh.")
    print ("1. Get over it, keep practicing, your moment will come!")
    print ("2. Cry like a bitch.") 
    
print ("Now you're at the eyre. Your Aunt is dead. You (1) LOL or (2) say a prayer.")

eyre = input("> ")

if eyre == ("1"):
    print ("Duh, you came all this way for nothing. Games make you laugh, huh?!")
    print ("Now what though? (1) you'll kill that hound yet! or (2) Keep practicing!")
elif eyre == ("2"):
    print ("I don't think so. You ARE an imposter after all! Stopped in ur tracks.")
else: 
    print ("I can't do this anymore.")

