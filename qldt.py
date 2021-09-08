import json
import requests
import time

TOKEN = "1486037320:AAFTQXb4r9d3izojncvlNCKQXIKSHttmZCs"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


text, chat = get_last_chat_id_and_text(get_updates())


id=["129289","129290","129278","129283","129304","129305","129306","129197","129200","129198","128204","129201","129199","128203","129192","129193","129194","129195","129196","128413","129166","129167","129176","129177","129186","129187","129229"]  
lop= ["Lập trình nâng cao", "Lập trình nâng cao", "Hệ thống nhúng", "Hệ thống nhúng", "Viễn thám", "Xử lý ảnh số", "Xử lý ảnh số", "Điện tử số", "Điện tử số", "Điện tử số", "Điện tử số", "Điện tử số", "Điện tử số", "Anten và truyền sóng", "Anten và truyền sóng", "Anten và truyền sóng", "Anten và truyền sóng", "Anten và truyền sóng", "Anten và truyền sóng", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++", "Kỹ thuật lập trình C/C++"]

ky="20211"

headers = {
    "accept": "*/*",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "content-type": "text/x-gwt-rpc; charset=UTF-8",
    "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-gwt-module-base": "https://qldt.hust.edu.vn/soicteducationstudent/",
    "x-gwt-permutation": "657CC2B6DE59491D5D25A1DD806A190B"
}
ix=0
print("Start...")
while (1):
    for i in range(0,len(id)):
        raw_data = "7|0|10|https://qldt.hust.ed.vn/soicteducationstudent/|64A3D74A7F505C8AE0C51B09092739A7|com.soict.edu.core.client.DataService|searchClasses|java.lang.String/2004016611|java.lang.Long/4227064769|java.util.List|"+ky+"|java.util.Arrays$ArrayList/2507071751|"+id[i]+"|1|2|3|4|4|5|6|6|7|8|6|QzaRkAAAA|6|P__________|9|1|5|10|"
        auth_url='https://qldt.hust.edu.vn/soicteducationstudent/data'
        request = requests.post(auth_url,headers=headers, data=raw_data)
        if (request.text.find("Teacher")>0):
            print(lop[i]," - ", id[i]," đã có phân công giáo viên.")
            send_message(lop[i]+" - "+ id[i] +" đã có phân công giáo viên.", chat)
            print(request.text)
    time.sleep(900)
    ix=ix+15
    if (ix==60):
        ix=0
        send_message("Checking", chat)

