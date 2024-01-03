#Title: Evolution of Technology Learning Application
#Built Using Python and Tkinter
#Created by: Sachin Gupta



from tkinter import *
import tkinter as tk

'''Above: Importing the appropriate libraries'''

def incorrect():
  print('Incorrect, Please try again.')

def correct():
  print('Correct!')

def done():
  print('Thanks For Attending The Course.\nThe Course Is Now Done.')

'''Above: Will print this text depending on the future question answers.'''

def pagetwoanswer():
  print('Yes, you need electricity.')

def telegraphcom():
  print('The telegraph: Transmits and receives electrical signals, of which could mean different messages. - 1844')

def telephonecom():
  print('The telephone: Alexander Graham Bell invented the telephone allowing for voice communication. - 1876')

def automobilecom():
  print('The automobile: The previously made engine was used in conjunction with wheels and a metal frame to make the automobile/car. - 1885')

def radiocom():
  print('The radio: Could transmit audio across long distances. - 1901')

def televisioncom():
  print('The television: Philo Farnsworth was aged 16 when he was convinced that images could be transmitted. 5 years later, he created the first television of which transmitted a horizontal black line. - 1927')

'''Above: Will print this to go with the button clicked on as this is a bit about the topic they clicked on.'''

def pagefiveraminput():
  print(" ")
  raminput = int(input("How much RAM do you have in GB? "))
  xram = raminput * (1048576 / 128)
  print("\nYour PC has", str(xram), "times more RAM than the 128 KB of RAM that the first Apple Macintosh PC had.")

score = 0

'''Above: Collects user's RAM, multiplies by 1048576 to get the GB in KB. Then it divides by 128 to get the multiplier of their RAM to 128 KB in Macintosh.'''

def lhundredone():
  user_input = input("100: True or False: The telegraph was invented in 1844? ")
  global score
  if user_input.lower() == "true":
    score = score + 100
    print("You are correct.")
  else:
    print("You are incorrect")

def lhundredtwo():
  user_input = input("100: True or False: At one point, electronic technology was banned in Mexico? ")
  global score
  if user_input.lower() == "false":
    score = score + 100
    print("You are correct.")
  else:
    print("You are incorrect")

def lhundredthree():
  user_input = input("100: True or False: A stone knife isn’t a technology? ")
  global score
  if user_input.lower() == "false":
    score = score + 100
    print("You are correct.")
  else:
    print("You are incorrect")


def ltwohundredone():
  user_input = input("200: True or False: Electronic technologies is used in many aspects of our lives? ")
  global score
  if user_input.lower() == "true":
    score = score + 200
    print("You are correct.")
  else:
    print("You are incorrect")

def ltwohundredtwo():
  user_input = input("200: PC stands for which of the following: (private computer, pablo’s computer, personal computer, public computer): ")
  global score
  if user_input.lower() == "personal computer":
    score = score + 200
    print("You are correct.")
  else:
    print("You are incorrect")

def ltwohundredthree():
  user_input = input("200: RAM stands for which of the following: (Random Access Memory, Read Only Memory, Nothing, Reading a mall): ")
  global score
  if user_input.lower() == "random access memory":
    score = score + 200
    print("You are correct.")
  else:
    print("You are incorrect")


def lthreehundredone():
  user_input = input("300: Which of the following is the name of the first personal computer: (Kenbak, Macintosh, Asus, Intel ii): ")
  global score
  if user_input.lower() == "kenbak":
    score = score + 300
    print("You are correct.")
  else:
    print("You are incorrect")

def lthreehundredtwo():
  user_input = input("300: Name the system used for driving directions in cars: ")
  global score
  if user_input.lower() == "gps" or user_input.lower() == "global positioning system":
    score = score + 300
    print("You are correct.")
  else:
    print("You are incorrect")

def lthreehundredthree():
  user_input = input("300: Alexander Graham Bell invented which of the following: (lightbulb, electricity, radio, telephone): ")
  global score
  if user_input.lower() == "telephone":
    score = score + 300
    print("You are correct.")
  else:
    print("You are incorrect")


def lfourhundredone():
  user_input = input("Which is the function of Micheal Faraday's invention in 1831, the “electric dynamo”.(television, crude power generator, light bulb, transmits electrical signals): ")
  global score
  if user_input.lower() == "crude power generator":
    score = score + 400
    print("You are correct.")
  else:
    print("You are incorrect")

def lfourhundredtwo():
  user_input = input("400: What did the first television display to the user? (swirly line, vertical line, horizontal line, smiley face): ")
  global score
  if user_input.lower() == "horizontal line":
    score = score + 400
    print("You are correct.")
  else:
    print("You are incorrect")

def lfourhundredthree():
  user_input = input("400: What did Charles Babbage name his invention in 1822 after. (his name, a friends joke, his dog’s name backwards, a popular rapper)")
  global score
  if user_input.lower() == "his name":
    score = score + 400
    print("You are correct.")
  else:
    print("You are incorrect")


def lfivehundredone():
  user_input = input("500: How much RAM did the first Apple Macintosh PC have: (input any integer answer, in KB): ")
  global score
  if user_input == "128":
    score = score + 500
    print("You are correct.")
  else:
    print("You are incorrect")

def lfivehundredtwo():
  user_input = input("500: In what year was Apple's first Macintosh PC released in? (input any integer answer): ")
  global score
  if user_input == "1984":
    score = score + 500
    print("You are correct.")
  else:
    print("You are incorrect")

def lfivehundredthree():
  user_input = input("What does GPS stand for? (input any answer): ")
  global score
  if user_input.lower() == "global positioning system":
    score = score + 500
    print("You are correct.")
  else:
    print("You are incorrect")

'''Above: These functions are executed when the corresponding jeopardy button number (100, 200, 300, 400, 500) is clicked on. The question is outputted as a prompt to the input. If answer is correct and it matches up with the preset answer, their score is now added to by the corresponding question value (100, 200, 300, 400, 500) and you are correct is printed. If wrong, you are incorrect is printed.'''

def thescore():
  print("The current amount of money is:", str(score)+ "$")

'''Above: When jeopardy question is right, variable score is increased by the allocated amount. Then, if the button is clicked, that score is printed.'''

'''Below: Below is the functions for each of the 11 total pages. Also, all the functions have a next button to go to the next page/window (except Section 10: Diploma and Section 9: The End).'''

#Note: Below: The code is structured in reverse order
#of the pages (10, 9, 8, ...) this is because
#the pages have a "Next" button which calls the
#next page/function. Therefore, that page
#would have to already occur in the code for it to be
#called.

def ten():
  root = Tk()
  root.title("Section 10: Diploma")

  thy = input("Please enter your name: ")
  theirname = str(thy).upper()
  w = tk.Label(root, height = 15, width = 63, text="\n\nELECTRONIC TECHNOLOGY\n\n\nUpon The Recommendation Of The Faculty\nHereby Confers On\n\n" + theirname + "\n\nthe degree of Evolution Of Technology\n\n")

  w.pack()

  button = tk.Button(root, 
                   text="Go Back", 
                   command=nine)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Below: The function recieves their name from 
an input. It is then incorporated into a diploma
which has words based on the MIT diploma. This
diploma is a certificate for them completing
this Evolution Of Technology course.'''

def nine():
  root = Tk()
  root.title("Section 9: The End")

  w = tk.Label(root, height = 15, width = 63, text="Congratulations on completing the online course about the Evolution \nof Technology, brought to you by Etech!\n\nMore about etech (electric technology).\n We are founded by Sachin Gupta, an entrepreneur \nlooking to educate others about the technology space through free      \ninteractive courses. Please donate to support more of our free courses.")

  w.pack()

  button = tk.Button(root, 
                   text="Restart The Course", 
                   command=zero)
  button.pack(side=tk.LEFT)

  button = tk.Button(root, 
                   text="View Evolution of Technology Certification", 
                   command=ten)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 9: The End page (not including the diploma page).'''

def eight(): ###Add jeopardy code here.
  root = Tk()
  root.title("Section 8: Jeopardy")

  w = tk.Label(root, height = 15, width = 63, text="The Evolution of Technology: Jeopardy\n\n\n\n\n\n\n\n\n\n\n")
  #w.pack()
  
  w.place(x=100, y=100)

  w.pack()
  
  hundredone = Button(root, text='$100', command=lhundredone).place(x=53, y=100)

  hundredtwo = Button(root, text='$100', command=lhundredtwo).place(x=53, y=150)

  hundredthree = Button(root, text='$100', command=lhundredthree).place(x=53, y=200)



  twohundredone = Button(root, text='$200', command=ltwohundredone).place(x=153, y=100)

  twohundredtwo = Button(root, text='$200', command=ltwohundredtwo).place(x=153, y=150)

  twohundredthree = Button(root, text='$200', command=ltwohundredthree).place(x=153, y=200)



  threehundredone = Button(root, text='$300', command=lthreehundredone).place(x=253, y=100)

  threehundredtwo = Button(root, text='$300', command=lthreehundredtwo).place(x=253, y=150)

  threehundredthree = Button(root, text='$300', command=lthreehundredthree).place(x=253, y=200)



  fourhundredone = Button(root, text='$400', command=lfourhundredone).place(x=353, y=100)

  fourhundredtwo = Button(root, text='$400', command=lfourhundredtwo).place(x=353, y=150)

  fourhundredthree = Button(root, text='$400', command=lfourhundredthree).place(x=353, y=200)



  fivehundredone = Button(root, text='$500', command=lfivehundredone).place(x=453, y=100)

  fivehundredtwo = Button(root, text='$500', command=lfivehundredtwo).place(x=453, y=150)

  fivehundredthree = Button(root, text='$500', command=lfivehundredthree).place(x=453, y=200)



  clicktoseescore = Button(root, text='Click to see current amount of money.', command=thescore).place(x=130, y=250)

  button = tk.Button(root, 
                   text="Next", 
                   command=nine)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 8: Jeopardy Game. Each number is a button in which when clicked, calls a function of which prints the question, gives points if correct, and prints if it is correct or not.'''

def sevencontmore():
  root = Tk()
  root.title("Section 7 Continued Even More")

  w = tk.Label(root, height = 15, width = 63, text="Electronic Technology in the workplace: At work, computers are         \nused to write down notes, communicate with colleagues, and make    \npresentations and documents with word-processing softwares. Also,   \nin the medical field there is technology to monitor heart rate, do        \nscans (x-rays), and in testing DNA for different viruses/diseases/etc.  \n Lastly, there are companies built around making (hardware) electrical \n technology and companies that make the content for                          \nthem (applications and software).                                                     ")

  w.pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=eight)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 7 Continued Even More page/window.'''

def sevencont():
  root = Tk()
  root.title("Section 7 Continued")

  w = tk.Label(root, height = 15, width = 63, text="Electronic Technology in our home: Inside of our homes we have          \nelectronic technology all over the place. We use it to play games, find   \nrecipes, monitor your home (with security/camera systems), for our       \nentertainment, for doing work, and even in communicating with others. \n\nElectronic Technology in transportation: When driving we often use       \nGPS (global positioning system) systems for directions. Also, many new \nautomobiles/cars now have screens to see our speed and driving           \ninformation better, to watch movies/videos, and even to display and     \nadjust the radio,temperature, volume, and conditions of the car. There \nare also collision detection systems/sensors and self-driving technology \nthrough machine learning to help in the automotive experience.          \n\n")

  w.pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=sevencontmore)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 7 Continued page/window.'''

def seven():
  root = Tk()
  root.title("Section 7")

  w = tk.Label(root, height = 15, width = 63, text="Over time companies would develop better computer and device         \nhardware which were even smaller in size. This allowed for hand.        \nheld devices such as phones and tablets to be made as there were      \nsmall enough processors and cpus to allow such technologies.             \n\nBack then electronic technology was just an invention and nothing      \nmore. No one would have predicted the large scale and such high       \namount of functionality that technology can now do.                          \n\n")

  w.pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=sevencont)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 7 page/window.'''

def six(): #THis is not done #Add the left and right pictures.
  root = Tk()
  root.title("Section 6")

  w = tk.Label(root, height = 15, width = 63, text="With the internet being invented in 1974 and Artificial Intelligence \nalready being invented too, everything was already ready and in    \nplace and the sky was the limit for technology. Over the next 40     \nyears there would not be too many groundbreaking new inventions\n in the technology space, rather technology would be                          \nimproved and diversified into almost all areas for our lives.             \n\nWhich is the newer technology? \n\nTypewriter             Laptop               ")

  w.pack()

  button = tk.Button(root, 
                   text="Left Item", 
                   command=incorrect).place(x=155, y=230)

  button = tk.Button(root, 
                   text="Right Item", 
                   command=correct).place(x=275, y=230)
  
  button = tk.Button(root, 
                   text="Next", 
                   command=seven)
  button.pack(side=tk.LEFT)


  root.mainloop()

'''Above: Function for the Section 6 page/window. Please not the photos don't work here in repl.it.'''

def five():
  root = Tk()
  root.title("Section 5")

  w = tk.Label(root, height = 15, width = 63, text="RAM is an important part of any computer. It gives              \n applications a place to be stored and having more of it can \ngreatly increase the performance and speed of your PC.     \n\n\nNow try this: Input your device’s RAM in GB and                   \nit will be compared to the first Apple Macintosh PC.             ")

  w.pack()

  button = tk.Button(root, 
                   text="Click to input amount of RAM (in GB) into the console.", 
                   command=pagefiveraminput).place(x=80, y=235)
  
  button = tk.Button(root, 
                   text="Next", 
                   command=six)
  button.pack(side=tk.LEFT)


  root.mainloop()

'''Above: Function for the Section 5 page/window. Here, the user inputs their amount of RAM and it is compared through a multiplier to the first Macintosh's RAM which was just 128 KB.'''


def four():
  root = Tk()
  root.title("Section 4")

  w = tk.Label(root, height = 15, width = 63, text="Computers: In 1822, Charles Babbage developed the babbage \ndifference engine, the first mechanical computer. It used          \nvacuum tubes and capacitors to calculate math polynomial      \nfunctions. Then in 1937, John Attanasoff created the first         \n electronic digital computer which would take binary numbers, \n calculate them, and store it in capacitors.\n\nThe first personal computer is the Kenbak-1,released in 1971.\n Soon after many other companies released their own version of\na personal computer (PC) including Apple’s Macintosh PC in 1984")
  w.pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=five)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 4 page/window.'''

def three():
  root = Tk()
  root.title("Section 3")

  w = tk.Label(root, height = 15, width = 63, text="Please click on each of the following buttons to \nlearn more about how and when they were invented.")
  w.pack()

  telegraphbutton = Button(root, text='Telegraph', command=telegraphcom).place(x=40, y=200)

  telephonebutton = Button(root, text='Telephone', command=telephonecom).place(x=140, y=200)

  automobilebutton = Button(root, text='Automobile', command=automobilecom).place(x=242, y=200)

  radiobutton = Button(root, text='Radio', command=radiocom).place(x=350, y=200)

  televisionbutton = Button(root, text='Television', command=televisioncom).place(x=420, y=200)

  button = tk.Button(root, 
                   text="Next", 
                   command=four)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 3 page/window. When the word button (Telegraph, Telephone, etc.) is clicked on, some information of its origin (how it was invented, when it was invented, etc.) is printed to the console.'''

def two():
  root = Tk()
  root.title("Section 2")

  w = tk.Label(root, height = 8, width = 63, text="Now, what is one thing that is \nrequired for electronic technology?")
  w.pack()
  
  button = tk.Button(root, 
                   text="Click for answer.", 
                   command=pagetwoanswer).place(x=200, y=120)

  z = tk.Label(root, height = 7, width = 63, text="\nIn 1831 it was Micheal Faraday who created the “electric    \ndynamo” which is a crude power generator. This innovation \nallowed electricity to be used in technology, allowing for the\ncreation of computers and other electronic technologies. Micheal Faraday\n brought the start to electrical technology, a staple in the modern day.")
  z.pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=three)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 2 page/window.'''

def one():

  root = Tk()

  w = tk.Label(root, height = 8, width = 63, text="Technology is using scientific knowledge towards a practical purpose,\nwith evolution building on the effectivity and efficiency of the technology \nthat was made. Something as simple as a stone knife is a technology,\n though electronic technology is the main concept in this course.\n\n\nWhich of the following is not classified as an electronic technology?")
  w.pack()
#
  root.title("Section 1")

  var = IntVar()
  R1 = Radiobutton(root, text="Chair", command=correct).pack( anchor = W )

  R2 = Radiobutton(root, text="Iphone", command=incorrect).pack( anchor = W )

  R3 = Radiobutton(root, text="Tesla Model X", command=incorrect).pack( anchor = W)

  R4 = Radiobutton(root, text="Tablet", command=incorrect).pack( anchor = W)

  label = Label(root).pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=two)
  button.pack(side=tk.LEFT)

  root.mainloop()

'''Above: Function for the Section 1 page/window. Which uses the radiobutton function to display a multiple choice type question. Depending on answer, correct and incorrect is printed to the console.'''

def zero():

  root = Tk()

  w = tk.Label(root, height = 15, width = 63, text="electrictech.com/learn-about/technology-evolution/\n\n\n\n\nWelcome to etechs learning course on the Evolution of Technology.\n\n\nPlease click on \"Next\" to get started.")
  w.pack()

  button = tk.Button(root, 
                   text="Next", 
                   command=one)
  button.pack(side=tk.LEFT)

  root.title("Section 0: Introduction")

  root.mainloop()

'''Above: Function for the Section 0 page/window which is actually the first window. It is the landing page or introduction page or first page to appear to the user.'''

zero()

'''Above: Calls the function zero(). This allows the introduction/landing page to be shown to the user. Then the other pages are called through mostly the Next buttons.'''


#Summative: Evolution of Technology
#Grade 11 Summer School, Computer Science, Ms. Brace.
#Sachin Gupta

#Please view the code/program in repl.it
#the repl.it link: https://replit.com/join/ehzrstdupp-sachin9

#Got some HELP with mainly the Tkinter interface from the following websites:

#The slides provided by you (teacher)
#https://www.python-course.eu/tkinter_buttons.php
#https://www.python-course.eu/tkinter_labels.php
