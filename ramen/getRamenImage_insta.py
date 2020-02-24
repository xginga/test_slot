
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import  pprint
import os,time,sys

#APIキーとシークレットを指定する
key="19377146f72ba5cfde430c7629d9adbc"
secret="7b9cd60a281837cb"
wait_time=2

def main():
    #go_download("ラーメン","1nomario")
    go_download("まりお","3mario")

def go_download(keyword,dir):
    #画像の保存パス
    savedir="./images/datasets/"+dir
    if not os._exists(savedir):
        os.mkdir(savedir)
    #APIでダウンロード
    flickr=FlickrAPI(key,secret,format="parsed-json")
    res=flickr.photos.search(
        text=keyword,
        per_page=300,
        media="photos",
        sort="relevance",
        safe_search=1,
        extras="url_q,license")
    
    #検索結果を確認
    photos=res["photos"]
    pprint(photos)
    try:
        #一枚ずつ画像をダウンロード
        for i ,photo in enumerate(photos["photo"]):
            url_q=photo["url_q"]
            filepath=savedir+"/"+photo["id"]+".jpg"
            if os.path.exists(filepath):continue
            print(str(i+1)+":download=",url_q)
            urlretrieve(url_q,filepath)
            time.sleep(wait_time)
           
    except:
        import traceback
        traceback.print_exc()
            
if __name__=="__main__":
    main()