import moviepy.editor as mpe
from pytube import YouTube
clip=mpe.VideoFileClip("E:\\practice_v\ROSÉ - On The Ground MV.mp4")#enter location of video file
audio_bg=mpe.AudioFileClip("E:\\practice_a\ROSÉ - On The Ground MV.mp4") #enter location of audio file
final_clip=clip.set_audio(audio_bg)


#give the file name of your file manually or enter the link  
inp=input("Manually save the name [y/n] \t")
if inp=="y":
    
    name=input("Enter the name of the file \t")
    final_clip.write_videofile(name+".mp4")
else:    
    link=input("Enter the link \t") 
    yt=YouTube(link)
    final_clip.write_videofile(yt.title+".mp4")  


