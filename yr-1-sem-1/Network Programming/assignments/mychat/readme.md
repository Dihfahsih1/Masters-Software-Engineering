# LiveStream - Group Live call

## Description 
A Group video calling application using the Agora Web SDK with a Django backend.
This a more of a livestream app that is makes use of MPEG- DASH for proper video quality.

##  How to use this source code

#### 1 - Clone repo
```
git clone https://github.com/Dihfahsih1/Masters-Software-Engineering/tree/main/yr-sem1/Network%20Programming/assignments/mychat
```

#### 2 - Install requirements
```
cd mychat
pip install -r requirements.txt
```

#### 3 - Update Agora credentals
In order to use this project you will need to replace the agora credentials in `views.py` and `streams.js`.

Create an account at agora.io and create an `app`. Once you create your app, you will want to copy the `appid` & `appCertificate` to update `views.py` and `streams.js`.
###### views.py
```
def getToken(request):
    appId = "YOUR APP ID"
    appCertificate = "YOUR APPS CERTIFICATE"
    ......
```

###### streams.js
```
....
const APP_ID = 'YOUR APP ID'
....
```


#### 4 - Start server
```
python manage.py runserver
```
