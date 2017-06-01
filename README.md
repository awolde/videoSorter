video sorter
============
I wrote this script to organize my videos from different cameras into a directory structure that is easy to drag files from and make a dvd or blu ray.

The script will create directoires with yyyy-mm format inside the `prefix` directory and create links of the videos it found in the your library directory, in my code that is set to `/vol4/photos`. Change it to whatever directory you dump your files to.

sample tree structure after you run the script....
```
$ python videoSorter.py
$ tree
/vol4/BluRayVideoLinks/
├── 2004-02
│   ├── 00000.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00579.MPG
│   ├── 00001.MPG -> /vol4/Photos/OldPictures/Pict/MOV00579.MPG
│   ├── 00002.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00674.MPG
│   ├── 00003.MPG -> /vol4/Photos/OldPictures/Pict/MOV00674.MPG
│   ├── 00004.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00723.MPG
│   └── 00005.MPG -> /vol4/Photos/OldPictures/Pict/MOV00723.MPG
├── 2004-03
│   ├── 00000.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00773.MPG
│   ├── 00001.MPG -> /vol4/Photos/OldPictures/Pict/MOV00773.MPG
│   ├── 00002.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00782.MPG
│   ├── 00003.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00783.MPG
│   ├── 00004.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00784.MPG
│   ├── 00005.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00785.MPG
│   └── 00006.MPG -> /vol4/Photos/OldPictures/T/recent pics/MOV00786.MPG
├── 2009-08
│   ├── 00000.MPG -> /vol4/Photos/OldPictures/babi's farewell/MOV01722.MPG
│   ├── 00001.MPG -> /vol4/Photos/OldPictures/babi's farewell/MOV01723.MPG
│   ├── 00002.MPG -> /vol4/Photos/OldPictures/babi's farewell/MOV01724.MPG
│   └── 00003.MPG -> /vol4/Photos/OldPictures/babi's farewell/MOV01725.MPG
├── 2009-09
│   ├── 00000.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13332.AVI
│   ├── 00001.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13334.AVI
│   ├── 00002.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13340.AVI
│   ├── 00003.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13354.AVI
│   ├── 00004.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13406.AVI
│   ├── 00005.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13407.AVI
│   ├── 00006.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13497.AVI
│   ├── 00007.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13526.AVI
│   ├── 00010.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13534.AVI
│   ├── 00011.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13535.AVI
│   └── 00012.AVI -> /vol4/Photos/Ager Bet Sept 2009/SDC13536.AVI
├── 2009-12
│   ├── 00000.MPG -> /vol4/Photos/OldPictures/New/wenchi/DSC01961.MPG
│   ├── 00001.MPG -> /vol4/Photos/OldPictures/New/wenchi/DSC01962.MPG
```

So now you can drag the 00000 to 00xxx files to any dvd creator software and encode them to make videos. Lot of digital videos shot by phones and cameras never get to be enjoyed unless you burn them to a dvd or BluRay :-)
