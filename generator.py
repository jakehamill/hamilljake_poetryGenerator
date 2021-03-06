# -*- coding: utf-8 -*-
"""
Author: Jake Hamill
Description: python poen generator
License: GNU General Public License 
August 28, 2018

"""



from playsound import playsound
from gtts import gTTS
import random

# list of nouns

line1 = ["The storm bubbles on the horizon. ", "Storms are blowing on the horizon. ",
         "The storm bubbles far on the horizon. ", "The storm bubble is far on the horizon. ",
         "A storm is far away ball over-the-horizon. ", "There is a storm on the horizon for "
         "dispersion into the distance. ", "Storms are blown on the horizon. ",
         "The storm is scattered far on the horizon. ", "Storm bubbles far on horizon. ", ]

line2 = ["Shape shifting, always moving closer and farther away. ", " Its always a transformation "
         "and a distant transformation. ", "Shape shifting is always farther and far away. ", "Deformation, always " 
         "getting closer. ", "The changed form moves timelessly. ", 
         "Shape-shifting to mobile, remote and far away. ", "Shapsifting is a generation of bright colored paint "
         "that is always farther and far away, and is shaking the house. ",
         "The shape moves around and far away. ", "Move the shape, allways moving and farther. ", ]

line3 = ["Light pours through holes in thick grey clouds. ", "The light passes through the thick gray clouds .",
         "Light rushes into holes of the fat grey clouds. ", "Light filtering through a hole in the thick "
         "gray clouds. ", "Light is poured out through the holes of thick grey clouds. ", 
         "Light sheds through holes in thick grey clouds. ", "Light is thrown through the holes of thick "
         "grey clouds. ", "Light drains from circles in the grey cloud. ",  ]

line4 = ["Glimmering off of houses that perspire through generations of brightly colored paint. ",
         "The sweaty house is brighter through several generations of brightly coloured paint. ",
         "A mantle cuts in houses that perspire in generations of paint ablaze and colorful. ", 
         "Sparkle home-sweat through several generations of bright colors. ",
         "The twinkling of a hard house. The generation of bright-colored paint. ",
         "Glimmering off of houses that perspire through generations of shiney colored paint. ",
         "The glitter from the home, sweats through a lot of bright colors. ", 
         "Glitters on houses sweat through generations of paint in bright colors. ", ]

line5 = ["Paint that keeps these structures huffing and puffing with bones exhausted. ",
         "The paint that keeps these structures tired of panting and swelling bones . ",
         "Painting holding these structures huffing and suffering after bone use. ", 
         "Paint maintaining this structure burnout with bones bloated. ", "I'm tired of the painting bone that "
         "holds these structures. ", "Paint that keeps these structures dead and burning. ", "Paint that "
         "keeps these structures laughing at the bones. ", "The color allows these structures to poke, "
         "inflate, and make the bones completely bored. ", "The paint that preserves these structures drains "
         "the bones and puffs. ",  
  ]

line6 = ["I know that if these houses can get one more layer of paint then I might just see them once again "
         "standing brilliantly against this wall of gray. ", 
         "I know that if these houses can be painted one more layer, then I might see them again close to the "
         "gray wall. ", "I know that if these buildings can find one more layer in the painting then I could "
         "just see them again a second time brilliant against this wall in grey. ", 
         "If we paint the houses one more time, then I may look at them once again. " 
         "This gray wall is standing well. ", "I'm tired of the painting bone that holds these structures, and " 
         "I'm tired of these houses, and I'm going to see them again, and I'm standing on this gray wall, "
         "and I'm standing on this gray wall. ", "I know that if these houses would get another layer of color "
         "then I could see them again fried with the walls of this gray. ",   ]


first = random.choice(line1)
second = random.choice(line2)
third = random.choice(line3)
fourth = random.choice(line4)
fifth = random.choice(line5)
sixth = random.choice(line6)


poem = first + second + third + fourth + fifth + sixth
print poem

#text to speech
tts = gTTS(text=poem, lang="en")

#write audio file
tts.save("mp3s/poemgenfinal_02.mp3")

#play audio file
playsound("mp3s/poemgenfinal_02.mp3")

  
    
    
    


