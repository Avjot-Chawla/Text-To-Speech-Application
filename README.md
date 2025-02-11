# Text-To-Speech Application

A Python-based **Text-To-Speech (TTS) Application** that utilizes the `pyttsx3` library for speech synthesis and `tkinter` for a user-friendly graphical user interface (GUI). This project allows users to convert text into speech with customization options such as **voice gender selection**, **adjustable speech speed**, and **saving audio as an MP3 file**.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Authors and Acknowledgements](#authors-and-acknowledgements)

## Overview

The **Text-To-Speech Application** provides an efficient and customizable way to **convert text into speech** using Python. It enhances accessibility for users by offering **voice gender options**, **adjustable speed**, and **MP3 file export**. The GUI ensures ease of use, making text-to-speech functionality accessible to everyone.

## Features

- **Text-to-Speech Conversion**: Converts text input into speech.
- **Voice Gender Selection**: Choose between **Male** or **Female** voices.
- **Speech Speed Adjustment**: Options for **Slow, Normal, and Fast** speech.
- **Audio Playback**: Play the generated speech directly from the application.
- **MP3 File Saving**: Save the speech output as an **MP3 file** for later use.
- **User-Friendly GUI**: Simple and intuitive interface using `tkinter`.

## Technologies Used

- **Programming Language**: Python (3.x)
- **Libraries**:
  - `pyttsx3` – Text-to-Speech conversion
  - `tkinter` – Graphical User Interface (GUI)
  - `os` – File handling for saving MP3 files

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/TextToSpeech.git
cd TextToSpeech
```

### 2. Install Dependencies
Ensure you have **Python 3.x** installed, then install the required libraries:
```bash
pip install pyttsx3
```

### 3. Run the Application
```bash
python main.py
```

## Usage

1. **Launch the application** by running `main.py`.
2. **Enter or paste the text** in the provided input box.
3. **Choose voice gender** (Male/Female).
4. **Adjust speech speed** (Slow, Normal, Fast).
5. **Click "Speak"** to play the audio.
6. **Click "Save"** to export the audio as an MP3 file.

## Project Structure

```
TextToSpeech/
├── src/                   # Main source code
│   ├── main.py            # Main application script
│   ├── tts_engine.py      # Handles text-to-speech processing
│   ├── gui.py             # GUI implementation using tkinter
│   ├── file_manager.py    # Manages file saving and directory handling
├── assets/                # Icons, images, and UI assets
│   ├── speaker_logo.png
│   ├── speak.png
│   ├── download.png
├── requirements.txt       # List of required dependencies
├── README.md              # This file
├── LICENSE                # License file
└── .gitignore             # Files to ignore in Git
```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features:
1. Fork the repository.
2. Create a new branch (`feature-improvement`).
3. Make changes and test them.
4. Submit a pull request.

## Authors and Acknowledgements

- **Avjot Singh Chawla** – RA2211003010584
- **Harsh Jaiswal** – RA2211003010580
- **Abhishek Singh** – RA2211003010543
- **Project Supervisor:** Dr. R. Thamizhamuthu  
  *Department of Computing Technologies, SRM Institute of Science and Technology*
