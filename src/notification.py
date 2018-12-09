#-*- coding: utf-8 -*-
class NotificationCenter(object):
    subscriber = dict()

    @staticmethod
    def subscribe(tag, subscribe):
        try:
            NotificationCenter.subscriber[tag] += [subscribe]
        except:
            NotificationCenter.subscriber[tag] = [subscribe]

    @staticmethod
    def unsubscribe(tag, subscribe):
        NotificationCenter.subscriber[tag].remove(subscribe)

    @staticmethod
    def notification(tag, values=None):
        if tag not in NotificationCenter.subscriber:
            return
        for subscriber in NotificationCenter.subscriber[tag]:
            if values == None:
                subscriber()
            else:
                subscriber(values)

class NotificationName:
    play = "PLAY"
    update = "UPDATE"
    end_video = "END_VIDEO"
    add_video = "ADD_VIDEO"
