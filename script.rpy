define mc = Character("srikant")
define elder = Character("Elder")
define friend = Character("Bhavya")
define child = Character("Aru")

# Background images
image bg_village_day = "images/bg_village_day.png"
image bg_hut = "images/bg_hut.png"
image bg_elder_house = "images/bg_elder_house.png"
image bg_night = "images/bg_night.png"
image bg_dawn = "images/bg_dawn.png"
image mch = "images/mc.png.png"
image elder = "images/elder.png.png"
image friend = "images/lira.png.png"
image child = "images/aru.png.png"
default karma = 0

label start:
    $ renpy.music.set_volume(1.0, delay=0, channel='music')

    # Scene 1: Village Dawn
    scene bg_village_day
    play music "audio/intro_theme.mp3"

    show mch
    "Sunlight spills over the village rooftops, warming the quiet streets."
    "Everything feels peaceful… almost too peaceful."
    "But peace always comes at a cost."

    "As you stroll down the main road, a small voice cries out near the well."

    menu:
        "Go help the child":
            $ karma += 1
            jump help_child
        "Ignore and keep walking":
            $ karma -= 1
            jump ignore_child

label help_child:
    scene bg_hut
    show mch at left
    show child at right

    child "Please… my cat fell into the well!"
    mc "Don't worry, I’ll get it out."
    "You reach down carefully, pulling the frightened cat out of the well."
    child "Thank you so much!"
    "Aru smiles brightly before running back home."

    hide mch
    hide child
    jump meet_elder

label ignore_child:
    scene bg_hut
    show mch at left
    "You walk past, pretending not to hear the crying."
    "A pang of guilt twists in your chest… but you keep moving."
    hide mch
    jump meet_elder

# Scene 2: Meeting the Elder
label meet_elder:
    scene bg_hut
    play music "audio/ominous_theme.mp3"
    show mch at left
    show elder at center

    elder "The prophecy speaks of one who must give up everything…"
    mc "Why does it always fall on someone to pay the price?"
    elder "Because balance demands it. Without loss, there is no growth."

    "Your eyes catch a half-hidden book under the table, its cover worn and strange symbols etched into it."

    menu:
        "Ask about the book":
            $ karma += 1
            jump ask_book
        "Say nothing and listen":
            jump stay_quiet

label ask_book:
    mc "Elder… what is that book?"
    elder "Ah… some truths are dangerous. But perhaps you are ready."
    "He opens it slowly, the symbols glowing faintly. Your heart skips a beat."
    hide srikant
    hide elder
    jump ritual_choice

label stay_quiet:
    "You bite your tongue. Some things are better left unknown."
    "Still… curiosity nags at the back of your mind."
    hide mch
    hide elder
    jump ritual_choice

# Scene 3: The Ritual Choice
label ritual_choice:
    scene bg_elder_house
    play music "audio/decision_theme.mp3"

    show mch at left
    show friend at right
    show elder at center

    "The altar looms ahead, candles flickering softly. The village’s fate rests on your shoulders."
    mc "If I do this, the village survives… but I’ll be forgotten."
    friend "You don’t have to do it!"
    mc "Someone has to. It might as well be me."

    menu:
        "Offer your own life":
            $ karma += 1
            jump accept_sacrifice
        "Offer someone else's life":
            $ karma -= 1
            jump dark_path
        "Refuse the ritual":
            jump refuse_sacrifice

label accept_sacrifice:
    scene bg_night
    play music "audio/sad_theme.mp3"

    show mch at left
    show elder at center

    "The shadows envelop you as the ritual begins."
    "The village is saved… but your name fades from memory."
    if karma > 0:
        "Even in silence, you feel a quiet peace."
    else:
        "Even in sacrifice, the weight of your choices lingers."

    hide mch
    hide elder
    hide friend
    jump ending

label refuse_sacrifice:
    scene bg_dawn
    play music "audio/hopeful_theme.mp3"

    show mch at left
    show friend at right

    "You step back from the altar. The world trembles around you, but you don’t bend."
    if karma >= 0:
        "Courage can take many forms, and sometimes refusing is the bravest act."
    else:
        "Still… the cost of inaction may yet come to claim everything."

    hide mch
    hide friend
    hide elder
    jump ending

label dark_path:
    scene bg_night
    play music "audio/ominous_theme.mp3"

    show mch at left
    show friend at right

    "You whisper another’s name into the flames."
    "The village is saved, but their screams haunt your memory."
    friend "What… what did you do?"
    mc "What had to be done."
    $ karma -= 2

    hide mch
    hide friend
    hide elder
    jump ending

label ending:
    if karma >= 2:
        scene bg_dawn
        play music "audio/hopeful_theme.mp3"
        "Your selflessness brought peace to the village."
        "Stories of your courage echo through generations."
        "You gave everything — and became immortal in memory."
    elif karma <= -2:
        scene bg_night
        play music "audio/ominous_theme.mp3"
        "The village survives… but your name carries both salvation and darkness."
        "Sacrifice came… at a terrible cost."
    else:
        scene bg_hut
        play music "audio/sad_theme.mp3"
        "The village survives, but a shadow lingers over everything."
        "Your choices echo silently, leaving no one completely unscarred."
    return
