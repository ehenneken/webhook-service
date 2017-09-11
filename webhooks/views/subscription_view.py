
from flask import request
from flask_restful import Resource

class Subscriptions(Resource):
    """
    Handles the (webhook) subscriptions table interactions
    """

    def get(self):
        """
        Get a listing of subscriptions
        """

    def delete(self):
        """
        Deletes all records in the subscriptions table
        Note: only an 'admin' can do this
        """

class Subscription(Resource):
    """
    Handles the (webhook) subscriptions table interactions
    """

    def get(self):
        """
        Get the user's webhook subscriptions
        """

    def post(self, subscription_id):
        """
        Creates new subscription
        """

    def delete(self, subscription_id):
        """
        Deletes subscription record
        """
