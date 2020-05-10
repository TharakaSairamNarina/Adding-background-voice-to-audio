import os
import glob
for foldername in os.listdir('each language folder'):
    for filename in os.listdir('each filename in folder'):    
        file_path='path/'+foldername+'/'+filename
        destination='path/'+foldername+'/'+filename
        if (filename.endswith(".wav")): 
            os.system("ffmpeg -i "+file_path+" -ac 1 -ar 48000 "+destination)