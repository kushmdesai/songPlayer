import function as f
d = 0
print("Hi with this code you can downlad and convert songs to .m3")
user = input("but first what is your name")
ps = input("Do you want to download song or playlist(s/p):")
if ps == "s": # tested for v1
    Url = input("Enter Url:")
    f.donwload_songs(Url,user)
elif ps == "p":  # tested for v1
    Url = input("Enter Url:")
    f.download_playlist(Url,user)
elif ps =="convert": # tested for v1
    f.converter(user)
elif ps =="move": # tested for v1
    f.mover()
elif ps =="delete": # tested for v1
    f.delete()
else: # tested for v1
    print("That is not a valid option")
    print("Try again later :)")
    d = 1

if d == 0:
    print("It is recommended that you delete all files from songsCache file to save space.")
    e = input("Do you want to empty the songCache file(YES/no)")
    if e == "YES":
        f.delete()