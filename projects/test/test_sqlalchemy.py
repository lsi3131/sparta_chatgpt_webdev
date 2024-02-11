import collections
import unittest
import random
import string
import re
import app
import os
from collections import *
from app import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Test(unittest.TestCase):
    def test_example1(self):
        print('===========')
        basedir = os.path.abspath(os.path.dirname(__file__))
        dbpath = 'sqlite:///' + os.path.join(basedir, 'database.db')
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = dbpath
        db = SQLAlchemy(app)

        print(f'{basedir}\n{dbpath}')
    


if __name__ == '__main__':
    unittest.main()
