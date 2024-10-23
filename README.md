# Enhancing security with speech recognition: A voice-based access control
This project implements a hands-free speech recognition system that allows users to securely access their confidential data using predefined passphrases. Each user has a unique passphrase, which, when matched with their stored password, grants access to their files.

The system integrates a graphical user interface (GUI) built with Tkinter, and leverages Google’s Recognize_speech API to detect and convert spoken phrases into text. The spoken text is then matched against predefined passphrases to authenticate users.

**Tools and Technologies**<br>
Programming Language: Python<br>
IDE: Visual Studio<br>
GUI Package: Tkinter (in-built with Python)<br>
Speech Recognition API: Google’s Recognize_speech<br>


This project also has added feature like excption handling where errors are handled in a manner where user will get to know how to deal with the problem that they are facing.
The software has a security feature of trying wrong password more then thrice where after continuous failure they are notified to restart the process after predefined time.
