from pathlib import Path
from dotenv import dotenv_values


ENV_FILE = Path(__file__).resolve().parent / '.env'

def get_env_variable(key, default=None):

    env_vars = dotenv_values(ENV_FILE)
    return env_vars.get(key, default)
