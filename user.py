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