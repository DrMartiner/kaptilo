# Deploy
## Local
- create virtualenv & install requirements
```bash
pyenv virtualenv 3.9.0 kaptilo
pyenv activate kaptilo
pip install poetry
poetry install
``` 
- copy .env file `cp .env.dev .env` or export to envs:
```bash
export IPINFO_TOKEN=...
export ALLOWED_HOSTS=localhost
export BASE_URL=https://localhost:8000
export RECAPTCHA_PUBLIC_KEY=...
export RECAPTCHA_PRIVATE_KEY=...
export REDIS_DSN=redis://localhost:6379
``` 
- add to env `export DB_DSN=postgres://user:pass@localhost/db_name` if you use Postgres 
- apply DB migrations `./manage.py migrate`
- created **admin:admin** `./manage.py create_super_user`
- run localserver `./manage.py runserver`
- open [localhost:8000/admin/super-sec/](http://localhost:8000/admin/super-sec/) and login as **admin:admin**

## Server
```bash
export IPINFO_TOKEN=...
export SECRET_KEY=...
export DOMAIN=domain.com
export RECAPTCHA_PUBLIC_KEY=...
export RECAPTCHA_PRIVATE_KEY=...

docker-compose up -d --build
docker-compose run back migrate
docker-compose run back collectstatic
docker-compose exec back ./manage.py create_super_user --username admin --password sup-pass-123
open https://domain.com:8000/admin/sec/
```

# Develop
### Before beginning
- execute `pre-commit install` to install pre-commit hooks

### Before make a commit
- if you install a lib, execute `make update-isort`
- execute `make lint` to call lints
 