import random
import datetime
from src.domain import Person
from src.domain import Activity


class MemoryRepository:

    def __init__(self):
        self.personsList = []
        self.activitiesList = []

    def generatePersons(self):
        nameList = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Charlotte", "James", "Amelia",
                    "Elijah", "Sophia", "William", "Isabella", "Henry", "Ava", "Lucas", "Mia",
                    "Benjamin", "Evelyn", "Theo", "Luna"]
        digits = "0123456789"
        index = 0
        while index < 20:
            Id = random.randrange(1000, 1100)
            found = 0
            for p in self.personsList:
                if p.get_id() == Id:
                    found = 1
            if found == 0:
                name = random.choice(nameList)
                phoneNumber = ""
                for i in range(10):
                    digit = random.choice(digits)
                    phoneNumber = phoneNumber + digit
                person = Person(Id, name, phoneNumber)
                self.personsList.append(person)
            else:
                index -= 1
            index += 1

    def generateActivities(self):
        descriptionList = ["game night", "workout", "personal project", "volunteering", "work", "walk", "birthday", "holiday"]
        index = 0
        while index < 20:
            Id = random.randrange(100)
            found = 0
            for a in self.activitiesList:
                if a.get_id() == Id:
                    found = 1
            if found == 0:
                year = random.randrange(2024, 2030)
                month = random.randrange(1, 12)
                if month == 2:
                    day = random.randrange(1, 28)
                elif month in (1,3,5,7,8,10,12):
                    day = random.randrange(1, 31)
                else:
                    day = random.randrange(1, 30)
                date = datetime.date(year, month, day)
                hour = random.randrange(0, 23)
                start_time = datetime.time(hour)
                end_hour = random.randrange(0, 23)
                while end_hour <= hour:
                    end_hour = random.randrange(0, 23)
                end_time = datetime.time(end_hour)
                time = {"start_time": start_time, "end_time": end_time}
                participants = []
                numberOfParticipants = random.randrange(20)
                for person in range(numberOfParticipants):
                    participant = random.choice(self.personsList)
                    if participant not in participants:
                        participants.append(participant)
                description = random.choice(descriptionList)
                activity = Activity(Id, date, time, participants, description)
                self.activitiesList.append(activity)
            else:
                index -= 1
            index += 1

    def validatePerson(self, person_id, name, phoneNumber):
        errors = ""
        try:
            person_id = int(person_id)
        except Exception as ex:
            errors = errors + str(ex) + " "
        for person in self.personsList:
            if person_id == person.get_id():
                errors = errors + "Id already exists! "
        if len(phoneNumber) != 10:
            errors += "Invalid phone number! (should have 10 digits) "
        if errors != "":
            raise Exception(errors)
        else:
            person = Person(person_id, name, phoneNumber)
            return person

    @staticmethod
    def validateExistingPerson(person_id, name, phoneNumber):
        errors = ""
        try:
            person_id = int(person_id)
        except Exception as ex:
            errors = errors + str(ex) + " "
        if len(phoneNumber) != 10:
            errors += "Invalid phone number! (should have 10 digits) "
        if errors != "":
            raise Exception(errors)
        else:
            person = Person(person_id, name, phoneNumber)
            return person

    def validateParticipants(self, participants, errors):
        idsList = []
        for person in self.personsList:
            idsList.append(person.get_id())
        participants = participants.strip()
        participants = participants.split()
        for participant in participants:
            participant = participant.strip(",")
            try:
                person_id = int(participant)
            except Exception as ex:
                errors += str(ex) + " "
            else:
                if person_id not in idsList:
                    errors += f"Participant {participant.get_id()} is not registered. "

    def validateActivity(self, activity_id, date, time, participants, description):
        errors = ""
        if participants is None:
            participants = ""
        try:
            activity_id = int(activity_id)
        except Exception as ex:
            errors = errors + str(ex) + " "
        # convert day and time to the necessary types (from ui!)?

        for activity in self.activitiesList:
            if activity_id == activity.get_id():
                errors = errors + "Id already exists! "
            if date == activity.get_date():
                if activity.time["end_time"] > time["start_time"]:
                    errors += f"Activity overlaps with activity {activity.get_id()}! "
            self.validateParticipants(participants, errors)
        # if type(participants) != list:
            # errors += "Participants should be a list. "
        if errors != "":
            raise Exception(errors)
        else:
            activity = Activity(activity_id, date, time, participants, description)
            return activity

    def validateExistingActivity(self, activity_id, date, time, participants, description):
        errors = ""
        if participants is None:
            participants = ""
        try:
            activity_id = int(activity_id)
        except Exception as ex:
            errors = errors + str(ex) + " "
        self.validateParticipants(participants, errors)
        # if type(participants) != list:
            # errors += "Participants should be a list. "
        if errors != "":
            raise Exception(errors)
        else:
            activity = Activity(activity_id, date, time, participants, description)
            return activity

    def addPerson(self, person_id, name, phoneNumber):
        try:
            person = self.validatePerson(person_id, name, phoneNumber)
        except Exception as ex:
            raise Exception(ex)
        else:
            self.personsList.append(person)

    def removePerson(self, person_id):
        found = 0
        for person in self.personsList:
            if person_id == person.get_id():
                self.personsList.remove(person)
                found = 1
                break
        if found == 0:
            raise Exception("Person not found!")

    def updatePerson(self, person_id, name, phoneNumber):
        found = 0
        for person in range(len(self.personsList)):  # person = index
            if person_id == self.personsList[person].get_id():
                found = 1
                if name == "":
                    name = self.personsList[person].get_name()
                if phoneNumber == "":
                    phoneNumber = self.personsList[person].get_number()
                try:
                    updatedPerson = self.validateExistingPerson(person_id, name, phoneNumber)
                except Exception as ex:
                    raise Exception(ex)
                else:
                    self.personsList.append(updatedPerson)
        if found == 0:
            raise Exception("Person not found!")

    def addActivity(self, activity_id, date, time, participants, description):
        try:
            activity = self.validateActivity(activity_id, date, time, participants, description)
        except Exception as ex:
            raise Exception(ex)
        else:
            self.activitiesList.append(activity)

    def removeActivity(self, activity_id):
        found = 0
        for activity in self.activitiesList:
            if activity.get_id() == activity_id:
                self.activitiesList.remove(activity)
                found = 1
        if found == 0:
            raise Exception("Activity not found!")

    def updateActivity(self, activity_id, date, time, persons, description):
        found = 0
        for activity in range(len(self.activitiesList)):  # activity = index
            if self.activitiesList[activity].get_id() == activity_id:
                found = 1
                try:
                    updatedActivity = self.validateExistingActivity(activity_id, date, time, persons, description)
                except Exception as ex:
                    raise Exception(ex)
                else:
                    self.activitiesList.append(updatedActivity)
        if found == 0:
            raise Exception("Activity not found!")

