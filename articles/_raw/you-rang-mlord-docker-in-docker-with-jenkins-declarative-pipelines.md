---
title: You Rang, M'Lord? Docker in Docker with Jenkins declarative pipelines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-17T19:42:55.000Z'
originalURL: https://freecodecamp.org/news/you-rang-mlord-docker-in-docker-with-jenkins-declarative-pipelines
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/butler.jpg
tags:
- name: CI/CD
  slug: cicd
- name: dind
  slug: dind
- name: Docker
  slug: docker
- name: Jenkins
  slug: jenkins
seo_title: null
seo_desc: "By Balázs Tápai\nResources. When they are unlimited they are not important.\
  \ But when they're limited, boy do you have challenges! \nRecently, my team has\
  \ faced such a challenge ourselves: we realised that we needed to upgrade the Node\
  \ version on one of..."
---

By Balázs Tápai

Resources. When they are unlimited they are not important. But when they're limited, boy do you have challenges! 

Recently, my team has faced such a challenge ourselves: we realised that we needed to upgrade the Node version on one of our Jenkins agents so we could build and properly test our Angular 7 app. However, we learned that we would also lose the ability to build our legacy AngularJS apps which require Node 8. 

What were we to do?

Apart from eliminating the famous "It works on my machine" problem, Docker came in handy to tackle such a problem. However, there were certain challenges that needed to be addressed, such as Docker in Docker. 

For this purpose, after a long period of trial and error, we [built and published](https://hub.docker.com/repository/docker/btapai/pipelines) a [docker file](https://github.com/TapaiBalazs/build-pipeline-docker-images) that fit our team's needs. It helps run our builds, and it looks like the following:

```
1. Install dependencies
2. Lint the code
3. Run unit tests
4. Run SonarQube analysis
5. Build the application
6. Build a docker image which would be deployed
7. Run the docker container
8. Run cypress tests
9. Push docker image to the repository
10. Run another Jenkins job to deploy it to the environment
11. Generate unit and functional test reports and publish them
12. Stop any running containers
13. Notify chat/email about the build

```

## The docker image we needed

Our project is an Angular 7 project, which was generated using the `angular-cli`. We also have some dependencies that need Node 10.x.x. We lint our code with `tslint`, and run our unit tests with `Karma` and `Jasmine`. For the unit tests we need a Chrome browser installed so they can run with headless Chrome.

This is why we decided to use the `cypress/browsers:node10.16.0-chrome77` image. After we installed the dependencies, linted our code and ran our unit tests, we ran the [SonarQube](https://www.npmjs.com/package/sonar-scanner) analysis. This required us to have `Openjdk 8` as well.

```dockerfile
FROM cypress/browsers:node10.16.0-chrome77

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

```

Once the sonar scan was ready, we built the application. One of the strongest principles in testing is that you should test the thing that will be used by your users.  
That is the reason that we wanted to test the built code in exactly the same docker container as it would be in production. 

We could, of course serve the front-end from a very simple `nodejs` static server.  
But that would mean that everything an Apache HTTP server or an NGINX server usually did would be missing (for example all the proxies, `gzip` or `brotli`).

Now while this is a strong principle, the biggest problem was that we were already running inside a Docker container. That is why we needed DIND (Docker in Docker). 

After spending a whole day with my colleague researching, we found a solution which ended up working like a charm. The first and most important thing is that our build container needed the Docker executable.

```dockerfile
# Install Docker executable
RUN apt-get update && apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/debian \
        $(lsb_release -cs) \
        stable" \
    && apt-get update \
    && apt-get install -y \
        docker-ce

RUN usermod -u 1002 node && groupmod -g 1002 node && gpasswd -a node docker

```

As you can see we installed the docker executable and the necessary certificates, but we also added the rights and groups for our user. This second part is necessary because the host machine, our Jenkins agent, starts the container with `-u 1002:1002`. That is the user ID of our Jenkins agent which runs the container unprivileged.

Of course this isn't everything. When the container starts, the docker daemon of the host machine must be mounted. So we needed to start the build container  
with some extra parameters. It looks like the following in a Jenkinsfile:

```groovy
pipeline {
  agent {
    docker {
     image 'btapai/pipelines:node-10.16.0-chrome77-openjdk8-CETtime-dind'
     label 'frontend'
     args '-v /var/run/docker.sock:/var/run/docker.sock -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket -e HOME=${workspace} --group-add docker'
    }
  }

// ...
}

```

As you can see, we mounted two Unix sockets. `/var/run/docker.sock` mounts the docker daemon to the build container.

`/var/run/dbus/system_bus_socket` is a socket that allows cypress to run inside our container.

We needed `-e HOME=${workspace}` to avoid access rights issues during the build.

`--group-add docker` passes the host machines docker group down, so that inside the container our user can use the docker daemon.

With these proper arguments, we were able to build our image, start it up and run our cypress tests against it. 

But let's take a deep breath here. In Jenkins, we wanted to use multi-branch pipelines. Multibranch pipelines in Jenkins would create a Jenkins job for each branch that contained a Jenkinsfile. This meant that when we developed multiple branches they would have their own views.

There were some problems with this. The first problem was that if we built our image with the same name in all the branches, there would be conflicts (since our docker daemon was technically not inside our build container).

The second problem arose when the docker run command used the same port in every build (because you can't start the second container on a port that is already taken).

The third issue was getting the proper URL for the running application, because Dorothy, you are not in Localhost anymore.

Let's start with the naming. Getting a unique name is pretty easy with git, because commit hashes are unique. However, to get a unique port we had to use a little trick when we declared our environment variables:

```groovy
pipeline {

// ..

  environment {
    BUILD_PORT = sh(
        script: 'shuf -i 2000-65000 -n 1',
        returnStdout: true
    ).trim()
  }

// ...

    stage('Functional Tests') {
      steps {
        sh "docker run -d -p ${BUILD_PORT}:80 --name ${GIT_COMMIT} application"
        // be patient, we are going to get the url as well. :)
      }
    }

// ...

}

```

With the `shuf -i 2000-65000 -n 1` command on certain Linux distributions you can generate a random number. Our base image uses Debian so we were lucky here.  
The `GIT_COMMIT` environment variable was provided in Jenkins via the SCM plugin.

Now came the hard part: we were inside a docker container, there was no localhost, and the network inside docker containers can change.

It was also funny that when we started our container, it was running on the host machine's docker daemon. So technically it was not running inside our container. We had to reach it from the inside.

After several hours of investigation my colleague found a possible solution:  
`docker inspect --format "{{ .NetworkSettings.IPAddress }}"`

But it did not work, because that IP address was not an IP address inside the container, but rather outside it. 

Then we tried the `NetworkSettings.Gateway` property, which worked like a charm.  
So our Functional testing stage looked like the following:

```groovy
stage('Functional Tests') {
  steps {
    sh "docker run -d -p ${BUILD_PORT}:80 --name ${GIT_COMMIT} application"
    sh 'npm run cypress:run -- --config baseUrl=http://`docker inspect --format "{{ .NetworkSettings.Gateway }}" "${GIT_COMMIT}"`:${BUILD_PORT}'
  }
}

```

It was a wonderful feeling to see our cypress tests running inside a docker container. 

But then some of them failed miserably. Because the failing cypress tests expected to see some dates.

```javascript
cy.get("created-date-cell")
  .should("be.visible")
  .and("contain", "2019.12.24 12:33:17")

```

But because our build container was set to a different timezone, the displayed date on our front-end was different. 

Fortunately, it was an easy fix, and my colleague had seen it before. We installed the necessary time zones and locales. In our case we set the build container's timezone to `Europe/Budapest`, because our tests were written in this timezone.

```dockerfile
# SETUP-LOCALE
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends locales \
    && apt-get clean \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && sed -i -e 's/# hu_HU.UTF-8 UTF-8/hu_HU.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen

ENV LANG="en_US.UTF-8" \
    LANGUAGE= \
    LC_CTYPE="en_US.UTF-8" \
    LC_NUMERIC="hu_HU.UTF-8" \
    LC_TIME="hu_HU.UTF-8" \
    LC_COLLATE="en_US.UTF-8" \
    LC_MONETARY="hu_HU.UTF-8" \
    LC_MESSAGES="en_US.UTF-8" \
    LC_PAPER="hu_HU.UTF-8" \
    LC_NAME="hu_HU.UTF-8" \
    LC_ADDRESS="hu_HU.UTF-8" \
    LC_TELEPHONE="hu_HU.UTF-8" \
    LC_MEASUREMENT="hu_HU.UTF-8" \
    LC_IDENTIFICATION="hu_HU.UTF-8" \
    LC_ALL=

# SETUP-TIMEZONE
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends tzdata \
    && apt-get clean \
    && echo 'Europe/Budapest' > /etc/timezone && rm /etc/localtime \
    && ln -snf /usr/share/zoneinfo/'Europe/Budapest' /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

```

Since every crucial part of the build was now resolved, pushing the built image to the registry was just a docker push command. You can check out the whole dockerfile [here](https://github.com/TapaiBalazs/build-pipeline-docker-images/blob/master/pipelines/node-chrome-openjdk-CET-dind/Dockerfile).

One thing remained, which was to stop running containers when the cypress tests failed. We did this easily using the `always` post step.

```groovy
post {
  always {
    script {
      try {
        sh "docker stop ${GIT_COMMIT} && docker rm ${GIT_COMMIT}"
      } catch (Exception e) {
        echo 'No docker containers were running'
      }
    }
  }
}

```

Thank you very much for reading this blog post. I hope it helps you.

The original article can be read on my blog:

%[https://tapaibalazs.netlify.com/jenkins-and-docker-in-docker/]


