Schedule Management System
This is a straightforward command-line interface (CLI) application designed to help you manage your daily schedules. You can easily add new tasks, view all your existing schedules, and mark specific tasks as complete. The application stores all schedule data in a MySQL database.

Features
Add Schedule: Quickly input new schedules with a title, description, and start/end dates.

View Schedules: See a clear list of all your schedules, including their completion status and details.

Complete Schedule: Mark any task as finished with a simple command.

Prerequisites
Before running this application, make sure you have the following installed on your system:

Python 3: This application is written in Python.

MySQL Database: You'll need a running MySQL server.

PyMySQL: This is the Python library that enables your application to connect with MySQL.

Setup
Follow these steps to get your schedule management system up and running:

1. Database Configuration
First, set up your schedule_db database and the schedules table within your MySQL server. Open your MySQL client and run these commands:
