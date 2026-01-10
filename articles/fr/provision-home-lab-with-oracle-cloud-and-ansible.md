---
title: Comment approvisionner un laboratoire domestique avec Oracle Cloud et Ansible
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-11-15T21:52:50.000Z'
originalURL: https://freecodecamp.org/news/provision-home-lab-with-oracle-cloud-and-ansible
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-pixabay-210158.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: servers
  slug: servers
- name: software architecture
  slug: software-architecture
- name: SSL
  slug: ssl
seo_title: Comment approvisionner un laboratoire domestique avec Oracle Cloud et Ansible
seo_desc: Imagine for a moment that you been working hard to setup a website, protected
  with SSL, and then your hardware fails. This means that unless you have a perfect
  backup of your machine, you will need to install all the software and configuration
  files ...
---

Imaginez un instant que vous avez travaillé dur pour configurer un site web, protégé avec SSL, et que votre matériel tombe en panne. Cela signifie que, sauf si vous avez une sauvegarde parfaite de votre machine, vous devrez installer tous les logiciels et fichiers de configuration à la main.

Et si ce n'est pas un seul serveur mais plusieurs ? Le temps nécessaire pour les réparer tous augmentera de manière exponentielle – et comme il s'agit d'un processus manuel, il sera plus sujet aux erreurs.

Et puis le scénario cauchemardesque : vous n'avez pas de sauvegarde à jour, ou vous avez des sauvegardes incomplètes. Ou le pire – il n'y a pas de sauvegardes du tout. Ce dernier cas est plus courant que vous ne le pensez, surtout dans les laboratoires domestiques où vous bricolez et jouez avec des choses par vous-même.

Dans ce tutoriel, je vais vous montrer comment faire un approvisionnement complet de l'infrastructure d'une paire de serveurs web sur un fournisseur de cloud, avec des certificats SSL et des métriques de surveillance avec Prometheus.

## Ce dont vous avez besoin pour cette installation

La première chose dont vous avez besoin est un fournisseur de cloud. Oracle Cloud offre une version *Free Tier* de leurs services cloud, qui vous permet de configurer des machines virtuelles gratuitement. C'est idéal pour un laboratoire domestique avec de nombreuses fonctionnalités riches que vous pouvez utiliser pour essayer de nouveaux outils et techniques.

Vous aurez également besoin d'un outil d'automatisation. J'ai utilisé Ansible car il n'a pas beaucoup de exigences (vous avez seulement besoin d'un démon SSH et d'une authentification par clé publique pour commencer). J'aime aussi parce qu'il fonctionne également bien, quel que soit l'environnement cloud que vous essayez d'approvisionner.

Dans ce tutoriel, nous utiliserons la version Open Source de cet outil, car elle est plus que suffisante pour nos besoins.

### Ce qui est inclus dans le playbook Ansible

Un playbook Ansible n'est rien de plus qu'un ensemble d'instructions que vous définissez pour exécuter des *tâches* qui modifieront l'état d'un hôte. Ces actions sont effectuées sur un inventaire d'hôtes que vous définissez.

Ici, vous allez apprendre les éléments suivants :

* Comment nettoyer les sources d'inventaire en utilisant la disposition appropriée dans vos playbooks.

* Comment approvisionner deux instances NGINX, avec la demande de leurs certificats SSL gratuits appropriés en utilisant Certbot.

* Comment configurer les pare-feux Linux locaux et ajouter un agent Prometheus node_exporter et un scraper pour collecter ces données.

* Des concepts comme les variables, les rôles (avec inclusion de tâches), et l'exécution conditionnelle.

* Des techniques importantes comme l'étiquetage des tâches, les messages de débogage, et la validation statique avec ansible-lint.

Tout le code peut être trouvé dans ce dépôt GitHub.

## Ce que vous devriez savoir avant d'essayer cela

Parce que nous allons couvrir plusieurs tâches ici, vous devrez probablement être familiarisé avec plusieurs choses (je fournirai des liens au fur et à mesure) :

* Ce n'est pas un cours d'introduction à Ansible mais plutôt un "comment tout s'assemble" avec un playbook plus détaillé, mais pas trop complexe.

* Un compte OCI Cloud Free Tier

* Un compte privilégié, très probablement SUDO

* Des connaissances de base sur TCP/IP et les pare-feux avec firewalld

* Comment utiliser RPM et comment packager des applications (nous ne le ferons pas ici, mais cela aide à comprendre quand un RPM est meilleur qu'une tâche complexe dans Ansible)

### Ce qui n'est pas inclus ici

OCI Cloud dispose d'une API REST complète pour gérer de nombreux aspects de leur environnement cloud. Leur page de configuration (plus précisément le SDK) est également très détaillée.

## Vous ferez probablement les choses différemment en production.

### Installer le OCI-Metrics-datasource au lieu des agents Prometheus sur une machine virtuelle

Vous pouvez aller sur cette page pour l'installer sur votre instance Grafana (Bare metal ou Cloud). Vous devez également configurer vos identifiants et permissions comme expliqué ici.

C'est probablement le moyen le plus efficace de surveiller vos ressources car vous n'avez pas besoin d'exécuter des agents sur vos machines virtuelles. Mais j'installerai plutôt un agent Prometheus node_exporter et un scraper qui seront visibles depuis une instance Grafana Cloud.

### Un Prometheus exposé sur un endpoint Internet n'est pas une bonne idée

Il est très clair, j'expose mon scraper Prometheus à Internet pour que Grafana cloud puisse y accéder. Sur un Intranet avec un cloud privé et votre Grafana local, ce n'est pas un problème – mais ici, un agent Prometheus poussant des données vers Grafana serait une meilleure option.

Néanmoins, Grafana fournit une liste d'adresses IP publiques que vous pouvez utiliser pour configurer votre liste d'autorisation.

Donc ce qui suit fonctionnera :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/oracle_cloud_ingress_rules.png align="left")

*Règles d'entrée Oracle Cloud*

Mais ce n'est pas le meilleur. Au lieu de cela, vous voulez restreindre les adresses IP spécifiques qui peuvent extraire des données de vos services exposés. L'exportateur prometheus peut être complètement caché de Grafana sur le port 9100. Au lieu de cela, nous devons seulement exposer le scraper Prometheus qui écoute sur le port 9000.

Pour ce laboratoire domestique, ce n'est pas un gros problème d'avoir de tels services entièrement exposés. Mais si vous avez un serveur avec des données sensibles, vous devez restreindre qui peut atteindre le service !

Une alternative à l'endpoint Prometheus est de pousser les données vers Grafana en utilisant un agent Grafana mais je ne couvrirai pas cette option ici.

# Analyse du Playbook

Ansible vous permet d'avoir un seul fichier avec les instructions du playbook, mais finalement vous trouverez que cette structure est difficile à maintenir.

Pour mon playbook, j'ai décidé de garder la structure suggérée :

```shell
tree -A 
.
├── inventory
│   └── cloud.yaml
├── oracle.yaml
├── roles
│   └── oracle
│       ├── files
│       │   ├── logrotate_prometheus-node-exporter
│       │   ├── prometheus-node-exporter
│       │   └── requirements_certboot.txt
│       ├── handlers
│       │   └── main.yaml
│       ├── meta
│       ├── tasks
│       │   ├── controller.yaml
│       │   ├── main.yaml
│       │   ├── metrics.yaml
│       │   └── nginx.yaml
│       ├── templates
│       │   ├── prometheus-node-exporter.service
│       │   ├── prometheus.service
│       │   └── prometheus.yaml
│       └── vars
│           └── main.yaml
└── site.yaml
```

Voici une brève description de la manière dont le contenu est organisé :

1. Vous pouvez avoir plus d'un site. Vous contrôlez cela à l'intérieur du fichier site.yaml.

2. La liste des hôtes est à l'intérieur du répertoire inventory. Vous pouvez avoir plus d'un fichier d'inventaire ou des scripts pour générer la liste des hôtes, ou une combinaison des deux.

3. Les rôles/oracle regroupent les tâches. Nous n'avons qu'un seul rôle appelé 'oracle' car c'est le fournisseur de cloud sur lequel je me concentre ici.

4. Notre playbook utilise des métadonnées sous forme de variables, chacune étant définie dans le répertoire 'vars'. De cette façon, nous pouvons personnaliser le comportement du playbook à plusieurs endroits :

```yaml
---
# Variables communes pour mes environnements Oracle Cloud
controller_host: XXXX.com
ssl_maintainer_email: YYYYYY@ZZZZ.com
architecture: arm64
prometheus_version: 2.38.0
prometheus_port: 9090
prometheus_node_exporter_nodes: "['X-server1:{{ node_exporter_port }}', 'Y-server2:{{ node_exporter_port }}' ]"
node_exporter_version: 1.4.0
node_exporter_port: 9100
internal_network: QQ.0.0.0/24
```

Le répertoire files de roles/oracle contient des fichiers qui peuvent être copiés tels quels dans le répertoire distant. Le répertoire templates est similaire, mais les fichiers qui s'y trouvent peuvent être personnalisés pour chaque hôte en utilisant le langage de templating Jinja.

```yaml
# Un modèle pour le fichier de configuration du scraper prometheus
---
global:
    scrape_interval: 30s
    evaluation_interval: 30s
    scrape_timeout: 10s
    external_labels:
        monitor: 'oracle-cloud-metrics'

scrape_configs:
  - job_name: 'node-exporter'
    static_configs:
      - targets: {{ prometheus_node_exporter_nodes }}
    tls_config:
      insecure_skip_verify: true
```

Le répertoire 'tasks' est l'endroit où nous stockons nos tâches, c'est-à-dire les actions qui modifieront l'état du serveur. Notez qu'Ansible n'exécutera pas les tâches si ce n'est pas nécessaire. L'idée est que vous pouvez réexécuter un playbook autant de fois que nécessaire et l'état final sera le même.

```yaml
# Fragment du fichier de tâches nginx. Voyez comment nous notifions un handler pour redémarrer nginx après le renouvellement du certificat SSL.
---
- name: Copier le fichier des exigences
  ansible.builtin.copy:
    src: requirements_certboot.txt
    dest: /opt/requirements_certboot.txt
  tags: certbot_requirements

- name: Configurer Certbot
  pip:
    requirements: /opt/requirements_certboot.txt
    virtualenv: /opt/certbot/
    virtualenv_site_packages: true
    virtualenv_command: /usr/bin/python3 -m venv
  tags: certbot_env

- name: Obtenir le certificat SSL
  command:
    argv:
      - /opt/certbot/bin/certbot
      - --nginx
      - --agree-tos
      - -m {{ ssl_maintainer_email }}
      - -d {{ inventory_hostname }}
      - --non-interactive
  notify:
    - Redémarrer Nginx
  tags: certbot_install
```

Il y a un répertoire spécial appelé 'handlers'. Là, nous définissons les actions qui doivent se produire si une tâche change l'état de notre hôte.

Nous avons maintenant une image de la façon dont toutes les pièces fonctionnent ensemble, alors parlons de quelques détails spécifiques.

### Approvisionnement du pare-feu

Avec Ansible, vous pouvez remplacer une séquence de commandes comme celle-ci :

```python
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
```

Avec un module firewalld :

```yaml
---
- name: Activer HTTP au pare-feu Linux
  firewalld:
    zone: public
    service: http
    permanent: true
    state: enabled
    immediate: yes
  notify:
    - Recharger le pare-feu
  tags: firewalld_https

- name: Activer HTTPS au pare-feu Linux
  firewalld:
    zone: public
    service: https
    permanent: true
    state: enabled
    immediate: yes
  notify:
    - Recharger le pare-feu
  tags: firewalld_https
```

### Les tâches communes ont de belles remplacements

Au lieu d'exécuter SUDO avec une commande privilégiée :

```python
sudo dnf install -y nginx
sudo systemctl enable nginx.service --now
```

Vous pouvez avoir quelque chose comme ceci :

```yaml
# fichier oracle.yaml, qui indique quels rôles appeler, inclus depuis site.yaml
---
- hosts: oracle
  serial: 2
  remote_user: opc
  become: true
  become_user: root
  roles:
  - oracle
# Tâche NGINX (roles/oracle/tasks/nginx.yaml)
- name: Assurer que nginx est à la dernière version
  dnf:
    name: nginx >= 1.14.1
    state: present
    update_cache: true
  tags: install_nginx
# Et un handler qui redémarrera NGINX après sa modification (handlers/main.yaml)
---
- name: Redémarrer Nginx
  ansible.builtin.service:
    name: nginx
    state: restarted
- name: Recharger le pare-feu
  ansible.builtin.systemd:
    name: firewalld.service
    state: reloaded
```

## Comment exécuter les playbooks

Normalement, vous n'attendez pas d'avoir tout le playbook écrit, mais vous exécutez les morceaux dont vous avez besoin dans le bon ordre. À un moment donné, vous aurez votre playbook entier terminé et prêt à être exécuté.

### Assurez-vous que le playbook se comporte correctement avec --check avant de faire des changements

La toute première étape consiste à vérifier votre fichier de playbook pour les erreurs. Pour cela, vous pouvez utiliser yamllint :

```shell
yamllint roles/oracle/tasks/main.yaml
```

Mais faire cela pour chaque fichier yaml dans votre playbook peut être fastidieux et sujet aux erreurs. En alternative, vous pouvez exécuter le playbook en mode 'dry-run', pour voir ce qui va se passer sans réellement faire de changements :

[![asciicast](https://asciinema.org/a/537302.svg align="left")](https://asciinema.org/a/537302)

Une autre façon de tester progressivement un playbook complexe est d'exécuter une tâche spécifique en utilisant une balise ou un groupe de balises. De cette façon, vous pouvez faire une exécution contrôlée de votre playbook :

*Gardez à l'esprit que cela n'exécutera aucune dépendance que vous avez pu définir dans votre playbook, cependant* :

[![asciicast](https://asciinema.org/a/537303.svg align="left")](https://asciinema.org/a/537303)

### Utiliser Ansible-lint lorsque ansible-playbook --check n'est pas suffisant

Certaines erreurs sont plus subtiles et ne seront pas détectées avec ansible-playbook --check. Pour obtenir une vérification plus complète de vos playbooks avant que des problèmes mineurs ne deviennent un casse-tête, vous pouvez utiliser ansible-lint. Alors, installons-le :

```shell
python3 -m venv ~/virtualenv/ansiblelint && . ~/virtualenv/ansiblelint/bin/activate
pip install --upgrade pip
pip install --upgrade wheel
pip install ansible-lint
```

Maintenant, nous pouvons vérifier le playbook :

```shell
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ ansible-lint site.yaml 
WARNING  Overriding detected file kind 'yaml' with 'playbook' for given positional argument: site.yaml
WARNING  Listing 1 violation(s) that are fatal
syntax-check[specific]: couldn't resolve module/action 'firewalld'. This often indicates a misspelling, missing collection, or incorrect module path.
roles/oracle/tasks/nginx.yaml:2:3
```

Étrange, firewalld est disponible sur notre installation Ansible. Qu'est-ce qui a été installé par ansible-lint ?

```shell
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ ansible --version
ansible [core 2.14.0]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/josevnz/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/josevnz/virtualenv/ansiblelint/lib64/python3.9/site-packages/ansible
  ansible collection location = /home/josevnz/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/josevnz/virtualenv/ansiblelint/bin/ansible
  python version = 3.9.9 (main, Nov 19 2021, 00:00:00) [GCC 10.3.1 20210422 (Red Hat 10.3.1-1)] (/home/josevnz/virtualenv/ansiblelint/bin/python3)
  jinja version = 3.1.2
  libyaml = True
```

Ansible-lint a installé son propre ansible [core], et firewalld fait partie de la collection ansible.posix. Nous allons utiliser Ansible Galaxy pour l'installer :

```shell
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ which ansible-galaxy
~/virtualenv/ansiblelint/bin/ansible-galaxy
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ ansible-galaxy collection install ansible.posix
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/download/ansible-posix-1.4.0.tar.gz to /home/josevnz/.ansible/tmp/ansible-local-18099xpw_8usc/tmp8msc9uf5/ansible-posix-1.4.0-_f17f525
Installing 'ansible.posix:1.4.0' to '/home/josevnz/.ansible/collections/ansible_collections/ansible/posix'
ansible.posix:1.4.0 was installed successfully
```

En l'exécutant à nouveau :

```shell
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ ansible-lint site.yaml 
WARNING  Overriding detected file kind 'yaml' with 'playbook' for given positional argument: site.yaml
WARNING  Listing 50 violation(s) that are fatal
name[play]: All plays should be named. (warning)
oracle.yaml:2

fqcn[action-core]: Use FQCN for builtin module actions (service).
roles/oracle/handlers/main.yaml:2 Use `ansible.builtin.service` or `ansible.legacy.service` instead.

fqcn[action-core]: Use FQCN for builtin module actions (command).
roles/oracle/handlers/main.yaml:6 Use `ansible.builtin.command` or `ansible.legacy.command` instead.
```

Certains avertissements sont pédants ('Use FQCN for builtin module actions (command)') et d'autres nécessitent de l'attention (Les commandes ne devraient pas changer les choses si rien ne doit être fait.).

Ansible-lint a trouvé de nombreuses odeurs dans le playbook, il y a une option pour réécrire les fichiers et corriger certaines de ces erreurs automatiquement :

[![asciicast](https://asciinema.org/a/538053.svg align="left")](https://asciinema.org/a/538053)

Il y a quelques directives que vous pouvez suivre pour corriger ces problèmes. Voici quelques-unes qui peuvent être directement appliquées aux avertissements que nous avons reçus plus tôt :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/ansible_error_fixes.png align="left")

Notez que toutes les erreurs sont faciles à résoudre. Certaines commandes décident elles-mêmes si elles doivent apporter des modifications ou non, mais ont du mal à communiquer avec Ansible :

```yaml
- name: Obtenir le certificat SSL
  ansible.builtin.shell:
    argv:
      - /opt/certbot/bin/certbot
      - --nginx
      - --agree-tos
      - -m "{{ ssl_maintainer_email }}"
      - -d "{{ inventory_hostname }}"
      - --non-interactive
  notify:
    - Redémarrer Nginx
  tags: certbot_install
```

Dans notre cas, certboot imprime un message si le certificat n'est pas encore dû pour le renouvellement. Si cette sortie est manquante, alors nous déclenchons le redémarrage de Nginx (voir définir changé) :

```yaml
- name: Obtenir le certificat SSL
  ansible.builtin.shell:
    argv:
      - /opt/certbot/bin/certbot
      - --nginx
      - --agree-tos
      - -m {{ ssl_maintainer_email }}
      - -d {{ inventory_hostname }}
      - --non-interactive
  register: certbot_output # Enregistre la sortie de certbot.
  changed_when: 
    - '"Certificate not yet due for renewal" not in certbot_output.stdout'
  notify:
    - Redémarrer Nginx
  tags: certbot_install
```

Je veux utiliser shell, car j'ai besoin d'étendre la variable pour certbot, mais ansible-lint n'est toujours pas content :

```shell
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ ansible-lint site.yaml
WARNING  Overriding detected file kind 'yaml' with 'playbook' for given positional argument: site.yaml
WARNING  Listing 1 violation(s) that are fatal
command-instead-of-shell: Use shell only when shell functionality is required.
roles/oracle/tasks/nginx.yaml:47 Task/Handler: Get SSL certificate

You can skip specific rules or tags by adding them to your configuration file:
# .config/ansible-lint.yml
warn_list:  # or 'skip_list' to silence them completely
  - command-instead-of-shell  # Use shell only when shell functionality is required.

                   Rule Violation Summary                    
 count tag                      profile rule associated tags 
     1 command-instead-of-shell basic   command-shell, idiom 

Failed after min profile: 1 failure(s), 0 warning(s) on 8 files.
```

Il est temps de traiter cette erreur comme un avertissement, car je sais qu'ils ne sont pas des problèmes, en créant un .config/ansible-lint.yml :

```shell
(ansiblelint) [josevnz@dmaf5 OracleCloudHomeLab]$ ansible-lint site.yaml
WARNING  Overriding detected file kind 'yaml' with 'playbook' for given positional argument: site.yaml
WARNING  Listing 1 violation(s) that are fatal
command-instead-of-shell: Use shell only when shell functionality is required. (warning)
roles/oracle/tasks/nginx.yaml:47 Task/Handler: Get SSL certificate


                        Rule Violation Summary                         
 count tag                      profile rule associated tags           
     1 command-instead-of-shell basic   command-shell, idiom (warning) 

Passed with min profile: 0 failure(s), 1 warning(s) on 8 files.
```

Beaucoup mieux maintenant, l'avertissement n'est pas traité comme une erreur.

### Bonnes pratiques Jinja

Si vous prévoyez d'utiliser des variables et des modèles Jinja, assurez-vous de les mettre entre guillemets (exemple : "dest: /opt/prometheus-{{ prometheus_version }}.linux-{{ architecture }}.tar.gz")

### Limiter où le playbook s'exécute avec --limit et --tags

Disons que vous êtes seulement intéressé à exécuter votre playbook sur un certain hôte. Dans ce cas, vous pouvez également le faire en utilisant le drapeau --limit :

```shell
ansible-playbook --inventory inventory --limit fido.yourcompany.com --tags certbot_renew site.yaml
```

[![asciicast](https://asciinema.org/a/537304.svg align="left")](https://asciinema.org/a/537304)

Ici, nous avons exécuté uniquement une tâche étiquetée certbot_renew sur l'hôte fido.yourcompany.com.

### Comment gérer un vrai problème

Rendons cela intéressant : disons que j'étais impatient de mettre à jour l'une de mes exigences pour certboot, et que j'ai changé les versions de pip en '22.3.1' :

```text
pip==22.3.1
wheel==0.38.4
certbot==1.32.0
certbot-nginx==1.32.0
```

Lorsque j'exécute le playbook, nous avons une erreur :

[![asciicast](https://asciinema.org/a/537318.svg align="left")](https://asciinema.org/a/537318)

C'est un problème avec les versions spécifiées dans le fichier requirements_certboot.txt. Lorsque vous installez une bibliothèque Python en utilisant un environnement virtuel, vous pouvez spécifier des versions comme ceci :

pip==22.3.1 wheel==0.38.1 certbot==1.23.0 certbot-nginx==1.23.0

Pour corriger le problème, nous allons revenir aux versions utilisées dans le fichier et ensuite réexécuter le fichier des exigences et la tâche d'installation de Certbot :

```yaml
- name: Configurer Certbot
  pip:
    requirements: /opt/requirements_certboot.txt
    virtualenv: /opt/certbot/
    virtualenv_site_packages: true
    virtualenv_command: /usr/bin/python3 -m venv
    state: forcereinstall
  tags: certbot_env
```

```shell
ansible-playbook --inventory inventory --tags certbot_env site.yaml
```

Voir cela en action :

[![asciicast](https://asciinema.org/a/537320.svg align="left")](https://asciinema.org/a/537320)

### Comment exécuter le playbook entier

```shell
ansible-playbook --inventory inventory site.yaml
```

Il est temps d'exécuter le playbook entier :

[![asciicast](https://asciinema.org/a/537322.svg align="left")](https://asciinema.org/a/537322)

## Conclusion

Ce tutoriel ne fait qu'effleurer la surface de ce que vous pouvez faire avec Ansible. Voici donc quelques ressources supplémentaires que vous devriez explorer pour en apprendre davantage :

* Améliorer les inventaires : Comment créer des fichiers d'inventaire dynamiques dans Ansible, Comment écrire un script Python pour créer des inventaires dynamiques Ansible, Comment écrire un plugin Ansible pour créer des fichiers d'inventaire

* Parfois vos playbooks s'exécuteront lentement, et vous devrez peut-être évaluer la consommation de ressources avec les plugins de rappel Ansible.

* Et il y aura un moment où un débogage plus approfondi sera nécessaire.