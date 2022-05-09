import unittest
import song

class TestMusicShare(unittest.TestCase):
    def test_song_build():
            """tests that song object is created correctly 
    """
    song1 =  song.Song(title= "505", artist= "Arctic Monkeys", genre= "Rock")
    #actual = 
