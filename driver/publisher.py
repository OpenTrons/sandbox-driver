#!/usr/bin/env python3


import json, collections


class Publisher:

    topic = {
        'frontend' : 'com.opentrons.frontend',
        'driver' : 'com.opentrons.driver',
        'labware' : 'com.opentrons.labware',
        'bootloader' : 'com.opentrons.bootloader'
    }

    def __init__(self, session=None):
        """
        """
        print('publisher.__init__ called')
        self.caller = None
        if session is not None:
            self.caller = session


    def set_caller(self, session):
        """
        """
        print('publisher.set_caller called')
        self.caller = session


    def publish(self,topic,type_,name,message,param):
        """
        """
        print('publisher.publish called')
        if self.caller is not None and topic is not None and type_ is not None and name is not None and message is not None and param is not None:
            if self.caller._myAppSession is not None:
                msg = {'type':type_,'data':{name:{message:param}}}
                print()
                print('topic:')
                print(self.topic.get(topic))
                print('msg:')
                print(str(msg))
                print()
                try:
                    self.caller._myAppSession.publish(self.topic.get(topic),json.dumps(msg))
                except:
                    print("error trying to publish")
                    raise
            else:
                print("error trying to publish, caller._myAppSession is None")

