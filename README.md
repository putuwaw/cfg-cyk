# CFG-CYK

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Forks](https://img.shields.io/github/forks/putuwaw/cfg-cyk?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/putuwaw/cfg-cyk?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/putuwaw/cfg-cyk?style=for-the-badge)

CFG-CYK is a website based string checker using CFG with CYK algorithm using table filling method.

## Features💡
By using CFG-CYK you can:
- [x] Checks whether a string is valid or not.
- [x] Convert the CFG (Context Free grammar) to CNF (Chomsky Normal Form).
- [x] Get the final triangular table from table filling method.

## Technology 👨‍💻
CFG-CYK is created using:
- [Python](https://www.python.org/) - Python as the main programming language.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Flask is a web framework for Python, based on the Werkzeug toolkit.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework that allows for the creation of easy and responsive web layouts.
- [Heroku](https://www.heroku.com/) - Heroku is a platform as a service (PaaS) that we use to deploy our apps.
- [Vercel](https://vercel.com/) - Vercel is a cloud platform that we use to deploy our apps.
- [Docker](https://www.docker.com/) - Docker is a platform for developing, shipping, and running our applications.


## Structure 📂
```
CFG-CYK
├── .github
├── handlers
├── docs
├── modules
├── static
│   ├── images
│   ├── scripts
│   └── styles
├── templates
├── tests
├── .gitignore
├── Dockerfile
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── requirements.txt
├── set_of_production.txt
└── vercel.json
```
- [.github](.github/) is a folder that used to place Github related stuff, like issue template and CI pipeline.
- [handlers](handlers/) contain handler to handling HTTP request methods, especially POST method.
- [docs](docs/) contain documentation of this app.
- [modules](modules/) contain the main modules for convert CFG to CNF and implement CFG with CYK algorithm using table filling method.
- [static](static/) contain static files like images, CSS, and JavaScript files.
- [templates](templates/) contain the file that will be rendered for display in the browser.
- [tests](tests/) contain unit test to make sure the main module work properly.
- [.gitignore](.gitignore) is a file to exclude some folders like venv.
- [Dockerfile](Dockerfile) is a file that contains all the commands to build an image.
- [LICENSE](LICENSE) is a file that contains the license we use in this app.
- [Procfile](Procfile) is a file that specifies the commands that are executed by an Heroku app on startup.
- [README.md](README.md) is the file you are reading now.
- [app.py](app.py) is the main file of this app.
- [requirements.txt](requirements.txt) is a file that contains a list of dependencies used in this app.
- [set_of_production.txt](set_of_production.txt) is a file that contains set of production of the grammar.
- [vercel.json](vercel.json) is a file that contains configuration and override the default behavior of Vercel.

## Requirements 📦
- Python 3.10 or later
- Bootstrap v4.6.2 or later
- Docker 20.10.17 or later

## Installation 🛠️
- Install Docker.
- Pull the image from [Docker Hub](https://hub.docker.com/r/putuwaw/cfg-cyk):
```
docker pull putuwaw/cfg-cyk
```
- Run the downloaded image:
```
docker run -p 8000:8000 putuwaw/cfg-cyk
```
- Open web browser and visit:
```
localhost:8000
```

## Contributors ✨
<br>
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/putuwaw"><img src="https://avatars.githubusercontent.com/u/90038606?v=4" width="150px;" alt=""/><br><sub><b>Putu Widyantara</b></sub></td> 
    <td align="center"><a href="https://github.com/KEVINMOSESWALELENG"><img src="https://avatars.githubusercontent.com/u/103045275?v=4" width="150px;" alt=""/><br><sub><b>Kevin Moses</b></sub></td> 
    <td align="center"><a href="https://github.com/Antoniusata"><img src="https://avatars.githubusercontent.com/u/103051993?v=4" width="150px;" alt=""/><br><sub><b>Antonius Ata</b></sub></td>
    <td align="center"><a href="https://github.com/YogaLaksana"><img src="https://avatars.githubusercontent.com/u/103047470?v=4" width="150px;" alt=""/><br><sub><b>Yoga Laksana</b></sub></td>
  </tr>
</table>