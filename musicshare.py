#326 Final Project
#BY Larissa Warthen, Jaclyn Welfeld, Olivia Zama
import user
import song
import musicShareGUI

def recomender(user, friend):
    """Creates a playlist of songs that dont already exist in both the user and friends respective
     playlist-if the song has a genre common to the user

    Args:
        user (object): represents the current person interacting with program
        friend (object): user object associated as friend to the current user

    Returns:
        list: list of new song reccomendations based off genre overlap
    """
    playlist1 = user.playlist
    playlist2 = friend.playlist
    
    difSongs = []
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
            
def userLogin(username, password):
    userData = open('user_database.csv','r')
    
    for line in userData:
        line.split()
        
        if username == line[0]:
            if password == line[1]:
                #access to user object/ user object is one of focus, get method?
                pass
            else:
                print('Incorrect Password')
        else:
            print('User Not Found')
            
    userData.close()
                
    
    
def main ():
    """
    """
    # prompt user to login or create new user
    # login -> enter username and password (would require object shit )
    # create new user -> create username, password. enter email
   



if __name__ == "__main__":
    pass



    


