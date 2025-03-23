# Car Dealership Management System

The Car Dealership Management System is designed to streamline the operations of a car dealership by providing tools for inventory management, customer relationship management, and employee administration. The system aims to improve efficiency, enhance customer service, and provide valuable insights of every car dealer through sentiment analysis of reviews given by customers.

## Features

- User Authentication
- Dealership Information
- Review System
- User-friendly Interface
- Admin Functionality
- Data Management

## Installation

To set up this project locally, follow these steps:

### Clone the repository
```sh
git clone https://github.com/milantony05/car-dealership.git
```

### Navigate to the project directory
```sh
cd car-dealership/server
```

### Run the Express-MongoDB server (server-side)
```sh
cd car-dealership/server/database
docker build . -t nodeapp
docker-compose up
```
Keep the server running in this terminal.
Launch the application on [Port 3030](http://localhost:3030/) to obtain the URL.<br>
Open `djangoapp/.env` and paste the link beside `backend_url`.

### Start the Code Engine for sentiment analysis
Code Engine Projects are provided by IBM Skills Network.
```sh
cd car-dealership/server/djangoapp/microservices
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
```
Connect to the URL that is generated and copy the url.<br>
Open `djangoapp/.env` and paste the link beside `sentiment_analyzer_url`.

### Build the client-side
```sh
cd car-dealership/server/frontend
npm install
npm run build
```

### Environment setup (Django server)
```sh
cd car-dealership/server
pip install virtualenv
python3 -m venv djangoenv
source djangoenv/bin/activate  # On Windows use `djangoenv\Scripts\activate`
python3 -m pip install -U -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Usage

After setup, access the website through [Port 8000](http://localhost:8000/).<br>
To access the admin site after creating superuser, append `/admin` to the url.

## Tech Stack

This project is built with the following technologies:
- **Frontend:** HTML, CSS, React.js
- **Backend:** Django (Python), Express.js (Node.js)
- **Database:** SQLite (for car model and make), MongoDB (for dealers and reviews)
- **Microservices:**  
  - **Django Proxy Service** (to interact with the dealerships and reviews service)
  - **Express Mongo Service** (running in a Docker container)
  - **Sentiment Analyzer Service** (deployed on IBM Cloud Code Engine)
- **Containerization & Deployment:** Docker, Kubernetes
- **CI/CD:** GitHub Actions, Cloud IDE

## System Requirements

- **Operating System:** Windows 10/11, macOS, or Linux
- **Web Browser:** Chrome, Firefox, Safari, or Edge (latest versions)
- **Backend:** Python 3.8+ (for Django), Node.js 14+ (for Express.js)
- **Database:** SQLite (for car model and make), MongoDB 4.0+ (for dealers and reviews)
- **Containerization & Deployment:** Docker, Kubernetes
- **Cloud Services:** IBM Cloud Code Engine (for sentiment analysis service)
- **Development Tools:** Git, Cloud IDE (for project setup and deployment)

## Gallery

![1](https://github.com/user-attachments/assets/42f67dc1-fcbc-4536-a640-4ffbe9e2cbfd)

![2](https://github.com/user-attachments/assets/1b589b83-0edc-4a85-98fe-b5fd6ebe883c)

![3](https://github.com/user-attachments/assets/33912f36-bb0a-47f8-b59c-45ce9e917a44)

![4](https://github.com/user-attachments/assets/c8769a88-ec40-44ef-b250-103d1b42a2a1)

![5](https://github.com/user-attachments/assets/0f81f5ff-6194-4098-8297-05d44eecec1c)

![6](https://github.com/user-attachments/assets/54e87996-7c40-45d5-9e25-f0fd099a925a)

![7](https://github.com/user-attachments/assets/8fa61f0b-11a0-4617-86e8-6c5ef84c2602)

## Contact

**Milan Tony** - milantony2005@gmail.com
