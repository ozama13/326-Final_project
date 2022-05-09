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
        
        
    def __repr__(self) -> str:
        """Displays the song as a title and artists

        Returns:
            str: string of title with artist of each song 
        """
        return f"{self.title} by {self.artist}"


