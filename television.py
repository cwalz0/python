class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False
        self.__status = False
        self.__volume = self.MIN_VOLUME
        self.__vol_cache = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        return self.__status

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__vol_cache = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__vol_cache
                self.__muted = False

    def channel_up(self):
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
            return self.__channel

    def channel_down(self):
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
            return self.__channel

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__vol_cache
                self.__muted = False

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            return self.__volume

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__vol_cache
                self.__muted = False

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
            return self.__volume

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"