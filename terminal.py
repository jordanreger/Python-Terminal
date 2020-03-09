import json, hashlib, os, time, sys

# <login>

def login():
  username = input("Username: ")
  with open('cache.txt', 'w+') as cache:
    cache.write(username)
  file = open(f'{username}.json')
  user_dict = json.load(file)
  username = username.encode('utf-8')
  userhash = hashlib.sha256(username).hexdigest()
  if(userhash == user_dict['username']):
    password = input("Password: ")
    password = password.encode('utf-8')
    passhash = hashlib.sha256(password).hexdigest()
    if(passhash == user_dict['password']):
      print("Logged in...\n")
      time.sleep(0.25)
      clear()
      main()
    else:
      print("Invalid password.")
      time.sleep(1)
      clear()
      menu()
    

def new_user():
  username = input("Username: ")

  if(os.path.exists(f'{username}.json') != True):
    password = input("Password: ")
    if(username != '' and password != ''):
      with open(f'{username}.json', 'w+') as file:
        username = username.encode('utf-8')
        password = password.encode('utf-8')
        userhash = hashlib.sha256(username).hexdigest()
        passhash = hashlib.sha256(password).hexdigest()

        user_json = {
        'username': userhash,
        'password': passhash
        }

        file.write(json.dumps(user_json, indent=4))
        file.close()
  else:
    print("Username taken.")
    time.sleep(1)
    clear()
    menu()

def menu():
  userInput = input("Login or sign up: ")
  if(userInput.lower() == 'login'):
    login()
  elif(userInput.lower() == 'sign up'):
    new_user()

# </login>


# <terminal blocks>

def clear():
    os.system("clear")

def ping():
    os.system("ping " + str(destination))
    main()

def helpme():
    print(""" 
 _____________ 
|             |
|  Commands!  |
|_____________|
|  1)clear    |
|  2)ping     |
|  3)login    |
|  4)cowsay   |
|  5)clear    |
|  6)It-crowd |
|_____________|""")
    print("Press Ctr c to exit")
    main()

def cowsay():
    slash = chr(92)
    print(" ", end = "")
    print("_" * (len(message) + 4))
    print("/", end = "")
    print(" " * (len(message) + 4), end = "")
    print(slash)
    print("| ", message," |")
    print(slash, end = "")
    print("_" * (len(message) + 4), end = "")
    print("/")
    print("        \   ^__^               ")
    print("         \  (00)\_______       ")
    print("            (__)\       )\/\   ")
    print("                ||----W |      ")
    print("                ||     ||      ")
    print("                ``     ``      ")
    main()

def exit_fun():
  sys.exit()


def main():
    file = open('cache.txt', 'r')
    username = file.read()
    user = ("badterminal@" +  str(username))
    definput = str(user) + ":~ $ "
    command = input(definput)
    if command == '':
        main()
    if command == 'cowsay':
        print("cowsay command requires --[quote] or arg --[message] ")
        main()
    if command == 'ping':
        print("ping command requires arg --[destination]")
        main()
    if command == 'cowsay':
        cowsay()
    if command == 'help':
        helpme()
    if command == 'clear':
        clear()
    if command == 'exit':
        exit_fun()
    if command[0:6] == 'cowsay':
        global message
        quotes = ["Be yourself; everyone else is already taken.","Be the change that you wish to see in the world.", "Live as if you were to die tomorrow. Learn as if you were to live forever.", "We are all in the gutter, but some of us are looking at the stars.", "Life isn't about finding yourself. Life is about creating yourself.", "Do what you can, with what you have, where you are.", "A person's a person, no matter how small.", "Happiness is not something ready made. It comes from your own actions.", "Peace begins with a smile.", "Whatever you are, be a good one.", "Two wrongs don't make a right, but they make a good excuse.", "If my life is going to mean anything, I have to live it myself.", "Always do what you are afraid to do.", "Pain is inevitable. Suffering is optional.", "Talent hits a target no one else can hit. Genius hits a target no one else can see.", "Turn your wounds into wisdom."]
        message = command[7::]
        if message == "quote":
            quote = random.choice(quotes)
            message = quote
            cowsay()
        else:
            cowsay()
    if command[0:4] == 'ping':
        global destination
        destination = command[5::]
        ping()
    if command == 'ls':
        ls()
    if command == 'login':
        print()
        login()
    if command == '01189998819991197253':
        print("Congratulations You found the secret!")
        time.sleep(2)
        message = "Jordan, I know this is bad, but it took me a long time."
        cowsay()    

    else:
        print("Not a valid command")
        main()

# </terminal blocks>

menu()
