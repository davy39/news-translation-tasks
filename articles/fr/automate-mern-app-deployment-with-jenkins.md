---
title: Développement d'applications MERN – Comment construire un pipeline CI/CD avec
  Jenkins
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-08T17:42:07.000Z'
originalURL: https://freecodecamp.org/news/automate-mern-app-deployment-with-jenkins
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/CICD-Pipeline-with-Jenkins.png
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
- name: Express
  slug: express
- name: Jenkins
  slug: jenkins
- name: mongo
  slug: mongo
- name: node
  slug: node
- name: React
  slug: react
seo_title: Développement d'applications MERN – Comment construire un pipeline CI/CD
  avec Jenkins
seo_desc: "By Rakesh Potnuru\nAs you continue to develop your software, you must also\
  \ continue to integrate it with previous code and deploy it to servers. \nManually\
  \ doing this is a time-consuming process that can occasionally result in errors.\
  \ So we need to do ..."
---

Par Rakesh Potnuru

Alors que vous continuez à développer votre logiciel, vous devez également continuer à l'intégrer avec le code précédent et à le déployer sur des serveurs. 

Faire cela manuellement est un processus chronophage qui peut parfois entraîner des erreurs. Nous devons donc le faire de manière continue et automatisée – ce que vous apprendrez dans cet article.

Nous allons voir comment vous pouvez améliorer votre processus de développement d'applications MERN (MongoDB, Express, React et NodeJs) en configurant un pipeline CI/CD avec Jenkins. Vous verrez comment automatiser le déploiement pour des mises en production plus rapides et plus efficaces.

## Commençons

### Prérequis

* Compréhension de base des technologies de la stack MERN.
* Compréhension de base de Docker.
* Obtenez le code source depuis [GitHub](https://github.com/itsrakeshhq/productivity-app)

## Le Problème

Prenons cette [application de productivité](https://github.com/itsrakeshhq/productivity-app) – c'est un projet MERN que nous allons utiliser dans cet article. Il y a de nombreuses étapes que nous devons accomplir, de la construction de l'application à son envoi vers Docker Hub. 

Tout d'abord, nous devons exécuter des tests avec une commande pour déterminer si tous les tests passent ou non. Si tous les tests passent, nous construisons les images Docker puis nous envoyons ces images vers Docker Hub. Si votre application est extrêmement complexe, vous devrez peut-être prendre des étapes supplémentaires. 

Maintenant, imaginez que nous faisons tout cela manuellement, ce qui prend du temps et peut entraîner des erreurs.

![Mème d'attente de déploiement sans DevOps](https://i.imgur.com/iWAmMm4.jpg)
_Mème d'attente de déploiement sans DevOps_

## La Solution

Pour résoudre ce problème, nous pouvons créer un pipeline CI/CD. Ainsi, chaque fois que vous ajoutez une fonctionnalité ou corrigez un bug, ce pipeline est déclenché. Cela effectue automatiquement toutes les étapes, des tests au déploiement.

## Qu'est-ce que le CI/CD et pourquoi est-ce important ?

L'**I**ntégration **C**ontinue et le **D**éploiement **C**ontinu (CI/CD) est une série d'étapes effectuées pour automatiser l'intégration et le déploiement de logiciels. Le CI/CD est le cœur de DevOps.

![Étapes du CI/CD](https://i.imgur.com/uMFtPwJ.png)
_Étapes du CI/CD_

Du développement au déploiement, notre application MERN passe par quatre étapes majeures : les tests, la construction des images Docker, l'envoi vers un registre et le déploiement sur un fournisseur de cloud. Tout cela est fait manuellement en exécutant diverses commandes. Et nous devons faire cela chaque fois qu'une nouvelle fonctionnalité est ajoutée ou qu'un bug est corrigé. 

Mais cela réduit considérablement la productivité des développeurs, c'est pourquoi le CI/CD peut être si utile pour automatiser ce processus. Dans cet article, nous couvrirons les étapes jusqu'à l'envoi vers le registre.

![Mème CI/CD](https://i.imgur.com/g2omESy.png)
_Mème CI/CD_

## Le Projet

Le projet que nous allons utiliser dans ce tutoriel est une application full-stack MERN très simple.

![Démonstration du projet](https://i.imgur.com/GSvRlQ0.gif)
_Démonstration du projet_

Il contient deux microservices.

1. Frontend
2. Backend

Vous pouvez en savoir plus sur le projet [ici](https://blog.itsrakesh.co/lets-build-and-deploy-a-full-stack-mern-web-application).

Ces deux applications contiennent un Dockerfile. Vous pouvez apprendre à dockeriser une application MERN [ici](https://blog.itsrakesh.co/dockerizing-your-mern-stack-app-a-step-by-step-guide).

## Qu'est-ce que Jenkins ?

Pour exécuter un pipeline CI/CD, nous avons besoin d'un serveur CI/CD. C'est là que toutes les étapes écrites dans un pipeline s'exécutent. 

Il existe de nombreux services disponibles sur le marché, notamment GitHub Actions, Travis CI, Circle CI, GitLab CI/CD, AWS CodePipeline, Azure DevOps et Google Cloud Build. Jenkins est l'un des outils CI/CD populaires, et c'est ce que nous allons utiliser ici.

## Comment configurer un serveur Jenkins sur Azure

Puisque Jenkins est open source et qu'il ne fournit pas de solution cloud, nous devons soit l'exécuter localement, soit l'auto-héberger sur un fournisseur de cloud. Maintenant, l'exécuter localement peut être difficile, en particulier pour les utilisateurs de Windows. Par conséquent, j'ai choisi de l'auto-héberger sur Azure pour cette démonstration.

Si vous souhaitez l'exécuter localement ou l'auto-héberger ailleurs qu'Azure (suivez [ces](https://www.jenkins.io/doc/book/installing/) guides de Jenkins), passez cette section et allez à la section **Comment configurer Jenkins**. 

Tout d'abord, vous devrez vous connecter à votre compte [Azure](https://Azure.microsoft.com?wt.mc_id=studentamb_90351) (créez-en un si vous n'en avez pas déjà un). Ouvrez Azure Cloud Shell.

![Ouverture de Azure Cloud Shell](https://i.imgur.com/IN6RXAe.png)
_Ouverture de Azure Cloud Shell_

Créez ensuite un répertoire appelé `jenkins` pour stocker toute la configuration de Jenkins, et basculez vers ce répertoire :

```bash
mkdir jenkins
cd jenkins

```

Créez un fichier appelé `cloud-init-jenkins.txt`. Ouvrez-le avec nano ou vim,

```bash
touch cloud-init-jenkins.txt
nano cloud-init-jenkins.txt

```

et collez ce code dedans :

```bash
#cloud-config
package_upgrade: true
runcmd:
  - sudo apt install openjdk-11-jre -y
  - wget -qO - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
  - sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
  - sudo apt-get update && sudo apt-get install jenkins -y
  - sudo service jenkins restart

```

Ici, nous allons utiliser ce fichier pour installer Jenkins après avoir créé une machine virtuelle. Tout d'abord, nous installons openjdk, qui est requis pour que Jenkins fonctionne. Ensuite, nous redémarrons le service Jenkins après l'avoir installé.

Ensuite, créez un groupe de ressources. (Un groupe de ressources dans Azure est comme un conteneur qui contient toutes les ressources liées d'un projet dans un seul groupe. En savoir plus sur les groupes de ressources [ici](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group?wt.mc_id=studentamb_90351).)

```bash
az group create --name jenkins-rg --location centralindia

```

**Note :** assurez-vous de changer l'emplacement pour celui qui est le plus proche de vous.

Maintenant, créez une machine virtuelle.

```bash
az vm create \
--resource-group jenkins-rg \
--name jenkins-vm \
--image UbuntuLTS \
--admin-username "azureuser" \
--generate-ssh-keys \
--public-ip-sku Standard \
--custom-data cloud-init-jenkins.txt

```

Vous pouvez vérifier l'installation de la VM avec cette commande :

```bash
az vm list -d -o table --query "[?name=='jenkins-vm']"

```

Ne soyez pas confus. Cette commande affiche simplement les données JSON dans un format tabulaire pour une vérification facile.

Le serveur Jenkins s'exécute sur le port `8080`, nous devons donc exposer ce port sur notre VM. Vous pouvez le faire comme ceci :

```bash
az vm open-port \
--resource-group jenkins-rg \
--name jenkins-vm  \
--port 8080 --priority 1010

```

Maintenant, nous pouvons accéder au tableau de bord Jenkins dans le navigateur avec l'URL `http://<votre-ip-vm>:8080`. Utilisez cette commande pour obtenir l'adresse IP de la VM :

```bash
az vm show \
--resource-group jenkins-rg \
--name jenkins-vm -d \
--query [publicIps] \
--output tsv

```

Vous pouvez maintenant voir l'application Jenkins dans votre navigateur.

![Tableau de bord Jenkins](https://i.imgur.com/Sy1Glar.png)
_Tableau de bord Jenkins_

Comme vous le remarquerez, Jenkins nous demande de fournir un mot de passe administrateur qui est généré automatiquement lors de son installation.

Mais d'abord, connectons-nous en SSH à notre machine virtuelle où Jenkins est installé.

```bash
ssh azureuser@<ip_address>

```

Maintenant, tapez la commande suivante pour obtenir le mot de passe :

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

```

Copiez et collez-le. Ensuite, cliquez sur **Continuer**.

## Comment configurer Jenkins

Tout d'abord, vous devrez cliquer sur **Installer les plugins suggérés**. Cela prendra un certain temps pour installer tous les plugins.

![Installation des plugins suggérés](https://i.imgur.com/vDaaqE3.png)
_Installation des plugins suggérés_

Un utilisateur administrateur est nécessaire pour restreindre l'accès à Jenkins. Alors allez-y et créez-en un. Après avoir terminé, cliquez sur **Enregistrer et continuer**.

![Créer un utilisateur administrateur](https://i.imgur.com/qqkwQN6.png)
_Créer un utilisateur administrateur_

Maintenant, vous serez présenté avec le tableau de bord Jenkins.

La première étape consiste à installer le plugin "Blue Ocean". Jenkins a une interface très ancienne, ce qui peut rendre son utilisation difficile pour certaines personnes. Ce plugin Blue Ocean fournit une interface moderne pour certains composants de Jenkins (comme la création d'un pipeline).

Pour installer des plugins, allez dans **Gérer Jenkins** -> cliquez sur **Gérer les plugins** sous "Configuration du système" -> **Plugins disponibles**. Recherchez "Blue Ocean" -> cochez la case et cliquez sur **Télécharger maintenant et installer après redémarrage**.

![Blue Ocean](https://i.imgur.com/dAKBLiq.png)
_Blue Ocean_

Super, nous sommes prêts. Maintenant, créons un pipeline.

## Comment écrire un Jenkinsfile

Pour créer un pipeline, nous avons besoin d'un **Jenkinsfile**. Ce fichier contient toutes les configurations du pipeline – étapes, étapes, etc. Jenkinsfile est à Jenkins ce qu'un Dockerfile est à Docker.

Jenkinsfile utilise la syntaxe **Groovy**. La syntaxe est très simple. Vous pouvez tout comprendre simplement en la regardant.

Commençons par écrire :

```groovy
pipeline {

}

```

Le mot 'agent' doit être la première chose que vous mentionnez dans le pipeline. Un agent est similaire à un conteneur ou un environnement dans lequel les jobs s'exécutent. Vous pouvez utiliser plusieurs agents pour exécuter des jobs en parallèle. Vous pouvez trouver plus d'informations sur les agents Jenkins [ici](https://www.jenkins.io/doc/book/using/using-agents/).

```groovy
pipeline {
	agent any
}

```

Ici, nous disons à Jenkins d'utiliser n'importe quel agent disponible.

Nous avons un total de 5 étapes dans notre pipeline :

![Étapes du pipeline CI/CD](https://i.imgur.com/ezvdElo.png)
_Étapes du pipeline CI/CD_

### Étape 1 : Récupérer le code

Différents outils CI/CD utilisent différentes conventions de nommage. Dans Jenkins, celles-ci sont appelées étapes. Dans chaque étape, nous écrivons diverses étapes.

Notre première étape consiste à récupérer le code depuis un système de gestion de code source (dans notre cas, GitHub).

```groovy
pipeline {
	agent any

	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
	}
}

```

Validez les modifications et envoyez-les à votre dépôt GitHub.

Puisque nous n'avons pas encore créé de pipelines, faisons cela maintenant.

Avant de commencer, nous devons nous assurer que Git est installé sur notre système. Si vous avez suivi mes étapes précédentes pour installer Jenkins sur une VM Azure, Git est déjà installé. 

Vous pouvez le tester en exécutant la commande suivante (assurez-vous d'être toujours connecté en SSH à la VM) :

```bash
git --version

```

Si ce n'est pas déjà installé, vous pouvez le faire avec :

```bash
sudo apt install git

```

Ouvrez Blue Ocean. Cliquez sur **Créer un nouveau pipeline**.

![Création d'un nouveau pipeline](https://i.imgur.com/FNffT6p.png)
_Création d'un nouveau pipeline_

Ensuite, sélectionnez votre système de gestion de code source. Si vous avez choisi GitHub, vous devez fournir un jeton d'accès pour que Jenkins puisse accéder à votre dépôt. Je recommande de cliquer sur **Créer un jeton d'accès ici** car il s'agit d'un modèle avec toutes les permissions nécessaires. Ensuite, cliquez sur **Connecter**.

![Sélection du SCM](https://i.imgur.com/H9TUsHV.png)
_Sélection du SCM_

Après cela, un pipeline sera créé. Puisque notre dépôt contient déjà un Jenkinsfile, Jenkins le détecte automatiquement et exécute les étapes et étapes que nous avons mentionnées dans le pipeline.

Si tout s'est bien passé, toute la page deviendra verte. (Autres couleurs : **bleu** indique que le pipeline est en cours d'exécution, **rouge** indique qu'il y a eu un problème dans le pipeline, et **gris** indique que nous avons arrêté le pipeline.)

![Première étape réussie](https://i.imgur.com/FtvJlND.png)
_Première étape réussie_

### Étape 2 : Exécuter les tests du frontend

En général, tous les pipelines CI/CD contiennent des tests qui doivent être exécutés avant le déploiement. J'ai donc ajouté des tests simples au frontend et au backend. Commençons par les tests du frontend.

```groovy
stage('Client Tests') {
	steps {
		dir('client') {
			sh 'npm install'
			sh 'npm test'
		}
	}
}

```

Nous changeons le répertoire pour `client/` car c'est là que se trouve le code du frontend. Ensuite, nous installons les dépendances avec `npm install` et exécutons les tests avec `npm test` dans un shell.

Encore une fois, avant de redémarrer le pipeline, nous devons nous assurer que node et npm sont installés ou non. Installez node et npm avec ces commandes dans la machine virtuelle :

```bash
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -

```

Après cela, exécutez ce qui suit :

```bash
sudo apt-get install -y nodejs

```

Maintenant, validez le code et redémarrez le pipeline.

![Exécuter les tests du client](https://i.imgur.com/OWYcdDu.png)
_Exécuter les tests du client_

### Étape 3 : Exécuter les tests du backend

Maintenant, faites la même chose pour les tests du backend.

Mais il y a une chose que nous devons faire avant de continuer. Si vous regardez le code et `activity.test.js`, nous utilisons quelques variables d'environnement. Ajoutons donc ces variables d'environnement dans Jenkins.

#### Comment ajouter des variables d'environnement dans Jenkins

Pour ajouter des variables d'environnement, allez dans **Gérer Jenkins** -> cliquez sur **Gérer les identifiants** sous "Sécurité" -> **Système** -> **Identifiants globaux (non restreints)** -> cliquez sur **+ Ajouter des identifiants**.

Pour **Type**, sélectionnez "Texte secret", laissez **Portée** par défaut, et pour **Secret**, écrivez la valeur secrète et **ID**. C'est ce que nous utilisons lorsque nous utilisons ces variables d'environnement dans le Jenkinsfile.

Ajoutez les variables d'environnement suivantes :

![Variables d'environnement](https://i.imgur.com/xGjg2mG.png)
_Variables d'environnement_

Ensuite, dans le Jenkinsfile, utilisez ces variables d'environnement :

```groovy
environment {
	MONGODB_URI = credentials('mongodb-uri')
	TOKEN_KEY = credentials('token-key')
	EMAIL = credentials('email')
	PASSWORD = credentials('password')
}

```

Ajoutez une étape pour installer les dépendances, définissez ces variables dans l'environnement Jenkins et exécutez les tests :

```groovy
stage('Server Tests') {
	steps {
		dir('server') {
			sh 'npm install'
			sh 'export MONGODB_URI=$MONGODB_URI'
			sh 'export TOKEN_KEY=$TOKEN_KEY'
			sh 'export EMAIL=$EMAIL'
			sh 'export PASSWORD=$PASSWORD'
			sh 'npm test'
		}
	}
}

```

Encore une fois, validez le code et redémarrez le pipeline.

![Exécuter les tests du serveur](https://i.imgur.com/hpjMUyT.png)
_Exécuter les tests du serveur_

### Étape 4 : Construire les images Docker

Maintenant, nous devons spécifier une étape pour construire les images Docker à partir des Dockerfiles.

Avant de continuer, installez Docker dans la VM (si ce n'est pas déjà fait).

Pour installer Docker :

```bash
sudo apt install docker.io

```

Ajoutez l'utilisateur `jenkins` au groupe `docker` afin que Jenkins puisse accéder au démon Docker – sinon vous obtiendrez une erreur de permission refusée.

```bash
sudo usermod -a -G docker jenkins

```

Ensuite, redémarrez le service `jenkins`.

```bash
sudo systemctl restart jenkins

```

Ajoutez une étape dans le Jenkinsfile.

```groovy
stage('Build Images') {
	steps {
		sh 'docker build -t rakeshpotnuru/productivity-app:client-latest client'
		sh 'docker build -t rakeshpotnuru/productivity-app:server-latest server'
	}
}

```

Validez le code et redémarrez le pipeline.

![Construire les images Docker](https://i.imgur.com/USh63SD.png)
_Construire les images Docker_

### Étape 5 : Envoyer les images vers le registre

En tant qu'étape finale, nous allons envoyer les images vers Docker Hub.

Avant cela, ajoutez votre nom d'utilisateur et mot de passe Docker Hub au gestionnaire d'identifiants Jenkins, mais pour **Type**, choisissez "Nom d'utilisateur avec mot de passe".

![Type d'identifiant nom d'utilisateur avec mot de passe](https://i.imgur.com/ue0MMKM.png)
_Type d'identifiant nom d'utilisateur avec mot de passe_

Ajoutez l'étape finale où nous nous connectons et envoyons les images vers Docker Hub.

```groovy
stage('Push Images to DockerHub') {
	steps {
		withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
			sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
			sh 'docker push rakeshpotnuru/productivity-app:client-latest'
			sh 'docker push rakeshpotnuru/productivity-app:server-latest'
		}
	}
}

```

![Envoyer les images vers DockerHub](https://i.imgur.com/copfIou.png)
_Envoyer les images vers DockerHub_

Voici le Jenkinsfile complet :

```groovy
// Ceci est un Jenkinsfile. C'est un script que Jenkins exécutera lorsqu'un build sera déclenché.
pipeline {
    // Indique à Jenkins d'exécuter le pipeline sur n'importe quel agent disponible.
    agent any

    // Définition des variables d'environnement pour le build.
    environment {
        MONGODB_URI = credentials('mongodb-uri')
        TOKEN_KEY = credentials('token-key')
        EMAIL = credentials('email')
        PASSWORD = credentials('password')
    }

    // Ceci est le pipeline. C'est une série d'étapes que Jenkins exécutera.
    stages {
        // Cette étape indique à Jenkins de récupérer le code source depuis le système de gestion de code source.
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Cette étape indique à Jenkins d'exécuter les tests dans le répertoire client.
        stage('Client Tests') {
            steps {
                dir('client') {
                    sh 'npm install'
                    sh 'npm test'
                }
            }
        }
        
        // Cette étape indique à Jenkins d'exécuter les tests dans le répertoire serveur.
        stage('Server Tests') {
            steps {
                dir('server') {
                    sh 'npm install'
                    sh 'export MONGODB_URI=$MONGODB_URI'
                    sh 'export TOKEN_KEY=$TOKEN_KEY'
                    sh 'export EMAIL=$EMAIL'
                    sh 'export PASSWORD=$PASSWORD'
                    sh 'npm test'
                }
            }
        }
        
        // Cette étape indique à Jenkins de construire les images pour le client et le serveur.
        stage('Build Images') {
            steps {
                sh 'docker build -t rakeshpotnuru/productivity-app:client-latest client'
                sh 'docker build -t rakeshpotnuru/productivity-app:server-latest server'
            }
        }
        
        // Cette étape indique à Jenkins d'envoyer les images vers DockerHub.
        stage('Push Images to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker push rakeshpotnuru/productivity-app:client-latest'
                    sh 'docker push rakeshpotnuru/productivity-app:server-latest'
                }
            }
        }
    }
}

```

![Pipeline exécuté avec succès](https://i.imgur.com/NQxFXhO.png)
_Pipeline exécuté avec succès_

## Conclusion

En résumé, passons en revue ce que nous avons couvert :

* Nous avons exploré l'importance de la mise en œuvre de l'Intégration Continue et du Déploiement Continu (CI/CD) dans le développement logiciel.
* Nous avons approfondi les fondamentaux de Jenkins et acquis des connaissances sur la manière de déployer un serveur Jenkins sur la plateforme cloud Azure.
* Nous avons personnalisé Jenkins pour répondre à nos besoins spécifiques.
* Enfin, nous avons écrit un Jenkinsfile et construit un pipeline en utilisant l'interface conviviale de Jenkins Blue Ocean.

C'est tout pour l'instant ! Merci d'avoir lu 🙂.

Connectez-vous avec moi sur [twitter](https://twitter.com/rakesh_at_tweet).