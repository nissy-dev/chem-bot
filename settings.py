# -*- coding: utf-8 -*-
from dotenv import load_dotenv, find_dotenv

# load .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path, verbose=True)
