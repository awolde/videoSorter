video sorter
============
I wrote this script to organize my videos from different cameras into a directory structure that is easy to drag files from and make a dvd or blu ray.

The script will create directoires with yyyy-mm format inside the `prefix` directory and create links of the videos it found in the your library directory, in my code that is set to `/vol4/photos`. Change it to whatever directory you dump your files to.

sample tree structure after you run the script....
```
$ python videoSorter.py
$ tree
prefix-dir
.
├── 2004-02
│   ├── 00000.MOV -> /vol4/Photos/Oictures/T/recent pics/MOV00579.MPG
│   ├── 00001.MOV -> /vol4/Photos/Oictures/Pict/MOV00579.MPG
│   ├── 00002.MOV -> /vol4/Photos/Oictures/T/recent pics/MOV00674.MPG
├── 2004-03
│   ├── 00000.MOV -> /vol4/Photos/Oictures/T/recent pics/MOV00773.MPG
│   ├── 00001.MOV -> /vol4/Photos/OPictures/Pict/MOV00773.MPG
│   ├── 00002.MOV -> /vol4/Photos/Oictures/T/recent pics/MOV00782.MPG
├── 2009-08
│   ├── 00000.MOV -> /vol4/Photos/Pictures/babi/MOV01722.MPG
├── 2009-09
│   ├── 00000.MOV -> /vol4/Photos/Ager Bet Sept 2009/SDC13332.AVI
│   ├── 00001.MP4 -> /vol4/Photos/Ager Bet Sept 2009/SDC13334.AVI
```

