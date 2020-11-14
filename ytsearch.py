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
    

n = 5 #number of search results

query = "jeje diamond"

search = SearchVideos(str(query), offset = 1, mode = "json", max_results = n)

ytresults = search.result()

# print(ytresults)

result_dict = json.loads(ytresults)

# print (result_dict)

# result_dict = json.loads(ytresults)

data = ''
for n in range(n):
    title = (result_dict['search_result'][n]['title'])
    duration = (result_dict['search_result'][n]['duration']) 

    output = json.dumps(ytresults, ensure_ascii=True, indent=2)

    dump = data+output

    print (output)




