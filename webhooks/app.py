
from views import Account
from views import Accounts
from views import ApiKey
from views import SecretKey
from views import Registration
from views import Registrations
from views import Subscription
from views import Subscriptions
from views import Triggering

def create_app():
    """
    Create the application and return it to the user
    :return: flask.Flask application
    """

    app = Flask(__name__, static_folder=None)
    app.url_map.strict_slashes = False

    load_config(app)

    logging.config.dictConfig(
        app.config['WEBHOOKS_LOGGING']
    )

    api = Api(app)

    # Define all endpoints and associated views:
    # Interact with all accounts
    api.add_resource(Accounts,
                     '/accounts',
                     methods = ['GET','DELETE'])
    # Interact with a specific account
    api.add_resource(Account,
                     '/account/<account_id>',
                     '/account',
                     methods = ['GET','POST','UPDATE','DELETE'])
    # Support resetting of API keys
    api.add_resource(ApiKey,
                     '/account/reset/apikey',
                     methods = ['POST'])
    # Support resetting of secret keys
    api.add_resource(SecretKey,
                     '/account/reset/secretkey',
                     methods = ['POST'])
    # Interact with all webhooks
    api.add_resource(Registrations,
                     '/registrations',
                     methods = ['GET','DELETE'])
    # Interact with a specific webhook
    api.add_resource(Registration,
                     '/registration',
                     methods = ['GET','POST','UPDATE','DELETE'])
    # Interact with all subscriptions
    api.add_resource(Subscriptions,
                     '/subscriptions',
                     methods = ['GET','DELETE'])
    # Interact with a specific subscription
    api.add_resource(Subscription,
                     '/subscription',
                     methods = ['GET','POST','DELETE'])
    # Interact with triggers
    api.add_resource(Triggering,
                     '/triggered',
                     '/triggered/<registration_id>',
                     methods = ['GET','POST'])

def load_config(app):
    """
    Loads configuration in the following order:
        1. config.py
        2. local_config.py (ignore failures)
    :param app: flask.Flask application instance
    :return: None
    """

    app.config.from_pyfile('config.py')

    try:
        app.config.from_pyfile('local_config.py')
    except IOError:
        app.logger.warning("Could not load local_config.py")

@app.before_request
def before_request():
    # Before any request handling, we want to check for media type
    if request.headers['content-type'].lower().find('application/json'):
        return 'Unsupported Media Type', 415

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, use_reloader=False, port=8081, host='0.0.0.0')
