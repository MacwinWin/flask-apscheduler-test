# flask-apscheduler-test

The demo code is used to testing the effect of combining of flask or connexion wiht flask-apscheduler. And contains two types of API, the first one is build-in API, the second one is custom API built by the build-in functions.

## Deploy

In the root derectory, run the following code:  

```bash
>>> docker compose up -d
```

## Run

Then, enter the container using the following code:

```bash
>>> docker exec -it flask-apscheduler-test /bin/bash
```

Then, stop the supervisor by the following code:

```bash
>>> supervisorctl -c Services/flask-apscheduler-test/supervisord.conf stop all
```

Then, run and you can see the following code:

```b
root@1097a63d4c7f:/app# python3 swagger_server/app.py 
/app/swagger_server/app.py:47: DeprecationWarning: 'app.json_encoder' is deprecated and will be removed in Flask 2.3. Customize 'app.json_provider_class' or 'app.json' instead.
  app.app.json_encoder = encoder.JSONEncoder
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.22.0.2:8000
Press CTRL+C to quit
2022-11-20 22:21:14.358093 execute task 1+2=3
2022-11-20 22:21:24.358596 execute task 1+2=3
2022-11-20 22:21:34.357602 execute task 1+2=3
2022-11-20 22:21:44.357543 execute task 1+2=3
2022-11-20 22:21:54.357700 execute task 1+2=3
2022-11-20 22:22:04.357793 execute task 1+2=3
2022-11-20 22:22:14.358036 execute task 1+2=3
2022-11-20 22:22:24.358291 execute task 1+2=3
2022-11-20 22:22:34.358224 execute task 1+2=3
```

## Test

Use Postman to test the api.

### Import the postman collection

![image](./Screen%20Shot%202022-11-20%20at%2022.39.17.png)

### Test the apis one by one

![image](./Screen%20Shot%202022-11-20%20at%2022.44.17.png)
