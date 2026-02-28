#weather App

from tkinter import *
from PIL import Image, ImageTk
#pip install pillow
import requests
import json


root=Tk()
root.title('Weather App')
ico = Image.open('weather.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#openweathermap

def get_data(root):
    city=user.get()
    print(city)
    API_URL="https://api.openweathermap.org/data/2.5/weather?q="+city+"API_KEY"
    resp=requests.get(API_URL)
    #print(resp)
    if resp.status_code == 200:
        data=resp.json()
        temperature=int(data['main']['temp']-273.15)
        #print(temperature)
        pressure=int(data['main']['pressure'])
        humidity=int(data['main']['humidity'])
        wind=int(data['wind']['speed'])
        condition=data['weather'][0]['main']
        print(temperature,pressure,humidity,wind,condition)
        output='Temperature:'+str(temperature)+'°C'+'\n'+'pressure:'+str(pressure)+'hpa'+'\n'+'Humidity:'+str(humidity)+'%'+'\n'+'Wind:'+str(wind)+'m/s'+'\n'+'Condition:'+condition
        print(output)
        label.config(text=output)
        

user=Entry(root,width=30,justify=CENTER,bg='pink',font=('poppins',20,'bold'))
user.grid(row=0,column=0)
user.bind("<Return>",get_data)



label=Label(root,width=26,bg='red',font=('poppins',20,'bold'))
label.grid(row=2,column=0)






root.mainloop()

