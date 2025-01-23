'''Press 1 for 101 Book Information
Press 2 for 202 Book Information
Press 3 for 303 Book Information
Press 4 for 404 Book Information
Press 5 for 505 Book Information
Then print Title,author, price, number of pages and genre of the book
Now, press 1 to land on the initial page 
else message,"thank you for visiting the skill circle library system'''


"""How to display text in different lines4-\n  """
 
def start():
    a=int(input("Press 1 for 101 Book Information\nPress 2 for 202 Book Information\nPress 3 for 303 Book Information\nPress 4 for 404 Book Information\nPress 5 for 505 Book Information"))
    if a==1:
        print("Name:a\nGenre:Scientific\nauthor:b\nprice:23\nnumber of pages:20")
    if a==2:
        print("Name:c\nGenre:Scientific\nauthor:d\nprice:23\nnumber of pages:20")
    if a==3:
        print("Name:e\nGenre:Scientific\nauthor:f\nprice:23\nnumber of pages:20")
    if a==4:
        print("Name:g\nGenre:Scientific\nauthor:h\nprice:23\nnumber of pages:20")
    if a==5:
        print("Name:i\nGenre:Scientific\nauthor:j\nprice:23\nnumber of pages:20")
    b=int(input("Press 1 to start again and press 2 to end"))
    if b==1:
        start()
    else:
        print("thank you for visiting Skillcircle Library System")
start()