""" Name : Marlon Cumberbatch
    ID : s5117589
    Date : 09/05/2019
    DESC : This program is an API this will grab information by using HTML requests and it will be displaying
    information such as news, Travel information and weather information.
   """

# Importing packages
import tkinter as tk
import requests
import webbrowser
from PIL import Image, ImageTk


# this function is responsible for opening a link where i will use later in the GUI
def callback():

    webbrowser.open_new("https://www.bbc.co.uk/")


# This function uses api key and the HTML and requests to gather the data from openweathermap.org
def get_weather(city, label):
    weather_key = "858fe475a1829494e4c0280d8b1ac03e"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "Metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    label["text"] = response_layout(weather)
    print(weather)


# This function is responsible for grabbing certain parts of the dictionaries and list and then displaying them
def response_layout(weather):
    try:
        name = weather["name"]
        description = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        temp_min = weather["main"]["temp_min"]
        temp_max = weather["main"]["temp_max"]

        final_str = "City: " + str(name) + "\n Description: " + str(description) \
                    + "\n Temperature: " + str(temp) + "\n Minimum: " + str(temp_min) + "\n Maximum: " + str(temp_max)
    except Exception as ex1:
        print("Caught when extracting weather information").format(ex1)
        final_str = "Cannot retrieve that information"

    return final_str


# This function uses api key and the HTML and requests to gather the data from transportapi.com
def get_travel(from_, to, label3):
    app_id = "3003a31f"
    app_key = "2bb1d528adad3e2200af1bca6f44271a"
    url = "https://transportapi.com/v3/uk/public/journey/from/{}/to/{}.json".format(from_, to)
    params = {"app_id": app_id, "app_key": app_key, from_: "from", to: "to"}
    reply = requests.get(url, params=params)
    travel = reply.json()
    label3["text"] = reply_layout(travel)
    print(travel)


# This function is responsible for grabbing certain parts of the dictionaries and list and then displaying them
def reply_layout(travel):
    try:
        from__point_name = travel["routes"][0]["route_parts"][0]["from_point_name"]
        to_point_name = travel["routes"][0]["route_parts"][0]["to_point_name"]
        destination = travel["routes"][0]["route_parts"][0]["destination"]
        line_name = travel["routes"][0]["route_parts"][0]["line_name"]
        final_str = "Starting : " + str(from__point_name) + "\n To : " + str(to_point_name) + \
                    "\n Switch at " + destination + "\n On " + str(line_name)
    except Exception as ex3:
        print("Caught when extracting travel information").format(ex3)
        final_str = "Cannot retrieve that information"

    return final_str


# This function uses api key and the HTML and requests to gather the data from newsapi.org
def get_news(label2):
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=79cfdc2408e74d90b868394990b4cf95"
    news_response = requests.get(url)
    news = news_response.json()
    print(news)
    label2["text"] = news_reply(news)


# This function is responsible for grabbing certain parts of the dictionaries and list and then displaying them
def news_reply(news):
    try:
        title = news["articles"][0]["title"]
        description = news["articles"][0]["description"]
        title2 = news["articles"][1]["title"]
        description2 = news["articles"][1]["description"]
        final_news = str(title) + "\n" + str(description) + "\n" + str(title2) + "\n" + str(description2)
    except Exception as ex2:
        print("Caught when extracting news article").format(ex2)
        final_news = "cannot retrieve article"
    return final_news


# This class is responsible for making the layout of pages and allowing several pages in the app
class ApiProject(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.geometry("1000x500")
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, PageOne, Transport):

            frame = F(container, self)

            self.frames[F] = frame

            frame.place(relheight=1, relwidth=1)

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


# The homepage for the application
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, bg="#7f7a7a")
        canvas.place(relheight=1, relwidth=1)
        load = Image.open("greyback.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(canvas, image=render)
        img.image = render
        img.place(relx=0, rely=0)
        label = tk.Label(canvas, text="Home Page", font=40, bd=10)
        label.place(relx=0.45)
        button1 = tk.Button(canvas, text="Weather page", command=lambda: controller.show_frame(PageOne))
        button1.place(relx=0.65, rely=0.8, relheight=0.2, relwidth=0.2)
        button2 = tk.Button(canvas, text="Train page", command=lambda: controller.show_frame(Transport))
        button2.place(relx=0.15, rely=0.8, relheight=0.2, relwidth=0.2)
        button3 = tk.Button(canvas, text="News article", command=lambda: get_news(label2))
        button3.place(relx=0.4, rely=0.8, relheight=0.2, relwidth=0.2)
        label2 = tk.Label(canvas,  font=12, bd=10)
        label2.place(relx=0.13, rely=0.15)
        link = tk.Label(canvas, text="https://www.bbc.co.uk/", fg="blue", cursor="hand2")
        link.place(rely=0.9, relx=0)
        link.bind("<Button-1>", callback)


# The weather page
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, bg="#7f7a7a")
        canvas.place(relheight=1, relwidth=1)
        load = Image.open("greyback.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(canvas, image=render)
        img.image = render
        img.place(relx=0, rely=0)
        label2 = tk.Label(canvas, text="Weather Page", font=40, bd=10)
        label2.place(relx=0.445)

        button1 = tk.Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0.15, rely=0.8, relheight=0.2, relwidth=0.2)

        button = tk.Button(self, text="Get Weather Details", activebackground="red", font=40,
                           command=lambda: get_weather(entry.get(), label))
        button.place(relx=0.65, rely=0.8, relheight=0.2, relwidth=0.2)
        entry = tk.Entry(self, bg="#fff9f9", font=40)
        entry.place(rely=0.5, relx=0.4)
        label = tk.Label(self, bg="#fff9f9", font=50)
        label.place(rely=0.3, relx=0.375)


# The Travel page
class Transport(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, bg="#7f7a7a")
        canvas.place(relheight=1, relwidth=1)
        load = Image.open("greyback.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(canvas, image=render)
        img.image = render
        img.place(relx=0, rely=0)
        entry1 = tk.Entry(self, font=40)
        entry1.place(rely=0.2, relx=0.4)
        entry2 = tk.Entry(self, font=40)
        entry2.place(rely=0.4, relx=0.4)
        label5 = tk.Label(self, text="Note : If the two stations are on several lines the destination is the line "
                                     "you need to switch at", font=40, bd=10)
        label5.place(relx=0.175, rely=0.3)

        button = tk.Button(self, text="Travel info", font=40, command=lambda: get_travel(entry1.get(), entry2.get(),
                                                                                         label3))
        button.place(relx=0.65, rely=0.8, relheight=0.2, relwidth=0.2)
        button3 = tk.Button(self, text="Back to home", font=40, command=lambda:
                            controller.show_frame(StartPage))
        button3.place(relx=0.15, rely=0.8, relheight=0.2, relwidth=0.2)
        label3 = tk.Label(self, bg="#fff9f9", font=50)
        label3.place(rely=0.6, relx=0.45)
        label4 = tk.Label(self, text="Train page", font=40, bd=10)
        label4.place(relx=0.45)


# Allows for the application to run and loop
app = ApiProject()
app.mainloop()
