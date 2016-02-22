#!/bin/bash
url_referer=$1
url_download=$2
file_name=$3
#wget -c --referer=https://www.kaggle.com/c/yelp-restaurant-photo-classification/data -O train_photos.tgz "https://kaggle2.blob.core.windows.net/competitions-data/kaggle/4829/train_photos.tgz?sv=2012-02-12&se=2016-02-13T17%3A08%3A58Z&sr=b&sp=r&sig=vmWzp%2FLMAOw7kHe6khhPI95nnDjH%2Bu7bebjMMmvRfyE%3D"
#wget -c --referer=http://pan.baidu.com/s/1nuepR0d -O dl_nlp.zip "http://www.baidupcs.com/rest/2.0/pcs/file?method=batchdownload&app_id=250528&zipcontent=%7B%22fs_id%22%3A%5B718118434897580%5D%7D&sign=DCb740ccc5511e5e8fedcff06b081203:A47Z2PHFiLoBgy6TZcdRZk%2F7p0A%3D&uid=1730478110&time=1454600654&dp-logid=788302039593798281&dp-callid=0"

wget -c --referer=$url_referer -O $file_name "${url_download}"
