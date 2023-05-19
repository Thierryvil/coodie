
from dynaconf import Dynaconf, Validator


settings = Dynaconf(
    settings_file=["settings.toml", '.secrets.toml'],
    validators=[
        Validator('DATABASE_NAME', must_exist=True),
        Validator('AUTH0_DOMAIN', must_exist=True),
        Validator('AUTH0_CLIENT_ID', must_exist=True),
        Validator('AUTH0_CLIENT_SECRET', must_exist=True)
    ]
)
