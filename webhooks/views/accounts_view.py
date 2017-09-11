



class Accounts(Resource):
    """
    Handles the REST API interaction for accounts
    """

    def get(self):
        """
        Get a listing of accounts (paginated if need be)
        Note: only an 'admin' should be able to do this
        """

    def delete(self):
        """
        Deletes all records (except admin) in the Accounts table
        Note: only an 'admin' should be able to do this
        """

class Account(Resource):
    """
    Handles the REST API interaction for accounts
    """

    def get(self, account_id):
        """
        Gets a user account.
        Note: Users can only see their own account
        """

    def update(self):
        """
        Updates account.
        Note: Only the 'endpoint' field can be updated
        Updating the endpoint also resets the failed_count
        """

    def post(self):
        """
        Creates a new account
        """

    def delete(self, account_id):
        """
        Deletes account record
        """
