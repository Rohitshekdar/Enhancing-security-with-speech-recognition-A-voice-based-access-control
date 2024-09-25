import speech_recognition as sr
from tkinter import *
import pyttsx3
import os

s = pyttsx3.init()
# Initialize speech recognizer
r = sr.Recognizer()

answer = "Press the Authenticate button to verify yourself"
s.say(answer)
s.runAndWait()

# Initialize user data
users_data = {"Boss": "Rohit", "Teacher": "Vinoda"}
admin_password = "this is the admin"  # Set a password for admin access
incorrect_attempts = 0
max_attempts = 3
def authenticate_user():
    # Record voice command
    with sr.Microphone() as source:
        print("Recording voice command...")
        audio = r.record(source, duration=5)  # Record for 5 seconds

    try:
        # Convert audio to text
        command = r.recognize_google(audio)

        # Perform authentication
        password1 = "this is your boss"
        password2 = "this is teacher"
        exitmessage="please exit"
        # Check if the command matches a registered user's password
        if command in users_data.values():
            user_name = next(name for name, password in users_data.items() if password == command)
            authenticate_user_role(user_name)
            
        # Check if the command is the admin password
        elif command == admin_password:
            authenticate_user_role("Admin")
            
        elif command == password1:
            is_condition_true = True
            filename = "rohit.txt"


            if is_condition_true:
                try:
                    with open(filename, "r") as file:
            # Read the contents of the file
                     contents = file.read()
                     print("The Contents of the File are :\n")
                     print(contents)
                     
                except FileNotFoundError:
                    print(f"File '{filename}' not found")
            authenticate_user_role("Boss")

        elif command == password2:
            is_condition_true = True
            filename = "vinoda.txt"


            if is_condition_true:
                try:
                    with open(filename, "r") as file:
            # Read the contents of the file
                     contents = file.read()
                     print("The Contents of the File are :\n")
                     print(contents)
                     
                except FileNotFoundError:
                    print(f"File '{filename}' not found")
            authenticate_user_role("Teacher")

        elif command==exitmessage:
            is_condition_true=True
            if is_condition_true:
                try:
                    answer="Thank you user for your valuable time. Please visit again!!"
                    s.say(answer)
                    s.runAndWait()      
                    exit()
                except sr.UnknownValueError: 
                    label.config(text="Authentication failed.")
                    s.say("Authentication Failed! Try again")
                    s.runAndWait()   
        else:
            
            
                global incorrect_attempts
            # Display authentication failed message
                incorrect_attempts += 1
                label.config(text="Authentication failed.")
                s.say("Authentication Failed! Try again")
                if incorrect_attempts >= max_attempts:
                    s.say("You have exceeded the maximum number of incorrect attempts. Exiting the program.")
                    s.runAndWait()
                    exit()
                s.runAndWait()
                
                    
    except sr.UnknownValueError:
        # Display unknown speech error message
        label.config(text="Unable to recognize speech.")

    except sr.RequestError as e:
        # Display speech recognition error message
        label.config(text="Could not connect to speech recognition service.")

def authenticate_user_role(user_role):
    # Display authentication success message based on user role
    label.config(text=f"Authentication successful! Welcome {user_role}")
    s.say(f"Authentication successful! Welcome {user_role}")
    s.runAndWait()


    # Check if the user is an admin
    if user_role == "Admin":
        # Show the "Show Registered Users" button
        show_users_button.pack()
        show_registered_users()

    else:
        # Hide the "Show Registered Users" button for regular users
        show_users_button.pack_forget()

def show_registered_users():
    # Create a new window to display registered users
    registered_users_window = Toplevel(root)
    registered_users_window.title("Registered Users")

    # Display the registered users
    for role, name in users_data.items():
        user_label = Label(registered_users_window, text=f"{role}: {name}")
        user_label.pack()

def register_new_user():
    # Create a new window for user registration
    register_window = Toplevel(root)
    register_window.title("Register New User")

    # Function to get voice input for registration
    def get_voice_input(prompt):
        s.say(prompt)
        s.runAndWait()

        with sr.Microphone() as source:
            print(f"Recording {prompt}...")
            audio = r.record(source, duration=5)  # Record for 5 seconds

        try:
            # Convert audio to text
            input_text = r.recognize_google(audio)
            return input_text

        except sr.UnknownValueError:
            print(f"Unable to recognize {prompt}.")
            return None

    # Get user's name
    user_name = get_voice_input("Please say your name.")
    if user_name:
        name_label = Label(register_window, text=f"Name: {user_name}")
        name_label.pack()

    # Get user's password
    user_password = get_voice_input("Please say your password.")
    if user_password:
        password_label = Label(register_window, text="Password: ********")
        password_label.pack()

        # Update user_data with the new user
        users_data[user_name.capitalize()] = user_password  # Assuming user name is unique

# Create Tkinter window
root = Tk()
root.geometry("500x500+450+150")
root.title("Speech-Based Authentication")
root.configure(bg="grey")

# Create label for authentication result
label = Label(root, text="Please speak the unlock command.")
label.pack()

# Checkbox to select user role
admin_checkbox_var = IntVar()
admin_checkbox = Checkbutton(root, text="Admin", variable=admin_checkbox_var)
admin_checkbox.pack()

# Create button to initiate authentication
authenticate_button = Button(root, text="Authenticate", command=authenticate_user)

authenticate_button.pack()
authenticate_button.place(x=210,y=85)
# Create button to show registered users
show_users_button = Button(root, text="Show Registered Users", command=show_registered_users)
# Initially hide the "Show Registered Users" button

show_users_button.pack()
show_users_button.place(x=185,y=200)
# Create button to register new user
register_button = Button(root, text="Register New User", command=register_new_user)

register_button.pack()
register_button.place(x=195,y=150)


root.mainloop()
