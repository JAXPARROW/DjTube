from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from youtubesearchpython import SearchVideos
import urllib.parse
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
    'format':'worstvideo[ext=mp4]+worstaudio', #during testing to reduce data consumption
    # 'format':'bestvideo+bestaudio', #to be used in production environment
    'embed-thumbnail':'True',
    'write-description':'True',
    'write-info-json':'True',
    'write-annotations':'True',
    'writethumbnail':'True',
    'restrict-filenames':'True'
    }


def index(request):

    if request.method == 'POST':
        query = request.POST['video_name']
        n = 12
        search = SearchVideos(str(query), offset = 1, mode = "json", max_results = n)

        ytresults = search.result()

        result_dict = json.loads(ytresults)        

        context = {
            "result" : result_dict,
        
                
        }
        template_name = "youloader/results.html"
        return render(request, template_name, context)

    else:
        query = "no copyright sound"
        n = 12

        search = SearchVideos(str(query), offset = 1, mode = "json", max_results = n)

        index_results = search.result()

        result_dict = json.loads(index_results)

        # link = result_dict.search_result.link

        context = {
            "result" : result_dict
        }

        template_name = "youloader/index.html"
        return render(request, template_name, context)

        # print(link)



def download_audio(request):
    if request.method == 'POST':
        link = request.POST['result.link']
        print(link)
        # try:
        #    with youtube_dl.YoutubeDL(audio_opts) as ydl:
        #        ydl.download(link)

        # except:
        #     pass



# def download_audio(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')

#         print(url)





