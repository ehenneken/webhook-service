

class Registrations(Resource):
    """
    Handles the REST API interaction for Registrations
    """

    def get(self):
        """
        Get a listing of Registrations (paginated if need be)
        """

    def delete(self):
        """
        Deletes all records in the Registrations table
        """


class Registration(Resource):

    def get(self):
        """
        Get the user's registered webhooks
        """

    def update(self, registration_id):
        """
        Updates registration. Only one field can be updated: description
        """

    def post(self):
        """
        Creates a new registration
        """


    def delete(self, registration_id):
        """
        Deletes registration record, will also remove the records for this
        registration_id in the subscription table as well
        """
