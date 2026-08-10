"""Create a class:

Playlist

It should have:

name
songs — a list of songs"""

class Playlist:
    def __init__(self,name,songs):
        self.name=name
        self.songs=songs
    def __len__(self):
        return len(self.songs)   
     
playlist = Playlist(
    "My Playlist",
    ["Song 1", "Song 2", "Song 3", "Song 4"]
)

print(len(playlist))   