import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle():
    tv = Television()
    assert tv.power() == True 
    assert tv.power() == False

def test_channel_up():
    tv = Television()
    tv.power()
    assert tv.channel_up() == 1
    assert tv.channel_up() == 2
    assert tv.channel_up() == 3
    assert tv.channel_up() == 0

def test_channel_down():
    tv = Television()
    tv.power()
    assert tv.channel_down() == 3
    assert tv.channel_down() == 2
    assert tv.channel_down() == 1
    assert tv.channel_down() == 0

def test_volume_up():
    tv = Television()
    tv.power()
    assert tv.volume_up() == 1
    assert tv.volume_up() == 2
    assert tv.volume_up() == 2

def test_volume_down():
    tv = Television()
    tv.power()
    assert tv.volume_down() == 0
    tv.volume_up()
    assert tv.volume_down() == 0
    tv.volume_up()
    tv.volume_up()
    assert tv.volume_down() == 1

def test_mute():
    tv = Television()
    tv.power()
    assert tv.mute() == True 
    assert tv.mute() == False