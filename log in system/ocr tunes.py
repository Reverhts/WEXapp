import time, csv, hashlib

song_library=[["Flowers", "Miley Cyrus", "Pop", int(200)],["Kill Bill", "SZA", "Pop", int(155)], ["Creepin'", "Metro Boomin", "Pop", int(221)], ["Starlight", "Dave", "Rap", int(212)],["OMG", "NewJeans", "Kpop", int(212)], ["I wanna be yours", "Arctic Monkeys", "Indie", int(183)],["Rich Flex", "Drake", "Rap", int(239)],["Lose Yourself", "Eminem", "Hip Hop", int(328)],["As it was", "Harry Styles", "Pop", int(120)],["Bad Habits", "Ed Sheeran", "Pop", int(233)],["Heat Waves", "Hose", "Blues", int(240)],["Save your tears", "Ariana Grande", "Pop", int(192)], ["Stuck with U", "Justin Bieber", "Pop", int(220)],["Bones", "Imagine Dragons", "Rock", int(226)], ["Under the Influence", "Chris Brown", "R&B", int(180)],["Just Wanna Rock", "Lil Uzi Vert", "Hip Hop", int(232)],["Starboy", "The Weeknd", "Pop", int(230)],["Snooze", "SZA", "Soul", int(192)],["Anti-Hero", "Taylor Swift", "Pop", int(200)],["Here with me", "d4vd", "Pop", int(242)]]

sorted_songs = sorted(song_library, key=lambda x: x[0])
print(sorted_songs)
''''
login_array = []

def read_csv():
    file = open("log in system\\OCRlogin.csv", "r")
    file_reader=csv.reader(file)
    
    for row in file_reader:
        login_array.append(row)
    file.close()

def csv_create():
    file=open("log in system\\OCRlogin.csv", "w",newline="")
    csv_writer=csv.writer(file)
    for i in login_array:
        csv_writer.writerow(i)
    file.close()

def login(username, password):

    username_flag = False
    hash=hashlib.md5(password.encode())
    password=hash.hexdigest()

    for i in range(len(login_array)):

        if username == login_array[i][0]:
            print("Username found")
            username_flag = True
            if password==login_array[i][1]:
                print("Welcome",username)
                return True
            else:
                print("Password incorrect")
                timer=10
                counter=1
                while password!=login_array[i][1]:
                    counter+=1
                    if counter>2:
                        print("You are locked out for ",timer,"seconds")
                        time.sleep(timer)
                        timer=timer*2
                    password=input("Password: ")
                    hash=hashlib.md5(password.encode())
                    password=hash.hexdigest()
                return True

                    
        #stop looping when password founf
    if username_flag==False:
        print("Username not found")
        return False
    
    return False

def create_account():
    flag=False       
    username=input("Please enter a unique username: ")
    
    for i in range(len(login_array)):
        if username.upper()==login_array[i][0].upper():
            print("Username is already taken")
            flag=True
    
    if flag==False:
        print("Username accepted")
        password=input("Please enter a password: ")
        while len(password)<8:
            print("Please use a minimum of 8 characters")
            password=input("Please enter a password: ")
        
        hash=hashlib.md5(password.encode())
        password=hash.hexdigest()

        dob = input("Enter your date of birth: ")
        fav_artist = input("Enter your favourite artist: ")
        fav_genre = input("Enter your favourite genre: ")

        temp=[username,password,dob,fav_artist,fav_genre]
        login_array.append(temp)

        file = open("log in system\\OCRlogin.csv", "a", newline="")
        csv_writer=csv.writer(file)
        csv_writer.writerow(temp)
        file.close()

    else:
        create_account()

def menu():
    print("***** Welcome to the OCRTunes Login system *****")
    print()
    print(" 1) Login \n 2) Create Account")
    #change account details
    pick=input("...")

    if pick=="1":
        flag=False
        while flag==False:
            username = input("Username: ")
            password = input("Password: ")

            flag = login(username, password)
    
    if pick=="2":
        create_account()

read_csv()

menu()

flag=False

while flag==False:


    username = input("Username: ")
    password = input("Password: ")

    flag = login(username, password)

'''

#def create_playlist():
    