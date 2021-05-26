# Generated by Django 3.2.3 on 2021-05-20 18:42

from django.db import migrations


def populate_db(apps, schema_editor):
    Challenge = apps.get_model('challenges', 'Challenge')
    Hint = apps.get_model('challenges', 'Hint')


    challenge_0 = Challenge(flag="password", title="Level 0", order=0,  hidden=False, description="This level is what we call beginner's luck. You either have it... or ya don't!")
    challenge_0.save()


    hint_0_0 = Hint(challenge=challenge_0, hint="HTML")
    hint_0_0.save()

    hint_0_1 = Hint(challenge=challenge_0, hint="Browser Developer Tools")
    hint_0_1.save()

    challenge_1 = Challenge(flag="FJKLDAS$@*()789fds", title="Level 1", order=1, hidden=False, description="This one will be tougher than the last one. Enter the password to continue!")
    challenge_1.save()


    hint_1_0 = Hint(challenge=challenge_1, hint="HTML")
    hint_1_0.save()

    hint_1_1 = Hint(challenge=challenge_1, hint="Browser Developer Tools")
    hint_1_1.save()


    challenge_2 = Challenge(flag="0iL2oV4eH6aC8kI10nG", title="Level 2", order=2, hidden=False, description="This time, I am going to be better about where I keep my passwords saved. Plus! I just started learning javascript so I am going to use that to beef up my secruity measures")
    challenge_2.save()

    hint_2_0 = Hint(challenge=challenge_2, hint="HTML")
    hint_2_0.save()

    hint_2_0 = Hint(challenge=challenge_2, hint="Javascript Functions")
    hint_2_0.save()

    hint_2_0 = Hint(challenge=challenge_2, hint="Browser Developer Tools")
    hint_2_0.save()



    challenge_3 = Challenge(flag="@UK#K3ir3i2dsa", title="Level 3", order=3, hidden=False, description="This time I'm not going to rely on javascript generating some password for me. I'm keeping this one offsite")
    challenge_3.save()
   

    hint_3_0 = Hint(challenge=challenge_3, hint="HTML Request Headers")
    hint_3_0.save()



    challenge_4 = Challenge(flag="T/E))2n-_-0!cj4--H*0?", title="Level 4", order=4, hidden=False, description="I have been learning even more Javascript tricks that I think are going to help me have better security on the site! I think this is much more safe now")
    challenge_4.save()


    hint_4_0 = Hint(challenge=challenge_4, hint="Developer Tools")
    hint_4_0.save()

    challenge_5 = Challenge(flag="A0,b,C2,d,E4,f,G6", title="Level 5", order=5, hidden=False, description="Okay... So you figured that out. This time I swear it won't be as easy as hiding it in the html. This time the password uses javascript to hide it better but I'll still be able to find it if I forget. Plus! This time its served by the server and I doubt you'd figure out how to access that.")
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

    
    challenge_6 = Challenge(flag="@U/*D4(DV}wT{F`e", title="Level 6", order=6, hidden=False, description="Okay... I admit. You are pretty good. Luckily I have a friend that know how to use forms and he showed me some tips on securing my passwords better when I can't remember them.")
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


    challenge_7 = Challenge(flag="/D3<]3v34Q3H,tDn", title="Level 7", order=7, hidden=False, description="This time, I made sure that my server side validation was setup. Plus, I got my server setup where my passwords aren't in the code")
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


    challenge_8 = Challenge(flag="1a2s3d4f5g6h7j8k9l", title="Level 8", order=8, hidden=False, description="Well if you got here then you found my flaw for the next couple hours because it's gonna take time for my friend to patch that....")
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


    challenge_9 = Challenge(flag="er4w{^a=Z,dGeyF=", title="Level 9", order=9, hidden=False, description="If you have gotten to this level, you have already seen enough to solve this one. I entrust you with this gem of knowledge.")
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

    hint_9_9 = Hint(challenge=challenge_9, hint="Hackers often take advantage of already known vulnerabilities. Have you seen code you haven't used?")
    hint_9_9.save()


    challenge_10 = Challenge(flag="RARW101010RKDFJLS", title="Level 10", order=10, hidden=False, description="At least I have one more form of security. Admin. That one you can never break into! HA!")
    challenge_10.save()

    hint_10_0 = Hint(challenge=challenge_10, hint="Brute Force Attacks")
    hint_10_0.save()

    hint_10_1 = Hint(challenge=challenge_10, hint="Fetch Commands in Javascript")
    hint_10_1.save()


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
            ]
