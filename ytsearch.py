from __future__ import unicode_literals
from youtubesearchpython import SearchVideos
import youtube_dl
import json


ydl_opts = {
    'format': 'bestaudio/best',
    'audio-quality':'0',
    'embed-thumbnail':'True',
    'writethumbnail':'True',
    'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'},
            {'key': 'EmbedThumbnail',},]}

n = 1 #number of search results

query = "panda kanyewest"

search = SearchVideos(str(query), offset = 1, mode = "json", max_results = n)

ytresults = search.result()


result_dict = json.loads(ytresults)


for n in range(n):

    title = (result_dict['search_result'][n]['title']) #gets the title of the video
    link =  (result_dict['search_result'][n]['link']) #gets the link of the video
    duration = (result_dict['search_result'][n]['duration'])  #gets the duration of the video
    views = (result_dict['search_result'][n]['views']) #gets the number of views


    print(title)
    print(link)

# print(ytresults)

# youtube-dl --extract-audio --audio-format mp3 link 

sound_list = []

sound_list.append(link)

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(sound_list)

except:
    pass