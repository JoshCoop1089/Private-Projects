# -*- coding: utf-8 -*-

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    songList = []
    currentSize = 0
#    Check if first song can fit, or just return a fail
    if songs[0][2] > max_size:
        return songList
    else:
        songList.append(songs[0][0])
        currentSize += songs[0][2]
        
#        Check rest of list by smallest size and non chosen
    songsRemaining = sorted(songs[1:], key = lambda tup:tup[2])
    while len(songsRemaining) > 0 and currentSize + songsRemaining[0][2] <= max_size:
        songName = songsRemaining[0][0]
        songList.append(songName)
        currentSize += songsRemaining[0][2]
        songsRemaining = songsRemaining[1:]

    return songList

    
    
    
    
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 12.2
print(song_playlist(songs, max_size))
ans = ['Roar','Wannabe','Timber']
print("Should be: " + str(ans))
max_size = 11
print(song_playlist(songs, max_size))
ans = ['Roar','Wannabe']
print("Should be: " + str(ans))
