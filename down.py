#!/usr/bin/env python3
import pandas as pd
import sys
import os, glob
import wget

file_with_links = sys.argv[1]

def to_extract(file_with_links=file_with_links):
    cols = ['user','timeStamp','media','hashtag']
    df = pd.read_csv(file_with_links, names=cols)
    df.drop_duplicates(subset=['media'], inplace=True)
    content = df.media.values

    urls_2_down = []
    for i in content:
        ext = i.split('.')[-1]
        if(ext == 'm3u8' or 'mp4'):
            urls_2_down.append(i)
        else:
            pass       

    for j in urls_2_down:
        name = j.split('/')[-1]
        pwd = os.path.dirname(os.path.realpath(__file__))

        to_down_vid = pwd + '/vid' + '/' 

        if(j.split('.')[-1] == 'mp4'):
            try:
                path_to_save = to_down_vid + name
                print('Downloading... ' + path_to_save)
                wget.download(j,path_to_save)
            except:
                print("can't download this video ...")
                pass    
        elif(j.split('.')[-1] == 'm3u8'):
            path_to_video = ''.join([j,'?tag=10']) # url
            path_to_save = to_down_vid + name.split('.')[0] + '.mp4' # -o parameter
            try:
                print('Downloading... ' + path_to_save)
                os.system("youtube-dl {} -i -q --no-warnings -o {}".format(path_to_video,path_to_save))
            except:
                print("can't download this video ...")
                pass                   

pwd = os.path.dirname(os.path.realpath(__file__))
folder_to_clean = pwd + '/vid' + '/'        
def getFileWithExt():
    ext = '*.mp4'
    os.chdir(folder_to_clean)

    to_avoid_dup = []
    for f in glob.glob(ext):
        to_avoid_dup.append(f)
    
    dup = ' (1)'
    for g in to_avoid_dup:
        if(dup in g):
            os.remove(os.path.join(folder_to_clean, g))
            print('\n' + 'Removing... ' + g)
        else:
            pass
    print('All good with videos!!!')

if __name__ == "__main__":
    to_extract()
    getFileWithExt()
    pass    
