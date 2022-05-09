from unittest import assertTrue
import musicshare
import song
import user

def test_song_build():
    """tests that song object is created correctly 
    """
    song1 =  song.Song(title= "505", artist= "Arctic Monkeys", genre= "Rock")
    assert song1.title == '505','wrong title'
    assert song1.artist == 'Arctic Monkeys','wrong artist'
    assert song1.genre == 'Rock','wrong genre'

def test_user():
    """tests that user object is created correctly 
    """
    user1 = user.User(username= 'ssmith', password= 'ssmith12', email= 'ssmith@rocketmail.com')
    assert user1.username == 'ssmith','wrong username login'
    assert user1.artist == 'ssmith12','wrong password'
    assert user1.genre == 'ssmith@rocketmail.com','wrong email'

def test_addFriend():
    """tests that friend is added to friendlist correctly 
    """
    user1 = "Ilana"
    user2 = "Esther"
    user1.AddFriend(user2)
    assertTrue(user2 is in user1.friends, 'we aint chill like that') 


