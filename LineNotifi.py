import http.client
import json


url = 'https://notify-api.line.me/api/notify'

def getToken():
    try:
        conn = http.client.HTTPConnection('localhost', 3000)
        conn.request('GET', '/notification')

        response = conn.getresponse()
        data = response.read()

        if response.status == 200:
            datas = json.loads(data)
            # Assuming datas is a list of dictionaries with 'token' key
            for data in datas:
                token = data['token']
            print(token)
            conn.close()
            return token
        else:
            print('Error:', response.status, response.reason)
            conn.close()
    except Exception as e:
        print('Error occurred while processing responseToken:', e)
    
def send_text(text):
    conn = http.client.HTTPSConnection('notify-api.line.me')
    token = "j5Vy1V07apBG2tuWIuJ4S5aolnhM7VhBRla7ZdDnYgh"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {token}'
    }
    body = f'message={text}'
    conn.request('POST', '/api/notify', body, headers)

    response = conn.getresponse()
    data = response.read()
    print(data.decode())
    conn.close()




"""
    while True:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        
        cv2.imshow("Captured Image", frame)
        
        key = cv2.waitKey(1)
        if key == ord('c'):  # ถ้าผู้ใช้กด 'c'
            filename = "01.jpg"
            cv2.imwrite(filename, frame)
            sendCatEat(token, 'ส้ม')
        elif key == 27:  # ถ้าผู้ใช้กด ESC
            break
    cap.release()
    cv2.destroyAllWindows()
""" 
