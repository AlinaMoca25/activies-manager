import datetime
# from src.repository import MemoryRepository
# from src.repository.fileRepository import FileRepository


class Services:

    def __init__(self, repository):
        self.memoryRepo = repository
        self.memoryRepo.generatePersons()
        self.memoryRepo.generateActivities()

    def addPerson(self, person_id, name, phoneNumber):
        self.memoryRepo.addPerson(person_id, name, phoneNumber)

    def removePerson(self, person_id):
        try:
            person_id = int(person_id)
        except Exception as ex:
            raise Exception(ex)
        else:
            self.memoryRepo.removePerson(person_id)

    def updatePerson(self, person_id, name, phoneNumber):
        try:
            person_id = int(person_id)
        except Exception as ex:
            raise Exception(ex)
        self.memoryRepo.updatePerson(person_id, name, phoneNumber)

    def listOfPersons(self):
        return self.memoryRepo.personsList

    def searchPerson(self, name, phoneNumber):
        searchResults = []
        name = name.lower()
        for person in self.memoryRepo.personsList:
            if name != "":
                personName = person.get_name()
                personName = personName.lower()
                if name in personName:
                    searchResults.append(person)
            elif phoneNumber != "":
                if phoneNumber in person.get_number():
                    searchResults.append(person)
        return searchResults

    def addActivity(self, activity_id, date, time, participants, description):
        self.memoryRepo.addActivity(activity_id, date, time, participants, description)

    def removeActivity(self, activity_id):
        try:
            activity_id = int(activity_id)
        except Exception as ex:
            raise Exception(ex)
        else:
            self.memoryRepo.removeActivity(activity_id)

    def updateActivity(self, activity_id, date, time, participants, description):
        try:
            activity_id = int(activity_id)
        except Exception as ex:
            raise Exception(ex)
        self.memoryRepo.updateActivity(activity_id, date, time, participants, description)

    def listOfActivities(self):
        return self.memoryRepo.activitiesList

    def searchActivity(self, date, time, description):
        searchResults = []
        description = description.lower()
        for activity in self.memoryRepo.activitiesList:
            if date != "":
                if activity.get_date() == date:
                    searchResults.append(activity)
            if time != "":
                start_time = activity.time["start_time"]
                end_time = activity.time["end_time"]
                if start_time <= time <= end_time:
                    searchResults.append(activity)
            if description != "":
                activityDescription = activity.get_description()
                activityDescription = activityDescription.lower()
                if description in activityDescription:
                    searchResults.append(activity)
        return searchResults

    @staticmethod
    def sortListOfActivitiesByStartTime(listOfActivities):
        for activity in range(len(listOfActivities)-1):  # activity = index
            if listOfActivities[activity+1].get_time()["start_time"] < listOfActivities[activity].get_time()["start_time"]:
                listOfActivities[activity+1], listOfActivities[activity] = listOfActivities[activity], listOfActivities[activity+1]
        return listOfActivities

    def activitiesForGivenDate(self, date):
        activitiesFromSearchedDate = []
        for activity in self.memoryRepo.activitiesList:
            if date == activity.get_date():
                activitiesFromSearchedDate.append(activity)
        activitiesFromSearchedDate = self.sortListOfActivitiesByStartTime(activitiesFromSearchedDate)
        return activitiesFromSearchedDate

    @staticmethod
    def sortDaysByFreeTime(toSort):
        for i in range(len(toSort["free_time"])-1):
            for j in range(i+1, len(toSort["free_time"])):
                if toSort["free_time"][j] < toSort["free_time"][i]:
                    toSort["free_time"][j], toSort["free_time"][i] = toSort["free_time"][i], toSort["free_time"][j]
                    toSort["date"][j], toSort["date"][i] = toSort["date"][i], toSort["date"][j]
        return toSort

    def listOfBusiestDays(self):
        busiestDays = {"date": [], "free_time": []}
        for index in range(len(self.memoryRepo.activitiesList)):
            sameDateActivities = self.activitiesForGivenDate(self.memoryRepo.activitiesList[index].get_date())
            busyTime = 0
            for activity in sameDateActivities:
                busyTime += (int(activity.time["end_time"].hour) - int(activity.time["start_time"].hour))
            freeTime = 24 - busyTime
            busiestDays["date"].append(self.memoryRepo.activitiesList[index].get_date())
            busiestDays["free_time"].append(freeTime)
        busiestDays = self.sortDaysByFreeTime(busiestDays)
        busiest_days = busiestDays["date"]
        free_time = busiestDays["free_time"]
        return busiest_days, free_time

    def searchActivitiesWithGivenPersons(self, person_id):
        searchResults = []
        for activity in range(len(self.memoryRepo.activitiesList)):  # activity = index
            if self.memoryRepo.activitiesList[activity].get_date() >= datetime.date.today():
                for person in self.memoryRepo.activitiesList[activity].participants:
                    if person.get_id() == person_id:
                        searchResults.append(self.memoryRepo.activitiesList[activity])
        return searchResults
