import json
import os

from google.cloud import firestore
from google.oauth2 import service_account

credentials=None

if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    # Obtain the service account key from the environment variable
    service_account_key_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

    # Load the JSON key into a dictionary
    service_account_key_dict = json.loads(service_account_key_json)

    # Use the dictionary to authenticate
    credentials = service_account.Credentials.from_service_account_info(
        service_account_key_dict
    )

# Initialize Firestore with the project ID and credentials
db = firestore.Client(credentials=credentials)

# Get a reference to the Firestore collection
collection_ref = db.collection("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    doc_ref = collection_ref.document(period)
    doc_ref.set({"incomes": incomes, "expenses": expenses, "comment": comment})
    return doc_ref.get().to_dict()


# def fetch_all_periods():
#     """Returns a list of all periods"""
#     docs = collection_ref.stream()
#     return [doc.to_dict() for doc in docs]
def fetch_all_periods():
    """Returns a list of all periods"""
    docs = collection_ref.stream()
    return [{"key": doc.id, **doc.to_dict()} for doc in docs]


def get_period(period):
    """If not found, the function will return None"""
    doc_ref = collection_ref.document(period)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
# --- DATABASE INTERFACE ---
def get_all_periods():
    items = fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods
