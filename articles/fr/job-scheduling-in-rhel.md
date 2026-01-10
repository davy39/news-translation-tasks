---
title: Planification des tâches dans RHEL – cron et at expliqués avec des exemples
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-29T14:06:44.000Z'
originalURL: https://freecodecamp.org/news/job-scheduling-in-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004567.png
tags:
- name: Linux
  slug: linux
seo_title: Planification des tâches dans RHEL – cron et at expliqués avec des exemples
seo_desc: Efficiently executing tasks at designated times or in response to certain
  events is essential in RHEL's job scheduling process. With the help of various tools
  and utilities, you can easily coordinate and automate job scheduling, eliminating
  the need ...
---

Exécuter efficacement des tâches à des heures désignées ou en réponse à certains événements est essentiel dans le processus de planification des tâches de RHEL. À l'aide de divers outils et utilitaires, vous pouvez facilement coordonner et automatiser la planification des tâches, éliminant ainsi le besoin d'intervention manuelle.

Certains outils courants pour la planification des tâches dans RHEL incluent :

* cron : Un planificateur de tâches basé sur le temps dans les systèmes d'exploitation de type Unix. Les utilisateurs peuvent planifier des tâches répétitives en créant des entrées dans le fichier crontab, en spécifiant quand et à quelle fréquence ces tâches doivent s'exécuter.
    
* at : La commande `at` permet aux utilisateurs de planifier des tâches ponctuelles à exécuter à une heure spécifiée dans le futur.
    

## **Table des matières**

Voici ce que nous allons couvrir dans ce guide complet :

* [Qu'est-ce qu'un démon](#heading-quest-ce-quun-demon)?
    
* [Qu'est-ce que systemctl](#heading-quest-ce-que-systemctl)?
    
* [Planification des tâches avec at](#heading-planification-des-taches-avec-at)
    
* [Planification des tâches avec crontab](#heading-planification-des-taches-avec-crontab)
    
* [Exercices pratiques](#practical-exercise)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'un démon ?

Dans Red Hat Enterprise Linux (RHEL) et d'autres systèmes d'exploitation de type Unix, un "démon" est un processus en arrière-plan qui s'exécute en continu, fournissant généralement des services ou des fonctionnalités spécifiques au système d'exploitation ou aux applications.

Les démons sont souvent responsables de la gestion de diverses tâches telles que la gestion du matériel, la réponse aux requêtes réseau, l'exécution de tâches planifiées et la facilitation de la communication entre différents composants logiciels.

Ces tâches ne nécessitent généralement pas l'intervention directe de l'utilisateur et sont généralement effectuées sans intervention de l'utilisateur.

Des exemples courants de démons incluent les serveurs web (comme Apache ou NGINX), les serveurs de bases de données (tels que MySQL ou PostgreSQL) et les services système (comme cron pour la planification des tâches ou systemd pour la gestion de divers services système).

## Qu'est-ce que `systemctl` ?

Systemctl est un outil essentiel dans Red Hat Enterprise Linux (RHEL) qui permet aux utilisateurs de contrôler et de superviser leur système et gestionnaire de services systemd avec facilité.

Cet utilitaire en ligne de commande offre une manière transparente d'interagir avec le système d'init systemd, qui joue un rôle crucial dans le démarrage du système d'exploitation, la supervision des services et la gestion d'une gamme de fonctionnalités système.

Examinons de plus près ce que cet outil peut faire :

### Gestion des services

#### Démarrage et arrêt des services

* `systemctl start service_name` lance un service. Voici un exemple :
    

```bash
systemctl start atd
```

La commande ci-dessus `systemctl start atd` est utilisée dans les systèmes Linux pour démarrer le service `atd` (qui signifie "AT Daemon") en utilisant l'utilitaire `systemctl`.

* `systemctl stop service_name` arrête un service. Voici un exemple :
    

```bash
systemctl stop atd
```

En exécutant `systemctl stop atd`, vous instruisez le système d'arrêter le service `atd`. Par conséquent, toute tâche ou travail planifié pour s'exécuter en utilisant la commande `at` ne sera pas traité jusqu'à ce que le service soit redémarré.

#### Activation et désactivation des services

* `systemctl enable service_name` définit un service pour qu'il démarre automatiquement au démarrage. Voici un exemple :
    

```bash
systemctl enable crond
```

Ce code définit le service `crond` pour qu'il démarre automatiquement à chaque démarrage du système. Cela garantit que le service cron, responsable de la gestion des tâches planifiées, est actif et prêt à exécuter des commandes à leurs heures spécifiées sans nécessiter d'intervention manuelle après chaque redémarrage du système.

* `systemctl disable service_name` empêche un service de démarrer automatiquement au démarrage. Voici un exemple :
    

```bash
systemctl disable crond
```

L'exécution de la commande ci-dessus supprime la configuration qui permet au service `crond` de démarrer automatiquement lorsque le système démarre. Par conséquent, après un redémarrage du système, le service `crond` ne sera pas initié automatiquement. Les utilisateurs devront démarrer manuellement le service s'ils souhaitent utiliser cron pour la planification des tâches.

### Affichage du statut du service

#### Vérification du statut du service

* `systemctl status service_name` affiche le statut actuel et les informations sur un service. Voici un exemple :
    

```bash
systemctl status crond
```

Cela fournit des informations sur le fait que le service `crond` est en cours d'exécution, arrêté ou rencontre des problèmes. Il inclut généralement des détails tels que le fait que le service est actif ou inactif, quand il a été démarré ou arrêté pour la dernière fois, et tout message d'erreur ou avertissement lié à son fonctionnement.

#### Affichage de tous les services

* `systemctl list-units --type=service` liste tous les services actifs. Voici un exemple :
    

```bash
systemctl list-units --type=service
```

Cela fournit une liste complète de tous les services — à la fois actifs et inactifs — gérés par `systemd` sur le système. Cette sortie inclut des informations telles que le nom de l'unité, le statut de chargement, le statut actif (s'il est en cours d'exécution ou non) et la description de chaque service.

Toutes les commandes possibles de gestion des services `systemctl` sont listées ci-dessous. Vous pouvez explorer toutes ces commandes par vous-même pour mieux comprendre leur fonctionnement.

```bash
systemctl start <service> : Démarre un service.

systemctl stop <service> : Arrête un service.

systemctl restart <service> : Redémarre un service.

systemctl reload <service> : Recharge la configuration d'un service sans l'arrêter.

systemctl status <service> : Affiche le statut actuel et les informations sur un service.

systemctl enable <service> : Active un service pour qu'il démarre automatiquement au démarrage.

systemctl disable <service> : Désactive un service pour qu'il ne démarre pas automatiquement au démarrage.

systemctl is-active <service> : Vérifie si un service est actuellement en cours d'exécution.

systemctl is-enabled <service> : Vérifie si un service est activé pour démarrer au démarrage.

systemctl is-failed <service> : Vérifie si un service a échoué.
```

### Contrôle du système

#### Redémarrage et arrêt

* `systemctl reboot` redémarre le système. Voici un exemple :
    

```bash
systemctl reboot
```

Cela arrête le système d'exploitation, termine tous les processus et services en cours d'exécution, puis démarre le processus de démarrage. Il ramène le système à un état frais.

* `systemctl poweroff` arrête le système. Voici un exemple :
    

```bash
systemctl poweroff
```

Cela déclenche une série d'actions qui incluent l'arrêt de tous les services et processus en cours d'exécution de manière ordonnée, la sauvegarde de toute donnée nécessaire, et enfin l'arrêt du système.

#### Mise en veille et hibernation

* `systemctl suspend` met le système en état de veille. Voici un exemple :
    

```bash
systemctl suspend
```

Cela déclenche la mise en veille du système. Dans cet état, le système arrête la plupart des opérations, y compris le CPU et d'autres composants matériels, pour économiser l'énergie.

Mais il conserve l'état actuel du système en mémoire (RAM) afin que, lorsqu'il est repris, le système puisse rapidement revenir à son état précédent sans un processus de démarrage complet.

* `systemctl hibernate` met le système en hibernation. Voici un exemple :
    

```bash
systemctl hibernate
```

Il sauvegarde tout ce que vous faites sur votre ordinateur sur le disque dur, puis éteint complètement l'ordinateur. Lorsque vous le redémarrez, il restaure exactement ce sur quoi vous travailliez auparavant, comme vous l'aviez laissé. Cela est différent de la "mise en veille", qui conserve votre travail en mode basse consommation mais toujours allumé.

### Affichage des informations système

#### Affichage des journaux système

* `journalctl` affiche les journaux système et les entrées de journal. Voici un exemple :
    

```bash
journalctl
```

Cela affiche les journaux qui incluent les messages système, les messages du noyau, les journaux des services et d'autres événements enregistrés par le système.

* `journalctl -u <unit>` affiche les journaux pour une unité spécifique. Voici un exemple :
    

```bash
journalctl -u crond
```

Vous verrez les journaux qui sont liés au service `crond` spécifiquement. Cela inclut les messages, les erreurs ou d'autres informations enregistrées par le démon `crond`, qui est responsable de la gestion des tâches planifiées à l'aide du planificateur de tâches cron.

* `journalctl --since=<time>` montre les journaux depuis une heure spécifique. Voici un exemple :
    

```bash
journalctl --since "2024-01-01 08:00:00"
```

Cela récupère et affiche les journaux système qui ont été générés ou enregistrés après le 1er janvier 2023, à 8h00. Cela aide à réduire les journaux pour afficher les événements ou messages système qui se sont produits à partir de ce moment précis, et peut vous aider à dépanner ou analyser l'activité récente du système.

Ces commandes de `systemctl` sont suffisantes pour démarrer un module de planification de tâches. Vous pouvez toujours explorer plus de commandes `systemctl` par vous-même.

## Planification des tâches avec `at`

La commande `at` est utilisée pour planifier des tâches ou commandes ponctuelles qui seront exécutées à une heure future désignée. Cette fonctionnalité est particulièrement utile pour automatiser les tâches que vous devez effectuer plus tard, afin de ne pas avoir à vous en souvenir.

Pour utiliser `at`, vous devrez vérifier les points suivants :

* Assurez-vous que le démon `at` (`atd`) est en cours d'exécution pour que les tâches `at` s'exécutent. Vous pouvez utiliser la commande `systemctl` pour vérifier si `atd` est en cours d'exécution ou non. Si ce n'est pas le cas, vous pouvez utiliser `systemctl` pour le démarrer (et vous pouvez voir comment faire cela dans la section `systemctl` de ce tutoriel).
    
* Les permissions peuvent être restreintes pour les utilisateurs non-administrateurs pour utiliser `at`, selon les paramètres du système.
    
* Si vous manipulez quelque chose dans un fichier, assurez-vous d'avoir les permissions Lecture-Écriture-Exécution pour ce même fichier.
    

### Syntaxe de `at`

```bash
at <time>
```

### Exemples d'utilisation de la commande `at`

Voyons comment fonctionne la commande `at` en pratique avec quelques exemples.

Tout d'abord, voici comment vous pouvez afficher un message à une heure spécifique :

```bash
at 15:35
```

Maintenant, disons que vous devez donner des commandes qui s'exécuteront automatiquement à 15h35 :

```bash
echo "Réunion dans 30 minutes" >> sample.txt
```

Appuyez sur `Ctrl + D` pour terminer la saisie des commandes et planifier la tâche. Cela imprimera "Réunion dans 30 minutes" dans le fichier sample.txt à 15h35.

Peut-être avez-vous un script nommé `backup.sh` et vous voulez qu'il s'exécute à 2h du matin. Voici comment vous feriez cela :

```bash
at -f backup.sh 02:00
```

Ce code planifie le script `backup.sh` pour qu'il s'exécute à 2h00. Le contenu de `backup.sh` sera exécuté comme s'il avait été saisi directement dans le terminal à cette heure spécifiée.

Vous pouvez également utiliser la commande suivante pour voir une liste des tâches `at` en attente :

```bash
atq
```

La commande `atq` vous aide à afficher et gérer une liste des tâches `at` en attente, vous permettant de référencer facilement les tâches planifiées et leurs heures d'exécution.

Voici un exemple de sortie de la commande `atq` :

```bash
10	Wed Jan 12 03:00:00 2023 a user123
```

* La première colonne représente le numéro de la tâche.
    
* La deuxième colonne montre l'heure d'exécution planifiée pour chaque tâche.
    
* La troisième colonne indique le niveau de priorité ('a' dans ce cas).
    
* 'a' est généralement le niveau de priorité par défaut attribué aux tâches `at`, et à mesure que les lettres descendent dans l'alphabet ('b', 'c', 'd', et ainsi de suite), le niveau de priorité diminue.
    
* La quatrième colonne affiche le nom d'utilisateur de l'utilisateur qui a planifié la tâche (si disponible).
    

Voici comment supprimer une tâche :

```bash
atrm 10
```

Le code ci-dessus supprime la tâche `at` avec le numéro d'ID '3' de la file d'attente `at`, l'empêchant de s'exécuter à son heure planifiée. Vous pouvez trouver l'ID de la tâche avec la commande `atq`. L'ID de la tâche est dans la 1ère colonne de la sortie.

### `at.allow` et `at.deny`

Les fichiers `at.allow` et `at.deny` sont utilisés pour contrôler l'accès des utilisateurs à la planification des tâches en utilisant `at`. Ces fichiers sont généralement situés dans `/etc/` dans RHEL.

Le fichier `at.allow` spécifie la liste des utilisateurs autorisés à utiliser la commande `at` pour planifier des tâches. Si ce fichier existe, seuls les utilisateurs listés dans celui-ci peuvent planifier des tâches `at`. Si le fichier n'existe pas, il se comporte comme s'il était vide, permettant à tous les utilisateurs sauf ceux restreints par `at.deny`.

Le fichier `at.deny` spécifie la liste des utilisateurs à qui l'accès à la commande `at` est refusé. Si ce fichier existe et qu'un utilisateur y est listé, cet utilisateur ne pourra pas planifier de tâches `at`.

Si `at.allow` et `at.deny` existent tous les deux, `at.allow` prend le pas. Si aucun des deux n'existe, seul le superutilisateur (root) peut planifier des tâches `at`.

#### Gestion de l'accès – résumé et récapitulatif

* Si `at.allow` existe, seuls les utilisateurs listés dans ce fichier peuvent utiliser `at`.
    
* Si `at.deny` existe mais pas `at.allow`, les utilisateurs non listés dans `at.deny` peuvent utiliser `at`.
    
* Si ni `at.allow` ni `at.deny` n'existent, par défaut, seul le superutilisateur (root) peut utiliser `at`.
    

#### Exemples de `at.allow` et `at.deny`

Disons que vous voulez restreindre l'utilisation de `at` à des utilisateurs spécifiques :

Créez un fichier `at.allow` comme ceci :

```bash
sudo touch /etc/at.allow 
sudo echo "user1" >> /etc/at.allow 
sudo echo "user2" >> /etc/at.allow
```

Cela permet uniquement à `user1` et `user2` de planifier des tâches `at`.

Alternativement, vous pouvez utiliser le fichier `at.deny` comme ceci :

```bash
sudo touch /etc/at.deny 
sudo echo "user3" >> /etc/at.deny
```

Cela refuse l'accès à `user3` pour utiliser `at`.

## Planification des tâches avec `crontab`

Cron permet aux utilisateurs de planifier des actions et commandes récurrentes à des heures, dates ou intervalles spécifiques. Ce puissant planificateur de tâches stocke toutes les informations de planification dans un fichier spécial appelé `crontab`.

### Commandes de base de crontab

* `crontab -e` : Ouvre le fichier crontab de l'utilisateur dans un éditeur pour ajouter ou modifier des tâches cron.
    
* `crontab -l` : Liste les tâches cron de l'utilisateur.
    
* `crontab -r` : Supprime toutes les tâches cron de l'utilisateur.
    

Quelques points à noter sur `crontab` :

* Chaque utilisateur peut avoir son propre `crontab`.
    
* Le démon `cron` (`crond`) doit être en cours d'exécution pour que les tâches cron s'exécutent.
    
* Utilisez toujours des chemins absolus pour les scripts et commandes dans les tâches cron.
    

### Format de `crontab`

Le fichier `crontab` a cinq champs suivis de la commande/du script à exécuter. Voici à quoi il ressemble :

```bash
* * * * * command_to_execute
- - - - -
| | | | |
| | | | +----- Jour de la semaine (0 - 7) (Dimanche est 0 ou 7)
| | | +------- Mois (1 - 12)
| | +--------- Jour du mois (1 - 31)
| +----------- Heure (0 - 23)
+------------- Minute (0 - 59)
```

Si vous avez oublié le format de `crontab`, vous pouvez toujours exécuter la commande `cat /etc/crontab` et elle affichera le format pour vous.

### Exemples d'utilisation de `crontab`

#### Exécuter un script toutes les heures

```bash
crontab -e
```

La commande ci-dessus ouvrira l'éditeur avec Vim ou un autre que vous avez configuré. Dans cet éditeur, vous écriverez la tâche basée sur le format `crontab` comme ci-dessous :

```bash
0 * * * * /path/to/script.sh
```

* `0` représente le champ des minutes. Dans ce cas, il est défini sur `0`, indiquant que la tâche cron se déclenchera lorsque la minute sera `0`, c'est-à-dire au début de chaque heure.
    
* `*` (astérisques) indique que toutes les valeurs possibles pour ce champ sont valides. Donc, `* * * * *` signifie que la tâche s'exécutera chaque minute de chaque heure, chaque jour, chaque mois et chaque jour de la semaine.
    
* En mettant tout cela ensemble, la tâche cron `0 * * * * /path/to/script.sh` signifie que le script situé à `/path/to/script.sh` s'exécutera chaque heure au début de l'heure (lorsque la minute est `0`).
    

#### Exécuter une commande à des heures spécifiques

Tout d'abord, exécutez `crontab -e`.

```bash
0 15 * * * command_to_execute
```

* `0` représente le champ des minutes. Dans ce cas, il est défini sur `0`, indiquant que la tâche cron se déclenchera au début de l'heure.
    
* `15` représente le champ des heures. Il est défini sur `15`, ce qui signifie que la tâche s'exécutera à la 15ème heure de la journée, c'est-à-dire 15h00.
    

`* * * * *` : Les astérisques désignent toutes les valeurs possibles pour chaque champ lié au temps. Dans ce cas :

* `*` pour le jour du mois et les champs du mois signifie qu'il s'applique à chaque jour de chaque mois.
    
* `*` pour le champ du jour de la semaine signifie qu'il s'applique à chaque jour de la semaine.
    
* `command_to_execute` représente la commande ou le script qui sera exécuté à l'heure spécifiée. Ce espace réservé doit être remplacé par la commande réelle que vous souhaitez exécuter à 15h00 quotidiennement.
    

#### Exécuter une tâche chaque jour de la semaine

Tout d'abord, faites `crontab -e`.

```bash
0 9 * * 1-5 command_to_execute
```

Le code ci-dessus spécifie que `command_to_execute` s'exécutera à 9h00 du lundi au vendredi. Cette tâche cron est utile pour planifier des tâches qui doivent s'exécuter uniquement les jours de la semaine à une heure spécifique.

#### Exécuter une tâche toutes les 15 minutes

Tout d'abord, faites `crontab -e`.

```bash
*/15 * * * * command_to_execute
```

Cela spécifie que `command_to_execute` s'exécutera à 0, 15, 30 et 45 minutes de chaque heure, chaque jour, chaque mois et chaque jour de la semaine. Cette tâche cron est utile pour planifier des tâches qui doivent être exécutées à intervalles réguliers, dans ce cas, toutes les 15 minutes.

### `cron.allow` et `cron.deny`

Vous utilisez ces fichiers `cron.allow` et `cron.deny` pour contrôler quels utilisateurs sont autorisés à utiliser le service `cron` pour planifier des tâches périodiques. Ces fichiers sont généralement situés dans `/etc/` dans RHEL.

Le fichier `cron.allow` spécifie la liste des utilisateurs autorisés à utiliser le service `cron` pour planifier des tâches en utilisant `crontab`. Si ce fichier existe, seuls les utilisateurs listés dans celui-ci peuvent créer des entrées `crontab`. Si le fichier n'existe pas, il se comporte comme s'il était vide, permettant à tous les utilisateurs sauf ceux restreints par `cron.deny`.

Le fichier `cron.deny` spécifie la liste des utilisateurs à qui l'accès au service `cron` est refusé. Si ce fichier existe et qu'un utilisateur y est listé, cet utilisateur ne pourra pas créer d'entrées `crontab`. Si `cron.allow` et `cron.deny` existent tous les deux, `cron.allow` prend le pas. Si aucun des deux n'existe, seul le superutilisateur (root) peut créer des entrées `crontab`.

#### Gestion de l'accès – résumé

* Si `cron.allow` existe, seuls les utilisateurs listés dans ce fichier peuvent créer des entrées `crontab`.
    
* Si `cron.deny` existe mais pas `cron.allow`, les utilisateurs non listés dans `cron.deny` peuvent créer des entrées `crontab`.
    
* Si ni `cron.allow` ni `cron.deny` n'existent, par défaut, seul le superutilisateur (root) peut créer des entrées `crontab`.
    

#### Exemple d'utilisation de `cron.allow` et `cron.deny`

Disons que vous voulez restreindre l'utilisation de `cron` à des utilisateurs spécifiques.

Créez un fichier `cron.allow` :

```bash
sudo touch /etc/cron.allow 
sudo echo "user1" >> /etc/cron.allow 
sudo echo "user2" >> /etc/cron.allow
```

Cela permet uniquement à `user1` et `user2` de créer des entrées `crontab`.

Alternativement, vous pouvez utiliser le fichier `cron.deny` :

```bash
sudo touch /etc/cron.deny 
sudo echo "user3" >> /etc/cron.deny
```

Cela refuse l'accès à `user3` pour créer des entrées `crontab`.

## Exercices pratiques

### Gestion des services avec `systemctl`

* Passez en revue le statut actuel des services système en utilisant `systemctl`.
    
* Démarrez, arrêtez, activez ou désactivez un service pour comprendre leurs fonctionnalités.
    
### Planification de tâches immédiates avec `at`

* Utilisez la commande `at` pour planifier une tâche ponctuelle immédiate (par exemple, afficher un message, exécuter une commande) à exécuter quelques minutes après l'heure actuelle.
    
* Vérifiez les permissions d'accès pour les commandes `at` en comprenant la fonctionnalité de `at.allow` et `at.deny`.
    
### Configuration de `at.allow` et `at.deny`

* Créez un fichier `at.allow` pour spécifier les utilisateurs autorisés à utiliser `at` en listant les noms d'utilisateur (s'il n'existe pas).
    
* Créez un fichier `at.deny` pour restreindre les utilisateurs d'utiliser `at` en listant les noms d'utilisateur (si nécessaire).
    
* Essayez de planifier une tâche `at` en utilisant différents comptes utilisateurs pour observer l'effet de ces fichiers.
    
### Tâches récurrentes avec `cron`

* Ouvrez le crontab en utilisant `crontab -e`.
    
* Planifiez une tâche à exécuter à une heure spécifique chaque jour ou chaque semaine en utilisant `cron`.
    
* Vérifiez les permissions d'accès pour les commandes `cron` en comprenant la fonctionnalité de `cron.allow` et `cron.deny`.
    
### Configuration de `cron.allow` et `cron.deny`

* Créez un fichier `cron.allow` pour spécifier les utilisateurs autorisés à utiliser `cron` en listant les noms d'utilisateur (s'il n'existe pas).
    
* Créez un fichier `cron.deny` pour restreindre les utilisateurs d'utiliser `cron` en listant les noms d'utilisateur (si nécessaire).
    
* Essayez de modifier ou de créer une tâche `cron` en utilisant différents comptes utilisateurs pour observer l'effet de ces fichiers.
    
### Observation et vérification

* Surveillez le statut des tâches planifiées en utilisant les commandes respectives (`atq`, `crontab -l`).
    
* Validez les restrictions d'accès et les permissions pour les commandes `at` et `cron` en observant les tentatives des utilisateurs et les refus d'accès.
    
### Nettoyage et exploration

* Supprimez ou modifiez les fichiers de contrôle d'accès (`at.allow`, `at.deny`, `cron.allow`, `cron.deny`) et observez les changements dans l'accessibilité des commandes.
    
* Explorez des commandes supplémentaires `systemctl`, `at` et `cron` pour approfondir votre compréhension de la planification des tâches et du contrôle d'accès.
    

## **Conclusion**

Merci d'avoir exploré le monde de l'administration de Red Hat Enterprise Linux (RHEL) avec moi aujourd'hui. Vous pouvez plonger plus profondément dans le domaine de l'expertise Linux et rester à l'écoute pour plus de contenu perspicace dans mes futurs tutoriels.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)