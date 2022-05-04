#326 Final Project
#BY Larissa Warthen, Jaclyn Welfeld, Olivia Zama

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

def makeList(u1, u2):
    ## return to users 
    for i in u1.playlist:
        


if __name__ == "__main__":
    pass



    


