from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
from django.http import FileResponse
import os 


# Create your views here.
def greetings(request):
	res = render(request,'ydownloader/home.html')
	return res

def download(request):
	if request.method == 'POST':
		video_url=request.POST['video_url']
		# video_url = 'https://www.youtube.com/watch?v=LIlmQ8xhRRI'
		yt = YouTube(video_url)
		thumbnail_url = yt.thumbnail_url
		title = yt.title
		length = yt.length
		desc = yt.description
		view = yt.views
		rating = yt.rating
		age_restricted = yt.age_restricted
		res = render(request,'ydownloader/home.html',{"title":title,"thumbnail_url":thumbnail_url,"video_url":video_url,"description":desc,"length":length,"views":view,"rating":rating,"age_restricted":age_restricted})
		return res
	else:
		res = render(request,'ydownloader/home.html')
		return res

def downloading(request):
	if request.method == 'POST':
		formatRadio = request.POST['formatRadio']
		if formatRadio != "audio":
			qualityRadio = request.POST['qualityRadio']
		video_url_d = request.POST['video_url_d']
		print(formatRadio)
		# print(qualityRadio)
		yt = YouTube(video_url_d)
		print(yt)
		print("Downloading start ....")
	# homedir = os.path.expanduser("~")
	# dirs = homedir + '/Downloads'

	if formatRadio == "audio":
			# yt.streams.filter(type = formatRadio).last().download()
		response = FileResponse(open(yt.streams.filter(type = formatRadio).last().download(), 'rb'))
	else:
			# yt.streams.first().download()
		response = FileResponse(open(yt.streams.first().download(), 'rb'))
	print("Downloding completed")
	# res = render(request,'ydownloader/home.html',{"msg":"Downloading completed Thanks for try our service"})
	  
	return response

    # r'C:\Users\ankit\Downloads'
    #  r'C:\Users\ankit\Downloads'
	# streams.filter(progressive=True).all()
	# yt.streams.filter(type = formatRadio,resolution=qualityRadio).first().download(r'C:\Users\ankit\Downloads')



    # return FileResponse(open(YouTube(url).streams.first().download(skip_existing=True),'rb'))