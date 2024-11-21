class Television:
    '''
    A class used to change power, volume and channel of a television
    Attributes:
        MIN_VOLUME (int): The minimum volume level.
        MAX_VOLUME (int): The maximum volume level.
        MIN_CHANNEL (int): The minimum channel number.
        MAX_CHANNEL (int): The maximum channel number.
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Initialize the Television object
        '''
        self.__muted = False
        self.__status = False
        self.__volume = self.MIN_VOLUME
        self.__vol_cache = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> bool:
        '''
        Toggle the power status of the Television
        
        Returns:
            bool: The current power state (True = ON, False = OFF)
        '''
        self.__status = not self.__status
        return self.__status

    def mute(self) -> bool:
        '''
        Toggle the mute status of the Television
        
        Returns:
            bool: The current mute state (True = ON, False = OFF)
        '''
        if self.__status:
            if not self.__muted:
                self.__vol_cache = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__vol_cache
                self.__muted = False
            return self.__muted

    def channel_up(self) -> int:
        '''
        Increases the channel by 1 
        
        Returns:
            int: The current channel
        '''
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
            return self.__channel

    def channel_down(self) -> int:
        '''
        Decreases the channel by 1 
        
        Returns:
            int: The current channel
        '''
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
            return self.__channel

    def volume_up(self) -> int:
        '''
        Increases the volume by 1
        If the volume is at the max, it stays the same
        
        Returns:
            int: The current volume
        '''
        if self.__status:
            if self.__muted:
                self.__volume = self.__vol_cache
                self.__muted = False

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            return self.__volume

    def volume_down(self) -> int:
        '''
        Decreases the volume by 1
        If the volume is at the min, it stays the same
        
        Returns:
            int: The current volume
        '''
        if self.__status:
            if self.__muted:
                self.__volume = self.__vol_cache
                self.__muted = False

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
            return self.__volume

    def __str__(self) -> str:
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"