---
title: Comment sécuriser les infrastructures serveur cloud en utilisant Falco, Prometheus,
  Grafana et Docker
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-05-10T14:58:47.000Z'
originalURL: https://freecodecamp.org/news/secure-server-infrastructure-clouds-using-falco-prometheus-grafana-and-docker
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-aleksandar-pasaric-325185--1-.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: containers
  slug: containers
- name: cybersecurity
  slug: cybersecurity
- name: Docker
  slug: docker
- name: information security
  slug: information-security
seo_title: Comment sécuriser les infrastructures serveur cloud en utilisant Falco,
  Prometheus, Grafana et Docker
seo_desc: 'I was recently looking for a way to keep tabs on our containers and applications
  at work. Specifically, I was interested in detecting anomalies in the configuration.
  After a little research, I stumbled on Falco.

  What I found was a very complete Open ...'
---

Je cherchais récemment un moyen de surveiller nos conteneurs et applications au travail. Plus précisément, je m'intéressais à la détection des anomalies dans la configuration. Après quelques recherches, je suis tombé sur [Falco](https://github.com/falcosecurity/falco).

Ce que j'ai découvert, c'est une plateforme Open Source très complète avec de nombreuses fonctionnalités et une excellente documentation. Je voulais donc partager mon expérience avec vous.

Que allons-nous couvrir dans cet article ?

* Comment installer l'agent [Falco](https://falco.org/) sur l'hôte que vous souhaitez surveiller pour les événements (anomalies/violations)
  
* Comment ajuster Falco pour réduire les faux positifs et obtenir les informations dont vous avez vraiment besoin
  
* Comment utiliser [Prometheus](https://prometheus.io/) pour collecter les événements Falco dans un emplacement central, avec l'aide des exporters et d'un scraper.
  
* Enfin, comment connecter le scraper avec [Grafana](https://grafana.com/) pour la visualisation et les alertes
  

## **De quoi avez-vous besoin pour ce tutoriel ?**

* Une machine ou des machines avec Linux installé. Une machine virtuelle devrait fonctionner.
  
* Vous aurez besoin de permissions superutilisateur pour pouvoir installer/configurer Docker, RPM et les processus systemd
  
* Nous utiliserons des conteneurs Docker, donc une connaissance de base de Docker est requise
  
* Une connaissance pratique de Python/Bash, car nous écrirons quelques scripts pour tester et améliorer notre configuration.
  

À la fin, vous serez en mesure de configurer chacun des composants suivants :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/falco_monitoring.png align="left")

Ne soyez pas intimidé – je fournirai des liens vers la documentation et une explication approfondie de chacune de ces tâches au fur et à mesure.

## Table des matières

1. [**Qu'est-ce que Falco ?**](#questcequefalco)
  
2. [**Comment installer Falco**](#commentinstallerfalco)
  
3. [**Configuration de base**](#configurationdebase)
  
4. [**Comment tester la configuration par défaut**](#commenttesterlaconfigurationpardéfaut)
  
5. [**Les valeurs par défaut ne sont pas toujours bonnes**](#lesvaleurspardéfautnefontpas toujoursbonnes)
  
6. [**Intégrations Falco**](#intégrationsfalco)
  
7. [**En savoir plus**](#ensavoirplus)
  

# **Qu'est-ce que Falco ?**

La meilleure façon de décrire cet outil est d'apprendre ce qu'il peut faire :

> Falco peut détecter et alerter sur tout comportement impliquant des appels système Linux.
> 
> Les alertes Falco peuvent être déclenchées par l'utilisation d'appels système spécifiques, leurs arguments, et par les propriétés du processus appelant. Par exemple, Falco peut facilement détecter des incidents incluant, mais sans s'y limiter :

* Un shell est en cours d'exécution à l'intérieur d'un conteneur ou d'un pod dans Kubernetes.
  
* Un conteneur est en cours d'exécution en mode privilégié, ou monte un chemin sensible, tel que /proc, à partir de l'hôte.
  
* Un processus serveur engendre un processus enfant d'un type inattendu.
  
* Lecture inattendue d'un fichier sensible, tel que /etc/shadow.
  
* Un fichier non-périphérique est écrit dans /dev.
  
* Un binaire système standard, tel que ls, établit une connexion réseau sortante.
  
* Un pod privilégié est démarré dans un cluster Kubernetes.
  

# **Comment installer Falco**

Je vais installer Falco en utilisant un RPM ([des instructions similaires existent](https://falco.org/docs/getting-started/installation/) pour apt-get, et même des conteneurs Docker). Dans mon cas, j'ai estimé que l'installation native était la meilleure, et le RPM l'a rendue très facile :

```python
[josevnz@macmini2 ~]$ sudo -i dnf install https://download.falco.org/packages/rpm/falco-0.31.1-x86_64.rpm
Last metadata expiration check: 2:53:53 ago on Sun 01 May 2022 04:13:09 PM EDT.
falco-0.31.1-x86_64.rpm                                                                                                                                                                                                       1.7 MB/s |  12 MB     00:07    
Dependencies resolved.
==============================================================================================================================================================================================================================================================
 Package                                                          Architecture                                      Version                                                                     Repository                                               Size
==============================================================================================================================================================================================================================================================
Installing:
 falco                                                            x86_64                                            0.31.1-1                                                                    @commandline                                             12 M
Installing dependencies:
 dkms                                                             noarch                                            2.8.1-4.20200214git5ca628c.fc30                                             updates                                                  78 k
 elfutils-libelf-devel                                            x86_64                                            0.179-2.fc30                                                                updates                                                  27 k
 kernel-devel                                                     x86_64                                            5.6.13-100.fc30                                                             updates                                                  14 M

Transaction Summary
==============================================================================================================================================================================================================================================================
Install  4 Packages

Total size: 26 M
Total download size: 14 M
Installed size: 92 M
Is this ok [y/N]: y
Downloading Packages:
(1/3): elfutils-libelf-devel-0.179-2.fc30.x86_64.rpm                                                                                                                                                                          253 kB/s |  27 kB     00:00    
(2/3): dkms-2.8.1-4.20200214git5ca628c.fc30.noarch.rpm                                                                                                                                                                        342 kB/s |  78 kB     00:00    
(3/3): kernel-devel-5.6.13-100.fc30.x86_64.rpm                                                                                                                                                                                1.9 MB/s |  14 MB     00:07    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                                                                                         1.8 MB/s |  14 MB     00:07     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                                                                                                                      1/1 
  Installing       : kernel-devel-5.6.13-100.fc30.x86_64                                                                                                                                                                                                  1/4 
  Running scriptlet: kernel-devel-5.6.13-100.fc30.x86_64                                                                                                                                                                                                  1/4 
  Installing       : elfutils-libelf-devel-0.179-2.fc30.x86_64                                                                                                                                                                                            2/4 
  Installing       : dkms-2.8.1-4.20200214git5ca628c.fc30.noarch                                                                                                                                                                                          3/4 
  Running scriptlet: dkms-2.8.1-4.20200214git5ca628c.fc30.noarch                                                                                                                                                                                          3/4 
  Running scriptlet: falco-0.31.1-1.x86_64                                                                                                                                                                                                                4/4 
  Installing       : falco-0.31.1-1.x86_64                                                                                                                                                                                                                4/4 
  Running scriptlet: falco-0.31.1-1.x86_64
```

# **Configuration de base**

Sauf si nous voulons faire un traitement de sortie très basique, nous voulons activer la sortie JSON :

```python
# Si vous souhaitez que les événements soient en JSON ou en texte
json_output: true
```

Il deviendra évident pourquoi très bientôt.

Ensuite, [démarrez](https://falco.org/docs/getting-started/running/) l'agent Falco :

```python
[josevnz@macmini2 falco]$ sudo systemctl start falco.service 
[josevnz@macmini2 falco]$ sudo systemctl status falco.service 
 25cf falco.service - Falco: Container Native Runtime Security
   Loaded: loaded (/usr/lib/systemd/system/falco.service; disabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-05-01 19:20:52 EDT; 1s ago
     Docs: https://falco.org/docs/
  Process: 26887 ExecStartPre=/sbin/modprobe falco (code=exited, status=0/SUCCESS)
 Main PID: 26888 (falco)
    Tasks: 1 (limit: 2310)
   Memory: 65.8M
   CGroup: /system.slice/falco.service
            2514 250026888 /usr/bin/falco --pidfile=/var/run/falco.pid

May 01 19:20:52 macmini2 systemd[1]: Starting Falco: Container Native Runtime Security...
May 01 19:20:52 macmini2 systemd[1]: Started Falco: Container Native Runtime Security.
May 01 19:20:52 macmini2 falco[26888]: Falco version 0.31.1 (driver version b7eb0dd65226a8dc254d228c8d950d07bf3521d2)
May 01 19:20:52 macmini2 falco[26888]: Falco initialized with configuration file /etc/falco/falco.yaml
May 01 19:20:52 macmini2 falco[26888]: Loading rules from file /etc/falco/falco_rules.yaml:
May 01 19:20:53 macmini2 falco[26888]: Loading rules from file /etc/falco/falco_rules.local.yaml:
May 01 19:20:54 macmini2 falco[26888]: Loading rules from file /etc/falco/k8s_audit_rules.yaml:
```

# **Comment tester la configuration par défaut**

Selon votre [configuration](https://falco.org/docs/configuration/), vous pouvez ou non obtenir des événements immédiatement après le démarrage de Falco :

```python
[josevnz@macmini2 falco]$ sudo journalctl --unit falco --follow
-- Logs begin at Tue 2021-05-25 00:15:22 EDT. --
May 01 19:20:52 macmini2 systemd[1]: Starting Falco: Container Native Runtime Security...
May 01 19:20:52 macmini2 systemd[1]: Started Falco: Container Native Runtime Security.
May 01 19:20:52 macmini2 falco[26888]: Falco version 0.31.1 (driver version b7eb0dd65226a8dc254d228c8d950d07bf3521d2)
May 01 19:20:52 macmini2 falco[26888]: Falco initialized with configuration file /etc/falco/falco.yaml
May 01 19:20:52 macmini2 falco[26888]: Loading rules from file /etc/falco/falco_rules.yaml:
May 01 19:20:53 macmini2 falco[26888]: Loading rules from file /etc/falco/falco_rules.local.yaml:
May 01 19:20:54 macmini2 falco[26888]: Loading rules from file /etc/falco/k8s_audit_rules.yaml:
May 01 19:20:55 macmini2 falco[26888]: Starting internal webserver, listening on port 8765
```

Ne vous inquiétez pas. Nous allons exécuter quelques commandes qui feront que Falco enregistrera des avertissements et des alertes. Il est temps de voir comment cela fonctionne !

## **Comment exécuter un conteneur privilégié**

L'utilisation de conteneurs privilégiés [est considérée comme une mauvaise pratique](https://materials.rangeforce.com/tutorial/2020/06/25/Escaping-Docker-Privileged-Containers/), alors voyons si cet événement est détecté par Falco :

```python
[josevnz@macmini2 ~]$ docker run --rm --interactive --tty --privileged --volume /etc/shadow:/mnt/shadow fedora:latest ls -l /mnt/shadow
----------. 1 root root 1198 Nov 21 20:51 /mnt/shadow
```

Et notre journal Falco ?

```python
May 01 19:29:32 macmini2 falco[26888]: {"output":"19:29:32.918828894: Informational Privileged container started (user=root user_loginuid=0 command=container:bfb9637a47a6 kind_lumiere (id=bfb9637a47a6) image=fedora:latest)","priority":"Informational","rule":"Launch Privileged Container","source":"syscall","tags":["cis","container","mitre_lateral_movement","mitre_privilege_escalation"],"time":"2022-05-01T23:29:32.918828894Z", "output_fields": {"container.id":"bfb9637a47a6","container.image.repository":"fedora","container.image.tag":"latest","container.name":"kind_lumiere","evt.time":1651447772918828894,"proc.cmdline":"container:bfb9637a47a6","user.loginuid":0,"user.name":"root"}}
```

Cela apparaît comme un événement informatif. Définitivement l'une de ces choses à surveiller. Demandez-vous si l'application dans le conteneur a besoin de privilèges élevés.

Vous avez probablement aussi remarqué que chaque message a des tags. Faites attention à ceux qui commencent par "mitre\_\*", ils sont liés à la [base de connaissances Mitre Attack](https://attack.mitre.org/) des attaques et des mitigations. Oui, vous passerez un certain temps à les lire.

## **Comment créer un fichier dans le répertoire /root**

Cet exemple montre comment abuser de l'utilisateur root combiné avec des volumes dans un conteneur...

```python
[josevnz@macmini2 ~]$ docker run --rm --interactive --tty --user root --volume /root:/mnt/ fedora:latest touch /mnt/test_file
[josevnz@macmini2 ~]$
```

Réaction de Falco :

```python
May 01 19:32:02 macmini2 falco[26888]: {"output":"19:32:02.434286167: Informational Container with sensitive mount started (user=root user_loginuid=0 command=container:ef061174c7ef distracted_lalande (id=ef061174c7ef) image=fedora:latest mounts=/root:/mnt::true:rprivate)","priority":"Informational","rule":"Launch Sensitive Mount Container","source":"syscall","tags":["cis","container","mitre_lateral_movement"],"time":"2022-05-01T23:32:02.434286167Z", "output_fields": {"container.id":"ef061174c7ef","container.image.repository":"fedora","container.image.tag":"latest","container.mounts":"/root:/mnt::true:rprivate","container.name":"distracted_lalande","evt.time":1651447922434286167,"proc.cmdline":"container:ef061174c7ef","user.loginuid":0,"user.name":"root"}}
```

Montage sensible détecté !

## **Augmentons les enjeux en créant un fichier dans /bin**

D'accord, disons que nous faisons ceci :

```python
[josevnz@macmini2 ~]$ sudo -i
[root@macmini2 ~]# touch /bin/should_not_be_here
```

Qu'en pense Falco ?

```python
May 01 19:36:41 macmini2 falco[26888]: {"output":"19:36:41.237634398: Error File below a known binary directory opened for writing (user=root user_loginuid=1000 command=touch /bin/should_not_be_here file=/bin/should_not_be_here parent=bash pcmdline=bash gparent=sudo container_id=host image=<NA>)","priority":"Error","rule":"Write below binary dir","source":"syscall","tags":["filesystem","mitre_persistence"],"time":"2022-05-01T23:36:41.237634398Z", "output_fields": {"container.id":"host","container.image.repository":null,"evt.time":1651448201237634398,"fd.name":"/bin/should_not_be_here","proc.aname[2]":"sudo","proc.cmdline":"touch /bin/should_not_be_here","proc.pcmdline":"bash","proc.pname":"bash","user.loginuid":1000,"user.name":"root"}}
```

Une erreur, un répertoire binaire ouvert en écriture. Bonne détection.

# **Les valeurs par défaut ne sont pas toujours bonnes**

Après que Falco ait fonctionné pendant un certain temps, il est bon de se faire une idée des types d'événements que nous voulons ignorer et de ceux que nous voulons investiguer.

La première étape est d'obtenir une liste de tous les événements, en utilisant notre format JSON sur la charge utile :

```python
sudo journalctl --unit falco --no-page --output=cat > /tmp/falco_json_lines.txt
```

Le 'output=cat' indique à journalctl de nous donner la charge utile du message sans les horodatages (ne vous inquiétez pas, le message JSON lui-même contient des horodatages).

```shell
Starting Falco: Container Native Runtime Security...
Started Falco: Container Native Runtime Security.
Falco version 0.31.1 (driver version b7eb0dd65226a8dc254d228c8d950d07bf3521d2)
Falco initialized with configuration file /etc/falco/falco.yaml
Loading rules from file /etc/falco/falco_rules.yaml:
Loading rules from file /etc/falco/falco_rules.local.yaml:
Loading rules from file /etc/falco/k8s_audit_rules.yaml:
Starting internal webserver, listening on port 8765
{"output":"19:29:32.918828894: Informational Privileged container started (user=root user_loginuid=0 command=container:bfb9637a47a6 kind_lumiere (id=bfb9637a47a6) image=fedora:latest)","priority":"Informational","rule":"Launch Privileged Container","source":"syscall","tags":["cis","container","mitre_lateral_movement","mitre_privilege_escalation"],"time":"2022-05-01T23:29:32.918828894Z", "output_fields": {"container.id":"bfb9637a47a6","container.image.repository":"fedora","container.image.tag":"latest","container.name":"kind_lumiere","evt.time":1651447772918828894,"proc.cmdline":"container:bfb9637a47a6","user.loginuid":0,"user.name":"root"}}
{"output":"19:32:02.434286167: Informational Container with sensitive mount started (user=root user_loginuid=0 command=container:ef061174c7ef distracted_lalande (id=ef061174c7ef) image=fedora:latest mounts=/root:/mnt::true:rprivate)","priority":"Informational","rule":"Launch Sensitive Mount Container","source":"syscall","tags":["cis","container","mitre_lateral_movement"],"time":"2022-05-01T23:32:02.434286167Z", "output_fields": {"container.id":"ef061174c7ef","container.image.repository":"fedora","container.image.tag":"latest","container.mounts":"/root:/mnt::true:rprivate","container.name":"distracted_lalande","evt.time":1651447922434286167,"proc.cmdline":"container:ef061174c7ef","user.loginuid":0,"user.name":"root"}}
```

Jusqu'à présent, cela semble intéressant, mais qu'en est-il de ceci ?

```python
{"output":"23:04:10.609949471: Warning Shell history had been deleted or renamed (user=josevnz user_loginuid=1000 type=openat command=bash fd.name=/home/josevnz/.bash_history-01112.tmp name=/home/josevnz/.bash_history-01112.tmp path=<NA> oldpath=<NA> host (id=host))","priority":"Warning","rule":"Delete or rename shell history","source":"syscall","tags":["mitre_defense_evasion","process"],"time":"2022-05-04T03:04:10.609949471Z", "output_fields": {"container.id":"host","container.name":"host","evt.arg.name":"/home/josevnz/.bash_history-01112.tmp","evt.arg.oldpath":null,"evt.arg.path":null,"evt.time":1651633450609949471,"evt.type":"openat","fd.name":"/home/josevnz/.bash_history-01112.tmp","proc.cmdline":"bash","user.loginuid":1000,"user.name":"josevnz"}}
{"output":"23:04:10.635602857: Warning Shell history had been deleted or renamed (user=josevnz user_loginuid=1000 type=openat command=bash fd.name=/home/josevnz/.bash_history-01627.tmp name=/home/josevnz/.bash_history-01627.tmp path=<NA> oldpath=<NA> host (id=host))","priority":"Warning","rule":"Delete or rename shell history","source":"syscall","tags":["mitre_defense_evasion","process"],"time":"2022-05-04T03:04:10.635602857Z", "output_fields": {"container.id":"host","container.name":"host","evt.arg.name":"/home/josevnz/.bash_history-01627.tmp","evt.arg.oldpath":null,"evt.arg.path":null,"evt.time":1651633450635602857,"evt.type":"openat","fd.name":"/home/josevnz/.bash_history-01627.tmp","proc.cmdline":"bash","user.loginuid":1000,"user.name":"josevnz"}}
{"output":"23:04:10.635851215: Warning Shell history had been deleted or renamed (user=josevnz user_loginuid=1000 type=rename command=bash fd.name=<NA> name=<NA> path=<NA> oldpath=/home/josevnz/.bash_history-01627.tmp host (id=host))","priority":"Warning","rule":"Delete or rename shell history","source":"syscall","tags":["mitre_defense_evasion","process"],"time":"2022-05-04T03:04:10.635851215Z", "output_fields": {"container.id":"host","container.name":"host","evt.arg.name":null,"evt.arg.oldpath":"/home/josevnz/.bash_history-01627.tmp","evt.arg.path":null,"evt.time":1651633450635851215,"evt.type":"rename","fd.name":null,"proc.cmdline":"bash","user.loginuid":1000,"user.name":"josevnz"}}
{"output":"23:04:10.661829867: Warning Shell history had been deleted or renamed (user=josevnz user_loginuid=1000 type=rename command=bash fd.name=<NA> name=<NA> path=<NA> oldpath=/home/josevnz/.bash_history-01112.tmp host (id=host))","priority":"Warning","rule":"Delete or rename shell history","source":"syscall","tags":["mitre_defense_evasion","process"],"time":"2022-05-04T03:04:10.661829867Z", "output_fields": {"container.id":"host","container.name":"host","evt.arg.name":null,"evt.arg.oldpath":"/home/josevnz/.bash_history-01112.tmp","evt.arg.path":null,"evt.time":1651633450661829867,"evt.type":"rename","fd.name":null,"proc.cmdline":"bash","user.loginuid":1000,"user.name":"josevnz"}}
```

Ceci est une opération normale/légitime. Trouvons un moyen de renforcer cette règle ou de la supprimer complètement.

Tout d'abord, ouvrez le fichier `/etc/falco/falco_rules.yaml` et cherchez la règle 'Delete or rename shell history' (sortie JSON que nous avons vue précédemment) :

```yaml
- list: docker_binaries
  items: [docker, dockerd, exe, docker-compose, docker-entrypoi, docker-runc-cur, docker-current, dockerd-current]

 macro: var_lib_docker_filepath
  condition: (evt.arg.name startswith /var/lib/docker or fd.name startswith /var/lib/docker)

- rule: Delete or rename shell history
  desc: Detect shell history deletion
  condition: >
    (modify_shell_history or truncate_shell_history) and
       not var_lib_docker_filepath and
       not proc.name in (docker_binaries)
  output: >
    Shell history had been deleted or renamed (user=%user.name user_loginuid=%user.loginuid type=%evt.type command=%proc.cmdline fd.name=%fd.name name=%evt.arg.name path=%evt.arg.path oldpath=%evt.arg.oldpath %container.info)
  priority:
    WARNING
  tags: [process, mitre_defense_evasion]
```

Les règles Falco sont expliquées [en détail](https://falco.org/docs/rules/) dans la documentation officielle. En regardant simplement ce morceau, vous remarquerez quelques choses.

À propos des conditions :

1. Prise en charge de la logique complexe,
   
2. macros comme `var_lib_docker_filepath`
   
3. listes comme `(docker_binaries)`
   
4. et variables spéciales avec des champs comme `proc.name`.
   

Il est recommandé de ne pas modifier ce fichier. Au lieu de cela, vous devriez remplacer ce dont vous avez besoin dans le fichier `/etc/falco/falco_rules.local.yaml` :

```yaml
# Add new rules, like this one
# - rule: The program "sudo" is run in a container
#   desc: An event will trigger every time you run sudo in a container
#   condition: evt.type = execve and evt.dir=< and container.id != host and proc.name = sudo
#   output: "Sudo run in container (user=%user.name %container.info parent=%proc.pname cmdline=%proc.cmdline)"
#   priority: ERROR
#   tags: [users, container]

# Or override/append to any rule, macro, or list from the Default Rules
```

Pour l'exemple, disons que nous nous soucions lorsque l'historique du super-utilisateur (root) est écrasé, mais que tout le monde est autorisé. La meilleure partie est que vous n'avez pas à remplacer toute la règle.

Ainsi, la règle originale obtiendra une condition ajoutée :

```yaml
- rule: Delete or rename shell history
  append: true
  condition: and user.name=root
```

Il est toujours bon de valider que vos règles sont correctement écrites. Pour cela, vous pouvez demander à Falco de vérifier les règles originales et vos remplacements ensemble :

```shell
[root@macmini2 ~]# falco --validate /etc/falco/falco_rules.yaml --validate /etc/falco/falco_rules.local.yaml 
Fri May  6 20:48:00 2022: Validating rules file(s):
Fri May  6 20:48:00 2022:    /etc/falco/falco_rules.yaml
Fri May  6 20:48:00 2022:    /etc/falco/falco_rules.local.yaml
/etc/falco/falco_rules.yaml: Ok
/etc/falco/falco_rules.local.yaml: Ok
Fri May  6 20:48:01 2022: Ok

# Si les règles sont OK, redémarrez Falco
[root@macmini2 ~]# systemctl restart falco.service
```

## **Comment créer un explorateur d'événements simple en Python**

Vous serez probablement d'accord pour dire que se faire une idée des règles qui sont du bruit et de celles qui sont utiles est fastidieux.

Nous devons normaliser ces données, et nous allons utiliser un script Python qui va :

* Supprimer les données non-JSON
  
* Agrégat des types d'événements sans les horodatages
  
* Générer quelques statistiques d'agrégation, afin que nous puissions nous concentrer sur les événements les plus fréquents dans notre système
  

Un petit script Python peut faire l'affaire. Je laisse de côté la partie rendu de l'UI (veuillez consulter le code pour voir le tableau complet), et je vais plutôt vous montrer les parties d'analyse de fichier :

```python
#!/usr/bin/env python3
"""
Aggregate Falco events to make it easier to override rules
Jose Vicente Nunez (kodegeek.com@protonmail.com)
"""
import json
import re
from argparse import ArgumentParser
from pathlib import Path
from rich.console import Console
from falcotutor.ui import EventDisplayApp, create_event_table, add_rows_to_create_event_table


def filter_events(journalctl_out: Path) -> dict[any, any]:
    """
    :param journalctl_out:
    :return:
    """
    with open(journalctl_out, 'r') as journalctl_file:
        for row in journalctl_file:
            if re.search("^{", row):
                data = json.loads(row)
                if 'rule' in data and 'output_fields' in data:
                    yield data


def aggregate_events(local_event: dict[any, any], aggregated_events: dict[any, any]):
    rule = local_event['rule']
    if rule not in aggregated_events:
        aggregated_events[rule] = {
            'count': 0,
            'priority': local_event['priority'],
            'last_timestamp': "",
            'last_fields': ""
        }
    aggregated_events[rule]['count'] += 1
    aggregated_events[rule]['last_timestamp'] = local_event['time']
    del local_event['output_fields']['evt.time']
    aggregated_events[rule]['last_fields'] = json.dumps(local_event['output_fields'], indent=True)


if __name__ == "__main__":
    CONSOLE = Console()
    AGGREGATED = {}
    PARSER = ArgumentParser(description=__doc__)
    PARSER.add_argument(
        "falco_event",
        action="store"
    )
    ARGS = PARSER.parse_args()
    try:
        event_table = create_event_table()
        for event in filter_events(ARGS.falco_event):
            aggregate_events(local_event=event, aggregated_events=AGGREGATED)
        add_rows_to_create_event_table(AGGREGATED, event_table)
        EventDisplayApp.run(
            event_file=ARGS.falco_event,
            title="Falco aggregated events report",
            event_table=event_table
        )
    except KeyboardInterrupt:
        CONSOLE.print("[bold]Program interrupted...[/bold]")
```

Une fois le fichier chargé en tant que dictionnaire, nous devons simplement itérer pour agrégat les événements, puis afficher les résultats sous forme de tableau trié par compte :

[![asciicast](https://asciinema.org/a/492898.svg align="left")](https://asciinema.org/a/492898)

## **Comment afficher les règles Falco**

Si vous êtes comme moi, vous regardez toujours le fichier /etc/falco/falco\_rules.yaml pour comprendre ce qui est surveillé. Une vue brève de ces règles (sans regarder le fichier YAML verbeux avec des commentaires) est un bel ajout :

```python
#!/usr/bin/env python3
"""
Show brief content of default Falco rule YAML files
Jose Vicente Nunez (kodegeek.com@protonmail.com)
"""
from argparse import ArgumentParser
from pathlib import Path
from rich.console import Console
import yaml
from falcotutor.ui import create_rules_table, add_rows_to_create_rules_table, RulesDisplayApp


def load_rulez(falco_rulez: Path) -> dict[any, any]:
    rulez = {}
    with open(falco_rulez, 'rt') as falco_file:
        for rule_data in yaml.full_load(falco_file):
            if 'rule' in rule_data:
                rule_name = rule_data['rule']
                del rule_data['rule']
                rulez[rule_name] = rule_data
    return rulez


if __name__ == "__main__":
    CONSOLE = Console()
    AGGREGATED = {}
    PARSER = ArgumentParser(description=__doc__)
    PARSER.add_argument(
        "falco_rules",
        action="store"
    )
    ARGS = PARSER.parse_args()
    try:
        RULES = load_rulez(ARGS.falco_rules)
        RULE_TBL = create_rules_table()
        add_rows_to_create_rules_table(lrules=RULES, rules_tbl=RULE_TBL)
        RulesDisplayApp.run(
            rules_file=ARGS.falco_rules,
            title="Falco brief rule display",
            rules_table=RULE_TBL
        )
    except KeyboardInterrupt:
        CONSOLE.print("[bold]Program interrupted...[/bold]")
```

Vous pourriez améliorer ce script en ajoutant un filtrage des règles selon certains critères, par exemple (nom de la règle, priorité, activé/désactivé). Cette version ne fait aucun filtrage :

[![asciicast](https://asciinema.org/a/492908.svg align="left")](https://asciinema.org/a/492908)

# **Intégrations Falco**

Vous avez probablement remarqué deux choses de notre expérimentation précédente :

1. La charge utile des événements ne contient pas l'hôte. Si vous souhaitez localiser un serveur défaillant, vous devez améliorer la manière dont un événement multi-hôte est signalé (l'analyse d'un fichier journalctl provenant de nombreux hôtes n'est pas pratique).
   
2. Nous voulons recevoir des alertes dans un emplacement centralisé. Il serait bien d'avoir un moyen de "pousser" ces événements au lieu d'aller les chercher.
   

Il est temps de consolider ces alertes en un seul endroit.

## **Comment utiliser Falco Exporter**

L'[exporter Falco](https://github.com/falcosecurity/falco-exporter) nous permettra de partager les alertes Falco avec le scraper Prometheus. Nous devons d'abord activer [gRPC](https://grpc.io/) dans le fichier /etc/falco/falco.yaml

```python
# Serveur gRPC utilisant une socket unix
grpc:
  enabled: true
  bind_address: "unix:///var/run/falco.sock"
  # lorsque threadiness est 0, Falco le devine automatiquement en fonction du nombre de cœurs en ligne
  threadiness: 0

# Service de sortie gRPC.
# Par défaut, il est désactivé.
# En activant cela, tous les événements de sortie seront conservés en mémoire jusqu'à ce que vous les lisiez avec un client gRPC.
# Assurez-vous d'avoir un consommateur pour eux ou laissez cela désactivé.
grpc_output:
  enabled: true
```

Redémarrez Falco :

```python
[root@macmini2 ~]# systemctl restart falco.service 
[root@macmini2 ~]# systemctl status falco.service 
 25cf falco.service - Falco: Container Native Runtime Security
   Loaded: loaded (/usr/lib/systemd/system/falco.service; disabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-05-01 20:35:01 EDT; 26s ago
     Docs: https://falco.org/docs/
  Process: 28285 ExecStartPre=/sbin/modprobe falco (code=exited, status=0/SUCCESS)
 Main PID: 28288 (falco)
    Tasks: 11 (limit: 2310)
   Memory: 80.9M
   CGroup: /system.slice/falco.service
            2514 250028288 /usr/bin/falco --pidfile=/var/run/falco.pid

May 01 20:35:01 macmini2 systemd[1]: Starting Falco: Container Native Runtime Security...
May 01 20:35:01 macmini2 systemd[1]: Started Falco: Container Native Runtime Security.
May 01 20:35:01 macmini2 falco[28288]: Falco version 0.31.1 (driver version b7eb0dd65226a8dc254d228c8d950d07bf3521d2)
May 01 20:35:01 macmini2 falco[28288]: Falco initialized with configuration file /etc/falco/falco.yaml
May 01 20:35:01 macmini2 falco[28288]: Loading rules from file /etc/falco/falco_rules.yaml:
May 01 20:35:02 macmini2 falco[28288]: Loading rules from file /etc/falco/falco_rules.local.yaml:
May 01 20:35:03 macmini2 falco[28288]: Loading rules from file /etc/falco/k8s_audit_rules.yaml:
May 01 20:35:04 macmini2 falco[28288]: Starting internal webserver, listening on port 8765
May 01 20:35:04 macmini2 falco[28288]: gRPC server threadiness equals to 2
May 01 20:35:04 macmini2 falco[28288]: Starting gRPC server at unix:///var/run/falco.sock
```

Vérifiez rapidement que tout est OK (rappel, l'agent Falco est en cours d'exécution sur macmini2) :

```shell
josevnz@raspberrypi:~$ curl --fail http://macmini2:8765/healthz
{"status": "ok"}josevnz@raspberrypi:~$
```

Ensuite, nous exécutons le falco-exporter. Pour faciliter les choses, nous utiliserons un conteneur Docker [avec quelques remplacements dans la ligne de commande](https://docs.docker.com/engine/reference/commandline/run/).

```python
[root@macmini2 ~]# docker run --restart always --name falco-exporter --detach --volume /var/run/falco.sock:/var/run/falco.sock --network=host falcosecurity/falco-exporter --listen-address 192.168.1.16:9376
7d157af0251ea4bc73b8c355a74eaf4dd24a5348cbe3f5f2ea9d7147c6c366c8
[root@macmini2 ~]# docker logs falco-exporter
2022/05/02 00:56:30 connecting to gRPC server at unix:///var/run/falco.sock (timeout 2m0s)
2022/05/02 00:56:30 listening on http://192.168.1.16:9376/metrics
2022/05/02 00:56:30 connected to gRPC server, subscribing events stream
2022/05/02 00:56:30 ready

# Vérifiez avec CURL si l'URL est accessible
[root@macmini2 ~]# curl http://192.168.1.16:9376/metrics
# HELP go_gc_duration_seconds A summary of the pause duration of garbage collection cycles.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 0
go_gc_duration_seconds{quantile="0.25"} 0
go_gc_duration_seconds{quantile="0.5"} 0
go_gc_duration_seconds{quantile="0.75"} 0
go_gc_duration_seconds{quantile="1"} 0
go_gc_duration_seconds_sum 0
go_gc_duration_seconds_count 0
# HELP go_goroutines Number of goroutines that currently exist.
# TYPE go_goroutines gauge
go_goroutines 18
# HELP go_info Information about the Go environment.
# TYPE go_info gauge
go_info{version="go1.14.15"} 1
# HELP go_memstats_alloc_bytes Number of bytes allocated and still in use.
# TYPE go_memstats_alloc_bytes gauge
go_memstats_alloc_bytes 2.011112e+06
```

Pour être complet, laissez-moi vous montrer également comment capturer les métriques de performance de l'hôte [en utilisant l'exporter de nœud](https://prometheus.io/docs/guides/node-exporter/) (nous l'utiliserons plus tard pour surveiller combien de ressources sont utilisées par Falco et pour nous assurer que notre installation ne nuit pas au serveur) :

```python
docker run --detach --net="host" --pid="host" --volume "/:/host:ro,rslave" quay.io/prometheus/node-exporter:latest --path.rootfs=/host
```

L'exporter de nœud et l'exporter falco s'exécuteront sur chaque hôte dont les données doivent être scrapées. Maintenant, vous devez attendre pour collecter toutes ces métriques dans un seul emplacement. Pour cela, nous utiliserons l'agent [Prometheus](https://prometheus.io/docs/prometheus/latest/getting_started/) :

```python
---
# /etc/prometheus.yaml sur raspberrypi
global:
    scrape_interval: 30s
    evaluation_interval: 30s
    scrape_timeout: 10s
    external_labels:
        monitor: 'nunez-family-monitor'

scrape_configs:
  - job_name: 'falco-exporter'
    static_configs:
      - targets: ['macmini2.home:9376']
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['macmini2.home:9100', 'raspberrypi.home:9100', 'dmaf5:9100']
  - job_name: 'docker-exporter'
    static_configs:
      - targets: ['macmini2.home:9323', 'raspberrypi.home:9323', 'dmaf5:9323']

    tls_config:
      insecure_skip_verify: true
```

Ensuite, assurez-vous que le scraper Prometheus peut communiquer avec chacun des nœuds. Nous visitons l'interface web :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/prometheus-raspberrypi.png align="left")

Bien, Prometheus est capable de scraper Falco. Nous pouvons même exécuter une simple requête pour voir quelques événements :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/prometheus-query-falco.png align="left")

Ensuite, nous devons configurer la vue UI pour les événements, et pour cela nous utiliserons Grafana.

Il existe de nombreuses façons d'installer Grafana. Dans mon cas [j'utiliserai un conteneur Docker Grafana](https://grafana.com/docs/grafana/latest/installation/docker/) (j'exécuterai Grafana sur le même hôte où Prometheus est en cours d'exécution : raspberripi.home) :

```python
docker pull grafana/grafana:main-ubuntu
mkdir -p /data/grafana
chown syslog /data/grafana
docker run --user 104 --name grafana --detach --tty --volume /data/grafana:/var/lib/grafana -p 3000:3000 grafana/grafana:main-ubuntu
```

Une fois Grafana démarré, vous devrez changer votre mot de passe et vous devrez également vous connecter avec Prometheus :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-prometheus-falco.png align="left")

Une fois Grafana démarré, nous pouvons [importer le tableau de bord Falco](https://grafana.com/grafana/dashboards/11914) comme [expliqué ici](https://grafana.com/docs/reference/export_import/).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/falco-grafana-integration.png align="left")

Une fois le tableau de bord importé, nous pouvons générer quelques événements pour déclencher Falco sur l'hôte où il est installé :

```python
[root@macmini2 ~]# for i in $(seq 1 60); do docker run --rm --interactive --tty --privileged fedora:latest /bin/bash -c ls; touch /root/test; rm -f /root/test; sleep 1; done
```

Après un petit moment, vous devriez voir quelque chose comme ceci sur votre tableau de bord Grafana :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-falco-dashboard.png align="left")

Les événements s'écoulent, et vous pouvez voir de quel hôte ils proviennent.

## **Comment créer des alertes pour vos événements Falco**

Idéalement, si vous avez les événements Falco dans Grafana, vous pouvez en faire des éléments actionnables et générer des alertes à partir de ceux-ci.

Je ne veux pas être bombardé d'alertes non critiques, donc la première chose à savoir est à quel niveau d'événements filtrer :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-priority-events.png align="left")

Tout ce qui a une priorité inférieure à 3 sera traité comme une alerte.

Grafana a [une bonne documentation sur la façon de configurer une alerte](https://grafana.com/docs/grafana/latest/alerting/unified-alerting/alerting-rules/create-grafana-managed-rule/), donc je vais montrer ici uniquement le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-falco-alert-definition.png align="left")

L'étape suivante consiste à envoyer les alertes quelque part.

## **Les alertes doivent aller quelque part – Comment définir un point de contact en utilisant Discord**

Pour cet exemple, nous utiliserons [Discord](https://discord.com/) comme destination pour les alertes. Discord a un guide très détaillé sur la façon de configurer un [WebHook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks), donc je vais vous montrer ici uniquement les résultats finaux de mon Webhook Discord :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-discord-webhook.png align="left")

Nous copions cette URL et configurerons ensuite un nouveau point de contact Grafana qui utilise notre Webhook Discord (*nous définissons cela comme un point de contact par défaut pour toutes les alertes*) :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-contact-point-discord.png align="left")

À partir de là, nous pouvons envoyer un message de test à Discord, juste pour confirmer que ce pipeline fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-discord-events-test.png align="left")

Nous nous rapprochons. Maintenant, si nous retournons à notre définition d'alerte, nous devrions voir qu'elle est dans l'état 'firing' :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-falco-alert-firing.png align="left")

Et si tout se passe bien, nous voyons également notre première alerte Falco dans Discord :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-falco-discord-alert.png align="left")

Nous pouvons voir ici tous les champs que nous obtenons dans la sortie journalctl. La différence est que tous ces messages proviendront de tous les serveurs où vous définissez le pont Falco-Prometheus-Grafana.

## **Mention honorable : Comment agréger les alertes en utilisant Falcon Sidekick/ Falcon Sidekick-UI**

[Falco Sidekick](https://github.com/falcosecurity/falcosidekick) est une autre façon de collecter et d'envoyer des événements vers d'autres destinations, comme [Falco Sidekick-UI](https://github.com/falcosecurity/falcosidekick-ui). Mais il ne vous indiquera pas l'hôte d'origine (au moins jusqu'à Falco 0.31.1).

Cela n'est probablement pas un problème pour une alerte provenant d'un cluster K8s ou d'une application conteneurisée où le nom de l'image vous donnera beaucoup d'informations. Mais si votre événement se produit dans un environnement bare-metal, et que vous avez plus de 2 machines, cela deviendra un casse-tête.

Pour cette raison, je ne couvrirai pas Sidekick ici – vous pouvez rester avec l'intégration Grafana pour le moment.

# **En savoir plus**

Falco dispose d'un excellent environnement d'apprentissage interactif [environnement](https://falco.org/docs/getting-started/third-party/learning/). Vous devriez l'essayer pour voir ce qui est possible. Il y a beaucoup de choses que je n'ai pas couvertes ici, comme les exceptions de règles par exemple.

De plus, saviez-vous que Falco peut être étendu en utilisant des [plugins](https://falco.org/docs/plugins/) ? Vous pouvez vous amuser et apprendre en utilisant C++ ou Go comme langage de choix.

Le blog de Falco contient de nombreux [articles intéressants](https://falco.org/blog/), y compris des publications sur les dernières menaces.

Enfin, le projet dispose d'une communauté très active sur [de nombreux canaux](https://falco.org/community/). Choisissez le vôtre et explorez.

N'hésitez pas à [forker mon code](https://github.com/josevnz/Falco) et à signaler [tout problème](https://github.com/josevnz/Falco/issues) si vous en trouvez. Mais surtout, explorez et apprenez en faisant.