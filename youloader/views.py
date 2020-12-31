from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from youtubesearchpython import SearchVideos
import urllib.parse
import youtube_dl
import json


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


audio_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/downloads/audios/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}




video_opts = {
    'format':'worstvideo[ext=mp4]+worstaudio', #during testing to reduce data consumption
    # 'format':'bestvideo+bestaudio', #to be used in production environment
    'embed-thumbnail':'True',
    'write-description':'True',
    'write-info-json':'True',
    'write-annotations':'True',
    'writethumbnail':'True',
    'progress_hooks': [my_hook],
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


        context = {
            "result" : result_dict
        }

        template_name = "youloader/index.html"
        return render(request, template_name, context)




def video_details(request, id):
    search = SearchVideos(str(id), offset = 1, mode = "json", max_results = 1)

    ytresults = search.result()

    result_dict = json.loads(ytresults)

    link = (result_dict['search_result'][0]['link'])

    # print(link)


    context = {
        "result" : result_dict,
    
            
    }
    template_name = "youloader/video_details.html"
    return render(request, template_name, context)




def download_audio(request, id):
    search = SearchVideos(str(id), offset = 1, mode = "json", max_results = 1)

    ytresults = search.result()

    result_dict = json.loads(ytresults)

    link = (result_dict['search_result'][0]['link'])


    # print(link)

    # return HttpResponse(link)

    try:
      with youtube_dl.YoutubeDL(audio_opts) as ydl_audio:
        ydl_audio.download([link])

        return HttpResponse('Downloading..............')

    except:
        return HttpResponse('failed to download! ')

        # try:
        #    with youtube_dl.YoutubeDL(audio_opts) as ydl:
        #        ydl.download(link)

        # except:
        #     pass



# def download_audio(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')

#         print(url)





