# Blood-Donation-Database-Project
Purpose:
This project aims to create an organized blood management database in order to efficiently retrieve donor information and requests.

## Features
- Register and manage blood donors
- Record blood donations
- Handle and track blood requests
- Search donors by blood group
- Dashboard showing donor and request statistics

## Architecture

```text
blood_donation_manager/
│
├── app.py
├── blood_bank.db
│
├── templates/
│   ├── add_donor.html
│   ├── index.html
│   ├── record_donation.html
│   ├── make_request.html
│   └── search.html
│
└── static/
    └── style.css
```

## Tools
- **Frontend:** HTML, CSS (Flask templates, static assets)
- **Backend:** Python (Flask framework)
- **Database:** SQLite
- **Server:** Flask built-in development server

## Deployment & Setup
```text
Install Dependencies: 
pip install flask\

Run the app:
python app.py

You will see an output like:
Running on http://127.0.0.1:5000

Now open the browser and navigate to:
http://127.0.0.1:5000
```
