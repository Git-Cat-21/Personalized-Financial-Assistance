# Project Setup Guide 

### Prerequisities
Make sure to have Node.js installed on your system. You can download and install it by following the instructions in this video:

[Node js installation](https://www.youtube.com/watch?v=06X51c6WHsQ)

### Clone the Repository 
First, clone the repository to your local machine:
```bash
git clone https://github.com/Git-Cat-21/Personalized-Financial-Assistance.git
cd Personalized-Financial-Assistance
```


### Installation Steps

1.**Install Python Dependencies**
```bash
pip install -r requirements.txt
```

2.**Initialize Node.js and Install Dependencies**
- Initialize your Node.js project (only required once):
    ```bash
    npm init -y
    ```

- Install the required Node.js packages:
    ```bash
    npm install express mysql2 ejs
    ```


### Running the Application

1. Open **two terminals**.

2. In the **first terminal**, start the Node.js service:
```bash
node data_fetch.js
```

3. In the **second terminal**, start the Python application:
```bash
python app.py
```

> This will start the backend services on both Node.js and Python. Keep both terminals open to run the services simultaneously.