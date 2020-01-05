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