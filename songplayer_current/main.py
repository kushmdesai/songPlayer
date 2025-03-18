import function as f
d = 0
user = input("but first what is your username:")
ps = input("Do you want to download a song:")
if ps == "yes": # tested for v3
    Url = f.searcher("")
    f.donwload_songs(Url,user)
elif ps == "p":  # do not test for v3 soon to be deleted(not tested for v3)
    Url = input("what is the url of the playlist you would like to download:")
    f.download_playlist(Url,user)
else: #tested for v3
    print("That is not a valid option")
    print("Try again later :)")