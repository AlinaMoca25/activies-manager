import unittest
from src.repository import MemoryRepository
from src.domain import Person
from domain import Activity
import datetime


class MyTestCase(unittest.TestCase):

    def test_add_person(self):
        repo = MemoryRepository()

        person = Person(12, "Mara", "9615707513")
        repo.addPerson(12, "Mara", "9615707513")
        self.assertEqual(person.get_id(), repo.personsList[0].get_id())
        self.assertEqual(person.get_name(), repo.personsList[0].get_name())
        self.assertEqual(person.get_number(), repo.personsList[0].get_number())

        try:
            repo.addPerson(12, "bad person", "235")
        except Exception as ex:
            self.assertEqual(str(ex), "Id already exists! Invalid phone number! (should have 10 digits) ")

    def test_add_activity(self):
        repo = MemoryRepository()
        activity = Activity(11, datetime.date(2022, 12, 21), {"start_time": datetime.time(12), "end_time": datetime.time(14)}, None, "desc")
        repo.addActivity(11, datetime.date(2022, 12, 21), {"start_time": datetime.time(12), "end_time": datetime.time(14)}, None, "desc")
        # self.assertEqual(activity, repo.activitiesList[0])
        self.assertEqual(activity.get_id(), repo.activitiesList[0].get_id())
        self.assertEqual(activity.get_date(), repo.activitiesList[0].get_date())
        self.assertEqual(activity.get_time(), repo.activitiesList[0].get_time())
        self.assertEqual(activity.get_participants(), repo.activitiesList[0].get_participants())
        self.assertEqual(activity.get_description(), repo.activitiesList[0].get_description())

        try:
            repo.addActivity(11, datetime.date(2022, 12, 21), {"start_time": datetime.time(13), "end_time": datetime.time(15)}, None, "bad activity")
        except Exception as ex:
            self.assertEqual(str(ex), f"Id already exists! Activity overlaps with activity {activity.get_id()}! ")


if __name__ == '__main__':
    unittest.main()
