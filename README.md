# djangoAdvancedapp
Advanced django app using docker and postgresql

# First clone this repo

```
git clone <repo_url>
```

## Then do the following

```
cd djangoadvancedapp
```

## Build the app

```
docker-compose build
```

## After building the app , migrate the database

```
docker-compose run web python manage.py migrate
```

## Now run the app 

```
docker-compose up
```

## Go to http://localhost:8001/ and check


## if you are not using docker do this,

## create a new folder called app and inside the folder create virtual environment

```
mkdir app
cd app
python -m venv env
```

## now clone this repo inside app folder

```
git clone <repo_url>
```

## activate the virtual environment
```
cd env
cd scripts
activate
```

## install the requirements

```
cd djangoadvancedapp
pip install -r requirements.txt
```

## Do the migrations

```
python manage.py migrate
```

## run the app

```
python manage.py runserver
```

## Now go to http://localhost:8000 and check

## Note (to run this app using python server)-
- You have to have postgresql installed
- go to settings.py and change the database settings similiar to your postgres settings.