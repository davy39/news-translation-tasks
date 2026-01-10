---
title: Comment approvisionner un Nexus Sonatype OSS sur un Orange PI 5 avec Ansible
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2023-05-05T21:34:24.000Z'
originalURL: https://freecodecamp.org/news/provision-nexus-sonatype-oss-on-an-orange-pi-5-with-ansible
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cropped_museum.jpeg
tags:
- name: hardware
  slug: hardware
- name: Linux
  slug: linux
- name: Raspberry Pi
  slug: raspberry-pi
seo_title: Comment approvisionner un Nexus Sonatype OSS sur un Orange PI 5 avec Ansible
seo_desc: 'Nexus 3 OSS is an Open Source artifact repository manager that can handle
  multiple formats like container images, Python PIP, Java jar, and many others.

  Why have an on-premise artifact manager? There are many reasons for it:


  Use your private infrast...'
---

Nexus 3 OSS est un [gestionnaire de dépôt d'artéfacts Open Source](https://github.com/sonatype/nexus-public) qui peut gérer plusieurs formats comme les images de conteneurs, Python PIP, Java jar, et bien d'autres.

Pourquoi avoir un gestionnaire d'artéfacts sur site ? Il y a plusieurs raisons pour cela :

* Utilisez votre infrastructure privée : Vous pouvez avoir du code propriétaire qui doit être protégé.
  
* Vitesse de téléchargement des artéfacts plus rapide : Si vous téléchargez constamment les mêmes artéfacts via Internet, vous pouvez les mettre en cache à un emplacement central, au bénéfice de vos multiples utilisateurs sur plusieurs serveurs en les mettant en cache.
  
* Contrôlez quels artéfacts arrivent dans votre chaîne de construction : Centralisez l'emplacement des artéfacts, assurez-vous qu'ils sont approuvés pour l'utilisation, et confirmez également qu'ils ne contiennent pas de code malveillant.
  
* Séparer qui peut avoir accès à vos artéfacts : Vous pouvez avoir des exigences plus strictes sur qui peut accéder à certains artéfacts au sein de votre propre organisation.
  

Dans cet article, je vais vous montrer comment télécharger, installer et configurer la version OSS de Nexus 3 en utilisant un playbook Ansible.

Nexus 3 fonctionnera sur un [ordinateur Orange PI 5 avec 8 Go de RAM](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html), mais cet approvisionnement peut être effectué sur n'importe quelle machine avec les [exigences minimales](https://help.sonatype.com/repomanager3/product-information/sonatype-nexus-repository-system-requirements). Une partie de la configuration consistera à définir un proxy pour [PyPI.org](https://pypi.org/), pour les machines listées dans mon fichier [inventory](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/inventories/home/hosts.yaml).

## Ce dont vous avez besoin pour exécuter le code de ce tutoriel

1. Une connexion Internet pour télécharger le [code source](https://github.com/josevnz/Nexus3OnOrangePI) pour le playbook Ansible, Nexus et les modules PIP
  
2. Deux machines Linux ou plus (j'ai utilisé [Debian](https://raspi.debian.net/), [Armbian](https://www.armbian.com/orangepi-5/) et [Fedora IOT](https://getfedora.org/iot/)), avec au moins 8 Go de RAM. Mon cluster est un mélange de Raspberry PI 4 et d'un OrangePI 5.
  
3. Le contrôleur Ansible fonctionnera sur la machine Fedora, mais n'importe quel serveur peut être le contrôleur. Les [instructions d'installation pour Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) sont faciles à suivre.
  

## Organisation du Playbook

J'ai divisé les tâches en groupes et le playbook résultant ressemble à ceci :

```shell
[josevnz@dmaf5 Nexus3OnOrangePI]$ tree -N ansible/
ansible/
├── inventories
│   └── home
│       └── hosts.yaml
├── roles
│   ├── clients
│   │   ├── tasks
│   │   │   └── main.yaml
│   │   └── templates
│   │       └── pip.conf.j2
│   └── nexus
│       ├── files
│       │   └── swagger.json
│       ├── tasks
│       │   ├── download.yaml
│       │   ├── install.yaml
│       │   ├── main.yaml
│       │   ├── post_install.yaml
│       │   ├── pre_install.yaml
│       │   ├── repositories.yaml
│       │   ├── third_party.yaml
│       │   └── user.yaml
│       └── templates
│           ├── logrotate.nexus3.j2
│           ├── nexus3.service.j2
│           ├── nexus.rc.j2
│           └── nexus.vmoptions.j2
├── site.yaml
├── vars
│   ├── clients.yaml
│   └── nexus.yaml
└── vault
    ├── nexus_password.enc
    └── README.md

13 directories, 21 files
```

Maintenant, un peu d'explications :

* Il y a deux rôles : 'nexus' et 'clients'. Le rôle nexus est utilisé pour configurer le logiciel de gestion des artéfacts, tandis que le rôle client configure les paramètres [pip](https://docs.python.org/3/installing/index.html) sur chaque machine.
  
* Vars contient des variables utilisées dans chaque rôle, séparées par fichiers pour rendre leur utilisation plus claire
  
* Nous avons des mots de passe, et nous les gérons en utilisant la fonctionnalité [Ansible vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html).
  
* Le fichier '[site.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/site.yaml)' orchestres l'exécution des rôles :
  

```yaml
- hosts: all
  tags: clients
  vars_files:
    - vars/clients.yaml
  roles:
    - clients
- hosts: nexus_server
  tags: nexus
  become_user: root
  become: true
  vars_files:
    - vars/nexus.yaml
  roles:
    - nexus
```

Passons maintenant à l'univers où le playbook sera exécuté.

## L'Inventaire des Hôtes

Dans mon cas, il est assez simple - j'ai deux groupes principaux : 'clients' et la machine où le serveur Nexus 3 lui-même fonctionnera :

```yaml
all:
  children:
    nexus_server:
      hosts:
        orangepi5.home:
    home_lab:
      hosts:
        dmaf5.home:
        raspberrypi.home:
        orangepi5.home:
```

La prochaine tâche importante est de télécharger et de configurer Nexus 3.

## Comment Installer Nexus 3

Le fichier [main.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/main.yaml) décrit l'ordre et le but de chaque tâche d'installation pour le rôle Nexus :

```yaml
# Tasks listed here are related to the remote Nexus 3 server
# Included tasks are called in order
---
  - include_tasks: third_party.yaml
  - include_tasks: pre_install.yaml
  - include_tasks: download.yaml
  - include_tasks: install.yaml
  - include_tasks: post_install.yaml
  - include_tasks: user.yaml
  - include_tasks: repositories.yaml
```

Voyons d'abord ce que j'aime appeler les "tâches principales" :

1. [third\_party.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/third_party.yaml) : Ici, nous installons OpenJDK8 (Nexus 3 est écrit en Java) et logrotate pour gérer les anciens logs.
  
2. [pre\_install.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/pre_install.yaml) : Beaucoup de choses se passent ici, comme la création des répertoires requis pour nexus, un utilisateur non privilégié dédié qui exécutera le processus.
  
3. [download.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/download.yaml) : Comme son nom l'indique, nous obtenons une version fraîche du logiciel Nexus 3 OSS et nous assurons qu'il a la bonne somme de contrôle. Nous ne voulons pas installer de logiciels malveillants depuis Internet.
  

Ensuite viennent les tâches qui tombent dans le groupe "installation personnalisée" :

1. [install.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/install.yaml) : Décompressez le logiciel, préparez l'unité systemd pour le démarrer automatiquement, configurez les paramètres JVM pour Nexus et déployez la configuration logrotate.
  
2. [post\_install.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/post_install.yaml) : Des choses passionnantes se passent ici - le logiciel est installé et nous l'exécutons pour la première fois. Nous changeons également le mot de passe par défaut [en utilisant l'API REST](https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api), afin de pouvoir passer à l'étape de personnalisation.
  
3. [user.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/user.yaml) : Ici, nous préparons l'accès de nos utilisateurs finaux aux services offerts par Nexus. Nous faisons cela en utilisant une combinaison de l'API REST et du code client Ansible :
  

```yaml
# https://help.sonatype.com/repomanager3/installation-and-upgrades/post-install-checklist
# https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api
---
- name: Enable anonymous user
  tags: anonymous
  ansible.builtin.uri:
    user: ""
    password: ""
    url: "/v1/security/anonymous"
    method: PUT
    body_format: raw
    status_code: [ 200, 202, 204 ]
    headers:
      Content-Type: application/json
    body: |-
      { "enabled" : true, "userId" : "anonymous", "realmName" : "NexusAuthorizingRealm" }
    force_basic_auth: true
    return_content: true
  any_errors_fatal: true
- name: Enable Docker security realm
  tags: docker_realm
  ansible.builtin.uri:
    user: ""
    password: ""
    url: "/v1/security/realms/active"
    method: PUT
    body_format: raw
    status_code: [ 200, 202, 204 ]
    headers:
      Content-Type: application/json
    body: |-
      [ "NexusAuthenticatingRealm", "NexusAuthorizingRealm", "DockerToken" ]
    force_basic_auth: true
    return_content: true
  any_errors_fatal: true
```

La logique est facile à suivre, en utilisant la méthode http 'PUT', vous pouvez dire qu'il s'agit d'une opération de modification (ce qui signifie que les rôles et utilisateurs existants existent déjà). La détection des erreurs est effectuée en obtenant les codes HTTP retournés par Nexus.

L'étape suivante consiste à préparer notre proxy local PyPi. Il s'agit d'une tâche en plusieurs étapes et sera décrite en détail ci-dessous.

## Comment Configurer le Proxy PyPI sur Nexus 3

Le dernier fichier du rôle Nexus 3 est '[repositories.yaml](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/nexus/tasks/repositories.yaml)'. Ici, nous passons par les étapes suivantes :

1. Vérifiez si le proxy a déjà été configuré (opération GET ou lecture seule)
  
2. S'il n'existe pas, créez-en un nouveau (méthode POST avec une charge utile JSON contenant les détails pour créer un tout nouveau dépôt)
  

Remarquez que ce playbook n'offre pas l'option de mise à jour des paramètres du dépôt. Il est possible de le faire avec l'API REST, mais je laisserai cela comme exercice au lecteur.

Les tâches pour préparer le proxy PyPi sont présentées ci-dessous :

```yaml
# Create proxy for repositories
# https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api
# PyPi: https://pip.pypa.io/en/stable/user_guide/
---
- name: Check if the PyPi proxy exists
  tags: pypi_proxy_exists
  ansible.builtin.uri:
    user: ""
    password: ""
    url: "/v1/repositories/pypi/proxy/python_proxy"
    method: GET
    body_format: raw
    status_code: [ 200, 202, 204, 404 ]
    headers:
      Content-Type: application/json
    force_basic_auth: true
    return_content: true
  any_errors_fatal: true
  register: python_local
- name: Create PyPI proxy
  tags: pypi_proxy_create
  ansible.builtin.uri:
    user: ""
    password: ""
    url: "/v1/repositories/pypi/proxy"
    method: POST
    body_format: raw
    status_code: [ 201 ]
    headers:
      Content-Type: application/json
    body: |-
      {
        "name": "python_proxy",
        "online": true,
        "storage": {
          "blobStoreName": "default",
          "strictContentTypeValidation": true
        },
        "proxy": {
          "remoteUrl": "https://pypi.org/",
          "contentMaxAge": -1,
          "metadataMaxAge": 1440
        },
        "negativeCache": {
          "enabled": true,
          "timeToLive": 1440
        },
        "httpClient": {
          "blocked": false,
          "autoBlock": true,
          "connection": {
            "retries": 0,
            "timeout": 60,
            "enableCircularRedirects": false,
            "enableCookies": true,
            "useTrustStore": false
          }
        }
      }
    force_basic_auth: true
    return_content: true
  any_errors_fatal: true
  when: python_local.status == 404
```

Nous y sommes presque. Maintenant, nous devons dire à nos clients PyPi qu'ils doivent utiliser notre Nexus local et non le site PyPi direct pour obtenir nos bibliothèques Python.

## Comment Configurer les Clients

Le rôle des clients est beaucoup plus simple et ne nécessite que le déploiement d'un [modèle pour pip.conf](https://tutorials.kodegeek.com/Nexus3OnOrangePI/ansible/roles/clients/templates/pip.conf.j2) avec suffisamment d'informations pour forcer la recherche dans notre nouveau dépôt :

```yaml
# Tasks here are meant to be used on our clients user
---
- name: Create installation directory for pip.conf
  tags: pip_basedir
  ansible.builtin.file:
    state: directory
    path: ""
    owner: ""
    group: ""
    mode: "u+rwx,go-rwx"
- name: Copy pip.conf file
  tags: pip_copy
  ansible.builtin.template:
    src: pip.conf.j2
    dest: "/pip.conf"
    owner: ""
    group: ""
    mode: u=rxw,g=r,o=r
```

Le fichier résultant est déployé sur '*~/.config/pip/pip.conf*' de chaque machine :

```yaml
# https://pip.pypa.io/en/stable/topics/configuration/
[global]
timeout = 60
[install]
index = http://orangepi5.home:8081/repository/python_proxy/pypi
index-url = http://orangepi5.home:8081/repository/python_proxy/simple/
trusted-host = orangepi5.home
```

Le fichier ci-dessus montre un exemple de l'apparence de la version finale du fichier une fois déployé sur mon cluster (le vôtre sera différent avec l'URL résolue).

Il est maintenant temps d'exécuter l'ensemble du playbook et de voir à quoi il ressemble.

## Comment Exécuter le Playbook

Pour exécuter le playbook, nous passons quelques arguments :

1. L'emplacement de notre inventaire d'hôtes
  
2. L'emplacement du fichier de mot de passe chiffré et un fichier principal contenant le mot de passe principal pour déverrouiller le contenu du fichier protégé
  
3. Et enfin l'emplacement de notre fichier principal de playbook
  

```shell
cd ansible
ansible-playbook --inventory  inventories --extra-vars @vault/nexus_password.enc --vault-password-file $HOME/vault/ansible_vault_pass site.yaml
```

[![asciicast](https://asciinema.org/a/579355.svg align="left")](https://asciinema.org/a/579355)

### Comment tester le nouveau proxy PyPI

Pour tester notre nouveau proxy, nous allons installer [Python Rich](https://github.com/Textualize/rich) en utilisant pip et un environnement virtuel.

```shell
josevnz@orangepi5:~$ python3 -m venv ~/virtualenv/rich
(rich) josevnz@orangepi5:~$ . ~/virtualenv/rich/bin/activate
(rich) josevnz@orangepi5:~$ pip install rich
Looking in indexes: http://orangepi5.home:8081/repository/python_proxy/simple/
Collecting rich
  Downloading http://orangepi5.home:8081/repository/python_proxy/packages/rich/13.3.4/rich-13.3.4-py3-none-any.whl (238 kB)
      238.7/238.7 KB 14.8 MB/s eta 0:00:00
Collecting pygments<3.0.0,>=2.13.0
  Downloading http://orangepi5.home:8081/repository/python_proxy/packages/pygments/2.15.0/Pygments-2.15.0-py3-none-any.whl (1.1 MB)
      1.1/1.1 MB 23.8 MB/s eta 0:00:00
Collecting markdown-it-py<3.0.0,>=2.2.0
  Downloading http://orangepi5.home:8081/repository/python_proxy/packages/markdown-it-py/2.2.0/markdown_it_py-2.2.0-py3-none-any.whl (84 kB)
      84.5/84.5 KB 6.9 MB/s eta 0:00:00
Collecting mdurl~=0.1
  Downloading http://orangepi5.home:8081/repository/python_proxy/packages/mdurl/0.1.2/mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-2.2.0 mdurl-0.1.2 pygments-2.15.0 rich-13.3.4
```

Et ensuite nous pouvons confirmer que le cache a effectivement été utilisé en voyant les nouveaux artéfacts dans le nouveau dépôt :

![New artifacts on the Python_proxy PyPI repository](https://tutorials.kodegeek.com/Nexus3OnOrangePI/sonatype_browse_python_proxy.png align="left")

*Voir les artéfacts PyPi*

Voyons une démonstration du client en action, installant autre chose :

[![asciicast](https://asciinema.org/a/579357.svg align="left")](https://asciinema.org/a/579357)

## Personnalisation Avancée en Utilisant l'API REST

Chaque installation de Nexus vous permet de télécharger un fichier JSON qui décrit l'API prise en charge par le serveur. Par exemple, sur mon serveur, vous pouvez obtenir une copie comme ceci depuis mon serveur orangepi5.home :

```shell
curl --fail --remote-name http://orangepi5.home:8081/service/rest/swagger.json
```

De plus, l'interface utilisateur vous permet d'essayer les autres points de terminaison de l'API REST pour personnaliser votre installation.

![API Swagger documentation on Nexus 3](https://tutorials.kodegeek.com/Nexus3OnOrangePI/api-swagger.png align="left")

*Test de l'API REST*

## Conclusion

Je recommande de passer un peu de temps et de lire le [livre Nexus 3](https://help.sonatype.com/repomanager3) pour vous familiariser avec les fonctionnalités que cet outil peut offrir.

La communauté a préparé des [installeurs Debian et RPM](https://github.com/sonatype-nexus-community/nexus-repository-installer), si vous avez besoin de ce type de configuration plutôt que d'utiliser Ansible.

Nexus 3 *a beaucoup* de paramètres configurables. Nous n'avons couvert que la surface ici. En préparant cet article, j'ai trouvé '[ThoTeam Nexus3-oss repository](https://github.com/ansible-ThoTeam/nexus3-oss)' avec un playbook très complet et à jour, mais il était bien plus complexe que tout ce dont j'avais besoin pour mon laboratoire à domicile.

[Archiva](https://archiva.apache.org/) est un autre gestionnaire d'artéfacts Open Source, il est plus limité en fonctionnalités mais aussi plus simple à configurer.

Il y a une [liste de contrôle post-installation](https://help.sonatype.com/repomanager3/installation-and-upgrades/post-install-checklist) avec certaines tâches que je n'ai pas eu besoin de compléter pour mon laboratoire à domicile. Veuillez la consulter pour vous assurer que votre configuration est complète.