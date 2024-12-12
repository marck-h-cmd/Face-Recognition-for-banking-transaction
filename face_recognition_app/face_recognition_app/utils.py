from pathlib import Path
from dotenv import dotenv_values


ENV_FILE = Path(__file__).resolve().parent / '.env'

env_vars = dotenv_values(ENV_FILE)
def get_env_variable(key, default=None):

    return env_vars.get(key, default)
