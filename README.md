# social-posts
This is a simple app to help people that need to post on social networks groups organize.
The idea is to help people who need to do inbound marketing.
It is also a django project I used to learn.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* I have tested this project on a Linux Antergos 64;
* Python 3.6.2 
* Django 1.11

### Installing

Clone this repository, create a virtual envinroment and install the requirements.txt. Just follow the steps bellow:

```
$ mkdir socialposts
$ cd socialposts
$ python -m venv .
$ source ./bin/activate
$ git clone https://github.com/renanbs/social-posts.git src
$ cd src
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser 
$ python manage.py runserver
```

## Live working version

* [SOCIAL-POSTS](http://socialpostscontrol.herokuapp.com/) - LIVE

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Renan
