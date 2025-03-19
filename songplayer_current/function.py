from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix import Search
from pydub import AudioSegment
import eyed3
import os

def simpleSearch(prompt):
    results = Search(prompt)
    for video in results.videos:
        return video.watch_url

def searcher(prompt):
    moresongs = "yes"
    songlist = []
    while moresongs == "yes":
        if prompt == "":
            prompt = input("What song do you want download:")
        results = Search(prompt)
        for video in results.videos:
            songlist.append(video.watch_url)
            print("Added: " + video.title)
            break
        moresongs = input("Do you want to download another song?(yes/no):")
        if moresongs == "yes":
            prompt = ""
        if moresongs == "no":
            break
    return songlist

def dir_list(path):
    dir_list = os.listdir(path)
    dir_list = sorted(dir_list)
    return dir_list

def converter(user):
    path = "/home/kush/development/songplayer/m4a"
    song_list = dir_list(path)
    for songs in song_list:
        song_path = "/home/kush/development/songplayer/m4a/" + songs
        songs = songs.replace(".m4a","")
        output_path = "/home/kush/development/songplayer/mp3/" +user+"Playlist/"+ songs + ".mp3"
        audio = AudioSegment.from_file(song_path)
        audio.export(output_path, format = "mp3")
    metadataAdder(user)
    mover()
    print("Your songs are now Downloaded")

def mover():
    origin_path = "/home/kush/development/songplayer/m4a/"
    new_path = "/home/kush/development/songplayer/songsCache/"
    move_list = dir_list(origin_path)
    for songs in move_list:
        os.rename(origin_path + songs, new_path + songs)

def donwload_songs(Url,user):
    for songs in Url:
        yt = YouTube(songs)
        ys = yt.streams.get_audio_only()
        ys.download(output_path="/home/kush/development/songplayer/m4a")
    converter(user)

def download_playlist(Url,user):
    pl = Playlist(Url)
    print("Your songs are now downloading")
    for video in pl.videos:
        ys = video.streams.get_audio_only()
        ys.download(output_path="/home/kush/development/songplayer/m4a")
    converter(user)

def delete():
    path = "/home/kush/development/songplayer/songsCache/"
    delete_list = dir_list(path)
    for songs in delete_list:
        path = "/home/kush/development/songplayer/songsCache/"
        os.remove(path + songs)
        print(songs + " is deleted")

def metadataLoader(Url):
    yt = YouTube(Url)
    artist = yt.author
    title = yt.title
    return artist, title

def metadataAdder(User):
    dir = dir_list("/home/kush/development/songplayer/mp3/"+ User + "Playlist/")
    for songs in dir:
        Url = simpleSearch(songs)
        artist,title = metadataLoader(Url)
        audiofile = eyed3.load("/home/kush/development/songplayer/mp3/" + User + "Playlist/" + songs)
        audiofile.tag.artist = artist
        audiofile.tag.album = User
        audiofile.tag.album_artist = "By "+ User
        audiofile.tag.title = title
        audiofile.tag.save()