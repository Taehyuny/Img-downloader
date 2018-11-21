import requests, shutil

def get(max_count = 35):
    #urllib.request.urlretrieve(다운로드 할 이미지 URL, 저장할 경로 및 파일명)
    count = 0
    img_url = "https://lovelive.aqours.faith/17450/"
    while count <= max_count:
        tempcount = str(count)
        img_url2 = img_url + tempcount  + ".jpg"
        print("+-----[ %d번 째 이미지 ]-----+" %count)
        print("+-----[ 주소 : %s ]-----+" %img_url2)
        #urllib.request.urlretrieve(img_url2.)
        r = requests.get(img_url2, stream = True, headers = {'User-agent':'Mozilla/5.0'})
        if r.status_code == 200:
            with open('img_test/%s.jpg' % tempcount, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        count += 1

    else:
        print("크롤링 종료")
get()