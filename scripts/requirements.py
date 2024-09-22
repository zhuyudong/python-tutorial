base_dependencies = ["alembic", 
                     "aiomysql", "apscheduler", " asgi-lifespan", " bcrypt==4.0.1 beanie boto3 botocore celery celery-sqlalchemy-scheduler colored colorama colorlog croniter cryptography dacite email-validator emails esdk-obs-python fastapi fastapi-async-sqlalchemy fastapi-cache2 fastapi-jwt fastapi-limiter fastapi-mail fastapi-pagination filterpy grpcio gunicorn huaweicloudsdkobs httpx httpx-oauth jinja2 jira jsonschema loguru matplotlib mimesis minio msgpack motor numpy openpyxl oauthlib passlib paramiko", " pycrypto", " pydantic", " pydantic-settings pydash pymongo pymysql pyjwt pyserial pytz python-decouple", " python-gitlab", " python-jose", " python-multipart requests", " requests-oauthlib", " rich", " sentry-sdk", " scipy", " sqlalchemy", " 'sqlalchemy[mypy]' sqlalchemy-stubs", " sqlalchemy-utils", " stackprinter", " structlog", " tenacity tzlocal", " ua-parser", " user-agents", " uvicorn", " whitenoise"]
dev_dependencies = []

with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    in_test_section = False
    for line in lines:
        line = line.strip()
        if line.startswith('[test]'):
            in_test_section = True
        elif in_test_section:
            dev_dependencies.append(line)
        else:
            if line and not line.startswith('#'):
                base_dependencies.append(line)

with open('requirements/base.txt', 'w') as f:
    f.writelines('\n'.join(base_dependencies))

with open('requirements/dev.txt', 'w') as f:
    f.writelines('\n'.join(dev_dependencies))