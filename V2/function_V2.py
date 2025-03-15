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

def yn(user):
    yn = input("Do you want to convert to .mp3(y/n):")
    if yn == "y":
        converter(user)
    elif yn == "n":
        print("Ok bye")
    else:
        print("That is not an accepted answer try again later :(")

def converter(user):
    path = "../m4a"
    song_list = dir_list(path)
    print("List Sorted")
    print("List of Songs: " , song_list)
    for songs in song_list:
        print("-------------------------------------------------------------------------------------")
        print("Now downloading " + songs)
        song_path = "../m4a/" + songs
        songs = songs.replace(".m4a","")
        output_path = "../mp3/" +user+"Playlist/"+ songs + ".mp3"
        audio = AudioSegment.from_file(song_path)
        audio.export(output_path, format = "mp3")
        print(songs + "is finished converting")
    print("-------------------------------------------------------------------------------------")
    mv()

def mover():
    origin_path = "../m4a/"
    new_path = "../songsCache/"
    move_list = dir_list(origin_path)
    for songs in move_list:
        os.rename(origin_path + songs, new_path + songs)
    print("Songs moved to songsCache file")
    print("If you want to delete all songs in songsCache file then rerunthe code with the start code as delete")

def donwload_songs(Url,user):
    yt = YouTube(Url)
    ys = yt.streams.get_audio_only()
    ys.download(output_path="../m4a")
    print(yt.title + " is now downloading")
    yn(user)

def download_playlist(Url,user):
    pl = Playlist(Url)
    print("Your songs are now downloading")
    for video in pl.videos:
        ys = video.streams.get_audio_only()
        ys.download(output_path="../m4a")
    yn(user)

def delete():


    path = "../songsCache/"
    delete_list = dir_list(path)
    for songs in delete_list:
        path = "../songsCache/"
        os.remove(path + songs)
        print(songs + " is deleted")
    print("All cached songs have been deleted")