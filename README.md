# python-tutorial

## init

```sh
git init
git remote origin https://github.com/zhuyudong/python-tutorial.git
git add .
git commit -m "feat: init"
# git config pull.rebase false  # merge
git config pull.rebase true   # rebase
# git config pull.ff only       # fast-forward only
git config --global user.name "Yudong.zhu"
git config --global user.email "yudong8.zhu@gmail.com"

git pull origin main
# git branch --set-upstream-to=origin/main main
git push -u origin main
```

## installing

```sh
python3 --version # Python 3.12.6
which python3 # /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
which pip3 # /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3
```

`vim ~/.zshrc`

```sh
alias pip="/Library/Frameworks/Python.framework/Versions/3.12/bin/pip3"
alias python="/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"
```

`source ~/.zshrc`

~~`python -m venv venv`~~

~~`. venv/bin/activate`~~

```sh
pip install alembic aiomysql apscheduler asgi-lifespan bcrypt==4.0.1 beanie boto3 botocore celery celery-sqlalchemy-scheduler colored colorama colorlog croniter cryptography dacite email-validator emails esdk-obs-python fastapi fastapi-async-sqlalchemy fastapi-cache2 fastapi-jwt fastapi-limiter fastapi-mail fastapi-pagination filterpy grpcio gunicorn huaweicloudsdkobs httpx httpx-oauth jinja2 jira jsonschema loguru matplotlib mimesis minio msgpack motor numpy openpyxl oauthlib passlib paramiko pycrypto pydantic pydantic-settings pydash pymongo pymysql pyjwt pyserial pytz python-decouple python-gitlab python-jose python-multipart requests requests-oauthlib rich sentry-sdk scipy sqlalchemy 'sqlalchemy[mypy]' sqlalchemy-stubs sqlalchemy-utils stackprinter structlog tenacity tzlocal ua-parser user-agents uvicorn whitenoise -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```

```sh
pip install add-trailing-comma autoflake black coverage flake8 isort mypy mypy-extensions packaging pip-upgrader pre-commit pytest pytest-asyncio pytest-cov pytest-mock pyupgrade ruff -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```

```sh
brew install hatch
hatch --version # Hatch, version 1.12.0
hatch --help
hatch new --init # generated pyproject.toml
```

## reference

- [python](https://www.python.org/downloads/)
- [python3-cookbook](https://github.com/yidao620c/python3-cookbook)
- [StrongVPN](https://strongtech.org/vpn-apps/macos/)
- [Visual Studio Code](https://code.visualstudio.com/docs/setup/mac)