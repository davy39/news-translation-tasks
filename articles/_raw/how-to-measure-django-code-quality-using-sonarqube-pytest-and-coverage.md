---
title: How to Measure Django Code Quality Using SonarQube, Pytest, and Coverage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-18T16:36:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-measure-django-code-quality-using-sonarqube-pytest-and-coverage
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/istockphoto-91813442-612x612.jpg
tags:
- name: Code Quality
  slug: code-quality
- name: Django
  slug: django
- name: Python
  slug: python
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Ridwan Yusuf

  Greetings, fellow coding enthusiasts!

  We''re going to dive deep into the realm of Django code quality assessment. In this
  comprehensive guide, I''ll walk you through an in-depth approach to measuring the
  code quality of your Django-base...'
---

By Ridwan Yusuf

Greetings, fellow coding enthusiasts!

We're going to dive deep into the realm of Django code quality assessment. In this comprehensive guide, I'll walk you through an in-depth approach to measuring the code quality of your Django-based application.

By the end of this tutorial, you will be able to:

1. Build CRUD APIs using Django and DRF (Django REST Framework)
2. Write automated tests for the APIs using Pytest
3. Measure code test coverage using Coverage
4. Utilize SonarQube to assess code quality, identify code smells, security vulnerabilities, and more

Prerequisites to follow along in this tutorial include:

1. Python 3 installation on your chosen Operating System (OS). We'll use Python 3.10 in this tutorial.
2. Basic knowledge of Python and Django
3. Any code editor of your choice

Without any further delay, let's jump right in and get started.

## How to Get the APIs Up and Running

To begin, open your Terminal or bash. Create a directory or folder for your project using the command:

```bash
mkdir django-quality && cd django-quality
```

In my case, the folder name is "django-quality".

To isolate the project dependencies, we need to utilize a Python virtual environment.

To create a virtual environment, use the following command in your Terminal or bash:

```bash
python3 -m venv venv
```

Activate the virtualenv by running this command:

```bash
source venv/bin/activate

```

If everything works fine, you should see the virtual environment indicator enclosed in brackets, similar to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/venv-activated.png)
_Python Virtualenv activated successfully_

At the root directory of your project, create a folder called "requirements" that will house the external packages required for various development stages, such as dev (development) and staging.

Inside the "requirements" folder, create two files: "**base.txt**" and "**dev.txt**". The "base.txt" file will include generic packages required by the application, while the "dev.txt" file will contain dependencies specific to development mode.

By now, the contents in your project folder should have the following structure

```bash
- requirements
    ├── base.txt
    └── dev.txt
- venv

```

Here are the updated contents for the "base.txt" and "dev.txt" files:

`base.txt`

```bash
Django==4.0.6
djangorestframework==3.13.1
drf-spectacular==0.22.1
```

`dev.txt`

```bash
-r base.txt
pytest-django==4.5.2
pytest-factoryboy==2.5.0
pytest-cov==4.1.0
```

* djangorestframework: Used for API development.
* drf-spectacular : Used for automated documentation of the APIs.
* pytest-cov: Utilized for measuring code coverage during testing. 
* pytest-factoryboy: Used for creating test data using factory patterns.

Make sure your virtual environment is activated, then run the following command at the root directory to install the dependencies specified in "dev.txt":

```bash
pip install -r requirements/dev.txt
```

To create a new Django project, you can run the following command:

```bash
django-admin startproject core .
```

The name of the project is 'core'. You can decide to use any suitable name that fits your use case.

By now, you should see a couple of files and folders automatically created after running the command.

Here is the current project structure:

```bash
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements
│   ├── base.txt
│   └── dev.txt
└── venv
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/project-folder-structurefold-min.png)
_Current Folder Structure in VSCode_

The APIs we will create will be a basic blog API with CRUD functionality. Let's create a new app within the project to host all the files related to the blog features.

Run this command to create a new app called 'blog':

```bash
python manage.py startapp blog
```

By now, a new folder named 'blog' has been auto-created by the command.

Here is the folder structure:

```bash
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── core
├── manage.py
├── requirements
└── venv

```

Update the `models.py` file in the `blog` folder. The `Blog` class defines the database schema for the blog.

`blog/models.py`

```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

Create a new file named 'serializers.py' inside the 'blog' folder and update its content as shown below:

`blog/serializers.py`

```python
from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
    extra_kwargs = {
            "created_at": {"read_only": True},
        }
```

The `BlogSerializer` class is utilized for validating incoming blog data sent by the client (such as from the frontend or mobile app) to ensure it adheres to the expected format.

Additionally, the serializer class is used for both serialization (converting Python objects to a transmittable format like JSON) and deserialization (converting a transmittable format like JSON back to Python objects).

Let's create the view to handle CRUD functionality, leveraging the DRF `ModelViewSet` to effortlessly create APIs with just a few lines of code.

`blog/views.py`

```python
from rest_framework import filters, viewsets

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    http_method_names = ["get", "post", "delete", "patch","put"]
    serializer_class = BlogSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["published"]
    search_fields = ["title", "body"]
    ordering_fields = [
        "created_at",
    ]

```

Create a new file named 'blog.urls' in the 'blog' folder.

By utilizing the DRF router for URL configuration, the URLs are automatically generated based on the allowed methods defined in the `BlogViewSet`.

`blog/urls.py`

```python
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import BlogViewSet

app_name = "blog"

router = DefaultRouter()
router.register("", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

```

The next step is to register the `urls.py` file defined in the 'blog' app within the main project's `urls.py` file. To do this, you should locate the project's `urls.py` file, which serves as the starting point for URL routing.

`core/urls.py`

```python

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/blogs/', include('blog.urls')),
]


```

The `api/v1/blogs/` URL is mapped to the URLs defined in `blog.urls`. Additionally, other URLs are utilized for automated API documentation.

Update the `settings.py` file located inside the `core` folder. This file contains configurations for the Django application.

In the `INSTALLED_APPS` section, register the newly created 'blog' app, along with any desired third-party apps. Note that for brevity, the default Django apps are not included in the following list:

`settings.py`

```python
INSTALLED_APPS = [


    #Third-party Apps
    'drf_spectacular',

    #Local Apps
    'blog',
]
```

Update the `settings.py` file to include configurations related to Django REST Framework (DRF) and documentation.

`settings.py`

```python

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


SPECTACULAR_SETTINGS = {
    'SCHEMA_PATH_PREFIX': r'/api/v1',
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    'COMPONENT_SPLIT_PATCH': True,
    'COMPONENT_SPLIT_REQUEST': True,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
        "displayRequestDuration": True
    },
    'UPLOADED_FILES_USE_URL': True,
    'TITLE': 'Django-Pytest-Sonarqube - Blog API',
    'DESCRIPTION': 'A simple API setup with Django, Pytest & Sonarqube',
    'VERSION': '1.0.0',
    'LICENCE': {'name': 'BSD License'},
    'CONTACT': {'name': 'Ridwan Ray', 'email': 'ridwanray.com'},
    #OAUTH2 SPEC
    'OAUTH2_FLOWS': [],
    'OAUTH2_AUTHORIZATION_URL': None,
    'OAUTH2_TOKEN_URL': None,
    'OAUTH2_REFRESH_URL': None,
    'OAUTH2_SCOPES': None,
}

```

With all the necessary configurations in place, let's run the migrations command to ensure that the models in the application are synchronized with the database schema.

Execute the following commands in the root directory to synchronize the models with the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

To start the development server, run the following command:

```bash
python manage.py runserver
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/dev-server.png)
_Starting local development server with runserver command_

The application is now running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
To access the documentation, visit [http://127.0.0.1:8000/api/v1/doc/](http://127.0.0.1:8000/api/v1/doc/).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/blog-doc-min-1--1.png)
_Automated Blog API documentation using drf-spectacular_

## How to Write Automated Tests with Pytest

Pytest, the testing tool we're using for writing automated tests, is included as part of the dependencies declared in the requirement folder. Now, let's write some tests and explore its functionality.

In the blog folder, a file named "tests.py" is automatically generated when starting the blog app. To organize the tests, create a new folder called "tests" within the blog directory.

Move the initial "tests.py" file into the newly created "tests" folder. To make the "tests" folder a module, create an empty file named "**__init__.py**".

Create a new file named 'conftest.py' inside the 'tests' folder. This file will store any pytest fixtures (that is, reusable components) required during the test writing process.

Test folder structure:

```bash
├── tests
│   ├── conftest.py
│   ├── factories.py
│   ├── __init__.py
│   ├── __pycache__
│   └── tests.py

```

`tests/conftests.py`

```python
import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()
```

The `api_client()` is a Pytest fixture utilized for making actual API calls.

Create a new file named 'factories.py'. This file will include the factories used during test writing. Factories provide a convenient way to create objects (that is, model instances) without the need to specify all attributes each time.

`tests/factories.py`

```python

import factory
from faker import Faker
from blog.models import Blog

fake = Faker()

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog
        
    title = fake.name()
    body = fake.text()
    published = True
```

`tests/tests.py`

```python
import pytest
from django.urls import reverse
from .factories import BlogFactory

pytestmark = pytest.mark.django_db


class TestBlogCRUD:
    blog_list_url = reverse('blog:blog-list')

    def test_create_blog(self, api_client):
        data = {
            "title": "Good news",
            "body": "Something good starts small",
            "published": True
            }

        response = api_client.post(self.blog_list_url, data)
        assert response.status_code == 201
        returned_json = response.json()
        assert 'id' in returned_json
        assert returned_json['title'] == data['title']
        assert returned_json['body'] == data['body']
        assert returned_json['published'] == data['published']

    def test_retrieve_blogs(self, api_client):
        BlogFactory.create_batch(5)
        response = api_client.get(self.blog_list_url)
        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_delete_blog(self, api_client):
        blog = BlogFactory()
        url = reverse("blog:blog-detail",
                      kwargs={"pk": blog.id})
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_update_blog(self, api_client):
        blog = BlogFactory(published= True)
        data = {
            "title": "New title",
            "body": "New body",
            "published": False,
        }
        url = reverse("blog:blog-detail",
                      kwargs={"pk": blog.id})

        response = api_client.patch(url, data)
        assert response.status_code == 200
        returned_json = response.json()
        assert returned_json['title'] == data['title']
        assert returned_json['body'] == data['body']
        assert returned_json['published'] == data['published']
        
```

The TestBlogCRUD class tests the CRUD functionalities of the application. The class defines four methods, each testing a specific CRUD functionality.

Create a Pytest configuration file named `pytest.ini` in the root directory. This file will contain settings that instruct Pytest on how to locate the test files.

`pytest.ini`

```ini
[pytest]
DJANGO_SETTINGS_MODULE = core.settings
python_files = tests.py test_*.py *_tests.py
addopts = -p no:warnings --no-migrations --reuse-db
```

To run the tests, execute the `pytest` command in the root directory as shown below:

```bash
pytest
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/pytest-output.png)
_Pytest testcases result_

The test results indicate that all four test cases have passed successfully.

As of the time of writing, two popular tools used in the Python community for reporting test coverage in a codebase are Coverage and pytest-cov.

In our case, we'll be using **pytest-cov** for its flexibility when it comes to reporting test coverage.

Create a new file named 'setup.cfg' in the root directory. This file serves as the configuration file for coverage.

`setup.cfg`

```bash
[coverage:run]
source = .
branch = True
[coverage:report]
show_missing = True
skip_covered = True
```

The `source` value in the `[coverage:run]` section specifies the root directory location from which test coverage will be measured.

In addition to statement coverage in the test report, branch coverage identifies uncovered branches when using conditional statements (for example if, else, case).

Note: It is possible to specify folders to omit from test coverage, such as migration folders, in the `setup.cfg` file. We will configure these settings in SonarQube.

Let's rerun the test cases using the following command:

```bash
pytest --cov --cov-report=xml

```

The `--cov-report` option specifies the format of the coverage report. Various formats like HTML, XML, JSON, and so on are supported. In this case, we specify `xml` because it is supported by SonarQube.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-13-05-20-43-min.png)
_Pytest coverage report in XML format_

For HTML format, a folder named 'htmlcov' will be generated in the root directory. This folder contains the 'index.html' file, which allows you to visualize the coverage results and areas that are not covered.

## How to Setup SonarQube

SonarQube is a tool used for static code analysis. It helps in identifying code quality issues, bugs, vulnerabilities, and code smells in software projects.

To simplify the process, we can run a Docker container based on the SonarQube image.

Execute the following command in the command line:

```bash
docker run -d -p 9000:9000 -p 9092:9092 sonarqube
```

After a few moments, depending on your internet speed, visit [http://0.0.0.0:9000/](http://0.0.0.0:9000/).

You can use the following login credentials to access the application: Username: admin Password: admin

Next, you need to download Sonar Scanner. Visit this [link](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/) and select the option that is compatible with your operating system (OS).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sonar-scanner.png)
_SonarScanner download on the Sonarsource.com website_

Unzip the sonar-scanner and move it from the 'Downloads' folder to a secure directory .

```bash
unzip sonar-scanner-cli-4.8.0.2856-linux.zip

mv sonar-scanner-4.2.0.1873-linux /opt/sonar-scanner
```

Add the following lines to the content of the `sonar-scanner.properties` file located at `/opt/sonar-scanner/conf/sonar-scanner.properties`:

```bash
vim  /opt/sonar-scanner/conf/sonar-scanner.properties
```

Add these two lines and save the file:

```bash
sonar.host.url=http://localhost:9000
sonar.sourceEncoding=UTF-8
```

Add /opt/sonar-scanner/bin to the system's PATH environment variable by executing this command:

```bash
export PATH="$PATH:/opt/sonar-scanner/bin
```

Update the content of .bashrc:

```bash
vim ~/.bashrc
```

Add this line to the .bashrc file and save it:

```bash
export PATH="$PATH:/opt/sonar-scanner/bin
```

Run the following command to apply the changes to your current terminal session:

```bash
source ~/.bashrc
```

To ensure that everything is functioning properly, execute the following command:

```bash
sonar-scanner -v
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/scanner2.png)
_Checking sonarqube version on the terminal_

Navigate to the 'Projects' tab on the SonarQube dashboard and proceed to manually create a new project.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/WhatsApp-Image-2023-07-13-at-06.22.56.jpeg)
_Creating a new project on the sonarqube dashboard_

Provide a suitable name for the project, then select the option "Use the global setting" before proceeding to create the project.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/create-suitable-name.png)
_Choosing appropriate name as the name of the new preoject_

![Image](https://www.freecodecamp.org/news/content/images/2023/07/create-globa-setting.png)
_Configuring new project to use global settings_

After creating the project, you will be prompted to select the analysis method for your project. Choose the 'Locally' option.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/WhatsApp-Image-2023-07-13-at-06.34.22.jpeg)
_Run analysis on the project locally_

After selecting the 'Locally' option, you will be required to generate a token. Click on 'Continue' to proceed. Next, select the programming language of your project and the operating system (OS) it will be running on.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/lang-os.png)
_Choose the programming language of project and OS_

Copy the command displayed, as we'll use it to execute the analysis for the project.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/WhatsApp-Image-2023-07-13-at-06.38.29.jpeg)
_Code needed to run analyis_

Here is the content of the command:

```bash
sonar-scanner \
  -Dsonar.projectKey=newretailer \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://0.0.0.0:9000 \
  -Dsonar.token=sqp_7b6aada8ce53e97ebb7b2bf5e9b64d53b8938a6f \
  -Dsonar.python.version=3
```

Note: We have added an additional line to the command to specify the Python version as `-Dsonar.python.version=3`.

Before executing the analysis command, follow these steps:

1. Click on "Project Settings" and then select "General Settings".
2. Next, navigate to the "Analysis Scope" tab.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/source-file-exclusion.png)
_Source files that should be ignored by the analysis_

Source File Exclusions are used to specify files or folders that SonarQube should not analyze as part of the codebase. These may include files or directories that are not directly part of the code but are still present in the project directory. 

Some common examples of such files or folders are:

* venv (virtualenv)
* htmlcov (coverage HTML format)
* node_modules (Node.js modules directory)

Code Coverage Exclusions are used to specify files or folders that should be excluded when calculating the coverage percentage.

Here are the patterns for the files and folders ignored:  
**/tests/**, **/migrations/**, **/admin.py, **/apps.py, core/asgi.py, core/wsgi.py, manage.py

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-13-06-55-38.png)
_Patterns used to exclude some files from coverage report and coverage percent calculation_

On the "Languages" tab, select "Python" as the programming language for the project. Then update the path to the coverage report as "_coverage_.xml".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/uo.png)
_Programming language selection and XML coverage report location_

Execute the previously provided command at the root directory:

```bash
sonar-scanner   -Dsonar.projectKey=DjangoSonar   -Dsonar.sources=.   -Dsonar.host.url=http://0.0.0.0:9000   -Dsonar.token=sqp_bb1dc2534249bf567c681f4acc440c2e278cb43f   -Dsonar.python.coverage.reportPaths=coverage.xml -Dsonar.python.version=3
```

If everything is functioning properly, you should see a successful result.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sonarsuccess.png)
_Running sonarqube analysis on the project with command given on the dashboard_

If you encounter errors related to unauthorized access or permission issues when trying to analyze a project locally, follow these steps:

1. Visit the SonarQube Administrator interface.
2. Navigate to the 'Security' section.
3. Look for the option labeled 'Force user authentication' and disable it.
4. Save the changes and rerun the analysis using the previous command.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/force-user-auth.png)
_Debugging authentication error during project analysis_

Another way to troubleshoot any errors is to visit the warning notifications and check for any errors encountered during the project analysis.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/WhatsApp-Image-2023-07-13-at-07.50.30.jpeg)
_Warning messages for analysis_

Click on "Overall Code" to access the overall code analysis section:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-13-07-18-26-1.png)
_SonarQube analysis result for the project on the dashboard_

## Wrapping Up

The complete source code for this project is available on [Github](https://github.com/ridwanray/django-sonarqube-pytest-coverage).

Remember to create a `.gitignore` file in the root directory of your GitHub repository to specify files and directories that should be ignored and not committed.

This article has explored the process of measuring Django code quality using powerful tools such as SonarQube, Pytest, and Coverage. By integrating these tools, you can gain insights into code health, write effective tests, and ensure adequate code coverage. 

Applying these practices enhances code quality, resulting in efficient development processes and high-quality software.

If you enjoyed this article, you can check out my [video collection](https://youtube.com/@ridwanray/) on [YouTube](https://youtube.com/@ridwanray/) to find more fun stuff to learn. And follow me on [LinkedIn](https://www.linkedin.com/in/ridwan-yusufa/)

### References:

* [https://github.com/amirajoodani/sonarqube](https://github.com/amirajoodani/sonarqube)
* [https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/)
* [https://coverage.readthedocs.io/en/7.2.7/](https://coverage.readthedocs.io/en/7.2.7/)
* [https://docs.pytest.org/en/7.1.x/getting-started.html](https://docs.pytest.org/en/7.1.x/getting-started.html)

  
  

