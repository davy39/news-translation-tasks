---
title: Comment sécuriser votre serveur web avec l'intégration continue en utilisant
  NGINX et CircleCI
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-01-19T16:46:59.000Z'
originalURL: https://freecodecamp.org/news/secure-web-server-with-continuous-integration-using-nginx-and-circleci
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/feature-image.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: nginx
  slug: nginx
- name: Security
  slug: security
seo_title: Comment sécuriser votre serveur web avec l'intégration continue en utilisant
  NGINX et CircleCI
seo_desc: 'Web servers are responsible for delivering web pages and various resources
  to clients through the internet. They can exist either as software or hardware components.

  But unfortunately, they often become targets for hackers and malicious individuals
  s...'
---

Les serveurs web sont responsables de la livraison de pages web et de diverses ressources aux clients via Internet. Ils peuvent exister sous forme de composants logiciels ou matériels.

Malheureusement, ils deviennent souvent des cibles pour les pirates et les individus malveillants cherchant à exploiter toute vulnérabilité pour compromettre les données et perturber le fonctionnement. Par conséquent, vous devrez donner la priorité à la sécurité de votre serveur web en le mettant à jour et en implémentant des mesures de protection contre les menaces.

Pour améliorer la sécurité de votre serveur web, une approche efficace consiste à utiliser l'[intégration continue](https://www.freecodecamp.org/news/what-is-ci-cd/) (CI). La CI est une technique DevOps qui permet la fusion automatisée des modifications de code des ingénieurs logiciels dans un seul dépôt. Cette pratique améliore la qualité du code, minimise les bugs et accélère la livraison du code.

En utilisant la CI, vous pouvez automatiser les processus de test, de construction et de déploiement pour le code et la configuration de vos serveurs web. Vous pouvez également vous assurer que votre serveur web maintient constamment un état stable.

Dans ce tutoriel, je vais vous guider à travers le processus de renforcement de la sécurité de votre serveur web en utilisant deux outils populaires et puissants : [NGINX](https://www.freecodecamp.org/news/nginx/) et CircleCI.

NGINX, qui est un serveur web open source, fournit une gamme de fonctionnalités et de modules qui peuvent grandement améliorer la sécurité de votre serveur web. Ceux-ci incluent le chiffrement SSL/TLS, les en-têtes de sécurité et la prise en charge de HTTP/2.

D'autre part, CircleCI offre des options basées sur le cloud et auto-hébergées pour l'intégration continue (CI) et la livraison continue (CD), permettant des processus de déploiement fluides.

En suivant ce guide, vous apprendrez comment :

* Configurer NGINX pour utiliser le chiffrement SSL/TLS et les en-têtes de sécurité

* Créer un dépôt GitHub et pousser vos fichiers de configuration NGINX vers celui-ci

* Créer un projet CircleCI et le lier à votre dépôt GitHub

* Créer un fichier de configuration CircleCI et définir votre pipeline CI

* Tester et déployer votre serveur web avec CircleCI

### Voici ce que nous allons couvrir :

* [Prérequis](#)

* [Étape 1 : Configurer NGINX pour utiliser le chiffrement SSL/TLS](#configurer-nginx-pour-utiliser-le-chiffrement-ssl-tls)

* [Étape 2 : Configurer NGINX pour inclure les en-têtes de sécurité](#)

* [Étape 3 : Créer un dépôt GitHub et pousser votre configuration NGINX](#)

* [Étape 4 : Créer un projet CircleCI et le lier à votre dépôt GitHub](#)

* [Étape 5 : Créer un fichier de configuration CircleCI et définir votre pipeline CI](#)

* [Étape 6 : Tester et déployer votre serveur web avec CircleCI](#)

Commençons !

## Prérequis

Avant de commencer ce guide, vous devez vous assurer que vous avez les éléments suivants :

* Un serveur web exécutant NGINX. Si vous n'en avez pas, vous pouvez suivre ce [guide](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04) pour installer NGINX sur Ubuntu 20.04. Vous pouvez également utiliser tout autre système d'exploitation ou fournisseur de cloud qui prend en charge NGINX.

* Un compte GitHub. Si vous n'en avez pas, vous pouvez vous inscrire gratuitement [ici](https://github.com/join).

* Un compte CircleCI. Si vous n'en avez pas, vous pouvez vous inscrire gratuitement [ici](https://circleci.com/signup/). Vous devrez également lier votre compte GitHub à votre compte CircleCI.

* Certaines connaissances de base en [développement web](https://www.freecodecamp.org/news/learn-web-development-with-this-free-20-hour-course/) et en [commandes Linux](https://www.freecodecamp.org/news/helpful-linux-commands-you-should-know/). Vous devriez être familier avec les concepts de serveurs web, de chiffrement SSL/TLS, d'en-têtes de sécurité et de CI. Vous devriez également être à l'aise avec l'utilisation de la ligne de commande et l'édition de fichiers de configuration.

Une fois que vous avez ces éléments, vous êtes prêt à procéder aux étapes suivantes.

## Étape 1 : Configurer NGINX pour utiliser le chiffrement SSL/TLS

Le chiffrement SSL/TLS garantit la transmission des données entre votre serveur web et les clients. Il protège contre l'interception ou la manipulation des informations. Il joue également un rôle dans la vérification de l'identité et de la fiabilité de votre serveur web.

Vous avez besoin d'un certificat SSL/TLS pour utiliser SSL/TLS pour votre serveur web. Un certificat SSL/TLS contient des informations sur votre serveur web, telles que son nom de domaine, son propriétaire et sa clé publique. La validité du certificat est vérifiée par la signature numérique unique d'une autorité de certification (CA).

Vous pouvez soit acheter un certificat SSL/TLS auprès d'une autorité de certification commerciale, telle que DigiCert, Symantec ou GlobalSign, soit en obtenir un gratuitement auprès d'une autorité de certification à but non lucratif, telle que Let's Encrypt. Vous pouvez également créer votre propre certificat auto-signé, mais cela n'est pas recommandé pour une utilisation en production, car il ne sera pas approuvé par la plupart des navigateurs et des clients.

Dans ce guide, vous utiliserez Let's Encrypt pour obtenir un certificat SSL/TLS gratuit pour votre serveur web. Pour utiliser Let's Encrypt, vous devez installer un client logiciel sur votre serveur web qui peut communiquer avec l'autorité de certification et effectuer les tâches nécessaires.

L'un des clients les plus courants et recommandés pour Let's Encrypt est Certbot. Certbot est un outil en ligne de commande qui peut automatiquement demander, installer et renouveler des certificats pour votre serveur web. Il peut également configurer votre serveur web pour utiliser les certificats et activer HTTPS.

Pour installer Certbot sur votre serveur web, exécutez les commandes suivantes :

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
```

Après avoir installé Certbot, utilisez-le pour demander et installer un certificat pour votre serveur web. Vous devez fournir votre nom de domaine et votre adresse e-mail pour le certificat.

Pour demander et installer un certificat pour votre serveur web, exécutez la commande suivante :

```bash
sudo certbot --nginx -d votredomaine.com
```

Remplacez votredomaine.com par votre nom de domaine réel.

Suivez les invites et répondez aux questions. Certbot vérifiera automatiquement la propriété de votre domaine, obtiendra un certificat et l'installera sur votre serveur web. Il vous demandera également si vous souhaitez rediriger tout le trafic HTTP vers HTTPS. Choisissez l'option 2 pour activer la redirection.

Une fois le processus terminé, vous verrez un message comme celui-ci :

![message de succès de certbot](https://i.ibb.co/wBVfh1R/carbon-1.png align="left")

Vous avez maintenant configuré avec succès NGINX pour utiliser le chiffrement SSL/TLS avec un certificat de Let's Encrypt. Vous pouvez maintenant accéder à votre serveur web en utilisant HTTPS et voir l'icône de cadenas dans votre navigateur.

![Icône de cadenas](https://i.ibb.co/b3pqJBB/secureverification2.png align="left")

Vous pouvez également tester la sécurité de votre serveur web en utilisant des outils en ligne, tels que SSL Labs. Vous devriez voir une note de A ou supérieure.

Note : Les certificats Let's Encrypt sont valables pendant 90 jours. Certbot peut les renouveler automatiquement pour vous avant qu'ils n'expirent.

Pour activer le renouvellement automatique, vous devez créer une tâche CRON ou un minuteur systemd qui exécute la commande suivante au moins une fois par jour :

```bash
sudo certbot renew
```

Vous pouvez également tester le processus de renouvellement manuellement en exécutant la commande suivante :

```bash
sudo certbot renew --dry-run
```

Cela effectuera un essai sans apporter de modifications.

Si vous rencontrez des erreurs ou des problèmes, vous pouvez consulter la [documentation de Certbot](https://eff-certbot.readthedocs.io/en/latest/) ou le [forum communautaire de Let's Encrypt](https://community.letsencrypt.org/) pour obtenir de l'aide.

## Étape 2 : Configurer NGINX pour inclure les en-têtes de sécurité

Les en-têtes de sécurité aident à instruire le navigateur pour appliquer certaines politiques ou restrictions de sécurité lors de la gestion de votre contenu web. Ils peuvent prévenir ou atténuer les attaques web courantes, telles que le cross-site scripting (XSS), le clickjacking, l'injection de contenu, et plus encore.

Dans cette étape, vous ajouterez des en-têtes de sécurité à votre configuration NGINX. Ces en-têtes incluent X Frame Options, X Content Type Options, X XSS Protection, et Content Security Policy.

### X-Frame-Options

L'en-tête X-Frame-Options indique au navigateur s'il doit ou non autoriser votre page web à être affichée dans un frame, iframe, embed ou objet. Cela peut vous aider à prévenir les attaques de clickjacking, où un attaquant superpose un frame caché sur votre page web et trompe l'utilisateur en cliquant dessus.

Il existe trois valeurs possibles pour cet en-tête :

* DENY : Cette valeur empêche votre page web d'être affichée dans un frame.

* SAMEORIGIN : Cette valeur permet à votre page web d'être affichée dans un frame uniquement si le frame provient de la même origine que votre page web.

* ALLOW-FROM URI : Cette valeur permet à votre page web d'être affichée dans un frame uniquement si le frame provient de l'URI spécifié.

Pour activer l'en-tête X-Frame-Options dans NGINX, ajoutez la ligne suivante à votre bloc serveur dans votre fichier de configuration NGINX (/etc/nginx/sites-enabled/example.conf) :

```nginx
add_header X-Frame-Options "SAMEORIGIN";
```

Cela permettra à votre page web d'être affichée dans un frame uniquement si le frame provient de la même origine que votre page web. Vous pouvez changer la valeur en DENY ou ALLOW-FROM uri selon vos besoins.

Enregistrez le fichier et redémarrez NGINX pour appliquer les modifications.

### X-Content-Type-Options

L'en-tête X-Content-Type-Options indique au navigateur d'effectuer le sniffing de type MIME. Cette fonctionnalité tente de déterminer le type de contenu d'une ressource en analysant son contenu ou son extension de fichier.

En utilisant cet en-tête, vous pouvez vous protéger contre les attaques par injection de contenu. Ces attaques impliquent le téléchargement d'un fichier avec un type de contenu pour exploiter l'interprétation du navigateur.

Il n'y a qu'une seule valeur possible pour cet en-tête :

* nosniff : Cette valeur empêche le navigateur d'effectuer le sniffing de type MIME.

Pour activer l'en-tête X-Content-Type-Options dans NGINX, ajoutez la ligne suivante à votre bloc serveur dans votre fichier de configuration NGINX (/etc/nginx/sites-enabled/example.conf) :

```nginx
add_header X-Content-Type-Options "nosniff";
```

Cela empêchera le navigateur d'effectuer le sniffing de type MIME sur vos ressources web.

Enregistrez le fichier et redémarrez NGINX pour appliquer les modifications.

### X-XSS-Protection

L'en-tête X-XSS-Protection indique au navigateur d'activer ou de désactiver son filtre XSS intégré, qui peut détecter et bloquer certains types d'attaques XSS. Cela peut vous aider à prévenir les attaques XSS, où un attaquant injecte du code malveillant dans votre page web qui s'exécute dans le navigateur.

Il existe trois valeurs possibles pour cet en-tête :

* 0 : Cette valeur désactive le filtre XSS.

* 1 : Cette valeur active le filtre XSS et assainit la page si une attaque XSS est détectée.

* 1; mode=block : Cette valeur active le filtre XSS et bloque la page si une attaque XSS est détectée.

Pour activer l'en-tête X-XSS-Protection dans NGINX, ajoutez la ligne suivante à votre bloc serveur dans votre fichier de configuration NGINX (/etc/nginx/sites-enabled/example.conf) :

```nginx
add_header X-XSS-Protection "1; mode=block";
```

Cela activera le filtre XSS et bloquera la page si une attaque XSS est détectée. Vous pouvez changer la valeur en 0 ou 1 selon vos besoins.

Enregistrez le fichier et redémarrez NGINX pour appliquer les modifications.

### Content-Security-Policy

L'en-tête Content-Security-Policy indique au navigateur d'appliquer un ensemble de règles qui restreignent les sources et les types de contenu qui peuvent être chargés et exécutés sur votre page web. Cela peut vous aider à prévenir les attaques XSS, l'injection de contenu et d'autres types d'attaques qui reposent sur le chargement de contenu malveillant ou non approuvé.

La valeur de cet en-tête est une politique complexe qui se compose de plusieurs directives et valeurs. Chaque directive spécifie un type de contenu et une liste de sources qui sont autorisées ou interdites pour ce contenu.

Par exemple, la politique suivante permet uniquement les scripts et les styles de la même origine, et les images de la même origine ou de votredomaine.com :

```nginx
Content-Security-Policy: default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' votredomaine.com;
```

L'en-tête Content-Security-Policy est très puissant et flexible, mais aussi très compliqué et sujet aux erreurs. Vous devez concevoir et tester soigneusement votre politique pour vous assurer qu'elle ne casse pas la fonctionnalité de votre site web ou n'introduit pas de nouvelles vulnérabilités. Vous pouvez utiliser des outils comme CSP Evaluator ou CSP Scanner pour vérifier et améliorer votre politique.

Pour activer l'en-tête Content-Security-Policy dans NGINX, ajoutez la ligne suivante à votre bloc serveur dans votre fichier de configuration NGINX (/etc/nginx/sites-enabled/example.conf) :

```nginx
add_header Content-Security-Policy "default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' votredomaine.com;";
```

Cela appliquera la politique que vous avez décrite ci-dessus. Vous pouvez changer la politique selon vos besoins.

Enregistrez le fichier et redémarrez NGINX pour appliquer les modifications.

## Étape 3 : Créer un dépôt GitHub et pousser votre configuration NGINX

Pour créer un dépôt GitHub et pousser vos fichiers de configuration NGINX vers celui-ci, suivez ces étapes :

### Créer un dépôt GitHub

Tout d'abord, connectez-vous à votre compte GitHub et allez à la page d'accueil de GitHub.

Cliquez sur l'icône plus dans le coin supérieur droit de la page, et sélectionnez "New repository" dans le menu déroulant.

![Menu déroulant](https://i.ibb.co/vkWX0BJ/dropdownmenu-edited.png align="left")

Sur la page suivante, entrez un nom pour votre dépôt dans le champ "Repository name". Ce nom doit être court et descriptif, reflétant précisément le contenu du dépôt. Par exemple, vous pouvez le nommer "nginx-config".

Dans le champ "Description", vous pouvez entrer une description plus longue du dépôt si vous le souhaitez. Cela est facultatif, mais cela peut être utile pour fournir plus d'informations sur le but du dépôt.

Par exemple, vous pouvez écrire "Un dépôt pour stocker et gérer mes fichiers de configuration NGINX".

Vous pouvez définir la visibilité selon vos préférences. Si vous souhaitez que d'autres puissent voir votre travail, définissez-la sur "Public". Sinon, définissez-la sur "Private".

Laissez l'option "Initialize this repository with a README" décochée, car vous souhaitez créer un dépôt vide.

![Configuration du nouveau dépôt](https://i.ibb.co/SQVJbqh/settingupnewrepo.png align="left")

Cliquez sur le bouton "Create repository" pour créer le dépôt.

Votre nouveau dépôt vide sera créé et vous serez redirigé vers la page du dépôt.

### Pousser vos fichiers de configuration NGINX vers le dépôt GitHub

Sur votre serveur web, accédez au répertoire où se trouvent vos fichiers de configuration NGINX. Par défaut, il s'agit de /etc/nginx sur la plupart des distributions Linux.

Initialisez un nouveau dépôt Git dans ce répertoire en exécutant la commande suivante :

```bash
git init
```

Cela créera un nouveau répertoire .git dans le répertoire actuel, qui sera utilisé pour stocker toutes les informations de contrôle de version pour votre projet.

Ajoutez tous les fichiers de configuration que vous souhaitez inclure dans le dépôt en exécutant la commande suivante :

```bash
git add .
```

Cela ajoutera tous les fichiers dans le répertoire actuel et ses sous-répertoires au dépôt. Vous pouvez également spécifier des fichiers individuels à ajouter en remplaçant le (.) par les noms de fichiers, séparés par des espaces.

Ensuite, validez les fichiers dans le dépôt en exécutant la commande suivante :

```bash
git commit -m "Initial commit"
```

Cela créera le premier commit dans le dépôt, qui inclura tous les fichiers qui ont été ajoutés à l'étape précédente. Le drapeau -m est utilisé pour spécifier un message de commit, qui doit brièvement décrire les modifications apportées dans ce commit.

Retournez à votre page de dépôt GitHub et copiez l'URL de votre dépôt. Vous pouvez la trouver sous la section "Code". Elle devrait ressembler à ceci :

![url github](https://i.ibb.co/GThsRSV/code-Button.png align="left")

Sur votre serveur web, ajoutez l'URL de votre dépôt GitHub comme distant pour votre dépôt Git en exécutant la commande suivante :

```bash
git remote add origin https://github.com/username/nginx-config.git
```

Remplacez username par votre nom d'utilisateur GitHub et nginx-config par le nom de votre dépôt. L'origine est le nom du distant, que vous pouvez changer en ce que vous voulez.

Poussez votre dépôt Git local vers le dépôt GitHub en exécutant la commande suivante :

```bash
git push -u origin master
```

Cela poussera votre branche master, qui est la branche par défaut dans Git, vers le distant origin, qui est le dépôt GitHub que vous avez créé. Le drapeau -u est utilisé pour définir l'amont pour votre branche, ce qui signifie que vous pouvez utiliser git push ou git pull sans spécifier le distant ou la branche à l'avenir.

Entrez votre nom d'utilisateur et votre mot de passe GitHub lorsque vous y êtes invité. Si vous avez activé l'authentification à deux facteurs, vous devrez utiliser un jeton d'accès personnel au lieu de votre mot de passe. Vous pouvez en générer un à partir de votre page de paramètres GitHub.

Vous avez créé avec succès un dépôt GitHub et poussé vos fichiers de configuration NGINX vers celui-ci. Vous pouvez maintenant consulter et gérer vos fichiers de configuration sur GitHub.

## Étape 4 : Créer un projet CircleCI et le lier à votre dépôt GitHub

CircleCI est une plateforme qui offre des options basées sur le cloud et auto-hébergées pour l'intégration continue et la livraison continue. Elle vous permet de créer et d'exécuter des pipelines qui automatisent et rationalisent votre processus de déploiement et de mise à jour du serveur web.

Pour utiliser CircleCI, vous devez créer un projet CircleCI et le lier à votre dépôt GitHub. Cela permettra à CircleCI d'accéder à votre code et à vos fichiers de configuration, et de déclencher des builds chaque fois que vous poussez vers GitHub.

Pour créer un projet CircleCI et le lier à votre dépôt GitHub, suivez ces étapes :

### Inscription à CircleCI et connexion de votre compte GitHub

Commencez par vous connecter à votre compte CircleCI ou inscrivez-vous gratuitement [ici](https://circleci.com/login/).

Sur le tableau de bord CircleCI, cliquez sur le bouton "Create Project" dans le coin supérieur droit de la page.

![Bouton Créer un projet](https://i.ibb.co/wyPsNjk/project-button.png align="left")

Sur la page suivante, sélectionnez "GitHub" comme fournisseur de contrôle de version et cliquez sur le bouton "Connect with GitHub".

![Choix de Github](https://i.ibb.co/MhywfHF/choosing-github.png align="left")

Sur la page suivante, autorisez CircleCI à accéder à votre compte GitHub en cliquant sur le bouton "Authorize circleci".

Sur la page suivante, entrez un "Nom de projet" et suivez les instructions restantes pour créer avec succès un projet CircleCI.

![Entrez le nom du projet](https://i.ibb.co/MkYZBTF/Project-Name.png align="left")

### Créer un projet CircleCI et le lier à votre dépôt GitHub

Ensuite, créez une nouvelle paire de clés SSH dans votre terminal :

```bash
ssh-keygen -t ed25519 -f ~/.ssh/project_key -C email@example.com
```

Ensuite, copiez la clé privée générée :

```bash
pbcopy < ~/.ssh/project_key
```

Ensuite, entrez-la dans le champ de la clé privée :

![Entrez la clé SSH privée](https://i.ibb.co/0Qs2TNJ/Private-SSH-Key.png align="left")

Vous verrez une liste de vos dépôts GitHub. Trouvez le dépôt que vous avez créé à l'étape précédente et cliquez sur le bouton "Create Project" à côté.

Vous verrez maintenant une liste de modèles pour différents langages et frameworks. Comme vous utilisez Python et Flask, sélectionnez le modèle "Python" et cliquez sur le bouton "Use this config".

Sur la page suivante, vous verrez le fichier de configuration CircleCI généré (config.yml) qui définit votre pipeline. Vous pouvez examiner et modifier le fichier si vous le souhaitez, ou le laisser tel quel pour l'instant. Cliquez sur le bouton "Start building" pour créer le projet et le lier à votre dépôt GitHub.

Votre nouveau projet CircleCI sera créé et lié à votre dépôt GitHub.

Vous avez maintenant créé avec succès un projet CircleCI et l'avez lié à votre dépôt GitHub. Vous pouvez maintenant configurer et exécuter votre pipeline sur CircleCI.

## Étape 5 : Créer un fichier de configuration CircleCI et définir votre pipeline CI

Un fichier de configuration CircleCI est un fichier YAML qui définit votre pipeline CI. Un pipeline CI est une séquence de tâches qui s'exécutent chaque fois que vous poussez des modifications vers votre dépôt GitHub. Chaque tâche se compose d'étapes qui effectuent des tâches spécifiques, telles que l'exécution de commandes, l'installation de dépendances ou le déploiement de votre serveur web.

Dans cette étape, vous allez créer un fichier de configuration CircleCI et définir votre pipeline CI. Vous utiliserez le modèle Python que vous avez sélectionné à l'étape précédente comme point de départ, et vous le modifierez pour répondre à vos besoins. Vous expliquerez également ce que chaque étape du pipeline fait et comment elle aide à automatiser et à sécuriser le déploiement de votre serveur web.

### Créer un fichier de configuration CircleCI

Sur votre serveur web, accédez au répertoire où se trouvent vos fichiers de configuration NGINX. Par défaut, il s'agit de /etc/nginx sur la plupart des distributions Linux.

Créez un nouveau répertoire appelé .circleci dans ce répertoire en exécutant la commande suivante :

```bash
mkdir .circleci
```

C'est là que vous stockerez votre fichier de configuration CircleCI.

Ensuite, créez un nouveau fichier appelé config.yml dans le répertoire .circleci en exécutant la commande suivante :

```bash
touch .circleci/config.yml
```

C'est votre fichier de configuration CircleCI.

Ouvrez le fichier config.yml avec votre éditeur de texte préféré et collez le code suivant :

```yaml
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/python:3.9
    steps:
      - checkout
      - run:
          name: Install dependencies
          command: |
            pip install -r requirements.txt
      - run:
          name: Run tests
          command: |
            pytest
  deploy:
    machine:
      image: ubuntu-2004:202101-01
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints:
            - "YOUR_FINGERPRINT"
      - run:
          name: Deploy Nginx configuration
          command: |
            scp -r nginx root@YOUR_IP:/etc
            ssh root@YOUR_IP "systemctl restart nginx"

workflows:
  version: 2
  build-and-deploy:
    jobs:
      - build
      - deploy:
          requires:
            - build
          filters:
            branches:
              only: main
```

C'est votre fichier de configuration CircleCI qui définit votre pipeline CI. Vous expliquerez chaque partie du fichier dans la section suivante.

Enfin, enregistrez et fermez le fichier.

### Définir votre pipeline CI

Passons en revue chaque partie du fichier config.yml et voyons ce qu'il fait.

* Ligne 1 : Cela indique la version de la plateforme CircleCI que vous utilisez. 2.1 est la version la plus récente.

* Ligne 3 : Le niveau jobs contient une collection d'enfants, représentant vos tâches. Vous spécifiez les noms pour ces tâches, par exemple, build, test, deploy.

* Ligne 6 : Il s'agit de l'image Docker. L'exemple montre cimg/python:3.9, qui est une image fournie par CircleCI qui contient Python 3.9 et d'autres outils courants.

* Ligne 9 : La directive run exécute une commande shell ou un script. Vous pouvez spécifier un nom et une commande pour chaque directive run.

* Ligne 11 : L'attribut command est une liste de commandes shell que vous souhaitez exécuter. Dans ce cas, vous installez les dépendances pour votre application web en utilisant pip.

* Ligne 12 : Il s'agit d'une autre directive run qui exécute les tests pour votre application web en utilisant pytest.

* Ligne 13 : deploy est le deuxième enfant dans la collection jobs. Cette tâche est responsable du déploiement de votre configuration NGINX sur votre serveur web.

* Ligne 14 : Cela spécifie que vous utilisez un exécuteur de machine pour cette tâche. Un exécuteur de machine fournit une machine virtuelle complète avec un accès root et divers outils installés.

* Ligne 15 : Il s'agit de l'image de la machine. L'exemple montre ubuntu-2004:202101-01, qui est une image fournie par CircleCI qui contient Ubuntu 20.04 et d'autres outils courants.

* Ligne 16 : La collection steps est une liste de directives run et d'autres commandes que vous souhaitez exécuter dans cette tâche.

* Ligne 18 : La commande add\_ssh\_keys ajoute vos clés SSH à la machine. Vous devez fournir les empreintes des clés que vous souhaitez utiliser. Vous pouvez générer et ajouter des clés SSH à partir de votre page de paramètres CircleCI.

* Ligne 21 : L'attribut command est une liste de commandes shell que vous souhaitez exécuter. Dans ce cas, vous utilisez SCP pour copier vos fichiers de configuration NGINX de la machine vers votre serveur web, et SSH pour redémarrer le service NGINX sur votre serveur web. Vous devez remplacer YOUR\_FINGERPRINT par l'empreinte de votre clé SSH, et YOUR\_IP par l'adresse IP de votre serveur web.

* Ligne 24 : Cela indique la version de la syntaxe du workflow que vous utilisez. 2 est la version la plus récente.

* Ligne 29 : L'attribut required spécifie les dépendances de cette tâche. Dans ce cas, vous dites que la tâche deploy nécessite que la tâche build se termine avec succès avant de s'exécuter.

* Ligne 30 : L'attribut filters spécifie les conditions d'exécution de cette tâche. Dans ce cas, vous dites que la tâche deploy ne doit s'exécuter que sur la branche main de votre dépôt GitHub.

### Pousser votre fichier de configuration CircleCI vers votre dépôt GitHub

Sur votre serveur web, ajoutez, validez et poussez votre fichier de configuration CircleCI vers votre dépôt GitHub en exécutant les commandes suivantes :

```bash
git add .circleci/config.yml
git commit -m "Add CircleCI config file"
git push origin main
```

Cela déclenchera une nouvelle build sur CircleCI et exécutera votre pipeline CI.

Allez sur votre tableau de bord CircleCI et cliquez sur le workflow build-and-deploy.

Vous pouvez cliquer sur chaque tâche pour voir les détails et les logs des étapes.

Attendez que le workflow se termine.

Vous avez créé avec succès un fichier de configuration CircleCI et défini votre pipeline CI. Vous pouvez maintenant automatiser et sécuriser le déploiement de votre serveur web avec CircleCI. Vous pouvez également modifier et améliorer votre fichier de configuration selon vos besoins.

## Étape 6 : Tester et déployer votre serveur web avec CircleCI

Maintenant que vous avez créé un projet CircleCI et un fichier de configuration pour votre pipeline CI, vous pouvez tester et déployer votre serveur web avec CircleCI. Vous pouvez déclencher et surveiller votre pipeline CI à partir de l'application web CircleCI ou de la ligne de commande. Vous pouvez également vérifier que votre serveur web est déployé et sécurisé correctement en utilisant des outils en ligne ou en accédant à votre serveur web en utilisant HTTPS.

### Déclencher et surveiller votre pipeline CI à partir de l'application web CircleCI

Pour déclencher et surveiller votre pipeline CI à partir de l'application web CircleCI, suivez ces étapes :

* Allez sur le tableau de bord CircleCI.

* Sur le tableau de bord, vous verrez une liste de vos projets et pipelines. Trouvez le projet que vous avez créé à l'étape précédente et cliquez dessus.

* Sur la page du projet, vous verrez une liste de vos branches et workflows. Trouvez la branche vers laquelle vous avez poussé votre fichier de configuration CircleCI à l'étape précédente et cliquez sur le workflow build-and-deploy.

* Sur la page du workflow, vous verrez une représentation graphique de votre pipeline, montrant le statut et la durée de chaque tâche et étape. Vous pouvez cliquer sur chaque tâche ou étape pour voir les détails et les logs des commandes qui ont été exécutées.

* Attendez que le workflow se termine. Si tout se passe bien, vous verrez une coche verte à côté de chaque tâche et étape, indiquant qu'elles ont réussi.

Vous avez déclenché et surveillé avec succès votre pipeline CI à partir de l'application web CircleCI. Vous pouvez également déclencher et surveiller votre pipeline CI à partir de la ligne de commande.

### Déclencher et surveiller votre pipeline CI à partir de la ligne de commande

Pour déclencher et surveiller votre pipeline CI à partir de la ligne de commande, suivez ces étapes :

* Sur votre serveur web, accédez au répertoire où se trouvent vos fichiers de configuration NGINX. Par défaut, il s'agit de /etc/nginx sur la plupart des distributions Linux.

* Apportez quelques modifications à vos fichiers de configuration, telles que l'ajout ou la suppression d'en-têtes de sécurité, et enregistrez-les.

* Ajoutez, validez et poussez vos modifications vers votre dépôt GitHub en exécutant les commandes suivantes :

```bash
git add .
git commit -m "Update Nginx configuration"
git push origin main
```

Cela déclenchera une nouvelle build sur CircleCI et exécutera votre pipeline CI.

Pour surveiller votre pipeline CI à partir de la ligne de commande, vous pouvez utiliser l'interface de ligne de commande CircleCI, qui est un outil qui vous permet d'interagir avec CircleCI à partir de votre terminal. Vous pouvez installer l'interface de ligne de commande CircleCI en suivant les instructions sur le site officiel.

Après avoir installé l'interface de ligne de commande CircleCI, vous pouvez utiliser la commande `circleci` pour effectuer diverses actions, telles que lister vos projets, pipelines, workflows, tâches et artefacts. Vous pouvez également utiliser le drapeau --help pour voir les options et arguments disponibles pour chaque commande.

Pour surveiller votre pipeline CI à partir de la ligne de commande, vous pouvez utiliser la commande circleci pipeline pour lister et décrire vos pipelines.

Par exemple, vous pouvez exécuter la commande suivante pour lister les pipelines de votre projet :

```bash
circleci pipeline list --org-slug <VCS>/<your-vcs-org-or-username> --project-slug <VCS>/<your-repo-name>
```

Remplacez `<VCS>` par gh ou bb selon votre système de contrôle de version. Remplacez `<your-vcs-org-or-username>` par votre organisation ou nom d'utilisateur GitHub ou Bitbucket. Remplacez `<your-repo-name>` par le nom de votre dépôt. Vous verrez quelque chose comme ceci :

![Sortie de la commande](https://i.ibb.co/JKqc0cn/carbon-5.png align="left")

Vous pouvez utiliser l'ID ou le numéro de pipeline pour décrire un pipeline spécifique et voir ses détails, tels que le statut, les workflows, les tâches et les étapes. Par exemple, vous pouvez exécuter la commande suivante pour décrire le dernier pipeline de votre projet :

```bash
circleci pipeline describe --org-slug <VCS>/<your-vcs-org-or-username> --project-slug <VCS>/<your-repo-name> --pipeline-number <number>
```

Remplacez `<number>` par le numéro de pipeline que vous souhaitez décrire.

Attendez que le pipeline se termine. Si tout se passe bien, vous verrez un message de succès pour chaque tâche et étape, indiquant qu'elles ont réussi.

Vous avez déclenché et surveillé avec succès votre pipeline CI à partir de la ligne de commande. Vous pouvez également vérifier que votre serveur web est déployé et sécurisé correctement.

### Vérifier que votre serveur web est déployé et sécurisé correctement

Pour vérifier que votre serveur web est déployé et sécurisé correctement, vous pouvez utiliser des outils en ligne ou accéder à votre serveur web en utilisant HTTPS. Voici quelques exemples :

Pour vérifier que votre serveur web utilise la dernière configuration Nginx que vous avez poussée vers GitHub, vous pouvez utiliser un outil comme [curl](https://curl.se/) ou [wget](https://www.gnu.org/software/wget/) pour faire une requête à votre serveur web et inspecter les en-têtes de réponse.

Par exemple, vous pouvez exécuter la commande suivante pour voir les en-têtes de sécurité que votre serveur web envoie :

```bash
curl -I https://www.votredomaine.com
```

Remplacez votredomaine.com par votre nom de domaine réel.

Vous pouvez comparer les en-têtes avec ceux que vous avez configurés dans votre fichier de configuration NGINX et voir s'ils correspondent.

Pour vérifier que votre serveur web utilise le certificat SSL/TLS que vous avez installé avec Certbot, vous pouvez utiliser un outil comme [SSL Labs](https://www.ssllabs.com/ssltest/) ou [HTBridge](https://www.htbridge.com/ssl/) pour scanner votre serveur web et vérifier sa configuration SSL/TLS et sa note. Vous pouvez vérifier les détails de votre certificat, tels que l'émetteur, la validité et la chaîne. Vous pouvez également vérifier la note de votre configuration SSL/TLS, qui devrait être A ou supérieure.

Pour vérifier que votre serveur web est accessible et fonctionnel en utilisant HTTPS, vous pouvez simplement ouvrir votre navigateur web et visiter votre serveur web en utilisant HTTPS. Par exemple, vous pouvez aller sur https://www.votredomaine.com et voir votre page web.

Vous pouvez vérifier l'icône de cadenas dans votre navigateur, qui indique que votre connexion est sécurisée. Vous pouvez également cliquer sur l'icône et voir les détails de votre certificat et de votre connexion.

![Visualisation du certificat](https://i.ibb.co/dGwr57V/certificate-viewer.png align="left")

## Conclusion

Dans cet article, vous avez appris comment sécuriser votre serveur web en utilisant NGINX et CircleCI. NGINX et CircleCI, lorsqu'ils sont utilisés ensemble, peuvent fournir une solution puissante pour garantir la sécurité continue de vos applications web.

Restez à la pointe en intégrant ces technologies dans votre flux de travail, et donnez à votre équipe les moyens de fournir des services web sécurisés et fiables.

N'oubliez pas de partager ce guide avec vos collègues, amis et communautés en ligne si vous le trouvez instructif.