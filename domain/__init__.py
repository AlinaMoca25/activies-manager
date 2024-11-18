class Person:

    def __init__(self, _id, name, phoneNumber):
        self._id = _id
        self._name = name
        self._phoneNumber = phoneNumber

    def __str__(self):
        return f"Person {self._id} - name: {self._name}, phoneNumber: {self._phoneNumber}"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_number(self):
        return self._phoneNumber

    # def set_id(self, newId):
    #   self._id = newId

    def set_name(self, newName):
        self._name = newName

    def set_number(self, newNumber):
        self._phoneNumber = newNumber


class Activity:

    def __init__(self, _id, date, time: dict, participants: list = None, description: str = ""):
        """
        initializes the Activity class
        :param _id: unique id
        :param date: datetime.date, when the activity will be held
        :param time: dictionary with keys: start_time and end_time, which are hours (stored as datetime.time)
        :param participants: list of elements of type Person
        :param description: string, describes the activity
        """
        if participants is None:
            participants = []
        self._id = _id
        self.date = date
        self.time = time
        self.participants = participants
        self.description = description

    def __str__(self):
        time = f"{self.time["start_time"]} - {self.time["end_time"]}"
        listOfParticipants = []
        for participant in self.participants:
            listOfParticipants.append(str(participant))
        return (f"Activity {self._id}: \n"
                f"- date: {self.date}, time: {time} \n"
                f"- participants: {listOfParticipants} \n"
                f"- description: {self.description}.")

    def get_id(self):
        return self._id

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_participants(self):
        return self.participants

    def get_description(self):
        return self.description

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def set_participants(self, participants):
        self.participants = participants

    def set_description(self, description):
        self.description = description

