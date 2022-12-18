#!/usr/bin/env python3
import pyboblight
import time
import random

if __name__=='__main__':
    #initialize
    client=pyboblight.BobCLient('10.0.1.200')
    
    #print light information
    print(client.lights)
    
    #send random colors for 20 seconds
    now=time.time()
    stop=now+20
    while time.time()<stop:
        time.sleep(0.1)
        #prepare the light color changes
        for name,light in client.lights.items():
            light.set_color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #tell the client to update the current light color state on the server
        client.update()