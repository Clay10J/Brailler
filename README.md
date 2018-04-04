## **Brailler**

**Setting up the Raspberry Pi**

 - Install Raspbian using NOOBS
	 - Follow the instructions at: https://projects.raspberrypi.org/en/projects/noobs-install
 - Install Python3
	 - Follow the instructions at: https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f
 - Install Speech2Text Compatability (? means untested at the moment)
	 - Windows
		 - pip3 install SpeechRecognition
		 - pip3 install pyaudio
		 - pip3 install google-api-python-client
	 - MacOS
		 - pip3 install SpeechRecognition
		 - brew install portaudio
		 - pip3 install pyaudio
		 - pip3 install google-api-python-client
	 - Linux
		 - (?)sudo apt-get install SpeechRecognition
		 - sudo apt-get install python-pyaudio python3-pyaudio
		 - (?) sudo apt-get install google-api-python-client
 - Install PDF2Text Compatability
 	 - MacOS
		 - brew install tesseract --all-languages
		 - brew install leptonica
		 - pip3 install tesseract-ocr
 - PyCNC
	 - TODO: ADD THIS PART
 - Download Project Files to Raspberry Pi
	 - TODO: ADD THIS PART
 - Configure Raspberry Pi Bootup to automatically run the project files
	- TODO: ADD THIS PART

