from os.path import dirname, realpath

from dynaconf import Dynaconf

current_directory = dirname(realpath(__file__))

settings = Dynaconf(
    root_path=current_directory,
    envvar_prefix="COODIE",
    environments=True,
    settings_files=[
        "settings.toml",
        ".secrets.toml",
    ],
    env_switcher="COODIE_MODE",
)
