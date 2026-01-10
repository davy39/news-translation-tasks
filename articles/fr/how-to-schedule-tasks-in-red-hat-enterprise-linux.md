---
title: Comment planifier des tâches dans Red Hat Enterprise Linux
subtitle: ''
author: Hang Hu
co_authors: []
series: null
date: '2025-06-26T00:51:21.744Z'
originalURL: https://freecodecamp.org/news/how-to-schedule-tasks-in-red-hat-enterprise-linux
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750869114329/79072c41-988a-41f2-9e2f-25618d78fefc.png
tags:
- name: RHEL
  slug: rhel
- name: Linux
  slug: linux
- name: rhcsa
  slug: rhcsa
seo_title: Comment planifier des tâches dans Red Hat Enterprise Linux
seo_desc: Red Hat Enterprise Linux (RHEL) is a leading enterprise-grade Linux distribution
  widely regarded as the gold standard for mission-critical server environments. It
  provides robust, secure, and scalable solutions for organizations ranging from small
  bu...
---

Red Hat Enterprise Linux (RHEL) est une distribution Linux de niveau entreprise, largement considérée comme la référence en matière d'environnements serveurs critiques. Elle offre des solutions robustes, sécurisées et évolutives pour les organisations, allant des petites entreprises aux sociétés du Fortune 500, alimentant tout, des serveurs web et des bases de données à l'infrastructure cloud et aux applications conteneurisées.

Vous pouvez utiliser les capacités de planification des tâches de RHEL dans des scénarios tels que l'automatisation de la maintenance du système (par exemple, la rotation des journaux ou les opérations de sauvegarde), la gestion des tâches administratives de routine (comme le nettoyage des comptes utilisateurs ou les mises à jour de sécurité), ou l'orchestration de flux de travail complexes dans des environnements d'entreprise. Ces outils de planification sont essentiels pour maintenir la santé du système et garantir que les opérations critiques s'exécutent sans intervention manuelle.

Pour les administrateurs système, pensez à la planification des tâches comme l'épine dorsale de la gestion automatisée des systèmes, vous permettant de configurer des processus qui s'exécutent de manière fiable en arrière-plan tandis que vous vous concentrez sur des initiatives plus stratégiques. Sa puissance réside dans sa flexibilité et sa fiabilité, en faisant une compétence indispensable pour quiconque gère des systèmes Linux dans des environnements de production.

Dans ce tutoriel, vous apprendrez à planifier des tâches dans Red Hat Enterprise Linux en utilisant divers outils et techniques intégrés. Ce contenu fait partie de **Planifier des tâches futures**, qui est le chapitre 2 du cours [Administration système Red Hat (RH134)](https://labex.io/courses/red-hat-system-administration-rh134-labs). RH134 est un cours fondamental pour la certification Red Hat Certified System Administrator (RHCSA), l'une des certifications les plus respectées dans le domaine de l'administration Linux.

Ce tutoriel pratique offre une expérience concrète des concepts de planification couverts dans le programme RH134, vous donnant les compétences nécessaires pour automatiser efficacement les tâches dans des environnements RHEL d'entreprise.

### Voici ce que nous allons couvrir :

* [Comment planifier un travail ponctuel avec 'at'](#heading-comment-planifier-un-travail-ponctuel-avec-at)

* [Comment gérer les travaux 'at'](#heading-comment-gerer-les-travaux-at)

* [Comment planifier des travaux utilisateur récurrents avec 'crontab'](#heading-comment-planifier-des-travaux-utilisateur-recurrents-avec-crontab)

* [Comment gérer les entrées 'crontab' de l'utilisateur](#heading-comment-gerer-les-entrees-crontab-de-lutilisateur)

* [Comment planifier des travaux système récurrents avec les répertoires cron](#heading-comment-planifier-des-travaux-systeme-recurrents-avec-les-repertoires-cron)

* [Comment configurer les temporisateurs systemd pour les tâches récurrentes](#heading-comment-configurer-les-temporisateurs-systemd-pour-les-taches-recurrentes)

* [Comment gérer les fichiers temporaires avec systemd-tmpfiles](#heading-comment-gerer-les-fichiers-temporaires-avec-systemd-tmpfiles)

## **Prérequis**

Ce tutoriel est conçu pour être accessible aux débutants ! Vous avez juste besoin d'une familiarité de base avec l'utilisation de la ligne de commande Linux. Si vous pouvez naviguer dans les répertoires et exécuter des commandes simples, vous êtes prêt à commencer.

Pour ceux qui cherchent à approfondir leurs connaissances RHEL, l'[Arbre de compétences RHEL](https://labex.io/skilltrees/rhel) offre des laboratoires pratiques complets, y compris [RH124](https://labex.io/courses/red-hat-system-administration-rh124-labs), [RH134](https://labex.io/courses/red-hat-system-administration-rh134-labs), [RH294](https://labex.io/courses/red-hat-enterprise-linux-automation-with-ansible-rh294), et d'autres cours pour les certifications RHCSA et RHCE.

Ne vous inquiétez pas si vous êtes nouveau dans Red Hat Enterprise Linux – je vais tout expliquer étape par étape, et ces concepts fonctionnent sur la plupart des distributions Linux également.

## **Comment planifier un travail ponctuel avec 'at'**

Tout d'abord, apprenons à planifier un travail pour qu'il s'exécute une fois à un moment futur en utilisant la commande `at`. La commande `at` est utile pour exécuter des commandes qui n'ont pas besoin d'être exécutées de manière répétée. Nous allons planifier un travail simple, inspecter ses détails, puis le supprimer.

Dans ce tutoriel, nous travaillerons directement sur le système local pour apprendre la planification des tâches. Vous exécuterez toutes les commandes dans votre environnement de terminal actuel.

Planifions un travail pour imprimer la date et l'heure actuelles dans un fichier nommé `~/myjob.txt` dans votre répertoire personnel. Nous allons le planifier pour qu'il s'exécute dans 3 minutes :

```bash
at now + 3 minutes << EOF
date > ~/myjob.txt
EOF
```

Le message `warning: commands will be executed using /bin/sh` est normal. La sortie `job N at ...` indique le numéro du travail et l'heure d'exécution planifiée. Notez le numéro du travail, car vous en aurez besoin plus tard.

Ensuite, planifions un autre travail de manière interactive. Cette méthode est utile pour entrer plusieurs commandes ou des scripts plus complexes. Nous allons planifier un travail pour ajouter "Hello from at job!" à `~/at_output.txt` dans 5 minutes :

```bash
at now + 5 minutes
```

Après avoir tapé la commande et appuyé sur Entrée, vous verrez un prompt `at>`. Tapez votre commande, puis appuyez sur `Ctrl+d` pour terminer :

```bash
at > echo "Hello from at job!" >> ~/at_output.txt
at > Ctrl+d
```

Pour voir les travaux actuellement dans la file d'attente `at`, utilisez la commande `atq`. Cette commande liste tous les travaux `at` en attente pour l'utilisateur actuel.

```bash
atq
```

La sortie affichera le numéro du travail, l'heure planifiée, la file d'attente et l'utilisateur qui l'a planifié.

![Sortie de la commande atq montrant les travaux planifiés](https://cdn.hashnode.com/res/hashnode/image/upload/v1750726190789/d2dd54c0-80a0-4bb2-8561-3114bb279387.png align="center")

Vous pouvez inspecter les commandes qu'un travail `at` spécifique exécutera en utilisant la commande `at -c` suivie du numéro du travail. Remplacez `N` par l'un des numéros de travail que vous avez notés précédemment.

```bash
at -c N
```

Cette commande affichera le script shell que `at` exécutera pour ce travail. Vous devriez voir la commande `date > ~/myjob.txt` ou `echo "Hello from at job!" >> ~/at_output.txt` dans la sortie.

Enfin, pour supprimer un travail `at` planifié, utilisez la commande `atrm` suivie du numéro du travail. Supprimons le premier travail que nous avons planifié. Remplacez `N` par le numéro du travail de votre premier travail.

```bash
atrm N
```

Après avoir supprimé le travail, vous pouvez utiliser `atq` à nouveau pour vérifier qu'il n'est plus dans la file d'attente.

```bash
atq
```

Vous devriez maintenant ne voir que le deuxième travail (s'il ne s'est pas encore exécuté) ou une file d'attente vide si les deux travaux ont été supprimés ou exécutés.

Cela complète la première étape de la planification de travaux ponctuels avec la commande `at`.

## **Comment gérer les travaux 'at'**

Maintenant, approfondissons la gestion des travaux `at`, y compris la planification de travaux avec différentes files d'attente et la vérification de leur exécution. Comprendre les files d'attente `at` peut être utile pour prioriser les tâches ou séparer différents types de travaux ponctuels.

Nous continuerons à travailler sur le système local pour explorer des fonctionnalités plus avancées de gestion des travaux `at`.

La commande `at` vous permet de spécifier une file d'attente en utilisant l'option `-q`. Les files d'attente sont des lettres uniques de `a` à `z`. La file d'attente `a` est celle par défaut, et les travaux dans les files d'attente `a` à `z` sont exécutés avec une priorité décroissante (niceness). La file d'attente `a` a la priorité la plus élevée, et la file d'attente `z` a la priorité la plus faible. La file d'attente `b` est réservée aux travaux par lots.

Planifions un travail dans la file d'attente `g` (une file d'attente de priorité inférieure) pour qu'il s'exécute dans 2 minutes. Ce travail créera un fichier nommé `~/queue_g_job.txt` avec un horodatage :

```bash
at -q g now + 2 minutes << EOF
date > ~/queue_g_job.txt
EOF
```

Vous verrez une sortie similaire à `job N at ...`. Notez ce numéro de travail.

Ensuite, planifions un autre travail, cette fois dans la file d'attente `b` (file d'attente par lots), qui est généralement utilisée pour les travaux qui peuvent s'exécuter lorsque la charge du système est faible. Ce travail ajoutera "Batch job executed!" à `~/batch_job.txt`. Nous allons le planifier pour qu'il s'exécute dans 4 minutes :

```bash
at -q b now + 4 minutes << EOF
echo "Batch job executed!" >> ~/batch_job.txt
EOF
```

Notez à nouveau le numéro du travail.

Pour voir tous les travaux en attente, y compris ceux dans différentes files d'attente, utilisez `atq`.

```bash
atq
```

Vous devriez maintenant voir les deux travaux listés, avec leurs lettres de file d'attente respectives (`g` et `b`).

![Sortie de la commande atq montrant les travaux planifiés](https://cdn.hashnode.com/res/hashnode/image/upload/v1750726218380/bcc9d551-0530-48d1-bf7f-46073c6f77a6.png align="center")

Maintenant, attendez que vos travaux planifiés s'exécutent. Attendez au moins 5 minutes pour permettre à tous les travaux de se terminer. Vous pouvez vérifier si les fichiers créés par vos travaux `at` existent et contiennent le contenu attendu.

Vérifiez `~/queue_g_job.txt` :

```bash
cat ~/queue_g_job.txt
```

Vous devriez voir une chaîne de date et d'heure.

Vérifiez `~/batch_job.txt` :

```bash
cat ~/batch_job.txt
```

Vous devriez voir "Batch job executed!".

Si les fichiers ne sont pas présents ou vides, cela peut signifier que les travaux ne se sont pas encore exécutés, ou qu'il y a eu un problème avec la commande. Vous pouvez revérifier `atq` pour voir s'ils sont toujours en attente.

## **Comment planifier des travaux utilisateur récurrents avec 'crontab'**

Ensuite, vous apprendrez à planifier des tâches récurrentes pour un utilisateur spécifique en utilisant `crontab`. Contrairement aux travaux `at`, qui s'exécutent une fois, les travaux `cron` s'exécutent de manière répétée à des intervalles spécifiés. Cela est idéal pour la maintenance de routine, les sauvegardes de données ou la génération de rapports.

Nous continuerons à travailler sur le système local pour apprendre la gestion de crontab utilisateur.

La commande `crontab` permet aux utilisateurs de créer, modifier et consulter leurs propres travaux `cron`. Chaque utilisateur a son propre fichier `crontab`.

Pour modifier votre fichier `crontab`, utilisez la commande `crontab -e`. Cela ouvrira votre fichier `crontab` dans l'éditeur de texte par défaut (généralement `vim`).

```bash
crontab -e
```

**Instructions pour l'éditeur Vim :**

* Appuyez sur `i` pour entrer en mode insertion (vous verrez `-- INSERT --` en bas)

* Utilisez les touches fléchées pour naviguer

* Pour sauvegarder et quitter : Appuyez sur `Esc` pour quitter le mode insertion, puis tapez `:wq` et appuyez sur `Entrée`

* Pour quitter sans sauvegarder : Appuyez sur `Esc`, puis tapez `:q!` et appuyez sur `Entrée`

À l'intérieur de l'éditeur, vous ajouterez une nouvelle ligne pour définir votre travail `cron`. Une entrée `cron` a cinq champs de temps et de date, suivis de la commande à exécuter. Les champs sont :

* **Minute (0-59)**

* **Heure (0-23)**

* **Jour du mois (1-31)**

* **Mois (1-12)**

* **Jour de la semaine (0-7, où 0 ou 7 est dimanche)**

Vous pouvez utiliser `*` comme caractère générique pour signifier "tous" pour un champ, ou `/` pour spécifier des valeurs d'étape (par exemple, `*/5` pour toutes les 5 minutes).

Planifions un travail qui ajoute la date et l'heure actuelles à un fichier nommé `~/my_cron_log.txt` toutes les minutes. Cela nous permettra d'observer rapidement le travail `cron` en action.

Suivez ces étapes dans Vim :

1. Appuyez sur `i` pour entrer en mode insertion

2. Ajoutez la ligne suivante au fichier `crontab` :

```bash
* * * * * /usr/bin/date >> ~/my_cron_log.txt
```

3. Appuyez sur `Esc` pour quitter le mode insertion

4. Tapez `:wq` et appuyez sur `Entrée` pour sauvegarder et quitter

Vous devriez voir un message indiquant qu'un nouveau `crontab` a été installé :

```plaintext
crontab: installing new crontab
```

Pour vérifier que votre travail `cron` a été ajouté avec succès, vous pouvez lister vos entrées `crontab` en utilisant la commande `crontab -l` :

```bash
crontab -l
```

Vous devriez voir la ligne que vous venez d'ajouter :

```plaintext
* * * * * /usr/bin/date >> ~/my_cron_log.txt
```

Maintenant, attendez une minute ou deux pour permettre au travail `cron` de s'exécuter au moins une fois. Vous pouvez vérifier l'heure actuelle pour voir quand la prochaine minute se produira :

```bash
date
```

Après avoir attendu au moins deux minutes pour permettre au travail cron de s'exécuter quelques fois, vérifiez le contenu du fichier `~/my_cron_log.txt`.

```bash
cat ~/my_cron_log.txt
```

Vous devriez voir une ou plusieurs lignes, chacune contenant une date et une heure, indiquant que votre travail `cron` a été exécuté.

![Sortie du travail cron dans le fichier journal](https://cdn.hashnode.com/res/hashnode/image/upload/v1750726409656/bfd85cf0-316a-4c1d-89c2-0d60c30cd33f.png align="center")

```plaintext
Mon Apr 8 10:30:01 AM EDT 2025
Mon Apr 8 10:31:01 AM EDT 2025
```

## **Comment gérer les entrées 'crontab' de l'utilisateur**

Maintenant, vous apprendrez des techniques plus avancées pour gérer les entrées `crontab` de l'utilisateur, y compris la modification des travaux existants, l'ajout de plusieurs travaux et la compréhension des chaînes spéciales `cron`. Une gestion efficace de `crontab` est cruciale pour automatiser les tâches de routine.

Nous continuerons à travailler sur le système local pour explorer des techniques avancées de gestion de crontab.

Commençons par ajouter un nouveau travail `cron`. Ce travail ajoutera "Hello from cron!" à `~/cron_messages.txt` toutes les deux minutes.

Ouvrez votre `crontab` pour l'éditer :

```bash
crontab -e
```

Dans Vim :

1. Appuyez sur `i` pour entrer en mode insertion

2. Ajoutez la ligne suivante au fichier `crontab` :

```bash
*/2 * * * * echo "Hello from cron!" >> ~/cron_messages.txt
```

3. Appuyez sur `Esc` pour quitter le mode insertion

4. Tapez `:wq` et appuyez sur `Entrée` pour sauvegarder et quitter

Vérifiez que l'entrée est ajoutée :

```bash
crontab -l
```

Vous devriez voir la ligne nouvellement ajoutée.

Maintenant, ajoutons un autre travail `cron` qui s'exécute quotidiennement à 08:00 AM. Ce travail enregistrera l'utilisation du disque de votre répertoire personnel dans `~/disk_usage.log`.

Ouvrez votre `crontab` pour l'éditer à nouveau :

```bash
crontab -e
```

Dans Vim :

1. Appuyez sur `i` pour entrer en mode insertion

2. Ajoutez la ligne suivante sous la précédente :

```bash
0 8 * * * du -sh ~ >> ~/disk_usage.log
```

3. Appuyez sur `Esc` pour quitter le mode insertion

4. Tapez `:wq` et appuyez sur `Entrée` pour sauvegarder et quitter

Vérifiez que les deux entrées sont présentes :

```bash
crontab -l
```

Vous devriez maintenant voir les deux travaux `cron` listés.

`cron` prend également en charge des chaînes spéciales qui peuvent simplifier les planifications courantes. Celles-ci incluent `@reboot`, `@yearly`, `@annually`, `@monthly`, `@weekly`, `@daily`, `@midnight` et `@hourly`. Par exemple, `@hourly` est équivalent à `0 * * * *`.

Ajoutons un travail qui s'exécute toutes les heures et enregistre le temps de fonctionnement du système dans `~/uptime_log.txt`.

Ouvrez votre `crontab` pour l'éditer :

```bash
crontab -e
```

Dans Vim :

1. Appuyez sur `i` pour entrer en mode insertion

2. Ajoutez la ligne suivante :

```bash
@hourly uptime >> ~/uptime_log.txt
```

3. Appuyez sur `Esc` pour quitter le mode insertion

4. Tapez `:wq` et appuyez sur `Entrée` pour sauvegarder et quitter

Vérifiez les trois entrées :

```bash
crontab -l
```

Vous devriez maintenant voir les trois travaux `cron`.

Pour démontrer l'effet de ces travaux, nous allons attendre une courte période. Comme les travaux sont planifiés à différents intervalles, nous ne les verrons pas tous s'exécuter immédiatement, mais nous pouvons vérifier la configuration.

Attendez au moins 3 minutes pour permettre au travail `*/2` de s'exécuter au moins une fois.

Vérifiez le fichier `~/cron_messages.txt` :

```bash
cat ~/cron_messages.txt
```

Vous devriez voir au moins un message "Hello from cron!".

```plaintext
Hello from cron!
```

Les fichiers `~/disk_usage.log` et `~/uptime_log.txt` peuvent ne pas être créés encore, selon l'heure actuelle, car ils sont planifiés pour une exécution quotidienne et horaire, respectivement. L'important est que leurs entrées soient correctement configurées dans votre `crontab`.

## **Comment planifier des travaux système récurrents avec les répertoires** `cron`

Dans cette étape, vous apprendrez à planifier des tâches récurrentes à l'échelle du système en utilisant les répertoires `cron`. Contrairement aux entrées `crontab` utilisateur, qui sont spécifiques à un utilisateur, les travaux `cron` système sont gérés par l'utilisateur root et affectent l'ensemble du système. Ceux-ci sont généralement utilisés pour la maintenance du système, la rotation des journaux et d'autres tâches administratives.

Nous continuerons à travailler sur le système local pour explorer la configuration des travaux cron à l'échelle du système.

Les travaux `cron` à l'échelle du système sont définis dans `/etc/crontab` ou en plaçant des scripts dans des répertoires spécifiques :

* `/etc/cron.hourly/` : Les scripts dans ce répertoire s'exécutent une fois par heure.

* `/etc/cron.daily/` : Les scripts dans ce répertoire s'exécutent une fois par jour.

* `/etc/cron.weekly/` : Les scripts dans ce répertoire s'exécutent une fois par semaine.

* `/etc/cron.monthly/` : Les scripts dans ce répertoire s'exécutent une fois par mois.

Ces répertoires sont traités par l'utilitaire `run-parts`, qui exécute tous les fichiers exécutables qu'ils contiennent.

Pour gérer les travaux `cron` système, vous avez besoin de privilèges root. Comme l'utilisateur labex a accès sudo, nous pouvons utiliser `sudo` pour les commandes requises.

Créons un script simple qui enregistre un message dans le journal système. Nous placerons ce script dans `/etc/cron.hourly/` pour qu'il s'exécute toutes les heures.

Tout d'abord, créez le fichier de script `/etc/cron.hourly/my_hourly_script` :

```bash
sudo nano /etc/cron.hourly/my_hourly_script
```

Ajoutez le contenu suivant au fichier :

```bash
#!/bin/bash
logger "Hourly cron job executed at $(date)"
```

Enregistrez et quittez l'éditeur (`Ctrl+o`, `Entrée`, `Ctrl+x` dans `nano`).

Ensuite, vous devez rendre le script exécutable. Sans les permissions d'exécution, `run-parts` l'ignorera.

```bash
sudo chmod +x /etc/cron.hourly/my_hourly_script
```

Maintenant, vérifions que le script est exécutable :

```bash
ls -l /etc/cron.hourly/my_hourly_script
```

Vous devriez voir `x` dans les permissions, par exemple : `-rwxr-xr-x`.

Comme les travaux `cron.hourly` s'exécutent une fois par heure, nous ne pouvons pas attendre une heure complète pour vérifier leur exécution dans ce tutoriel. Mais nous pouvons déclencher manuellement la commande `run-parts` pour le répertoire horaire afin de simuler son exécution.

```bash
sudo run-parts /etc/cron.hourly/
```

Cette commande exécutera tous les scripts exécutables dans `/etc/cron.hourly/`. Le script que nous avons créé utilise la commande `logger` pour écrire des messages dans le journal système.

Dans un système RHEL réel, vous pourriez vérifier les journaux système en utilisant `journalctl` ou `/var/log/messages` pour vérifier que le script s'est exécuté avec succès.

Cela complète l'étape de gestion des travaux cron système. Le script restera en place et s'exécutera toutes les heures dans un environnement système réel.

## **Comment configurer les temporisateurs** `systemd` **pour les tâches récurrentes**

Ensuite, vous apprendrez à propos des temporisateurs `systemd`, qui sont une alternative moderne à `cron` pour planifier des tâches sur les systèmes Linux. Les temporisateurs `systemd` offrent plus de flexibilité et une meilleure intégration avec l'écosystème `systemd`.

Les temporisateurs `systemd` fonctionnent en conjonction avec les unités de service `systemd`. Une unité de temporisateur (fichier `.timer`) définit quand une tâche doit s'exécuter, et une unité de service (fichier `.service`) définit quelle tâche doit être exécutée.

Nous continuerons à travailler sur le système local pour explorer la configuration des temporisateurs systemd.

Vous aurez besoin de privilèges root pour créer des fichiers d'unité `systemd` dans les répertoires système. Comme l'utilisateur labex a accès sudo, nous pouvons utiliser `sudo` pour les commandes requises.

Créons un service simple qui enregistre un message dans un fichier. Nous placerons ce fichier d'unité de service dans `/etc/systemd/system/` qui est l'endroit où les unités de service personnalisées sont généralement stockées.

Créez le fichier d'unité de service `/etc/systemd/system/my-custom-task.service` :

```bash
sudo nano /etc/systemd/system/my-custom-task.service
```

Ajoutez le contenu suivant au fichier :

```ini
[Unit]
Description=My Custom Scheduled Task

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo "My custom task executed at $(date)" >> /var/log/my-custom-task.log'
```

Enregistrez et quittez l'éditeur (`Ctrl+o`, `Entrée`, `Ctrl+x` dans `nano`).

Ensuite, créez le fichier d'unité de temporisateur `/etc/systemd/system/my-custom-task.timer`. Ce temporisateur activera notre service toutes les 5 minutes.

```bash
sudo nano /etc/systemd/system/my-custom-task.timer
```

Ajoutez le contenu suivant au fichier :

```ini
[Unit]
Description=Run My Custom Scheduled Task every 5 minutes

[Timer]
OnCalendar=*:0/5
Persistent=true

[Install]
WantedBy=timers.target
```

Enregistrez et quittez l'éditeur.

**Explication de** `OnCalendar` :

* `*:0/5` signifie "toutes les 5 minutes".

* `*` pour l'année, le mois, le jour, l'heure (n'importe quelle valeur).

* `0/5` pour la minute, ce qui signifie à partir de la minute 0, toutes les 5 minutes (0, 5, 10, ..., 55).

Dans un environnement `systemd` typique, vous exécuteriez maintenant `systemctl daemon-reload` pour informer `systemd` des nouveaux fichiers d'unité, puis `systemctl enable --now my-custom-task.timer` pour démarrer le temporisateur.

Vérifions l'existence des fichiers créés :

```bash
ls -l /etc/systemd/system/my-custom-task.service
ls -l /etc/systemd/system/my-custom-task.timer
```

Vous devriez voir une sortie indiquant que les deux fichiers existent.

Pour simuler l'exécution du service, vous pouvez exécuter manuellement la commande définie dans `ExecStart` :

```bash
sudo /bin/bash -c 'echo "My custom task executed at $(date)" >> /var/log/my-custom-task.log'
```

Maintenant, vérifiez le fichier journal pour voir la sortie :

```bash
sudo cat /var/log/my-custom-task.log
```

Vous devriez voir le message que vous venez d'enregistrer :

```plaintext
My custom task executed at Tue Jun 10 06:54:40 UTC 2025
```

Cela complète l'étape de configuration du temporisateur systemd. Les fichiers d'unité de service et de temporisateur resteront en place pour référence.

## **Comment gérer les fichiers temporaires avec** `systemd-tmpfiles`

Maintenant, vous apprendrez à gérer les fichiers et répertoires temporaires en utilisant `systemd-tmpfiles`. Cet utilitaire fait partie de `systemd` et est responsable de la création, de la suppression et du nettoyage des fichiers et répertoires volatils et temporaires. Il est couramment utilisé pour gérer `/tmp`, `/var/tmp` et d'autres emplacements de stockage temporaire, garantissant que les anciens fichiers sont supprimés périodiquement.

Nous continuerons à travailler sur le système local pour explorer la configuration de systemd-tmpfiles.

Vous aurez besoin de privilèges root pour configurer `systemd-tmpfiles`. Comme l'utilisateur labex a accès sudo, nous pouvons utiliser `sudo` pour les commandes requises.

`systemd-tmpfiles` lit les fichiers de configuration à partir de `/etc/tmpfiles.d/` et `/usr/lib/tmpfiles.d/`. Ces fichiers définissent des règles pour créer, supprimer et gérer des fichiers et répertoires.

Créons un fichier de configuration personnalisé pour gérer un nouveau répertoire temporaire. Nous allons créer un répertoire `/run/my_temp_dir` et configurer `systemd-tmpfiles` pour supprimer les fichiers plus anciens que 1 minute.

Créez le fichier de configuration `/etc/tmpfiles.d/my_temp_dir.conf` :

```bash
sudo nano /etc/tmpfiles.d/my_temp_dir.conf
```

Ajoutez le contenu suivant au fichier :

```bash
d /run/my_temp_dir 0755 labex labex 1m
```

**Explication de la ligne :**

* `d` : Spécifie que cette entrée définit un répertoire.

* `/run/my_temp_dir` : Le chemin vers le répertoire.

* `0755` : Les permissions pour le répertoire.

* `labex labex` : Le propriétaire et le groupe pour le répertoire.

* `1m` : L'âge après lequel les fichiers dans ce répertoire doivent être supprimés (1 minute).

Enregistrez et quittez l'éditeur (`Ctrl+o`, `Entrée`, `Ctrl+x` dans `nano`).

Maintenant, disons à `systemd-tmpfiles` d'appliquer cette configuration. L'option `--create` créera le répertoire s'il n'existe pas.

```bash
sudo systemd-tmpfiles --create /etc/tmpfiles.d/my_temp_dir.conf
```

Vérifiez que le répertoire a été créé avec les permissions et le propriétaire corrects :

```bash
ls -ld /run/my_temp_dir
```

Vous devriez voir une sortie similaire à :

```plaintext
drwxr-xr-x 2 labex labex 6 Jun 10 06:55 /run/my_temp_dir
```

Ensuite, créons un fichier de test dans ce nouveau répertoire temporaire :

```bash
sudo touch /run/my_temp_dir/test_file.txt
```

Vérifiez que le fichier existe :

```bash
ls -l /run/my_temp_dir/test_file.txt
```

Maintenant, nous devons attendre plus d'une minute pour que le fichier devienne "ancien" selon notre configuration. Attendez au moins 70 secondes (1 minute et 10 secondes).

Après avoir attendu plus d'une minute, nous allons exécuter manuellement `systemd-tmpfiles` avec l'option `--clean` pour déclencher le processus de nettoyage basé sur notre configuration.

```bash
sudo systemd-tmpfiles --clean /etc/tmpfiles.d/my_temp_dir.conf
```

Enfin, vérifiez si le fichier `test_file.txt` a été supprimé :

```bash
ls -l /run/my_temp_dir/test_file.txt
```

Vous devriez obtenir une erreur "No such file or directory", indiquant que `systemd-tmpfiles` a réussi à nettoyer l'ancien fichier.

Cela complète la configuration de systemd-tmpfiles. Le fichier de configuration et le répertoire temporaire resteront en place pour référence.

## **Résumé**

Dans ce tutoriel, vous avez appris à planifier et gérer des tâches ponctuelles en utilisant la commande `at`, y compris la planification de travaux de manière interactive et non interactive, la visualisation de la file d'attente `at` avec `atq`, et la suppression des travaux en attente avec `atrm`. Vous avez également appris à planifier des tâches utilisateur récurrentes en utilisant `crontab`, y compris comment éditer, lister et supprimer des travaux cron, et vous avez appris la syntaxe cron pour spécifier les heures d'exécution.

Nous avons également démontré comment planifier des tâches système récurrentes en plaçant des scripts dans des répertoires cron standard (`/etc/cron.hourly`, `/etc/cron.daily`, etc.) et comment créer des travaux cron personnalisés dans `/etc/cron.d`.

Enfin, vous avez exploré la planification avancée des tâches avec les temporisateurs `systemd`, en apprenant à créer et activer des unités de service et de temporisateur pour des tâches récurrentes, et comment gérer les fichiers et répertoires temporaires en utilisant `systemd-tmpfiles` pour le nettoyage automatisé.

Ce tutoriel complet a fourni une expérience pratique dans la gestion des divers besoins de planification des tâches sur les systèmes RHEL, des commandes ponctuelles simples aux processus système récurrents complexes.

Pour pratiquer les opérations de ce tutoriel, essayez le laboratoire pratique interactif : [Planifier des tâches dans Red Hat Enterprise Linux](https://labex.io/labs/rhel-schedule-tasks-in-red-hat-enterprise-linux-588897?course=red-hat-system-administration-rh134-labs).