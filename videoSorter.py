import os
from os.path import splitext, join
import datetime
from collections import OrderedDict

def findVideos(files_dict,path, ext):
  for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
      full_path = join(root, name)
      #this line prints if there are any more video formats that I'm missing
#      if splitext(name)[1].lower() not in ['.jpg','.thm','.mp4','.mov','.png','.avi']:
 #       print full_path
      if splitext(name)[1].lower() in ext and '._' not in splitext(name)[0]:
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

def compareExt(file_name,src,dst):
  return {
    splitext(file_name)[1].lower(): createLink (src, dst, splitext(file_name)[1].upper())
  }

def processVideos(mydic,prefix):
  ordered_files = OrderedDict(sorted(mydic.items(), key=lambda t: t[1]))
  yearmonths=[]
  file_counter=0
  for files in ordered_files.items():
    moyr=datetime.datetime.fromtimestamp(int(files[1])).strftime('%Y-%m')
    src, dst = files[0], prefix + moyr + '/' + str("%5.5d"%(file_counter))
    if moyr not in yearmonths:
      #make the dir and linkt the first file
      yearmonths.append(moyr)
      print 'added', moyr
      if not os.path.exists(prefix + moyr):
        os.makedirs(prefix + moyr)
        file_counter=0
        dst = prefix + moyr + '/' + str("%5.5d"%(file_counter))
    compareExt(files[0],src,dst)
    print 'current file:', files[0], '==>', moyr + '/' + str("%5.5d"%(file_counter))
    file_counter+=1
  print len(ordered_files),'files processed!!'

prefix='/vol4/BluRayVideoLinks/'
extensions = ['.mp4', '.mov', '.avi', '.mpg', '.3gp']
mydic={}
mydic=findVideos(mydic,'/vol4/Photos',extensions)


processVideos(mydic,prefix)
