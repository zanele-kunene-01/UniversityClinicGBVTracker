# src/simple_factory.py

class Notification:
    def send(self):
        raise NotImplementedError

class EmailNotification(Notification):
    def send(self):
        return "Sending email notification"

class SMSNotification(Notification):
    def send(self):
       return "Sending SMS notification"

class PushNotification(Notification):
    def send(self):
        return "Sending push notification"

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "Email":
            return EmailNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        elif notification_type == "Push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")
            
Factory Method Use Case: Managing different types of user accounts (Student, Clinic Staff, Admin).

# src/factory_method.py

class UserAccount:
    def manage_account(self):
       raise NotImplementedError

class StudentAccount(UserAccount):
    def manage_account(self):
        return "Managing student account"

class ClinicStaffAccount(UserAccount):
    def manage_account(self):
        return "Managing clinic staff account"

class AdminAccount(UserAccount):
    def manage_account(self):
        return "Managing admin account"

class UserAccountFactory:
    def create_account(self, account_type):
        if account_type == "Student":
            return StudentAccount()
        elif account_type == "ClinicStaff":
            return ClinicStaffAccount()
        elif account_type == "Admin":
            return AdminAccount()
        else:
            raise ValueError("Unknown account type")

Abstract Factory Use Case: Creating different types of user interfaces (Web, Mobile).

# src/abstract_factory.py

class Button:
    def render(self):
        raise NotImplementedError
class WebButton(Button):
    def render(self):
        return "Rendering web button"

class MobileButton(Button):
    def render(self):
        return "Rendering mobile button"

class GUIFactory:
    def create_button(self):
        raise NotImplementedError

class WebGUIFactory(GUIFactory):
    def create_button(self):
        return WebButton()

class MobileGUIFactory(GUIFactory):
    def create_button(self):
        return MobileButton()

Builder Use Case: Building a detailed report with optional sections (Summary, Details, Conclusion).

# src/builder.py

class Report:
    def __init__(self):
        self.summary = None
        self.details = None
        self.conclusion = None

class ReportBuilder:
    def __init__(self):
        self.report = Report()
    def add_summary(self, summary):
        self.report.summary = summary
        return self
    def add_details(self, details):
        self.report.details = details
        return self
    def add_conclusion(self, conclusion):
        self.report.conclusion = conclusion
        return self
    def build(self):
        return self.report

Prototype Use Case: Cloning user profiles for testing purposes.

# src/prototype.py

import copy

class UserProfile:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def clone(self):
        return copy.deepcopy(self)

class UserProfileCache:
    def __init__(self):
        self.profiles = {}
    def load_cache(self):
        self.profiles["Admin"] = UserProfile("Admin", "admin@example.com")
        self.profiles["Guest"] = UserProfile("Guest", "guest@example.com")
    def get_profile(self, profile_type):
        return self.profiles[profile_type].clone()

Singleton Use Case: Ensuring a single instance of the database connection.

# src/singleton.py

class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    def connect(self):
        return "Connecting to the database"

**Read me**
### Creational Patterns

- **Simple Factory**: Used to create different types of notifications, demonstrating a centralized object creation strategy.

- **Factory Method**: Implemented for managing different types of user accounts, allowing subclasses to define account management methods.

- **Abstract Factory**: Used for GUI creation, supporting multiple platforms (Web, Mobile).

- **Builder**: Applied to the Report class to handle complex object creation with optional sections.

- **Prototype**: Implemented for user profile cloning, allowing objects to be copied without knowing their exact class.

- **Singleton**: Ensures a single instance of the DatabaseConnection class, providing a global point of access.

        
