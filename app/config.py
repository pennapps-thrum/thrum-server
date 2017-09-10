"""Configuration variables."""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

FIREBASE_KEY = os.environ.get("FIREBASE_KEY")
USER_ID = "fmGQ4gbuuzw:APA91bGQY3_txna8YHIjgup74YNuSH9F8ETqXtLudCSRDOLMba0qHekCP2GyBfvevl-SSkxmsMV3qM6rjx0nkhg6x6Ev2W1v6Qdmy5vgKa_djFsRqeFyuwVrB9wsNUN3t9LrMN0fMJm8"
