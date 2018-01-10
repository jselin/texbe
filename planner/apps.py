from django.apps import AppConfig
import os


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        return False

class PlannerConfig(AppConfig):
    name = 'planner'
    if (not get_env_variable('DJANGO_DEVELOPMENT')):
        path = '/opt/python/current/app/planner'

