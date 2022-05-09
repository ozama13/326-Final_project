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
        self.playlist = []
        self.friends = []
        
    def playlist(self, music):
        """list of User's personal songs aka the playlist of music they already like and listen to
        """
        self.playlist.append(music)
    
    def addFriend(self, userProfile):
        """
        """
        self.friends.append(userProfile)
        
    def __repr__(self) -> str:
        return f"{self.username}"