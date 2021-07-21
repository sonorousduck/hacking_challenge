# Generated by Django 3.2.3 on 2021-05-20 18:42

from django.db import migrations


def populate_db(apps, schema_editor):
    Challenge = apps.get_model('challenges', 'Challenge')
    Hint = apps.get_model('challenges', 'Hint')


    challenge_0 = Challenge(flag="password", title="Level 0", order=0, templateValue=0, hidden=False, description="You dare try to hack me!? You will never be able to!")
    challenge_0.save()


    hint_0_0 = Hint(challenge=challenge_0, hint="HTML")
    hint_0_0.save()

    hint_0_1 = Hint(challenge=challenge_0, hint="Browser Developer Tools")
    hint_0_1.save()

    challenge_1 = Challenge(flag="FJKLDAS$@*()789fds", title="Level 1", order=1, hidden=False, description="I admit, that first one was terrible security. This one isn't nearly as terrible.", templateValue=1)
    challenge_1.save()


    hint_1_0 = Hint(challenge=challenge_1, hint="HTML")
    hint_1_0.save()

    hint_1_1 = Hint(challenge=challenge_1, hint="Browser Developer Tools")
    hint_1_1.save()


    challenge_2 = Challenge(flag="0iL2oV4eH6aC8kI10nG", title="Level 2", order=2, hidden=False, description="HA! Javascript will help me here! Good luck with this one little pest!", templateValue=2)
    challenge_2.save()

    hint_2_0 = Hint(challenge=challenge_2, hint="HTML")
    hint_2_0.save()

    hint_2_0 = Hint(challenge=challenge_2, hint="Javascript Functions")
    hint_2_0.save()

    hint_2_0 = Hint(challenge=challenge_2, hint="Browser Developer Tools")
    hint_2_0.save()



    challenge_3 = Challenge(flag="@UK#K3ir3i2dsa", title="Level 3", order=3, hidden=False, description="Fine. Fine. Fine. I get it. Keeping it offsite would be a much better idea they told me. I'll do that.", templateValue=3)
    challenge_3.save()
   

    hint_3_0 = Hint(challenge=challenge_3, hint="HTTP Request Headers")
    hint_3_0.save()



    challenge_4 = Challenge(flag="T/E))2n-_-0!cj4--H*0?", title="Level 4", order=4, hidden=False, description="Do you not know who I am!? Leave me and my site alone! Offsite obviously didn't work. I'm using Javascript again.", templateValue=4)
    challenge_4.save()


    hint_4_0 = Hint(challenge=challenge_4, hint="Developer Tools")
    hint_4_0.save()

    challenge_5 = Challenge(flag="D0gI2qF4aO6", title="Level 5", order=5, hidden=False, description="I guess I underestimated just who YOU were. You ever think what would happen if I was hacking you at the same time? Or even just stealing your IP address to find out where you are? Mwahaha. Anyways, I moved it out of the html, having it be served by the server instead. Good luck lol.", templateValue=5)
    challenge_5.save()


    hint_5_0 = Hint(challenge=challenge_5, hint="HTML")
    hint_5_0.save()


    hint_5_1 = Hint(challenge=challenge_5, hint="Javascript Functions")
    hint_5_1.save()

    hint_5_2 = Hint(challenge=challenge_5, hint="Browser Developer Tools")
    hint_5_2.save()

    hint_5_3 = Hint(challenge=challenge_5, hint="HTML Forms")
    hint_5_3.save()

    hint_5_4 = Hint(challenge=challenge_5, hint="Website URL Routing")
    hint_5_4.save()

    
    challenge_6 = Challenge(flag="@U/*D4(DV}wT{F`e", title="Level 6", order=6, hidden=False, description="Forgive me if I seem neglectful now. I have... other tasks at hand. I just quickly implemented a sign in form instead. Sign in, gives password. Seems a little redundant for me to remember a password but oh well.", templateValue=6)
    challenge_6.save()



    hint_6_0 = Hint(challenge=challenge_6, hint="HTML")
    hint_6_0.save()

    hint_6_1 = Hint(challenge=challenge_6, hint="Javascript Functions")
    hint_6_1.save()

    hint_6_2 = Hint(challenge=challenge_6, hint="Browser Developer Tools")
    hint_6_2.save()

    hint_6_3 = Hint(challenge=challenge_6, hint="HTML Forms")
    hint_6_3.save()

    hint_6_3 = Hint(challenge=challenge_6, hint="GET/POST Request/Response")
    hint_6_3.save()


    challenge_7 = Challenge(flag="/D3<]3v34Q3H,tDn", title="Level 7", order=7, hidden=False, description="Hmmm... I think you could actually be handy to me. Use White Box and find the flags and submit them to me. Thank you kindly.", templateValue=7)
    challenge_7.save()

    hint_7_0 = Hint(challenge=challenge_7, hint="HTML")
    hint_7_0.save()

    hint_7_1 = Hint(challenge=challenge_7, hint="Javascript Functions")
    hint_7_1.save()

    hint_7_2 = Hint(challenge=challenge_7, hint="Browser Developer Tools")
    hint_7_2.save()

    hint_7_3 = Hint(challenge=challenge_7, hint="HTML Forms")
    hint_7_3.save()

    hint_7_4 = Hint(challenge=challenge_7, hint="GET/POST Request/Response")
    hint_7_4.save()

    hint_7_5 = Hint(challenge=challenge_7, hint="Unsanitized input")
    hint_7_5.save()

    hint_7_6 = Hint(challenge=challenge_7, hint="Unix list and read commands... meow")
    hint_7_6.save()

    hint_7_7 = Hint(challenge=challenge_7, hint="Hidden Files")
    hint_7_7.save()


    challenge_8 = Challenge(flag="1a2s3d4f5g6h7j8k9l", title="Level 8", order=8, hidden=False, description="Good. Good. There are more security flaws. Find them.", templateValue=8)
    challenge_8.save()

    hint_8_0 = Hint(challenge=challenge_8, hint="HTML")
    hint_8_0.save()

    hint_8_1 = Hint(challenge=challenge_8, hint="Javascript Functions")
    hint_8_1.save()

    hint_8_2 = Hint(challenge=challenge_8, hint="Browser Developer Tools")
    hint_8_2.save()

    hint_8_3 = Hint(challenge=challenge_8, hint="HTML Forms")
    hint_8_3.save()

    hint_8_4 = Hint(challenge=challenge_8, hint="GET/POST Request/Response")
    hint_8_4.save()

    hint_8_5 = Hint(challenge=challenge_8, hint="Unsanitized input")
    hint_8_5.save()

    hint_8_6 = Hint(challenge=challenge_8, hint="Unix list and read commands... meow")
    hint_8_6.save()

    hint_8_7 = Hint(challenge=challenge_8, hint="Hidden Files")
    hint_8_7.save()


    challenge_9 = Challenge(flag="er4w{^a=Z,dGeyF=", title="Level 9", order=9, hidden=False, description="You have potential, kid. Imma let you in on a little secret.", difficultyIndicator="Moderate", templateValue=9)
    challenge_9.save()

    
    hint_9_0 = Hint(challenge=challenge_9, hint="HTML")
    hint_9_0.save()

    hint_9_1 = Hint(challenge=challenge_9, hint="Javascript Functions")
    hint_9_1.save()

    hint_9_2 = Hint(challenge=challenge_9, hint="Browser Developer Tools")
    hint_9_2.save()

    hint_9_3 = Hint(challenge=challenge_9, hint="HTML Forms")
    hint_9_3.save()

    hint_9_4 = Hint(challenge=challenge_9, hint="GET/POST Request/Response")
    hint_9_4.save()

    hint_9_5 = Hint(challenge=challenge_9, hint="Unsanitized input")
    hint_9_5.save()

    hint_9_6 = Hint(challenge=challenge_9, hint="Unix list and read commands... meow")
    hint_9_6.save()

    hint_9_7 = Hint(challenge=challenge_9, hint="Hidden Files")
    hint_9_7.save()

    hint_9_8 = Hint(challenge=challenge_9, hint="Cookies")
    hint_9_8.save()

    hint_9_9 = Hint(challenge=challenge_9, hint="Where you make cookies is important")
    hint_9_9.save()


    challenge_10 = Challenge(flag="RARW101010RKDFJLS", title="Level 10", order=10, hidden=False, description="They think themselves so safe. Could you kindly get an admin's email and password for me?", difficultyIndicator="Moderate", templateValue=10)
    challenge_10.save()

    hint_10_0 = Hint(challenge=challenge_10, hint="Brute Force Attacks")
    hint_10_0.save()

    hint_10_1 = Hint(challenge=challenge_10, hint="Fetch Commands in Javascript")
    hint_10_1.save()

    challenge_11 = Challenge(flag="mYCaBbageS!", title="Cryptology part i.", description="This is designed to get a little experience with Cryptology. Thus this one is fairly easy. The hash was performed by shifting all letters 4 over", order=14, difficultyIndicator = "Hard", templateValue=11)
    challenge_11.save()

    hint_11_0 = Hint(challenge=challenge_11, hint="Basic Effort")
    hint_11_0.save()

    challenge_12 = Challenge(flag="YouAreAnAdminNow77@^</>", title="Cross Site Scripting", description="We need you to find a way to become an admin for the very man you were working for and end him. He is evil. You helped him. Our intel tells us there is a single way for this to be done. Good luck.", order=15, difficultyIndicator = "Hard", templateValue=12)
    challenge_12.save()

    hint_12_0 = Hint(challenge=challenge_12, hint="Cross Site Scripting")
    hint_12_0.save()


    challenge_13 = Challenge(flag="congratulations on decrypting this!", title="Cryptology Challenge", description="Below is a paragraph that has been encrypted. Solve it", order=16, difficultyIndicator="Hard", templateValue=13)
    challenge_13.save()

    hint_13_0 = Hint(challenge=challenge_13, hint="Code Breaking Skills")
    hint_13_0.save()

    hint_13_1 = Hint(challenge=challenge_13, hint="Tenacity.")
    hint_13_1.save()


    hint_13_2 = Hint(challenge=challenge_13, hint="Think about the most common letters in the alphabet and look for letters that are repeating often. Those are probably the most common letters")
    hint_13_2.save()


    hint_13_3 = Hint(challenge=challenge_13, hint="Don't be afraid to guess. The decryption of the flag and text both are recognizable English, so as you start narrowing things down, it should become easier and easier")
    hint_13_3.save()

    challenge_loneWolf_0 = Challenge(flag="#CH**O#SEN_#^%ON--=E", title="Lone Wolf Part 1", description="Your challenge is to break into a website called Lone Wolf (link down below) and shut it down. End their company for me.", order=11, difficultyIndicator = "Moderate", challengeSeries = "LoneWolf", templateValue=14)
    challenge_loneWolf_0.save()


    challenge_loneWolf_2 = Challenge(flag="DO!ITSTRI#^KETH445ESE*RV^ERD#@OWN", title="Lone Wolf Part 2", description="Your challenge is to break into a website called Lone Wolf (link down below) and shut it down. End their company for me.", order=12, difficultyIndicator = "Moderate", challengeSeries = "LoneWolf", templateValue=16)
    challenge_loneWolf_2.save()


    challenge_loneWolf_3 = Challenge(flag="Y2OU!@MONSdsTER%^", title="Lone Wolf Part 3", description="Your challenge is to break into a website called Lone Wolf (link down below) and shut it down. End their company for me.", order=13, difficultyIndicator = "Moderate", challengeSeries = "LoneWolf", templateValue=17)
    challenge_loneWolf_3.save()



class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
            ]
