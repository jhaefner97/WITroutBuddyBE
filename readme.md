# Fish Assist Weather API

## Requirements  
 - Python 3.10+ (Preferably 3.11+)
 - Requirements outlined in requirements.txt
 - Have .env file in directory
   - accu_weather_key={APIKEY}

## How to run
 - Clone repo to local machine
 - Open terminal in app directory
 - Windows
   - Ensure proper python version is installed (python --version)
   - Create python virtual environment
     - python -m venv venv
   - Activate virtual environment 
     - type ./venv/scripts/activate
   - Install dependencies
     - type pip install -r requirements.txt
   - Make sure .env file contains api key
   - Activate uvicorn web server
     - uvicorn main:app --reload
   - Go to localhost in browser port 8000
   - Have fun
 - Mac/Linux
   - Ensure proper python version is installed (python3 --version)
   - Create python virtual environment
     - python3 -m venv venv
   - Activate virtual environment
     - source ./venv/scripts/activate
   - Install dependencies
     - pip install -r requirements.txt
   - Make sure .env file contains api key
   - Activate uvicorn web server
     - uvicorn main:app --reload
   - Go to localhost in browser port 8000
   - Have fun 