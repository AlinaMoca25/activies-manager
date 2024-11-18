import datetime
import configparser
from src.repository import MemoryRepository
from src.repository.fileRepository import FileRepository
from src.repository.binaryFileRepository import BinaryFileRepository
from src.services import Services


class Console:

    def __init__(self, repository):
        self.services = Services(repository)

    def addPerson(self):
        print("Please enter the following data about the person: ")
        _id = input("Person id: ")
        name = input("Name: ")
        group = input("Phone number: ")
        self.services.addPerson(_id, name, group)
        print(f"Person {_id} added.")

    def addActivity(self):
        # data validation here?
        print("Please enter the following data about the activity: ")
        _id = input("Activity id: ")
        day = int(input("Date: day: "))
        month = int(input("month: "))
        year = int(input("year: "))
        try:
            date = datetime.date(year, month, day)
        except Exception as ex:
            print(ex)
        start_time = datetime.time(int(input("Time: start time: ")))
        end_time = datetime.time(int(input("end time: ")))
        time = {"start_time": start_time, "end_time": end_time}
        participants = input("Participants: ")
        description = input("Description: ")
        self.services.addActivity(_id, date, time, participants, description)
        print(f"Activity {_id} added.")

    def listPersons(self):
        personsList = self.services.listOfPersons()
        if len(personsList) > 0:
            for person in personsList:
                print(str(person))
        else:
            print("There are no persons registered.")

    def listActivities(self):
        activitiesList = self.services.listOfActivities()
        if len(activitiesList) > 0:
            for activity in activitiesList:
                print(str(activity))
        else:
            print("There are no activities registered.")

    def removePerson(self):
        person_id = input("Please enter the id of the person you want to remove: ")
        self.services.removePerson(person_id)
        print(f"Person {person_id} removed.")

    def removeActivity(self):
        activity_id = input("Please enter the id of the activity you want to remove: ")
        self.services.removeActivity(activity_id)
        print(f"Activity {activity_id} removed.")

    def updatePerson(self):
        person_id = input("Please enter the id of the person you want to update: ")
        name = input("Enter the new name (press enter if you don't want to update it): ")
        phoneNumber = input("Enter the new phone number (press enter if you don't want to update it): ")
        self.services.updatePerson(person_id, name, phoneNumber)
        print(f"Person {person_id} updated. ")

    def updateActivity(self):
        activity_id = input("Please enter the id of the activity you want to update: ")
        day = input("Please enter the new date of the activity: day: ")
        month = input("month: ")
        year = input("year: ")
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            date = datetime.date(year, month, day)
        except Exception as ex:
            print(ex)
        start_hour = input("Please enter the time of the activity: start hour: ")
        end_hour = input("end hour: ")
        try:
            start_hour = int(start_hour)
            end_hour = int(end_hour)
            time = {"start_time": datetime.time(start_hour), "end_time": datetime.time(end_hour)}  # correct here?
        except Exception as ex:
            print(ex)
        participants = input("Please enter the new list of participants: ")
        description = input("Please enter the new description: ")
        self.services.updateActivity(activity_id, date, time, participants, description)
        print(f"Activity {activity_id} updated. ")

    def searchPerson(self):
        searchResults = []
        criteria = input("Do you want to search the person by name or phone number? ")
        if criteria == "name":
            name = input("Please enter the (partial) name you want to search: ")
            searchResults = self.services.searchPerson(name, "")
        elif criteria == "phone number":
            phoneNumber = input("Please enter the (partial) number you want to search: ")
            searchResults = self.services.searchPerson("", phoneNumber)
        else:
            print("Please enter <<name>> or <<phone number>>. ")
        if len(searchResults) > 0:
            print("The following persons match what you searched for: ")
            for person in searchResults:
                print(str(person))
        else:
            print("No such persons found! ")

    def searchActivity(self):
        searchResults = []
        criteria = input("Do you want to search the activity by date, time or description? ")
        if criteria == "date":
            day = input("Please enter the date you want to search by: day: ")
            month = input("month: ")
            year = input("year: ")
            try:
                day = int(day)
                month = int(month)
                year = int(year)
                date = datetime.date(year, month, day)
            except Exception as ex:
                print(ex)
            else:
                searchResults = self.services.searchActivity(date, "", "")
        elif criteria == "time":
            hour = input("Please enter the hour you want to search by: ")
            try:
                hour = int(hour)
                time = datetime.time(hour)
            except Exception as ex:
                print(ex)
            else:
                searchResults = self.services.searchActivity("", time, "")
        elif criteria == "description":
            description = input("Please enter the (partial) description you want to search by: ")
            searchResults = self.services.searchActivity("", "", description)
        else:
            print("Please enter <<date>>, <<time>> or <<description>>. ")
        if len(searchResults) > 0:
            print("The following activities match what you searched for: ")
            for activity in searchResults:
                print(str(activity))
        else:
            print("No such activities found! ")

    def listActivitiesFromGivenDay(self):
        searchResults = []
        day = input("Please enter the date you want to search by: day: ")
        month = input("month: ")
        year = input("year: ")
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            date = datetime.date(year, month, day)
        except Exception as ex:
            print(ex)
        else:
            searchResults = self.services.activitiesForGivenDate(date)
        if len(searchResults) > 0:
            print("The following activities match what you searched for: ")
            for activity in searchResults:
                print(str(activity))
        else:
            print(f"No activities from {date} found! ")

    def displayBusiestDays(self):
        busiest_days, free_time = self.services.listOfBusiestDays()
        for i in range(len(busiest_days)):
            print("Date: " + str(busiest_days[i]) + " with free time: " + str(free_time[i]))

    def searchActivitiesWithGivenPerson(self):
        searchResults = []
        person = input("Please enter the id of the person whose activities you want to search: ")
        try:
            person = int(person)
        except Exception as ex:
            print(ex)
        else:
            searchResults = self.services.searchActivitiesWithGivenPersons(person)
        if len(searchResults) > 0:
            print("The following activities match what you searched for: ")
            for activity in searchResults:
                print(str(activity))
        else:
            print(f"No upcoming activities with person {person} found! ")


def menu(repository):
    print("Hi! What would you like to do?\n"
          "1. Add a person.\n"
          "2. Add an activity.\n"
          "3. Remove a person.\n"
          "4. Remove an activity.\n"
          "5. List persons.\n"
          "6. List activities.\n"
          "7. Update a person.\n"
          "8. Update an activity.\n"
          "9. Search persons.\n"
          "10. Search activities.\n"
          "11. List the activities for a given day.\n"
          "12. List the busiest days.\n"
          "13. Find activities with a certain person.\n"
          "0. Exit.")
    ADD_PERSON = 1
    ADD_ACTIVITY = 2
    REMOVE_PERSON = 3
    REMOVE_ACTIVITY = 4
    LIST_PERSONS = 5
    LIST_ACTIVITIES = 6
    UPDATE_PERSON = 7
    UPDATE_ACTIVITY = 8
    SEARCH_PERSON = 9
    SEARCH_ACTIVITY = 10
    LIST_ACTIVITIES_FOR_DAY_X = 11
    BUSIEST_DAYS = 12
    ACTIVITIES_WITH_PERSON_X = 13
    EXIT = 0

    UI = Console(repository)
    options = {
        ADD_PERSON: UI.addPerson,
        ADD_ACTIVITY: UI.addActivity,
        REMOVE_PERSON: UI.removePerson,
        REMOVE_ACTIVITY: UI.removeActivity,
        LIST_PERSONS: UI.listPersons,
        LIST_ACTIVITIES: UI.listActivities,
        UPDATE_PERSON: UI.updatePerson,
        UPDATE_ACTIVITY: UI.updateActivity,
        SEARCH_PERSON: UI.searchPerson,
        SEARCH_ACTIVITY: UI.searchActivity,
        LIST_ACTIVITIES_FOR_DAY_X: UI.listActivitiesFromGivenDay,
        BUSIEST_DAYS: UI.displayBusiestDays,
        ACTIVITIES_WITH_PERSON_X: UI.searchActivitiesWithGivenPerson
    }

    option = -1
    while option != EXIT:
        option = input("-> ")
        try:
            option = int(option)
        except Exception as ex:
            print(ex)
        if option in options:
            try:
                options[option]()
            except Exception as ex:
                print(ex)
        elif option == EXIT:
            print("End of the program.")
        else:
            print("Please enter a valid option! ")


def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    repositoryType = config.get('Repository', 'type')
    personsFileName = config.get('Repository', 'persons')
    activitiesFileName = config.get('Repository', 'activities')
    return repositoryType, personsFileName, activitiesFileName


if __name__ == "__main__":

    config_file_path = 'settings.properties'
    try:
        repoType, persons, activities = read_config(config_file_path)
    except configparser.Error as e:
        print(f"Error reading configuration: {e}")
    else:
        if repoType == "file":
            menu(FileRepository(persons, activities))
        elif repoType == "memory":
            menu(MemoryRepository)
        elif repoType == "binary file":
            menu(BinaryFileRepository(persons, activities))
