from django.apps import AppConfig
import os


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        return False

class PlannerConfig(AppConfig):
    name = 'planner'
    if(!get_env_variable):
        path = '/opt/python/current/app/planner'

