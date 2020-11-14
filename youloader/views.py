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
        n = 1
        search = SearchVideos(str(query), offset = 1, mode = "json", max_results = n)

        ytresults = search.result()

        result_dict = json.loads(ytresults)

        for n in range(n):

            video_id = (result_dict['search_result'][n]['id'])
            title = (result_dict['search_result'][n]['title']) 
            link =  (result_dict['search_result'][n]['link']) 
            duration = (result_dict['search_result'][n]['duration']) 
            views = (result_dict['search_result'][n]['views'])         

# print(ytresults)

        link_list = []
        link_list.append(link)

        url = link
        url = link.replace("watch?v=", "embed/") #convert watch link to embed url for UI

        url1 = "https://img.youtube.com"
        url2 = "/vi/{}/1.jpg".format(video_id)


    
        thumb_image = urllib.parse.urljoin(url1, url2)

        

        context = {
            # "result" : ytresults,
            "link":url,
            "title": title,
            "duration": duration,
            "views": views,
            "video":link,
                
        }
        template_name = "youloader/results.html"
        return render(request, template_name, context)

    else:
        template_name = "youloader/index.html"
        return render(request, template_name)




#def download_audio(request):
   # try:
    #    with youtube_dl.YoutubeDL(audio_opts) as ydl:
   #         ydl.download(link_list)

  #  except:
 #       pass



#def downloading_video(request):
   #     try:
  #      with youtube_dl.YoutubeDL(video_opts) as ydl:
 #           ydl.download(link_list)

#   except:
#        pass

