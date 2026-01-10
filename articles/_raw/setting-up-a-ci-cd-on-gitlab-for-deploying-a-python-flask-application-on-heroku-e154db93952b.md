---
title: Setting up CI/CD on GitLab for deploying Python Flask application on Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-13T04:31:28.000Z'
originalURL: https://freecodecamp.org/news/setting-up-a-ci-cd-on-gitlab-for-deploying-a-python-flask-application-on-heroku-e154db93952b
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb550740569d1a4cad5db.jpg
tags:
- name: Flask Framework
  slug: flask
- name: GitLab
  slug: gitlab
- name: Heroku
  slug: heroku
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bharath Kallur

  Recently I came across a challenge to deploy a Python Flask web application to Heroku.
  The code of the App was hosted in GitLab.

  Heroku supports deploying an App from GitHub, Dropbox along with the usual Heroku
  git. It had been quit...'
---

By Bharath Kallur

Recently I came across a challenge to deploy a Python Flask web application to Heroku. The code of the App was hosted in GitLab.

Heroku supports deploying an App from GitHub, Dropbox along with the usual Heroku git. It had been quite a while since I used Heroku. I was wondering if I can deploy code directly from my GitLab repository instead of using any of the sources mentioned above.

I couldn’t find any information or documentation around deploying applications hosted in a GitLab repository to [Heroku](https://devcenter.heroku.com/categories/deployment). I browsed a bit on GitLab and it turned out that apart from helping test and build your project, GitLab CI can also help [deploy](https://docs.gitlab.com/ce/ci/environments.html) you App to your hosting infrastructure. I was now intrigued.

Before I delve into how I deployed the App, I’d like to explain the benefits of using GitLab or GitHub when you can easily get things done with Heroku Git.

1. **Easier code maintenance** - With code repository hosting services like GitHub and GitLab, maintenance of code is easy.
2. **Customising pipelines** - With GitLab, we can write our own [yaml](http://yaml.org/) file and include the libraries required for running our application.
3. **For better understanding of Continuous Integration and Continuous Development (CI/CD)** - For beginners, this setup helps you understand the coding workflow of testing -> version control -> code maintenance -> application deployment.

Here are the steps required to deploy your App hosted in GitLab to Heroku. The steps here assume you already have a good understanding of Python, Flask, version control, GitLab and Heroku. This write up is also helpful for someone who is just starting out. I have kept it as simple as possible to get things up and running.

### Uploading the project to GitLab

1. Create a Python virtual environment for us to use. Get into the virtual environment.
2. Create a sample Python Flask application on your machine.
3. Verify that everything is running fine.
4. Run the command `pip freeze > requirements.`txt from within the main application folder to catch all the requirements for running your application.
5. Create a Procfile which is used by Heroku to declare what commands are run by your application on the Heroku platform. Procfile usually consists of the web server used to run the application. In our case let us use Gunicorn, the default Python WSGI HTTP server. The content of your Procfile will be `web: gunicorn <name of the app.py file>:<`app-name> where app-name is usually “app”. Place this file within the main application folder.
6. Now login (or signup) to GitLab and create a project. The moment you do this, you will get a standard set of instructions on how to “link” your code on your development machine to GitLab project. Just follow the commands, and after that you can do a git push or git pull to/from this project. This is a bit of an elaborate step and your last statement should look something like `git push -u origin master`. Once done, on refreshing the project page on GitLab, you should see all your code appear in GitLab.

![Image](https://cdn-media-1.freecodecamp.org/images/ZR0E8T-GwjFxcxSIqt-Hwe75YUHsM70s6kMG)
_Project repository in GitLab_

### Linking GitLab and Heroku

1. Login to the [Heroku web portal](https://www.heroku.com) and create an application. Give it a nice name and runtime selection.
2. Now within the my_app folder on your development machine, create a file called “.gitlab-ci.yaml” (note the ‘.’ in the beginning).
3. This yaml file will have the following structure.

```
my_app_file_name:
 script:
 — apt-get update -qy
 — apt-get install -y python-dev python-pip
 — pip install -r requirements.txt
 — export MONGOHQ_URL=$MONGO_URL
 
production:
 type: deploy
 script:
 — apt-get update -qy
 — apt-get install -y ruby-dev
 — gem install dpl
 — dpl — provider=heroku — app=task-mgmt-app — api-key=$HEROKU_SECRET_KEY
 only:
 — master
```

1. Change my_app_file_name to the file name of your flask application. You need to set the HEROKU_SECRET_KEY variable in the project variables. You will get this key in the [Heroku dashboard](https://dashboard.heroku.com/). To set it in your GitLab project, go to **Settings > CI/CD Pipelines** and search for **Secret Variables.** While using these variables in the yaml, we need to prepend the variable with the ‘$’ sign. It is a good practice not to share secret keys with anyone and also restrict access to them in the project.
2. You are almost there. Run the command `git add .gitlab-ci.yml` and `git commit -m <msg>` and `git push -u origin master`. You will see the file in the GitLab repository now.
3. On the GitLab “My Dashboard” page, click on **Pipelines > Jobs** to see the job which has started running.
4. In case you are using a database in your App, you might want to link it to the App by placing the details in the .gitlab-ci.yaml file. Please check [here](https://gitlab.com/bharathkallurs/tasks/blob/master/.gitlab-ci.yml) for an example. I have used MongDB in my application. Heroku provides adding a set of free libraries/apps to your application. There is an [mLab link](https://devcenter.heroku.com/articles/mongolab) for adding MongoDB.

![Image](https://cdn-media-1.freecodecamp.org/images/C3IGAaKXdfqtg4z1tVXvomMnTo3vQepyewix)
_Jobs list in the Pipeline_

![Image](https://cdn-media-1.freecodecamp.org/images/p79aifr4r3f4LDcoXJ0qEgUyeIKRnGvYvg16)
_A running job. Screenshot related to my_app_file_name in yaml._

![Image](https://cdn-media-1.freecodecamp.org/images/ZYTyYC9SiR0klvctSE8HMVEPgdNHm0UwUPt3)
_Successful App deploy on Heroku_

Yay! You have now successfully integrated your GitLab with Heroku with CI/CD configuration. Make all code changes you want in your repository, push it to the GitLab project, and see a job start every time there is a code push. For the current setup, I used GitLab public runners available [here](http://gitlab.com/ci). You can set up a custom GitLab runner and set appropriate configuration.

### Useful links :

1. [Creating heroku remote](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote)
2. [Setting up CI/CD from GitLab on Heroku](https://docs.gitlab.com/ce/ci/examples/test-and-deploy-python-application-to-heroku.html)
3. [A task management application - repository : GitLab, deployed on Heroku](https://gitlab.com/bharathkallurs/tasks/tree/master)

