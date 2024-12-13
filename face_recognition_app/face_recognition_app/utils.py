from pathlib import Path
from dotenv import dotenv_values, load_dotenv
import os
load_dotenv()

ENV_FILE = Path(__file__).resolve().parent.parent / '.env'
print(ENV_FILE)
load_dotenv(ENV_FILE)
env_vars = dotenv_values(ENV_FILE)
print(env_vars)
def get_env_variable(key, default=None):

    return os.getenv(key, default)
