---
title: Vous avez sonné, M'Lord ? Docker dans Docker avec les pipelines déclaratifs
  Jenkins
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
seo_title: Vous avez sonné, M'Lord ? Docker dans Docker avec les pipelines déclaratifs
  Jenkins
seo_desc: "By Balázs Tápai\nResources. When they are unlimited they are not important.\
  \ But when they're limited, boy do you have challenges! \nRecently, my team has\
  \ faced such a challenge ourselves: we realised that we needed to upgrade the Node\
  \ version on one of..."
---

Par Balázs Tápai

Ressources. Lorsqu'elles sont illimitées, elles ne sont pas importantes. Mais lorsqu'elles sont limitées, oh là là, vous avez des défis ! 

Récemment, mon équipe a été confrontée à un tel défi : nous avons réalisé que nous devions mettre à niveau la version de Node sur l'un de nos agents Jenkins afin de pouvoir construire et tester correctement notre application Angular 7. Cependant, nous avons appris que nous perdrions également la capacité de construire nos applications AngularJS héritées qui nécessitent Node 8. 

Que devions-nous faire ?

Outre l'élimination du célèbre problème "Ça marche sur ma machine", Docker s'est avéré utile pour résoudre un tel problème. Cependant, certains défis devaient être relevés, comme Docker dans Docker. 

À cette fin, après une longue période d'essais et d'erreurs, nous avons [construit et publié](https://hub.docker.com/repository/docker/btapai/pipelines) un [fichier docker](https://github.com/TapaiBalazs/build-pipeline-docker-images) qui répondait aux besoins de notre équipe. Il aide à exécuter nos builds, et voici à quoi il ressemble :

```
1. Installer les dépendances
2. Analyser le code
3. Exécuter les tests unitaires
4. Exécuter l'analyse SonarQube
5. Construire l'application
6. Construire une image docker qui serait déployée
7. Exécuter le conteneur docker
8. Exécuter les tests cypress
9. Pousser l'image docker vers le dépôt
10. Exécuter un autre travail Jenkins pour la déployer dans l'environnement
11. Générer des rapports de tests unitaires et fonctionnels et les publier
12. Arrêter tous les conteneurs en cours d'exécution
13. Notifier le chat/email concernant le build

```

## L'image docker dont nous avions besoin

Notre projet est un projet Angular 7, qui a été généré en utilisant `angular-cli`. Nous avons également quelques dépendances qui nécessitent Node 10.x.x. Nous analysons notre code avec `tslint`, et exécutons nos tests unitaires avec `Karma` et `Jasmine`. Pour les tests unitaires, nous avons besoin d'un navigateur Chrome installé pour qu'ils puissent s'exécuter avec Chrome en mode headless.

C'est pourquoi nous avons décidé d'utiliser l'image `cypress/browsers:node10.16.0-chrome77`. Après avoir installé les dépendances, analysé notre code et exécuté nos tests unitaires, nous avons exécuté l'analyse [SonarQube](https://www.npmjs.com/package/sonar-scanner). Cela nous a nécessité d'avoir également `Openjdk 8`.

```dockerfile
FROM cypress/browsers:node10.16.0-chrome77

# Installer OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Corriger les problèmes de certificats
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Configurer JAVA_HOME -- utile pour la ligne de commande docker
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

```

Une fois l'analyse sonar prête, nous avons construit l'application. L'un des principes les plus forts en matière de test est que vous devez tester la chose qui sera utilisée par vos utilisateurs. 
C'est la raison pour laquelle nous voulions tester le code construit dans exactement le même conteneur docker que celui qui serait en production. 

Nous aurions bien sûr pu servir le front-end à partir d'un serveur statique `nodejs` très simple. 
Mais cela signifierait que tout ce qu'un serveur Apache HTTP ou un serveur NGINX fait habituellement serait manquant (par exemple tous les proxies, `gzip` ou `brotli`).

Maintenant, bien que ce soit un principe fort, le plus gros problème était que nous étions déjà en train de fonctionner à l'intérieur d'un conteneur Docker. C'est pourquoi nous avions besoin de DIND (Docker dans Docker). 

Après avoir passé une journée entière avec mon collègue à faire des recherches, nous avons trouvé une solution qui a fini par fonctionner à merveille. La première et la plus importante chose est que notre conteneur de build avait besoin de l'exécutable Docker.

```dockerfile
# Installer l'exécutable Docker
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

Comme vous pouvez le voir, nous avons installé l'exécutable docker et les certificats nécessaires, mais nous avons également ajouté les droits et groupes pour notre utilisateur. Cette deuxième partie est nécessaire car la machine hôte, notre agent Jenkins, démarre le conteneur avec `-u 1002:1002`. C'est l'ID utilisateur de notre agent Jenkins qui exécute le conteneur non privilégié.

Bien sûr, ce n'est pas tout. Lorsque le conteneur démarre, le démon docker de la machine hôte doit être monté. Nous avons donc dû démarrer le conteneur de build 
avec certains paramètres supplémentaires. Voici à quoi cela ressemble dans un Jenkinsfile :

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

Comme vous pouvez le voir, nous avons monté deux sockets Unix. `/var/run/docker.sock` monte le démon docker dans le conteneur de build.

`/var/run/dbus/system_bus_socket` est un socket qui permet à cypress de s'exécuter à l'intérieur de notre conteneur.

Nous avions besoin de `-e HOME=${workspace}` pour éviter les problèmes de droits d'accès pendant la construction.

`--group-add docker` transmet le groupe docker des machines hôtes, afin que, à l'intérieur du conteneur, notre utilisateur puisse utiliser le démon docker.

Avec ces arguments appropriés, nous avons pu construire notre image, la démarrer et exécuter nos tests cypress contre elle. 

Mais prenons une profonde inspiration ici. Dans Jenkins, nous voulions utiliser des pipelines multi-branches. Les pipelines multi-branches dans Jenkins créeraient un travail Jenkins pour chaque branche contenant un Jenkinsfile. Cela signifiait que lorsque nous développons plusieurs branches, elles auraient leurs propres vues.

Il y avait quelques problèmes avec cela. Le premier problème était que si nous construisions notre image avec le même nom dans toutes les branches, il y aurait des conflits (puisque notre démon docker n'était techniquement pas à l'intérieur de notre conteneur de build).

Le deuxième problème est survenu lorsque la commande docker run utilisait le même port dans chaque build (car vous ne pouvez pas démarrer le deuxième conteneur sur un port déjà pris).

Le troisième problème était d'obtenir l'URL correcte pour l'application en cours d'exécution, car Dorothy, vous n'êtes plus en Localhost.

Commençons par le nommage. Obtenir un nom unique est assez facile avec git, car les hachages de commit sont uniques. Cependant, pour obtenir un port unique, nous avons dû utiliser un petit truc lorsque nous avons déclaré nos variables d'environnement :

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
        // soyez patient, nous allons obtenir l'url aussi. :)
      }
    }

// ...

}

```

Avec la commande `shuf -i 2000-65000 -n 1` sur certaines distributions Linux, vous pouvez générer un nombre aléatoire. Notre image de base utilise Debian, donc nous avons eu de la chance ici. 
La variable d'environnement `GIT_COMMIT` était fournie dans Jenkins via le plugin SCM.

Maintenant, la partie difficile : nous étions à l'intérieur d'un conteneur docker, il n'y avait pas de localhost, et le réseau à l'intérieur des conteneurs docker peut changer.

C'était aussi drôle que lorsque nous avons démarré notre conteneur, il s'exécutait sur le démon docker de la machine hôte. Donc techniquement, il ne s'exécutait pas à l'intérieur de notre conteneur. Nous devions l'atteindre de l'intérieur.

Après plusieurs heures d'investigation, mon collègue a trouvé une solution possible : 
`docker inspect --format "{{ .NetworkSettings.IPAddress }}"`

Mais cela n'a pas fonctionné, car cette adresse IP n'était pas une adresse IP à l'intérieur du conteneur, mais plutôt à l'extérieur.

Nous avons ensuite essayé la propriété `NetworkSettings.Gateway`, qui a fonctionné à merveille. 
Ainsi, notre étape de test fonctionnel ressemblait à ce qui suit :

```groovy
stage('Functional Tests') {
  steps {
    sh "docker run -d -p ${BUILD_PORT}:80 --name ${GIT_COMMIT} application"
    sh 'npm run cypress:run -- --config baseUrl=http://`docker inspect --format "{{ .NetworkSettings.Gateway }}" "${GIT_COMMIT}"`:${BUILD_PORT}'
  }
}

```

C'était une sensation merveilleuse de voir nos tests cypress s'exécuter à l'intérieur d'un conteneur docker. 

Mais ensuite, certains d'entre eux ont échoué misérablement. Parce que les tests cypress qui ont échoué s'attendaient à voir certaines dates.

```javascript
cy.get("created-date-cell")
  .should("be.visible")
  .and("contain", "2019.12.24 12:33:17")

```

Mais parce que notre conteneur de build était réglé sur un fuseau horaire différent, la date affichée sur notre front-end était différente. 

Heureusement, c'était une correction facile, et mon collègue l'avait déjà vue auparavant. Nous avons installé les fuseaux horaires et les locales nécessaires. Dans notre cas, nous avons réglé le fuseau horaire du conteneur de build sur `Europe/Budapest`, car nos tests étaient écrits dans ce fuseau horaire.

```dockerfile
# CONFIGURATION-LOCALE
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

# CONFIGURATION-FUSEAU HORAIRE
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends tzdata \
    && apt-get clean \
    && echo 'Europe/Budapest' > /etc/timezone && rm /etc/localtime \
    && ln -snf /usr/share/zoneinfo/'Europe/Budapest' /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

```

Puisque chaque partie cruciale de la construction était maintenant résolue, pousser l'image construite vers le registre n'était qu'une commande docker push. Vous pouvez consulter l'ensemble du dockerfile [ici](https://github.com/TapaiBalazs/build-pipeline-docker-images/blob/master/pipelines/node-chrome-openjdk-CET-dind/Dockerfile).

Une chose restait à faire, qui était d'arrêter les conteneurs en cours d'exécution lorsque les tests cypress échouaient. Nous l'avons fait facilement en utilisant l'étape post `always`.

```groovy
post {
  always {
    script {
      try {
        sh "docker stop ${GIT_COMMIT} && docker rm ${GIT_COMMIT}"
      } catch (Exception e) {
        echo 'Aucun conteneur docker n'était en cours d'exécution'
      }
    }
  }
}

```

Merci beaucoup d'avoir lu cet article de blog. J'espère qu'il vous aide.

L'article original peut être lu sur mon blog :

%[https://tapaibalazs.netlify.com/jenkins-and-docker-in-docker/]