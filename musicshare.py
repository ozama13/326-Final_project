#326 Final Project
#BY Larissa Warthen, Jaclyn Welfeld, Olivia Zama
"""Accessing Spotify's API using spotipy"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=66a84e6d0e50420ebe497d5453de9f0b,
                                               client_secret=1aa483825c284850bbce50957868a21e,
                                               redirect_uri=http://localhost:9000,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


class User:
    """Class for the users getting music reccomendations

    Attributes:
        _type_: _description_
    """
    
    def __init__(self, username, password, email):
        """initializes user attributes

        Args:
        username (string): user's spotify username
        password (string): user's spotify password
        email (string): user's email connected to spotify 
        """
        self.username = username
        self.password = password
        self.email = email
        
    def playlist(self):
        """list of User's personal songs aka the playlist of music they already like and listen to
        """
        pass
    
    def recomendList(self):
        """list of new songs for the user that are reccomended due to their friend's playlist
        """
        pass

class Song:
    """Class for song objects

    Attributes: 
        title ([string]): [x coordinate of the car]
        artist ([string]): [y coordinate of the car]
        genre ([string]): [starting heading of the car]
    """
    def __init__(self, title, artist, genre):
        """initializes song qualities including title, artist, and genre

        Args:
        title (string): title of song
        artist (string): artist of song
        genre (string): genre of song
        """
        self.title = title
        self.artist = artist
        self.genre = genre






def main ():
    """Creates song reccomendations for the user 

    Args:

    
    Returns:
        list: list of reccomended songs for the user

    Side Effects:
    
    """
    songReccs = []

    return songReccs

if __name__ == "__main__":
    pass



    


