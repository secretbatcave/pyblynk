import sys
TOKEN           = 'Ooooo Magic beans'

from pyblynk import Hardware, client


class dave(Hardware):
    '''This class inherits from pyblynk
    This allows you to create custom apps without having to 
    edit the original class.
    '''
    value = 0
    def OnDigitalWrite(self, pin, val):
        '''Evertime a digital write is issued
        this method is fired. You get the value,
        and the pin each time this even is fired
        '''
        print 'YEAHHHH', pin, val
        Hardware.PushVirtualRead(self, 0, 1)
    def OnDigitalRead(self, pin):
        print "digital read {0}".format(pin)
        return 1
    def OnVirtualRead(self, pin):
        print "incremented the value of {0}".format(pin)
        if self.value == None:
            self.value = 0
        else:
            self.value += 1
    def OnMessage_Unknown(self, msg_type, data):
        print "unknown message"
        print msg_type, data

connection = client()
if not connection.connect():
    print('Unable to connect')
    sys.exit(2)

if not connection.auth(TOKEN):
    print('Unable to auth')
    

#now activate the class we've bashed about    
blynkBoard = dave(connection)

##
#This is a blocking loop that runs everything.
#If you want to try and do anything at the same
#time, you'll need to use threads
##
try:
    while True:
        blynkBoard.manage()
except KeyboardInterrupt:
    raise

