__author__='Sadat'

from flask import Flask
from config import basedir

app=Flask(__name__)

import views
