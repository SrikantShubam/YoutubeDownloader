from pytube import YouTube
import time
import os
SAVE_PATH = "E:\\practice"   #save path 1  #tip have the same paths [because its the will of the code gods]
SAVE_PATH2 = "E:\\practice" #save path 2 
link = input("Please enter the link \t")    #use 399 download id it works 99% time, 398 also works
yt = YouTube(link) 

def video_only(SAVEPATH):

    print('Available formats are in the following order:')
    
  

    for stream in yt.streams.filter().all():
                
                    
        print("Resolution :{0}      Fps :{1}       Type :{2}        Download ID :{3}".format(stream.resolution,stream.fps,stream.mime_type,stream.itag))

    itag = input('\nEnter the download id ')
    stream = yt.streams.get_by_itag(itag) 

    print('\nDownloading--- '+yt.title+' into location : '+SAVEPATH)    
    stream.download(SAVEPATH)

    input('Hit Enter to exit')

def audio_only(SAVEPATH):
    
    strem= yt.streams.get_audio_only()
    print('\nDownloading--- '+yt.title+' into location : '+SAVEPATH)   
    strem.download(SAVEPATH)
  
    input('Hit Enter to exit')
# # else:                
def original_video(SAVEPATH):
    
  
    video_only(SAVEPATH+"_v")
    audio_only(SAVEPATH+"_a")
    compress()
 


    

def compress():
    s=input("Do you want to merge your files?[y/n]")
    if s=='y':
        import moviepy.editor as mpe
        from pytube import YouTube
        title=yt.title
        try :
            SAVE_PATH2 = "E:\\practice"  
            clip=mpe.VideoFileClip(SAVE_PATH2+"_v\\"+title+".mp4")  
            audio_bg=mpe.AudioFileClip(SAVE_PATH2+"_a\\"+title+".mp4")
            final_clip=clip.set_audio(audio_bg)
            final_clip.write_videofile(title+".mp4")
        except :
            print("Sorry , this file cannot be compressed as compiler can't determine file location you can still merge them manually by our merger !")   

    elif s=='n':
        print("Cool !")
    else :
        print("invalid input")        
 
user=int(input(" Press 1 for downloading video only \n Press 2 for downloading audio only \n Press 3 for downloading both \t"))
if  user == 1 :
       video_only(SAVE_PATH)
            
elif user==2: 
        audio_only(SAVE_PATH)
           
else:   
    original_video(SAVE_PATH2)
    time.sleep(1)



#test case
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
