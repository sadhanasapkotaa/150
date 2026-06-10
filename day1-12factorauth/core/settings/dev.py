# Override path from base.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
print(BASE_DIR)

import os

import environ

path = BASE_DIR / ".envs/.local/.django"


environ.Env.read_env(BASE_DIR / ".envs/.local/.django")
environ.Env.read_env(BASE_DIR / ".envs/.local/.postgres")


from .base import *

env = environ.Env()

DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
SECRET_KEY = env("SECRET_KEY")
