import requests, shutil

def get(max_count = 35):
    count = 0
    img_url = "enter url"
    while count <= max_count:
        tempcount = str(count)
        img_url2 = img_url + tempcount  + ".jpg"
        print("+-----[ %d번 째 이미지 ]-----+" %count)
        print("+-----[ 주소 : %s ]-----+" %img_url2)
        r = requests.get(img_url2, stream = True, headers = {'User-agent':'Mozilla/5.0'})
        if r.status_code == 200:
            with open('img_test/%s.jpg' % tempcount, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        count += 1

    else:
        print("크롤링 종료")
get()