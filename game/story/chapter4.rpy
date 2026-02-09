#chapter 4
#reply to this post or your mother will die in her sleep tonight

label chapter4:
    stop music fadeout 2.0
    
    scene bg black with dissolve
    
    n "Chapter 4"

    #monday
    
    scene bg classroom with fade
    
    play music "audio/music/mere - schooldaze.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    show rothbauer at center with dissolve:
        ypos y_roth
    
    rothbauer @ say "...That's the final lesson that will be on the midterm! We'll have a review on Wednesday then you'll be all set for Friday's exam."
    rothbauer @ say "That's all I have for you today. Good luck on your midterms!"
    
    hide rothbauer with dissolve
    
    n "The classroom fills with the sounds of papers shuffling and bags being zipped as students begin to file out."
    
    if historySkill < 3:
        n "You have a bad feeling about this history exam. Maybe you should ask someone for help studying."
        n "Rose is definitely the smartest person in this class. She's aced every quiz so far and always has her snout in the books."
        n "As much as you hate to ask, she might be your best bet. You muster up the courage to look over to her and clear your throat."
    
        player "Hey Rose, I-"
        
        show rose skirt armscrossed dismissive at center with dissolve:
            ypos y_rose
        
        rose @ say "Nope. Study on your own."
        
        player "But I-"
        
        rose @ say "Don't care."
        
        hide rose with dissolve
        
        n "Without even looking at you, she packs her things and walks away."
        n "You should have known she'd brush you off."
        
        
    else:
        n "You feel sufficiently prepared for this exam. A lot of it is stuff you've learned before, just in greater detail."
        #n "Still though, if you wanted to ace it you could go for some tutoring."
        
    scene bg schoolhallways autumn day with dissolve
    
    #play music "audio/music/vylet - there.ogg" fadein .4
    play music "audio/music/vylet - someday.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "On your way to stats, you spot Rori at the vending machine again playing with his rat companion."
    
    show rori rat concerned at center with dissolve:
        ypos y_rori
    
    rori @ say "Okay... sit! Sit? Please? I'll give you another pretzel if you sit."
    
    n "There's desperation in his voice. He must have been at this for a while but the rat just wants to crawl up and down his sleeves sniffing at every fold in the fabric."
    
    player "Hi Rori. G'day, Guts."
    
    show rori rat smile
    
    rori @ say "Heya [name]. I'm just trying to teach Guts some tricks. I think he sorta understands what I want him to do but he's... defiant."
    
    show rori rat neutral
    
    player "Must be in his rebellious phase."
    
    n "Guts looks up at you before running down Rori's sleeve and snatching the pretzel out of his hoof."
    
    show rori rat sassy
    
    rori @ say "Hey!"
    
    show gunner determined at center:
        ypos y_gunner
        xoffset -2000
    
    n "From the corner of your eye you see Gunner striding up to you."
    
    show rori with move:
        xoffset 350
    show gunner determined with move:
        ypos y_gunner
        xoffset -400
        #xpos 2500
        xzoom -1
    
    
    gunner @ say "Sup homos."
    
    menu:
        gunner "{cps=0}Sup homos.{/cps}"
        "How did you know??":
            $ youGay = True
            
            show rori rat concerned
            show gunner neutral
            
            player "H-how did you know I'm a homo?"
            
            show gunner cutie
            
            gunner @ say "It's shorthand for homo sapien."
            
            show gunner disgusted
            
            gunner @ say "Wait a minute, are you actually-"
            
        "I'm not a homo":
            $ roriPoints -= 1
            
            player "Hold up, I ain't no homo!"
            
            show gunner neutral
            show rori rat neutral
            
            gunner @ say "But you are a homo sapien!"
            
            show gunner eyesclosed smile
            
            gunner @ say "You literally cannot deny your homo-ness."
            
        "Respond \"Kill yourself\"":
            $ gunnerPoints -= 1
            
            show rori rat neutral
            
            player "Kill yourself."
            
            show gunner hissing
            
            gunner @ say "After you."
            
            show rori rat anxious2
            
            rori @ say "Guys..."
        
    show gunner uncomfy
    show rori rat anxious2
        
    gunner @ say "Holy shit a rat!!"
    
    pause .1
    
    show gunner:
        linear .3 xoffset 0
    pause .1
    show rori:
        linear .3 xoffset 600

    
    n "Gunner pounces on Rori, pawing and clawing at his hoodie as Guts scurries around frantically."
    
    show rori rat sassy
    
    rori @ say "Hey! Stop it!"
    
    show rori:
        linear .15 xoffset 250
        
    pause .1
    
    show gunner snoring at shudder
    
    pause .5
        
    show gunner:
        linear .2 ypos 2800
        
    pause .2
    
    show rori:
        linear .4 xoffset 400
    
    n "A sound not unlike a baseball being struck by a bat rings out as Rori's horns collide with Gunner's skull."
    n "Gunner falls flat on his back and Rori goes to check on Guts."
    
    show rori rat surprised
    
    rori @ say "Are you okay? Gunner didn't scratch you, did he?"
    
    show rori rat concerned
    
    n "Guts is still a bit shaken but he seems to find comfort in Rori's grasp."
    
    player "Dude I think you KO'd Gunner."
    
    rori @ say "Did I? I didn't mean to, I just reacted like any ram would."
    
    menu:
        rori "{cps=0}Did I? I didn't mean to, I just reacted like any ram would.{/cps}"
        "Let's steal his wallet":
            $ playerBullyLevel += 1
            
            player "He deserved it. Let's see how much cash he's carrying. I'm sure he won't miss a couple thousand bucks."
            
            show rori rat cheery blush
            
            rori @ say "Do what you will, I'm just glad Guts isn't hurt."
            
            hide rori with dissolve
            
            n "You crouch down to Gunner's limp body and feel around for his wallet but it's not long before his eyes snap open."
            
            show gunner hissing at center with dissolve:
                ypos y_gunner
            
            gunner @ say "Keep your paws to yourself, mister."
            
            show gunner itsover
            
            gunner @ say "Sheesh, I get knocked out for two seconds and you can't help trying to molest me."
            
            show gunner annoyed
            
            player "I was just checking your pulse."
            
            gunner @ say "Yeah yeah I've heard it all before. Trying to see if my cock throbs when you grab it."
            
            pause .1
            
            show gunner with move:
                xoffset -400
            
        "We should see if he's still alive":
            player "We should at least check and see if he's still breathing."
            
            rori @ say "G-good idea."
            rori @ say "I didn't kill him, did I?"
            
            n "You crouch down to Gunner's limp body and poke him on the shoulder."
            n "..."
            n "You poke again."
            n "..."
            n "Gunner starts to stir, groaning in pain. He reaches up to his head where Rori struck him and winces."
            
            show gunner hissing at center with dissolve:
                ypos y_gunner
                xoffset -400
            
            gunner @ say "Ughhh..."
            
            player "You okay?"
            
            show gunner itsover
            
            gunner @ say "It hurts so much..."
            
            player "You're not bleeding but you might have a concussion. We can take you to the hospital if you're gonna cry about it."
            
            show gunner wink frown
            
            gunner @ say "I don't care about that..."
            
            show gunner disgusted
            
            gunner @ say "I'm more upset that I got knocked out by *Rori* of all people."
            
            show rori rat neutral
            
            rori @ say "Oh, good to see he's still his usual self. I thought I might have given him brain damage."
            
    show gunner uncomfy

    n "Gunner rises to his feet, shaking his head."
    
    show rori rat sassy at center with dissolve:
        ypos y_rori
        xoffset 400
    
    rori @ say "What do you have to say for yourself? You scared our little rat buddy half to death!"
    
    gunner @ say "Sorry, instincts got a hold of me. I see prey animal, I go for it."
    
    #player "Are secretary birds considered prey animals? Feral ones are pretty aggressive."
    
    show rori rat anxious2
    
    rori @ say "Be nice to Guts! He's already crippled!"
    
    player "Yeah, what did he ever do to you?"
    
    gunner @ say "Wait, you named him? Is that the rat from a few weeks ago?"
    
    show rori rat silly
    
    rori @ say "Yup! I started visiting him regularly and we just sorta became friends."
    
    show gunner annoyed
    
    gunner @ say "Gross."
    
    show rori neutral
    
    rori @ say "Rats are actually super smart and learn quickly. I've been teaching him tricks! Watch"
    rori @ say "C'mere Guts, in one sleeve and out the other!"
    
    n "Rori holds open one of his sleeves and Guts crawls inside. A moment later he pops out from his other sleeve."
    
    player "Impressive. I could never do that."
    
    show gunner frown1
    
    gunner @ say "Yeah cool, just don't bring fleas into our room. The last thing I need is the black plague localized in our dorm during midterms."
    
    rori @ say "Don't worry, he's chill. I gave him a little bath and everything!"
    
    player "Sounds like you're taking great care of him!"
    
    show rori rat smile
    
    rori @ say "Yeah! I never had a pet before so I did a bunch of research and found out how to best take care of him!"
    
    show gunner snoring
    
    gunner @ say "I guess if he makes you so happy then I'll try to repress my feline instincts to kill it on sight."
    
    show rori rat flattered blush
    show gunner neutral
    
    rori @ say "Thanks. And I'll try to repress my sheep instincts to headbutt on reaction."
    
    show rori rat neutral
    
    player "It was a pretty well-timed overhead attack."
    player "I think it's about time we get to class now."
    
    rori @ say "Oki! See you guys later!"
    
    player "Bye Rori! Bye Guts!"
    
    gunner @ say "Later homos. Later rat."
    
    rori @ say "Good luck with midterms!"
    
    player "You too!"
    
    scene bg lecturehall with fade
    
    play music "audio/music/mere - schooldaze faster.ogg" fadein .4
    
    show box:
        ypos 0
    
    show herschel at center with dissolve:
        ypos y_herschel
    
    herschel @ say "Good afternoon class! The midterm is coming up on Friday but we still have a lot of content to cover so let's jump right in!"
    
    pause .1
    
    show herschel with move:
        xoffset 400
    show gunner displeased at center with dissolve:
        ypos y_gunner
        xoffset -350
        xzoom -1
    
    gunner @ say "You mean there's *more* to study?!"
    
    herschel @ say "Yup! The field of mathematics may as well be infinitely spanning, so there's little time to waste!"
    
    gunner @ say "Does that mean we won't even have a review on Wednesday?"
    
    herschel @ say "A review? This is college dear, not daycare."
    herschel @ say "Now then, starting with a Bernoulli distribution, we'll derive a probability mass function over k possible outcomes..."
    
    n "Gunner turns to look at you."
    
    gunner @ say "You and me are going to the library to study after this."
    
    scene bg library with fade
    
    play music "audio/music/vylet - sailing away.ogg" fadein .4
    
    show box:
        ypos 0
    
    n "After class, Gunner dragged you to the library and found a table for just the two of you."
    
    if statsSkill < 4:
        n "You don't really mind the impromptu study session, you could use some more practice in statistics."
        
    else:
        n "You're feeling confident in your math abilities to do well on the test, but a little extra practice won't hurt."
        
    show gunner neutral at center:
        ypos y_gunner
        
    gunner @ say "Okay, let's start from the start. What is probability?"
    
    player "You don't know?"
    
    show gunner displeased
    
    gunner @ say "Obviously I know, but this is gonna be a comprehensive review."
    
    player "There's not enough time in a day to go over half a semester's worth of lessons. Just focus on what you struggle with."
    
    show gunner pissed
    
    gunner @ say "Ok ok ok I just *cannot* afford to fail this class again."
    
    show gunner uncomfy
    
    gunner @ say "Like I get the basics but when you start throwing in factorials and shit it gets confusing."
    
    player "Yeah, there are a lot of formulas to memorize, and knowing when to use which one."
    
    gunner @ say "Right so like on last week's homework I couldn't figure out which to use..."
    
    n "Gunner opens his textbook and points at a problem. This one gave you some difficulty as well but you managed to solve it correctly."
    n "You work through a few problems with him then start looking over the ones that have stumped you."
    n "At least you try to but Gunner interrupts you every few minutes with another question."
    
    menu:
        n "{cps=0}At least you try to but Gunner interrupts you every few minutes with another question.{/cps}"
        "Focus on helping him":
            $ gunnerPoints += 1
            $ helpedGunnerStudy = True
            
            n "You'll be nice and help him out since he's so far behind you. You just hope you don't drop a letter grade by neglecting your own studies."
            
            show gunner cheeky1
            
            gunner @ say "Thanks for the help bro, it really means a lot!"
        "Focus on your own studies":
            $ statsSkill += 1
    
            player "You gotta try figuring these out on your own. I won't be there to help you during the test."
            
            show gunner cutie
            
            gunner @ say "We could always cheat :3"
            
            player "Yeah no I'm not copying your wrong answers."
            
            show gunner cheeky1
            
            gunner @ say "But can I copy your wrong answers?"
            
            menu:
                gunner "{cps=0}But can I copy your wrong answers?{/cps}"
                "Why not":
                    player "As long as you don't drag me into it when you get caught."
                    
                    gunner @ say "Hell yeah!!!"
                    
                    player "Shh! This is a library!"
                "Nah":
                    player "Mrs. Herschel will know something is up if we both get the same answers."
                    
                    show gunner charming
                    
                    gunner @ say "I'll take the fall for it if she notices."
                    
                    player "Whatever, it's your grade."
                    
            n "You resume working through problems, occasionally helping your study partner when it's trivial for you."
    
        
    #go to library to study with gunner but he distracts you. claims the concussion rori gave him earlier is messing with his ability to study
    #choose to either focus on your own studies or help him study
    #explain statistics and probability in terms of stock markets and betting

    #tuesday
    
    stop music fadeout 2.0
    
    scene bg black with dissolve
    
    n "The following day..."
    
    scene bg classroom with dissolve
    
    play music "audio/music/mere - retrograde.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    #margaret @ say "That just about sums up our review for Thursday's midterm! Study hard and do your best!"
    
    show celestine neutral at center with dissolve:
        ypos y_celestine
    
    celestine @ say "Bonjours les étudiants!"
    celestine @ say "We're officially one week away from the midterm! You're all doing well in class so I have no doubt that everyone pass!"
    celestine @ say "N'est-ce pas, [name]?"

    player "Err..."

    menu:
        player "{cps=0}Err...{/cps}"
        "Mais oui!":
            player "Mais oui!"

            celestine @ say "Très bon!"
        "Je ne sais pas...":
            player "Je ne sais pas..."

            celestine @ say "Hmm..."
            celestine @ say "Claire, pourriez-vous donner des cours à [name], s'il vous plaît?"

            show claire sweater happy at center with dissolve:
                xzoom -1
                xoffset -600
                ypos y_claire

            claire @ say "Mais oui!"

            celestine @ say "C'est parfait!"

            hide claire with dissolve

    celestine @ say "Let's begin a review of the semester so far, shall we?"
    
    hide celestine with dissolve
    
    n "Mrs. Celestine goes around the classroom asking questions in French to each student."
    n "Unsurprisingly, Claire has no trouble at all, whereas you have to take a few notes."
    n "After class ends she turns to you with a devious grin."
    
    show claire sweater leaning suggestive at center with dissolve:
        xzoom -1
        xoffset -600
        ypos y_claire
    
    claire @ say "Heyyyyy [name]~"
    claire @ say "I'm having trouble with a few French words, would you like to come over to my dorm and \"\"\"study\"\"\"?"
    
    menu:
        claire "{cps=0}I'm having trouble with a few French words, would you like to come over to my dorm and \"\"\"study\"\"\"?{/cps}"
        "No thanks":
            n "You have a feeling this would involve more than just studying."
        
            player "No thanks, I'm good on my own."
            
            show claire sweater sad
            
            claire @ say "Awww..."
            
            show claire sweater derp
            
            claire @ say "Well, good luck on your midterms!"
            
            show claire sweater happy
            
            player "You too!"
            
            n "You pack your things and head to the library to cram for the exams."
            
            scene bg library with fade
            
            play music "audio/music/vylet - sailing away.ogg" fadein .5
            
            show box with Dissolve(.2):
                ypos 0
            
            n "What will you study?"
            
            menu:
                "French":
                    $ frenchSkill += 2
                    n "You pick up your French textbook and practice some lessons."
                "Literature":
                    $ literatureSkill += 2
                    n "You open your totally legally acquired epub of [currentbook] and start reading."
                "History":
                    $ historySkill += 2
                    n "You crack open your History textbook and read up on some ancient cultures."
                "Statistics":
                    $ statsSkill += 2
                    n "You flip open your statistics book and open a calculator app to crunch some numbers."
                    
            n "Without any distractions in place you feel like you learned more than you normally do."
            n "That's about all you can do today. You hope that's enough to pass the midterm."
            
        "Yeah!":
            $ clairePoints += 1
            
            player "Yeah, I could go for a private study session!"
            
            show claire sweater overjoyed
            
            claire @ say "Yay!~"
            
            n "Claire proceeds to grab your hand and drag you to her dorm."
            
            scene bg avadorm with fade
            
            show box with Dissolve(.2):
                ypos 0
                
            call claireFrenchStudy2 from _call_claireFrenchStudy2
    
    
    #wednesday
    
    stop music fadeout 2.0
    
    scene bg black with dissolve
    
    n "The following day..."
    
    n "Today's the last day before midterms begin. Better pay attention in class and study hard."
    
    
    if claireSmoochies == True:
    
        scene bg campus autumn day with fade
        
        play music "audio/music/vylet - glamour.ogg" fadein .5
        
        show box with Dissolve(.2):
            ypos 0
    
        n "On your way to class you bump into Ava, looking frantic."
        
        show ava typical shocked at center with dissolve:
            ypos y_ava
        
        ava @ say "Oh uh... hey, [name]! Ready for midterms?"
        
        show ava typical happy
        
        player "I'm not sure. I guess I have to be cause they're coming whether I like it or not."
        
        show ava typical whimsical
        
        ava @ say "I know right? Just one of those things to do and be over with."
        ava @ say "..."
        
        show ava typical concerned
        
        n "Ava lowers her voice."
        
        ava @ say "So um..."
        
        show ava pose concerned
        
        ava @ say "Did you... do it with Claire last night?"
        
        menu:
            ava "{cps=0}Did you... do it with Claire last night?{/cps}"
            "I sure did" if clairePoints > 9:
                if avaPoints > 4:
                    $ avaCucked = True
                $ avaLostInterest = True
                $ avaJealousy += 3
                $ fuckedClaireEarly = True
                $ avaMad = True
                $ clairePoints += 2
                
                player "You really wanna know?"
                
                n "Ava nods."
                
                player "Yeah, I did."
                
                show ava typical unamused
                
                ava @ say "Oh..."
                
                show ava typical agitated
                
                ava @ say "I mean uh... congrats?"
                
                player "It was kind of a spontaneous thing, ya know?"
                
                show ava typical annoyed
                
                ava @ say "Right haha yeah, you two just saw the opportunity and fucked."
                
                show ava typical angry
                
                ava @ say "On the bed right underneath me."
                
                show ava typical unimpressed
                
                ava @ say "I had my headphones on so I couldn't hear you guys btw"
                ava @ say "Just in case you were self conscious about that part."
                
                player "I wasn't."
                
                show ava typical unamused
                
                ava @ say "Then I guess that's a relief."
                ava @ say "I was wondering why the hell the bunk bed was shaking so much."
                
                show claire flannel happy at offscreenleft:
                    ypos y_claire
                    xzoom -1
                
                player "Sorry about that, you know how Claire is."
                
                pause .1
                
                show ava:
                    xoffset 400
                show claire flustered at center:
                    xoffset -450
                    ypos y_claire
                with move
                
                claire @ say "Speaking of that big beautiful bunny..."
                
                show claire flannel happy
                
                n "Claire hops onto the scene with extra whimsy before practically draping herself on top of you."
                n "You can barely hold her up."
                
                show claire flannel laughing
                show ava typical agitated
                
                claire @ say "Way to go champ, you really handled that \"study session\" like a pro~"
                
                show claire flannel suggestive 
                show ava typical annoyed
                
                claire @ say "I'm sure you'll pass that midterm with flying colors ksksksksks!"
                
                player "Claire please get off of me, I'm too weak from last night."
                
                show ava typical angry
                show claire flannel surprised earsup
                
                claire @ say "Oh! I guess you deserve a break. You were doing a lot of heavy lifting after all~"
                
                show claire flannel happy
                show ava typical unimpressed
                
                ava @ say "Would you look at the time, I have to get to class."
                ava @ say "Sounds like you two spent a lot of time studying French last night."
                ava @ say "Hope it was worth it."
                
                pause .1
                
                show ava at flipright
                
                pause .3
                
                show ava at offscreenright with move
                
                n "Ava takes to the skies before you can say goodbye."
                
                show claire flannel suggestive
                
                claire @ say "She's jealous~"
                
                player "I feel bad that we kept her up last night."
                
                show claire flannel derp
                
                claire @ say "Yeahhhhh, we'll have to study at your place next time~"
                
                show claire flannel happy
                
                player "Mhm~ Think we better get to class now though."
                
                claire @ say "We'll do more stuff after midterms ksksksksks"
                claire @ say "See you around, cutie~"
                
                n "Claire gives you a kiss on your cheek then skips away."
                n "It's gonna be really hard to focus in class today."
                
                
                
                
            "I sure didn't":
                $ avaJealousy += 1
                $ kissedClaire = True
                
                player "Nah, we just kissed and stuff."
                
                show ava typical shocked
                
                ava @ say "Was it... nice? I mean would you do it again?"
                
                menu:
                    ava "{cps=0}Was it... nice? I mean would you do it again?{/cps}"
                    "Hell yeah":
                        $ avaJealousy += 1
                        $ avaMad = True
                        $ enjoyedKissingClaire = True
                        
                        player "Hell yeah, it was fucking awesome."
                        
                        show ava typical unamused
                        
                        ava @ say "I see..."
                        ava @ say "Well, I'm glad you found someone you enjoy."
                        
                        player "I know right? I used to think Claire was kinda annoying but now I really like spending time with her."
                        player "Should I ask her out??"
                        
                        n "Ava rolls her eyes."
                        
                        ava @ say "If she's the one you want then go for it I guess."
                        
                        show ava typical unimpressed 
                        
                        ava @ say "You could do better though. Just saying."
                        
                        player "I dunno, Claire might just be the best."
                        
                        show ava typical angry
                        
                        n "Ava scoffs."
                        
                        ava @ say "Whatever, I gotta head to class now."
                        
                        pause .1
                        
                        show ava at flipright
                        
                        pause .3
                        
                        show ava at offscreenright with move
                        
                        n "Ava takes to the skies before you can say goodbye."
                        
                        
                        
                        
                    "Probably not":
                        $ clairePoints -= 1
                        $ enjoyedKissingClaire = False
                        
                        player "Honestly probably not. I was just caught up in the moment and wanted to try it out, ya know?"
                        
                        show ava typical shy
                        
                        ava @ say "Y-yeah I totally get that haha!"
                        
                        show ava typical shocked
                        
                        ava @ say "Like I've come *this close* to kissing Gunner before but I'm still like, holding out in case he gives me the ick."
                        
                        if avaCommitted == True:
                            show ava typical enamored
                        
                            player "Well... I might be free. Just sayin'."
                            
                            show ava typical suggestive
                            
                            ava @ say "*Breee~*"
                            
                            show ava typical smug
                            
                            ava @ say "It'd be nice to explore that option soon~"
                            
                            show ava typical unimpressed
                            
                            ava @ say "But ugh midterms. I gotta go to class now. Maybe we can meet up later?"
                            #get coffee, just the two of us?
                            
                            player "I'd love to! Once all this midterm business is taken care of."
                            
                            show ava typical suggestive
                            
                            ava @ say "Can't wait~"
                        else:
                            player "You think you might have a backup plan?"
                            
                            show ava typical shy
                            
                            ava @ say "Hmmm... there's *someone* I've got my eyes on~"
                            
                            player "Who?"
                            
                            show ava typical unimpressed
                            
                            ava @ say "Someone really oblivious."
                            
                            player "Keeping it a secret, huh?"
                            
                            show ava typical unamused
                            
                            ava @ say "I'm really not."
                            
                            show ava typical happy
                            
                            ava @ say "I've gotta head to class now. See you later!"
                            
                            player "See ya!"
    
    
    ###claire bday scene goes here
    #claire "It was one hell of a birthday present!"
    
    stop music fadeout 2.0
    
    scene bg black with fade
    
    n "After classes end you suddenly get a sinking feeling in your gut."
    n "You could very well bomb these tests and have to retake classes, wasting valuable time and delaying your graduation."
    n "This is your last chance to prepare, better make it count."
    
    scene bg library with fade
    
    play music "audio/music/vylet - camelia.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
        
    #if you studied with claire last night then default this scene to the rose version
    
    $ randumb = renpy.random.randint(0, 1)
    
    if claireFrenchSession == 2:
        $ randumb = 0
    
    n "The library is packed with other students making their last stand. It's hard to even find a place to sit. Some are even sitting on the floor with their books sprawled out around them."    
    
    if randumb == 0:
        $ roseLibraryMidterms = True
        
        $ historySkill += 1
        
        n "Every available spot is taken. All except for one table with a single occupant emitting bitch aura so strong it repels all others."
        n "Be brave, [name]. Maybe if you sit at the far end she won't give you rabies."
        n "You try to sneakily pull out the chair and sit down before she notices."
        n "A sudden whizzing sound pierces the air followed by a stinging sensation on your hand, causing you to let go of the chair."
        
        player "Ow! What the fuck?"
        
        n "Looking down, you notice an ink splotch pooled in your fresh wound and a fountain pen lying on the ground."
        
        show rose skirt handonhip shy pendant at center with dissolve:
            ypos y_rose
            xzoom -1
        
        rose @ say "This table is reserved for God's chosen species. Get lost."
        
        menu:
            rose "{cps=0}This table is reserved for God's chosen species. Get lost.{/cps}"
            "All I see is a filthy raccoon.":
                $ rudeToRose += 1
                
                player "All I see here is a filthy trash panda."
                
                show rose skirt fistsclenched angry pendant
                
                rose @ say "And all I see is a barely evolved monkey taking up space and wasting valuable air!"
                
                player "I can't hear you over the sound of millennia of being the dominant species."
                
                rose @ say "Your extinction is long overdue!"
                
                player "And yet I'm still here."
                
                show rose skirt armscrossed dismissive pendant
                
                rose @ say "What have I done to deserve this hell?"
                
                menu:
                    rose "{cps=0}What have I done to deserve this hell?{/cps}"
                    "WTF is your problem?":
                        player "What the fuck is your problem? Why are you such a cunt?"
                        
                        show rose skirt armscrossed annoyed pendant
                        
                        rose @ say "Because I like being one."
                        
                        show rose skirt armscrossed smirk pendant
                        
                        rose @ say "It's a raccoon thing, you wouldn't get it."
                        
                        player "Nah, tons of people are cunts and you're not special."
                        
                        show rose skirt armscrossed dismissive pendant
                        
                        rose @ say "You mean that animalistic sort of reactionary tendency normies have? Please. You can barely think two steps ahead, let alone two hundred."
                        
                        show rose skirt armscrossed shy pendant
                        
                        rose @ say "Raccoons have a calculated view of the world and understand our place at the top. It's not our fault we're simply superior."
                        
                        player "So superior you ended up being trash gremlins once humans took over."
                        
                        show rose skirt fistsclenched angry pendant
                        
                        rose @ say "We're a species of survival! No matter what we always end up on top!"
                        rose @ say "The current age is proof of that! The human menace is nearly wiped out!"
                        
                        show rose skirt handonhip angry pendant at flipleft
                        
                        rose @ say "The past 5 presidents have been raccoons! The top 10 trillionaires are raccoons! The dean of our university is a raccoon!"
                        
                        show rose skirt handonhip smirk pendant
                        
                        rose @ say "It's our world and you're just living in it."
                        
                        player "I still don't get why you have to be such a bitch. The dean is a nice guy for a raccoon."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "He's gone soft. He has it all and there's no more power left for him to seek. So he likes to just be chill."
                        
                        show rose skirt handonhip dismissive pendant
                        
                        rose @ say "It's not like he'd tell you what he had to do to get where he is now."
                        
                        $ suspicionOfDean = True
                        
                        player "Whatever, I get it. Raccoons are simultaneously the most wrongfully persecuted group and the most powerful. Funny how that works."
                        
                        show rose skirt handonhip annoyed pendant
                        
                        rose @ say "You don't know a damn thing about the world, do you? I'll give you a hint, it's not at all like your cheap public education told you."
                        
                        player "Bitch I'm not even educated."
                        
                    "Karma for being a bitch":
                        player "Maybe it's just karma for you being such a bitch."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "Karma is something lesser species made up to feel good about themselves."
                        
                        player "It takes kindness and fairness to build a functioning society."
                        
                        show rose skirt handonhip smirk pendant
                        
                        rose @ say "That's what you think."
                        
                        player "What do you mean?"
                        
                    "I'm literally just existing":
                        player "I'm literally just existing here. Is that so bad?"
                        
                        show rose skirt handonhip angry pendant
                        
                        rose @ say "Ugh you don't even realize how terrible you are. It'd be sad if it weren't so disgusting!"
                        
                        player "What is your problem with humans? We basically built civilization from the ground up. You'd still be living in trees if not for us."
                        
                        show rose skirt handonhip furious pendant
                        
                        rose @ say "What an ignorant thing to say! And you genuinely believe it!"
                        
                        player "Uh yeah? Humans invented almost all the useful stuff while everyone else was living like their feral counterparts."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "This is your brain on human propaganda."
                        
                        player "What's that even supposed to mean?"
                        
                show rose skirt armscrossed dismissive pendant
                
                rose @ say "It's not my job to educate you."
                rose @ say "*Sigh*"
                rose @ say "...But I will if you do something for me."
                
                player "What?"
                
                show rose skirt armscrossed shy pendant
                
                rose @ say "Go get me a coffee. No sugar or milk. I will kill you if you bring me a coffee with that junk in it."
                rose @ say "I'm too deep in concentration to get it myself."
                
                n "She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?"
                
                menu:
                    n "{cps=0}She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?{/cps}"
                    "Go for it":
                        player "Fine whatever, I wanted to get one for myself anyway. After I listen to your lecture, I want to copy your notes for the midterm."
                        
                        show rose skirt armscrossed smirk pendant
                        
                        rose @ say "Deal."
                        
                        player "Be right back."
                        
                        call getRoseCoffee from _call_getRoseCoffee
                    "Fuck that":
                        $ frenchSkill += 1
                        $ statsSkill += 1
                        $ literatureSkill += 1
                        
                        $ rudeToRose += 1
                        
                        player "Screw that, get your own damn coffee. I don't need your raccoonist lecture about how I'm so terrible because of my ancestors."
                        
                        show rose skirt armscrossed dismissive pendant
                        
                        rose @ say "Typical human scum... Worthless."
                        
                        hide rose with dissolve
                        
                        n "You drop your backpack down onto the table and pull out your study material."
                        n "Stupid raccoon bitch, who does she think she is?"
                        n "You came here to study history but just looking at it makes you think of her."
                        n "You decide to study everything other than it."
                        n "You're better off in those classes now but you're not so sure you can ace the history test now. You'll just have to wing it cause it's getting late out."
                        n "You pack your things and get ready to leave but Rose looks like she's about to pull an all nighter."
                        
                        jump midtermDay1              
                
            "I belong here then.":
                player "Master species only? Then get out of my seat, trash panda."
                
                show rose skirt fistsclenched angry pendant
                
                rose @ say "How dare you insinuate you're anything more than a barely evolved monkey!"
                
                player "I can't hear you over the sound of millenia of being the dominant species."
                
                rose @ say "Your extinction is long overdue!"
                
                player "And yet I'm still here."
                
                show rose skirt armscrossed dismissive
                
                rose @ say "What have I done to deserve this hell?"
                
                menu:
                    rose "{cps=0}What have I done to deserve this hell?{/cps}"
                    "WTF is your problem?":
                        player "What the fuck is your problem? Why are you such a cunt?"
                        
                        show rose skirt armscrossed annoyed pendant
                        
                        rose @ say "Because I like being one."
                        rose @ say "It's a raccoon thing, you wouldn't get it."
                        
                        player "Nah, tons of people are cunts and you're not special."
                        
                        show rose skirt armscrossed dismissive pendant
                        
                        rose @ say "You mean that animalistic sort of reactionary tendency normies have? Please. You can barely think two steps ahead, let alone two hundred."
                        
                        show rose skirt armscrossed shy pendant
                        
                        rose @ say "Raccoons have a calculated view of the world and understand our place at the top. It's not our fault we're simply superior."
                        
                        player "So superior you ended up being trash gremlins once humans took over."
                        
                        show rose skirt fistsclenched angry pendant
                        
                        rose @ say "We're a species of survival! No matter what we always end up on top!"
                        rose @ say "The current age is proof of that! The human menace is nearly wiped out!"
                        
                        show rose skirt handonhip angry pendant at flipleft
                        
                        rose @ say "The past 5 presidents have been raccoons! The top 10 trillionaires are raccoons! The dean of our university is a raccoon!"
                        
                        show rose skirt handonhip smirk pendant
                        
                        rose @ say "It's our world and you're just living in it."
                        
                        player "I still don't get why you have to be such a bitch. The dean is a nice guy for a raccoon."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "He's gone soft. He has it all and there's no more power left for him to seek. So he likes to just be chill."
                        
                        show rose skirt handonhip dismissive pendant
                        
                        rose @ say "It's not like he'd tell you what he had to do to get where he is now."
                        
                        $ suspicionOfDean = True
                        
                        player "Whatever, I get it. Raccoons are simultaneously the most wrongfully persecuted group and the most powerful. Funny how that works."
                        
                        show rose skirt handonhip annoyed pendant
                        
                        rose @ say "You don't know a damn thing about the world, do you? I'll give you a hint, it's not at all like your cheap public education told you."
                        
                        player "Bitch I'm not even educated."
                        
                    "Karma for being a bitch":
                        player "Maybe it's just karma for you being such a bitch."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "Karma is something lesser species made up to feel good about themselves."
                        
                        player "It takes kindness and fairness to build a functioning society."
                        
                        show rose skirt handonhip smirk pendant
                        
                        rose @ say "That's what you think."
                        
                        player "What do you mean?"
                        
                    "I'm literally just existing":
                        player "I'm literally just existing here. Is that so bad?"
                        
                        show rose skirt handonhip angry pendant
                        
                        rose @ say "Ugh you don't even realize how terrible you are. It'd be sad if it weren't so disgusting!"
                        
                        player "What is your problem with humans? We basically built civilization from the ground up. You'd still be living in trees if not for us."
                        
                        show rose skirt handonhip furious pendant
                        
                        rose @ say "What an ignorant thing to say! And you genuinely believe it!"
                        
                        player "Uh yeah? Humans invented almost all the useful stuff while everyone else was living like their feral counterparts."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "This is your brain on human propaganda."
                        
                        player "What's that even supposed to mean?"
                        
                show rose skirt armscrossed dismissive pendant
                        
                rose @ say "It's not my job to educate you."
                rose @ say "*Sigh*"
                rose @ say "...But I will if you do something for me."
                
                player "What?"
                
                show rose skirt armscrossed shy pendant
                
                rose @ say "Go get me a coffee. No sugar or milk. I won't hesitate to kill you if you bring me a coffee with that junk in it."
                rose @ say "I'm too deep in concentration to get it myself."
                
                n "She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?"
                
                menu:
                    n "{cps=0}She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?{/cps}"
                    "Go for it":
                        player "Fine whatever, I wanted to get one for myself anyway. After I listen to your lecture, I want to copy your notes for the midterm."
                        
                        show rose skirt armscrossed smirk pendant
                        
                        rose @ say "Deal."
                        
                        player "Be right back."
                        
                        call getRoseCoffee from _call_getRoseCoffee_1
                    "Fuck that":
                        $ frenchSkill += 1
                        $ statsSkill += 1
                        $ literatureSkill += 1
                        
                        $ rudeToRose += 1
                        
                        player "Screw that, get your own damn coffee. I don't need your raccoonist lecture about how I'm so terrible because of my ancestors."
                        
                        show rose skirt armscrossed dismissive pendant
                        
                        rose @ say "Typical human scum... Worthless"
                        
                        hide rose with dissolve
                        
                        n "You drop your backpack down onto the table and pull out your study material."
                        n "Stupid raccoon bitch, who does she think she is?"
                        n "You came here to study history but just looking at it makes you think of her."
                        n "You decide to study everything other than it."
                        n "You're better off in those classes now but you're not so sure you can ace the history test now. You'll just have to wing it cause it's getting late out."
                        n "You pack your things and get ready to leave but Rose looks like she's about to pull an all nighter."
                        
                        jump midtermDay1                        
                
                
                
            "My mistake...":
                player "Sorry, my mistake... Here's your fountain pen back please don't stab me with it."
                
                n "She snatches the pen from your hand and returns to writing her notes like nothing ever happened."
                
                rose @ say "...What? Go on, shoo."
                rose @ say "Invasive species..."
                
                n "You look around at the table. It's full of open textbooks with print so tiny it strains your eyes to try reading them."
                
                player "Are you studying for the history midterm?"
                
                show rose skirt handonhip annoyed pendant
                
                rose @ say "You think I need to study for that class?"
                
                n "On the surface she sounds offended but you can sense a hint of pride, scoffing at the notion that she wouldn't be prepared."
                
                rose @ say "I'm doing PhD level independent work, gathering sources and making sense of a very contested point in history."
                
                menu:
                    rose "{cps=0}I'm doing PhD level independent work, gathering sources and making sense of a very contested point in history.{/cps}"
                    "Tell me more":
                        $ rosePoints += 1
                        
                        player "Sounds kinda interesting."
                        
                        show rose skirt handonhip dismissive pendant
                        
                        rose @ say "You wouldn't get it."
                        
                        if historySkill < 4:
                            player "You're right, I can barely even keep up in class. You're clearly the expert here."
                            
                            show rose skirt handonhip smirk pendant
                            
                            rose @ say "At least you acknowledge your inherent ineptitude."
                            
                            player "I still wanna know what it's about though."
                            
                            show rose skirt handonhip shy pendant
                            
                            n "Rose sighs and rolls her eyes."
                            
                        else:
                            player "Maybe not but I bet my ancestors were there. Considering how important humans were to every recorded historical event ever."
                            
                            n "Rose sets down her pen and stands up in her chair to get level with you."
                            
                            show rose skirt fistsclenched angry pendant
                            
                            rose @ say "Humanist propaganda!"
                            rose @ say "The only reason you egotistical freaks ended up at the forefront of history is because you *burned* everything else to the ground."
                            
                            show rose skirt armscrossed shy pendant
                            
                            n "With a 'hmph' she sits back down and resumes her reading, trying to regain her composure."
                            
                            player "Really? First time I've heard of it."
                        
                        rose @ say "Perhaps if you get me a coffee I'll attempt to educate you on how your kind are a blight on civilization."
                        rose @ say "If you can even understand it, that is."
                        
                    "Sounds boring":
                        player "Lame. Are you getting paid for it or something?"
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "I'm doing it out of my own interest. And it'll look good on a resume after I publish my results."
                        
                        player "What's it even about?"
                        
                        show rose skirt armscrossed dismissive pendant
                        
                        rose @ say "You wouldn't get it."
                        
                        if historySkill < 4:
                            player "You're right, I can barely even keep up in class. You're clearly the expert here."
                            
                            show rose skirt handonhip smirk pendant
                            
                            rose @ say "At least you acknowledge your inherent ineptitude."
                            
                            player "I still wanna know what it's about though."
                            
                            show rose skirt handonhip shy
                            
                            n "Rose sighs and rolls her eyes."
                            
                        else:
                            player "Maybe not but I bet my ancestors were there. Considering how important humans were to every recorded historical event ever."
                            
                            n "Rose sets down her pen and stands up in her chair to get level with you."
                            
                            show rose skirt fistsclenched angry pendant
                            
                            rose @ say "Humanist propaganda!"
                            rose @ say "The only reason you egotistical freaks ended up at the forefront of history is because you *burned* everything else to the ground."
                            
                            show rose skirt armscrossed shy pendant
                            
                            n "With a 'hmph' she sits back down and resumes her reading, trying to regain her composure."
                            
                            player "Really? First time I've heard of it."
                        
                        rose @ say "Perhaps if you get me a coffee I'll attempt to educate you on how your kind are a blight on civilization."
                        rose @ say "If you can even understand it, that is."      
                        
                n "She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?"
                
                menu:
                    n "{cps=0}She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?{/cps}"
                    "Go for it":
                        player "Fine whatever, I wanted to get one for myself anyway. How do you take it? Black like your soul?"
                        
                        rose @ say "Yes."
                        
                        player "Of course. Be right back."
                        
                        call getRoseCoffee from _call_getRoseCoffee_2
                        
                    "Fuck that":
                        $ frenchSkill += 1
                        $ statsSkill += 1
                        $ literatureSkill += 1
                        
                        $ rudeToRose += 1
                        
                        player "Screw that, get your own damn coffee."
                        
                        show rose skirt fistsclenched angry pendant
                        
                        rose @ say "Don't tell me what to do!"
                        
                        player "Shut up and go back to studying! I've got my own studies to take care of."
                        
                        rose @ say "Grrr..."
                        
                        hide rose with dissolve
                        
                        n "The two of you bury your noses in your books and pretend the other doesn't exist."
                        n "Just thinking about history is annoying you because she's such a nerd for it."
                        n "You decide to study everything other than it."
                        n "By the time you leave, Rose is still writing her report."
                        
                        jump midtermDay1
                
            "I'm sitting here regardless":    
                player "I'm sitting here whether you like it or not."
                player "I have a right to be here. It's the school's library, you don't own it."
                
                show rose skirt armscrossed smirk pendant
                
                rose @ say "I kinda do own it actually."
                rose @ say "I can just tell my grandpa you're harassing me and he'll get you expelled, blacklisted, sent to Guantanamo, suicided by two bullets in the back of your head..."
                rose @ say "Whichever I feel like."
                
                show rose skirt handonhip smug pendant
                
                $ suspicionOfDean = True
                
                player "Ooh yeah I'm real scared of your kind old grandpa who's friendly to me."
                ###if you've had coffee with him before mention it
                
                show rose skirt armscrossed shy pendant
                
                rose @ say "Looks can be deceiving. He can be ruthless. You have to be to get to where he is."
                
                player "Well let's just see what happens if I sit down."
                player "Oh wow nothing happened!"
                
                show rose skirt armscrossed furious pendant
                
                rose @ say "Nothing yet!"
                
                show rose skirt armscrossed annoyed pendant
                
                rose @ say "You're wasting my time. You're supposed to shut the fuck up in a library."
                
                player "You're the one who can't resist bitching me out!"
                
                rose @ say "It's the least you deserve!"
                
                player "I deserve a quiet space to study!"
                
                n "You shove Rose's books aside and set down your bag, pulling out your notebooks."
                
                show rose skirt armscrossed dismissive
                
                rose @ say "Ugh, human scum..."
                
                n "Rose just scoffs and puts in her earbuds, trying to ignore your existence."
                
                hide rose with dissolve
                
                n "About an hour into studying, you start to feel drowsy but you have so much material left to cover."
                n "Fffffuck you need a coffee if you're gonna survive. Luckily the cafe is only a short distance away."
                n "You won't have to worry about someone stealing your spot while you're away with Rose guarding the table, so you take a trip down to Coffee Zone."
                
                scene bg cafe autumn day with fade
                
                play music "audio/music/vylet - Guinea Pig Dreams.ogg" fadein .5
                
                show box:
                    ypos 0
                
                n "Coffee Zone is busier than you've ever seen it before. All the tables are taken and you have to wait in line before you can even see Mishka on the other side of the counter."
                n "Eventually you get to see the coffee queen rat, rushing to make everyone's orders all on her own."
                
                show mishka neutral at center with dissolve:
                    xzoom -1
                    #xpos -440
                    ypos y_mishka
                
                mishka @ say "[name]!"
                
                player "Hey Mishka! Is now a good time?"
                #Hope you don't mind me coming in on the busiest day of the year
                
                show mishka standing overjoyed
                
                mishka @ say "It gets so busy during exams week... But I will make the best drinks for you as always!"
                
                show mishka neutral -
                show mishka neutral standing
                
                player "You're the best Mishka."
                player "Take your time, I don't wanna rush you."
                
                show mishka anxious smile
                
                mishka @ say "Hah, thanks."
                
                show mishka neutral standing
                
                n "After you order, Mishka immediately gets to work on your drink."
                n "Would now be a good time to ask if she wants to hang out later?"
                n "She's pretty overworked but maybe once midterms are over you two will have some free time."
                
                menu:
                    n "{cps=0}She's pretty overworked but maybe once midterms are over you two will have some free time.{/cps}"
                    "\"You doing anything this weekend?\"":
                        $ mishkaPoints += 1
                        $ mishkaMidtermWeekendHangout = True
                    
                        player "Hey I was wondering if maybe you'd be free this weekend?"
                        
                        show mishka standing frown at flipleft
                        
                        mishka @ say "Sch-scho vy mayesh na-"
                        
                        n "The rat knocks over a ceramic mug, making a loud clattering noise. She hastily uprights the mug and turns to you."
                        
                        show mishka tired happy
                        
                        mishka @ say "Th-this weekend? I do not really have plans..."
                        
                        player "Great, neither do I! Would you wanna hang out?"
                        
                        show mishka standing wink 2 tongueout
                        
                        mishka @ say "Umm okay! We can do the hanging out!"
                        
                        show mishka -neutral
                        show mishka neutral standing
                        
                        player "Awesome! I'll figure out the details and let you know later, k?"
                        
                        mishka @ say "Of course, of course!"
                        
                        ###maybe later have an option where mishka's response changes if she likes or dislikes you
                    
                    "Now's not the time":
                        n "Nah, it's rude to ask her at work, especially when she's juggling orders like this."
                        
                n "You step back and let Mishka work on the drink and take more customer orders."
                n "The poor rat is going back and forth nonstop preparing multiple drinks at once yet doesn't miss a beat."
                n "A few minutes later she calls you up to the counter with the drink you asked for."
                
                player "Thanks! I have to get back to studying. Hopefully you find some time to study too!"
                
                show mishka mousey wink right
                
                mishka @ say "Oh don't worry about me... Dah skorovo!"
                
                player "See you around!"
                
                n "You take the cardboard cup and make your way back to the library."
                
                scene bg library with fade
                
                play music "audio/music/vylet - Every Little Thing She Does.ogg" fadein .5
                
                show box with Dissolve(.2):
                    ypos 0
                    
                n "You return to your seat across from Rose, reinvigorated to knock out this study session."
                
                show rose skirt handonhip shy pendant at center with dissolve:
                    ypos y_rose
                    
                n "The raccoon looks up from her book and sniffs the air."
                
                rose @ say "Coffee? Is that... ah it must be Costa Rican. My favorite type."
                
                show rose skirt handonhip smug pendant
                
                rose @ say "The best type."
                
                player "Yeah? I dunno I just got it from Coffee Zone."
                
                show rose skirt handonhip shy pendant
                
                rose @ say "Hm. I guess you're good for something after all. The scent of a hot drink makes reading all the more soothing."
                
                player "Wow is that a genuine compliment coming from you?"
                
                show rose skirt handonhip angry pendant
                
                rose @ say "Don't make the mistake of thinking I'm complementing *you.* A broken clock is right twice a day after all."
                
                show rose skirt handonhip dismissive pendant 
                
                rose @ say "You just happened to do something that enhanced my day. You should feel honored."
                
                #player "Riiiiiight."
                
                menu:
                    rose "{cps=0}You just happened to do something that enhanced my day. You should feel honored.{/cps}"
                    "Offer her a sip" if (rosePoints + historySkill) > 8:
                        $ rosePoints += 1
                        $ historySkill += 2
                        $ roseSip = True
                        
                        player "You want a sip? I haven't taken one yet."
                        
                        show rose skirt armscrossed dismissive pendant
                        
                        rose @ say "Psh, no."
                        
                        n "Rose narrows her eyes."
                        
                        show rose skirt armscrossed annoyed pendant
                        
                        rose @ say "You've only touched the outer sleeve around the cup, yes?"
                        
                        player "Yeah, why?"
                        
                        n "Rose gets up and walks over to you. She has to pull out a nearby chair and stand on top of it to reach the cup."
                        n "She takes hold of it, pulling it up out of the insulating sleeve and takes a long sip."
                        n "Well, chug is a more accurate term. Is she gonna leave any for you?"
                        
                        show rose skirt handonhip smug pendant
                        
                        n "She downs half the cup before setting it down with a satisfied sigh then returns to her seat across from you."
                        
                        show rose skirt handonhip shy pendant
                        
                        player "You're welcome?"
                        
                        rose @ say "I don't recall thanking you."
                        
                        player "Maybe you thought about it?"
                        
                        show rose skirt handonhip dismissive pendant
                        
                        rose @ say "Certainly not."
                        
                        player "The reward I get for trying to be nice..."
                        
                        show rose skirt handonhip annoyed pendant
                        
                        rose @ say "Expecting a reward for being nice just means you weren't being nice in the first place."
                        
                        show rose skirt handonhip shy pendant
                        
                        rose @ say "...But you can have my notes for the midterm as a consolation. I don't need them anymore and this saves me the trouble of disposing of them."
                        
                        player "Oh! I wasn't expecting that. Uh thanks."
                        
                        show rose skirt handonhip smug pendant
                        
                        rose @ say "Don't mention it, just bask in the glory of my flawless handwriting and excellent note structure."
                        
                        n "She flicks a sheet of paper toward you, landing perfectly in place for you to read."
                        
                        hide rose with dissolve
                        
                        n "Wow, she wasn't kidding! Rose's notes are incredibly neat and well-organized. Her handwriting consistency rivals that of a printer. Maybe she's onto something about raccoons being superior after all."
                        n "You feel like all the relevant information is laid out in the most straightforward way possible. This will definitely help boost your grade."
                        n "You start going over it and absorbing the knowledge."
                        
                        
                    "Keep it all to yourself":
                        player "You're welcome?"
                        
                        rose @ say "I don't recall thanking you."
                        
                        player "Maybe you thought about it?"
                        
                        rose @ say "Certainly not."
                        
                        n "Fucking bitch."
                        
                        hide rose with dissolve
                        
                        n "Now you're too annoyed by her to even look at your history notes. You'll have to study something else instead."
                        n "You end up briefly going over everything except history. You didn't absorb as much as you had hoped but you'll at least do a little better in your other classes."
                        
                
                
                jump midtermDay1
                
        
        
    
    else:
        $ avaLibraryMidterms = True
        
        n "Your only chance to find an open spot is when someone gets up and leaves. You drop down your bag and settle in before anyone else can steal it from you. It's your study spot now."
        n "By sheer coincidence, you find yourself bumping shoulders with a feathered friend."
        
        show ava typical happy at center with dissolve:
            ypos y_ava
        
        ava @ say "OMG hi [name]! Fancy seeing you here!"
        
        if avaMad == True:
            show ava typical embarrassed
            
            ava @ say "Sorry for getting pissy at you earlier."
            
            player "It's okay. I should have been more considerate about the Claire situation."
            
            show ava typical annoyed
            
            ava @ say "Yeah it's... well, I just wanna focus on passing my classes for now."
        
        else:
            player "Ava? Sorry, I didn't even see you there!"
        
        show ava typical whimsical
        
        ava @ say "This place gets soooo crowded during midterms, huh?"
        
        show ava typical happy
        
        player "Apparently! Might have to camp out for a spot next time!"
        
        show ava typical suggestive
        
        ava @ say "Oooh do you think they'd actually let us do that? Chirp!~"
        
        show ava typical smug
        
        player "Probably not. We'd have to be sneaky."
        
        show ava typical happy
        
        ava @ say "Hmmm... I might know a spot."
        
        show ava typical shocked
        
        ava @ say "But now's not the time! Midterms start tomorrow and I'm so not prepared aaaaaaaaa!!!"
        
        n "You look down at the bird's study materials sprawled out on the carpet."
        n "A notebook with flowery writing and sketches, her laptop plugged into her iconic camera transferring photos, and a stack of flash cards."

        player "I've got literature and French tomorrow. What are you working on?"
        
        show ava typical neutral
        
        ava @ say "I'm mostly worried about art history because I'm so bad at remembering dates!"
        
        show ava typical whimsical
        
        ava @ say "I usually space out in that class because so far it's all been like *ancient* stuff but I'm more of a modern bird ya know?"
        
        show ava typical happy
        
        ava @ say "So I've been making these flash cards to help me remember."
        
        player "Neat! I don't really do anything special when studying, I just read and pray I remember."
        
        ava @ say "You wanna try making some flash cards of your own? I've got plenty leftover!"
        
        menu:
            ava "{cps=0}You wanna try making some flash cards of your own? I've got plenty leftover!{/cps}"
            "Make some flash cards":
                $ avaPoints += 1
                $ literatureSkill += 1
                $ statsSkill += 1
                $ frenchSkill += 1
                
                player "Sure, I could give it a shot. We could quiz each other on our subjects too!"
                
                show ava typical excited
                
                ava @ say "Great idea!"
                
                hide ava with dissolve
                
                n "You start writing down some phrases from French on the cards and their translations on the back."
                n "After finishing a few that you know will be on the exam, you show them to Ava."
                
                player "Am I doing these right? Like this?"
                
                show ava typical happy at center with dissolve:
                    ypos y_ava
                
                ava @ say "Yup! Want me to read them out to you and you can try and answer them?"
                
                player "If that's supposed to help me memorize them better then yeah go for it."
                
                show ava typical excited
                
                ava @ say "It works wonders for some people!"
                
                show ava typical happy
                
                ava @ say "Ahem"
                
                ava @ say "Est-ce que j'ai bien dit ça?"
                
                show ava typical concerned
                
                ava @ say "Did I say that right?"
                
                player "You didn't give me a chance to answer!"
                
                show ava typical shocked
                
                ava @ say "Huh?"
                
                n "Ava looks at the back of the card to read the translation."
                
                ava @ say "\"Did I say that right?\""
                
                show ava typical unimpressed
                
                ava @ say "Very funny. Next one!"
                
                show ava typical neutral
                
                ava @ say "Comment prononcez-vous ces mots?"
                
                show ava typical unamused
                
                ava @ say "How do you even pronounce these?"
                
                player "You did it again!"
                
                show ava typical shocked
                
                ava @ say "What, really? Sorry! I don't know how to say these!"
                
                player "Just pretend the last letter of each word doesn't exist. That's usually how I do it."
                
                show ava typical happy
                
                ava @ say "Ok ok I think I got it."
                ava @ say "Je suis passionnée de photographie."
                
                show ava typical excited
                
                ava @ say "Oh I know what this says! \"I am passionate about photography!\""
                
                show ava typical suggestive
                
                ava @ say "Did you put that one in just for me?"
                
                show ava typical smug
                
                player "Heh no, but thanks for spoiling it for me."
                
                show ava typical whimsical
                
                ava @ say "Sorryyy! I guess I'm no good at this!"
                
                show ava typical happy
                
                player "It's alright. Want me to try doing your cards for you?"
                
                ava @ say "Sure!"
                
                hide ava with dissolve
                
                n "You pick up Ava's stack of flash cards and have more success reviewing her art history topics than your French ones."
                n "You even learn a few things about ancient art."
                
                #ava has sketches of ancient art on her cards?
                
            "Study independently":
                $ literatureSkill += 1
                $ frenchSkill += 1
                $ statsSkill += 2
                
                player "Thanks but I'll just stick to doing my own thing."
                
                show ava typical smug
                
                ava @ say "Oki! Lemme know if you wanna take a break and just chill for a bit!"
                
                player "Will do!"
                
                hide ava with dissolve
                
                n "You and Ava both study independently of each other but occasionally provide friendly distractions during momentary breaks."
                n "She shows you some photos she's working on editing for a project and gives you an overview of the history of art."
                n "You try showing her some of your French lessons but she has a hard time getting the hang of it."
                n "She's familiar with some of the books you've had to read for literature though and gives her impressions on them."
                
        n "You end up studying well into the evening alongside your birb friend. Looking out through the library's massive windows you can see it's already dark out."
        n "With a yawn, you start packing your things and try to get up from the floor but Ava grabs hold of your hand."
        
        show ava typical concerned at center with dissolve:
            ypos y_ava
        
        ava @ say "Going somewhere?"
        
        player "Uh yeah? It's getting late and the library is gonna close soon."
        
        show ava typical smug
        
        ava @ say "And?"
        
        player "And... I was gonna go back to my dorm and fall asleep?"
        
        show ava typical overjoyed
        
        ava @ say "Why not stay here with me?"
        
        show ava typical happy
        
        player "Here? At the library?"
        
        ava @ say "I wasn't kidding when I said it'd be fun to spend the night here!"
        
        menu:
            ava "{cps=0}I wasn't kidding when I said it'd be fun to spend the night here!{/cps}"
            "Stay here with Ava":
                $ avaPoints += 1
                $ literatureSkill -= 1
                $ frenchSkill -= 1
                $ avaLibraryAdventure = True
                
                ###cg of ava, mc, and claire hiding
                
                #player "You sure like to hang out in places you're not supposed to be."
                player "I'm down for it!"
                player "I could use a nice little adventure after studying all day!"
                
                show ava typical overjoyed
                
                ava @ say "Breeee! This is gonna be so much fun!"
                
                show ava typical smug
                
                ava @ say "We just have to find a good hiding spot and lay low when the staff does their final rounds."
                
                player "Any ideas?"
                
                show ava neutral
                
                ava @ say "Hmm...."
                
                pause .1
                
                show ava at flipright
                
                pause .6
                
                show ava at flipleft
                
                pause .6
                
                show ava at flipright
                
                pause .4
                
                show ava typical excited
                
                ava @ say "The individual study tables should work!"
                
                show ava typical happy
                
                ava @ say "They're enclosed from three sides and the open side faces the wall so we just have to crawl underneath a few minutes before closing time."
                
                player "Huh, that might actually work. Just gotta make sure nobody sees us."
                
                show ava typical smug
                
                ava @ say "Heh, maybe there's a book on sneaking we can check out first."
                
                show ava typical happy
                
                player "There's not that much time left. Almost everyone has left already. We better do it before they start closing for real."
                
                show ava typical motivated
                
                ava @ say "It's now or never!"
                
                hide ava with dissolve
                
                n "You and Ava nonchalantly make your way to the tables she was talking about. There's a row of them spaced out a few feet from each other and the last occupant just left."
                n "Looking around to make sure nobody is watching, you swiftly dive underneath one and pull the chair towards you."
                n "It's surprisingly roomy down here, and with the chair fully tucked in place, nobody would ever suspect a thing."
                n "You hear Ava do the same as you in the desk next to yours. Now all you have to do is wait."
                n "Your heart races as you become hypersensitive to all the sounds around you. Footsteps meander around and you hear disembodied voices of the staff chatting as they put stray books away."
                n "It feels like someone has been watching you... You can feel the vibrations of the floor as someone approaches your desk."
                n "Suddenly they veer off and you hear the clattering of chair against desk. Curiosity gets the better of you and you dare to take a peek."
                n "Seems Ava had the same idea. Both of you look to one side, watching a third party attempting to copy your hiding strategy."
                
                show claire sweater flustered at center with dissolve:
                    ypos y_claire
                    xoffset 550
                
                claire @ say "I think I'm stuck..."
                
                show ava typical shocked at center with dissolve:
                    ypos y_ava
                    xoffset -550
                    xzoom -1
                
                ava @ say "Claire?! What on Earth are you doing??"
                
                show claire sweater derp
                
                claire @ say "I could ask you the same thing!"
                
                show claire sweater happy
                
                claire @ say "I saw you and [name] swoop underneath these desks and thought that looked fun, so why don't I try it myself!"
                
                show ava typical angry
                
                ava @ say "You're gonna blow our cover!!"
                
                show claire sweater giggle
                
                claire @ say "That's not the only thing I'll blow~ Ksksksksksks!"
                
                show claire sweater suggestive earsup
                
                claire @ say "What are you two even up to, I wonder~"
                
                show ava typical unamused
                
                player "We're trying to stay the night in the library. It was kind of a spontaneous idea."
                
                show claire sweater happy
                
                claire @ say "Ooh the forbidden sleepover~ Mind if I join in?"
                
                player "Sorry but you're too big to even fit under there."
                
                show ava typical shocked
                
                ava @ say "Yeah, you're gonna get us all caught the moment someone walks by!"
                
                show claire sweater sad
                
                claire @ say "B-but-"
                claire @ say "I don't wanna miss out...!"
                claire @ say "You're gonna try stealing [name] from me, aren't you?!"
                
                show ava typical angry
                
                ava @ say "OMG stop being such a drama queen!"
                
                menu:
                    ava "{cps=0}OMG stop being such a drama queen!{/cps}"
                    "Claire can stay":
                        $ clairePoints += 1
                        $ claireLibraryAdventure = True
                    
                        player "*Sigh*"
                        player "This is so dumb."
                        player "Fine, you can stay Claire, but we're not bailing you out if you get caught."
                        
                        show claire sweater overjoyed
                        show ava typical neutral
                        
                        claire @ say "Yisssss!!! I'll be super sneaky, they won't know a thing!"
                        
                        show claire sweater happy
                        
                        ava @ say "Ugh, I hope this doesn't blow up in our faces."
                        
                        show claire sweater surprised earsup
                        show ava typical shocked
                        
                        player "Quiet down! They're shutting off the lights!"
                        
                        hide ava
                        hide claire
                        with dissolve
                        
                        n "You retreat back into your hidden alcove. It's starting to hurt your back being hunched over like this. You wonder how long you'll have to wait before it's safe to leave."
                        n "There's no way someone won't spot Claire."
                        n "Right?"
                        
                        scene bg library night with dissolve
                        
                        play music "audio/music/vylet - explorer.ogg" fadein .5
                        
                        show box:
                            ypos 0
                        
                        n "One by one, groups of lights shut off around you until you're in darkness and the voices of staff members fades away. All that's left now is the hum of the heating unit."
                        
                        call phone_start from _call_phone_start_24 
                        
                        call message_start("Ava", "You think we're good to come out now?", "avaavi.png") from _call_message_start_31 

                        call reply_message("Give it a couple minutes to be safe") from _call_reply_message_160 
                        
                        call message("Ava", "I can't believe Claire's fat ass didn't get caught", "avaavi.png") from _call_message_225 
                        
                        call message("Claire", "Ikr!!", "claireavi.png") from _call_message_226 
                        call message("Claire", "I think my butt is stuck", "claireavi.png") from _call_message_227 
                        
                        call reply_message("We'll help you out") from _call_reply_message_161 
                        
                        call message("Ava", "I think they're locking up now", "avaavi.png") from _call_message_228 
                        
                        call message("Claire", "This is sooo exciting!", "claireavi.png") from _call_message_229 
                        call message("Claire", "How did you guys come up with this idea lol", "claireavi.png") from _call_message_230 
                        
                        call message("Ava", "There's just something so interesting about school buildings at night!", "avaavi.png") from _call_message_231 
                        
                        call reply_message("It gives me chill bumps") from _call_reply_message_162 
                        call reply_message("Do birds get those?") from _call_reply_message_163 
                        
                        call message("Ava", "Noope :P", "avaavi.png") from _call_message_232 
                        call message("Ava", "lemme feel em when we get out of here lol", "avaavi.png") from _call_message_233 
                        
                        call message("Claire", "I call dibs on first touch", "claireavi.png") from _call_message_234 
                        
                        call reply_message("Sure lol") from _call_reply_message_164 
    
                        call phone_end from _call_phone_end_30
                        
                        n "A few minutes pass and you feel comfortable leaving your hiding spot. You push away the chair then go to pull the other one out for Ava."
                        
                        show ava glowy happy at center with dissolve:
                            ypos y_ava
                            xoffset -550
                            xzoom -1
                        
                        pause .1
                        
                        show ava glowy suggestive
                        
                        ava @ say "What a gentleman~"
                        
                        show ava glowy smug
                        
                        n "The dim glow from the ambient light leaking through the windows illuminates Ava's soft white feathers, revealing markings that normally aren't visible."
                        
                        if avaUrbex == True:
                            player "Hey, I can see your feather markings again!"
                            
                            show ava glowy unsure
                            
                            ava @ say "Oh?"
                            
                            show ava glowy whimsical
                            
                            ava @ say "Must be the coating on the windows polarizing the outside light or something that's making them visible for ya."
                            
                            show ava glowy unamused
                            
                            ava @ say "A shame most people can't see them all the time."
                            
                            if avaPoints > 5:
                                player "Do you have more markings? Like on your back?"
                                
                                show ava glowy suggestive
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                show ava glowy smug
                                
                                player "Aw."
                                
                                show ava glowy flattered
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                show ava glowy smug
                                
                                player "Fair."
                                
                            
                        else:
                            player "Whoa, you're... glowing."
                            
                            show ava glowy embarrassed
                            
                            ava @ say "Huh?"
                            
                            player "You've got spirals and stuff on your wings now!"
                            
                            show ava glowy concerned
                            
                            ava @ say "Yeah? They've always been there."
                            
                            show ava glowy whimsical
                            
                            ava @ say "Ohhh you can't normally see 'em though. Forgot, they're near ultraviolet."
                            
                            show ava glowy suggestive
                            
                            ava @ say "There's probably some polarized light coming through the windows letting you see it."
                            
                            if avaPoints > 5:
                                player "Do you have more markings? Like on your back?"
                                
                                show ava glowy suggestive
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                player "Aw."
                                
                                show ava glowy flattered
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                show ava glowy smug
                                
                                player "Fair."
                        
                        show ava glowy unsure
                                
                        claire @ say "Guys? I'm still stuck!"
                        
                        show ava glowy unamused
                        
                        ava @ say "Right, I forgot about her."
                        
                        player "We're coming, Claire."
                        
                        n "You and Ava grab hold of Claire's paws and pull with all your might. It takes a coupe of good yanks to finally dislodge her rear from the underside of the table."
                        
                        show claire sweater derp at center with dissolve:
                            ypos y_claire
                            xoffset 550
                                
                        claire @ say "Thanks! Ksksksks~"
                        
                        show claire sweater happy
                        show ava glowy happy
                        
                        claire @ say "Are we in the clear?"
                        
                        player "Seems like it. I don't see any guards or hear any alarms."
                        
                        show ava glowy excited
                        
                        ava @ say "The library is ours for the night!"
                        
                        show ava glowy unsure
                        show claire sweater overjoyed
                        
                        claire @ say "Woo!! Library sleepover!!!"
                        
                        ava @ say "Shshshshs!!! Somebody outside could still hear us!"
                        
                        show claire sweater sad
                        show ava glowy grouchy
                        
                        claire @ say "Sowwy."
                        
                        show claire sweater surprised earsup
                        show ava glowy happy
                        
                        player "So... now what?"
                        
                        ava @ say "I don't really know. I didn't think we'd get this far."
                        
                        player "I mean, it's late and we have midterms tomorrow. We can't exactly stay up all night painting each other's nails."
                        
                        show ava glowy whimsical
                        
                        ava @ say "How about we just... make a fort out of books and fall asleep in it?"
                        
                        show claire sweater pose laughing
                        
                        claire "Sounds good to me!"
                        
                        player "We're gonna need some big books."
                        
                        hide claire
                        hide ava
                        with dissolve
                        
                        n "The next half hour is spent finding books thick enough to serve as the base for your fort then filling out the rest with whatever manuscripts fit well enough."
                        n "You even manage to form an entrance with an archway that seems stable but leaves you in fear of it all toppling down on you."
                        
                        show claire sweater overjoyed at center:
                            ypos y_claire
                            xoffset 550
                        show ava glowy smug at center:
                            ypos y_ava
                            xzoom -1
                            xoffset -550
                        with dissolve
                
                        claire @ say "It's glorious!"
                        
                        show ava glowy suggestive
                        show claire sweater happy
                
                        ava @ say "I must say, this is quite an impressive fort!"
                        
                        show ava glowy whimsical
                        
                        ava @ say "I don't think we ever could have built such a thing during normal operating hours! The staff would have thrown a fit!"
                        
                        show ava glowy happy
                        
                        player "It'll be a fun surprise for them to find in the morning after we've left!"
                        
                        n "Inside is just roomy enough for you to sit upright. Ava built a nest of paperback books for you to curl up and sleep in."
                        
                        ava @ say "I tried to find the softest ones to sleep on."
                        
                        player "It beats sleeping on the ground in the woods."
                        
                        show claire sweater flustered
                        
                        claire @ say "Hey, I at least provided a soft bnnuy for you to lean back on!"
                        
                        show ava glowy flattered
                        
                        ava @ say "How about a soft bird this time instead?"
                
                        menu:
                            ava "{cps=0}How about a soft bird this time instead?{/cps}"
                            "Bnnuy":
                                player "Sorry Ava but I can't resist the bnnuy pillow."
                                
                                show claire sweater giggle
                                show ava glowy flattered
                                
                                ava @ say "Aww... I understand though, Claire is a top tier cuddler~"
                                
                                show claire sweater leaning suggestive
                                show ava glowy happy
                                
                                claire @ say "Everyone needs a big beautiful bunny~"
                                
                                n "Claire pulls you into her grasp, inescapable yet comforting."
                                
                                show claire sweater pose happy
                                
                                player "So warm and soft~"
                                
                                if claireBullyLevel > 0:
                                    show claire sweater pose suggestive earsup
                                
                                    claire @ say "Who's my little snuggleslut?"
                                    
                                    show ava glowy unsure
                                    
                                    player "Meeeee!~"
                                    
                                    ava @ say "What have you done to him?"
                                    
                                    claire @ say "Don't worry, he likes it~"
                                    
                                show claire sweater pose happy
                                show ava glowy happy
                                    
                                claire @ say "Now shush up and get some rest. We all got midterms tomorrow!"
                            
                            "Birb":
                                player "I'll take the birb this time."
                                
                                show ava glowy embarrassed
                                show claire sweater sad
                                
                                claire @ say ":skull::skull::skull:"
                                
                                show ava glowy whimsical
                                
                                ava @ say "I may not be a good mattress like Claire but I can be a good pillow~"
                            
                                n "Ava snuggles up to you, enveloping you in her soft feathers while Claire pouts beside you."
                                
                                show ava glowy concerned
                                
                                ava @ say "Don't be jealous~"
                                
                                claire @ say "It should have been meeeee!"
                                
                                player "Sorry Claire, this bird has been tempting me."
                                
                                show claire sweater pose suggestive earsup
                                
                                claire @ say "I don't blame you, she's been tempting me too!"
                                
                                show ava glowy embarrassed
                                
                                ava @ say "W-what?? Tempting you how?!"
                                
                                show claire sweater laughing
                                
                                claire @ say "Ksksksksks wouldn't you like to know~"
                                
                                show ava glowy angry
                            
                                ava @ say "Go to sleep, you creature!"
                                
                                player "Yeah, we have midterms tomorrow."
                                
                                show claire sweater happy
                                
                                claire @ say "Fiiine. G'night y'all!"
                            
                            
                            "Why not both?":
                                player "Why not both?"
                                
                                show ava glowy whimsical
                                
                                ava @ say "Geez, what a snuggle whore."
                                
                                show claire sweater leaning suggestive
                                
                                claire @ say "Don't listen to her, [name], I believe in snuggle positivity! It's perfectly valid to cuddle with lots of people!"
                                
                                show claire sweater laughing
                                
                                claire @ say "Also that's rich coming from you, Ava! Snuggle any catboys recently?"
                                
                                if avaPoints > 6:
                                    show ava glowy angry
                                    show claire sweater happy
                                
                                    ava @ say "As a matter of fact, no I have not!"
                                else:
                                    show ava glowy angry
                                    show claire sweater happy
                                    
                                    ava @ say "Maybe I have, so what! At least I kept my pants on!"
                                    
                                    claire @ say "For now~"
                                
                                player "Can we all just chill out and enjoy the present snuggles?"
                                
                                claire @ say "That's what I'm trying to do!"
                                
                                show ava glowy grouchy browless
                                show claire sweater pose suggestive
                                
                                claire @ say "Get in here, Ava!"
                                
                                n "Claire pulls Ava in as well, sandwiching you between the two ladies."
                                
                                claire @ say "Comfy?"
                                
                                player "Very."
                                
                                show ava glowy suggestive
                                
                                ava @ say "Yup!"
                                
                                claire @ say "Good~ Now shush up and get some rest. We all got midterms tomorrow!"
                            
                            "Neither":
                                player "I'm good. I've already settled into this stack of National Geographics."
                                
                                show claire sweater derp
                                show ava glowy grouchy browless
                                
                                claire @ say "Suit yourself!"
                                
                                show claire sweater happy
                                
                                claire @ say "I just hope you don't mind if Ava and I snuggle right here."
                                
                                show ava glowy unamused
                                
                                ava @ say "Who said I'd snuggle with you?!"
                                
                                show claire sweater pose suggestive
                                
                                claire @ say "Come on, I know you can't resist this soft bunny~"
                                
                                show ava glowy whimsical
                                
                                ava @ say "It's true, you're like a mother hen guarding her babies."
                                
                                show claire sweater happy
                                
                                claire @ say "Get over here and get some snuggles~"
                                
                                show ava glowy suggestive
                                
                                ava @ say "Fiiine~"
                                
                                show ava glowy smug
                                
                                n "Ava scooches over and gets embraced by Claire while you flip through some of the magazines lining the floor."
                                
                                claire @ say "Comfy?"
                                
                                ava @ say "Hehe yup!"
                
                                claire @ say "What about you, [name]? It's not too late to join the cuddles~"
                                
                                player "I'm good, thanks."
                                player "I was thinking of getting some sleep soon though. We all got midterms tomorrow and I wanna be rested up."
                                
                                claire @ say "Yeah, I wish we could stay up late but that's probably for the best."
                                claire @ say "Night guys!"
                        
                        
                        hide ava
                        hide claire
                        with dissolve
                                    
                        n "It's not easy falling asleep in an unfamiliar place, especially with the paranoia of getting caught."
                        n "You're keenly aware of every sound in the building, getting a mini heart attack each time a new one appears."
                        n "What's that? Did something just beep? It kinda sounded like the front door just opened."
                        
                        player "Wait- did you hear that just now?"
                        
                        show ava glowy unsure at center with dissolve:
                            ypos y_ava
                            xzoom -1
                            xoffset -350
                        
                        ava @ say "Was the the main entrance? Oh shit I think someone's coming!"
                        
                        show claire sweater surprised earsup at center with dissolve:
                            ypos y_claire
                            xoffset 400
                        
                        claire @ say "Abandon ship!"
                        
                        pause .1
                        
                        show ava at offscreenright:
                            ypos y_ava
                            xoffset 800
                        show claire at offscreenleft:
                            ypos y_claire
                            xoffset -800
                        with move
                        
                        n "Scrambling out of your book fort, you dodge the beams coming from a security guard's flashlight and remain unseen... for now."
                        n "You did manage to get separated from Ava and Claire in the process however."
                        n "Your body tenses up, instinctively holding your breath trying to avoid detection. You creep around a bookcase while the guard investigates your fortress."
                        
                        guard "Hey! Is someone there?"
                        
                        n "There's too many gaps in this shelf after you took so many books for the fort! You're a sitting duck!"
                        
                        show ava at center with move:
                            xzoom 1
                            xoffset 700
                            ypos y_ava
                        
                        ava @ say "Squawk!"
                        
                        pause .1
                        
                        show ava at offscreenright with move:
                            ypos y_ava
                            xoffset 700
                        
                        guard "Show yourself!"
                        
                        n "The guard turns his attention to Ava's distraction, giving you time to get away."
                        n "You find a relatively concealed spot but now it sounds like Ava's in trouble."
                        
                        guard "Alright, I see you! Come on out, birdie."
                        
                        menu:
                            guard "{cps=0}Alright, I see you! Come on out, birdie.{/cps}"
                            "Make a distraction":
                                n "You'll be giving up your perfect hiding spot but at least you'll take the heat off Ava."
                                n "Just as you're about to draw the guard's attention, Claire whistles to get his attention."
                            
                            "Stay quiet":
                                n "Sorry Ava, you should have hidden better."
                                
                                guard "Stop right there!"
                                      
                                show ava at center with move:
                                    xzoom 1
                                    xoffset 700
                                    ypos y_ava
                                                                        
                                ava @ say "Eek!"
                                
                                n "Just as the guard is about to apprehend Ava, Claire whistles to get his attention."
                                
                        n "She somehow climbed on top of a bookshelf and was towering over the guard."
                        
                        show claire sweater surprised earsup at center with move:
                            ypos y_claire
                            xoffset -650
                            xzoom -1
                                
                        claire @ say "Get out of here guys, I'll take him on!"
                        
                        n "The last thing you see is Claire jumping onto the guard, dropping him to the ground and causing the whole floor to shake before Ava takes your hand and pulls you to the exit."
                        
                        scene bg campus autumn night with fade
                        
                        play music "audio/ambient/outdoors night crickets.ogg" fadein .5
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        n "Outside, you lurk in the shadows waiting to see the result of the rabbit's scuffle with the guard."
                        
                        show claire sweater happy at center:
                            xoffset -2000
                        
                        show ava typical concerned at center with dissolve:
                            ypos y_ava
                            xoffset 500
                        
                        ava @ say "Oh my gosh, do you think she's okay? Should we go in and back her up?"
                        
                        player "Either she sacrificed herself for us or she'll emerge victorious in combat."
                        
                        show ava typical shocked
                        
                        n "A few minutes pass by and then a lone figure's sillouette appears behind the glass door."
                        n "Is that...?"
                        
                        show claire sweater happy at center with dissolve:
                            ypos y_claire
                            xoffset -400
                            xzoom -1
                        show ava typical overjoyed
                        
                        ava @ say "Claire!!! You made it!"
                        
                        n "Ava swoops in to give her a hug."
                        
                        pause .1
                        
                        show ava with move:
                            xoffset -200
                            
                        pause .4
                        
                        show ava with move:
                            xoffset 200
                        
                        show ava typical smug
                        show claire sweater flustered
                        
                        claire @ say "Haha someone's happy to see me~"
                        
                        player "We thought you got arrested!"
                        
                        show claire sweater derp
                        
                        claire @ say "That guard wasn't so tough!"
                        
                        show claire sweater happy
                        
                        claire @ say "Some basic judo was enough to knock him out cold!"
                        
                        player "Holy shit, you didn't have to assault an officer of the law for our sake."
                        
                        claire @ say "I know, but it sounded like fun~ So I did it anyway!"
                        
                        show ava typical shocked
                        
                        ava @ say "I'm glad we all made it out! That would have been such a nightmare the day before midterms!"
                        
                        claire @ say "I know right! Speaking of which, it's gotten pretty late hasn't it?"
                        
                        show ava typical happy
                        
                        player "That's more than enough excitement for the night. Come on, let's all get some rest before exams begin."
                        
                        hide ava
                        hide claire
                        with dissolve
                        
                        n "You walk Ava and Claire to their dorm, still riding the high from escaping the library."
                        n "Your heart's still racing by the time you make it back to your dorm but eventually the exhaustion catches up with you and you fall asleep."
                        
                         
                        
                    
                    "Claire must go":
                        $ clairePoints -= 1
                    
                        player "Sorry Claire, you gotta go. It's risky enough as it is with just me and Ava."
                        
                        claire @ say "I see how it is..."
                        
                        show ava pose concerned
                
                        ava @ say "It's nothing personal, there's just no way this could work."
                        
                        claire @ say "Yeah, I guess so."
                        
                        n "Claire emerges from under her table and gives you a wave before hopping away."
                        
                        show claire sweater derp
                        
                        claire @ say "Good luck! Don't get caught!"
                        
                        hide claire
                        hide ava
                        with dissolve
                        
                        n "You wave back and return to your hidden alcove. It's starting to hurt your back being hunched over like this. You wonder how long you'll have to wait before it's safe to leave."
                        
                        scene bg library night with dissolve
                        
                        play music "audio/music/vylet - explorer.ogg" fadein .5
                        
                        show box:
                            ypos 0
                        
                        n "One by one, groups of lights shut off around you until you're in darkness and the voices of staff members fades away. All that's left now is the hum of the heating unit."
                        
                        call phone_start from _call_phone_start_25 
                        
                        call message_start("Ava", "You think we're good to come out now?", "avaavi.png") from _call_message_start_32 

                        call reply_message("Give it a couple minutes to be safe") from _call_reply_message_165 
                        
                        call message("Ava", "Kay", "avaavi.png") from _call_message_235 
                        call message("Ava", "I can't believe we're doing this!!", "avaavi.png") from _call_message_236 
                        
                        call reply_message("I know right?") from _call_reply_message_166 
                        call reply_message("You sure love being in weird places don't you?") from _call_reply_message_167 
                        
                        call message("Ava", "Guilty as charged~ ^v^", "avaavi.png") from _call_message_237 
                        call message("Ava", "There's just something so interesting about school buildings at night!", "avaavi.png") from _call_message_238 
                        
                        call reply_message("It gives me chill bumps") from _call_reply_message_168 
                        call reply_message("Do birds get those?") from _call_reply_message_169 
                        
                        call message("Ava", "Noope :P", "avaavi.png") from _call_message_239 
                        call message("Ava", "lemme feel em when we get out of here lol", "avaavi.png") from _call_message_240 
                        
                        call reply_message("Sure lol") from _call_reply_message_170 
    
                        call phone_end from _call_phone_end_31
                        
                        n "A few minutes pass and you feel comfortable leaving your hiding spot. You push away the chair then go to pull the other one out for Ava."
                        
                        show ava glowy happy at center with dissolve:
                            ypos y_ava
                            xoffset -550
                            xzoom -1
                        
                        pause .1
                        
                        show ava glowy suggestive
                        
                        ava @ say "What a gentleman~"
                        
                        show ava glowy smug
                        
                        n "The dim glow from the ambient light leaking through the windows illuminates Ava's soft white feathers, revealing markings that normally aren't visible."
                        
                        if avaUrbex == True:
                            player "Hey, I can see your feather markings again!"
                            
                            show ava glowy unsure
                            
                            ava @ say "Oh?"
                            
                            show ava glowy whimsical
                            
                            ava @ say "Must be the coating on the windows polarizing the outside light or something that's making them visible for ya."
                            
                            show ava glowy unamused
                            
                            ava @ say "A shame most people can't see them all the time."
                            
                            if avaPoints > 5:
                                player "Do you have more markings? Like on your back?"
                                
                                show ava glowy suggestive
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                show ava glowy smug
                                
                                player "Aw."
                                
                                show ava glowy flattered
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                show ava glowy smug
                                
                                player "Fair."
                                
                            
                        else:
                            player "Whoa, you're... glowing."
                            
                            show ava glowy embarrassed
                            
                            ava @ say "Huh?"
                            
                            player "You've got spirals and stuff on your wings now!"
                            
                            show ava glowy concerned
                            
                            ava @ say "Yeah? They've always been there."
                            
                            show ava glowy whimsical
                            
                            ava @ say "Ohhh you can't normally see 'em though. Forgot, they're near ultraviolet."

                            show ava glowy suggestive
                            
                            ava @ say "There's probably some polarized light coming through the windows letting you see it."
                            
                            if avaPoints > 5:
                                player "Do you have more markings? Like on your back?"
                                
                                show ava glowy suggestive
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                player "Aw."
                                
                                show ava glowy flattered
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                show ava glowy smug
                                
                                player "Fair."
                                
                        show ava glowy happy
                            
                        ava @ say "So I guess we're in the clear?"
                        
                        player "Seems like it. I don't see any guards or hear any alarms."
                        
                        show ava glowy excited
                        
                        ava @ say "Then the library is ours for the night!"
                        
                        show ava glowy happy
                        
                        player "Just gotta hope nobody's watching the cameras."
                        
                        show ava glowy unamused
                        
                        ava @ say "There must be thousands of security cams around the university. There's no way someone will happen to see us."
                        
                        show ava glowy unsure
                        
                        ava @ say "Try and stay out of their field of view though just in case."
                        
                        player "So... now what?"
                        
                        show ava glowy waitwhat
                        
                        ava @ say "I don't really know. I didn't think we'd get this far."
                        
                        player "I mean, it's late and we have midterms tomorrow. We can't exactly stay up all night painting each other's nails."
                        
                        show ava glowy whimsical
                        
                        ava @ say "How about we just... make a fort out of books and fall asleep in it?"
                        
                        player "Sounds good to me!"
                        
                        hide ava with dissolve
                        
                        n "The next half hour is spent finding books thick enough to serve as the base for your fort then filling out the rest with whatever manuscripts fit well enough."
                        n "You manage to form an entrance with an archway that seems stable but leaves you in fear of it all toppling down on you."
                        
                        show ava glowy suggestive at center with dissolve:
                            xzoom -1
                            ypos y_ava
                
                        ava @ say "I must say, this is quite an impressive fort!"
                        
                        show ava glowy excited
                        
                        ava @ say "I don't think we ever could have built such a thing during normal operating hours! The staff would have thrown a fit!"
                        
                        show ava happy
                        
                        player "It'll be a fun surprise for them to find in the morning after we've left!"
                        
                        n "Inside is just roomy enough for you to sit upright. Ava built a nest of paperback books for you to curl up and sleep in."
                        
                        show ava glowy suggestive
                        
                        ava @ say "I tried to find the softest ones to sleep on."
                        
                        show ava glowy smug
                        
                        player "It beats sleeping on the ground in the woods."
                        player "No soft bunny though."
                        
                        show ava glowy suggestive
                        
                        ava @ say "How about a soft bird instead?"
                        
                        show ava glowy smug
                
                        player "That'll do."
                        
                        n "Ava snuggles up to you, enveloping you in her soft feathers."
                        
                        if avaPoints > 6:
                            n "This is comfy but you know what could be comfier?"
                            
                            player "Can I make a request?"
                            
                            show ava glowy waitwhat
                            
                            ava @ say "Is it lewd?"
                            
                            player "..."
                            player "A little."
                            
                            show ava glowy smug
                            
                            ava @ say "What is it?"
                            
                            menu:
                                ava "{cps=0}What is it?{/cps}"
                                "Use her boobs as a pillow":
                                    show ava glowy embarrassed
                                
                                    player "I bet your boobs would be the best pillow I've ever slept on. Can I rest my head on 'em?"
                                    
                                    show ava glowy flattered
                                    
                                    ava @ say "You're lucky I like you or I woulda slapped you."
                                    
                                    player "Is that a yes then?"
                                    
                                    ava @ say "It's no goose down but my feathers are pretty soft~"
                                    
                                    show ava glowy smug
                                    
                                    ava @ say "Go ahead, humie~"
                                    
                                    n "You maneuver into place and rest your head on her plush breasts. This beats even those super soft pillows hotels have."
                                    
                                    ava @ say "Ya like it?"
                                    
                                    player "It's perfect~"
                                    
                                    show ava glowy suggestive
                                    
                                    ava @ say "*Chirp*!"
                                    
                                    show ava glowy flattered
                                    
                                    ava @ say "I'm glad you're comfy~"
                                "Use her butt as a pillow":
                                    show ava glowy embarrassed
                                
                                    player "I bet your butt would be the best pillow I've ever slept on. Can I rest my head on it?"
                                    
                                    show ava glowy flattered
                                    
                                    ava @ say "You're lucky I like you or I woulda slapped you."
                                    
                                    player "Is that a yes then?"
                                    
                                    ava @ say "It's no goose down but my feathers are pretty soft~"

                                    show ava glowy smug
                                    
                                    ava @ say "Go ahead, humie~"
                                    
                                    n "You maneuver into place and rest your head on her plush ass. This beats even those super soft pillows hotels have."
                                    
                                    ava @ say "Ya like it?"
                                    
                                    player "It's perfect~"
                                    
                                    show ava glowy suggestive
                                    
                                    ava @ say "*Chirp*!"
                                    
                                    show ava glowy flattered
                                    
                                    ava @ say "I'm glad you're comfy~"
                                "Nevermind":
                                    player "Nevermind, it was a dumb thought."
                                    
                                    show ava glowy grouchy browless
                        
                                    n "Ava shrugs."
                                    
                                    ava @ say "Whatever you say~"
                                    
                                    show ava glowy flattered
                                    
                                    ava @ say "I guess I'm flattered you had a lewd thought about me though!"
                                    
                                    player "...Do you have lewd thoughts about me?"
                                    
                                    show ava glowy unsure
                                    
                                    ava @ say "Sometimes!~"
                                    
                                    player "Care to share any of them?"
                                    
                                    show ava glowy suggestive
                                    
                                    ava @ say "Well you didn't share yours so... nope!"
                                    
                                    player "Darn."
                                    
                        show ava glowy happy
                                    
                        ava @ say "Let's try and get some rest now. Got those midterms in the morning after all!"
                        
                        player "Yeah. Goodnight! Sleep tight!"
                        
                        show ava glowy smug
                        
                        ava @ say "Nighty night!"
                        
                        hide ava with dissolve
                                    
                        n "You close your eyes, feeling as though sleep could overtake you at any moment, yet it never comes."
                        n "Ava seems to be having trouble falling asleep as well."
                        n "She tosses and turns even though it's past midnight."
                        
                        show ava glowy unamused at center with dissolve:
                            ypos y_ava
                            
                        pause .3
                        
                        show ava at flipright
                        
                        pause .8
                        
                        show ava at flipleft
                        
                        pause .6
                        
                        ava @ say "...I can't sleep."
                        
                        player "Me neither."
                        
                        ava @ say "You anxious about the exams?"
                        
                        player "A little bit. You?"
                        
                        ava @ say "Same."
                        
                        show ava glowy unsure
                        
                        ava @ say "But I think staying the night in an unfamiliar and also illegal to be place maybe wasn't the best idea for tonight."
                        
                        player "Heh, you think so?"
                        
                        ava @ say "Maybe, but we're already here. And we made a whole fortress and everything!"
                        
                        player "I know right, isn't it awesome?"
                        
                        show ava glowy flattered
                        
                        ava @ say "It is~"
                        
                        show ava glowy suggestive
                        
                        ava @ say "But you know what this night really needs?"
                        
                        player "What?"
                        
                        show ava glowy excited
                        
                        ava @ say "A scary story!"
                        
                        show ava glowy smug
                        
                        player "Will that really put you to sleep? Won't it just give you nightmares?"
                        
                        show ava glowy excited
                        
                        ava @ say "I like nightmares! They're like horror movies in your head!"
                        
                        show ava glowy smug
                        
                        player "Heh okay weirdo~ Got any good stories to share?"
                        
                        ava @ say "I got a few~"
                        
                        n "The bird perks up and starts telling you some of her favorites about serial killers, urban legends, and straight up mythical cosmic horror conspiracy theories."
                        n "You get so engrossed in them that you hardly even notice the sound of the door opening."
                        
                        player "Wait- did you hear that just now?"
                        
                        show ava glowy unsure
                        
                        ava @ say "Was the the main entrance? Oh shit I think someone's coming!"
                        
                        hide ava with dissolve
                        
                        n "Scrambling out of your book fort, you dodge the beams coming from a security guard's flashlight and remain unseen... for now."
                        n "You did manage to get separated from Ava in the process however."
                        n "Your body tenses up, instinctively holding your breath trying to avoid detection. You creep around a bookcase while the guard investigates your fortress."
                        
                        guard "Hey! Is someone there?"
                        
                        n "There's too many gaps in this shelf after you took so many books for the fort! You're a sitting duck!"
                        
                        show ava glowy unsure at center with move:
                            xzoom 1
                            xoffset 700
                            ypos y_ava
                        
                        ava @ say "Squawk!"
                        
                        pause .1
                        
                        show ava at offscreenright with move:
                            ypos y_ava
                            xoffset 700
                        
                        guard "Show yourself!"
                        
                        n "The guard turns his attention to Ava's distraction, giving you time to get away."
                        n "You find a relatively concealed spot but now it sounds like Ava's in trouble."
                        
                        guard "Alright, I see you. Come on out, birdie."
                        
                        menu:
                            guard "{cps=0}Alright, I see you. Come on out, birdie.{/cps}"
                            "Make a distraction":
                                $ avaPoints += 1
                                $ distractedLibraryGuard = True
                            
                                n "You'll be giving up your perfect hiding spot but at least you'll take the heat off Ava."
                                
                                player "Over here, pig!"
                                
                                #guard is a literal pig
                                
                                guard "Who said that?!"
                                
                                n "The guard comes storming towards you. As good as your hiding spot is, it doesn't give you much room to get away."
                                n "You resign yourself to your fate and reveal yourself to the guard."
                                
                                player "I'm right here. It's just me here, alone."
                                
                                guard "Found you!"
                                
                                n "The guard apprehends you and roughly drags you out of the library, unamused by your antics."
                                
                                scene bg campus autumn night with fade
                                
                                play music "audio/ambient/outdoors night crickets.ogg" fadein .5
                                
                                show box with Dissolve(.2):
                                    ypos 0
                                
                                n "After chewing you out for wasting his time, he lets you off with a warning."
                                n "Once he's out of sight, Ava swoops down and tackle hugs you."
                                
                                show ava typical overjoyed at center with dissolve:
                                    ypos y_ava
                                    xzoom -1
                                
                                ava @ say "[name]! You didn't get arrested!"
                                
                                player "Heh, lucky me~"
                                
                                show ava typical shy
                                
                                ava @ say "Thanks for distracting the guard for me! I was soooo scared hahaha!"
                                
                                player "Don't mention it, it was nothing. You distracted him for me first after all."
                                
                                if avaPoints > 7:
                                    show ava typical suggestive
                                    
                                    ava @ say "Well I think you deserve a little reward~"
                                    
                                    show ava typical smug
                                    
                                    n "Ava sidles up to you, placing her wings on your chest. Standing on her tip toes, she gives you a quick kiss(?) on your cheek."
                                    
                                    player "Ow! Did you just peck me?"
                                    
                                    show ava typical embarrassed
                                    
                                    ava @ say "Sorry, beaks are awkward."
                                    
                                    show ava typical happy
                                    
                                    player "It's ok, I liked it~"
                                    
                                    show ava typical suggestive
                                    
                                    ava @ say "*Chirp!~*"
                                    
                                else:
                                    show ava typical suggestive
                                
                                    ava @ say "Well you're still my hero tonight~"
                                    
                                
                            "Stay quiet":
                                n "Sorry Ava, you should have hidden better."
                                
                                guard "Stop right there!"
                                
                                show ava at center with move:
                                    xzoom 1
                                    xoffset 700
                                    ypos y_ava
                                
                                ava @ say "Eek!"
                                
                                n "While the guard apprehends Ava, you quietly sneak out of the library. You're not getting arrested on the night before midterms, fuck that."
                                
                                scene bg campus autumn night with fade
                                
                                play music "audio/ambient/outdoors night crickets.ogg" fadein .5
                                
                                show box with Dissolve(.2):
                                    ypos 0
                                
                                n "You hang around in the shadows, waiting for Ava and the cop to leave."
                                n "Surprisingly, he releases her once they're out."
                                n "You wait until the coast is clear before running out to her."
                                
                                show ava typical unamused at center with dissolve:
                                    ypos y_ava
                                
                                player "Ava! You're okay!"
                                
                                show ava typical shy
                                
                                ava @ say "Heh, yeah..."
                                
                                show ava typical unamused
                                
                                ava @ say "The guard bitched me out but thankfully let me go."
                                
                                n "She seems embarrassed about the whole thing."
                                
                                show ava typical unamused
                                                                
                                ava @ say "That coulda gone a lot worse."
                                
                                player "Yeah, imagine getting arrested just before midterms. I don't think professors would take kindly to that excuse for missing the exam."
                                
                                show ava typical shocked
                                
                                ava @ say "That's pretty much the only reason that cop let me go! He said \"I'll let you off easy because you probably have exams tomorrow!\""
                                
                                player "Heh, he probably just didn't wanna fill out the paperwork for bringing you in."
                                
                                show ava profile shy
                                
                                ava @ say "That and I'm too cute to be arrested~"
                                
                                show ava profile smug 
                                
                                ava @ say "Seriously, I've been caught urbexing so often but they always let me go!"
                                
                                show ava pose happy
                                
                                player "Luckyyy! They'd probably put me away without a second thought!"
                                
                                ava @ say "Thankfully we didn't have to put that to the test tonight!"
                                
                        show ava typical concerned
                        
                        n "Ava looks back to the library."
                                
                        ava @ say "I guess we won't be sleeping in the fort tonight, huh?"
                        
                        player "Sadly no. I wish I could see the looks on their faces when the library staff discovers it though."
                        
                        show ava typical overjoyed
                        
                        ava @ say "It's a work of art!"
                        
                        show ava typical happy
                        
                        player "It truly is. And nobody will even know who made it."
                        
                        show ava typical suggestive
                        
                        ava @ say "Nobody but us~"
                        
                        show ava typical smug
                        
                        #player "Heh I guess you're right. Us and that pig cop."
                        
                        #ava @ say "Mhm."
                        
                        player "Yeah. It was an enjoyable night, but I'm ready to go to bed for real."
                        
                        show ava typical whimsical
                        
                        ava @ say "Saaaame. It's already past midnight."
                        
                        player "Oof. Good luck on your midterms!"
                        
                        show ava typical happy
                        
                        ava @ say "You too!"
                        
                        hide ava with dissolve
                        
                        n "You walk Ava back to her dorm, bid her a good night, then return to your place for some much needed sleep."        
                        
                        
        
                
                
                #talk about how she can't believe you don't just date claire already, you counter about her not dating gunner already. maybe both of you have eyes on someone else
                
                
                
                
            "Go back to your dorm":
                $ statsSkill += 1
                $ historySkill += 1
                $ literatureSkill += 1
                
                player "As exciting as that sounds, I'd rather sleep in my comfy bed without worrying about campus security throwing me in jail for trespassing and missing my midterm."
                
                show ava typical concerned
                
                ava @ say "Aww, where's your sense of adventure?"
                
                player "I left it at home."
                
                show ava typical happy
                
                ava @ say "Have it your way!"
                ava @ say "Guess I'll just spend the night in this library all on my lonesome!"
                
                player "K, have fun with that. Good luck on your midterms!"
                
                show ava excited
                
                ava @ say "You too!"
                
                hide ava with dissolve
                
                n "You leave Ava to her scheming. You wonder if she'll actually do it."
                n "You'd rather not do anything to endanger your midterms tomorrow. You return to your dorm and get some rest, trying to ignore the test anxiety creeping up on you."
        
        
        
    jump midtermDay1Cafe
    
    
label getRoseCoffee:
    $ rosePoints += 1
    $ historySkill += 1
    
    scene bg cafe autumn day with fade
    
    play music "audio/music/vylet - Guinea Pig Dreams.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Coffee Zone is busier than you've ever seen it before. All the tables are taken and you have to wait in line before you can even see Mishka on the other side of the counter."
    n "Eventually you get to see the coffee queen rat, rushing to make everyone's orders all on her own."
    
    mishka @ say "[name]!"
    
    show mishka neutral at center with dissolve:
        xzoom -1
        #xpos -440
        ypos y_mishka
    
    player "Hey Mishka! Is now a good time?"
    #Hope you don't mind me coming in on the busiest day of the year
    
    show mishka neutral tongueout wink right
    
    mishka @ say "It gets so busy during exams week... But I will make the best drinks for you as always!"
    
    show mishka -neutral
    show mishka neutral
    
    #show mishka neutral standing
    
    player "You're the best Mishka. Can you make one for my.... friend(?) too?"
    
    show mishka nervous
    
    mishka @ say "Oh? You have someone special you wish to impress?"
    
    player "N-no nothing like that. If anything I'm being coerced into buying her a drink."
    
    show mishka standing sleep
    
    mishka @ say "I see... Well friend or foe I will make it all the same!"
    
    show mishka neutral standing
    
    player "Take your time, I don't wanna rush you."
    
    mishka @ say "Hah, thanks."
    
    n "You order a drink for yourself and one for Rose. Mishka immediately gets to work on it."
    n "Would now be a good time to ask if she wants to hang out later?"
    n "She's pretty overworked but maybe once midterms are over you two will have some free time."
    
    menu:
        n "{cps=0}She's pretty overworked but maybe once midterms are over you two will have some free time.{/cps}"
        "\"You doing anything this weekend?\"":
            $ mishkaPoints += 1
            $ mishkaMidtermWeekendHangout = True
        
            player "Hey I was wondering if maybe you'd be free this weekend?"
            
            show mishka standing frown at flipleft
            
            mishka @ say "Sch-scho vy mayesh na-"
            
            n "The rat knocks over a ceramic mug, making a loud clattering noise. She hastily uprights the mug and turns to you."
            
            show mishka tired happy
            
            mishka @ say "Th-this weekend? I do not really have plans..."
            
            player "Great, neither do I! Would you wanna hang out?"
            
            show mishka standing wink 2 tongueout
            
            mishka @ say "Umm okay! We can do the hanging out!"
            
            show mishka -neutral
            show mishka neutral standing
            
            player "Awesome! I'll figure out the details and let you know later, k?"
            
            mishka @ say "Of course, of course!"
            
            ###maybe later have an option where mishka's response changes if she likes or dislikes you
        
        "Now's not the time":
            n "Nah, it's rude to ask her at work, especially when she's juggling orders like this."
            
    n "You step back and let Mishka work on the drinks and take more customer orders."
    n "The poor rat is going back and forth nonstop preparing multiple drinks at once yet doesn't miss a beat."
    n "A few minutes later she calls you up to the counter with the drinks you asked for."
    
    player "Thanks! I have to get back to studying. Hopefully you find some time to study too!"
    
    show mishka mousey wink right
    
    mishka @ say "Oh don't worry about me... Dah skorovo!"
    
    player "See you around!"
    
    n "You take the cardboard cups and make your way back to the library where Rose awaits."
    
    scene bg library with fade
    
    play music "audio/music/vylet - Every Little Thing She Does.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    n "As you're making your way back to Rose, an idea pops into your head."
    n "She's always getting on your case for no good reason. Perhaps it's time to pay her back for it."
    
    menu:
        n "{cps=0}She's always getting on your case for no good reason. Perhaps it's time to pay her back for it.{/cps}"
        "Spit in her coffee":
            $ rosePoints -= 1
            $ badEnd += 1
            $ spatInRosesCoffee = True
            
            n "You look around and find a spot where nobody can see you then pop the lid off of Rose's coffee."
            n "There we go, a nice globule of human spit to go on top of her drink. Bon appetit, bitch."
            n "You fix the lid back on top and return to her table."
            
            player "Here you go, the finest coffee in Harmonia."
            
            show rose skirt armscrossed shy pendant at center with dissolve:
                ypos y_rose
            
            rose @ say "Set it down there. No not there, away from my notes."
            
            show rose skirt armscrossed furious pendant
            
            rose @ say "No, not on top of that book you drooling neanderthal!"
            
            n "Holy fuck is she picky with the placement of this cup."
            
            ###use the autism hands sprite here
            show rose skirt handonhip shy pendant
            
            n "You set it down and she adjusts it by half a millimeter."
            
            player "...Aren't you gonna take a sip?"
            
            rose @ say "No."
            
            player "The hell? Why not?"
            
            rose @ say "Because human hands touched it."
            
            player "Then why'd you have me get it in the first place?!"
            
            show rose skirt handonhip smug pendant
            
            rose @ say "Because I require the aroma of a hot drink to maximize the efficiency of my studies."
            
            n "So you spat in her drink for nothing."
            
            
        "Don't spit in her coffee":
            n "What's wrong with you? How can you even entertain the notion of tampering with someone's drink like that?"
            
            if drankOliviasCoffee == True:
                n "Even if you're some sick freak who drank that alligator's coffee that surely had a few milliliters of her drool in it."
            
            n "You come back to Rose's table and deliver her drink, untampered with."
            
            player "Here you go, the finest coffee in Harmonia."
            
            show rose skirt armscrossed shy pendant at center with dissolve:
                ypos y_rose
            
            rose @ say "Set it down there. No not there, away from my notes."
            
            show rose skirt armscrossed furious pendant
            
            rose @ say "No, not on top of that book you drooling neanderthal!"
            
            n "Holy fuck is she picky with the placement of this cup."
            
            ###use the autism hands sprite here
            show rose skirt handonhip shy pendant
            
            n "You set it down and she adjusts it by half a millimeter."
            
    show rose skirt handonhip smug pendant
            
    rose @ say "Perfect. Now just sit over there while I explain to you why the human race was destined for extinction."
            
    n "Rose lists out a few dozen of humanities great fuck ups, including many you've never heard of and several you've only seen on iceberg conspiracy memes."
    n "From the eradication of entire cultures, to burning of the largest libraries, to some interesting views on industrial society and its future, she makes some good points."
    
    player "Okay but given the opportunity, wouldn't any anthromorph civilization do the same?"
    
    show rose skirt armscrossed dismissive pendant
    
    n "She sighs. Somehow you can tell she's had to explain this multiple times in her life, each time growing more and more weary."
    
    show rose skirt armscrossed shy pendant
    
    rose @ say "No, because most anthromorphs lack any ambition or competence to create the conditions to nearly destroy the world at least four times."
    rose @ say "Only raccoons are above humans in terms of intellect and it takes us ruling the remnants of human-based civilization with an iron paw to keep the world in a peaceful and prosperous state."
    
    player "You haven't even been in power for more than a few decades. You just can't say you're better than everyone else."
    
    show rose skirt handonhip smug pendant
    
    rose @ say "Raccoons are literally God's chosen people. Read a book for once."
    
    player "I'm not gonna argue religious bullshit with someone who wears a Satanic pendant. Just give me your notes for the midterm and I'll be on my way."
    
    rose @ say "Take them. I obviously don't need them to ace such an easy class."
    
    hide rose with dissolve
    
    n "Wow, Rose's notes are incredibly neat and well-organized. Her handwriting consistency rivals that of a printer. Maybe she's onto something about raccoons being superior after all."
    n "You feel like all the relevant information is laid out in the most straightforward way possible. This will definitely help boost your grade."
    n "You take them back to your dorm and read them in detail, absorbing more information than you could have otherwise."
    
    jump midtermDay1


label midtermDay1Cafe:
    stop music fadeout 2.0

    scene bg black with fade
    
    scene bg codadorm autumn day with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box:
        ypos 0

    n "Your alarm drags you up from the comfort of slumber, reminding you that today is one day you can't afford to sleep in."
    n "You need a coffee, badly."
    n "You barely got any sleep after last night's ordeal. You wonder if the fortress is still standing."
    n "There's just enough time to swing by the cafe before starting your literature exam."
    
    scene bg cafe autumn day with fade
    
    play music "audio/music/mere - coffeeLove.exe.ogg" fadein .5
    
    show box:
        ypos 0
    
    n "Coffee Zone is busier than you've ever seen it before. All the tables are taken and you have to wait in line before you can even see Mishka on the other side of the counter."
    n "Eventually you get to see the coffee queen rat, rushing to make everyone's orders all on her own."
    
    show mishka neutral at center with dissolve:
        xzoom -1
        #xpos -440
        ypos y_mishka
    
    mishka @ say "[name]!"
    
    player "Hey Mishka! Is now a good time?"
    #Hope you don't mind me coming in on the busiest day of the year
    
    show mishka standing overjoyed
    
    mishka @ say "It gets so busy during exams week... But I will make the best drinks for you as always!"
    
    show mishka neutral -
    show mishka neutral standing
    
    player "You're the best Mishka."
    
    n "Should you get a treat for Ms. Ellen? It might get her to go easy on you when she grades your paper."
    
    menu:
        n "{cps=0}Should you get a treat for Ms. Ellen? It might get her to go easy on you when she grades your paper.{/cps}"
        "Get her a cinnamon roll":
            $ ch4EllenSnack = True
        
            player "Could I get a cinnamon roll to go as well?"
            
            show mishka happy
        
            mishka @ say "You have luck by your side, this is the last one yet again!"
            
            player "Did you save it just for me?"
            
            show mishka nervous
            
            mishka @ say "Well... maybe~"
            
            player "You're so sweet. I'm gonna try bribing my literature professor with it."
            
            show mishka neutral eyesclosed
            
            mishka @ say "Hopefully that goes well!"
            
            show mishka neutral -
            show mishka neutral standing
            
            player "Speaking of which, you're insane to be working when midterms start today. You get enough time to study?"
            
        
        "Don't get her anything":
            $ goodEnd += 1
        
            n "Nah, you'll do this fair and square. You don't need a crutch to pass."
            
            player "You're insane to be working when midterms start today. You get enough time to study?"
            
    show mishka shy
    
    mishka @ say "Um.... Well... There is no need to worry about me, really!"
    
    player "If you say so. I'm sure you'll do well!"
    
    show mishka standing frown
    
    mishka @ say "Heh thanks..."
    
    show mishka standing overjoyed
    
    mishka @ say "I think you will do well too!"
    
    hide mishka with dissolve
    
    n "You finish up your order and stand around while she gets to work on it."
    n "Would now be a good time to ask if she wants to hang out later?"
    n "She's pretty overworked but maybe once midterms are over you two will have some free time."
    
    show mishka standing neutral at center with dissolve:
        ypos y_mishka
        xzoom -1
    
    menu:
        n "{cps=0}She's pretty overworked but maybe once midterms are over you two will have some free time.{/cps}"
        "\"You doing anything this weekend?\"":
            $ mishkaPoints += 1
            $ mishkaMidtermWeekendHangout = True
        
            player "Hey I was wondering if maybe you'd be free this weekend?"
            
            show mishka standing frown at flipleft
            
            mishka @ say "Sch-scho vy mayesh na-"
            
            n "The rat knocks over a ceramic mug, making a loud clattering noise. She hastily uprights the mug and turns to you."
            
            show mishka tired happy
            
            mishka @ say "Th-this weekend? I do not really have plans..."
            
            player "Great, neither do I! Would you wanna hang out?"
            
            show mishka standing wink 2 tongueout
            
            mishka @ say "Umm okay! We can do the hanging out!"
            
            show mishka -neutral
            show mishka neutral standing
            
            player "Awesome! I'll figure out the details and let you know later, k?"
            
            mishka @ say "Of course, of course!"
            
            ###maybe later have an option where mishka's response changes if she likes or dislikes you
        
        "Now's not the time":
            n "Nah, it's rude to ask her at work, especially when she's juggling orders like this."
            
    n "You step back and let Mishka work on drinks for multiple customers at once."
    n "The poor rat is going back and forth nonstop preparing multiple drinks at once yet doesn't miss a beat."
    n "A few minutes later she calls you up to the counter with the drinks you asked for."
    
    player "Thanks! See you around!"
    
    show mishka mousey wink right
    
    mishka @ say "Dah skorovo!"
    
    hide mishka with dissolve
    
    n "You take the cardboard cup and make your way to the literature building, taking sips along the way that gradually bring you back up to full consciousness."
    
    jump midtermDay1Cont
    
label midtermDay1:    
    #thursday
    
    scene bg codadorm autumn day with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Today's the day. Midterms."
    n "You'll be glad to get them over with."
    n "You've done everything you can to prepare. All that's left to do is face them with courage and put pencil to paper."
    
label midtermDay1Cont:
    scene bg lecturehall with fade
    
    play music "audio/music/mere - retrograde slowed.ogg" fadein .5
    
    show box:
        ypos 0
    
    n "The classroom is extra hectic just minutes before class is scheduled to begin."
    n "Tons of chatter, anxious students worrying over their grades, hastily trying to cram in knowledge and share answers before the teacher arrives."
    n "You're too tired from all the studying you've done throughout the week to bother. Instead you just try to remain calm."
    
    if ch4EllenSnack == True:
        n "On your way to your desk you drop off a bag containing the cafe's confection onto Ms. Ellen's table."
        n "She'll know who it's from."
        
    n "You sit down and close your eyes, getting a couple minutes of rest in before the exam begins."
    n "The room goes silent when the door opens and the sound of Ms. Ellen's heels clatters against the floor on her way to the podium."
    
    if ch4EllenSnack == True:
        n "She looks momentarily confused as she picks up the bag you left for her. She gives it a few sniffs then looks around the room."
        n "You give her a wink when her gaze meets yours and she returns it with a smile."
        
    show margaret neutral at center with dissolve:
        ypos y_margaret
        
    margaret @ say "Good morning class! I'm sure you're all as anxious to be done with this as I am so without further adiue, I'll just go ahead and hand out the exams. Do your best!"
    
    n "She goes around the room, dropping off a packet of papers on everyone's desk."
    n "Her tail brushed against your hand as she passed by you. So soft~ You just wanna reach out and stroke her fur, but you remember that'd be considered sexual harassment and get you canceled."
    n "You'll just have to take this boring exam instead."
    n "You pick up your pencil and get to work."
    
    scene bg lecturehall with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Not even an hour goes by and you're finished. You didn't think it was so bad."
    n "Half the class had already finished and left by the time you stand up and hand yours in."
    n "You've still got plenty of time before your next exam but you're too burnt out to study."
    n "What to do...?"
    
    scene bg roof autumn day with fade
    
    play music "audio/music/vylet - blockhead.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You felt compelled to come up here for some reason."
    n "Maybe it's because the breeze is comforting."
    n "Your worries melt away as you watch students walking to their next class several stories below you."
    n "You'll be among them in a few minutes, but for now this is your secret spot where you can just get away."
    n "Well, it's someone else's secret spot too."
    
    show margaret neutral at center with dissolve:
        ypos y_margaret
    
    margaret @ say "Oh? Looks like I'm late to the party~"
    
    player "Or maybe I'm just early."
    
    show margaret melancholy
    
    margaret @ say "How'd the exam go? Did I make it too easy?"
    
    player "I feel like it was pretty typical."
    
    show margaret happy
    
    margaret @ say "Good, I'm glad you didn't struggle with it too much!"
    
    show margaret neutral
    
    if ch4EllenSnack == True:
        $ ellenPoints += 1
        
        n "She unfurls the paper bag you left her and pulls out the cinnamon roll."
        
        margaret @ say "Am I right to assume this was your doing?"
        
        player "Guilty as charged, ma'am."
        
        margaret @ say "So you're bribing me? How sweet of you~"
        
        menu:
            margaret "{cps=0}So you're bribing me? How sweet of you~{/cps}"
            "It's not a bribe":
                player "It's not a bribe!"
                
                show margaret overjoyed
                
                margaret @ say "So you just did it out of love for your literature professor then, huh?"
                
                show margaret neutral
                
                player "Something like that..."
                player "I just knew you liked them so I got you one."
                
                show margaret flattered
                
                margaret @ say "We're not supposed to accept gifts from students but I'll make an exception. I always do~"
                
            "It's totally a bribe":
                player "Is it that obvious?"
                
                margaret @ say "People don't just give things away with no expectation of a favor in return."
                
                show margaret overjoyed
                
                margaret @ say "Lucky for you I'm willing to bump your grade up for sweet gestures like this. Just a bit!"
                
        show margaret neutral
        
        n "Miss Ellen takes a bite out of the treat. Her tail starts to wag immediately."
        
        if ellenPoints > 5:
            n "She tears a piece off and holds it out for you."
            
            show margaret melancholy
            
            margaret @ say "Want a bite?"
            
            player "Sure."
            
            n "You take the chunk of sweet glazed cinnamon roll and devour it in one go."
            n "You didn't realize how hungry that exam had made you."
            
        show margaret flattered
            
        margaret @ say "Y'know, this ain't the most expensive gift a student has given me, but it's up there with the sweetest!"
        
        show margaret neutral
        
        player "Oh? Do students buy you things often?"
        
        margaret @ say "A little more than you'd expect."
        
        show margaret intrigued shocked
        
        margaret @ say "I'm just a basic literature professor so I don't get free cars and vacation homes like some in the business and political science departments."
        
        show margaret neutral
        
        margaret @ say "It's usually small things like purses, shoes, phones..."
        
        show margaret intrigued shocked
        
        margaret @ say "I did have one student who was unusual. He wasn't even doing poorly in the class, he just... enjoyed giving me cash."
        margaret @ say "I think he ended up giving me over ten thousand dollars over the semester."
        
        show margaret neutral
        
        player "Without you even asking? I don't ever want to hear about male privelige ever again."
        
        show margaret melancholy
        
        margaret @ say "Hehehe a few thousand doesn't make up for the challenges I've faced."
        
        player "And here all I can offer are cinnamon rolls."
        
        margaret @ say "You don't have to do much to pass my class. Just listening to me rant is enough, either in the classroom or up here."
        margaret @ say "Preferably up here so I don't have to pay for therapy."
        
        player "I'll do what I can."
                
        
    else:
        show margaret smoking neutral
    
        n "She pulls a cigarette and a lighter from her pocket and lights one up."
    
        margaret @ say "I usually only smoke when I have a bad day but this one is to reward myself for making it through the week."
        
        player "Midterms rough on you too?"
        
        show margaret smoking sad shocked
        
        margaret @ say "I have to come up with all new questions and rubrics each semester."
        margaret @ say "I can't reuse the old ones because students were just buying them from upperclassmen."
        
        show margaret sadsmoking
        
        player "Wow. And here I thought I went to a decent university."
        
        show margaret smoking happy
        
        margaret @ say "Hah! If only you knew how rampant cheating was. Not just here but everywhere."
        
        show margaret smoking neutral
        
        if ellenPoints > 4:
            n "Ms. Ellen pulls the cigarette box out and shakes it around."
            
            show margaret smoking melancholy shocked
            
            margaret @ say "Huh, only one left."
            
            show margaret smoking intrigued
            
            margaret @ say "You want it?"
            
            menu:
                margaret "{cps=0}You want it?{/cps}"
                "Hell yeah":
                    $ ellenPoints += 1
                    $ smokedCig1 = True
                    
                    player "Smoking ciggies with my professor on the rooftop during school hours? How could I resist!"
                    
                    show margaret smoking neutral
                    
                    margaret @ say "Screw the rules!"
                    
                    n "You take the cig and put it between your lips. Flicking her lighter open, Ms. Ellen ignites it for you."
                    
                    player "*Cough*"
                    
                    margaret @ say "Heh, you ever smoked one before? I forgot the raised the age where you can buy 'em."
                    
                    player "No but I wanted to look cool."
                    
                    show margaret smoking intrigued
                    
                    margaret @ say "Cool? Not so much."
                    
                    show margaret smoking melancholy
                    
                    margaret @ say "Cute is maybe the more appropriate word."
                    
                    player "I'll take it."
                    
                "Nah":
                    player "Nah, smoking is bad for you."
                    
                    show margaret smoking intrigued shocked
                    
                    margaret @ say "Only in excess! But I'm not gonna pressure you into it, I'm too old for that."
                    
                    show margaret smoking intrigued -shocked
                    
                    player "Did somebody pressure you into trying it?"
                    
                    show margaret smoking melancholy
                    
                    margaret @ say "Only the struggles of life nudged me towards it."
                    margaret @ say "I used to be so against it until I finally tried one and then it became a routine."
                    margaret @ say "Gotta have something to look forward to and these smoke breaks scratch that itch!"
                    
                    player "I don't think I'm at that point in my life yet."
                    
                    margaret @ say "Suit yourself, that just leaves more for me~"
                    
        show margaret smoking intrigued
        
        margaret @ say "Y'know I've caught a few of your classmates cheating already."
        
        show margaret smoking happy
        
        margaret @ say "Some were even bold enough to look at their phones during the exam today thinking I wouldn't notice!"
        
        player "Are you gonna fail them?"
        
        show margaret smoking melancholy
        
        margaret @ say "Mmmmh probably not. I dunno. If I feel like it I might."
        
        show margaret smoking melancholy shocked
        
        margaret @ say "Writing up a report for academic dishonesty is suuuuuch a hassle."
        
        show margaret smoking neutral
        
        margaret @ say "I'll probably let it slide unless those students piss me off."
        
        player "I'll try and stay on your good side then."
        
        show margaret smoking melancholy
        
        margaret @ say "Just listening to me ramble on about things up here has put you in a pretty good spot, [name]."
        
        show margaret smoking neutral
        
        margaret @ say "You could cheat all you want and I wouldn't give it a second thought."
        
        player "So I didn't even have to put all that effort into that exam?"
        
        show margaret smoking happy
        
        margaret @ say "You *could* have just turned in a blank sheet of paper, but I actually enjoy reading your thoughts on the class material!"
        
        if literatureSkill < 4:
            show margaret smoking melancholy
            
            margaret @ say "Even if they're a bit... underdeveloped."
            
        show margaret smoking neutral
        
        margaret @ say "It's a lot more interesting than grading 80 other strangers' responses."
        
        player "Glad I can provide some entertainment value."
        
    if (ellenPoints + literatureSkill) > 7:
        if ch4EllenSnack == True:
            show margaret melancholy shocked
        else:
            show margaret smoking melancholy shocked
    
        n "Ms. Ellen looks like she's about to say something but hesitates."
        
        if ch4EllenSnack == True:
            n "She finishes her cinnamon roll then blurts it out."
        else:
            n "She takes a drag from her cigarette then blurts it out."
            
        if ch4EllenSnack == True:
            show margaret happy
        else:
            show margaret smoking happy
    
        margaret @ say "Hey, you got any plans for next week?"
        
        if ch4EllenSnack == True:
            show margaret neutral
        else:
            show margaret smoking neutral
        
        player "Sorta? Not really? Why?"
        
        if ch4EllenSnack == True:
            show margaret intrigued shocked
        else:
            show margaret smoking intrigued shocked
        
        margaret @ say "I was just wondering... how do I put this..."
        
        if ch4EllenSnack == True:
            show margaret sad shocked -intrigued
        else:
            show margaret smoking melancholy shocked -intrigued
        
        margaret @ say "I'm not supposed to just *invite* a student over to my place..."
        
        menu:
            margaret "{cps=0}I'm not supposed to just *invite* a student over to my place...{/cps}"
            "Invite yourself":
                $ invitedToEllensHouse = True
            
                player "What if I were to ask to come over? Maybe I'm just curious to see how a literature professor decorates her home."
                player "Probably lots of books, aren't there?"
                
                if ch4EllenSnack == True:
                    show margaret happy
                else:
                    show margaret smoking happy
                
                margaret @ say "Yes! Tons of them! Would you like to come over and see? I can show you my favorites! You might find some you like~"
                
                player "I'd love to!"
                
                if ch4EllenSnack == True:
                    show margaret overjoyed
                else:
                    show margaret smoking happy
                
                margaret @ say "Perfect! Let me write down my address for you and we can meet up sometime next week. Sound good?"
                
                n "Ms. Ellen can't stop her tail from rapidly wagging as she writes on a scrap piece of paper and hands it to you."
                
                player "Nice, I can't wait!"
                
                margaret @ say "Same!"
                
                if ch4EllenSnack == True:
                    show margaret neutral
                else:
                    show margaret smoking neutral
                
                n "It feels kinda off to arrange a visit to your teacher's house. But hey you're an adult, you can do whatever you want. It's not like it's illegal to swing by an older woman's house and hang out."
            "That would be weird":
                player "Uhhhh yeah that would be kinda weird."
                
                if ch4EllenSnack == True:
                    show margaret sad shocked
                else:
                    show margaret sadsmoking 
                
                margaret @ say "Haha... it would, wouldn't it? Forget I mentioned it!"
                
                if ch4EllenSnack == True:
                    show margaret intrigued
                else:
                    show margaret smoking melancholy
                
                margaret @ say "Y'know, we've been up here a while. Don't you have somewhere to be?"
        
    n "You check the time on your phone. Just a few minutes left until your next midterm."
        
    player "Oop, it was nice chatting up here with you but I gotta go take my exam in French now."
    
    if ch4EllenSnack == True:
        show margaret intrigued shocked
    else:
        show margaret smoking intrigued shocked
    
    margaret @ say "Oh? Bonne chance et à bientôt~"
    
    player "You can speak French??"
    
    if ch4EllenSnack == True:
        show margaret flattered
    else:
        show margaret smoking happy
    
    margaret @ say "Just a bit~ I'm friends with the professor."
    
    player "You know Mrs. Celestine?"
    
    margaret @ say "Yup! We hang out from time to time. Now get going before you're late!"
    
    player "Alright, see you later!"
    
    margaret @ say "Au revoir, [name]!"
    
    hide margaret with dissolve
    
    n "She waves you off as you hoist your bag up and head down the stairway on to your next exam."
    
    scene bg classroom with fade
    
    play music "audio/music/mere - retrograde.ogg" fadein .5
    
    show box:
        ypos 0
    
    n "You show up with only a few minutes to spare. Other students are flipping through their notes and books, making last minute preparations while Claire stares off into space, humming a tune to herself."
    
    show claire flannel surprised earsup at center with dissolve:
        ypos y_claire
    
    claire @ say "[name]! You're 87 seconds late compared to your average arrival time! That's like 1 and a half standard deviations from the norm!"
    claire @ say "Is everything alright?"
    
    show claire flannel surprised earsup
    
    if smokedCig1:
        claire @ say "Why do you smell like cigarettes? Since when do you smoke?"
        
        show claire flannel sad
        
        claire @ say "You're not seeing another woman, are you?"
    else:
        show claire flannel sad
        
        claire @ say "Were you talking with someone? You smell like dog."
        
    player "I was just chatting with my literature professor after my exam."
    
    show claire flannel happy
    
    claire @ say "Oh! Think you did well?"
    
    player "Well enough."
    
    if claireFrenchSession == 2:
        show claire flannel suggestive
    
        claire @ say "I'm sure you'll make a hundred on this test after all the studying we did together~"
        
        player "We didn't really do a whole lot of actual studying, did we?"
        
        show claire flannel laughing
        
        claire @ say "It was more like... immersive learning ksksksks~"
    elif claireFrenchSession == 1 or claireFrenchSession == 2:
        show claire flannel suggestive
        
        claire @ say "I'm sure you'll do pretty well on this test! After all, we did study together~"
        
        player "I don't think I learned much from that study session..."
        
        show claire flannel laughing
        
        claire @ say "I guess we'll have to study together more often!"
    else:
        claire @ say "I hope you're prepared for this test!"
        
        player "I guess we'll find out. I'm sure you'll have no problem with it."
        
        show claire flannel suggestive
        
        claire @ say "If ya want, you can copy my answers~"
        
        menu:
            claire "{cps=0}If ya want, you can copy my answers~{/cps}"
            "Do it":
                $ claireFrenchCheat1 = True
                
                player "If I get stuck I'll take a peek."
                
                claire @ say "Ksksksks feel free to peek as much as you want~"
            "Don't do it":
                player "Nah, I'll be fine."
                
                show claire flannel happy
                
                claire @ say "If you insist! I'm sure you'll do fine!"
                
    hide claire with dissolve
    
    pause .2
    
    show celestine neutral at center with dissolve:
        ypos y_celestine
        
    celestine @ say "Bonjour class! Please clear your desks and we'll begin the exam!"
    
    n "Mrs. Celestine passes out the paper packets and you get to work on yours."
    
    hide celestine with dissolve
    
    if frenchSkill < 5:
        n "Damn, some of these are actually kind of hard."
        
        if claireFrenchCheat1 == True:
            n "You might have to look at Claire's answers after all."
            n "She can obviously work through these much faster than you can but she's been intentionally waiting for you to finish each page before turning hers over."
            n "You quickly copy her answers, trying to rearrange the wording as best you can to obscure the fact that you've cheated your way through these questions."
        else:
            n "Maybe you should have taken Claire up on her offer after all."
            n "She's working through these too fast and is already 2 pages ahead of you."
            n "Guess you're on your own."
        
    else:
        n "You diligently go through them, pacing yourself."
        
        if claireFrenchCheat1 == True:
            n "These questions aren't actually that hard. No need to cheat off Claire after all."
            
        else:
            n "These questions aren't actually that hard."

        if claireFrenchSession == 2:
            n "Those extra study sessions with her paid off after all."
        elif claireFrenchSession == 1:
            n "That study session with her paid off after all."
    
    n "Before you know it, you reach the end of the exam. You give your answers a quick final look over before turning it in."
    
    show celestine neutral at center with dissolve:
        ypos y_celestine
    
    celestine @ say "Merci! Have a nice autumn break, [name]!"
    
    hide celestine neutral with dissolve
    
    scene bg campus autumn day with fade
    
    play music "audio/music/vylet - Catching On.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Outside you find Claire waiting for you."
    
    show claire flannel happy at center with dissolve:
        ypos y_claire
    
    claire @ say "So? How'd ya feel about that test?"
    
    if claireFrenchCheat1 == True:
        show claire flannel suggestive
    
        claire @ say "I saw ya copying my answers so you're gonna ace it~"
        
        player "Heh yeah thanks for letting me do that."
        
        show claire flannel happy
        
        claire @ say "No problem! You can cheat on me anytime! On tests I mean."
        
        n "Her tone suddenly becomes deadly serious."
        
        show claire flannel sad
        
        claire @ say "If we're dating and you cheat on me with another girl I'll murder you both."

        n "She looms over you, putting off an aura that's both protective and possessive."
        
        show ava typical happy at offscreenright:
            ypos y_ava
            xoffset 500
                
        n "Before you can piss yourself in fear, Ava comes swooping in and Claire returns to her usual bubbly self."
        
        pause .1
        
        show claire flannel happy at flipright
        
        pause .1
        
        show claire:
            xoffset -400
        show ava at center:
            xoffset 400
            ypos y_ava
        with move
        
        claire @ say "OMG hi Ava!!! x3"
        
        ava @ say "Sup guys!"
        ava @ say "Just got back from my first final. Hope yours went well!"
        
        claire @ say "I think I aced it!"
        
        player "I survived."
        
    
    else:
        if frenchSkill < 5:
            player "It was kinda hard for me..."
            
            show claire flannel surprised earsup
            
            #claire @ say "Really? You should have taken me up on my offers to study together!"
            
            claire @ say "Really? I guess we need to study together more often~"
        
        else:
            player "It wasn't so bad."
            
            if claireFrenchSession == 2:
                player "No doubt thanks to your help with those study sessions."
                
                show claire flannel suggestive
                
                claire @ say "Glad to be of service~"
                
            elif claireFrenchSession == 1 or claireFrenchSession == 2:
                player "No doubt thanks to your help with that study session."
                
                show claire flannel suggestive
                
                claire @ say "Glad to be of service~"
        
        if avaPoints > 5:
            show claire flannel surprised earsup
            
            show ava typical shocked at offscreenright:
                ypos y_ava
                xoffset 500
        
            n "Ava comes swooping in at high speed. She's heading right at you!"
            
            pause .1
            
            show claire at flipright
            
            ava @ say "[name]! Coming in hot!!"
            
            n "Instinct kicks in and you hold your arms out ready to catch her."
            
            pause .1
            
            show claire with move:
                xoffset -500
                
            pause .1
            
            show ava twirl at center with dissolve:
                xoffset 400
                ypos y_ava
            
            n "Once she flies into your grasp you spin in place to slow down her momentum."
            
            player "Gotchya!"
            
            hide ava with dissolve
                
            pause .1
            
            show ava typical shocked at center with dissolve:
                xoffset 400
                ypos y_ava
            
            show claire flannel happy
            show ava typical shy
            
            claire @ say "Nice Chad spin~"
            
            ava @ say "Whew, thanks [name]! My mind was still stuck on that last exam and I didn't hit the brakes in time."
            
            player "No problem. Better you crash into me than the ground."
            
            show ava typical happy
            show claire flannel derp
            
            claire @ say "She coulda crashed into me too. I'm a bigger target anyway!"
            
            show claire flannel surprised earsup
            show ava typical smug
            
            ava @ say "Maybe I picked my target deliberately~"
            
            show claire flannel happy
            
            claire @ say "Ksksksks you know you can let go of him now, right?"
            
            show ava typical shy
            
            ava @ say "R-right haha..."
            
            n "Ava pulls her wings back and preens her feathers into place."
            
            show ava typical happy
            show claire flannel suggestive
            
            claire @ say "Aww look at [name], he's blushing!"
            
            player "I am not!"
            
            show claire flannel laughing
            
            claire @ say "You are too!"
            
            show claire flannel suggestive
            
            claire @ say "I wonder if you'd blush if I swooped down into your arms like that~"
            
            show claire flannel happy
            show ava pose angry
            
            ava @ say "You'd crush him to death if you tried!"
            
            menu:
                ava "{cps=0}You'd crush him to death if you tried!{/cps}"
                "Worth it":
                    $ avaPoints -=1
                    $ clairePoints +=1
                    
                    show ava pose concerned
                    
                    player "It'd be worth it."
                    
                    show claire flannel suggestive
                    
                    claire @ say "See, he gets it."
                    
                    show claire flannel flustered
                    
                    claire @ say "I'll spare ya this time but it's the thought that counts!"
                    
                    show claire flannel happy
            
                "Rather get hit by a truck":
                    $ clairePoints -=1
                    
                    show ava pose concerned
                    
                    player "I'd rather get hit by a truck. At least then my death would be quick and painless."
                    
                    show claire flannel sad
            
                    claire @ say "Aww..."
                    
                    show claire flannel happy
            
        else:
            show claire flannel surprised earsup
            show ava typical shocked at offscreenright:
                ypos y_ava
                xoffset 500
        
            n "Ava comes swooping in at high speed but Claire is there to catch her and spin her around."
            
            show claire at flipright
            
            pause .4
            
            show ava at center:
                ypos y_ava
                xoffset 100
            show claire:
                xoffset -300
            with move
                
            pause .3
            
            show ava with move:
                xoffset 300
            
            claire @ say "Whoa! Someone's happy to see us ksksksksk!"
            
            show claire flannel happy
            
            player "Nice save."
            
            show ava pose concerned
            
            ava @ say "Sorry about that! My mind was still stuck on that last exam!"
            
            show ava typical shocked
            
            ava @ say "I hope I got that last question right..."

            pause .1
            
            show claire:
                xoffset -400
            show ava:
                xoffset 400
            with move
        
            n "Claire sets Ava down and pats her feathers back into place."
            
    player "You two still have one more exam today, right? I'm done for the day."
    
    ava @ say "Yup! I can't stay long 'cause I gotta rush to my next one."
    
    claire @ say "Yeah, we only got a few minutes left!"
    
    player "Good luck you two! I'm gonna head back to my dorm and get ready for tomorrow's exams."
    
    show ava typical excited
        
    ava @ say "See ya! We'll meet up before the autumn break!"
    
    show ava typical happy
    show claire flannel 
    
    claire @ say "Yeah let's hang all hang out tomorrow!"
    
    player "Sounds good to me. Later!"
    
    stop music fadeout 2.0
    
    scene bg codadorm autumn night with fade
    
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You're kinda burnt out from today's exams but you're only halfway through."
    n "You muster up the energy to study a bit for stats and history but wind up falling asleep early."
        
        
    # friday
    
    stop music fadeout 2.0
    
    scene bg black with fade
    
    n "The following day..."
    
    scene bg classroom with dissolve
    
    play music "audio/music/mere - schooldaze.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Just gotta get through two more exams and then you're home free."
    
    if hasRosesNotes == True:
        n "Reading through Rose's notes is sure to give you a massive leg up on this exam."
        
        player "Thanks again for the notes the other day."
        
        show rose skirt armscrossed dismissive at center with dissolve:
            ypos y_rose
        
        rose @ say "Whatever. Don't mention it."
        
        if rosePoints > 3:
            n "Ooh nice she's wearing the same perfume she was wearing at the library the other day."
            n "Even the page she gave you had the faint scent of goth bitch on it."
            n "You couldn't resist giving it a sniff or two while studying last night."
            
        hide rose with dissolve
        
    
    else:
        if historySkill > 3:
            n "You should do reasonably well on this one as long as there's no curveball questions."
            
        else:
            n "You could have spent more time studying this topic. Hopefully the questions aren't too hard."
            
        n "Now you're imagining Rose tutoring you. She'd bite you every time you got a question wrong."
        
    
        
    show rothbauer at center with dissolve:
        ypos y_roth
        
    rothbauer @ say "Good day, students! All you'll need for this exam is a pencil, so go ahead and clear your desks and let's get started!"
    rothbauer @ say "Oh but before we begin, I'd like to mention an opportunity for extra credit over the break."
    rothbauer @ say "All you have to do is research a \"conspiracy\" related to prehistoric civilization and write a one page paper explaining it and providing evidence that it may in fact be true."
    rothbauer @ say "Now then, let's get this exam out of the way!"
    
    hide rothbauer with dissolve
    
    n "The test is a blur of dynasties and eras, those who ruled and influenced early civilizations, and the lasting impacts of their actions. You're left dazed by the end of it."
    n "Once you're finished, you turn it in and hurry to your next exam without much time to spare."
        
    scene bg lecturehall with fade
    
    play music "audio/music/mere - schooldaze faster.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Gunner's already here and writing equations on his paws with a pen."
    n "There's not enough space for all of them."
    
    if statsSkill > 3:
        n "You feel like you'll be fine but he might not do so hot..."
        
        show gunner frown1 at center with dissolve:
            ypos y_gunner
        
        gunner @ say "It's so over. We're cooked."
        
        player "You might be cooked but I think I'll be okay."
        
        show gunner mischief
        
        gunner @ say "For real? Lemme peep your answers then."
        
        menu:
            gunner "{cps=0}For real? Lemme peep your answers then.{/cps}"
            "Let him":
                $ letGunnerCheatStats = True
                
                player "Fine, just don't get me in trouble."
                
                show gunner cheeky1
                
                gunner @ say "Thanks bro you're the best."
                
                player "I'm not liable for giving bad answers either. I'm not gonna be making 100\% on this."
                
                show gunner neutral
                
                gunner @ say "It's all good, you'll do better than I would."
            "Don't let him":
                player "Fuck that, you're gonna get me in trouble."
                
                show gunner mischief
                
                gunner @ say "No it's cool, I'll bail you out. I'm rich, remember?"
                
                player "How could I ever forget?"
                player "Why don't you just bribe Mrs. Herschel?"
                
                show gunner pissed
                
                gunner @ say "That's what I do with all my teachers but she's a bitch and won't take my money."
                
                show gunner annoyed
                
                player "Oh the horror."
                    
    else:
        n "You don't feel super confident about this one either."
        
        show gunner frown1 at center with dissolve:
            ypos y_gunner
        
        gunner @ say "It's so over. We're cooked."
        
        player "Just a bit."
        
        show gunner annoyed
        
        gunner @ say "Mrs. Herschel is notorious for giving extremely hard tests. Fuck this bitch."
        
    hide gunner with dissolve
    
    pause .2
        
    show herschel at center with dissolve:
        ypos y_herschel
        
    herschel @ say "Good morning class! You know what day it is! Clear your desks and let the fun begin!"
    
    #gunner @ say "See, this is her idea of fun. She's a sadist!"
    
    hide herschel with dissolve
    
    n "When you get your test, your faced with a wall of verbose word problems and mathematical formulas including some symbols you've never even seen before."
    n "This is gonna be tougher than you thought."
    n "You focus your concentration on recalling every bit of statistical knowledge you've studied over the semester."
    
    if letGunnerCheatStats == True:
        n "You give enough space so Gunner can peek at your answers and wait for him to finish before turning the page."
        n "God damn he's so slow. He better hurry up or you're leaving him behind."
        
    else:
        n "Gunner tries to peek at your answers but you're moving too fast for him. You're already on the next page."
        n "Too bad buddy, if you don't hurry up you won't even finish this exam in time."
        
    n "When Mrs. Herschel calls for everyone to put their pencils down, Gunner spends a solid extra minute writing answers while the tests are collected."
    
    show herschel at center with dissolve:
        ypos y_herschel
        xoffset 450
    
    herschel @ say "That's enough, Gunner. I've given you plenty of extra time. If you want more, tell the department heads that you have a disability."
    
    show gunner annoyed at center with dissolve:
        ypos y_gunner
        xoffset -450
        xzoom -1
    
    gunner @ say "Like tell them I'm retarded?"
    
    herschel @ say "*Sigh*"
    herschel @ say "They might fall for it."
        
    player "Snrk!"
    
    show gunner displeased
    
    gunner @ say "Don't you 'snrk!'"
    
    show gunner itsover
    
    gunner @ say "Whatever, I'll just pay them off."
    
    show gunner frown1
    
    herschel @ say "Money only gets you so far, young man."
    
    hide herschel with dissolve
    
    menu:
        "Encourage him":
            $ gunnerPoints += 1
            
            player "Come on dude, the semester's only halfway over. You can still pull this together."
            
            n "Gunner takes a deep breath and composes himself."
            
            show gunner neutral
            
            gunner "You're right, this is just a minor setback. I only need to improve enough to get that sweet, sweet D."
            
            n "You start to crack up at the obvious joke."
            
            show gunner annoyed
            
            gunner "Shut up, you know what I meant."
            
            
        "Taunt him":
            $ gunnerPoints -= 1
            
            player "LMFAOOOO get dunked on richboiii!"
            
            show gunner annoyed
            
            gunner @ say "I'm gonna pay you $100 to shut the fuck up."
            
            player "Deal!"
            
            n "Gunner slides a crisp hundo your way and you gladly take it. Easiest money you've ever made."
            
    show gunner optimistic
        
    gunner @ say "Gotta run but we'll meet up later for lunch, k?"
    gunner @ say "I wanna get the whole squad together one last time before autumn break!"
    gunner @ say "We'll meet up at that Thai place. No stupid contests this time."
    
    player "Cool, see you there."
    
    stop music fadeout 2.0
    
    scene bg black with fade
    
    n "You return to your dorm and unwind for a bit until Gunner texts you saying everyone's ready."
    
    scene bg town summer day with fade
    
    play music "audio/music/vylet - That Feeling I Get in my Heart.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "When you arrive, Claire waves you over to their table."
    
    show gunner cheeky1 at center:
        ypos y_gunner
        xoffset -400
        xzoom -1
    show rori jacket smile at center:
        ypos y_rori
        xoffset -650
        xzoom -1
    show ava typical happy at center:
        ypos y_ava
        xoffset 300
    show claire sweater happy at center:
        ypos y_claire
        xoffset 650
    with dissolve
    
    claire @ say "There he is!!"
    
    gunner @ say "[name]! You made it!"
    
    show gunner neutral
    show ava pose concerned
    
    ava @ say "Did you get lost on the way here?"
    
    show rori armscrossed anxious
    
    rori @ say "Yeah man, we've been waiting for you for a while."
    
    n "Truth be told maybe you did get a little lost. You kinda spaced out and don't even remember how you got here."
    
    show rori jacket armscrossed neutral
    show ava typical happy
    
    player "Sorry guys, I'll try and be faster next time."
    
    claire @ say "It's alright! We were just talking about our plans for the autumn break now that midterms are outta the way!"
    
    player "Plans? Oh right, I didn't make any."
    
    show ava typical shocked
    
    ava @ say "You mean you're not going back home?"
    
    n "You shrug."
    
    show ava typical concerned
    show rori jacket anxious
    show gunner frown1
    show claire sweater sad
    
    player "No? Why would I?"
    
    n "Your friends look to each other uneasily."
    
    ava @ say "I've got my bags packed and ready to go already."
    
    claire @ say "If I'd known you'd be here alone I wouldn't have made plans to visit home!"
    
    gunner @ say "My flight home leaves tonight. What are you gonna do here for a whole week?"
    
    if mishkaMidtermWeekendHangout == True:
        show rori jacket neutral
        show gunner neutral
        show claire sweater surprised earsup
        show ava typical happy
    
        player "I made some plans with Mishka."
        
        claire @ say "Huh? Are you two going on a date?!"
        
        player "No no, we're just gonna hang out!"
        
        show rori jacket yawn lookingaway blush
        
        rori @ say "Y'know I'm staying here too. We can hang out and chill whenever!"
    else:
        player "Same thing I always do, whatever I feel like."
        
        show rori jacket yawn lookingaway blush
    
        rori @ say "Don't worry, I'm staying too! We can hang out and chill whenever."
        
    show gunner neutral
    show claire sweater happy
    show ava typical happy
    
    menu:
        rori "{cps=0}Y'know I'm staying here too. We can hang out and chill whenever!{/cps}"
        "That sounds nice":
            $ roriPoints += 1
            
            player "That sounds nice. We can play vidya and watch anime :3"
            
            show rori jacket armscrossed smile
            
            rori @ say "Ba-a-a-a-a-ah~"
            rori @ say "I'd love that :3"
            
            show gunner annoyed
            
            gunner @ say "Our dorm better not smell like gay sex when I get back."
            
            menu:
                gunner "{cps=0}Our dorm better not smell like gay sex when I get back.{/cps}"
                "It won't":
                    player "It won't."
                    player "...probably."
                    
                    show claire sweater sad
                    
                    claire @ say "Why do all the hot ones end up being gay?"
                    
                    show ava typical shy
                    
                    ava @ say "You got it backwards, all the gay ones end up being hot."
                    
                    
                "We'll take it to my dorm":
                    $ hittingOnRori = True
                    
                    player "Guess you'll have to come to my dorm, Rori."
                    
                    show rori jacket surprised
                    
                    rori @ say "OwO"
                    rori @ say "W-what do you mean? We're not really gonna... are we?"
                    
                    show rori jacket lookingaway blush
                    
                    player "Hahaha no of course not... unless..?"
            
        "We'll see":
            player "We'll see. I might just wanna lie in bed all week."
            
            show rori jacket neutral
            
            rori @ say "That works too. Lemme know if you feel like doing anything. I'll just be in my dorm compiling kernels and debugging bootloaders."
            
            show rori jacket sleepy
            
            rori @ say "Might install ReiserFS before it gets deprecated just to see what it's all about."
            
            show gunner annoyed
            
            gunner @ say "So glad I'm not into that nerd shit."
            
            show claire sweater suggestive earsup
            
            claire @ say "Hey, nerd shit can be sexy!"
            claire @ say "Tell me more about obscure file systems made by wife-murderers, Rori~"
            
            show ava typical enamored
    
            ava @ say "Wife-murderers you say?"
            
            show ava typical suggestive 
            show rori jacket anxious
            
            ava @ say "Now I'm interested~"
            
            show ava typical shocked
            
            gunner @ say "You guys are freaks."
            
            player "Silence, normie."
            
    show ava typical happy
    show claire sweater happy
    show rori jacket neutral
    show gunner neutral

    n "The waitress comes to take your orders, putting a pause on your conversation."
    n "The rest of your afternoon is spent discussing everyone's plans upon returning home."
    n "After lunch you all walk back to campus to say goodbye before parting ways."
    
    claire @ say "I'm gonna miss you guys!!!"
    
    ava @ say "Same! I hope you all have a great autumn break!"
    
    gunner @ say "Hold down the fort, Rori. If anyone breaks in, there's a 1911 under my pillow you can use."
    
    show rori jacket sleepy
    
    rori @ say "Let me guess, it's made of solid gold?"
    
    show gunner uncomfy
    
    gunner @ say "They make them out of anything else?"
    
    show rori jacket neutral
    
    player "It's kinda weird, it feels like we're saying farewell forever."
    
    show claire sweater sad
    
    claire @ say "Awww we'll be back before you know it!"
    
    show claire sweater happy
    show ava typical excited
    
    ava @ say "Yeah! And we can still text each other!"
    
    show ava typical happy
    
    player "I mean I've been with you guys since this semester started. This is the first time we'll be apart since we met."
    
    show ava pose concerned
    show rori jacket worried
    show claire sweater surprised earsup
    
    player "It's like going back to before I started college, back when I was on my own."
    
    show rori jacket smile
    
    player "At least Rori will still be here."
    
    rori @ say "I know how you feel. You know you can text me if you ever get lonely and we can hang out!"
    
    show claire sweater giggle
    show ava typical shocked
    
    claire @ say "Oh my god I would ship you two so hard if I wasn't gonna take [name] for myself."
    
    if avaCommitted == True:
        show ava typical shy
        
        ava @ say "Saaame~"
        
    show ava typical happy
    show claire sweater happy
    show gunner itsover
        
    gunner @ say "Rori, *please* take [name] so I don't have to compete with him for Ava. Thank you."
    
    show rori jacket anxious
    
    rori @ say "Guys..."
    
    show rori jacket neutral
    show gunner neutral
    
    claire @ say "We're just teasin' ya~"
    
    show claire sweater suggestive
    
    claire @ say "But you two *would* make a cute couple ksksksksk~"
    
    show claire sweater happy
    show ava typical whimsical
    
    ava @ say "Come on, I think we've tortured him enough. We can't stick around forever, we've all got our flights to catch!"
    
    show ava typical happy
    
    ava @ say "I'm glad we got to see each other one last time before the break!"
    
    show gunner cheeky1
    
    gunner @ say "For sure. We'll have to catch up once we're back!"
    
    claire @ say "Safe travels you two!"
    
    gunner @ say "Call me when you get home!"
    
    show ava typical shy
    
    ava @ say "I will~"
    
    show ava typical happy
    
    n "After an extremely protracted goodbye from everyone, your friends leave one by one until it's just you and Rori left."
    
    hide gunner with dissolve
    hide ava with dissolve
    hide claire with dissolve
    
    
    pause .1
    
    show rori jacket sleepy with move:
        xoffset -300
    
    rori @ say "Whew, that was exhausting."
    
    player "I thought they'd never leave."
    
    show rori jacket neutral
    
    if hittingOnRori == True:
        rori @ say "...Were you serious about doing stuff at your dorm?"
        
        show rori jacket worried2
        
        menu:
            rori "{cps=0}...Were you serious about doing stuff at your dorm?{/cps}"
            "Yeah, kinda":
                player "The door's always open for ya~"
                
                if roriPoints > 4:                    
                    rori @ say "I uh..."
                    
                    show rori jacket armscrossed lookingaway smile blush
                    
                    rori @ say "I might come in one night >w>"
                else:
                    show rori jacket armscrossed lookingaway smile blush
                    
                    rori @ say "I'll uh... keep that in mind UwU"
            "Maybe? I don't know":
                player "Yes? No? Maybe. I don't know."
                
                if roriPoints > 4:
                    show rori jacket armscrossed lookingaway smile blush
                    
                    rori @ say "Well uh... if you wanna... Just let me know haha?"
                    
                else:
                    show rori jacket anxious
                    
                    rori @ say "N-nevermind. Forget I said anything."
            "Nooooo haha":
                player "Noooo haha I was just joking around."
                player "I wouldn't wanna have hot and sweaty sex with an adorable sheep boy after missing out on a new episode of Kitsune Chronicles because we were too busy kissing."
                player "That would be gay."
                
                show rori jacket armscrossed lookingaway smile blush
                
                rori @ say "You're right, it would be."
                
    show rori jacket anxious
    
    stop music fadeout 2.0
    
    n "Rori looks past you with a face of utter horror and dread."
    
    ###alt intro where you get rory mixed up with rori and think he's trooned out. 50/50 chance?
    
    play music "audio/music/vylet - manehattan's finest.ogg" fadein .4
    
    show rory autumn nautral at offscreenright:
        ypos y_rory
    
    rori @ say "Oh no, is that who I think it is?"
    
    pause .1
    
    show rory autumn neutral at center with move:
        ypos y_rory
        xoffset 350
    
    show rori jacket armscrossed annoyed

    rory @ say "Heyyyyyy lil bro~"
    
    n "She looks over you from top to bottom. You can't tell if she's intrigued or disgusted."
    
    rory @ say "Is this your boyfriend? Just kidding, you could never get a boyfriend!"
    
    rori @ say "What do you want? Don't you have some butterflies to be pulling the wings off of?"
    
    rory @ say "Oh no, I stopped doing that ages ago. I aim for bigger targets now~"
    
    menu:
        rory "{cps=0}Oh no, I stopped doing that ages ago. I aim for bigger targets now~{/cps}"
        "Who the hell is this bitch?":
            player "Rori you wanna tell me who this bitch is?"
            
            rori @ say "She-"
            
            rory @ say "This bitch right here-"
            
            n "She points to Rori."
            
            rory @ say "- that's my little brother unfortunately. We're twins but I'm older by a few minutes~ Like everything in life he came in last place."
            
            player "I didn't ask you."
            
            rory @ say "Didn't you? You said Rory right? With a \'y\'"
            
            player "You're both named Rori?"
            player "Are you fucking serious?"
            
            rory @ say "Pfffft hahahah I know it's confusing, right? At home I'm usually referred to as \"the better Rory~\""
            
            rori @ say "More like cunt Rory!"
            
            rory @ say "You're just jealous that I have one~"
            
            n "You're sensing some sibling rivalry going on here."
            
            rory @ say "And you are?"
            
            player "[name]. Can't say it's been a pleasure to meet you."
            
            rory @ say "Well if you like Rori, you'll love me~"
        "I love this bitch already":
            player "Damn this bitch seems kinda evil."
            player "I'm into that."
            
            rori @ say "Don't be. She's just a psychopath."
            
            rory @ say "How rude!"
            rory @ say "Well if my dear brother won't introduce me to his friend, I guess I'll have to do it."
            rory @ say "I'm Rory. With a \'y~\'"
            rory @ say "I'm his twin sister, older by just a couple minutes."
            
            n "She holds out her hoof and you reach out to shake it."
            
            show rori jacket surprised
            
            rori @ say "[name] wait!!!"
            
            show rori jacket concerned
            
            n "Too late."
            
            show rori jacket anxious
            
            n "Rory grabs hold of your soft fleshy human hand and absolutely *crushes* it."
            n "You pull back, yelping in pain."
            
            player "Ow! What the fuck!"
            
            rory @ say "Oops hehehe sorry~"
            rory @ say "I forget how fragile others can be."
            
            n "One of your fingers is sticking out at an unnatural angle. You can neither feel it nor move it."
            
            player "I think you broke something."
            
            rory @ say "No worries, I can fix it!"
            
            n "Before you have time to react, Rory grabs hold of your finger and moves it back into place."
            
            player "Aaaaaaagh!!!"
            
            rory @ say "Good as new!"
            
            n "Through the excruciating pain, you find that you can in fact move your finger again."
            
            show rori jacket sleepy
            
            rori @ say "I tried to warn you..."
            rori @ say "This is how she's always been. Imagine living with her."
            
            rory @ say "Yes, imagine living with someone as perfect as *me~*"
            rory @ say "You should be honored to have had the privilege, little Rori~"
            
        "Introduce yourself politely":
            player "I don't believe we've met before. I'm [name]."
            
            rory @ say "Nice to meet me, isn't it? I'm Rory -- with a \"y~\""
            
            n "She does a little curtsy."
            
            rory @ say "So nice of you to wrangle my little brother Rori in my absence!"
            
            if roriPoints > 4:
                player "Rori's nice, I like him."
            else:
                player "He can be a handful sometimes."
            
            rory @ say "I'm surprised they even admitted him to Harmonia. They must have seen his name and got it mixed up with mine~"
            
            rori @ say "I'm surprised they haven't admitted you to a mental asylum!"
            
            n "There is legitimate anger in Rori's voice."
            
            player "What's your problem? She's your sister isn't she?"
            
            rori @ say "She's a psychopath! Don't be fooled!"
            
            rory @ say "Don't mind him, he's just jealous!"
            
            
            
            #rori @ say "Shut up, I deserve to be here more than you!"
            #
            #rory @ say "Do you?"
            #rory @ say "I'm clearly the better candidate!"
            
    
    rory @ say "I'm basically exactly like him but better in every way!"
    rory @ say "While he's busy downloading kernels, I'm uploading code for them~"
    rory @ say "I can run circles around him in his favorite games~ He used to cry when I'd perfect KO him in Tekken 10 times in a row!"
    
    show rori jacket armscrossed anxious
    
    rory @ say "Now he just ragequits!"
    rory @ say "*And* I can climb faster than him with one hoof tied behind my back! We actually tested this once and I humiliated him~"
    
    if roriPoints > 5:
        player "My Rori is kind and sweet."
        
        show rori jacket surprised
        
        rori @ say "Y-your Rori?"
        
        show rori jacket worried
        
        rory @ say "I see, you're one of *those* types."
        #rory @ say "I can be sweeter than him... I just choose not to~"
        rory @ say "Don't make the mistake of conflating passiveness with kindness."
        rory @ say "Rori's personality is a result of him being submissive. He may appear to be nice on the surface, but he's really just desperate for affection."
        rory @ say "But even then, I bet I'm sweeter~"
    else:
        player "You can't be better at everything. Rori has to have something he beats you at."
        
        show rori jacket concerned
        
        rory @ say "That's the sad part, he really doesn't!"
        rory @ say "I'm just a straight upgrade from him."
        rory @ say "Literally~"
        
        #rory @ say "The only reason to choose him over me is for his dick, which isn't even that big."
        
        #player "H-how would you know?"
        
        #rory @ say "Doesn't matter. I could turn any gay man straight anyway~"
        
        #rory @ say "Why settle for him when you could have me instead?"
    
    #rory @ say "I haven't met anyone worthy of me yet. I'm almost afraid I never will."
    
    show rori jacket armscrossed annoyed
    
    rori @ say "What do you want, Rory? Did you come over here just to torture me?"
            
    rory @ say "I just wanted to say goodbye my little bro before I go back home for autumn break, that's all!"
    rory @ say "I know it must have been rough when Ma and Pa denied your request to visit."
    rory @ say "But don't worry, we'll enjoy the time I'm home without you!"
    
    rori @ say "Oh go to hell."
    
    rory @ say "Not right now, I've got a flight to catch!"
    
    rori @ say "I hope it crashes and you burn to death!"
    
    rory @ say "Hehehe you know that would never happen~"
    rory @ say "It was really nice meeting your boyfriend. Enjoy him while you can, because I might decide to make him mine when I come back! Hahahaha!"
    
    show rori jacket surprised
    
    n "She shoulder checks Rori so hard he falls to the ground as she walks away."
    
    pause .1
    
    show rory at offscreenleft:
        ypos y_rory
        xoffset -200
    show rori jacket worried2:
        xoffset -450
    with move
    
    menu:
        n "{cps=0}She shoulder checks Rori so hard he falls to the ground as she walks away.{/cps}"
        "Help him up":
            n "You hold out your hand to grab onto and hoist him back up onto his hooves."
            
        "Let him get up":
            n "He doesn't need your pity. Helping him will just bruise his ego even more."
            n "He picks himself up and brushes the leaves and dirt off his jacket."
            
    show rori jacket armscrossed annoyed
    
    rori @ say "Grrrr that bitch..."
    
    player "And you lived with her for years? That must have been brutal."
    
    rori @ say "I don't care if she's my sister, I genuinely hate her."
    rori @ say "I don't even care that she's better at everything, the world would be a better place without her in it."
    
    player "Geez man. At least she's going away for the week."
    
    show rori jacket anxious
    
    rori @ say "Yeah... Luckily I haven't run into her much here. But now that she's seen me with friends she'll stop at nothing to sabotage me."
    
    show rori jacket concerned
    
    rori @ say "She can't stand seeing me happy. It's the one thing that gets under her skin."
    
    player "...You wanna talk about it?"
    
    show rori jacket worried2
    
    rori @ say "I dunno. Not right now. I wanna be alone."
    
    player "Alright. I'll see you around man."
    
    rori @ say "Yeah. And thanks for being here for me."
    
    player "Anytime. That's what bros are for."
    
    stop music fadeout 2.0
    
    scene bg black with fade
    
#saturday
    scene bg codadorm autumn day with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box:
        ypos 0

    n "It's officially the first day of your autumn break. No more worries until school starts back up again."
    n "You can enjoy life at your own pace and do whatever you want."
    
    if mishkaMidtermWeekendHangout == True:
        n "You agreed to meet up with Mishka at the cafe today. She said it would be closed for the duration of the break but that it would be a good spot to hang out."
                
        call roseInHallways from _call_roseInHallways
        
        jump writingWithMishka
        
    call roseInHallways from _call_roseInHallways_1
    
    jump ch4GoWithRori
        

label roseInHallways:
    scene bg codadormhallways autumn day with dissolve
    
    play music "audio/music/vylet - blockhead.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0

    n "On your way out, you nearly trip over some short gremlin-type creature."
    n "Oh wait, that's just Rose."
    
    show rose skirt furiouspose at center with dissolve:
        ypos y_rose
    
    rose @ say "Watch it, punk!"
    
    player "Rose?? What are you doing in my dorm building?"
    
    show rose skirt fistsclenched angry
    
    rose @ say "*Your* dorm building?! If it's anyone's, it's mine!"
    
    player "Wait, you've been living here this whole time?"
    
    show rose skirt armscrossed shy
    
    rose @ say "...Yes."
    
    player "Aren't you rich? Don't you have a mansion you could be living in instead?"
    
    show rose skirt armscrossed dismissive
    
    rose @ say "*Sigh* I don't know why I'm even entertaining you but yes normally I would be residing in the family mansion."
    rose @ say "But granddad insists that I spend some time in the dorms to \"meet people and make friends\" whatever that means."
    
    player "I'm people."
    
    show rose skirt armscrossed annoyed
    
    rose @ say "No, you're not. You're barely even sapient."
    
    menu:
        rose "{cps=0}No, you're not. You're barely even sapient.{/cps}"
        "About this mansion...":
            player "About this mansion... I think I could get you back in there."
            
            show rose skirt handonhip smirk
            
            rose @ say "I doubt it but let me hear your stupid idea. I could use a laugh."
            
            show rose skirt handonhip smug
            
            player "Your grandpa just wants to see you with a friend then he'll let you back in, right?"
            
            show rose skirt handonhip annoyed
            
            player "I could be your rental friend!"
            
            show rose skirt handonhip angry
            
            rose @ say "I think I just puked a little."
            
            show rose skirt armscrossed shy
            
            rose @ say "Just moving back into the mansion wouldn't be worth spending a second with a h*man."
            
            show rose skirt armscrossed dismissive
            
            rose @ say "...But he's also holding my inheritance hostage."
            
            show rose skirt armscrossed annoyed
            
            rose @ say "And I don't know which is worse, being in the presence of you or being poor."
            
            player "It's just pretend, you don't have to commit to it."
            player "But the more convincing it looks the less time we'll have to spend together."
            
            show rose skirt armscrossed unsure
            
            rose @ say "Ugh, what have I done to deserve such a fate?"
            
            player "Gee, I wonder."
            player "So are you down?"
            
            show rose skirt handonhip annoyed
            
            rose @ say "What's the catch?"
            
            player "I wanna sleep over at the mansion."
            
            show rose skirt furiouspose
            
            rose @ say "Hell no!"
            
            player "Just for one night! We can even sleep in different rooms!"
            
            if (rosePoints + historySkill) > 6:
                $ mansionQuestStarted = True
            
                rose @ say "I hate this and I hate you but if it will make my filthy human-sympathizer granddad happy then..."
                
                show rose skirt armscrossed shy
                
                rose @ say "Fine."
                
                show rose skirt armscrossed annoyed
                
                rose @ say "We'll \"\"\"hang out\"\"\" on occasion within view of my grandfather. You'll stand no closer than 5 feet away from me and under no circumstances will you so much as lay a finger on me."
                
                show rose skirt armscrossed shy
                
                rose @ say "Once I'm back in my rightful home, we cease all contact forever and ideally you kill yourself."
                
                player "Deal. Except for the killing myself part. You gotta offer up something good for that."
                
                if (rosePoints + historySkill) > 7:
                
                    rose @ say "What, like a pat on the back?"
                    
                    player "I was thinking more like..."
                    
                    menu:
                        player "{cps=0}I was thinking more like...{/cps}"
                        "A date":
                            player "A date?"
                            
                            show rose skirt fistsclenched angry
                            
                            rose @ say "Absolutely not."
                            
                            player "For real, I'll take you out and if you decline a second date I'll kill myself on the spot."
                            
                            show rose skirt handonhip annoyed
                            
                            rose @ say "Not happening."
                            
                            player "Alright alright, we'll just be \"friends\" til you get your mansion."
                            
                            show rose skirt handonhip dismissive
                            
                            rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                            rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                            
                            player "Yeah whatever. See you around, \"friend~\""
                            
                            rose @ say "Weirdo creep."
                        "A kiss":
                            player "A kiss?"
                            
                            rose @ say "None in stock."
                            
                            player "Just one little smooch and then I'm dead. A kiss of death."
                            
                            rose @ say "You can kiss the barrel of a shotgun."
                            
                            player "Alright alright, we'll just be \"friends\" til you get your mansion."
                            
                            show rose skirt handonhip dismissive
                            
                            rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                            rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                            
                            player "Yeah whatever. See you around, \"friend~\""
                            
                            rose @ say "Weirdo creep."
                        "A pawjob" if rosePoints > 6:
                            n "Yeah why not, you feel confident enough to say this."
                            
                            player "Gimme a pawjob and I'll blow my brains out after blowing my load."
                            
                            show rose skirt fistsclenched angry
                            
                            rose @ say "The only paws you'll be getting will be me knocking your lights out."
                            
                            n "It seems your confidence was misplaced..."
                            
                            player "Alright alright, we'll just be \"friends\" til you get your mansion."
                            
                            show rose skirt handonhip dismissive
                            
                            rose @ say "Fine, whatever."
                            rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                            rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                            
                            player "Yeah yeah. See you around, \"friend~\""
                            
                            rose @ say "Weirdo creep."
                        "Your panties" if avaPantsu == True or clairePantsu == True:
                            $ rosePantsu = True
                            
                            player "Ok hear me out..."
                            
                            rose @ say "Uh huh?"
                            
                            player "I've been starting a collection..."
                            
                            show rose skirt armscrossed dismissive
                            
                            rose @ say "Riiiight."
                            
                            player "Of women's panties."
                            
                            show rose skirt fistsclenched angry
                            
                            rose @ say "Oh go fuck yourself."
                            
                            player "I know right? It all started from this stupid frat boy panty raid thing."
                            player "And I'd kill to have yours."
                            player "Kill myself even."
                            
                            show rose skirt handonhip annoyed
                            
                            rose @ say "Aside from how disgusting it is to ask that of anyone, let alone someone who hates your guts-"
                            rose @ say "Do you have any idea how much these cost?!"
                            
                            player "It's just underwear, it can't be that expensive."
                            
                            rose @ say "I don't wear *anything* that costs less than $850."
                            rose @ say "Not even my socks."
                            
                            player "Is that per sock or do you count them as a pair?"
                            
                            show rose skirt handonhip dismissive
                            
                            rose @ say "*Sigh*"
                            
                            show rose skirt handonhip shy
                            
                            rose @ say "You know what, fine. It's for the greater good."
                            
                            player "H-holy shit...!"
                            
                            hide rose with dissolve
                            
                            n "Right then and there Rose bends over and reaches under her skirt. She steps out of a pair of lacey purple panties, the soft silk shining in the sun's glow."
                            n "You swear they were sparkling, like you were in an anime."
                            n "She tosses them to you and the first thing you can think to do is sniff them."
                            
                            stop music fadeout 2.0
                            
                            scene bg black with dissolve
                            
                            n "Wait, what's happening...?"
                            n "The hallway is spinning and you feel as though you're being dragged backwards at high speed."
                            
                            scene bg codadormhallways autumn day with fade
                            
                            show box with Dissolve(.2):
                                ypos 0
                            
                            n "You wake up on the floor, panties nowhere to be found."
                            n "What just happened?"
                            n "You pull yourself up onto your feet and suddenly recall."
                            n "The moment you asked for Rose's panties she jumped up and smacked you on your head, knocking you out cold."
                            n "But it felt so real in that dream..."
                            n "You're just gonna count that as a W."
                            
                            
                    
                else:
                    #what, you want a handjob?
                    #kinda
                    #well you're not getting one
                    rose @ say "How about I let you lick my boots?"
                    
                    player "How about you lick my balls?"
                    
                    show rose skirt handonhip angry
                    
                    rose @ say "How about I kick you in the balls?"
                    
                    player "Barefoot?"
                    
                    show rose skirt handonhip dismissive
                    
                    rose @ say "Forget it."
                    
                    player "Alright alright, we'll just be \"friends\" til you get your mansion."
                    
                    rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                    rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                    
                    player "Yeah whatever. See you around, \"friend~\""
                    
                    rose @ say "Weirdo creep."
                    
            else:
                rose @ say "You're just as retarded as the rest of your species if you think I'd agree to any of this!"
                rose @ say "I'd sooner burn the mansion down than let you take one step into it!"
                
                player "Suit yourself. Have fun living in the dorms for the next four years."
                
                n "You do a cool 360 and walk away, staring her down as you moonwalk out of there."
            
            
        "Have fun living in the dorms, bitch":
            player "Ok then have fun living in the dorms, bitch."
            
            rose @ say "I was actually on my way to the library."
            
            if avaLibraryAdventure == True:
                player "I tried to live in the library once. Maybe you could do the same."
                
                show rose skirt armscrossed shy
                
                rose @ say "Did it work out?"
                
                player "No."
                
                rose @ say "Sad."
            else:
                player "Why don't you move into the library? You practically already live there."
                
                show rose skirt armscrossed dismissive
                
                rose @ say "I just might. This dorm has a human infestation and the only solution is to burn the whole thing down."
                
            player "Why are you going to the library? Midterms are over. We have a week off school."
            
            show rose skirt handonhip shy
            
            rose @ say "Your kind wouldn't understand concepts like diligence and perfectionism so I don't expect you to get it."
            rose @ say "But if you must know, I'm going to do some research on dinosaurs."
            
            player "You're actually doing the history extra credit? You already have a hundred in that class."
            
            show rose skirt armscrossed smirk
            
            rose @ say "A hundred and one mind you."
            
            show rose skirt armscrossed shy
            
            rose @ say "But yes, I'm aiming for a hundred and two. Plus the material is good to know. Not easy to find information on that era since y'know, you destroyed it all."
            
            player "I wasn't there!"
            
            show rose skirt armscrossed dismissive
            
            rose @ say "Yet if you were, you'd destroy it with your incompetence."
            
            player "Fuck this and fuck you. I've got better things to do."
            
            rose @ say "So do I. So get out of my way."
            
            n "You decide to flex your height and take a step over her rather than around."
            
            show rose skirt armscrossed annoyed
            
            rose @ say "Ugh, please die."
            
            player "No you."
            
            n "The two of you head in opposite directions, taking different stairwells to the base floor, then pretend not to see each other on the way out."
            
        
label writingWithMishka:
    scene bg campus autumn day with fade
    
    $ writingWithMishka1 = True
    
    play music "audio/music/vylet - two creatures walk into a bar.ogg" fadein .4
    
    show box:
        ypos 0

    play music "audio/music/vylet - I Wish I Could Tell You.ogg" fadein 1.0
    
    n "Outside the cafe you see Mishka standing by herself, watching street birds hop around and peck at the ground."
    n "They fly away as you approach and Mishka notices you."
    
    show mishka neutral at center with dissolve:
        xzoom -1
        #xpos -440
        ypos y_mishka
    
    mishka @ say "[name]! You're here!"
    
    #player "Sorry, am I late? I thought we agreed to meet up at noon."
    
    #n "You check the time on your phone. It's only 11:45."
    
    #mishka @ say "Nyet, it's okay. I just thought you might"
    
    player "Hey Mishka! Sorry to keep you waiting."
    
    mishka @ say "No worries!"
    
    show mishka nervous
    
    mishka @ say "So...."
    
    n "She looks around nervously."
    
    show mishka shy
    
    mishka @ say "I'm not sure what to do now."
    
    show mishka neutral standing
    
    #player "I think college students are supposed to go to parties during these breaks."
    player "Honestly me neither."
    player "The campus is a ghost town cause of autumn break."
    
    mishka @ say "Would you like to go inside? I can make drinks for us."
    
    n "You shrug your shoulders."
    
    player "Might as well."
    
    scene bg cafe autumn day with fade
    
    play music "audio/music/vylet - two creatures walk into a bar.ogg" fadein .4
    
    show box:
        ypos 0
    
    n "Mishka unlocks the door and leads you inside where she starts the make the usual coffee for you."
    
    player "At least there's no customers to worry about today."
    
    show mishka neutral standing at center with dissolve:
        ypos y_mishka
    
    mishka @ say "None except you! But do not worry, I won't charge for this."
    
    player "Thanks. Is working at a cafe fun? I like the chill vibes drinking here but it looks pretty hectic making the drinks for everyone."
    
    show mishka standing tongueout
    
    mishka @ say "Oh it gets pretty hard at times! But it's fairly routine work I would say."
    
    player "You're here like all the time. How do you find time for classes?"
    
    show mishka shy sad
    
    mishka @ say "Well I..."
    #Справді немає потреби!
    
    show mishka standing sleep
    
    mishka @ say "Spravdi nemaye potreby!"
    
    player "Pardon?"
    
    show mishka standing neutral
    
    mishka @ say "Nevermind. What do you do for fun?"
    
    menu:
        mishka "{cps=0}Nevermind. What do you do for fun?{/cps}"
        "Troll online image boards":
            player "I engage in the art of baiting people online."
            
            show mishka anxious sad
            
            mishka @ say "You do... baiting to people? I am not familiar with this term."
            
            player "It's a niche hobby where the goal is to make strangers get mad."
            
            show mishka anxious smile
            
            mishka @ say "I see."
            
            n "You can tell by the look on her face that she doesn't understand the point."
            n "You're starting to question the point of it all yourself."
            
            player "Over time people catch on to trolling efforts and it takes a lot of creativity to come up with new bait but I'm pretty good at it."
            player "I'm known as a master baiter."
            
            show mishka standing neutral
            
            mishka @ say "So it's like creative writing?"
            
            player "Sorta?"
            
            show mishka standing sleep
            
            mishka @ say "Ahh how fascinating! I liked to write too!"
            
        
        "Write spicy fanfics":
            player "I like to write."
            
            n "Mishka's eyes widen with excitement."
            
            mishka @ say "You do?!"
            
            show mishka anxious neutral
            
            mishka @ say "What sort of things do you write?"
            
            n "You're embarrassed to confess to the type of literature you enjoy."
            
            player "Just like uh... y'know, stuff. Romance stories I guess you could say."
            
            show mishka happy
            
            mishka @ say "Ahh how fascinating! I liked to write too!"
            
        #"":
            
        
        "Nothing":
            player "For fun? What's that?"
            
            show mishka anxious smile
            
            mishka @ say "You know, what are things you enjoy doing?"
            
            player "I'm not really sure? I don't do a whole lot."
            
            show mishka anxious sad
        
            mishka @ say "Really? Nothing?"
            
            show mishka happy
            
            mishka @ say "Why don't you try something new?"
            
            show mishka neutral standing
            
            player "Like what?"
            
            show mishka neutral tongueout wink right
            
            mishka @ say "When I found myself in your position I took to creative writing!"
            
    show mishka neutral -
    show mishka neutral standing
            
    player "What did you write?"
    
    mishka @ say "Stories based on cartoons I watched!"
    
    pause .1
    
    show mishka with move:
        xoffset -200
    
    pause .4
    
    show mishka at flipright
    
    pause .3
    
    show mishka with move:
        xoffset 0
    
    n "Mishka finishes with the drinks and finds a table for you to sit at."
    
    mishka @ say "Back in my home village we had a satellite dish for the television that could just barely pick up signals. Sometimes it would show cartoons but mostly old Soviet era ones."
    
    player "Wow, I totally forgot that was even a thing. Both satellite TV and the Soviet Union."
    
    show mishka happy
    
    mishka @ say "Yes, both were awful!"
    
    show mishka neutral standing
    
    mishka @ say "Eventually we got a computer and I could download western cartoons with fan made Ukrainian dubs! I liked them because they were so much more lighthearted!"
    
    show mishka anxious smile
    
    mishka @ say "It was good escapism when shells were landing near our village."
    
    player "...Shells?"
    
    show mishka anxious sad
     
    mishka @ say "Ehh, it's not important. Sorry to bring it up."
    
    show mishka neutral wink right
    
    mishka @ say "But this is how I started to be learning English!"
    
    show mishka neutral -
    show mishka neutral standing
    
    mishka @ say "I downloaded western fanfictions of my favorite cartoons and read through them. Then I tried writing my own!"
    
    n "You nod then take a sip of your drink, scalding your tongue on 200 degrees of hot coffee (93.3C for countries without freedom units)."
    
    player "Did you post them online?"
    
    mishka @ say "I did! But they are lost to time now."
    
    n "She takes a sip of her coffee then looks to you with a smile."
    
    mishka @ say "Maybe... we could write one together?"
    
    menu:
        mishka "{cps=0}Maybe... we could write one together?{/cps}"
        "Sounds fun!":
            player "I'd be down to try it. I've never written with someone before though."
            
            mishka @ say "That's okay, we can figure it out!"
            
            n "You discuss some basic premises, characters, and plot and settle on a rough plan."
            
        "I'd rather not":
            player "Ehhh I'd rather not. I'm not that great of a writer."
            
            mishka @ say "Oh come on, at least give it a try!"
    
            player "Alright, but I probably won't be that much help."
            
            mishka @ say "All that matters is that we have fun with it!"
    
            n "Mishka guides you through setting up some basic premises, characters, and a plot."
    
    n "Mishka grabs some napkins and pulls a pen from her jacket pocket. She begins sketching diagrams."
    
    mishka @ say "I like to start draw outlines and arrows pointing out related events. You know basic three act structure, right?"
    
    player "Uhh yeah. Beginning, middle, end."
    
    hide mishka with dissolve
    
    #mishka @ say "Yup! I like to start with the end then work my way backwards!"
    #mishka @ say "Got any ideas?"
    #
    #player "For the ending?? Okay uhhh what if... "
    #
    #
    #menu:
    #    "A storm comes...":
    #        player "...a giant storm comes and wipes out the town."
    #        
    #        mishka @ say "And then?"
    #        
    #        player "I dunno?"
    #        
    #        mishka @ say "That's like the climax of the story but there's gotta be more!"
    #        mishka @ say "If the town gets destroyed by the storm then the people will have to rebuild!"
    #        
    #        player "I guess that gives all the characters a moment to get together and start all over again."
    #        
    #        mishka @ say "Absolutely! Things are forever changed but they still have a home and each other and live happily ever after!"
    #        mishka @ say "Now let's go back and start at the beginning to figure out how to get there..."
    #    
    #    "The protagonist dies":
    #        
    #        player "...the protagonist dies in the end?"
    #        
    #        mishka @ say "Seems kinda bleak. Does he do a heroic sacrifice or something?"
    #        
    #        player "Maybe... not? Sometimes people just die."
    #        
    #        mishka @ say "Yeah but narratively there has to be something there. There needs to be a reason to write it like that!"
    #        
    #        player "Okay well maybe the whole story is about like setting things up to pass the torch to the future generations?"
    #        
    #        mishka @ say "That could work! Except I think it might cause conflict with some parts of the lore."
    #        
    #        player "Yeah, I didn't think of that."
    #        
    #        mishka @ say "It's like that saying \"It's about the journey, not the destination.\""
    #        
    #        player "Huh, I think that actually works better. Like the main character is focusing on figuring out to spend his days before the inevitable end."
    #        
    #        mishka @ say "In that case it should be a hopeful tragedy!"
    #        
    #        player "Isn't that kind of a contradiction?"
    #        
    #        mishka @ say "Not really! If his death is a tragedy then that means someone cares about him."
    #        mishka @ say "And if someone cares, then that must mean they had good times together."
    #        mishka @ say "So he'll have left his mark on the world."
    #        
    #        player "I guess that makes sense. I just hope it's not all for nothing."
    #        
    #        mishka @ say "Nobody said writing would be easy!"
            
    n "You spend the whole day workshopping your story ideas with Mishka, chugging through multiple cups of coffee."
    n "Before you know it, it's dark outside."
    
    scene bg cafe autumn night with dissolve
    
    #play music "audio/ambient/outdoors night crickets.ogg" fadein 0.1
    
    show box with Dissolve(.2):
        ypos 0
    
    show mishka neutral eyesclosed at center with dissolve:
        ypos y_mishka
    
    mishka @ say "*Yaaaawn*"
    
    show mishka neutral standing
    
    mishka @ say "I think we will have to stop for now."
    
    player "Damn, we spent the whole day just writing."
    
    show mishka nervous
    
    mishka @ say "Yeah!! Did you enjoy it?"
    
    menu:
        mishka "{cps=0}Yeah!! Did you enjoy it?{/cps}"
        "I did. A lot.":
            $ mishkaPoints += 1
        
            player "I did! A lot! I'm glad you dragged me into it."
            
            show mishka nervous
            
            mishka @ say "Hehe I'm glad I could drag you into it! We should write more together some time."
            
            player "Of course! We have to finish the story after all!"
            
            show mishka anxious neutral
            
            mishka @ say "Yeah!!"
            
            hide mishka with dissolve
            
        "It was alright":
            player "It was alright. Maybe writing's not my thing after all."
            
            show mishka nervous
    
            mishka @ say "Aww. Sorry to hear."
            
            show mishka anxious sad 
            
            mishka @ say "Maybe I should not have dragged you into this..."
            
            player "No it's fine, it was a nice gesture I just can't write well with others."
            
            mishka @ say "..."
            
    
    n "You help Mishka throw away all the cups and wipe down the table before saying goodbye and returning to your dorm for the night."
    
    stop music fadeout 2.0

    scene bg black with fade

    hide box


label ch4GoWithRori:
    n "After lazing around your dorm for a bit, you get bored and decide to take a walk around campus."
    
    scene bg campus autumn day with fade
    
    play music "audio/music/vylet - Pancake.ogg" fadein .4
    
    show box:
        ypos 0
    
    n "The campus is like a ghost town now that the autumn break is in effect."
    n "There's only the sound of wind rustling through the leaves and... hoof steps?"
    n "You turn around and see Rori with his nose buried in his phone. He doesn't even notice you."
    
    show rori jacket at offscreenright:
        ypos y_rori
    
    player "Yo! Rori!"
    
    show rori jacket anxious at center with move:
        ypos y_rori
        xoffset -300
        
    #pause .1
    
    show rori jacket anxious with move:
        ypos 3000
    
    rori @ say "Huh?"
    
    n "Doubly distracted, he walks straight into a lamp post. Ouch."
    
    show rori at center:
        ypos 3000
        xzoom -1
        xoffset 0
    
    n "You walk over and help him up."
    
    show rori with move:
        ypos y_rori
    
    player "You alright?"
    
    show rori jacket sleepy
    
    rori @ say "Ugh... Yeah I'm fine, thanks."
    
    player "Dude what are you doing on your phone that's so important you're walking into things?"
    
    show rori jacket neutral
    
    rori @ say "Just one of those monster catcher games."
    
    player "A what now?"
    
    rori @ say "You know, the kind where you walk around in real life and find creatures in the app."
    
    player "Sounds lame."
    
    show rori jacket yawn lookingaway blush
    
    rori @ say "Normies were super into it a few years ago but now only the most hardcore dedicated fans still play it."
    
    show rori jacket smile
    
    rori @ say "You wanna install it? I'll show you how to play!"
    
    #menu:
    #    "Nah":
    #        player "Nah, keep that shit off my phone. I only play the highest quality kemono girl VNs on it."
    #        
    #        rori @ say "Suit yourself."
    #        
    #        player "Don't you have better games we could play?"
    #        
    #        rori @ say "Like back at my dorm? Sure, we could load up Super Smash Sister or something."
    #        
    #        player "Works for me."
    #    "Give it a shot":
    #        player "Alright but heads up my phone only has like 640KB of RAM."
    #        
    #        rori @ say "That's all anyone needs!"
    #        
    #        n "Rori sends you a download link from some sketchy Russian site and you let it run."
    #        
    #        player "Bro this shit runs at like negative frame rates."
    #        
    #        rori @ say "Yeah they're working on an optimization patch."
    #        
    #        player "Okay so what now?"
    #        
    #        rori @ say "We just walk around until we come across a monster. They're usually around landmarks and stuff."
    #        
    #        n "Rori takes you to a few hotspots on campus and shows you the ropes."
    #        n "There's literally no gameplay, you just swipe the screen and it automatically does everything."
    #        
    #        player "Rori I don't mean to be rude but this is gay as hell. Can we please do anything else?"
    #        
    #        rori @ say "Aww you don't like it? That's alright, it's not for everyone."
    #        rori @ say "How about we go back to my dorm and play a real game?"
    #        
    #        player "I'm down."
    
    player "I don't think my phone has enough RAM to render anything more complicated than pong."
    
    rori @ say "Fair enough. We could go back to my dorm and play on a real machine if you wanna."
    
    menu:
        rori "{cps=0}Fair enough. We could go back to my dorm and play on a real machine if you wanna.{/cps}"
        "Nah I'm good.":
            player "Ehh, I'm not really feelin' it. Maybe next time."
            
            show rori jacket concerned
            
            rori @ say "Aww okay. Guess I'll play something online then."
            
            show rori jacket neutral
            
            rori @ say "See you around!"
            
            player "See ya!"
            
            jump autumnBreakPt2
        
        "Sounds fun":
            $ roriPoints += 1
            $ ch4GamedWithRori = True
        
            player "Sounds good! Lead the way."
            
            jump gamesWithRoriCh4
label gamesWithRoriCh4:
    scene bg roridorm with fade
    
    play music "audio/music/vylet - Takamine.ogg" fadein .4
    
    show box:
        ypos 0
    
    n "Rori plugs some controllers into his PC then runs a few commands in a terminal. On his monitor an emulator pops up and the game begins to boot up."
    
    show rori jacket neutral at center with dissolve:
        ypos y_rori
    
    player "Yayyy modded Super Smash Sisters!"
    
    show rori jacket supersmug
    
    rori @ say "An all time classic!"
    rori @ say "Hold up, I got something for occasions like this."
    
    n "He leans forward and grabs a bottle of whiskey from under his desk."
    
    player "Whoa, where'd you get that? Won't the school expel you if they find out you have that in the dorms?"
    
    rori @ say "I guess we better dispose of the evidence then~"
    
    show rori jacket neutral
    
    rori @ say "Winner takes a shot after each round?"
    
    menu:
        rori "{cps=0}Winner takes a shot after each round?{/cps}"
        "You're on!":
            $ roriPoints += 1
            $ drunkWithRori = True
            
            player "Hell yeah, you're on!"
            player "Wait, the *winner* takes a shot?"
            
            rori @ say "No point in me clowning on you all day. The more I drink the more of a chance you have."
            
            player "This better not be a trap to get me drunk and accidentally say something gay."
            
            show rori jacket armscrossed supersmug
            
            rori @ say "Riiiight, \"accidentally\" hahaha"
            
            show rori jacket armscrossed lookingaway smile blush
            
            rori @ say "Don't worry, video game sleepovers don't *have* to be homo erotic."
            
            player "Who said this was a sleepover?"
            
            show rori jacket armscrossed smile -blush -lookingaway
            
            rori @ say "I mean, you're welcome to stay the night. Ain't like we got class to worry about."
            
            player "We'll see how it goes."
            
            n "You and Rori play a few rounds, taking shots after each game."
            
            show rori jacket -armscrossed neutral
            
            if roriPoints > 7:
                rori @ say "Hey."

                player "Yeah?"
                
                show rori lookingaway blush

                rori @ say "It's getting kinda hot in here."
                
                show rori supersmug
                
                rori @ say "You mind if I take my pants off?"
                
                menu:
                    rori "{cps=0}You mind if I take my pants off?{/cps}"
                    "Go ahead":
                        $ roriWentPantsless = True
                    
                        n "The alcohol has taken a hold of you. You don't even question the logic of removing his pants while leaving his jacket on."
                        
                        player "Go ahead, it's your dorm."
                        
                        show rori at shudder
                        
                        pause .2
                        
                        show rori jacket pantsless neutral blush
                        
                        show rori at flipright
                        
                        n "Rori yoinks off his pants mid-game and still manages to take all your stocks."
                        
                        n "Dammit, what was that part about not accidentally saying something gay?"
                        #n "Too late now, the genie is out of the bottle."

                    
                    "Only if I can too":
                        $ roriWentPantsless = True
                        $ playerWentPantsless = True
                        
                        n "The alcohol has taken a hold of you. You don't even question the logic of removing his pants while leaving his jacket on."
                        
                        player "Only if I can too. I swear you run it at a million degrees in here on purpose."
                        
                        if roriPoints > 8:
                            show rori jacket lookingaway blush
                        
                            rori @ say "That may have been the plan, yes~"
                        else:
                            show rori jacket supersmug
                        
                            rori @ say "I'm not stopping ya."
                            
                        show rori at shudder
                        
                        pause .2
                        
                        show rori jacket pantsless neutral blush
                        
                        show rori at flipright
                            
                        n "You try to stay focused on the game while shimmying out of your pants, but Rori manages to take his off and take out your last stock."
                        
                        n "Dammit, what was that part about not accidentally saying something gay?"
                        #n "Too late now, the genie is out of the bottle."
                    "That's kinda...":
                        $ roriPoints -= 2
                        
                        player "That's kinda gay, not gonna lie."
                        
                        show rori jacket surprised
                        
                        rori @ say "Is it?"
                        
                        show rori jacket worried
                        
                        n "He thinks for a moment."
                        
                        show rori jacket worried2
                        
                        rori @ say "O-oh, I didn't mean it in a sexual way! I'm just used to going pantsless at home when it's just me here!"
                        
                        player "Right. And you decided to try it with me here?"
                        
                        show rori jacket lookingaway blush
                        
                        rori @ say "I guess I'm just comfortable around you?"
                        
                        player "Aww bro."
                        player "For real though, leave those pants on. I came here to play Smash, not smash."
                        
                        rori @ say "Y-yeah haha..."
                
            
        "Decline":
            player "Nah, I don't really feel like getting drunk tonight."
            
            show rori jacket sleepy
            
            rori @ say "Meh, I'm still gonna take a drink for every win."
            
            show rori jacket laugh
            
            rori @ say "Maybe by the end of the day you'll be consistently beating my drunk ass!"
            
            show rori jacket neutral
            
            n "You play a few matches with Rori. He's clearly more skilled at this than you, despite his hooved handicap."
            n "It's not long before he gets tipsy enough to start making mistakes and losing games to you though."
            
    show rori jacket neutral

    n "A few more matches go by with you chattering about random topics. Then you remember the other day and decide to bring it up."
            
    player "Hey so if you don't mind me asking, what's the deal with your sister? Why is she such a cunt?"
    
    show rori jacket sleepy
    
    rori @ say "Ugh that's just how she's always been."
    rori @ say "Like she's literally my evil twin."
    
    show rori jacket worried2
    
    rori @ say "I got all the gay and submissive genes and she got the psychopath ones."
    
    player "I don't think that's how genes work."
    
    show rori jacket sleepy
    
    rori @ say "Either way she was raised to think she's better than everyone, which ironically made her try to live up to that ideal."
    
    show rori jacket anxious
    
    rori @ say "And she always used me to prove her superiority."
    
    player "Damn bro that sucks. Kinda makes me glad I was a lone child."
    
    show rori jacket concerned
    
    rori @ say "I'm giving you fair warning, do *not* get close to her. She has maxxed out her manipulation stat and will take advantage of you in any way she can."
    
    n "Rori is starting to get tilted and slip up in the game more as he talks about his sister."
    
    show rori jacket sleepy
    
    rori @ say "Seriously, she is just irredeemably awful. But at least she made me realize how women are so I can just be a fag in peace now."
    
    menu:
        rori "{cps=0}Seriously, she is just irredeemably awful. But at least she made me realize how women are so I can just be a fag in peace now.{/cps}"
        "You don't have to be alone" if roriPoints > 6:
            $ youGay = True
            
            player "Y'know you don't have to be a fag alone."
            
            show rori jacket yawn lookingaway blush
            
            rori @ say "Wha?"
            
            show rori jacket worried2
            
            player "I mean... uhh..."
            player "We could be fags... together?"
            
            show rori supersmug
            
            rori @ say "That sounds nice."
            rori @ say "If you want, we could totally snuggle on my bed :3"
            
            player "Let's do it!"
            
            jump roriSnuggles
        "Not all women...":
            player "Come on Rori, not all women are evil bitches devoid of empathy. I bet you could find a nice one."
            
            rori @ say "No thanks. Bros before hoes. The only good women are 2D."
            
            player "What about Ava and Claire? They're sweet."
            
            show rori jacket yawn lookingaway blush
            
            rori @ say "They're cute but they're manipulative. Even at their best, they're waging a war path to get what they want."
            
            show rori jacket worried2
            
            player "A war path? Dude you're exaggerating."
            
            show rori jacket anxious
            
            rori @ say "Kinda but you get what I mean. Women are selfish by design."
            rori @ say "At least with guys we can have some comradery. We instinctively *understand* each other on a primal level."
            
            show rori jacket concerned
            
            rori @ say "And I... I take comfort in that."
            
            player "I don't mean to sound homophobic but it just seems like you hate women."
            
            show rori jacket neutral
            
            rori @ say "Yeah and? I don't wanna be alone forever so what other option do I have than to be gay?"
            
            show rori jacket lookingaway blush
            
            rori @ say "Besides, some boys are really cute."
            
            if roriPoints > 7:
                player "Am I one of those?"
            
                rori @ say "Of course!"
                rori @ say "Cute enough for me to snuggle at least."
                
                player "For real? Why are we sitting here playing a party game for children instead of doing that?"
                
                rori @ say "I dunno, I thought the video games would be like foreplay."
                
                jump roriSnuggles
            else:
                player "Okay dude hate on women all you want, just don't make baseless assertions about my friends just because your sister is a cunt."
                
                show rori jacket worried2
                
                rori @ say "Sorry, I didn't mean to ruin the mood... It's just-"
                rori @ say "I thought you'd understand."
                
                player "..."
                
                n "The rest of the evening is awkward. Eventually you get tired and go back to your dorm."
            
            #if roriPoints > 4:
                #player "You're kinda right. Like I'm sensing that you wanna snuggle with me right now."
        "Hope you find someone":
            player "Sounds like you've had it rough. You really don't deserve to be alone. I hope you find someone you vibe with."
        
            rori @ say "*Sigh* yeah me too."
            
            show rori jacket sleepy
            
            rori @ say "But complaining about it just makes me sound like an incel."
            
            player "Dude our whole friend group is incels, barring Gunner."
            
            rori @ say "Ava and Claire don't count. Women can't be incels."
            
            player "You heard them at the snuggle puddle, they said nobody liked them in high school."
            
            show rori jacket worried2
            
            rori @ say "I don't know if I believe that. Either way, I'd keep them at a distance."
            
            player "Noted. But have you seen the way that bunny looks at me?"
            
            show rori jacket sleepy
            
            rori @ say "Yes, I've noticed. She definitely has a crazed look in her eyes. Be careful around her."
            
            n "You play a few more rounds with Rori before calling it a night."
    
    jump autumnBreakPt2
    
label roriSnuggles:
    n "You hop onto Rori's bed and pat the mattress."
    
    player "Hop on dude~"
    
    show rori jacket supersmug
    
    rori @ say "Hahaha oooookay, this is a little different from the cuddle puddle."
    
    show rori jacket smile
    
    rori @ say "Since it's just the two of us, this is definitely a little bit gay~"
    
    player "Yeah whatever, get that sheep butt over here."
    
    n "Rori flops onto the bed and rolls over to you, ending up face to face with you."
    
    show rori jacket worried2
    
    rori @ say "*gulp*"
    
    player "So uh... come here often?"
    
    show rori jacket smile

    rori @ say "Usually every night."
    
    player "Is this how you snuggle?"
    
    n "You wrap your arm around him and pull him close."
    
    show rori jacket yawn blush lookingaway
    
    rori @ say "Eeep!"
    rori @ say "I'm nervous, okay??"
    
    show rori jacket smile -lookingaway
    
    player "What are you nervous for? It's just two bros snuggling."
    
    rori @ say "It's *not* just two bros snuggling!"
    
    show rori jacket anxious
    
    rori @ say "I mean I... kinda like you so I just don't wanna fuck this up."
    
    player "Well I kinda like you too, otherwise I wouldn't be snuggling with you."
    
    if romanticFantasy == False:
        rori @ say "I..."
        
        show rori jacket lookingaway blush
        
        rori @ say "*Sigh* Do you wanna listen to me ramble or do you just wanna snug? I'm good with either."
        
        menu:
            rori "{cps=0}*Sigh* Do you wanna listen to me ramble or do you just wanna snug? I'm good with either.{/cps}"
            "Listen":
                $ roriPoints += 1
                $ romanticFantasy = True
                $ roriRomanticFantasy = True
                
                player "Go ahead and talk, I'll listen."
                
                show rori jacket neutral
                
                rori @ say "Thanks. I wouldn't bring this up to anyone else but I feel comfortable saying it to you cause... I think you'll get it."
                
                show rori jacket concerned
                
                rori @ say "I've never known what it's like to love or be loved by someone. I kept to myself in high school and mostly stayed inside my room doing computer stuff at home."
                rori @ say "Between the isolation and torment from my family, I just- developed a desire for a certain kind of person. Someone who's genuine and caring."
                rori @ say "And who appreciates me for who I am."
                
                show rori jacket sleepy
                
                rori @ say "I'm not gonna settle for someone who doesn't see my perspective. I need someone who can empathize with me. Does that make sense?"
                
                show rori jacket yawn lookingaway blush
                
                rori @ say "Call it a romantic fantasy of mine. I just want to love someone who loves me back and we'd do anything for each other."
                rori @ say "I don't think relationships like that can be forced into existing. I think I'll have to meet exactly the right person and go from there."
                
                show rori jacket smile -lookingaway
                
                rori @ say "Okay rant over."
                
                player "Wow. I haven't really thought of it in words like that but yeah I kinda agree with you. Some people just aren't meant to be together but conversely some are perfect for each other."
                player "I honestly don't really know if I'm the right one for you. Maybe I am?"
                
                rori @ say "We wouldn't be snuggling like this if there wasn't a chance."
                
                player "Lucky we're still young and have time to figure shit out."
                
                n "Rori looks into your eyes and smiles sweetly."
                
                rori @ say "Yeah~"
                
                show rori jacket cheery
                
                rori @ say "By the way, we don't have to rush and have this all figured out right now. I'm happy to just enjoy spending time with you however we feel like."
                
                rori @ say "Soooo like if you wanted to smooch or somethin' we could give it a shot just to see how it feels?"
                
                show rori jacket smile
                
                menu:
                    rori "{cps=0}Soooo like if you wanted to smooch or somethin' we could give it a shot just to see how it feels?{/cps}"
                    "Kiss him":
                        $ roriPoints += 1
                        $ kissedRori = True
                        
                        player "What, you mean liiiiike... this?"
                        
                        show rori jacket anxious
                        
                        n "You gently raise his chin with your fingers and press your lips to his."
                        
                        show rori jacket cheery blush
                        show rori jacket cheery 
                        
                        n "He seems shocked you actually did it at first, but then he melts in your embrace and leans into it."
                        n "It seems to last forever, or at least until you're out of breath."
                        
                        show rori jacket yawn blush lookingaway
                        
                        rori @ say "*Gasp!*"
                        rori @ say "Whew that sure was... something!"
                        
                        show rori jacket supersmug
                        
                        rori @ say "A very exciting something!"
                        
                        player "Yeah? You wanna do it again?~"
                        
                        show rori jacket smile
                        
                        rori @ say "You bet!"
                        
                        n "He enthusiastically pulls you in for a peppering of smoochies. It gets to the point where you have to pull him off you just to get a breath."
                    
                        rori @ say "Heh sorry, I got a little carried away. I've been touch-starved my whole life."
                        
                        player "I know how it is. I just need to come up to breathe every now and then!"
                        
                        if roriPoints > 8:
                            show rori jacket yawn lookingaway blush
                        
                            rori @ say "You know we can actually go beyond this if you want?"
                            
                            show rori jacket smile -lookingaway
                            
                            player "Wait what? Is there like kissing level 2 or something?"
                            
                            show rori jacket supersmug
                            
                            rori @ say "Pffft no! Well I mean yeah there kinda is I think but that's not what I'm talking about."
                            
                            player "You're gonna have to spell it out for me then."
                            
                            n "Rori giggles and whispers it into your ear."
                            
                            rori @ say "Human male on male anthro~"
                        
                            n "You fully understand what you must do."
                        
                            menu:
                                n "{cps=0}You fully understand what you must do.{/cps}"
                                "Gay ram sex":
                                    $ roriPoints += 1
                                    $ fuckedRoriEarly = True
                                    
                                    show rori jacket supersmug blush
                                    show rori jacket supersmug
                                    
                                    player "Alright, we just have to decide who's gonna top."
                                    
                                    rori @ say "...Rock-paper-scissors for it?"
                                    
                                    player "Okay, do we shoot on three or do like one-two-three-shoot?"
                                    
                                    show rori jacket neutral
                                    
                                    rori @ say "Let's just go on three."
                                    
                                    player "Best two out of three?"
                                    
                                    rori @ say "Yeah."
                                    rori @ say "Okay ready?"
                                    
                                    player "Ready!"
                                    
                                    stop music fadeout 2.0
                                    
                                    scene bg black with dissolve
                                    
                                    n "You ended up getting the result you wanted."
                                    
                                
                                "No gay ram sex":
                                    player "Sorry but I'm not ready to have gay ram sex right now."
                                    
                                    show rori jacket laugh
                                    
                                    rori @ say "That's okay! Like I said we don't have to speedrun this at all. We can just do whatever feels right."
                                    
                                    show rori jacket smile
                                    
                                    player "Thanks for understanding."
                                    
                                    rori @ say "Thanks for being here with me~"
                                    
                                    player "You mind if I stay the night?"
                                    
                                    show rori jacket supersmug blush
                                    show rori jacket supersmug
                                    
                                    rori @ say "Go right ahead~"
                                    
                                    stop music fadeout 2.0
                                    
                                    scene bg black with dissolve
                            
                    
                    "Don't kiss him":
                        player "I'm actually good like this. Just wanna take it slow and snuggle my ram friend."
                        
                        show rori jacket cheery
                    
                        rori @ say "That's perfectly fine! I'm good with whatever."
                        
                        show rori jacket smile
                        
                        rori @ say "I'm enjoying this as-is already~"
                        
                        player "Good~"
                        
                        n "You rest your chin on his head as you hold him close."
                        n "This is nice."
                        n "You could just close your eyes and fall asleep just like this."
                        
                        stop music fadeout 2.0
                        
                        scene bg black with dissolve
                        
                jump morningAfterRamSnug
            
            "Snug":
                jump ramSnuggle

label ramSnuggle:
    player "Let's just enjoy the moment. We both wanna snuggle a cute boy, so here we are."
    
    show rori jacket smile -lookingaway
    
    rori @ say "Fair. Snugs are nice."
    
    n "Rori settles in, leaning in even closer to your face."
    
    rori @ say "You're nice to be around. I wouldn't mind doing this more often."

    player "You're pretty nice to be around yourself. I never thought I'd meet such an adorable dorky sheep twink who vibes with me."
    
    rori @ say "Hey! I'm taller than you!"
    
    player "Still a twink."
    
    show rori jacket supersmug blush
    show rori jacket supersmug 
    
    rori @ say "Your twink~"
    
    n "You reach your hand lower and get a handful of fluffy sheep booty."
    
    show rori jacket yawn lookingaway blush
    
    rori @ say "Mmh~"
    
    show rori jacket blush lookingaway
    
    menu:
        "Ask if he wants to go further":
            n "You're in bed with this pantless ram, cuddling and grabbing his ass. This is obviously going somewhere."
            
            player "You wanna take this further?"
            
            show rori jacket anxious
            
            rori @ say "U-um well, how much further are you talkin'?"
            
            menu:
                rori "{cps=0}U-um well, how much further are you talkin'?{/cps}"
                "Some smoochies":
                    $ roriPoints += 1
                    $ kissedRori = True
                    
                    player "Nothing crazy, just some smoochies."
                    
                    show rori jacket cheery
                    
                    rori @ say "That I can do, but only for you~"
                    
                    show rori jacket supersmug blush
                    show rori jacket supersmug
                    
                    player "Just some experimental smoochies. To test if you're *actually* gay."
                    
                    rori @ say "Oh yes, we're just testing if *I'm* gay."
                    
                    player "Yup. Now shut up and kiss me, you fag~"
                    
                    rori @ say "Gladly~"
                    
                    n "Rori leans in and pushes his lips to yours."
                    n "Time seems to stand still."
                    n "Your brain races to determine how you feel about this while coming up with no clear answers."
                    n "Eventually you run out of breath and have to pull back."
                    
                    show rori jacket cheery
                    
                    rori @ say "How was that?"
                    
                    show rori jacket smile
                    
                    player "Fucking awesome!"
                    player "I mean, analysis was inconclusive. More evidence is needed."
                    
                    show rori jacket supersmug blush
                    show rori jacket supersmug
                    
                    rori @ say "Then come here and get some more~"
            
                    n "Rori enthusiastically pulls you in for round two. You think you could get used to this."
                
                
                "Gay ram sex":
                    $ roriPoints += 2
                    
                    player "I kinda wanna try out this gay sex thing I read about on the internet."
                    
                    show rori jacket concerned
                    
                    rori @ say "I hate to break it to you but gay sex is a myth. It doesn't actually exist."
                    
                    player "Darn. It seemed really hot."
                    
                    show rori jacket laugh
                    
                    rori @ say "Hahaha let's try it anyway~"
                    
                    show rori jacket lookingaway blush
                    
                    player "For real? Like actually seriously?"
                    
                    show rori jacket smile -lookingaway
                    
                    rori @ say "Yeah? I don't see why not. You're hot and I have an emotional attachment to you."
                    
                    player "UwU same goes for you~"
                    
                    rori @ say "We'd just be... experimenting. That's what college is for right?"
                    
                    player "Alright alright, we just have to decide who's gonna top."
                    
                    show rori jacket neutral
                    
                    rori @ say "...Rock-paper-scissors for it?"
                    
                    player "Okay, do we shoot on three or do like one-two-three-shoot?"
                    
                    rori @ say "Let's just go on three."
                    
                    player "Best two out of three?"
                    
                    rori @ say "Yeah."
                    rori @ say "Okay ready?"
                    
                    player "Ready!"
                    
                    stop music fadeout 2.0
                    
                    scene bg black
                    
                    n "You ended up getting the result you wanted."
                    
                
        "This is as far as you go":                    
            n "You rest your chin on his head as you hold him close."
            n "This is nice."
            n "You could just close your eyes and fall asleep just like this."

label morningAfterRamSnug:
    stop music fadeout 2.0
    
    scene bg black with dissolve

    n "The following morning..."
    
    scene bg roridorm with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You wake up with Rori slumbering in your arms."
    n "You almost can't believe how last night went."
    n "He starts to stir and awaken from his slumber."
    
    show rori jacket pantsless neutral at center with dissolve:
        ypos y_rori
    
    player "Morning, cutie~"
    
    show rori jacket pantsless supersmug blush
    
    rori @ say "Morning~"
    
    n "He yawns and gives you one last tight embrace before rolling out of bed."
    
    show rori jacket pantsless smirk lookingaway blush
    
    rori @ say "Mmmh, last night was pretty wild huh?"
    
    player "Not wild enough I'd say."
    
    show rori jacket supersmug blush
    
    rori @ say "Heh, you freak~"
    
    n "He smirks at you then looks away."    
    
    show rori jacket anxious
    
    rori @ say "To tell you the truth, it was really nice but I don't think I can do that again without us committing to each other. You know what I mean?"
    
    player "I get you. It was just an experiment."
    
    show rori jacket supersmug blush
    
    rori @ say "A fun experiment~"
    
    show rori jacket concerned
    
    rori @ say "But now it's time to get serious."
    rori @ say "I think we'll both need time to figure things out for ourselves."
    
    player "For sure."
    
    hide rori with dissolve
    
    n "You spend some time getting yourself together than give Rori a big hug before leaving to return to your own dorm."
    
    #rori @ say "Until then..."
    #n "He gives you a parting kiss"
    

    #rori @ say "That alcohol is really starting to kick in~"


label autumnBreakPt2:
    stop music fadeout 2.0

    scene bg black with dissolve

    n "The following day..."
    
    scene bg codadorm autumn day with fade
    
    play music "audio/music/Vylet Pony - Cozy Pone.ogg" fadein .4
    
    show box:
        ypos 0
    
    n "It sure is nice waking up on a Monday without having to worry about going to classes."
    n "But it does get a little boring not having anything to do. No responsibilities but also half your friends are away."
    n "Wait, you have the technology to see what they're up to. Time to stalk some social media."
    
    #n "How does she have so many autumn break pictures already when it's only just begun?"
    #n "Ooh Claire went to the beach!"
    
    image porcupine_social = "images/coda social media porcupine.png"
    #show image "images/coda social media porcupine.png" at center with dissolve:
    show porcupine_social at center with dissolve:
        yoffset 200
    
    n "You end up on Claire's account and see what she's posted recently."
    n "\"OwO?\""
    n "What did she mean by this?"
    n "You scroll down to her more recent pics."
    
    image claire_social1 = "images/coda social media claire1.png"
    #show image "images/coda social media claire1.png" at center
    show claire_social1 at center:
        yoffset 200
    
    n "It's your typical girl's social account, full of selfies."
    
    image claire_social2 = "images/coda social media claire2.png"
    show claire_social2 at center:
        yoffset 200
    #show image "images/coda social media claire2.png" at center
    
    hide claire_social1
    hide porcupine_social
    
    n "God damn."
    n "You're surprised she doesn't have more followers."
    n "Oh? She just sent you a message!"
    
    hide claire_social2 with dissolve
    
    call phone_start from _call_phone_start_26 
    
    call message_start("Claire", "Heyyyy~", "claireavi.png") from _call_message_start_33 
    call message("Claire", "Just got a notif saying you were scrollin my profile", "claireavi.png") from _call_message_241 
    call message("Claire", "Like what u see? ;3", "claireavi.png") from _call_message_242 
    
    if clairePoints > 12:
        call reply_message("Yeah, you lookin cute lmao") from _call_reply_message_171
    
        call message("Claire", "Thx UwU", "claireavi.png") from _call_message_243 
    if clairePoints <= 12:
        call reply_message("I accidentally clicked your page I swear") from _call_reply_message_172
        
        call message("Claire", "Suuuuure", "claireavi.png") from _call_message_252 
        
    call reply_message("How's your break going?") from _call_reply_message_173
    
    call message("Claire", "Good! I miss u tho!!!", "claireavi.png") from _call_message_254 
    
    call reply_message("Aww it's only been a couple days") from _call_reply_message_174
    call reply_message("I miss the gang too tho") from _call_reply_message_175
    call reply_message("Yeah it gets lonely without you all here") from _call_reply_message_176 
    
    call message("Claire", "DW we'll be back to have fun again soon!!!", "claireavi.png") from _call_message_255 
    
    if fuckedClaireEarly == True:
        call reply_message("Speaking of fun...") from _call_reply_message_177 
        call reply_message("That thing we did last week was nice~") from _call_reply_message_178 
        
        call message("Claire", "It sure was~", "claireavi.png") from _call_message_256 
        call message("Claire", "But it happened at the worst time possible cause midterms and now I'm a million miles away ;^;", "claireavi.png") from _call_message_257 
        call message("Claire", "I wish we could have had more time to talk about it in person", "claireavi.png") from _call_message_258 
        
        call reply_message("Ikr") from _call_reply_message_179 
        call reply_message("I don't regret it but it was sort of a heat of the moment thing") from _call_reply_message_180 
        call reply_message("I'm still trying to figure some things out") from _call_reply_message_181 
        call reply_message("But I'd love to spend more time with you when you're back <3") from _call_reply_message_182 
        
        call message("Claire", "Okiiii I get u", "claireavi.png") from _call_message_259 
        call message("Claire", "Take your time thinking", "claireavi.png") from _call_message_260 
        call message("Claire", "I know you'll be mine sooner or later >:3", "claireavi.png") from _call_message_261 
        
        #ikr it was reallllly bad timing cause of finals and then my flight home so we didnt even have a chance to talk about it!
        #i don't regret it but i don't think i'm quite ready for a relationship at the moment. i still need to figure some things out but i'll get back to you on that soon i promise

    call reply_message("Hold on, Ava's texting me") from _call_reply_message_190
    
    call message("Claire", "OMG TELL THAT BITCH I SAID HIIIII", "claireavi.png") from _call_message_262 
    
    call message("Ava", "Hi [name]! Just wanted to see how you're doing!", "avaavi.png") from _call_message_263 
    
    call reply_message("I'm good lol just bored cause half my friends abandoned me") from _call_reply_message_192
    
    call message("Ava", "Sorry!!!! O^O", "avaavi.png") from _call_message_264 
    
    call reply_message("jk it's nice to chill and not worry about anything for a bit") from _call_reply_message_193
    
    call message("Ava", "Hang in there! Claire tells me she has plans for all of us once we're back ^v^", "avaavi.png") from _call_message_265 
    
    call reply_message("Not sure if I should be excited or nervous") from _call_reply_message_194
    call reply_message("How's your break going?") from _call_reply_message_195
    
    call message("Ava", "Pretty good! I'm at a party right now and you'll never believe who showed up!", "avaavi.png") from _call_message_266 
    
    call message("Gunner", "Sup humie", "gunneravi.png") from _call_message_267 
    
    call reply_message("The hell? Gunner lives near you?") from _call_reply_message_196
    
    call message("Ava", "Not exaaaaactly", "avaavi.png") from _call_message_268 
    
    call message("Gunner", "I can be anywhere on the continent in a couple hours", "gunneravi.png") from _call_message_269 
    call message("Gunner", "The perks of owning a private supersonic jet :3c", "gunneravi.png") from _call_message_270 
    
    call reply_message("Oh I see you're simply stalking her") from _call_reply_message_197
    
    call message("Gunner", "It's legally not considered stalking if I'm hot", "gunneravi.png") from _call_message_271 
    
    call message("Ava", "Facts", "avaavi.png") from _call_message_272 
    call message("Ava", "Wish you were here [name]!", "avaavi.png") from _call_message_273 
    
    call reply_message("Hopefully I can make it next time") from _call_reply_message_198
    
    call screen phone_reply("Without Gunner","withoutGunner","Get everyone together","everyoneParty")
    
label withoutGunner:
    $ partyWithoutGunner = True
    
    call phone_after_menu from _call_phone_after_menu_7 
    
    call message_start("me", "Gunner's not invited tho", "testimage.png") from _call_message_start_34 

    call message("Gunner", "Fuck you, what did I do", "gunneravi.png") from _call_message_274 
    
    call reply_message("Sorry bro, just don't wanna watch you get cucked when I steal your crush") from _call_reply_message_199
    
    call message("Gunner", "Over my dead body", "gunneravi.png") from _call_message_275 
    call message("Gunner", "We all know how this ends", "gunneravi.png") from _call_message_276 
    call message("Gunner", "I get the cute girl and you end up with a 400 pound bunny", "gunneravi.png") from _call_message_277 

    call message("Ava", ">implying Claire isn't a cutie", "avaavi.png") from _call_message_278 
    
    call reply_message("Plot twist: Claire steals Ava from us") from _call_reply_message_200
    
    call message("Ava", "And then you two start going out together! :>", "avaavi.png") from _call_message_279 
    
    call message("Gunner", "Yeah I'd just kill myself", "gunneravi.png") from _call_message_280 
    call message("Gunner", "Txt you later [name], enjoy jerking off alone", "gunneravi.png") from _call_message_281 
    
    call reply_message("You too") from _call_reply_message_201
    
    call message("Ava", "See you soon!", "avaavi.png") from _call_message_282 
    
    call phone_end from _call_phone_end_32 
    
    jump afterAutumnPhone
label everyoneParty:
    $ partyWithEveryone = True

    call phone_after_menu from _call_phone_after_menu_8 
    
    call message_start("me", "We should party with the whole crew", "testimage.png") from _call_message_start_35 
    
    call message("Ava", "Yeah! Claire's fun to party with!", "avaavi.png") from _call_message_283 
    
    call message("Gunner", "You remember that time I tried bringing Rori with us :|", "gunneravi.png") from _call_message_284 
    
    call reply_message("He was just shy cause it was his first time") from _call_reply_message_202
    
    call message("Ava", "I bet he'd be a real party animal!", "avaavi.png") from _call_message_285 
    
    call message("Gunner", "Speaking of which, we've got a party to get back to >:3", "gunneravi.png") from _call_message_286 
    
    call message("Ava", "Yeahhhhh txt u later [name]!", "avaavi.png") from _call_message_287 

    call reply_message("See you guys later. Try not to get too wild.") from _call_reply_message_210

    call phone_end from _call_phone_end_33 
    
    jump afterAutumnPhone
    
label afterAutumnPhone:
    n "Seems like everyone's enjoying their autumn break."
    
    if partyWithoutGunner == True:
        n "It kinda irks you that you can't be at that party with Ava."
        n "The thought of Gunner flirting with her pisses you off."
        n "You'll have to get your revenge next time you see them. Maybe you'll challenge him to a duel to the death."
    
    
    if invitedToEllensHouse == False:
        n "There's not much to do here. You hadn't realized how dull your life could be without friends to hang out with."
        n "Rori's busy tinkering with his loonix boxes today and you don't even know how to find Mishka with the cafe being closed."
        n "That leaves... no one? You really need to make more friends."
        #n "Only options now are to go for a walk or masturbate."
        n "You should get out of this dorm. It's starting to feel like a prison."
        
        jump trish1
    
    else:
        n "Lucky for you, you've got plans today. Big plans."
        n "Your hot milf dog professor wants you to come over to her house today. You know what that means?"
        
        scene bg streets with dissolve
        
        play music "audio/ambient/outdoors night crickets.ogg" fadein 0.1
        
        show box with Dissolve(.2):
            ypos 0
        
        n "*knock knock knock*"
        n "You almost can't believe you're doing this. You're starting to feel nervous."
        n "Did you remember to brush your teeth this morning? What if she thinks you smell weird?"
        n "Were you supposed to bring condoms? Does it even matter?"
        n "Is this even the right address? What if she was just messing with you and gave you a fake one?"
        n "You're about to knock on the door again when it creeps open."
        
        show margaret pajamas shocked at center with dissolve:
            ypos y_margaret
        
        margaret @ say "Hello..?"
        
        show margaret melancholy pawdown
        
        margaret @ say "Oh my goodness, [name]! I can't believe you actually showed up! Were we supposed to meet today? I thought it was tomorrow!"
        
        player "You said to come over on Monday..."
        
        margaret @ say "Right, silly me. I thought it was still Sunday. Come on in and make yourself at home!"
        
        scene bg ellenbedroom with dissolve
        
        play music "audio/music/vylet - sleepless.ogg" fadein .4
        
        show box with Dissolve(.2):
            ypos 0
        
        n "Ms. Ellen invites you inside and shows you to her bedroom."
        n "Oh god oh fuck it's really happening"
        n "You wonder what her favorite position is. Probably doggystyle lmao."
        n "As your mind races with perverse thoughts, something catches your attention."
        
        player "Wait a minute, is that a SNES?"
        
        show margaret pajamas shy at center with dissolve:
            ypos y_margaret
            xoffset -100
            xzoom -1
        
        margaret @ say "Yeah? I was doing my yearly playthrough of Chrono Trigger."
        
        player "Holy based. How far are you?"
        
        show margaret pajamas smile pawdown
        
        margaret @ say "I just got to Magus's castle. I'm gonna run through it with Frog and Lucca."
        
        player "Nice. I didn't expect you to be a gamer!"
        
        show margaret happy
        
        margaret @ say "I'm really not! I don't play a lot of the new stuff."
        
        show margaret content
        
        margaret @ say "As with literature, I'm only really fond of the classics~"
        
        menu:
            margaret "{cps=0}As with literature, I'm only really fond of the classics~{/cps}"
            "Same":
                $ ellenPoints += 1
                
                player "Same. Nothing beats that era of games."
                
                show margaret happy
                
                margaret @ say "So many good RPGs~"
                
                show margaret downtrodden pawdown
                
                margaret @ say "I'm still waiting on a good translation hack for some Japan exclusives..."
                
                player "You must have played a ton if you're that deep into it."
                
                show margaret melancholy pawdown
                
                margaret @ say "I might've played as many RPGs as I've read books! And I've read *a lot* of books."
                
                n "Any inkling of having an intimate moment with your professor has left your mind and been replaced with a desire to experience the golden age of gaming with someone who grew up with it."
                
                player "Any chance you've got anything we could play together?"
                
                show margaret smile pawdown
                
                margaret @ say "Of course!"
            "These were before my time":
                player "SNES is before my time but it has some good games."
                
                show margaret upset pawdown
        
                margaret @ say "Now you've made me feel old. I could have sworn this was next gen just a few years ago!"
                
                show margaret surprised
                
                margaret @ say "3D stuff still feels new to me to be honest."
                
                player "Wow. We really are from different generations."
                
                show margaret unimpressed
                
                margaret @ say "You kids are all used to realistic graphics that leave nothing to the imagination!"
                
                show margaret melancholy
                
                margaret @ say "But I tell you, I've been brought to tears from 8-bit games that only had 256 colors to work with!"
                #and paying to win but we had to work for victory! And we only had 256 colors to work with!"
                
                player "Heh okay boomer. I started out on a PS2 but I'd be down to play some retro games with you."
                
                show margaret annoyed
                
                n "Miss Ellen winces when you say \"retro.\" These consoles may seem outdated to you but to her they're still as revolutionary as the day they released."
        
        show margaret neutral
        
        margaret @ say "I'm sure I have a multiplayer game somewhere around here..."
        margaret @ say "I've never really had the chance to play with someone before hah..."
        
        n "Plastic clatters against plastic as she digs around a disorganized pile of cartridges."
        
        show margaret pajamas shocked
        
        margaret @ say "Oh how about this one?"
        
        show margaret neutral
        
        n "She holds up SNES cart, the label worn and hard to read."
        
        player "Battletoads? Really?"
        
        show margaret grin pawdown
        
        margaret @ say "Bet I can get a higher score than you~"
        
        n "Her tail swishes eagerly. How can you say no?"
        
        player "Alright but if I win I'm staying the night."
        
        show margaret suggestive -pawdown
        
        margaret @ say "Deal!"
        
        n "She rips out the previous cartridge and slams Battletoads into the console before flipping the power switch."
        
        show margaret pajamas happy
        
        margaret @ say "Aaaaand here's your controller!"
        
        show margaret pajamas neutral
        
        n "As she unwinds the cord, a sweet aroma fills the air followed by beeping coming from the other room."
        
        show margaret pajamas shocked
        
        margaret @ say "Oh! I forgot I had cookies in the oven! Be right back."
        
        pause .1
        
        show margaret at offscreenright with move:
            ypos y_margaret
            xoffset 300
        
        n "First video games with your professor and now home baked cookies?"
        n "This day just keeps getting better and better."
        
        scene bg ellenbedroom with fade
        
        play music "audio/music/mere - schooldaze faster.ogg" fadein .4
        
        show box with Dissolve(.2):
            ypos 0
        
        n "The hours pass by, laying in your professors bed while munching on cookies and running through this beat 'em up game."
        n "Once Ms. Ellen taught you the strats it actually became pretty fun. Of course her score was naturally always just ahead of yours."
        n "She wasn't kidding about being experienced."
        
        show margaret pajamas happy at center with dissolve:
            ypos y_margaret
        
        margaret @ say "Oh this is the final level! Get ready!!!"
        
        hide margaret with dissolve
        
        n "You lean forward, taking the game a bit more seriously now."
        n "It gets pretty tough but Ms. Ellen is always there to bail you out."
        
        if ellenPoints > 7:
            $ stayedNightAtMargaretsHouse = True
            
            n "You're neck and neck throughout the final sequence but she hangs back during the last moments, allowing you to get the killing blow on the boss."
            n "You're sweating and your hands are shaking from all the button mashing but you've done it. Your score ends up being a hair above hers."
            
            show margaret pajamas content at center with dissolve:
                ypos y_margaret
            
            margaret @ say "Oh noooo, you won! Guess that means you're staying the night~"
            
            player "You let me win on purpose, didn't you?"
            
            show margaret shy pawdown
            
            margaret @ say "Mmmmmaybe~"
            
            show margaret melancholy pawdown
            
            margaret @ say "Or maybe I'm just too good of a Battletoads mentor hehe!"
            
            show margaret mischief
            
            margaret @ say "Either way, you're mine now! And I'm gonna force you to play more of these \"retro\" games with me!"
            
            player "Nooo, anything but that haha!"
            player "I definitely don't enjoy older things haha!"
            
            show margaret suggestive -pawdown
            
            margaret @ say "You will once I'm done with you~"
            
            n "Ms. Ellen pounces on you, growling and playfully biting at your neck. She's so gentle though it gives you more of a ticklish feeling."
            
            player "Pfffft hahaha whoa now! Down girl! Sit!"
            
            show margaret surprised
            
            n "Your professor immediately halts and pulls off of you, sitting like the dog she is. She seems to be awaiting another command."
            
            show margaret shy pawdown
            
            player "Uhh roll over?"
            
            n "Without hesitation, she rolls onto her back. Instinctively you reach out to rub her belly."
            
            player "Who's a good girl?~"
            
            show margaret shocked pawdown
            
            margaret @ say "Meeee? Is it me?!"
            
            player "Mmmyeah~"
            
            show margaret happy
            
            n "Her tail wags so fast you're afraid she'll take flight."
            
            margaret @ say "Woof!"
            
            show margaret surprised
            
            margaret @ say "Err, pardon me..."
            
            pause .1
            
            show margaret at shudder
            
            pause .2
            
            show margaret upset pawdown at flipright
            
            n "She suddenly regains her composure and sits back up."
            
            margaret @ say "I don't know what came over me..."
            
            show margaret shocked pawdown
            
            margaret @ say "It just felt so right to do those things... maybe because you're a human?"
            
            player "I guess this old dog can still learn new tricks~"
            
            show margaret mischief -pawdown
            
            margaret @ say "I'd be more than just man's best friend if we kept that up~"
            
            show margaret surprised
            
            margaret @ say "Sorry, pretend I didn't say that!"
            
            pause .1
            
            show margaret at flipleft
            
            n "Flustered, she looks away and reaches down to picks up a catridge off the floor. Kirby Super Star. Excellent taste."
            
            show margaret happy
            
            margaret @ say "Hey, wanna 100\% The Great Cave Offensive with me?"
            
            show margaret neutral
            
            player "Of course!"
            
            hide margaret with dissolve
            
            n "You blaze through the whole game well into the night until your eyes are strained from staring at the screen for so long."
            n "You're starting to get tired too."
            n "Miss Ellen offered to let you stay the night. You wonder where you'll sleep."
            
            player "*Yawn*"
            player "Getting sleepy."
            
            show margaret pajamas neutral at center with dissolve:
                ypos y_margaret
            
            margaret @ say "Me too."
            
            show margaret content
            
            margaret @ say "I had a lot of fun just chilling with you today. Not having to worry about classes or pretend to be professional is nice."
            
            player "Yeah, you're really nice to hang out with. Didn't feel awkward at all. Not even being sarcastic."
            
            show margaret melancholy pawdown
            
            margaret @ say "You think so? Maybe we should do this more often then?~"
            
            player "Play vidya on your bed? Or hang out in general?"
            
            show margaret happy
            
            margaret @ say "Both!"
            
            show margaret melancholy -pawdown
            
            margaret @ say "But some days I do just lie in bed all day. Would be nice to have some company~"
            
            show margaret shy pawdown
            
            margaret @ say "Speaking of which..."
            
            n "She reclines on the bed. Her head hits the pillow with a satisfying *pomf* sound."
            
            show margaret suggestive -pawdown
            
            margaret @ say "Would you like to sleep with me?"
            
            n "Did-"
            n "Did she just"
            
            player "Y-you want me to sleep with you?"
            
            show margaret neutral
            
            margaret @ say "Yeah!"
            
            show margaret surprised
            
            margaret @ say "O-oh, not like that honey."
            
            show margaret pleading
            
            margaret @ say "I just didn't want you to have to sleep on the couch is all."
            
            show margaret melancholy
            
            margaret @ say "Sorry, I could have worded that better."
            
            player "I would think a literature professor would be more careful with her words."
            
            show margaret content
            
            margaret @ say "I may be a little irresponsible heh..."
            
            player "It's cute~"
            
            show margaret happy
            
            margaret @ say "Speak for yourself!"
            
            show margaret neutral
            
            n "She slips under the blanket and holds it up for you."
            
            show margaret scolding
            
            margaret @ say "Now hurry up and get in, I'm getting cold!"
            
            show margaret suggestive
            
            player "Yes ma'am~"
            
            n "You crawl underneath the cover and pop your head up above the pillows."
            n "God there's so many pillows. How many cushions does a single dog need?"
            
            show margaret neutral
            
            margaret @ say "Comfy?"
            
            player "Quite."
            
            margaret @ say "Good~"
            
            n "She rolls over and reaches for the lamp on the bedstand beside you. She has to crawl over you to get to it."
            
            show margaret melancholy
            
            margaret @ say "Heh, sorry about that. I can't sleep with the light on."
            
            player "It's all good."
            
            if romanticFantasy == False:
                show margaret shocked pawdown
                
                margaret @ say "You're not cold are you?"
                
                n "Miss Ellen grabs hold of your hand."
                
                margaret @ say "My, you're burning up!"
                
                show margaret shy
                
                margaret @ say "Would you mind if I steal some of your warmth?"
                
                menu:
                    margaret "{cps=0}Would you mind if I steal some of your warmth?{/cps}"
                    "Go for it":
                        $ margaretRomanticFantasy = True
                        $ romanticFantasy = True
                        $ ellenPoints += 1
                        
                        player "Go for it. Steal as much as you want."
                        
                        show margaret grin pawdown
                        
                        n "Once again you get pounced on, this time in a more snuggly way."
                        n "Miss Ellen's soft fur wraps around you, caressing your skin. You gently stroke it with your fingers."
                        n "Up close, she's got that dog smell but very well groomed. You can't say you mind it."
                        
                        margaret @ say "Thanks [name]~"
                        
                        player "Don't mention it. You get the warmth, I get the floof."
                        
                        show margaret suggestive pawdown
                        
                        margaret @ say "Hehe go ahead and scritch all you want~ Just be careful where those hands end up!"
                        
                        player "I won't go anywhere you don't want me to!"
                        
                        show margaret happy
                        
                        margaret @ say "Behind the ears is a good spot~"
                        
                        player "Where even are they?"
                        
                        margaret @ say "Somewhere underneath all this hair, hun."
                        
                        n "You feel around until your fingertips make contact with her velvety soft ears."
                        
                        player "Like this?"
                        
                        show margaret content
                        
                        margaret @ say "Mmmh oh yeah, that's the stuff~"
                        
                        n "Her leg kicks as you rub behind her ear."
                        
                        player "Such a good dog~"
                        
                        show margaret suggestive -pawdown
                        
                        margaret @ say "You haven't seen anything yet~"
                        
                        show margaret surprised
                        
                        margaret @ say "Gosh I can't believe I'm engaging in casual pet play with a student... I imagine the university wouldn't think highly of that."
                        
                        player "Don't worry, I won't tell anyone."
                        
                        show margaret neutral
                        
                        margaret @ say "I know you wouldn't."
                        
                        show margaret shy
                        
                        margaret @ say "But even if you did, I don't think I'd regret it."
                        
                        show margaret angry
                        
                        margaret @ say "Screw the university! I don't want to be chained down to that facade of academics and prestige."
                        
                        show margaret downtrodden
                        
                        margaret @ say "*Sigh*"
                        
                        show margaret pajamas melancholy shocked
                        
                        margaret @ say "I just want to live my life. Is that so wrong?"
                        
                        player "This might be a dumb question, but why don't you? Just live your life I mean."
                        
                        show margaret downtrodden pawdown
                        
                        margaret @ say "I suppose it's not that easy. Habits are hard to break you know?"
                        margaret @ say "There's comfort in having my cushy job and being looked up to and being entrusted with all these responsibilities."
                        margaret @ say "But if I could go back and never have any of it..."
                        
                        show margaret melancholy pawdown
                        
                        margaret @ say "I just miss those days in the old arcades. No worries, no plans, just living in the moment."
                        
                        player "I think I get what you mean. That's sorta how my life is right now. I just wake up each day and get dragged into some wacky thing one of my friends schemed."
                        
                        show margaret happy
                        
                        margaret @ say "Exactly! I want to have someone to try new things with, explore different places. Not get bogged down in figuring out mortgages and slideshow presentations."
                        
                        show margaret seethe
                        
                        margaret @ say "But at my age, everyone's so involved in their careers and appearances. They're more concerned about looking good than having a good time."
                        
                        show margaret unsure
                        
                        margaret @ say "And well, anyone who's not is struggling just to keep their head above the water."
                        
                        player "So you want a luxurious life style without the responsibilities?"
                        
                        show margaret upset pawdown
                        
                        margaret @ say "When you put it like that, it does sound selfish doesn't it?"
                        
                        show margaret unimpressed
                        
                        margaret @ say "But I don't care. I know what I want. I just don't know how to get it."
                        margaret @ say "I should be living like it's my last day on this earth. I ain't getting any younger so I might as well make the most of it all."
                        
                        show margaret content
                        
                        margaret @ say "Traveling, partying, some general mischief, a little bit of sex drugs and rock and roll..."
                        
                        show margaret downtrodden pawdown
                        
                        margaret @ say "I wish I had someone who felt the same way. Dedicated to each other and up against the rest of the world to make it ours. We'd make it work."
                        
                        player "Sounds like a lot to ask for..."
                        
                        menu:
                            player "{cps=0}Sounds like a lot to ask for...{/cps}"
                            "I hope you find what you're looking for":
                                show margaret pajamas upset pawdown
                            
                                player "But I hope you find someone who can do all that for you."
                                player "I'm just a broke student figuring things out as I go along, but I can at least treat you like a friend rather than a professor."
                                
                                show margaret content
                                
                                margaret @ say "Thank you, [name], that's incredibly sweet of you~"
                                
                                show margaret downtrodden pawdown
                                
                                margaret @ say "Maybe what I'm asking for is too much... it's just a silly little romantic fantasy I have, nothing more."
                                margaret @ say "Next week I'll get up and go back to teaching like it's all the same to me."
                                
                                show margaret melancholy pawdown
                                
                                margaret @ say "But at least you'll know I'm thinking about quitting my job and buying a camper van to travel the country!"
                                
                                player "If you do, let me know! I could be swayed to drop out and see what this country has to offer to a vagabond."
                                
                                show margaret shy pawdown
                                
                                margaret @ say "It's probably not as glamorous as it sounds, but hey I'd let you come along in exchange for scritches~"
                                
                                player "Heh, good bitches get scritches~"
                                
                                show margaret angry
                                
                                margaret @ say "Hey! Is that any way to speak about your professor?"
                                
                                player "Sorry."
                                
                                show margaret content
                                
                                margaret @ say "Hehe I'm kidding~ You just said you see me more as a friend at this point anyway so I think any semblance of professionalism has gone out the window."
                                
                                player "True. I was just testing the waters."
                                
                                show margaret grin pawdown
                                
                                margaret @ say "As long as it's behind closed doors... I'll be a good bitch for the scritch~"
                                
                                show margaret suggestive
                                
                                player "That's a good girl~"
                                
                                n "You reward her with a barrage of scritches with both hands all over her back. You can't get enough of that cute hind leg kick she does on reflex."
                                
                                margaret @ say "*Whiiiiine*"
                                
                                n "You can hear her tail swishing against the blanket."
                                
                                player "Alright, that's all I had left in me. Need to sleep now."
                                
                                show margaret melancholy
                                
                                n "She lets out a disappointed whine."
                                
                                margaret @ say "Aww, just when the fun is starting..."
                                
                                show margaret neutral
                                
                                margaret @ say "It has gotten quite late though. See you in the morning, [name]~"
                                
                                player "Goodnight Miss Ellen. I'm glad to be here with you like this tonight."
                                
                                margaret @ say "As am I~ Goodnight~"
                                
                             
                            "Could be me >:3":
                                $ ellenPoints += 1
                                
                                player "Bet I could fill that role >:3"
                                
                                show margaret mischief
                                
                                margaret @ say "Kshh, you? You really think so?"
                                
                                show margaret pajamas shocked 
                                
                                margaret @ say "Wait, you sounded way too eager. What's going on in that head of yours?"
                                
                                show margaret unimpressed
                                
                                player "Nothing, I just like the idea of dropping out and roaming the country in a camper van with a hot milf teacher is all."
                                
                                show margaret melancholy pawdown
                                
                                margaret @ say "M-me? A hot milf?! And who said anything about living in a camper van?"
                                
                                player "You said you wanted to travel and try new things. Life on the road is about as free as it gets. With a camper you can go anywhere you want!"
                                
                                show margaret content
                                
                                margaret @ say "Admittedly, it does sound nice... even if it's a bit of a mid-life crisis cliche. I'll say it does make for a cute little romantic fantasy."
                        
                                player "I'm not too attached to the idea of sitting still for four years getting a useless meme degree, I'm just doing it cause I've got nothing better to do."
                                
                                show margaret downtrodden pawdown
                                
                                margaret @ say "Well, I guess if I retired early to travel it would be nice to have a handy man to fix things up for me~"
                                
                                player "Yeah? I can do a lot more than that too! We could be wild party animals on the road, having fun wherever we go~"
                                
                                show margaret melancholy -pawdown
                                
                                margaret @ say "Pshh okay it does sound fun. ...But you're not serious are you?"
                                
                                player "Depends on if you'd be down for it."
                                
                                show margaret shy pawdown
                                
                                margaret @ say "Hmm... I'll definitely have to consider it."
                                
                                player "Would scritches sweeten the deal?"
                                
                                show margaret happy
                                
                                margaret @ say "You've seen how easily I'm bribed with small tokens of affection~"
                                
                                n "You work your fingers into her back, gently digging your nails in until she's kicking her leg on reflex."
                                
                                show margaret suggestive
                                
                                margaret @ say "Oooh, there's just something about humans that can do that *so* well~"
                                
                                player "Imagine this but every single night~"
                        
                                margaret @ say "You drive a hard bargain, young man~"
                                margaret @ say "I can't just up and leave everything behind right this minute but I won't flat out say no to your little plan~"
                                
                                player "So there's a chance?"
                                
                                show margaret smile pawdown
                                
                                margaret @ say "However small it may be, but yes there's a chance."
                                
                                show margaret melancholy
                                
                                margaret @ say "Let's sleep on it for now though, okay? It's past my bedtime."
                                
                                player "Alright. Goodnight Miss Ellen."
                                
                                margaret @ say "Goodnight, [name]."
                                
                                n "The professor leans in and plants a sweet smooch on your lips before realizing what she's done and suddenly tensing up."
                                
                                show margaret surprised
                                
                                margaret @ say "Ah-!"
                                margaret @ say "That was an accident!!!"
                                
                                pause .1
                                
                                show margaret at flipright
                                
                                show margaret unsure
                                
                                margaret @ say "Sorry, it was just a force of habit. Say goodnight and then a little smooch. That's how I did it for over a decade."
                                
                                player "It's okay, I understand."
                                
                                n "You gently stroke her fur until she calms down."
                                
                                show margaret upset pawdown
                                
                                player "Even if you didn't mean anything by it, I kinda liked it. So there's that."
                                
                                show margaret suggestive
                                
                                margaret @ say "Yeah, I bet a little perv like you absolutely would~"
                                
                                player "Huh?"
                                
                                n "You become aware that in stroking her fur, your hand has ended up squarely on her ass."
                                
                                player "Well I don't see you complaining!"
                                
                                show margaret shy
                                
                                margaret @ say "You're right, I'm not~"
                                margaret @ say "But let's leave it here for tonight, because I am seriously tired."
                                
                                show margaret suggestive pawdown 
                                
                                margaret @ say "Keep scritching though."
                                
                                player "Yes ma'am~"
                                
                                n "You gently knead your fingers into her plush rump as you drift into sleep."
                        
                                        
                    
                    "It's all mine":
                        $ ellenPoints -= 1
                    
                        player "Sorry, this warmth is all mine."
                        
                        show margaret downtrodden pawdown
                        
                        margaret @ say "Aww... Forget I asked."
                        
                        show margaret neutral
                        
                        margaret @ say "Have a good night [name]."
                        
                        player "You too, Ms. Ellen."
                        
                        
            
            else:
                n "You settle in against the silky sheets and close your eyes."
                n "It's almost unbelievable that you're here right now, lying beside your literature professor after a long day of gaming."
                n "Hopefully she doesn't regret it in the morning."
                
            stop music fadeout 2.0
            
            scene bg black with dissolve
            
            scene bg ellenbedroom with fade
            
            play music "audio/ambient/morning birds.ogg" fadein 0.1
            
            show box with Dissolve(.2):
                ypos 0
        
            n "When you rouse from slumber, the other half of the bed is empty."
            n "Did Ms. Ellen change her mind about \"sleeping with you?\""
            n "You stretch and crawl out of bed. What now?"
            n "You're looking through her game collection when a savory smell wafts through the room."
            n "When you're about to see what's cooking, Miss Ellen bursts through the door."
            
            show margaret pajamas happy at center with dissolve:
                ypos y_margaret
            
            margaret @ say "Heya sleepyhead! Come get some breakfast! Hope you like pancakes and bacon!"
            
            n "After subsisting on nothing but cookies and snacks yesterday, you could go for a real meal."
            
            player "That sounds perfect right about now!"
            
            hide margaret with dissolve
            
            n "Miss Ellen leads you to the dining room and gives you a full breakfast before sending you on your way."
            n "...She's definitely wife material. Dunno why her ex-husband divorced her."
                

            
        else:
            n "You're neck and neck throughout the final sequence but you manage to get the killing blow on the boss."
            n "You're sweating and your hands are shaking from all the button mashing but for all your efforts you still end up with a lower score."
            
            show margaret pajamas content at center with dissolve:
                ypos y_margaret
            
            margaret @ say "Darn, what a shame. You almost had me there!"
            
            player "I didn't think I was dealing with a pro gamer here!"
            
            show margaret grin pawdown
            
            margaret @ say "All that time in the arcades finally paid off!"
            
            show margaret suggestive
            
            player "You went to arcades?"
            
            margaret @ say "Of course! They were THE place to be! How do you think I got into gaming?"
            
            show margaret downtrodden pawdown
            
            margaret @ say "A shame they don't really exist anymore. I'd love to relive those days."
            
            player "Man, I never even got to experience one."
            
            margaret @ say "Those days are long gone, unfortunately."
            margaret @ say "*Sigh*"
            
            show margaret happy
            
            margaret @ say "But this was close enough I'd say!"
            
            show margaret pajamas neutral
            
            player "Yeah! Playing retro games with my literature professor ended up being way more fun than I would have thought!"
            player "I'd love to do it again whenever you wanna go back to the good old days!"
            
            margaret @ say "I've got plenty of free time so just hit me up!"
            
            n "Miss Ellen stands up and stretches. She checks the time and looks outside."
            
            show margaret pajamas shocked
            
            margaret @ say "My, it's gotten late. Will you be okay walking back home in the dark?"
            
            player "I can manage. It's just a short way back to my dorm."
            
            show margaret pajamas melancholy -shocked
            
            margaret @ say "Well then, I'll see you in class then?"
            
            player "Yup. See you next week!"
            
            n "Miss Ellen gives you a parting hug, pulling you off the ground for a moment."
            
            player "Whoa haha, easy girl."
            
            show margaret shy
            
            margaret @ say "Thanks for hanging out with me. It's not every day I get to feel this young again!"
            
            player "It was awesome getting to see this side of you. You're not really a snooty professor, you're just a chill gamer girl."
            
            show margaret happy
            
            margaret @ say "Haha well if you reveal my secret to anybody, I'll fail you!"
            
            player "And doom me to another semester with you?"
            
            show margaret suggestive
            
            margaret @ say "Yes~"
            
            show margaret grin pawdown
            
            margaret @ say "Now gimme some scritches before you leave!"
            
            player "Yes ma'am~"
            
            hide margaret with dissolve
            
            n "You smile as her leg kicks on reaction from your fingers digging into her fur. You leave her wagging her tail even as you step out the door and wave goodbye."
            

        
        jump midweekAutumnBreak
    


label trish1:
    $ metTrish = True
    
    scene bg campus autumn day with dissolve
    
    play music "audio/music/Vylet Pony - lemonade.ogg" fadein .4
    
    show box:
        ypos 0
    
    n "A walk around the campus does wonders for your sanity. Sometimes you really just need to get that blood pumping."
    n "As you round a corner, you're knocked backward and fall to the ground."
    
    #rewrite this a bit so trish reflects on your choices

    trish @ say "Oh my gosh are you okay???"
    #hide sayfarleft with Dissolve(.2)
    
    show trish neutral at norm with dissolve:
        xzoom -1
    
    n "Standing over you is the fattest possum you've seen in your life."
    n "Even fatter than the one your cousin caught in his garage and kept as a pet."
    n "And she smells more like trash than your cousin's possum ever did."
    n "While you're still seeing stars, she pulls you up to your feet."
    
    player "Uhh, sorry about that."
    
    n "You do a 360 and start to walk away but just end up bumping into her again."
    
    trish @ say "You alright there? Did you bump your head or something?"
    trish @ say "I bumped my head once really hard when I was little and since then I don't remember things too good anymore."
    trish @ say "Then again, I don't remember if I had good memory when I was little so maybe I was always like this."
    trish @ say "What did you say your name was again?"
    
    player "[name]? Wait yeah it's definitely [name]."
    
    n "You must have hit your head harder than you thought."
    
    trish @ say "Hehe I guess you don't remember things either! We have so much in common!"
    trish @ say "My name's uhh...."
    trish @ say "Ummmmmm....."
    trish @ say "Oh yeah, it's Trish! Trish de la {a=https://e926.net/posts?tags=trish_\%284chan\%29}Trash{/a}!"
    
    if gunnerRaid == True:
        player "Wait I remember you! You raided my underwear drawer!"
        
        trish @ say "Ksksksks guilty as charged!"
        trish @ say "It was part of my sorority's initiation ritual!"
        
        player "More like humiliation ritual!"
        
        trish @ say "Sorryyyy, would you like them back? I'm wearing them right now. Kinda tight on me though."
        
        player "What the fuck? Just... keep them."
    
    trish @ say "So where are you going?"
    
    player "Nowhere really? I'm just on a walk-"
    
    trish @ say "Noooo I mean where are you *going?*"
    trish @ say "Like in liiiiife?"
    
    player "Oh. Still probably nowhere."    
    player "Why do you ask?"
    
    trish @ say "Cause you've got an interesting aura about you!"
    
    player "Aura? What's that all about?"
    
    trish @ say "Let's just say I can detect certain things about you~"
    trish @ say "Liiiiike I know you've got a crush!"
    
    player "Is it that obvious?"
    player "Wait, have you been following me?"
    
    trish @ say "No no, I can just tell from your aura!"
    trish @ say "You have that loner vibe. But perhaps you don't want to be alone forever?"
    trish @ say "Oop, sorry! I don't wanna keep you! Time is of the essence after all!"
    trish @ say "I'm sure we'll see each other again! Farewell!"
    
    hide trish with dissolve
    
    n "That was strange. What a weirdo."
    
    if autumnBreakOver == True:
        jump ch4Finale
    else:
        jump midweekAutumnBreak
    
    
    #trish @ say "Let's see... what else?"
    #
    #n "Trish waves her hands around your head. She seems to be concentrating hard."
    #
    #trish @ say "There sure are a lot of paths ahead of you! Let's see, maybe some of the routes you've taken already will give me some context..."
    #trish @ say "Oh my, you're quite popular! I see, I see... Yup, that checks out."
    #
    #if fuckedClaireEarly == True or fuckedRoriEarly == True:
    #    trish @ say "You've done *something*... with *someone*... that perhaps wasn't the right time to do it?"
    #    trish @ say "You may have wanted it, but I sense some guilt and commitment issues."
    #    trish @ say "Not a big deal though, I'm sure those can be worked out!"
    #    
    #if avaPoints > 4:
    #    trish @ say "Ooh I sense some competition! There's something you want but someone standing in your way."
    #    trish @ say "That's always a tricky situation! Especially if you don't want to let anyone go."
    #
    #if invitedToEllensHouse == True:
    #    trish @ say "Are your desires somewhat... unconventional? Are you a bit concerned about the ramifications of *that*?"
    #    trish @ say "People could lose their jobs because of you. But maybe that's okay?"
    #    
    #if historyCheated == True or claireFrenchCheat1 == True or gaveCinRoll == True or ch4EllenSnack == True:
    #    trish @ say "I guess you're not above bending the rules to get what you want... What a rebel!"
    #else:
    #    trish @ say "You tend to play by the rules, which is admirable! Will it always get you where you wanna go?"
    #    
    #if spicyVictory == True:
    #    trish @ say "You seem to work hard for the things you truly want. You don't always have to go that far though!"
    #else:
    #    trish @ say "You lost something recently and you'll never live it down, but it's not over yet!"
    #
    #if clairePoints > 5:
    #    trish @ say "OwO there's someone you've been spending a lot of time with! I wonder where that will go~"
    #else:
    #    trish @ say "Aww, looks like there's someone who likes you but you don't quite like them back."
    #
    #
    #n "You feel a tingly sensation in your brain. How could she know about that?"
    #
    #player "Okay I get it, you have some vague notions of a few things I've done this semester. Got any more dollar store magic tricks?"
    #
    #trish @ say "Yup!"
    #trish @ say "Close your eyes and think of someone~"
    #trish @ say "I don't just see the past, aura has a present and a future!"
    #
    #$ trishFortunes = 0
    #
    #menu:
    #    "Go along with it":
    #        player "Okay but don't try and steal my wallet, it's empty."
    #
    #        n "You're not sure why, but you feel like this possum might be onto something. Can she really read your aura just like that?"
    #        
    #        trish @ say "Are you thinking of someone? Don't tell me who, just think."
    #        
    #        n "Who are you thinking of?"
    #        
    #        jump thinkingCharacter
    #    "Refuse":
    #        player "Yeah nah, I'm not looking for a fortune telling. I'll figure things out on my own."
    #    
    #        trish @ say "I had a feeling you'd say that. Just wanted to give the offer!"
    #        trish @ say "You seemed kinda lonely so I wanted to talk to you because I'm a loner too!"
    #        trish @ say "I'm not sure why but people usually seem repulsed by me."
    #        
    #        player "Maybe it's the smell?"
    #        
    #        trish @ say "Yeah maybe! I think everyone can smell auras. Y'know, like subconsciously. And their subcon tells them to stay away from me."
    #        trish @ say "And when I bumped into you I read your aura and could tell you were a little different too."
    #        
    #        player "That's probably just the autism."
    #        
    #        trish @ say "Yummmmm autistic aura~~~"
    #        
    #        player "Okay what the heck even is an aura?"
    #        
    #        trish @ say "It's kinda hard to define. It's a metaphysical property all sentient beings possess that influences your connections and pathways in life."
    #        trish @ say "I believe it's an evolved social mechanism."
    #        
    #        player "Sounds like something a schizophrenic would come up with."
    #        player "Tell me more."
    #        
    #        trish @ say "Ohmygosh okay! *huff huff* Sorry I'm just getting really excited, not many people care to hear about my aura theories!"
    #        trish @ say "In fact, you're the first person I've talked to for this long at Harmonia!"
    #        trish @ say "Though I did kinda have to knock you out for this to happen."
    #        
    #        player "I forgive you."
    #        player "So what do you think my aura says about me?"
    #        
    #        trish @ say "I suspect you have an aura that repels most people but allows a few select ones through."
    #        trish @ say "You're like a black coffee! Bitter tasting and intolerable for most unless you dress it up with cream and sugar, but some people really prefer the bitterness!"
    #        
    #        player "I can be pretty bitter."
    #        player "So auras are like inherent personal biases we have towards types of people?"
    #        
    #        trish @ say "Yisssss!!!"
    #        trish @ say "Now you're getting it!"
    #        trish @ say "You might get along with another bitter aura because you're the same, or you might get along with a creamy aura because you pair well together!"
    #        trish @ say "But oftentimes the requirements are highly specific. You need a certain type of additive to go with a certain roast."
    #        
    #        player "That just sounds like a measure of how well people get along based on their personality."
    #        
    #        trish @ say "It does! But it's deeper than that."
    #        trish @ say "Now consider that someone doesn't have to taste a coffee to tell it's bitter. It's already in the air. They can smell it."
    #        trish @ say "They can smell your aura too. Not literally, it's just a metaphor."
    #        trish @ say "Your aura permeates into all aspects of your existence. Through walls, space, time, information systems like internets, possibly even across people you encounter..."
    #        trish @ say "The point is, someone can read your aura without ever knowing your personality."
    #        trish @ say "In fact your personality, or the one you present to others, doesn't have to match your aura!"
    #        trish @ say "You can have a sour aura and be a sweet person."
    #        
    #        player "That's... huh. So how are auras consciously perceived?"
    #        
    #        trish @ say "They're not!"
    #        trish @ say "At least not normally."
    #        trish @ say "I'm training to be proficient in reading auras but I still get them wrong all the time. I may even be completely wrong about you!"
    #        trish @ say "It's an underdeveloped scientific field of study that has been suppressed by governments because it has dangerous implications so I'm like a pioneer in researching this kinda stuff."
    #        
    #        player "Wow and it's totally not made up bullshit?"
    #        
    #        trish @ say "Nope! It's as real as the simulation we're living in!"
    #        trish @ say "That is to say, it's \'canon,\' whatever that means."
    #        
    #        player "And what exactly are the implications of auras being real?"
    #        
    #        trish @ say "It's tied to fate. Everyone has a fate but your aura determines how you reach it. It can even affect the final outcome to some degree!"
    #        trish @ say "It's true! I've seen it before!!!"
    #        trish @ say "I'm so excited to observe and research this phenomenon more! I'm collecting all my notes and working on a paper to publish once I have sufficient evidence."
    #        
    #        player "So it's all unproven theory as of now?"
    #        
    #        trish @ say "*Huff huff* sort of? Metaphysical interactions are kinda hard to prove real. It's like a black hole of information that has to be deduced."
    #        #trish @ say "I'm getting a *strong* sense that your aura will be crucial for my research so I'm gonna start stalking you, k? Hope you don't mind!"
    #        
    #        trish @ say "I'm sorry I took up so much of your time, I was just excited to talk about auras with someone who would listen."
    #        
    #        player "It's fine, it was really interesting to hear about!"
    #        
    #        trish @ say "Hehe I'm glad! I have a feeling this won't be the last time we meet"
    #        #trish @ say "Hehe I'm glad! I'll let you go for now, but I'll be keeping my eye on you."
    #        
    #        player "Yeah sure, see you around."
    #        
    #        n "What a weirdo."
    #        
    #        if autumnBreakOver == True:
    #            jump ch4Finale
    #        else:
    #            jump midweekAutumnBreak
#    
#
#label thinkingCharacter:
#    menu:
#        "Claire":
#            $ clairePoints += 1
#            
#            player "Yeah I'm thinking of someone."
#            
#            trish @ say "Ok mhm yeah I got you..."
#            
#            trish @ say "This might sound obvious but I can tell she's suuuper into you! Like she would *die* for you."
#            trish @ say "I can't believe you aren't together yet! What's the holdup?"
#            
#            if clairePoints > 4:
#                player "I dunno, things just keep getting in the way I guess."
#                
#                trish @ say "Well I think you'll have your chance soon!"
#            else:
#                player "That's the problem, I don't like her as much as she likes me."
#                
#                trish @ say "Mhhhh yeah that could be a problem. Why don't you give her a chance!"
#                
#                player "Hmm, not sure I want to."
#            
#        "Ava":
#            $ avaPoints += 1
#            player "Yeah I'm thinking of someone."
#            
#            if avaCucked == True:
#                trish @ say "I hate to break it to ya but I think you botched this one."
#                
#                player "What? What did I do?"
#                
#                trish @ say ""
#            elif avaPoints < 4:
#                trish @ say "I hope you're not too into this one, 'cause she might be going towards someone else!"
#                
#                player "I kinda figured that was the case."
#            
#            else:
#                trish @ say "Huh, this one is as into you as that other one! Seems she has a backup plan but you're plan A!"
#                
#                player "Yay! I believe you because it's what I want to hear!"
#        
#        "Rori":
#            $ roriPoints += 1
#            
#            player "Yeah I'm thinking of someone."
#            
#            trish @ say "Gayyyyyyy!"
#            trish @ say "Ksksksksks just kidding! Unless..?"
#            
#            if fuckedRoriEarly:
#                trish @ say "Oh wow that's super gay..!"
#                
#                player "Hey stop, go back!"
#                
#                trish @ say "Sorry, sorry! I'll just ignore that thing I just saw in your memories."
#                trish @ say "Really though he seems sweet, and if you like him that much you should let him know!"
#            else:
#                trish @ say "Aww, what a sweetie! I can't tell how much he likes you but you two would definitely make a great couple!"
#        
#        "Ms. Ellen":
#            $ ellenPoints += 1
#            
#            player "Yeah I'm thinking of someone."
#        
#            trish @ say "There's not much there at the moment buuuuut..."
#            
#            if ellenPoints > 3:
#                trish @ say "She definitely sees something in you~"
#            else:
#                trish @ say "That could totally change."
#        "Rose":
#            $ rosePoints += 1
#            player "Yeah I'm thinking of someone."
#            
#            trish @ say "Ooh that's one mean bitch! What is it that you see in her?"
#            trish @ say "Ah, I should have known."
#            
#            if rosePoints > 3:
#                trish @ say "The good news is you're not *entirely* on her bad side!"
#                
#            else:
#                trish @ say "Yeah I don't think she's ever gonna warm up to you, sorry."
#            
#        "Mishka":
#            $ mishkaPoints += 1
#            
#            player "Yeah I'm thinking of someone."
#            
#            if mishkaPoints > 2:
#                trish @ say "She might be the one."
#                
#                player "The one?"
#                player "What do you mean \"might be?\""
#                
#                trish @ say "I'm not a fortune teller, just an aura sniffer!"
#                trish @ say "All I can say is out of all the outcomes, that one might be the best."
#            else:
#                trish @ say "Cute! Do I need to say anything else?"
#                
#                player "I was kind of expecting a fortune."
#                
#                trish @ say "I'm not a fortune teller, just an aura sniffer!"
#                trish @ say "All I can sniff out is that you two would get along well."
#        
#        "Someone else":
#            jump thinkingCharacterAlt
#    
#label thinkingCharacterAlt:
#    menu:
#        "Rory":
#            $ roryPoints += 1
#            
#            player "Yeah I'm thinking of someone."
#            
#            trish @ say "Verrrry interesting choice..."
#            trish @ say "You're wanting to know if she'd be into you?"
#            trish @ say "Well yes and no. I won't say any more."
#        
#        "Gunner":
#            $ gunnerPoints += 1
#            
#            player "Yeah I'm thinking of someone."
#            
#            trish @ say "Yup, you two are gonna end up together. 100 percent."
#            trish @ say "I'm just messing with ya! That doesn't happen in any of his nine lives."
#        "Trish":
#            player "Yeah I'm thinking of someone."
#            
#            trish @ say "Oh my gosh, I'm so flattered!"
#            
#            player "Wait, you can actually tell I'm thinking of you?"
#            
#            trish @ say "I can tell a lot of things~"
#            trish @ say "That yummy aura is telling me we'll be seeing each other again~"
#            trish @ say "I for one am excited!"
#            
#            player "I can't tell if I should be or not."
#        #"Dean Kaczynski":
#            #player "Yeah I'm thinking of someone."
#            
#            #trish @ say "..."
#            #trish @ say "Well... hm, how do I put this?"
#            #trish @ say ""
#        "???":
#            player "Yeah I'm thinking of someone..? Wait, am I? Who the fuck is that?"
#            
#            trish @ say "Who indeed? I'm not sure how to interpret this one."
#            trish @ say "I think you'd like her though."
#            
#            player "Does she like me?"
#            
#            trish @ say "Yes, but not in a way you'd like."
#            
#            player "Aww."
#            
#        "Someone else":
#            jump thinkingCharacter
#            
#label afterTrishFortune:
#    $ trishFortunes += 1
#    
#    if trishFortunes < 2:
#        trish @ say "Let's do this one more time. Choose carefully!"
#        trish @ say "You ready?"
#        
#        jump thinkingCharacter
#        
#    n "You open your eyes, dizzy, as if someone's been digging around your brain."
#    
#    trish @ say "Believe me now? That aura you've got is just so delicious, I couldn't help myself!"
#    
#    player "You were kinda vague but... also spot on? Just who are you?"
#    
#    trish @ say "I'm just a derpy possum! There's nothin' real special about me but I done a bunch of travelin' and got to see a lot of things."
#    trish @ say "And eventually I learned how to see through people and taste their auras!"
#    trish @ say "I won't spoil the fun you've got in store. There's lots of options still but I have a feeling you'll go a certain way. Just sit back and enjoy it all playing out!"
#    
#    player "I guess that's all I can really do."
#    
#    trish @ say "That's the spirit! I'll be keeping an eye out for you. It was really nice meeting my future-"
#    trish @ say "Woops, I mean a new friend!"
#    
#    player "Cool, yeah. See you around."
#    
#    n "What a weirdo."
#    
#    if autumnBreakOver == True:
#        jump ch4Finale
#    else:
#        jump midweekAutumnBreak
#
#    
    
label midweekAutumnBreak:
    scene bg codadorm autumn day with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box:
        ypos 0

    n "You find yourself without much to do at the moment halfway into your autumn break. You really underestimated how much classes give you something to do with your time."
    n "That and half your friends are away."
    n "Maybe now's a good time to do that extra credit assignment for history?"
    
    menu:
        n "{cps=0}Maybe now's a good time to do that extra credit assignment for history?{/cps}"
        "Yah":
            $ historySkill += 2
            $ didHistoryExtraCreditCh4 = True
            
            #n "Getting work done during down time now lets you slack off later. Sounds like a win win to you."
            n "This should be a fun little project, looking into what the government doesn't want you to know."
            
            scene bg library with fade
            
            play music "audio/music/vylet - Hold on before i forget.ogg" fadein .4
            
            show box with Dissolve(.2):
                ypos 0
            
            n "The library is dead silent, more so than usual. You'd think it was closed if the lights weren't on."
            n "You begin to peruse the shelves. If you were a book containing forbidden knowledge, where would you be?"
            n "After turning a corner, you trip over a stack of books haphazardly left in the aisle."
            
            rose @ say "Grrr! Watch where you're going!"
            
            n "You look down to find an angry raccoon looking up at you."
            
            show rose skirt furiouspose at center with dissolve:
                ypos y_rose
            
            n "Oh boy here we go again."
            
            menu:
                n "{cps=0}Oh boy here we go again.{/cps}"
                "Sorry":
                    player "Sorry, didn't mean to knock over your book fortress."
                    
                    show rose skirt armscrossed dismissive
                    
                    rose @ say "Whatever. Go away."
                    
                    n "She busies herself reconstructing the stack. It quickly ends up taller than she is."
                    
                    player "Want me to help?"
                    
                    show rose handonhip shy
                    
                    rose @ say "No."
                    
                    player "Fine, I'll just pester you instead. You here working on the extra credit for Rothbauer?"
                    
                    show rose skirt handonhip annoyed
                    
                    rose @ say "*Sigh*"
                    rose @ say "That's what I *was* doing before you interrupted."
                    
                    player "He's gonna have to invent a grade higher than an A for you."
                    
                    show rose skirt handonhip smirk
                    
                    rose @ say "Perfection is the lowest standard."
                    
                    n "You can sense a hint of pride in her voice."
                    
                    player "Cool, find anything interesting?"
                    
                    show rose skirt handonhip shy
                    
                    rose @ say "Yes but it's way beyond your comprehension."
                    
                    player "Got anything my tiny human brain *could* comprehend?"
                    
                    if (rosePoints + historySkill) > 8:
                        rose @ say "Hmm."
                        
                        n "She slips a book out from the stack and tosses it to you."
                        
                        show rose skirt handonhip smug
                        
                        rose @ say "Try this. It's baby's first redpill. Perfect for someone like you."
                        
                        n "You look down and read the title."
                        n "\"Human Society and Its Future\""
                        
                        player "Very funny. Too bad none of this came true."
                        
                        show rose skirt handonhip shy
                        
                        rose @ say "We narrowly avoided it. All it took was two mass extinction events but it was worth the cost."
                        
                        player "You know, your hatred for humanity is starting to grow on me. It's actually kinda cute."
                        
                        show rose skirt fistsclenched angry
                        
                        rose @ say "There's nothing cute about wanting you dead!"
                        
                        player "I dunno, yandere is pretty hot."
                        
                        show rose skirt armscrossed dismissive
                        
                        rose @ say "If this is a reverse psychological trick to get me to stop hating on your entire species, it's not gonna work."
                        
                        player "Good, I wouldn't have it any other way. You're perfect the way you are."
                        
                        show rose skirt flatteredpose
                        
                        rose @ say "Well I..."
                        
                        show rose skirt fistsclenched angry
                        
                        rose @ say "I know I am! I don't need your affirmation!"
                        
                        show rose skirt furiouspose
                        
                        rose @ say "Here, take this and go learn something!"
                        
                        n "Rose shoves a book into your hands. It's titled \"The Human History Iceberg.\""
                        
                        player "Ooh, this looks like a good one! Thanks~"
                        
                        show rose skirt armscrossed unsure
                        
                        rose @ say "If you don't get an A on the assignment, I'll be more disappointed in you than usual."
                        
                        hide rose with dissolve
                        
                        n "Clutching the book, you scuttle on out of there to write your report. You can barely get a quarter of the way down the iceberg before the required foreknowledge goes beyond your understanding."
                        
                        player "What kind of crack was the author on? The hell do you mean the moon landing was a cover up for exiling humans off the planet?"
                        #n "For that matter, how did JFK personally do 9/11?"
                        #n "The author states he hired a hit on himself to produce a rare chemical in his brain at the moment of death to astral project into the pilots' heads but fails to explain the motivation to do such a thing."
                        
                        n "These conspiracies seem a little out there, but there might be some truth in a few of them."
                        n "Rose would know more."
                        n "You find her in a more extravagant book fort than before."
                        
                        player "Wow, someone's been busy."
                        
                        show rose skirt armscrossed shy at center with dissolve:
                            ypos y_rose
                        
                        rose @ say "Go away human scum. I'm building a kingdom for the master species."
                        
                        player "Riiight. Anyway I had a question about this conspiracy."
                        
                        show rose skirt armscrossed dismissive
                        
                        rose @ say "If it has to do with humans being awful and ruining everything for everyone, it's not a conspiracy it's just a fact of their nature."
                        
                        player "Yeah okay it says that modern raccoons are the descendants of human and arcoon hybrids. Is that true?"
                        
                        show rose skirt armscrossed shy
                        
                        n "Rose goes silent for a moment."
                        
                        show rose skirt armscrossed unsure
                        
                        rose @ say "...There's evidence to suggest it is, yes."
                        
                        player "So that makes you...?"
                        
                        show rose skirt fistsclenched angry
                        
                        rose @ say "Damn you humans, you ruin everything you touch!"
                        
                        show rose skirt furiouspose
                        
                        rose @ say "Arcoonians should have killed you all on sight. Kept the bloodline pure..."
                        
                        player "..."
                        
                        n "Things are starting to make a little more sense now. Her hatred for humans seems a bit less irrational now."
                        
                        show rose skirt handonhip annoyed
                        
                        rose @ say "*IF* that conspiracy is even slightly true, the modern raccoon is still the best living species IN SPITE of any dormant human DNA presence!"
                        
                        menu:
                            rose "{cps=0}*IF* that conspiracy is even slightly true, the modern raccoon is still the best living species IN SPITE of any dormant human DNA presence!{/cps}"
                            "It's just a dumb theory":
                                $ rosePoints += 1
                                
                                player "Honestly the theory sounds dumb as fuck and doesn't make any sense."
                                player "Humans can't even hybridize with raccoons. There's not enough matching DNA so I doubt it would even work for a pureblood arcoon."
                                
                                show rose skirt handonhip dismissive
                                
                                rose @ say "It's based on some DNA records and computer models showing it could *maybe* theoretically happen. We don't have the whole picture."
                                rose @ say "Scientists are working to reconstruct arcoon DNA in full. Until then we won't know for sure what happened."
                                rose @ say "Either way, they died out and the modern raccoon is adapted to the modern world. They probably used advanced technology to alter their DNA for how gay and retarded the world was becoming."
                                
                                player "Right. Then they'd destroy said technology to prevent others from getting their filthy hands on it."
                                
                                show rose skirt handonhip annoyed
                                
                                rose @ say "Exactly! That's the level they operated on! So advanced even their ancient scrapped designs are science fiction to us!"
                                
                                show rose skirt furiouspose
                                
                                rose @ say "Once civilization stabilizes from the disease that was humanity, we'll bring back glorious arcoonian culture!"
                                
                                show rose skirt armscrossed furious
                                
                                rose @ say "A new wave of philosophers! Independence! Ferocity! Individual freedoms! Academics will truly be great again!"
                        
                                player "Make academics great again? What's wrong with our education?"
                                
                                show rose skirt armscrossed annoyed
                                
                                rose @ say "It's been tainted by communism. Only humans could make a mistake so big it ruins intellectual discourse for multiple future generations."
                                
                                player "You got me there. Sorry for inventing communism."
                                
                                show rose skirt armscrossed smirk
                                
                                rose @ say "Admitting you're the problem is the first step in recovery."
                                
                                show rose skirt armscrossed shy
                                
                                player "I think you got that slightly wrong but who am I to argue?"
                                player "Thanks for the help with the extra credit though. See you in class next week."
                                
                                show rose skirt armscrossed dismissive
                                
                                rose @ say "Still hoping you get struck by lightning, but yeah see you in class I guess."
                                
                                hide rose with dissolve
                                
                                n "Wow, that's a massive improvement! You think she's starting to warm up to you!"
                            "So you're coping?":
                                $ rosePoints -= 2
                            
                                player "I sorta get it now. All that cope about hating humans because you're partly one."
                                
                                show rose skirt furiouspose
                                
                                rose @ say "Shut UP!!!"
                                rose @ say "You and I have NOTHING in common, least of all on a genetic level!"
                                rose @ say "You've barely evolved past being a feral ape for eons, whereas raccoons are the pinnacle of natural selection!"
                                
                                player "LMAO your ancestors fucked human men."
                                player "Maybe arcoonians weren't that great until they got a little human DNA in them?"
                                
                                show rose skirt fistsclenched angry
                                
                                rose @ say "How dare you even suggest such a thing!"
                                rose @ say "I can't wait until your kind is dead and buried for good."
                                
                                player "Hey at least my genetics will live on inside you and the rest of the raccoons!"
                                
                                rose @ say "Damn you humans... You can burn in hell and if you don't leave me alone I'll send you straight there!"
                                
                                show rose skirt fistsclenched angry knife
                                
                                n "Oh shit she might be serious."
                                #n "Oh shit she might be serious. She's reaching for her hip, her hand on an imprint beneath her clothes that looks suspiciously like a handgun."
                                n "You take a step back and hold your hands up in the air."
                                
                                player "Hey, I was just playing. No need to take me seriously. I was just on my way out."
                                
                                #n "You book it out of the library as fast as you can before she decides to use you as target practice."
                                n "You book it out of the library as fast as you can."
                                
                                hide rose with dissolve
                                
                                player "SEEYOUINCLASSNEXTWEEK!!!"
                                
                                
                        
                        
                        
                    else:
                        rose @ say "I'm not doing your research for you."
                        
                        player "Okay well it looks like you've hoarded all the good books for yourself so lemme just... yoink!"
                        
                        n "You grab a random book off the ground. It's titled \"The Human History Iceberg\""
                        
                        show rose skirt fistsclenched angry
                        
                        rose @ say "Hey!"
                        
                        show rose skirt armscrossed dismissive
                        
                        rose @ say "Oh whatever, take it and leave."
                        
                        hide rose with dissolve
                        
                        n "Clutching the book, you scuttle on out of there to write your report. You can barely get a quarter of the way down the iceberg before the required foreknowledge goes beyond your understanding."
                        
                        player "What kind of crack was the author on? The hell do you mean the moon landing was a cover up for exiling humans off the planet?"
                        #n "For that matter, how did JFK personally do 9/11?"
                        #n "The author states he hired a hit on himself to produce a rare chemical in his brain at the moment of death to astral project into the pilots' heads but fails to explain the motivation to do such a thing."
                        
                        n "These conspiracies seem a little out there, but there might be some truth in a few of them."
                        n "Rose would know more."
                        n "You find her in a more extravagant book fort than before."
                        
                        player "Wow, someone's been busy."
                        
                        show rose skirt armscrossed shy at center with dissolve:
                            ypos y_rose
                        
                        rose @ say "Go away human scum. I'm building a kingdom for the master species."
                        
                        player "Riiight. Anyway I had a question about this conspiracy."
                        
                        show rose skirt armscrossed dismissive
                        
                        rose @ say "If it has to do with humans being awful and ruining everything for everyone, it's not a conspiracy it's just a fact of their nature."
                        
                        player "Yeah okay it says that modern raccoons are the descendants of human and arcoon hybrids. Is that true?"
                        
                        show rose skirt fistsclenched angry
                        
                        rose @ say "What?!"
                        
                        n "Rose bursts from her fort, knocking over a support wall and causing to all come crashing down."
                        n "She snatches the book from your hands and scours over the page you had it flipped to."
                        
                        show rose armscrossed annoyed
                        
                        rose @ say "Utter fanfiction."
                        rose @ say "The modern raccoon is a result of a carefully crafted eugenics program to produce the perfect organism."
                        rose @ say "Highly advanced genetic modification was involved but the technology was destroyed so the plebs couldn't get their paws on it."
                        
                        player "Oh. I just thought it was odd that it was the only part of the book that provided evidence. The whole DNA sequence is laid out in a table and seemed pretty legit."
                        player "I guess it's just fake science though, huh?"
                        
                        show rose armscrossed dismissive
                        
                        rose @ say "Yeah. You're better off researching something more worthwhile."
                        
                        show rose armscrossed shy
                        
                        rose @ say "Like... this book has a good explanation!"
                        
                        n "She holds up a copy of \"Mesozoic Man: Escaping Extinction.\""
                        
                        rose @ say "That ought to get you up to speed on how humans screwed the dinosaurs -- *ahem* FIGURATIVELY! -- then locked them out of the bunkers after causing the apocalypse."
                        
                        player "Oh neat! Do you actually believe humans are that old? Or is it just more \"humans bad\" propaganda?"
                        
                        rose @ say "It's a complex history, but yes there's ample evidence that the civilization before ours was destroyed by humans."
                        
                        show rose armscrossed dismissive
                        
                        rose @ say "Now whether your kind were alien invaders or demonic spawn remains to be decisively concluded. Personally I think it's both."
                        
                        player "Thanks for clearing that up. I'll get to work finishing my paper now. Hope yours is going well too!"
                        
                        show rose armscrossed annoyed
                        
                        rose @ say "Don't worry about me. Mr. Rothbauer is gonna learn a few new things from my paper!"
                        
                        player "Heh I'm sure he will. See you in class!"
                        
                        hide rose with dissolve
                        
                        n "You return to your desk and bang out the rest of your paper."
                        n "On your way home you pass by Rose again, who has a whole stack of pages she's written on her conspiracy of choice. She probably has a novel's worth of material already in her head."
                        
                        
                        #if you offered to help her with the mansion situation, offer to take a pic of you and her studying together to send to her grandpa
                        
                        
                    
                    
                    jump autumnBreakLockIn
                    
                    
                "Fuck you":
                    $ rosePoints -= 1
                    $ rudeToRose += 1
                    
                    player "Fuck you and your stupid book fort!"
                    
                    n "You kick the remainder of the stack and watch the books spill all over the floor."
                    
                    #if rosePoints < 2:
                        #rose @ say "Listen you human****r, if you don't clean up this mess you made, you're done for!"
                    #else:
                    
                    show rose skirt armscrossed annoyed
                    
                    rose @ say "Listen you humanoid, if you don't clean up this mess you made, you're done for!"
                    
                    menu:
                        rose "{cps=0}Listen you humanoid, if you don't clean up this mess you made, you're done for!{/cps}"
                        "Nope":
                            $ roseWarning = True
                            $ rosePoints -= 1
                            $ historySkill += 1
                            
                            player "Nope. You've done nothing but antagonize me so this is the least you deserve."
                            player "Have fun organizing those again. I know you must have ordered them in some extremely autistic way that took all day."
                            
                            show rose fistsclenched angry
                            
                            rose @ say "Ugh just leave me alone!"
                            rose @ say "I'm seriously this close to putting you down. Killing an endangered species may be a felony but I've got connections to escape jail time."
                            rose @ say "Consider this a warning to stay out of my way from now on."
                            
                            player "Whatever. I've got more important things to do than waste time on trash like you."
                            
                            hide rose with dissolve
                            
                            n "You kick aside her books and march through the aisle."
                            n "Eventually you find a book related to your search and produce a half-assed paper."
                            n "You would have put in more effort but that raccoon makes you seethe so much, you can't stop thinking about your mutual hatred for each other."
                            
                            jump autumnBreakLockIn
                        "Okay fine, sorry":
                            $ historySkill += 1
                            
                            n "That may have been a bit too far, even for all the trouble she's given you."
                            
                            player "Alright fine, that was a bit much. Sorry I guess."
                            
                            n "You drop down and begin gathering the books and piling them up."
                            
                            show rose skirt armscrossed annoyed
                            
                            rose @ say "What the hell are you doing? Stack them by weight, not cover surface area!"
                            
                            show rose skirt armscrossed dismissive
                            
                            rose @ say "You know what? Don't even bother. You can't get anything right. Just leave."
                            
                            player "Fine, if that's what you really want."
                            
                            hide rose with dissolve
                            
                            n "You stand up and step away. Perhaps it's for the best."
                            n "You take a look back at her and start to feel bad. You sure know how to handle the ladies, don't you?"
                            n "Eventually you find a book related to your search and produce a half-assed paper."
                            n "You would have put in more effort but you're mind is stuck in a loop replaying that Rose encounter and how you could have done better."
                            
                            jump autumnBreakLockIn
                            
                            
                            
                        "Or what, you'll shoot me?":
                            player "Fuck that. What're you gonna do, shoot me?"
                            
                            n "A deranged grin forms on Rose's face."
                            
                            show rose skirt armscrossed smirk
                            
                            rose @ say "Yes actually!"
                            
                            show rose skirt shootinggun
                            
                            n "She quickdraws a pistol from her skirt and takes aim at you."
                            n "*BANG*"
                            
                            stop music fadeout 2.0
                            
                            scene bg black
                            
                            n "The last thing you see is the muzzle flash illuminating the raccoon's face before you crumple to the ground."
                            n "A hole in your heart leaks pint after pint of blood, draining your consciousness."
                            n "Your skin goes cold and your vision fades to black."
                            
                            rose @ say "You get what you fucking deserve."
                            
                            jump ending
                        
                            
                        
            
            
        "Nah":
            n "Yeah no, you're not gonna waste your life away hitting the books. That's not natural."
            n "Your monkey brain tells you what you need is a good old fashioned walk. Some fresh air and sunlight to clear your mind."
            
            scene bg campus autumn day with dissolve
            
            play music "audio/music/vylet - Ordinarily.ogg" fadein .4
            
            show box with Dissolve(.2):
                ypos 0
            
            if metLina == False:
                $ metLina = True
                
                n "It's not long before you come across a stranger who strikes up a conversation."
                
                show lina neutral at center with dissolve:
                    ypos y_lina
                    xzoom -1
                
                lina @ say "Heya! I've seen you around before!"
                
                player "You have?"
                
                lina @ say "Yeah, like just around on campus! You're a student too, aren't you?"
                
                player "Oh, right. I'm afraid I never noticed you."
                
                lina @ say "That's alright. I'm just kinda in the background!"
                
                player "Well it's nice to finally meet you I guess! My name's [name]."
                
                lina @ say "I'm Lina! A pleasure to finally get to meet you as well!"    
                lina @ "You're a human!"
                
                player "And you're a... bird?"
                
                lina @ say "A harpy eagle to be precise. We can see from pretty far away."
                lina @ say "It's always easy to spot you 'cause you're the only human around!"
                
                player "Thanks? I think? You haven't been stalking me, have you?"
                
                lina @ say "Noooo, nothing like that! I just see you talking with that bunny girl and secretary bird all the time."
                
                player "Yeah they're... something haha."
                
                player "So you got left behind too? For autumn break?"
                
                lina @ say "Yeahhhh I didn't wanna fly all the way back home. Besides..."
                
                n "A sinister smirk forms on her beak."
                
                lina @ say "Long breaks like this are the perfect time to conduct panty raids!"
                
                player "Seriously? A buddy of mine had a hard time convincing me that was a real thing."
                
                lina @ say "Oh it's very real~"
                lina @ say "I mean, either that or I've just been breaking in and burglarizing all this time."
                
                if gunnerRaid == True:
                    player "Yeah I ended up joining him and a gay friend a few weeks ago to do a raid. It was pretty fun."
                    
                    lina @ say "OMG for real??? Who's panties did ya nab?"
                    
                    if avaPantsu == True:
                        player "Uhhhh you probably don't know her. The photography bird girl I hang out with."
                        
                        lina @ say "Ooooh her?~ I bet she's got some cute ones~"
                        lina @ say "But I might be biased cause we're both birbs hehe~"
                        
                        player "Yeah they're pretty nice~"
                        
                        lina @ say "Think you could help a bird out in getting a pair herself?"
                        
                        menu:
                            lina "{cps=0}Think you could help a bird out in getting a pair herself?{/cps}"
                            "Visit Ava's dorm with Lina":
                                player "Mmmh alright, I could show you where her dorm is."
                                
                                lina @ say "And be an accomplice to my raid?"
                                
                                player "Eh why not?"
                                
                                lina @ say "Yay! Panty raiding buddy!!!"
                                
                                player "Yeah please don't shout that at the top of your lungs."
                                
                                lina @ say "Heh sorry. Shall we go then?"
                                
                                
                                jump pantyRaidLina1
                            "Stay out of it":
                                player "I'll have no part in helping you with that."
                                
                                lina @ say "A master panty hunter like me doesn't need any help!"
                                lina @ say "I'll amass the biggest collection of stolen panties this university has ever seen!"
                                
                                player "Good luck with that. Have a nice day."
                                
                                n "That's enough talking to the mentally ill for today. You've got better things to do."
                                
                                lina @ say "See ya!"
                                
                                jump celestineMargaretVisit1
                        
                        
                        
                        
                    
                    if clairePantsu == True:
                        player "Uhhh that big bunny girl I hang out with."
                        
                        lina @ say "Ooooh you're into the chunky ones, huh?"
                        lina @ say "Not my cuppa tea but I've got a few like that in my collection~"
                        
                        player "She's roommates with the other bird girl I talk to."
                        
                        lina @ say "The photographer one? I could go for taking a pair from her~"
                        
                        menu:
                            lina "{cps=0}The photographer one? I could go for taking a pair from her~{/cps}"
                            "Visit Ava's dorm with Lina":
                                player "If you want, I could show you where her dorm is."
                                
                                lina @ say "And be an accomplice to my raid?"
                                
                                player "Eh why not?"
                                
                                lina @ say "Yay! Panty raiding buddy!!!"
                                
                                player "Yeah please don't shout that at the top of your lungs."
                                
                                lina @ say "Heh sorry. Shall we go then?"
                                

                                jump pantyRaidLina1
                                
                            "Stay out of it":
                                player "I'll have no part in helping you with that."
                                
                                lina @ say "A master panty hunter like me doesn't need any help!"
                                lina @ say "I'll amass the biggest collection of stolen panties this university has ever seen!"
                                
                                player "Good luck with that. Have a nice day."
                                
                                n "That's enough talking to the mentally ill for today. You've got better things to do."
                        
                                lina @ say "See ya!"
                        
                                jump celestineMargaretVisit1
                        
                        
                    else:
                        player "I didn't end up with any. I was just playing chaperone."
                        
                        lina @ say "Aww, what a shame."
                        lina @ say "You wanna make up for it and come with me tonight?"
                        
                        player "What, let's go rob someone's house tonight?"
                        
                        lina @ say "Just their panties!"
                        
                        menu:
                            lina "{cps=0}Just their panties!{/cps}"
                            "I'm in":
                                player "I'm game. I was kinda nervous the first time but I think I can handle it now."
                                
                                lina @ say "Relax, I'm a pro at this! There's not a chance we'll get caught!"
                                
                                
                                jump pantyRaidLina1
                                
                            "I'm out":
                                player "Count me out. I had enough of it the first time."
                                
                                lina @ say "Alright then, that just leaves more for me~"
                                
                                jump celestineMargaretVisit1
            
                else:
                    player "Is everyone in this university a deranged pervert?"
                        
                    lina @ say "It's just a hobby, okay??"
                    lina @ say "There's no greater joy than finding a jackpot of cute frilly panties and adding to my collection~"
                    
                    player "Man, humans leave anthromorphs to their own devices for like 2 generations and this is what happens."
                    
                    lina @ say "Don't be a stick in the mud! I can show you how fun it really is!"
                    
                    menu:
                        lina "{cps=0}Don't be a stick in the mud! I can show you how fun it really is!{/cps}"
                        "I'm in":
                            player "Eh sure, I'll do it. Somehow it feels more innocent to go on a raid with a girl than with two frat boys."
                            
                            lina @ say "That's the spirit!"
                            
                            jump pantyRaidLina1
                            
                            
                        "I'm out":
                            player "Count me out. I don't need to be on the sexual offenders registry."
                            
                            lina @ say "Alright then, that just leaves more for me~"
                            
                            player "Good luck on your panty quest!"
                            
                            lina @ say "A master underwear thief like me doesn't need luck! It's pure motivation and skill!"
                            
                            player "Haha sure, well show me whatever spoils you find later."
                            
                            lina @ say "I will!"
                    
                            jump celestineMargaretVisit1
            
                
            else:
                n "It's not long before you come across someone you've seen before."
                
                show lina neutral at center with dissolve:
                    ypos y_lina
            
                lina @ say "Hey, it's you again!"
                
                player "Huh? Oh hey, the saxophone bird."
            
                if featherMuncher == True:
                    lina @ say "Give me back the money you stole from me!"
                    
                    player "Sorry, I spent it already."
                    
                    lina @ say "What kind of person steals from a street performer anyway? You bum!"
                    
                    player "Speak for yourself! You were the one extorting everyone for their hard earned cash."
                
                    lina @ say "I did no such thing! Anyone is free to donate or not!"
                    lina @ say "And what's wrong with being a feathermuncher, huh?"
                    
                    player "It's gay."
            
                    lina @ say "Ah, I see. My mistake."
                    lina @ say "Liking girls *is* pretty gay. You don't like girls do you?"
                    
                    player "What? No of course not!"
                    player "Wait a minute..."
                    
                    lina @ say "Hah! Got ya!"
                    lina @ say "See you around, dork. I got a panty raid to get to!"
                    
                    pause .1
                    
                    show lina neutral at offscreenleft with move:
                        ypos y_lina
                    
                    n "Dammit she's flying away before you can get a comeback in!"
                    n "You end up shouting slurs into the wind."
                    n "You're down 2 to 0 against this lesbird."
                    
                    
                    jump celestineMargaretVisit1
                    
                else:
                    lina @ say "I have a name, you know! Did you already forget it?"
                    
                    player "Lina, right? How goes it? Stuck on campus during the break I see."
                    
                    lina @ say "Yeahhh but I'm not complaining! I'm making the most of it in fact!"
                    
                    player "How's that?"
                    
                    n "She gestures for you to lean closer so she can whisper something to you."
                    
                    lina @ say "Have you ever heard of a... panty raid?"
                    
                    player "Oh god not this again. A buddy of mine had a hell of a time convincing me that was a real thing."
                    
                    if gunnerRaid == True:
                        player "I ended up joining him and a gay friend a few weeks ago to do a raid. It was pretty fun."
                    
                        lina @ say "OMG for real??? Who's panties did ya nab?"
                            
                        if avaPantsu == True:
                            player "Uhhhh you probably don't know her. The photography bird girl I hang out with."
                            
                            lina @ say "Ooooh her?~ I bet she's got some cute ones~"
                            lina @ say "But I might be biased cause we're both birbs hehe~"
                            
                            player "Yeah they're pretty nice~"
                            
                            lina @ say "Think you could help a bird out in getting a pair herself?"
                            
                            menu:
                                lina "{cps=0}Think you could help a bird out in getting a pair herself?{/cps}"
                                "Visit Ava's dorm with Lina":
                                    player "Mmmh alright, I could show you where her dorm is."
                                    
                                    lina @ say "And be an accomplice to my raid?"
                                    
                                    player "Eh why not?"
                                    
                                    lina @ say "Yay! Panty raiding buddy!!!"
                                    
                                    player "Yeah please don't shout that at the top of your lungs."
                                    
                                    lina @ say "Heh sorry. Shall we go then?"
                                    
                                    
                                    jump pantyRaidLina1
                                "Stay out of it":
                                    player "I'll have no part in helping you with that."
                                    
                                    lina @ say "A master panty hunter like me doesn't need any help!"
                                    lina @ say "I'll amass the biggest collection of stolen panties this university has ever seen!"
                                    
                                    player "Good luck with that. Have a nice day."
                                    
                                    n "That's enough talking to the mentally ill for today. You've got better things to do."
                                    
                                    lina @ say "See ya!"
                                    
                                    jump celestineMargaretVisit1
                            
                            
                        if clairePantsu == True:
                            player "Uhhh that big bunny girl I hang out with."
                            
                            lina @ say "Ooooh you're into the chunky ones, huh?"
                            lina @ say "Not my cuppa tea but I've got a few like that in my collection~"
                            
                            player "She's roommates with the other bird girl I talk to."
                            
                            lina @ say "The photographer one? I could go for taking a pair from her~"
                            
                            menu:
                                lina "{cps=0}The photographer one? I could go for taking a pair from her~{/cps}"
                                "Visit Ava's dorm with Lina":
                                    player "If you want, I could show you where her dorm is."
                                    
                                    lina @ say "And be an accomplice to my raid?"
                                    
                                    player "Eh why not?"
                                    
                                    lina @ say "Yay! Panty raiding buddy!!!"
                                    
                                    player "Yeah please don't shout that at the top of your lungs."
                                    
                                    lina @ say "Heh sorry. Shall we go then?"
                                    
                                    
                                    
                                    
                                    jump pantyRaidLina1
                                    
                                "Stay out of it":
                                    player "I'll have no part in helping you with that."
                                    
                                    lina @ say "A master panty hunter like me doesn't need any help!"
                                    lina @ say "I'll amass the biggest collection of stolen panties this university has ever seen!"
                                    
                                    player "Good luck with that. Have a nice day."
                                    
                                    n "That's enough talking to the mentally ill for today. You've got better things to do."
                            
                                    lina @ say "See ya!"
                            
                                    jump celestineMargaretVisit1
                            
                            
                        else:
                            player "I didn't end up with any. I was just playing chaperone."
                            
                            lina @ say "Aww, what a shame."
                            lina @ say "You wanna make up for it and come with me tonight?"
                            
                            player "What, let's go rob someone's house tonight?"
                            
                            lina @ say "Just their panties!"
                            
                            menu:
                                lina "{cps=0}Just their panties!{/cps}"
                                "I'm in":
                                    player "I'm game. I was kinda nervous the first time but I think I can handle it now."
                                    
                                    lina @ say "Relax, I'm a pro at this! There's not a chance we'll get caught!"
                                    
                                    
                                    
                                    
                                    
                                    
                                    jump pantyRaidLina1
                                    
                                    
                                "I'm out":
                                    player "Count me out. I had enough of it the first time."
                                    
                                    lina @ say "Alright then, that just leaves more for me~"
                                    
                                    player "Good luck on your panty quest!"
                                    
                                    lina @ say "A master underwear thief like me doesn't need luck! It's pure motivation and skill!"
                                    
                                    player "Haha sure, well show me whatever spoils you find later."
                                    
                                    lina @ say "I will!"
                            
                                    jump celestineMargaretVisit1
                        
                        
                    
                    
                    
                    else:
                        player "Is everyone in this university a deranged pervert?"
                        
                        lina @ say "It's just a hobby, okay??"
                        lina @ say "There's no greater joy than finding a jackpot of cute frilly panties and adding to my collection~"
                        
                        player "Man, humans leave anthromorphs to their own devices for like 2 generations and this is what happens."
                        
                        lina @ say "Don't be a stick in the mud! I can show you how fun it really is!"
                        
                        menu:
                            lina "{cps=0}Don't be a stick in the mud! I can show you how fun it really is!{/cps}"
                            "I'm in":
                                player "Eh sure, I'll do it. Somehow it feels more innocent to go on a raid with a girl than with two frat boys."
                                
                                lina @ say "That's the spirit!"
                                
                                
                                
                                
                                jump pantyRaidLina1
                                
                                
                            "I'm out":
                                player "Count me out. I don't need to be on the sexual offenders registry."
                                
                                lina @ say "Alright then, that just leaves more for me~"
                                
                                player "Good luck on your panty quest!"
                                
                                lina @ say "A master underwear thief like me doesn't need luck! It's pure motivation and skill!"
                                
                                player "Haha sure, well show me whatever spoils you find later."
                                
                                lina @ say "I will!"
                        
                                jump celestineMargaretVisit1
                            
                            
label pantyRaidLina1:
    $ linaPantyRaid = True
    $ clairePantsu = True

    scene bg oldhospital with fade
    
    show box with Dissolve(.2):
        ypos 0

    n "Lina's key fob got you inside Ava and Claire's dorm building and you brought her outside their room."
    
    player "Here it is. Last time I had an easier time getting in but it's locked now."
    
    show lina neutral at center with dissolve:
        ypos y_lina
    
    lina @ say "Not a problem! I've honed my lockpicking skills for moments like these!"
    
    n "Within seconds, Lina gets the door open."
    
    player "Wow, you really are a pro at this."
    
    hide lina with dissolve
    
    show bg avadorm with dissolve
    
    play music "audio/music/vylet - explorer.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Stepping inside the poorly lit room, you hurry to the clothes drawers."
    
    player "Ah, this one's Claire's."
    player "Huh? There's a note here addressed to... me?"
    
    n "You flip it open and read through it. Not even halfway through it has you blushing."
    
    show lina neutral at center with dissolve:
        ypos y_lina
    
    lina @ say "Well? What does it say!"
    
    player "Nothing, nothing. It's very private. Hey, stop!"
                    
    n "Lina swipes the note from your hand and flutters up to the top bunk to read it."
    
    lina @ say "Wow. This Claire lady is *really* into you."
    
    player "Tell me about it."
    
    lina @ say "Sounds like that bunny's panties are reserved for you!"
    
    menu:
        lina "{cps=0}Sounds like that bunny's panties are reserved for you!{/cps}"
        "Take them":
            $ clairePantsuLina = True
            
            player "Damn right."
            
            if clairePantsu == True:
                $ clairePantsu = True
                
                n "Now you have two pairs of big bunny panties. You don't even know what to do with one."
                
            else:
                n "You bunch them up and stuff them in your pocket."
                n "You're gonna have a hard time explaining this if you get stopped and searched."
                
            n "Let's see what Ava has to offer..."
                
        "Leave them":
            player "I came here for Ava's knickers."
            
            n "You close Claire's drawer and open the one beneath it."
            
        
    player "Hey!"
    
    n "Lina swooped down and snatched the only set of undergarments Ava left behind."
    
    player "Those were for me, not you!"
    
    lina @ say "Finders keepers~"
    lina @ say "Hey, she's the same size as me!"
        
    if avaPoints > 4:
        player "I swear if I have to compete with ANOTHER suitor for her I'm gonna start taking out the competition. And I don't mean like on a date."

        lina @ say "I dunno, we might hit it off!"
        
        player "I'm pretty sure she's straight."
        
        lina @ say "So is spaghetti until it gets hot!"
        
        player "Come on, I'll trade you Claire's panties for those."
        
        lina @ say "Nahhh, these are just what I came for~"
        
    if avaPantsu == True:
        player "Whatever, I already have one of Ava's."
                
    player "I think we're done here."
    
    lina @ say "Mhm! I told ya no panties are safe from me!"
    
    player "Glad I don't have to worry about you stealing the underwear off my ass."
    
    lina @ say "Yeah no, boys are gross lol"
    lina @ say "But thanks for joining me on this raid! Feel free to hit me up later if you wanna go on another raid!"
    
    player "If I ever find the time, sure."
        
    if clairePantsuLina == True:
        n "You leave the dorm and part ways, wondering what to do with your prize. And how Claire will react when she finds out what you've done."
    else:
        n "You leave the dorm and part ways, disappointed you couldn't get Ava's panties. They seem to be in high demand."
        
    jump autumnBreakLockIn
        
label celestineMargaretVisit1:
    scene bg town summer day with dissolve
    
    $ ellenPoints += 1
    
    play music "audio/music/vylet - there.ogg" fadein .4
    #play music "audio/music/vylet - earnest (feat. Sylver Stripe & Namii).ogg" fadein .4
    
    show box:
        ypos 0

    n "Continuing your walk, you end up in the town proper. The streets are empty. Not even traffic blocks the roadways."
    n "You guess college towns just get put on pause when students are away."
    n "But for the actual residents, it must be a break from all the hustle and bustle they bring."
    n "Looks like two of them are out having a pleasant day together right now."
    
    show margaret casual neutral at center with dissolve:
        ypos y_margaret
        xzoom -1
        xoffset -400
    show celestine neutral at center with dissolve:
        ypos y_celestine
        xoffset 400
        
    show margaret casual shocked
    
    margaret @ say "[name]? Fancy happening upon you this far out from the campus!"
    
    celestine @ say "Bonjour, [name]!"
    
    show margaret casual neutral
    
    player "Good afternoon! It's kinda weird seeing you two just hanging out but I guess even professors have friends."
    
    show margaret casual melancholy
    
    margaret @ say "Yup! We're just doing some winter clothes shopping while we can!"
    
    celestine @ say "Before those pesky students can pick the shelves clean!"
    
    show margaret casual neutral
    
    player "Wow, now I see how you view your students haha"
    
    celestine @ say "Don't get me wrong, I love my students, but nobody told me Harmonia was such a wild town!"
    
    n "Mrs. Celestine looks around and whispers something to you."
    
    celestine @ say "I'm *constantly* having to buy new undergarments because of a certain local \"tradition\" of stealing them!"
    
    show margaret casual melancholy
    
    margaret @ say "I'll admit it gets on my nerves. But boys will be boys."
    
    if margaretPantsu == True:
        show margaret casual frown
        
        n "Miss Ellen glares at you, out of Mrs. Celestine's sight."
        
        ###alt where she winks at you if you have high ellenpoints
        
        player "Haha y-yeah who would do such a thing?"
        
        n "Glare all you want, you're not getting them back."
    
    else:
        player "Riiiiight, boys."
        
    show margaret casual happy
        
    margaret @ say "Anyway, it was nice seeing you outside of the classroom!"
    
    show margaret casual neutral
    
    celestine @ say "Agreed! Hopefully you have something to keep yourself busy if you're stuck here during the break."
    
    player "I'm managing to get by. Eager for three quarters of my main friend group to get back from their vacation though."
    
    celestine @ say "We'd invite you to hang out with us but we were just about to go into..."
    
    n "She points at the women's lingerie store. Obviously wouldn't be a good look for two female professors to bring a male student along with them in there."
    
    player "Haha of course, I get it. You two have a nice day! I'll see you in class next week!"
    
    celestine @ say "À bientôt!"
    
    margaret @ say "I'll give you a heads up and say there'll be a quiz first thing on Tuesday!"
    
    player "Thanks!"
    
    hide margaret
    hide celestine
    with dissolve
    
    n "As you pass by each other, you glance into the window display of the store they're about to enter."
    n "You can't help but imagine them in the outfits you see."
    
    

label autumnBreakLockIn:
    stop music fadeout 2.0
    
    scene bg codadorm autumn day rain with fade
    
    #play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box with Dissolve(.2):
        ypos 0
    
    n "As your autumn break is coming to a close, you decide to take a day to make sure you're caught up on studies."
    n "A nasty storm brews outside as you open the university's coursework app on your laptop."
    n "Gusts of wind make the building creak and you swear the walls are tilting a little."
    n "Rain starts to pour down and it's not long before regular lightning strikes flash through your window."
    n "With a crash of thunder, the building shakes and the lights flicker."
    
    scene bg codadorm autumn day rain nopower
    
    show box:
        ypos 0
    
    n "Your internet connection shuts off and the room goes dark."
    n "The only source of illumination is the dull blue light emitted by your laptop screen that soon dies as well."
    
    rose @ say "Are you fucking kidding me?!"
    
    n "Sounds like your neighbor is enjoying the outage as much as you are."
    n "You hear some thuds like she's kicking the wall in the hallway."
    
    scene bg schoolhallways autumn night with fade
    
    play music "audio/music/vylet - blockhead.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    player "Hey, what the hell are you doing out here? Quit sperging out, it's just a power outage."
    
    show rose athletic furious at center with dissolve:
        ypos y_rose
    
    n "Rose is outside her door, clawing at it. She must have just got back from the gym, judging by her attire."
    
    rose @ say "In a sane society this would never even be a problem but just *look* at this!"
    
    n "Rose holds her key fob up to her door. The little LED that's supposed to flash green and unlock the door remains dark."
    
    rose @ say "Once again, the human desire to make everything electronic has failed to consider basic usability."
    
    show rose athletic tired
    
    player "What really? The door locks run on the main power?"
    player "I guess if you're locked out of your room you can stay in mine until the electricity comes back on."
    
    n "*click*"
    n "You look back to your door which has just shut on its own, locking you out."
    
    player "Oh fuck."
    
    n "You try your key a few times and get the same result as Rose."
    
    player "Okay I'm with you, smart electronics are dumb."
    
    n "Rose kicks her door one more time, just for good measure."
    n "The power might be out all day. Gotta find some way to pass the time."
    
    menu:
        n "{cps=0}The power might be out all day. Gotta find some way to pass the time.{/cps}"
        "Wanna go get some coffee?":
            $ offeredRoseCoffeeDuringOutage = True
            $ rosePoints += 1
        
            player "Wanna go get some coffee? It'll be my treat."
            
            show rose athletic dismissive
        
            rose @ say "What, when I'm dressed like this? I just got back from the gym!"
            
            player "I don't mind."
            
            show rose athletic furious
            
            rose @ say "Well I do!"
            
            show rose athletic tired
            
            player "I can bring something back for you then."
            
            if roseHatesYouALot == True:
                show rose athletic furious
            
                rose @ say "Forget it. Just leave me alone."
                
                player "Fine. Hope the power comes back soon. I'll be at Coffee Zone if you change your mind."
            
            else:
                show rose athletic irritated
            
                rose @ say "Psh. Do whatever you want, I don't care."
                
                n "You shrug."
                
                player "Lemme know if you change your mind I guess."
            
            jump mishkaPowerOutage
                
                
            
            
            
        "Leave her":
            n "You don't wanna spend the next few hours with a wet bitchy raccoon."
            n "You'll be content to get some coffee and wait for the power to come back on your own."
            
            player "I'm going out."
            
            show rose athletic furious
            
            rose @ say "Good. Get out of my sight."
            
            player "That's the idea."
            
            jump mishkaPowerOutage
            
label mishkaPowerOutage:
    scene bg cafe autumn day rain with dissolve
    
    play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein .4
    
    show box:
        ypos 0

    n "You pull off your hood and stomp your feet on the welcome mat upon arriving at the cafe. Luckily it seems that this part of the university still has power."
    n "The sign on the door said it was closed for autumn break but you saw Mishka from the window and she waved at you."
    
    show mishka neutral at center with dissolve:
        xzoom -1
        #xpos -440
        ypos y_mishka
    
    mishka @ say "Welcome, [name]! The shop is technically still closed but I came to get it ready for re-opening soon."
    
    show mishka neutral standing
    
    player "Perfect timing, Mishka! I hope your place didn't get hit by the power outage. I came here cause I dunno when my dorm will have electricity again."
    
    show mishka anxious smile
    
    mishka @ say "Nope! My home is all good. But I did come here for something else..."
    
    n "Mishka pulls an espresso shot from the machine and gives it a sip."
    
    show mishka happy
    
    mishka @ say "I don't have one of these fancy contraptions at home so it's nice to come here just to make myself a drink!"
    
    player "Your drinks are always worth going out of the way for!"
    
    show mishka neutral wink left
    
    mishka @ say "Hehe dyakuyu!"
    
    show mishka neutral standing
    
    mishka @ say "Is there something I can get for you?"
    
    if offeredRoseCoffeeDuringOutage == True:
        menu:
            mishka "{cps=0}Is there something I can get for you?{/cps}"
            "One coffee":
                n "You'll just get one for yourself."
                
                player "One coffee please. For here if that's okay."
                
                mishka @ say "Sure! I can stay here for a while. Hopefully the power comes back in your dorm soon."
                
                player "Yeah but I don't mind hanging out here until you have to go home."
                player "I didn't realize how dependent I was on electricity. I can't even unlock my door without it."
                
                show mishka anxious sad
                
                mishka @ say "Oh no! I don't mind staying until the electricity returns for you though!"
                
                player "They should have it fixed in a couple hours. Stuff like this happened all the time back home. Pretty much any time it stormed I'd have to prepare for the power to go out."
                
                show mishka nervous
                
                mishka @ say "And what did you do during that time?"
                
                player "Mostly played games on battery powered devices. I'd have to cook with candles."
                
                show mishka shy
                
                mishka @ say "Ah, I have had to do that before. The candle cooking."
                
                player "Yeah? And how'd you pass the time?"
                
                show mishka happy
                
                mishka @ say "Hehe I didn't have much that was battery powered but books don't need batteries!"
                
                show mishka standing neutral
                
                mishka @ say "I read a lot of science and math about reaching space."
                
                player "Cool! I like reading about space but the math stuff kinda goes beyond my understanding."
                
                show mishka neutral eyesclosed tongueout
                
                mishka @ say "It's not so hard if you have a good understanding of calculus!"
                
                player "Yeah count me out then."
                
                show mishka anxious smile
                
                mishka @ say "I see... maybe one day you'd like to learn and I could teach you?"
                
                player "I'll have to get through my statistics class first."
                
                show mishka happy
                
                mishka @ say "Well... I guess we'll see!"
                
                hide mishka with dissolve
                
                n "You sip on coffee with Mishka for a few hours until you figure the power must be back on in your dorm."
                n "By now the rain has subsided and you can both go home without getting soaked."
                
                #mishka @ say "It was good seeing you again! Come by any time!"
                
            
            "Two coffees":
                $ rosePoints += 1
                
                n "You'll bring one back for Rose after all."
                
                player "Two coffees please! To go!"
                
                show mishka anxious neutral
                
                mishka @ say "All for you? Or did you find someone to share with? Heheh~"
                
                player "There's someone who *might* appreciate it. That or she'll throw it in my face."
                
                show mishka neutral eyesclosed
                
                mishka @ say "Hoping it's the former!"
                
                player "That's the plan."
                
                show mishka standing neutral
                
                n "Mishka prepares your drinks and sends you off with a friendly wave as you brave the storm again."
                
                mishka @ say "Doh pobachennya! Good luck!"
                
                player "Thanks!"
                
                scene bg schoolhallways autumn night with fade
                
                play music "audio/music/vylet - tenderness.ogg" fadein .4
                
                show box with Dissolve(.2):
                    ypos 0
                
                n "Back at your dorm, the lights are still off. You left the lobby door ajar in case the door remained locked and without power."
                n "In the hallway you find Rose sitting with her back to the wall."
                n "You were right, the smell of coffee got her attention."
                
                show rose athletic tired lookingaway at center with dissolve:
                    ypos y_rose
                
                player "I got one for you."
                
                #rose @ say "Did you spit in it?"
                
                #player "Not this time."
                
                if roseHatesYouALot == True or rosePoints < 5:
                    show rose athletic furious
                    
                    #if she hates you and you have low points she'll splash the coffee in your face
                    
                    rose @ say "Too bad you ruined it by touching the cup with your human hands."
                    
                    player "Sorry, I'll wear gloves next time."
                    
                    show rose athletic irritated lookingaway
                    
                    rose @ say "Don't even bother getting me anything. I seriously just want you to fuck off."
                    
                    player "*Sigh.* More for me then I guess."
                    
                    hide rose with dissolve
                    
                    n "You slump against the wall, occasionally checking your phone in between sips until the power returns."
                    n "Rose doesn't even say anything to you, she just quietly unlocks her door and slips into her dorm."
                    
                    jump afterFallBreak
                else:
                    n "You hold out the drink. Rose hesitates for a moment before taking it and warming her paws."
                    
                    show rose athletic dismissive
                    
                    player "Don't worry, I got the darkest blend just for you."
                    
                    rose @ say "Hmph. You're too sweet."
                    
                    player "Was that sarcasm?"
                    
                    show rose athletic irritated
                    
                    rose @ say "No. But I hate sweetness."
                    
                    n "She takes a sip and you slump down in front of your own door."
                    
                    player "Have you ever tried it? Not being a cunt I mean?"
                    
                    show rose athletic smirk lookingaway
                    
                    rose @ say "Nah, I like being mean."
                    
                    player "Why?"
                    
                    show rose athletic tired
                    
                    n "Rose pauses as if she'd never considered it before."
                    
                    show rose athletic irritated
                    
                    rose @ say "It's just my nature. And I like the aesthetic."
                    
                    menu:
                        rose "{cps=0}It's just my nature. And I like the aesthetic.{/cps}"
                        "Valid":
                            $ rosePoints += 1
                            
                            player "And that's totally heccin' valid. You go girl!"
                            
                            show rose furious -lookingaway
                        
                            rose @ say "Oh shut up. I don't need your validation."
                            
                            show rose furious lookingaway
                            
                            rose @ say "I hate everyone and everyone hates me and that's just the way it's gonna be forever."
                            
                            player "What about your family?"
                            
                            show rose athletic dismissive
                            
                            rose @ say "You mean my grandpa? He's nice to everyone."
                            
                            player "Too bad he didn't teach you to be the same. It's clear he loves you though. And I'm sure you love him back."
                            
                            show rose athletic irritated
                            
                            rose @ say "Ick. \"Love\" doesn't exist. It's just a justification for treating people who can help you better so they're more likely to further your own goals."
                            
                            player "That's a bleak way of looking at it."
                            
                            show rose athletic unsure -lookingaway
                            
                            rose @ say "Yeah, and?"
                            
                            player "And I think you just need more people to show you kindness. Hence why I put up with all your bullshit and still brought you a coffee today."
                            
                            show rose athletic irritated
                            
                            rose @ say "Do you expect me to say thanks?"
                            
                            player "No but I expect you to appreciate that I thought of you."
                            
                            rose @ say "*siiiip*"
                            
                            show rose athletic smug lookingaway
                            
                            rose @ say "It's good."
                                
                            player "Glad you enjoy your black-as-your-soul coffee. I got something a little sweeter."
                            #player "I dunno how you drink it like that. I need at least a drop of milk or sweetener in mine."
                            
                            if (rosePoints + historySkill) > 9:
                                show rose athletic unsure
                            
                                rose @ say "...Mind if I try?"
                                
                                player "As long as you don't mind the fact that a filthy human took a sip from it."
                                
                                show rose athletic tired -lookingaway
                                
                                rose @ say "Ugh, take the lid off then."
                                
                                n "You pop off the lid and pass it to her."
                                
                                show rose athletic dismissive
                                
                                n "She sniffs it and gives it a lick but makes a face."
                                
                                rose @ say "Yup, I was right. Sweetness is overrated."
                                
                                player "You get used to it."
                                
                                n "She hands back your drink."
                                
                                show rose athletic furious
                                
                                rose @ say "I'd rather not."
                            else:
                                show rose athletic furious
                            
                                rose @ say "*Wretch*"
                                rose @ say "Learn to embrace the bitterness, coward."
                                
                                player "I'm trying to."
                                
                                
                            n "The lights suddenly turn on and the building begins to hum as the HVAC system comes alive."
                            
                            show rose athletic smirk lookingaway
                            
                            rose @ say "Finally!"
                            
                            n "Rose gets up and tries her key and the door unlocks."
                            
                            player "Guess I'll see you around, neighbor."
                            
                            show rose athletic irritated -lookingaway
                            
                            rose @ say "I wouldn't count on it."
                            
                            if rosePoints > 6:
                                show rose athletic smug lookingaway
                            
                                rose @ say "...But thanks for the coffee."
                                
                            hide rose with dissolve
                                
                            n "She heads into her room and slams the door."
                            n "What a day. You stand up and enter your room, sitting at your laptop to finally get some work done."
                            
                            
                            
                        
                        "Invalid":
                            player "So instead of trying to improve yourself, you just act like a feral raccoon and adopt a goth aesthetic to justify it?"
                            
                            show rose athletic furious
                            
                            rose @ say "I'm *constantly* in a state of self improvement. I work out every day, I've read a dozen books this semester alone, my grades are better than anyone *in the country.*"
                            
                            show rose athletic dismissive
                            
                            rose @ say "I'm already better than everyone else but that makes them jealous and act like crabs in a bucket."
                            
                            player "I'm just saying a little kindness never hurt."
                            
                            show rose athletic irritated lookingaway
                            
                            rose @ say "On the contrary, kindness is an act of weakness and submission. Strong people take what they want and always get their way. Kind people end up being pulled apart by others."
                            
                            player "Kindness isn't about selfish desires, but it does open some doors regardless."
                            
                            show rose athletic furious
                            
                            rose @ say "I'll bust down any doors in my way."
                            
                            player "How's that working for ya? Does your key work yet?"
                            
                            show rose athletic furious lookingaway
                            
                            rose @ say "Kindness isn't gonna magically bring the power back."
                            
                            n "The lights suddenly turn on and the building begins to hum as the HVAC system comes alive."
                            
                            player "Maybe it does. I was kind enough to bring you a drink and now the electricity's restored!"
                            
                            show rose athletic dismissive
                            
                            n "Rose rolls her eyes and gets up to try her key."
                            
                            rose @ say "Keep telling yourself that."
                            
                            player "Guess I'll see you around, huh neighbor?"
                            
                            show rose athletic irritated
                            
                            rose @ say "I wouldn't count on it."
                            
                            if rosePoints > 6:
                                show rose athletic smug lookingaway
                            
                                rose @ say "...But thanks for the coffee."
                                
                            hide rose with dissolve
                                
                            n "She heads into her room and slams the door."
                            n "What a day. You stand up and enter your room, sitting at your laptop to finally get some work done."
                            
                
                    jump afterFallBreak
                
                
    else:
        n "You'll just get one for yourself."
        
        player "One coffee please. For here if that's okay."
        
        mishka @ say "Sure! I can stay here for a while. Hopefully the power comes back in your dorm soon."
        
        player "Yeah but I don't mind hanging out here until you have to go home."
        player "I didn't realize how dependent I was on electricity. I can't even unlock my door without it."
        
        show mishka anxious sad
        
        mishka @ say "Oh no! I don't mind staying until the electricity returns for you though!"
        
        player "They should have it fixed in a couple hours. Stuff like this happened all the time back home. Pretty much any time it stormed I'd have to prepare for the power to go out."
        
        show mishka nervous
        
        mishka @ say "And what did you do during that time?"
        
        player "Mostly played games on battery powered devices. I'd have to cook with candles."
        
        show mishka shy
        
        mishka @ say "Ah, I have had to do that before. The candle cooking."
        
        player "Yeah? And how'd you pass the time?"
        
        show mishka happy
        
        mishka @ say "Hehe I didn't have much that was battery powered but books don't need batteries!"
        
        show mishka standing neutral
        
        mishka @ say "I read a lot of science and math about reaching space."
        
        player "Cool! I like reading about space but the math stuff kinda goes beyond my understanding."
        
        show mishka neutral eyesclosed tongueout
        
        mishka @ say "It's not so hard if you have a good understanding of calculus!"
        
        player "Yeah count me out then."
        
        show mishka anxious smile
        
        mishka @ say "I see... maybe one day you'd like to learn and I could teach you?"
        
        player "I'll have to get through my statistics class first."
        
        show mishka happy
        
        mishka @ say "Well... I guess we'll see!"
        
        hide mishka with dissolve
        
        n "You sip on coffee with Mishka for a few hours until you figure the power must be back on in your dorm."
        n "By now the rain has subsided and you can both go home without getting soaked."
        
        #mishka @ say "It was good seeing you again! Come by any time!"
            
            
    scene bg codadorm autumn day with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "When you return to your dorm, the lights are back on in the lobby and your key works on the door."
    n "Finally, you can get started on preparing for your return to class in a couple days."
    
    
    
label afterFallBreak:
    $ autumnBreakOver = True
    
    stop music fadeout 2.0
    
    scene bg black with fade

    n "As your break comes to a close, Ava, Claire, and Gunner return to Harmonia. It didn't feel like home without them."
    n "You spend the week just catching up on the events of everyone's vacations and antics."
    n "You also got your grades back from the midterms."
    
    if historySkill <= 2:
        n "Your history grade is abysmal."
    if historySkill > 2 and historySkill <= 5:
        n "You're doing fine in history. Could be better though."
    if historySkill > 5:
        n "You're doing great in history."
    if statsSkill <= 2:
        n "Holy fuck you're as bad as Gunner at statistics."
    if statsSkill > 2 and statsSkill <= 5:
        n "You got a high C in statistics. You'll take that."
    if statsSkill > 5:
        n "Gunner's gonna be jealous of your stats grade."
    if frenchSkill <= 2:
        n "Man, you're failing French. Claire is gonna kill you."
    if frenchSkill > 2 and frenchSkill <= 5:
        n "French is about what you expected. Neither bad nor great."
    if frenchSkill > 5:
        n "You're doing pretty good in French. Claire will be proud!"
    if literatureSkill <= 2:
        n "You should have bribed Ms. Ellen more to get a passing grade in literature."
    if literatureSkill > 2 and literatureSkill <= 5:
        n "As for literature, you're passing but not with any flying colors."
    if literatureSkill > 5:
        n "All your hard work in literature has paid off! Either that or Ms. Ellen just likes you."
    
    n "At least now you can plan to balance your time between studies and friends better."
    n "Just gotta pass with good enough grades to keep your scholarship."
    
    if metTrish == False:    
        n "For now though, you just feel like wandering around the campus on your own without a care in the world."
        
        jump trish1
        
    else:
        jump ch4Finale
    
    
    
    
label ch4Finale:
    scene bg codadorm autumn day with fade
    
    play music "audio/ambient/morning birds.ogg" fadein .5

    show box:
        ypos 0

    n "*knock knock knock*"

    claire @ say "[name]!!! Wake up! We've got a long day ahead of us!"

    n "You jolt awake and slowly piece together where you are."
    n "The past couple of days have felt like a dream. It's hard to remember what's real and what's not."    
    n "*KNOCK KNOCK KNOCK KNOCK*"
    n "You groan and roll out of bed."
    
    player "One second! Lemme put some pants on, jeez..."

    ava @ say "Take your time [name], we'll wait!"

    claire @ say "Or you could just open the door as you are right now :3"

    n "You throw on some clothes and open the door."
    
    show claire sweater wave happy at center:
        ypos y_claire
        xzoom -1
        xoffset -500
    show ava typical happy at center:
        ypos y_ava
        xoffset 450
    with dissolve

    claire @ say "Heyyyyy!!! Why haven't you been responding to our texts??"
    
    show claire sweater happy -wave

    player "Huh? What texts?"

    n "You pick up your phone to check but pressing the wake button only shows a dead battery on the screen."

    player "Woops. Guess I forgot to charge it."
    
    show claire sweater derp
    show ava typical whimsical

    ava @ say "It's cool. It's not like we were about to just abandon you today!"
    
    show claire sweater laughing
    show ava typical happy

    claire @ say "Yeah!! We've got a busy schedule today and it wouldn't be the same without you!"
    
    show claire sweater happy
    
    player "I'm flattered but remind me again what we're doing?"
    
    show ava typical concerned

    ava @ say "You already forgot?"
    
    show claire sweater overjoyed
    
    claire @ say "We're gonna get some boba tea and go out shopping and get massages at the spa and and and-"
    
    show ava typical happy
    show claire sweater happy
    
    player "Whoa, when did you plan this?"
    player "Did you just wake up and decide we were going out all day?"
    
    show ava typical shocked
    show claire sweater surprised earsup
    
    claire @ say "Oh my gosh do you really not remember?"

    ava @ say "Yeah, we had a whole conversation about this a couple days ago! Did you hit your head or something??"
    
    player "I don't think so? Sorry, I just genuinely don't remember this convo."
    
    show claire sweater happy
    show ava typical happy
    
    claire @ say "That's alright! We'll just have to make sure today's unforgettable then, huh?"
    
    player "Man, I've sure been tired lately. I slept in yesterday too and missed class."
    player "What's the occasion?"
    
    show claire sweater sad
    
    claire @ say "We just missed you so much we wanted to make up for it with a whole weekend together!"
    
    show claire sweater happy -earsup
    
    player "Aww, you guys~"
    
    show ava typical whimsical
    
    ava @ say "Come on, we've got a long day ahead of us! Let's get coffee first to wake you up, sleepyhead~"
    
    hide ava
    hide claire
    with dissolve
    
    stop music fadeout 2.0
    
    scene bg black with dissolve

    n "After grabbing breakfast at Coffee Zone, you, Claire and Ava roamed the streets off campus."
    n "The three of you walked through main street and explored the various antique shops, boutiques, and other stores."
    n "Getting pampered at the spa was the highlight of the day."
    n "Getting a massage while Ava and Claire gossiped about petty girl drama was nice."
    n "They barely even argued!"
    #n "Not to mention your nails have never looked better."
    n "They even had a sauna!"
    n "You suspect Claire let her towel slip on purpose when you were looking in her direction even though she swears it was an accident."
    n "Then there was the incident at the tea shop where she kept referring to your drinks as 'booba tea.'"
    n "Overall it was quite a pleasant day, but apparently the bird and bunny weren't done with you yet."
    
    scene bg town summer day with fade
    
    play music "audio/music/vylet - by the seaside.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0

    show ava typical happy at center:
        ypos y_ava
        xoffset 500
    show claire sweater happy at center:
        xzoom -1
        xoffset -500
        ypos y_claire
    with dissolve

    player "This was awesome, we should do this again sometime."
    
    show claire sweater surprised earsup

    claire @ say "Hey today's not over yet! The night's still young, you know~"
    
    show ava typical shocked

    ava @ say "Yeah, don't tell me you forgot our sleepover plans too!"

    player "Huh? I'm sleeping over at your place tonight?"

    show claire sweater leaning suggestive

    claire @ say "Other way around, silly~"
    
    show claire sweater happy
    show ava typical overjoyed

    ava @ say "Your dorm is so much nicer than ours! They gave you more room even though it's just you in here."
    
    show ava typical happy

    player "Yeah but where are you two gonna sleep? I only have one bed."
    
    show claire sweater giggle
    show ava typical smug

    claire @ say "Oh I'm sure we can make that work~"
    
    show ava typical shy

    ava @ say "Hehehe, hope ya don't mind getting cozy with us~"

    player "Well if you insist..."
    
    scene bg codadorm autumn night with fade
    
    play music "audio/music/vylet - sailing away.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0

    n "Claire flops on your bed and Ava flutters over."
    
    show ava typical happy at center:
        xoffset 500
        ypos y_ava
    show claire sweater happy at center:
        xzoom -1
        ypos y_claire
        xoffset -500
    with dissolve
    
    show claire sweater derp

    claire @ say "Go ahead and put some Flixnet on the TV, [name]!"
    
    n "You mindlessly turn on the TV without realizing it's set to automatically resume the last thing you were watching."
    n "Oh deer lord no, not this..."
    
    show claire sweater surprised earsup
    
    claire @ say "Ooh you're into \"Monster Girl Adventures\" too?"
    
    show claire sweater pose suggestive earsup
    
    claire @ say "Good taste, [name]~"
    
    show ava overjoyed

    ava @ say "I've heard of this one! Interesting choice, [name]..."
    
    show ava typical shy
    show claire sweater happy -pose -earsup
    
    n "They're... into it? Maybe a night of watching softcore anime porn with two girls won't be so bad after all."
    n "Wait, what's that?"
    n "The pungent odor of strong alcohol reaches your nose and you look to Claire and find her sipping on a bottle of clear fluid."
    n "You can see on the label it's 95\% alcohol by volume."
    
    show claire sweater derp

    claire @ say "You got any soda? Or am I gonna have to chug this raw?"
    
    show ava typical shocked

    player "What the..? Where'd you get that?"
    
    show claire sweater pose suggestive earsup
    show ava typical whimsical
    
    claire @ say "I told you I was bringing alcohol, duh. I managed to get my paws on a full bottle of the good stuff! Pretty sweet, huh?~"

    n "She says with a wink as she licks the bottle."
    
    show ava profile unimpressed

    ava @ say "I'd say it's the opposite of sweet tasting. Just smelling it from over here is making me sick..."
    
    show claire sweater flustered

    claire @ say "Aww, don't worry I'll mix it with somethin' to make it more palatable for ya!"

    player "I think I have some sodas in the fridge."

    n "You move to get up and grab some but Claire puts her paw on your shoulder and forces you back onto the bed."
    
    show claire sweater leaning suggestive

    claire @ say "I got it~"
    
    show ava typical happy
    hide claire with dissolve

    n "The big bunny blocks your view of the TV as she walks over to the fridge, swaying her hips."
    n "She opens the door and bends down, taking her time grabbing the drinks with her ass in the air and her little tail wagging."
    n "She somehow manages to be more lewd than the anime on the screen right now."
    n "She even looks behind her to make sure you're watching. It's not like you could avoid having her in your field of view no matter which direction you're facing."
    
    show ava typical whimsical
    
    n "You look over to Ava who stifles a giggle."

    player "Was this part of the plans we made earlier too?"
    
    show ava pose smug

    ava @ say "Hehehe no, this is just how she is~"
    
    show ava typical happy
    show claire sweater happy at center:
        ypos y_claire
        xzoom -1
        xoffset -500
    with dissolve
    
    n "Claire plops down on the bed with a pack of soda and some plastic cups you had lying around, knocking both you and Ava into the air."
    n "When you come back down, the bunny wraps her arms around both you and Ava, the two of you on each side of her."
    
    show claire sweater pose suggestive

    claire @ say "Trust me, once you get a little alcohol in this bird, she'll be the same way~"

    show ava typical angry

    ava @ say "Psh, not true!"

    n "Claire pours everyone a round of drinks, mixing extra soda in with Ava's to dilute the nail polish taste and smell."

    claire @ say "You're right, you could never match how sexy I am~"
    
    show ava annoyed

    ava @ say "More like how slutty you are!"
    
    show claire sweater leaning suggestive

    n "Claire sticks our her tongue."

    claire @ say "Try not to be so jealous~"
    
    show ava profile angry
    
    if avaPoints > 5 or avaCucked == True:
        ava @ say "Hmph!"

        n "Once again you find yourself in the middle of one of their bickering sessions. At least you have some booze to sip on while they go at it."
        n "They continue to argue while you watch the show."
        
        show ava tipsy shy
        show claire sweater suggestive -leaning
        with dissolve

        ava @ say "...and bigger ishn't always better! Small, perky tits are serper... suprer... serprerior! More gooder than your big dumb cow udders!"

        claire @ say "At leasht my titties are fuggable! *hic* Who would ever wanna feel up a flat board like your chesht?"

        ava @ say "Better to get a pawfuls of shoft feathery boobas than flabby floppy fatty fat fat fat!"

        n "High school did not prepare you for this."

        claire @ say "Let'sh ssssettle this right now! [name]! If you had to pick one us... *hic* for the tiddies! Who would you pick?"

        menu:
            claire "{cps=0}Let'sh ssssettle this right now! [name]! If you had to pick one us... *hic* for the tiddies! Who would you pick?{/cps}"
            "Claire":
                $ ellenPoints = ellenPoints + 1
                $ clairePoints += 1
                $ avaPoints = avaPoints - 1
                
                n "You hesitate, preparing yourself for Ava's wrath."

                player "...Claire."
                
                show ava pose angry
                show claire sweater leaning suggestive

                claire @ say "Hah! I told ya! Humans looooooove bigger~"

                n "The bunny pulls you in for a hug, pressing her massive pillowy chest into your face while Ava glares at you."
                
                ava @ say "Grrr... Who needfsdfsa tits when -hic- when I've got an ass like this!"
                
                n "The two move onto arguing about butts. Once Claire lets you go, you take another drink and the rest of the night becomes a blur."

                
            "Ava":
                $ rosePoints = rosePoints + 1
                $ roriPoints = roriPoints + 1
                $ clairePoints = clairePoints - 1
                
                n "You hesitate, preparing yourself for Claire's wrath."
                
                player "...Ava."
                
                show claire sweater sad
                show ava profile overjoyed

                ava @ say "Hah! I was right! [name] has a more refined taste in breasts~"

                n "The bird pulls you in for a hug, rubbing your face between her petite breasts while Claire glares at you."
                
                show claire sweater suggestive
                
                claire @ say "You may have won this battle but you saw how [name] was staring when I was bent overr earlierrrr!"
                
                show ava profile angry
                
                ava @ say "That's only cause your ass is bigger than the broad side of a barnnn!"

                claire @ say "I'll take that as a compliment~"

                n "The two move onto arguing about butts. Once Ava lets you go, you take another drink and the rest of the night becomes a blur."
            "Both":
                $ avaPoints = avaPoints + 1
                $ clairePoints = clairePoints + 1
                
                player "Both are pretty great to be honest."

                n "Both Claire and Ava instantly shift from being catty to being flattered. They both hug and nuzzle you tight, pressing their chests against you."
                
                show ava profile overjoyed
                show claire sweater overjoyed

                ava @ say "Ohmygosh [name] you're soooooooo sweet!!! I'm so sorry for calling your tits flabby Claire!"

                claire @ say "[name] you're the beshtttt!! I'm sorry for calling you flat Ava!"

                n "You can't breathe but that's alright. This is a good way to die."
                n "The rest of the night is a blur, but you recall Ava and Claire moving on to arguing about who has the better ass next."
            "Neither":
                $ roriPoints += 1
                $ clairePoints -= 2
                $ avaPoints -= 1
                
                show ava pose concerned
                show claire sweater surprised earsup
                
                player "Neither."
                
                show claire sweater laughing
                
                claire @ say "Gaaaaaay!"
                
                ava @ say "Yeah [name], what'ssss wrong wit -hic- with you??"
                
                player "Nothing! I just don't wanna choose between you two!"
                
                show claire sweater suggestive
                
                claire @ say "What, you want us boooooth??"
                
                show ava pose shy
                
                ava @ say "I think we could arrange that~"
                
                player "That's not what I..."
                
                n "They both hug and nuzzle you tight, pressing their chests against you."
                n "You're being smothered by anthro females."
                n "For some, this would be a great way to die."
                n "The rest of the night is a blur, but you recall Ava and Claire moving on to arguing about who has the better ass next."
                


        stop music fadeout 1.0

        hide box

        scene bg black with fade

        hide box

        show bg calendar
        show tmonday at norm
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7


        n "You wake up to the sound of banging on your door."
        
        scene bg codadorm autumn day with fade
        
        play music "audio/ambient/morning birds.ogg" fadein 0.1
        
        show box with Dissolve(.2):
            ypos 0
        
        n "*KNOCK KNOCK KNOCK KNOCK*"
        n "Each knock feels like they're hitting your head directly."
        n "Fuuuuuuck you're so hungover. You forgot to drink any water last night."
        n "You clumsily roll over Claire's body on your way out of bed. She's sound asleep and doesn't notice you, even as you trip over the blanket and hit the ground."
        n "You slowly open the door, just a crack."

        show gunner frown1 at center with dissolve:
            xoffset -400
            ypos y_gunner
            xzoom -1

        gunner @ say "Morning, [name]. You didn't show up to class the other day so Mrs. Herschel wanted me to give you this homework-"
        
        show gunner disgusted

        n "Gunner's eyes suddenly go wide."

        gunner @ say "Yo, is that Claire in your bed? Holy shit dude! I knew she was into you!"
        
        show gunner uncomfy

        n "You hear rummaging behind you. You take a peek and see Ava's head pop up from behind Claire's body."

        show ava topless waitwhat at center with dissolve:
            xoffset 500
            ypos y_ava

        show gunner uncomfy

        ava @ say "Gunner...? Oh uh, hey!!!"

        n "Grimacing, you slowly turn back to Gunner."

        #show gunner angry
        ###show gunner yiik pose
        
        show gunner pissed
        
        gunner @ say "Ava?!"
        gunner @ say "What the hell is going on??"
        gunner @ say "You better have a good explanation for this!"

        player "It's not what you think, we were just..."
        
        show gunner itsover

        gunner @ say "Ugh, whatever. Forget it."
        gunner @ say "Here, just take this. I gotta go. Later."

        hide gunner with dissolve

        n "He hands you a packet full of math problems and immediately turns away and leaves."
        
        show ava topless concerned

        ava @ say "..."

        ###if you have a certain number of avapoints, do this alt route instead
        #ava @ say "Who was that?"

        #player "...Nobody. Just a classmate dropping off some homework."

        #ava @ say "Mmh... What happened last night?"

        show claire topless flustered at center:
            xoffset -450
            xzoom -1
            ypos y_claire
        with dissolve

        claire @ say "*YAAAAAAAWN*"
        
        show claire topless suggestive earsdown
        
        claire @ say "Mornin'~"
        claire @ say "Last night sure was fun, huh?~"
        
        show ava topless unimpressed

        ava @ say "Ugh, maybe if I could remember it..."
        
        show claire topless laugh

        claire @ say "Aw, don't tell me you caught [name]'s amnesia too!"
        
        show claire topless happy
        
        show ava flattered

        ava @ say "Heheh... Yeah, I think that's enough drinking for me for a while..."
        
        show ava overjoyed
        
        ava @ say "Anyway, I'm sure I had a good time with you [name]!"
        
        show ava topless embarrassed
        
        if avaPoints < 5 or avaLostInterest == True:
            ava @ say "I just feel bad about Gunner..."
        else:
            ava @ say "I hope Gunner's not too upset..."
        
        menu:
            "He'll get over it":
                player "He'll get over it. We didn't even do anything."
                
                show ava topless bored
                
                ava @ say "Yeah... but this has kinda gone on long enough."
                ava @ say "It doesn't feel good stringing both of you along like this-"
                
            "Don't worry about him":
                show ava topless bored
            
                player "Don't worry about him. He can be pissy if he wants. He's just jealous."
                
                show claire topless sad
                
                claire @ say "You sure you wanna play this game, Ava? Using [name] to make Gunner chase after you more seems..."
                
                show ava topless waitwhat
                show claire topless surprised earsup
                
                ava @ say "Shshshs! I'm *definitely* not doing that!"
                
                show claire topless suggestive earsdown
                
                claire @ say "Suuuure."
            
            "We didn't even do anything":
                player "We didn't even do anything. It was basically just a cuddle puddle but drunk."
                
                ava @ say "Yeah... but still."
                
                if avaPoints < 5 or avaLostInterest == True:
                    ava @ say "I didn't want him to think I slept with you!"
                    
                    show claire topless laugh
        
                    claire @ say "Maybe don't wake up in [name]'s bed in front of him then?"
                    
                    show ava topless waitwhat
                    
                    ava @ say "I know! It was just bad timing."
                else:
                    ava @ say "I don't wanna lose him as a friend over something silly like this-"
                    
        show ava topless concerned
        show claire topless surprised earsup
                    
        ava @ say "[name]? Are you alright?"
        
        n "You suddenly feel faint. Your vision fades before you can even react. You're out cold before you even hit the floor."
    else:
        show ava typical unimpressed
    
        ava @ say "Screw this, I'm out."
        
        n "Ava gets up to leave."
        
        show claire sweater surprised earsup
        
        claire @ say "Wait! Where are you going?"
        
        ava @ say "I just said I'm leaving."
        
        player "Why?"
        
        show ava typical unamused
        
        ava @ say "This is dumb. Getting drunk at some boy's dorm on a weekend? That's just asking for trouble."
        
        show claire sweater derp
        
        claire @ say "Relax, we weren't planning on having an orgy or anything."
        
        show claire sweater happy
        
        claire @ say "And besides, you went to that party with Gunner over the break!"
        
        show ava typical annoyed
        
        #ava @ say "Oh I'm so glad you were just "
        ava @ say "Which I didn't even drink at."
        ava @ say "These stupid games are so tiring. Yeah I know we're in college and you're \"supposed\" to act like a whore but I'm looking for an actual romantic connection."
        
        menu:
            ava "{cps=0}These stupid games are so tiring. Yeah I know we're in college and you're \"supposed\" to act like a whore but I'm looking for an actual romantic connection.{/cps}"
            "Hold on...":
                player "Hold on now, I thought we were just casually hanging out."
                
                show ava typical neutral
                
                ava @ say "Well you can enjoy a \"casual\" fling with Claire tonight then. I'm leaving."
            
            "...":
                n "You don't know what to say so you remain silent."
                
                show claire sweater sad
                
                claire @ say "Sorry Ava... I just wanted to have fun together."
                
                show ava typical neutral
        
                ava @ say "Of course you did. Your version of fun."
                ava @ say "Whatever, enjoy your evening with [name]."
                
        pause .1
        
        show ava at flipright
        
        pause .1
        
        show ava at offscreenright with move:
            ypos y_ava
            xoffset 200
                
        n "She turns away and exits the room, softly closing the door behind her."
        
        player "Uh. Did I just fuck up?"
        
        show claire sweater sad
        
        claire @ say "No, I think she's just... conflicted."
        claire @ say "Don't tell her I revealed her secrets but..."
        claire @ say "She told me she wanted you to chase after her the way Gunner does."
        claire @ say "But she's just not feeling like you want her like that."
        
        player "Sorry? I guess?"
        player "I didn't really wanna compete in some love triangle and lose in the end."
        player "Besides, there's people I like more."
        
        show claire sweater surprised earsup
        
        claire @ say "Really?"
        claire @ say "Like who?"
        claire @ say "[name]? Are you alright?"

        n "You suddenly feel faint. Your vision fades before you can even react. You're out cold before you even hit the floor."
        
    stop music fadeout 2.0
                
    scene bg black
    
    pause .5
    
    n "..."
    n "........"
    n "*Beep* ... *beep* ... *beep* ..."
    
    scene bg hospital bed with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "The steady blips from a heartrate monitor welcome you back to consciousness."
    n "You're back in the hospital and you feel worse than ever before."
    n "Your muscles feel too weak to even lift your finger to the button to call the nurse."
    n "Once again your body gives up on you and you return to slumber."
    
    scene bg black with fade
    
    n "*Beep* ... *beep* ... *beep* ..."
    
    kitsuragi @ say "[name]? Are you awake?"
    
    scene bg hospital with fade
    
    play music "audio/music/vylet - do you remember the song she sang.ogg" fadein .4
    
    show box:
        ypos 0
        
    show kitsuragi at center:
        ypos y_kitsuragi
    
    player "Urgh..."
    player "I'd rather not be."
    
    kitsuragi @ say "Stay with me for a while."
    kitsuragi @ say "Your friends brought you in a week ago and this is the first time you've been coherent."
    
    player "A... whole week?!"
    
    #raise the tempo of the heart rate monitor
    
    kitsuragi @ say "Please try to stay calm. I need to ask you a few questions."
    kitsuragi @ say "Have you been experiencing any headaches, drowsiness, or nausea since the last time you were here?"
    
    player "I started getting sleepier just last week... err, the last week before I passed out I guess."
    player "And apparently I couldn't remember whole conversations I was a part of. Dunno if that is related."
    player "Also I literally won't know how I got to class sometimes. I'll just end up there like I woke up there."
    player "And occasionally I'll see static? Like that feeling like when you get up too fast after lying down for a while."
    
    kitsuragi @ say "I see."

    n "The nurse writes that down in a notepad then looks away and sighs."

    kitsuragi @ say "Look, there's no easy way to tell you this but the blood tests came back and..."
    kitsuragi @ say "And we can say with confidence that you do in fact have CORVID-91."

    n "You feel your heart sink to the bottom of your stomach."
    
    player "What?! You said I was fine last time I was here!"
    
    kitsuragi @ say "I know it's hard to accept."
    
    player "So this means I'm gonna die soon, right?"

    n "The nurse avoids eye contact, gesturing with her hands as she tries to come up with an answer for you."

    kitsuragi @ say "Well... since we caught it early... and there have been advancements in medicine... experimental technology could..."

    player "Just- how long do you think I have?"

    kitsuragi @ say "...Five years? Maybe more, maybe less. I don't know. This disease isn't easy to predict."

    player "So just enough time to graduate college and keel over. Great."
    
    kitsuragi @ say "Hey, I'm not saying for sure you'll pass away anytime soon, that was just an estimate based on average cases."
    kitsuragi @ say "Some people went ten, fifteen, almost twenty years before it was their time."
    kitsuragi @ say "You may not be around for as long as you'd like but you can do a lot in the time you have left."
    
    player "Even if I do stay around longer than expected, it'll be a miserable existence."
    player "I've seen how the affected get. They're practically zombies. No more energy, fading memory, totally apathetic."
    player "Just look at me, I'm already getting there!"
    
    kitsuragi @ say "My advice to you is to take advantage of every single day. Don't let any time go to waste. Enjoy your time here while it lasts."
    kitsuragi @ say "I guess that advice goes to everyone, but moreso in your case."

    player "So... that's it? \"You're dying, but make sure you spend your time wisely. Bye!\""

    kitsuragi @ say "Pretty much."
    kitsuragi @ say "My boss initially wanted to put you back in one of these beds so we could run more tests on you but I convinced him it would be pointless."
    kitsuragi @ say "You've got a life to live, a destiny to fulfill and such. No need to waste it in here. Do whatever you've always wanted to do."

    n "You look down, unsure of what do say or do."

    kitsuragi @ say "..."
    kitsuragi @ say "Look, I have a confession to make."
    kitsuragi @ say "I could see the signs from the first tests we ran on you."
    kitsuragi @ say "I intentionally mislead you and told you you probably didn't have the disease because I knew it would only make things worse."
    kitsuragi @ say "You've had CORVID syndrome for who knows how long, but you never even knew it until now."
    kitsuragi @ say "Don't let this drag you down. Just use this knowledge to prepare. Tell your friends how much you loved them before it's too late."
    kitsuragi @ say "I'm truly sorry, but that's the best advice I can give you."

    n "You want to argue but she's got a point."
    n "And besides, you really want to get out of this place as soon as possible."

    player "Fine. If that's all you have for me, then I'll be leaving. Thanks for the heads up."

    kitsuragi @ say "We'll continue to monitor your case and provide as much support as we can. Don't hesitate to call us if you feel strange in the slightest."
    kitsuragi @ say "Here's my card. Call me whenever you feel like, even if you just wanna talk or whatever."

    player "...Thanks."

    n "You take her card and pull yourself out of the bed, refusing her help."
    n "Just walking hurts like hell but it's nothing compared to the turmoil wracking your brain."
    
    scene bg codadorm autumn day with fade
    
    show box with Dissolve(.2):
        ypos 0
        
    play music "audio/music/vylet - wish.ogg" fadein .4
    
    n "By the time you get back to your dorm, you're panting heavily and exhausted all the energy you had left."
    n "You collapse onto your bed and close your eyes, trying to escape this reality."
    
    scene bg black with dissolve
    
    n "*Buzz buzz*"
    n "Who the hell is texting you at a time like this?"
    
    stop music fadeout 2.0


    jump ending