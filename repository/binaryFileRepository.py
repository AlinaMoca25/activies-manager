import pickle
from src.repository import MemoryRepository
from src.domain import Person
from src.domain import Activity


class BinaryFileRepository(MemoryRepository):
    def __init__(self, persons, activities):
        super().__init__()
        self.pickler = Pickler(persons, activities)
        # self.readPersonsFromFile()
        # self.readActivitiesFromFile()

    def generatePersons(self):
        super().generatePersons()
        self.savePersonsToFile()

    def generateActivities(self):
        super().generateActivities()
        self.saveActivitiesToFile()

    def addPerson(self, person_id, name, phoneNumber):
        super().addPerson(person_id, name, phoneNumber)
        self.savePersonsToFile()

    def addActivity(self, activity_id, date, time, participants, description):
        super().addActivity(activity_id, date, time, participants, description)
        self.saveActivitiesToFile()

    def removePerson(self, personID):
        super().removePerson(personID)
        self.savePersonsToFile()

    def removeActivity(self, activityID):
        super().removeActivity(activityID)
        self.saveActivitiesToFile()

    def updatePerson(self, person_id, name, phoneNumber):
        super().updatePerson(person_id, name, phoneNumber)
        self.savePersonsToFile()

    def updateActivity(self, activity_id, date, time, persons, description):
        super().updateActivity(activity_id, date, time, persons, description)
        self.saveActivitiesToFile()

    def savePersonsToFile(self):
        for person in self.personsList:
            self.pickler.dumpPersons(person)

    def saveActivitiesToFile(self):
        for activity in self.activitiesList:
            self.pickler.dumpActivities(activity)


class Pickler:
    def __init__(self, persons, activities):
        self.personsFile = persons
        self.activitiesFile = activities

    def dumpPersons(self, Object):
        with open(self.personsFile, "wb") as file:
            pickle.dump(Object, file)

    def dumpActivities(self, Object):
        with open(self.activitiesFile, "wb") as file:
            pickle.dump(Object, file)

    """def load(self):
        objectList = []
        with open(self.File, "rb") as file:
            try:
                while True:
                    Object = pickle.load(file)
                    objectList.append(Object)
            except EOFError:
                pass
        return objectList"""