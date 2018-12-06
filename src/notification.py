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
        for subscriber in NotificationCenter.subscriber[tag]:
            if values == None:
                subscriber()
            else:
                subscriber(values)

class NotificationName:
    play = "PLAY"
    end_video = "END_VIDEO"
