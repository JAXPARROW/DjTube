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
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'outtmpl': '/downloads/audios/%(title)s.%(ext)s',
    'postprocessors': [
    {
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',},
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'},

    ],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


video_opts = {
    # 'format':'worstvideo[ext=mp4]+worstaudio', #during testing to reduce data consumption,
    # 'format':'bestvideo+bestaudio', #to be used in production environment,
    'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '/downloads/videos/%(title)s.%(ext)s',
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



def get_video_details(id):
    search = SearchVideos(str(id), offset = 1, mode = "json", max_results = 1)
    ytresults = search.result()
    result_dict = json.loads(ytresults) 
    return result_dict



def from_youtube(request):
    video_id = request.GET.get('v','')
    view_prefix = 'https://www.youtube.com/watch?v='
    embedd_prefix = 'https://www.youtube.com/embed/'
    youtube_view = f'{view_prefix}{video_id}'
    youtube_embedd = f'{embedd_prefix}{video_id}'
    video_details = get_video_details(video_id)
    context = {
    "view" : youtube_view,
    "embedd" : youtube_embedd,
    "result": video_details,
    }
    template_name = "youloader/from_youtube.html"
    return render(request, template_name, context)
    


def download_audio(request, id):
    search = SearchVideos(str(id), offset = 1, mode = "json", max_results = 1)
    ytresults = search.result()
    result_dict = json.loads(ytresults)
    link = (result_dict['search_result'][0]['link'])
    try:
      with youtube_dl.YoutubeDL(audio_opts) as ydl_audio:
        ydl_audio.download([link])

        return HttpResponse('Audio downloaded!')

    except:
        return HttpResponse('failed to download! ')



def download_video(request, id):
    search = SearchVideos(str(id), offset = 1, mode = "json", max_results = 1)
    ytresults = search.result()
    result_dict = json.loads(ytresults)
    link = (result_dict['search_result'][0]['link'])
    try:
      with youtube_dl.YoutubeDL(video_opts) as ydl_audio:
        ydl_audio.download([link])

        return HttpResponse('Video downloaded!')

    except:
        return HttpResponse('failed to download! ')


