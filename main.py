import os
from pytube import YouTube

url = input('URL: ')
yt = YouTube(url)

print("Title:", yt.title)
print("YouTuber:", yt.author)
print("Published:", yt.publish_date)

command = input("Audio only? [y/n]: ")

if command == 'y':
    audio = yt.streams.filter(only_audio=True).first()
    file = audio.download("/Downloaded Audios/")
    base, ext = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
    print("Done")
    
else:
    res = input("Resolution? [best/1080/720/480/360]: ")
    if res == "best":
            video = yt.streams.get_highest_resolution()
            video.download("/Downloaded Videos/")
    else:
        video = yt.streams.get_by_resolution(res + 'p')
        video.download("/Downloaded Videos/")
    print("Done")

