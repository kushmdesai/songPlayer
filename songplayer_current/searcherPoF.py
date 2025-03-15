from pytubefix import Search

prompt = input("What is the name of the song you would like to downloads:")
results = Search(prompt)

for video in results.videos:
    print(f'Title: {video.title}')
    print(f'URL: {video.watch_url}')
    print(f'Duration: {video.length} sec')
    print(f'Author: {video.author}')
    print('---')