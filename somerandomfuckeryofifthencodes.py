#alright, some basic input output practice
print ("Alright, whats your name?")
name = input()
print ("Hi there", name)
print ('how are ya?')
how = input()
if how.lower() in ['yeet']:
    print ('lemme guess,' +name+' you bring many gifts?')
    gifts = input()
    if gifts.lower() in ["yes", "yep", "yee","ye",'yeet']:
        print ('alright, come on in')
    
else:
    print ('alright. Nice meeting yah. Enjoy your drink')
    input()