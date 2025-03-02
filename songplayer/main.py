import function as f
d = 0
ps = input("Do you want to download song or playlist(s/p):")
if ps == "s": # tested for v1
    Url = input("Enter Url:")
    f.donwload_songs(Url)
elif ps == "p":  # tested for v1
    Url = input("Enter Url:")
    f.download_playlist(Url)
elif ps =="convert": # tested for v1
    f.converter()
elif ps =="move": # tested for v1
    f.mover()
elif ps =="delete": # tested for v1
    f.delete()
else: # tested for v1
    print("That is not a valid option")
    print("Try again later :)")
    d = 1

if d == 0:
    print("!!!!!!!!!!DOING THIS WILL PREMANETNLY DELETE ALL FILES!!!!!!!!!!")
    e = input("do you want to empty the songCache file(YES/no)")
    if e == "YES":
        f.delete()
