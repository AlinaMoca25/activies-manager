import datetime
from src.repository import MemoryRepository
from src.domain import Person
from src.domain import Activity


class FileRepository(MemoryRepository):
    def __init__(self, persons, activities):
        super().__init__()
        self.personsFileName = persons
        self.activitiesFileName = activities
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
        file = open(self.personsFileName, 'w')
        file.write("The list of students is: ")
        for person in self.personsList:
            file.write("\n" + str(person))
        file.close()

    def saveActivitiesToFile(self):
        file = open(self.activitiesFileName, 'w')
        file.write("The list of activities is: ")
        for activity in self.activitiesList:
            file.write("\n" + str(activity))
        file.close()

    def readPersonsFromFile(self):
        file = open(self.personsFileName, 'r')
        for line in file:
            if line == "The list of students is:\n":
                pass
            else:
                person = self.convertToPerson(line)
                self.personsList.append(person)
        file.close()
        return self.personsList

    def readActivitiesFromFile(self):
        file = open(self.activitiesFileName, 'r')
        for line in file:
            if line == "The list of activities is:\n":
                pass
            else:
                line.split(",")
                Id = int(line[0])
                day = int(line[1])
                month = int(line[2])
                year = int(line[3])
                date = datetime.date(year, month, day)
                start_time = datetime.time(int(line[4]))
                end_time = datetime.time(int(line[5]))
                time = {"start_time": start_time, "end_time": end_time}
                # participants
                description = line[5]

        file.close()
        return self.activitiesList

    @staticmethod
    def convertToPerson(string):
        string = string.split()
        _id = 0
        name = ""
        phoneNumber = ""
        for index in range(len(string)):
            word = string[index]
            word.strip(",")
            if index == 1:
                _id = int(word)
            elif index == 4:
                name = word
            elif index == 6:
                phoneNumber = word
            else:
                pass
        return Person(_id, name, phoneNumber)

    @staticmethod
    def convertToActivity(string):
        pass
        # it's already split

        # return Activity(_id, date, time, participants, description)
