
try:
    print()
    '''
except NameError:
    print('Variable x is not defined')
    '''
except:
    print("Something went wrong")

finally: #executes whether an exception has occured or not.
    print("The 'try except' is finished")
    
    #types of blocks:
    #-except -finally -try {else block}