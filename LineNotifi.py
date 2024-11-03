import requests

url = 'https://notify-api.line.me/api/notify'
token = "YOUR TOKEN"
    
def send_text(text):
    LINE_HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    session_post = requests.post(url, headers=LINE_HEADERS , data = {'message':text})
    print(session_post.text)

def send_image( image_path, message):
    file_img = {'imageFile': open(image_path, 'rb')}
    LINE_HEADERS = {'Authorization':'Bearer '+token}
    session_post = requests.post(url, headers=LINE_HEADERS, files=file_img, data={'message': message})
    print(session_post.text)


def start():
    message = "\nเริ่มการทำงาน"
    send_text(message)

