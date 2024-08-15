# Bursary Management System

## Overview

The Bursary Management System is a Django-based web application designed to streamline the process of managing and distributing bursaries or scholarships. It provides an interface for students to apply for bursaries, allows administrators to review applications, and tracks disbursements. The system ensures transparency and efficiency in the entire bursary management process.

## Features

- **User Roles and Authentication:**
  - Student, Admin, and Reviewer roles with distinct privileges.
  - User registration and login functionality.

- **Student Features:**
  - Bursary application submission with necessary documentation.
  - View application status and receive notifications.
  - Update personal information.

- **Admin Features:**
  - Manage bursary programs (create, update, delete).
  - Review and approve/reject bursary applications.
  - Generate reports and manage disbursements.

- **Reviewer Features:**
  - Review applications and provide recommendations.

- **Application Tracking and Notifications:**
  - Track the status of bursary applications.
  - Automated email notifications for application status updates.

- **Reports and Analytics:**
  - Generate reports on bursary disbursement, applicant demographics, and more.

## Prerequisites

To run this project locally, you need the following installed on your system:

- Python 3.x
- Django 4.x
- SQLite (default database for development)
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/bursary-management-system.git
    cd bursary-management-system
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. Access the application in your browser at `http://127.0.0.1:8000/`.

## Project Structure

```
bursary_management_system/
├── bus/                   # Main Bursary logic (App)
├── core/                  # System Entry Point
├── main/                  # System Links
├── std/                   # Main Application Logic (App)
├── users/                 # Main User Logic (App)
├── static/                # Static files (CSS, JS, images)
├── media/                 # Uploaded files (e.g., application documents)
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database (for development)
└── requirements.txt       # List of dependencies
```

## How to Contribute

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For more information or to report issues, please contact:

- **Email:** georgesroberto21@gmail.com
- **WhatsApp:** [Georges](https://wa.me/+254796807438)

---

Happy Coding! 🎓
