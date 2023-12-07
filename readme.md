# Minuscule Agent Server

## Introduction
Welcome to the *Minuscule Agent Server* repository! This Flask server is designed to work with the *[Minuscule Agent](https://github.com/ImiPataki/minuscule_agent)*.
It contains the API documentations and handles the API calls. 3rd party API calls should be made through this server as
that would help to organize the code and make the agent more efficient by removing the unnecessary elements from the
API responses, processing and reformatting them if necessary.

## To read the full description of the framework please visit the following link: [Minuscule Agent](https://joinsingularity.beehiiv.com/p/automate-your-job)

## Installation

Follow these steps to install and run the server:

### Prerequisites
- Ensure you have Python installed on your machine, I used Python 3.11 but should work with older versions as well.
- Git for cloning the repository.

### Cloning the Repository
First, clone the repository into a folder named "agent":
```
git clone https://github.com/ImiPataki/minuscule_agent_server.git agent_server
```
### Setting Up the Environment
Navigate to the cloned directory and set up a virtual environment:

1. Open your command prompt or terminal.
2. Navigate to the `agent_server` folder:
```
cd agent_server
```
3. Create a virtual environment:
```
python -m venv venv
 ```
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate.bat
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

### Installing Dependencies
Install all the required packages:
```
pip install -r requirements.txt
```

## Usage
After installation, you can start the server by running:
```
python -m flask run --with-threads
```
Now you can start using the Minuscule Agent by running the `main.py` file in the `minuscule_agent` repository.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.



