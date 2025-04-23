Example Unit Test for Simple Factory Pattern in Python

# tests/test_simple_factory.py

import unittest

from simple_factory import NotificationFactory

class TestSimpleFactory(unittest.TestCase):

    def test_create_email_notification(self):

        notification = NotificationFactory.create_notification("Email")

        self.assertEqual(notification.send(), "Sending email notification")

    def test_create_sms_notification(self):

        notification = NotificationFactory.create_notification("SMS")

        self.assertEqual(notification.send(), "Sending SMS notification")

    def test_create_push_notification(self):

        notification = NotificationFactory.create_notification("Push")

        self.assertEqual(notification.send(), "Sending push notification")

    def test_invalid_notification_type(self):

        with self.assertRaises(ValueError):

            NotificationFactory.create_notification("InvalidType")


if __name__ == '__main__':

    unittest.main()

Example Unit Test for Factory Method Pattern in Python

# tests/test_factory_method.py

import unittest

from factory_method import UserAccountFactory

class TestFactoryMethod(unittest.TestCase):

    def test_create_student_account(self):

        account = UserAccountFactory().create_account("Student")

        self.assertEqual(account.manage_account(), "Managing student account")


    def test_create_clinic_staff_account(self):

        account = UserAccountFactory().create_account("ClinicStaff")

        self.assertEqual(account.manage_account(), "Managing clinic staff account")


    def test_create_admin_account(self):

        account = UserAccountFactory().create_account("Admin")

        self.assertEqual(account.manage_account(), "Managing admin account")


    def test_invalid_account_type(self):

        with self.assertRaises(ValueError):

            UserAccountFactory().create_account("InvalidType")


if __name__ == '__main__':

    unittest.main()

Example Unit Test for Abstract Factory Pattern in Python

# tests/test_abstract_factory.py

import unittest

from abstract_factory import WebGUIFactory, MobileGUIFactory


class TestAbstractFactory(unittest.TestCase):

    def test_create_web_button(self):

        factory = WebGUIFactory()

        button = factory.create_button()

        self.assertEqual(button.render(), "Rendering web button")


    def test_create_mobile_button(self):

        factory = MobileGUIFactory()

        button = factory.create_button()

        self.assertEqual(button.render(), "Rendering mobile button")

if __name__ == '__main__':

    unittest.main()

Example Unit Test for Builder Pattern in Python

# tests/test_builder.py

import unittest

from builder import ReportBuilder

class TestBuilder(unittest.TestCase):

    def test_build_report_with_all_sections(self):

        builder = ReportBuilder()

        report = builder.add_summary("Summary").add_details("Details").add_conclusion("Conclusion").build()

        self.assertEqual(report.summary, "Summary")

        self.assertEqual(report.details, "Details")

        self.assertEqual(report.conclusion, "Conclusion")

    def test_build_report_with_partial_sections(self):

        builder = ReportBuilder()

        report = builder.add_summary("Summary").add_details("Details").build()

        self.assertEqual(report.summary, "Summary")

        self.assertEqual(report.details, "Details")

        self.assertIsNone(report.conclusion)

if __name__ == '__main__':

    unittest.main()

Example Unit Test for Prototype Pattern in Python

# tests/test_prototype.py

import unittest

from prototype import UserProfileCache

class TestPrototype(unittest.TestCase):

    def test_clone_user_profile(self):

        cache = UserProfileCache()

        cache.load_cache()

        admin_profile = cache.get_profile("Admin")

        self.assertEqual(admin_profile.name, "Admin")

        self.assertEqual(admin_profile.email, "admin@example.com")

    def test_clone_guest_profile(self):

        cache = UserProfileCache()

        cache.load_cache()

        guest_profile = cache.get_profile("Guest")

        self.assertEqual(guest_profile.name, "Guest")

        self.assertEqual(guest_profile.email, "guest@example.com")

if __name__ == '__main__':

    unittest.main()

Example Unit Test for Singleton Pattern in Python

# tests/test_singleton.py

import unittest

from singleton import DatabaseConnection

class TestSingleton(unittest.TestCase):

    def test_singleton_instance(self):

        instance1 = DatabaseConnection()

        instance2 = DatabaseConnection()

        self.assertIs(instance1, instance2)

    def test_database_connection(self):

        instance = DatabaseConnection()

        self.assertEqual(instance.connect(), "Connecting to the database")

if __name__ == '__main__':

    unittest.main()
