def song_decoder(song):

    decoded_song = song.replace("WUB", " ")
    decoded_song = decoded_song.replace("  ", " ")
    decoded_song = decoded_song.replace("  ", " ")
    decoded_song = decoded_song.replace("  ", " ")

    if decoded_song[0] == " ":
        decoded_song = decoded_song[1:]
    if decoded_song[-1] == " ":
        decoded_song = decoded_song[:-1]
    return decoded_song


print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))