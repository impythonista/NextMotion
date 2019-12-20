# NextMotion

It's the NextMotion application to process the data.

# How to setup the project.
  - python version should be 3.6
  - Django 2.1

### Follow below instruction to install the depedencies.


##### Ubuntu

- Install python3.6
	```sh
	$ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
    $ sudo apt-get install python3.6-dev
	```
- Install Virtualenv
	```sh
	$ sudo apt-get install python3-pip
	$ sudo pip3 install virtualenv 
	```

### Follow below setups to setup the application.
- Create the virtual envoirments with python 3.6 version and activate
    ```sh
    $ virtualenv --python=python3.6 env
    $ source env/bin/activate
    ```

- Create the .env file to store the envoirment varible and it should be create in project root folder.
- Install python  dependencies, run into the project root directory.
	```sh
    $ pip install -r requirements.txt
    ```
- Below is all the required envoirment variable. below are the sample value of database.
    ```sh
    # email configuration.

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'enter user name'
    EMAIL_HOST_PASSWORD = '******'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```
- Go the the NextMotion project directory and migrate the db.
    ```sh
    $ cd NextMotion
    $ python manage.py migrate
    ```
   
- Create admin user in django and runserver.
    ```sh
    $ python manage.py createsuperuser
    $ python manage.py runserver
    ```
- URL of admin panel is.
	```sh
	http://127.0.0.1:8000/admin/
	```
 
- Access the db console using django
	```sh
	$ python manage.py dbshell
	```
- Access the project python shell
	```sh
	$ python manage.py shell
	```

- Run the test cases.
    ```sh
    $ python manage.py test
    ```

- I added the default sqlite db, please find below admin password and it's the basic token.

    ```sh
    $ username = admin
    $ password = admin@12345
    $ auth_token = 5e0f85d01c31dd826a965c48c14c60226319f6c2
    ```
- Please find the postman collection of API into the root project directory and below are the endpoints of api.
    
    ```sh
    GET api/invitations/ List all the invitations (with pagination) 
    POST api/invitations/ Create an invitation
    PATCH api/invitations/<id>/ Modify the invitation with the given id
    DELETE api/invitations/<id>/ Delete the invitation with the given id
    ```
