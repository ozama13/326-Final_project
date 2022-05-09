#326 Final Project
#BY Larissa Warthen, Jaclyn Welfeld, Olivia Zama
import user
import song

def recomender(user, friend):
    playlist1 = user.playlist
    playlist2 = friend.playlist
    
    userGenres = []
    songRecs = []
    
    #adds all songs that are in friends playlist that are not in user's
    difSongs = [song for song in playlist2 if song not in playlist1]
    
    #gather all of the genres in user's playlist
    for song in playlist1:
        userGenres.append(song.genre)
        
    #if the genre of the friends song is a genre in the user's playlist
    #it will be added to the recomended songs playlist
    for song in difSongs:
        if song.genre in userGenres:
            songRecs.append(song)
            
    return songRecs
            
    
def main ():
    """
    """
    pass
   



if __name__ == "__main__":
    pass



    


