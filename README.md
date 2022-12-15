# SE1-Placard
Placard project for SE1

## Description
Amirkabir university department of Computer Science, Software Engineering 1 project. 
This project is a SAAS for university student in order to publish promotions such as borrowing books etc.

## Usage
### building image
```
docker build -t placard .
docker run placard -d 
```

### running docker-compose
```
docker-compose up -d --build --force-recreate
```

### makemigrations and migrate after running docker-compose
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### running specific file (e.g. utils.py)
```
docker-compose exec web python brick/utils.py
```


Browse to `http://localhost` and you should see the landing page. 



### Collaboration
- [Fatemeh Farshidi](https://github.com/fatemehfarshidi)
- [Saya Hashemian](https://github.com/sayahashemian)
- [Ali Ghasemi](https://github.com/alighasemi01)
