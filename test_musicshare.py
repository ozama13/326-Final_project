import musicshare
import song
import user

def test_song():
    song1 =  song.Song(title= '505', artist= 'Arctic Monkeys', genre= 'Rock')
    assert song1.title == '505','wrong title'
    assert song1.artist == 'Arctic Monkeys','wrong artist'
    assert song1.genre == 'Rock','wrong genre'
    
    