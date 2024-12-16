# Enhancing security with speech recognition: A voice-based access control

## Overview  
This project implements a **hands-free speech recognition system** that enables users to securely access their confidential data using predefined passphrases. Each user is assigned a unique passphrase that acts as a key to unlock their files. By matching the spoken phrase with the stored passphrase, the system authenticates users and grants access to their data.  

The system includes a user-friendly **Graphical User Interface (GUI)** built with **Tkinter** and leverages **Google’s Recognize_speech API** for converting spoken phrases into text. Additional security measures and error-handling features ensure a seamless and secure user experience.  

## Features  
- **Hands-Free Operation:** Allows users to access their data without the need for typing passwords.  
- **Predefined Passphrases:** Each user has a unique passphrase stored for authentication.  
- **Speech Recognition:** Converts spoken phrases into text using Google's Recognize_speech API.  
- **Graphical User Interface:** A Tkinter-based GUI simplifies interaction and usability.  
- **Enhanced Security Features:**  
  - Limits users to **three failed attempts** before locking access.  
  - Notifies users to restart the process after a predefined waiting period.  
- **Exception Handling:**  
  - Provides clear error messages and guidance to resolve issues like microphone errors, unrecognized phrases, or internet connectivity problems.  

## Workflow  
1. **User Authentication:**  
   - The user speaks their predefined passphrase into the microphone.  
   - The system converts the speech to text and matches it against stored passphrases.  
2. **Access Grant:**  
   - If the passphrase matches, the user is granted access to their files.  
3. **Access Denial:**  
   - If the passphrase doesn’t match after three attempts, the system locks access and instructs the user to restart after a waiting period.  

## Tools and Technologies  
- **Programming Language:** Python  
- **IDE:** Visual Studio  
- **GUI Package:** Tkinter (in-built with Python)  
- **Speech Recognition API:** Google’s Recognize_speech  

## Requirements  
- **Software:**  
  - Python 3.7 or higher  
  - Required Python libraries:  
    ```bash  
    pip install SpeechRecognition tkinter  
    ```  
- **Hardware:**  
  - Microphone for speech input  
  - Computer with internet connectivity (required for the Google API)  

## How to Use  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/Speech-Recognition-System.git  
