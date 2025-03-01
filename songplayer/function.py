from pytubefix import YouTube
from pytubefix import Playlist
from pydub import AudioSegment
import os
def dir_list(path):
    dir_list = os.listdir(path)
    dir_list = sorted(dir_list)
    return dir_list

def mv():
    mv = input("Do you also want to move the files(y/n):")
    if mv == "y":
        mover()
    elif mv == "n":
        print("Okay bye")
    else:
        print("That is not an accepted answer try again later :(")

def yn():
    yn = input("Do you want to convert to .mp3(y/n):")
    if yn == "y":
        converter()
    elif yn == "n":
        print("Ok bye")
    else:
        print("That is not an accepted answer try again later :(")
def converter():
    path = "../m4a"
    song_list = dir_list(path)
    print("List Sorted")
    print(song_list)
    for songs in song_list:
        print("Now downloading " + songs)
        song_path = "../m4a/" + songs
        songs = songs.replace(".m4a","")
        output_path = "../mp3/" + songs + ".mp3"
        #print("Song path is: "+ song_path)
        #print("Output song path is: " + output_path)
        audio = AudioSegment.from_file(song_path)
        audio.export(output_path, format = "mp3")
        print(songs + "is finished converting")
    mv()

def mover():
    origin_path = "../m4a/"
    new_path = "../songsCache/"
    move_list = dir_list(origin_path)
    for songs in move_list:
        os.rename(origin_path + songs, new_path + songs)
    print("Songs moved to songsCache file")
    print("If you want to delete all songs in songsCache file then rerunthe code with the start code as delete")

def donwload_songs(Url):
    yt = YouTube(Url)
    ys = yt.streams.get_audio_only()
    ys.download(output_path="../m4a")
    print(yt.title + " is now downloading")
    yn()

def download_playlist(Url):
    pl = Playlist(Url)
    print("Your songs are now downloading")
    for video in pl.videos:
        ys = video.streams.get_audio_only()
        ys.download(output_path="../m4a")
    yn()

def delete():
    path = "../songsCache/"
    delete_list = dir_list(path)
    for songs in delete_list:
        path = "../songsCache/"
        os.remove(path + songs)
        print(songs + " is deleted")
    print("All cached songs have been deleted")