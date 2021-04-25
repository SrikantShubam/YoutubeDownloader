from pytube import YouTube
import moviepy.editor as mpe
import time
SAVE_PATH = "D:/" 
SAVE_PATH2 = "D:\\audio"
link = input("Please enter the link \t")
yt = YouTube(link) 
def video_only():
    
    #to_do 
    print('Available formats are in the following order:')
    print("Resolution--------Fps---------Type--------------Download id")
  

    for stream in yt.streams.filter().all():
                
                    
                    # print(str(stream.resolution +"--------"+stream.fps+"---------" +stream.itag+"-----"+stream.mime_type))
        print("{0}--------{1}---------{2}--------------{3}".format(stream.resolution,stream.fps,stream.mime_type,stream.itag))

    itag = input('\nEnter the download id ')
    stream = yt.streams.get_by_itag(itag) 

    print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)    
    stream.download(SAVE_PATH)

    input('Hit Enter to exit')

def audio_only():
    
    strem= yt.streams.get_audio_only()
    print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)   
    strem.download(SAVE_PATH)
    input('Hit Enter to exit')
# # else:                
def original_video():
    
    # video downloading
    print('Available formats are in the following order:')
    print("Resolution--------Fps---------Type--------------Download id")
    yt.streams.filter().all()
    for stream in yt.streams.filter().all():
        print("{0}--------{1}---------{2}--------------{3}".format(stream.resolution,stream.fps,stream.mime_type,stream.itag))
    itag = input('\nEnter the download id ')
    stream = yt.streams.get_by_itag(itag) 
    print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)    
    stream.download(SAVE_PATH)
    print("Video downloaded")
    #audio downloading
  
    str= yt.streams.get_audio_only()
    print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH2)   
    str.download(SAVE_PATH2)

   
    print("Audio downloaded")
    input('Hit Enter to exit')


    

def compress():
    clip=mpe.VideoFileClip("D:/"+yt.title)
    audio_bg=mpe.AudioFileClip("D:\\audio\\ "+yt.title)
    final_clip=clip.set_audio(audio_bg)
    final_clip.write_videofile(yt.title+".mp4")



 
# print('Available formats :')
# yt.streams.filter().all()

user=int(input("Press 1 for downloading video only \n Press 2 for downloading audio only \n Press 3 for downloading both \t"))
if  user == 1 :
       video_only()
            
elif user==2: 
        audio_only()
           
else:   
    original_video()
    time.sleep(1)
    compress()



# https://www.youtube.com/watch?v=K9_VFxzCuQ0&list=RDK9_VFxzCuQ0&start_radio=1



