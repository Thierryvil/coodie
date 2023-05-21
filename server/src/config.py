from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    enviroments=["development", "testing", "production"],
    load_env=True,
    enviroment=True,
    settings_files=["settings.toml", ".secrets.toml"],
    env_switcher="ENV_FOR_DYNACONF",
)
