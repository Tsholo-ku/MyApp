import requests
from tkinter import *


root = Tk()
frame = Frame(root, width=300)
frame.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
label1 = Label(topFrame, text="Enter a Cryptocurrency Ticker:")
e = Entry(topFrame, width=25, border=10,)
label1.pack()
e.pack()


def get_price(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    parameters = {
        "symbol": symbol
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "88f03537-8f22-4032-bf32-004a4ffe6dd1"

    }

    response = requests.get(url, params=parameters, headers=headers)

    return response.json().get("data", {}).get(symbol, {}).get("quote", {}).get("USD", {}).get("price", {})


def button_click1(symbols):
    current = e.get()
    global symbol
    symbol = "BTC"
    e.delete(0, END)
    e.insert(0, str(current) + str(symbol))


def button_click2(symbols):
    current = e.get()
    global symbol
    symbol = "ETH"
    e.delete(0, END)
    e.insert(0, str(current) + str(symbol))


def button_click3(symbols):
    current = e.get()
    global symbol
    symbol = "BNB"
    e.delete(0, END)
    e.insert(0, str(current) + str(symbol))


def button_click4(symbols):
    current = e.get()
    global symbol
    symbol = "ADA"
    e.delete(0, END)
    e.insert(0, str(current) + str(symbol))


def button_click5(symbols):
    current = e.get()
    global symbol
    symbol = "XRP"
    e.delete(0, END)
    e.insert(0, str(current) + str(symbol))


def button_click6(symbols):
    current = e.get()
    global symbol
    symbol = "DOGE"
    e.delete(0, END)
    e.insert(0, str(current) + str(symbol))


def button_enter(event):
    second_number = e.get()
    global symbol
    e.delete(0, END)
    e.insert(0, str(get_price(symbol)))


root.bind("<Return>", button_enter)


def button_clear():
    e.delete(0, END)


button_1 = Button(topFrame, text="BTC", bg="light grey", padx=40.5, pady=20, command=lambda: button_click1("BTC"))
button_2 = Button(topFrame, text="ETH", bg="light grey", padx=40, pady=20, command=lambda: button_click2("ETH"))
button_3 = Button(topFrame, text="BNB", bg="light grey", padx=41, pady=20, command=lambda: button_click3("BNB"))
button_4 = Button(bottomFrame, text="ADA", bg="light grey", padx=40, pady=20, command=lambda: button_click4("ADA"))
button_5 = Button(bottomFrame, text="XRP", bg="light grey", padx=40, pady=20, command=lambda: button_click5("XRP"))
button_6 = Button(bottomFrame, text="DOGE", bg="light grey", padx=39, pady=20, command=lambda: button_click6("DOGE"))
button_7 = Button(root, text="Clear", bg="grey", padx=20, pady=10, command=lambda: button_clear())
button_1.pack(side=LEFT)
button_2.pack(side=LEFT)
button_3.pack(side=LEFT)
button_4.pack(side=LEFT)
button_5.pack(side=LEFT)
button_6.pack(side=LEFT)
enterButton = Button(root, text="Enter", bg="grey", padx=20, pady=10, command=lambda: button_enter("Return"))
quitButton = Button(root, text="Quit", bg="grey", padx=20, pady=10, command=root.quit)
quitButton.pack(side=RIGHT)
button_7.pack(side=RIGHT)
enterButton.pack(side=RIGHT)


root.mainloop()
