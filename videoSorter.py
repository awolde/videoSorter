import os
from os.path import splitext, join
import datetime
from collections import OrderedDict

def findVideos(files_dict,path, ext):
  for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
      full_path = join(root, name)
      #if '.JPG' != splitext(name)[1] and '.jpg' != splitext(name)[1] and '.THM' != splitext(name)[1] and '.MP4' != splitext(name)[1] and '.MOV' != splitext(name)[1] 
      if splitext(name)[1].lower() not in ['.jpg','.thm','.mp4','.mov','.png','.avi']:
        print full_path
      if ext == splitext(name)[1]:
        try:
          mtime = os.path.getmtime(full_path)
          files_dict[full_path]=mtime
        except OSError as e:
          print e
          mtime = 0
  return files_dict

def createLink (src, dst, ext):
  try:
    os.symlink(src, dst + ext)
  except OSError as e:
    print e

def processVideos(mydic,prefix):
  ordered_files = OrderedDict(sorted(mydic.items(), key=lambda t: t[1]))
  yearmonths=[]
  file_counter=0
  for files in ordered_files.items():
    print 'current file:', files[0], '==>', files[1]
    moyr=datetime.datetime.fromtimestamp(int(files[1])).strftime('%Y-%m')
    src, dst = files[0], prefix + moyr + '/' + str("%5.5o"%(file_counter))
    if moyr not in yearmonths:
      #make the dir and linkt the first file
      yearmonths.append(moyr)
      print 'added', moyr
      if not os.path.exists(prefix + moyr):
        os.makedirs(prefix + moyr)
        file_counter=0
        
        dst = prefix + moyr + '/' + str("%5.5o"%(file_counter))
        if 'MOV' or 'mov' in files[0]:
          createLink (src, dst, '.MOV')
        elif 'mp4' or 'MP4' in files[0]:
          createLink (src, dst, '.MP4')
	elif 'avi' or 'AVI' in files[0]:
	  createLink (src, dst, 'AVI')
	elif 'mpg' or 'MPG' in files[0]:
	  createLink (src, dst, 'MPG')
        file_counter+=1
    else:
      #print 'dir already exists'
      #print files[0], '==>', datetime.datetime.fromtimestamp(int(files[1])).strftime('%Y-%m')
      if 'MOV' in files[0]:
        createLink (src, dst, '.MOV')
      else:
        createLink (src, dst, '.MP4')
      file_counter+=1
  print len(ordered_files),'files processed!!'

prefix='/vol4/BluRayVideoLinks/'
mydic={}
mydic=findVideos(mydic,'/vol4/Photos','.mp4')
mydic=findVideos(mydic,'/vol4/Photos','.MOV')
mydic=findVideos(mydic,'/vol4/Photos','.mov')
mydic=findVideos(mydic,'/vol4/Photos','.AVI')
mydic=findVideos(mydic,'/vol4/Photos','.avi')
mydic=findVideos(mydic,'/vol4/Photos','.MPG')
processVideos(mydic,prefix)
