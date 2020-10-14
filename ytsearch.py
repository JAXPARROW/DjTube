from __future__ import unicode_literals
from youtubesearchpython import SearchVideos
import youtube_dl
import json


audio_opts = {
    'format': 'bestaudio/best',
    'audio-quality':'0',
    'embed-thumbnail':'True',
    'writethumbnail':'True',
    'restrict-filenames':'True',
    'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'},
            {'key': 'EmbedThumbnail',},]}


video_opts = {
    # 'format':'worstvideo[ext=mp4]+worstaudio', #during testing to reduce data consumption
    'format':'bestvideo+bestaudio', #to be used in production environment
    'embed-thumbnail':'True',
    'write-description':'True',
    'write-info-json':'True',
    'write-annotations':'True',
    'writethumbnail':'True',
    'restrict-filenames':'True'
    }
    

n = 1 #number of search results

query = "rules dua lipa"

search = SearchVideos(str(query), offset = 1, mode = "json", max_results = n)

ytresults = search.result()


result_dict = json.loads(ytresults)


for n in range(n):

    title = (result_dict['search_result'][n]['title']) #gets the title of the video
    link =  (result_dict['search_result'][n]['link']) #gets the link of the video
    duration = (result_dict['search_result'][n]['duration'])  #gets the duration of the video
    views = (result_dict['search_result'][n]['views']) #gets the number of views


    # print(title)
    # print(link)

# print(ytresults)

#ytresults -- python str
#resultdict -- python dictionary
link_list = []
link_list.append(link)

# def show_info():
    






# youtube-dl --extract-audio --audio-format mp3 link 
def get_video():    
    try:
        with youtube_dl.YoutubeDL(video_opts) as ydl:
            ydl.download(link_list)

    except:
        pass

def get_audio():
    try:
        with youtube_dl.YoutubeDL(audio_opts) as ydl:
            ydl.download(link_list)

    except:
        pass

# show_info()
get_video()