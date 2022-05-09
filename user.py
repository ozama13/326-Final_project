class User:
    """Class for the users getting music reccomendations

    Attributes:
        username (string): user's spotify username
        password (string): user's spotify password
        email (string): user's email connected to spotify 
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
        
        #add new user to the user database
        userData = open(r"user_database","a")
        userData.write(f"{self.username}, {self.password}, {self.email}\n")
        userData.close()
        
    def playlist(self, music):
        """list of User's personal songs aka the playlist of music they already like and listen to
        """
        self.playlist.append(music)
    
    def addFriend(self, userProfile):
        """Adds a user object to the current user's Friend list
        Side Effects:
            Changes the friend list connected to the User Object
        """
        self.friends.append(userProfile)
        
    def __repr__(self) -> str:
        return f"{self.username}"