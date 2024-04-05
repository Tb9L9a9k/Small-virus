import webbrowser , random
link = ["www.google.com","www.x.com","www.yahoo.com","www.digikala.com","www.soft98.ir"]
while(1):
    s = random.choice(link)
    webbrowser.open(s)
