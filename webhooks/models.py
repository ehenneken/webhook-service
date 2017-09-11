"""
Models use to define the database

The database is not initiated here, but a pointer is created named db. This is
to be passed to the app creator within the Flask blueprint.
"""

import uuid
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.types import TypeDecorator, CHAR, String


db = SQLAlchemy()


class GUID(TypeDecorator):
    """
    Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    Taken from http://docs.sqlalchemy.org/en/latest/core/custom_types.html
    ?highlight=guid#backend-agnostic-guid-type

    Does not work if you simply do the following:
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    as Flask cannot serialise UUIDs correctly.

    """
    # Refers to the class of type being decorated
    impl = CHAR

    @staticmethod
    def load_dialect_impl(dialect):
        """
        Load the native type for the database type being used
        :param dialect: database type being used

        :return: native type of the database
        """
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    @staticmethod
    def process_bind_param(value, dialect):
        """
        Format the value for insertion in to the database
        :param value: value of interest
        :param dialect: database type

        :return: value cast to type expected
        """
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return '{0:.32x}'.format(uuid.UUID(value))
            else:
                # hexstring
                return '{0:.32x}'.format(value)

    @staticmethod
    def process_result_value(value, dialect):
        """
        Format the value when it is removed from the database
        :param value: value of interest
        :param dialect: database type

        :return: value cast to the type expected
        """
        if value is None:
            return value
        else:
            return uuid.UUID(value)

    @staticmethod
    def compare_against_backend(dialect, conn_type):
        """
        Return True if the types are different,
        False if not, or None to allow the default implementation
        to compare these types
        :param dialect: database type
        :param conn_type: type of the field

        :return: boolean
        """
        if dialect.name == 'postgresql':
            return isinstance(conn_type, UUID)
        else:
            return isinstance(conn_type, String)

class Accounts(db.Model):
    """
    Accounts table
    """
    __bind_key__ = 'webhooks'
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    absolute_uid = db.Column(db.Integer, unique=True)
    user_name = db.Colun(db.String)
    admin = db.Column(db.Boolean, default=False)
    api_key = db.Column(db.String, unique=True)
    secret_key = db.Column(db.String, unique=True)
    end_point = db.Column(db.String, unique=True)
    failed_count = db.Column(db.Integer)

    def __repr__(self):
        return '<User {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}>'\
            .format(self.id, self.absolute_uid,
            self.user_name, self.admin,
            self.api_key, self.secret_key,
            self.end_point, self.failed_count)

class Subscriptions(db.Model):
    """
    Subscriptions table
    """
    __bind_key__ = 'webhooks'
    __tablename__ = 'subscriptions'


class Registrations(db.Model):
    """
    Registrations table
    """
    __bind_key__ = 'webhooks'
    __tablename__ = 'registrations'


class Triggered(db.Model):
    """
    Trigerred Webhooks table
    """
    __bind_key__ = 'webhooks'
    __tablename__ = 'triggered'
