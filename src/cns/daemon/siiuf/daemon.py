""" """


class Daemon(object):

    def __init__(self, args):
        self.sentinel = True
        pass

    def run(self):
        raise NotImplementedError

        while self.sentinel:
            pass

    def stop(self):
        self.sentinel = False
