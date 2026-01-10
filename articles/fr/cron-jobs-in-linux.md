---
title: Comment automatiser des tâches avec des cron jobs sous Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-11-19T20:34:59.000Z'
originalURL: https://freecodecamp.org/news/cron-jobs-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Cron-jobs-Linux--1-.png
tags:
- name: automation
  slug: automation
- name: Linux
  slug: linux
seo_title: Comment automatiser des tâches avec des cron jobs sous Linux
seo_desc: "If you're working in IT, you might need to schedule various repetitive\
  \ tasks as part of your automation processes. \nFor example, you could schedule\
  \ a particular job to periodically execute at specific times of the day. This is\
  \ helpful for performing ..."
---

Si vous travaillez dans le domaine de l'informatique, vous pourriez avoir besoin de planifier diverses tâches répétitives dans le cadre de vos processus d'automatisation. 

Par exemple, vous pourriez planifier un travail particulier pour qu'il s'exécute périodiquement à des heures spécifiques de la journée. Cela est utile pour effectuer des sauvegardes quotidiennes, l'archivage mensuel des journaux, la suppression hebdomadaire de fichiers pour libérer de l'espace, et ainsi de suite.

Et si vous utilisez Linux comme système d'exploitation, vous utiliserez quelque chose appelé une tâche cron pour que cela se produise.

## Qu'est-ce qu'un cron ?

Cron est un utilitaire de planification de tâches présent dans les systèmes de type Unix. Le démon crond active la fonctionnalité cron et s'exécute en arrière-plan. Cron lit les **crontab** (tables cron) pour exécuter des scripts prédéfinis.

En utilisant une syntaxe spécifique, vous pouvez configurer une tâche cron pour planifier des scripts ou d'autres commandes à exécuter automatiquement.

Pour les utilisateurs individuels, le service cron vérifie le fichier suivant : **/var/spool/cron**/crontabs 

![Contenu de /var/spool/cron/crontabs ](https://www.freecodecamp.org/news/content/images/2021/11/image-53.png)
_Contenu de /var/spool/cron/crontabs_

### Qu'est-ce que les cron jobs sous Linux ?

Toute tâche que vous planifiez via crons est appelée une tâche cron. Les tâches cron nous aident à automatiser nos tâches routinières, qu'elles soient horaires, quotidiennes, mensuelles ou annuelles.

Maintenant, voyons comment fonctionnent les tâches cron.

## Comment contrôler l'accès aux crons

Pour utiliser les tâches cron, un administrateur doit autoriser les tâches cron à être ajoutées pour les utilisateurs dans le fichier '/etc/cron.allow'. 

Si vous obtenez une invite comme celle-ci, cela signifie que vous n'avez pas la permission d'utiliser cron.

![Ajout de tâche cron refusé pour l'utilisateur John.](https://www.freecodecamp.org/news/content/images/2021/11/image-51.png)
_Ajout de tâche cron refusé pour l'utilisateur John._

Pour permettre à John d'utiliser les crons, incluez son nom dans '/etc/cron.allow'. Cela permettra à John de créer et de modifier des tâches cron.

![Autorisation de John dans le fichier cron.allow](https://www.freecodecamp.org/news/content/images/2021/11/image-52.png)
_Autorisation de John dans le fichier cron.allow_

Les utilisateurs peuvent également se voir refuser l'accès aux tâches cron en entrant leurs noms d'utilisateur dans le fichier '/etc/cron.d/cron.deny'.

## Comment ajouter des cron jobs sous Linux

Tout d'abord, pour utiliser les tâches cron, vous devrez vérifier l'état du service cron. Si cron n'est pas installé, vous pouvez facilement le télécharger via le gestionnaire de paquets. Utilisez simplement ceci pour vérifier :

```bash
# Vérifier le service cron sur le système Linux
sudo systemctl status cron.service
```

### Syntaxe des cron jobs

Les crontabs utilisent les drapeaux suivants pour ajouter et lister les tâches cron.

* `**crontab -e**` : édite les entrées crontab pour ajouter, supprimer ou modifier des tâches cron.
* `**crontab -l**` : liste toutes les tâches cron pour l'utilisateur actuel.
* `**crontab -u username -l**` : liste les crons d'un autre utilisateur.
* `**crontab -u username -e**` : édite les crons d'un autre utilisateur.

Lorsque vous listez les crons, vous verrez quelque chose comme ceci :

```bash
# Exemple de tâche cron
* * * * * sh /path/to/script.sh
```

Dans l'exemple ci-dessus,

* * *  * * * représente respectivement minute(s) heure(s) jour(s) mois(s) jour(s) de la semaine.

<table>
<thead>
<tr>
<th></th>
<th>Valeur</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minutes</td>
<td>0-59</td>
<td>La commande serait exécutée à la minute spécifique.</td>
</tr>
<tr>
<td>Heures</td>
<td>0-23</td>
<td>La commande serait exécutée à l'heure spécifique.</td>
</tr>
<tr>
<td>Jours</td>
<td>1-31</td>
<td>Les commandes seraient exécutées ces jours du mois.</td>
</tr>
<tr>
<td>Mois</td>
<td>1-12</td>
<td>Le mois dans lequel les tâches doivent être exécutées.</td>
</tr>
<tr>
<td>Jours de la semaine</td>
<td>0-6</td>
<td>Jours de la semaine où les commandes s'exécuteraient. Ici, 0 est dimanche.</td>
</tr>
</tbody>
</table>

* `sh` représente que le script est un script bash et doit être exécuté depuis `/bin/bash`.
* `/path/to/script.sh` spécifie le chemin vers le script.

Voici le résumé de la syntaxe des tâches cron.

```bash
*   *   *   *   *  sh /path/to/script/script.sh
|   |   |   |   |              |
|   |   |   |   |      Commande ou Script à Exécuter        
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   | Jour de la Semaine(0-6)
|   |   |   |
|   |   | Mois de l'Année(1-12)
|   |   |
|   | Jour du Mois(1-31)  
|   |
| Heure(0-23)  
|
Min(0-59)
```

## Exemples de cron jobs

Voici quelques exemples de planification de tâches cron.

<table>
<thead>
<tr>
<th>Planification</th>
<th>Valeur planifiée</th>
</tr>
</thead>
<tbody>
<tr>
<td>5 0 * 8 *</td>
<td>À 00:05 en août.</td>
</tr>
<tr>
<td>5 4 * * 6</td>
<td>À 04:05 le samedi.</td>
</tr>
<tr>
<td>0 22 * * 1-5</td>
<td>À 22:00 chaque jour de la semaine du lundi au vendredi.</td>
</tr>
</tbody>
</table>

Ce n'est pas grave si vous ne pouvez pas tout comprendre d'un coup. Vous pouvez vous entraîner et générer des planifications cron avec [crontab guru](https://crontab.guru/).

### Comment configurer une tâche cron

Dans cette section, nous allons voir un exemple de la façon de planifier un script simple avec une tâche cron.

1. Créez un script appelé `date-script.sh` qui imprime la date et l'heure du système et les ajoute à un fichier. Le script est montré ci-dessous :

![Script pour imprimer la date.](https://www.freecodecamp.org/news/content/images/2021/11/image-67.png)
_Script pour imprimer la date._

2.  Rendez le script exécutable en lui donnant des droits d'exécution.

```bash
chmod 775 date-script.sh
```

3.  Ajoutez le script dans le crontab en utilisant `crontab -e`.

Ici, nous l'avons planifié pour qu'il s'exécute chaque minute.

![Ajout d'une tâche cron dans crontab chaque minute.](https://www.freecodecamp.org/news/content/images/2021/11/image-68.png)
_Ajout d'une tâche cron dans crontab chaque minute._

4.  Vérifiez la sortie du fichier `date-out.txt`. Selon le script, la date du système devrait être imprimée dans ce fichier chaque minute.

![Sortie de notre tâche cron.](https://www.freecodecamp.org/news/content/images/2021/11/image-65.png)
_Sortie de notre tâche cron._

## Comment dépanner les crons

Les crons sont vraiment utiles, mais ils ne fonctionnent pas toujours comme prévu. Heureusement, il existe des méthodes efficaces que vous pouvez utiliser pour les dépanner. 

1. **Vérifiez la planification.**

Tout d'abord, vous pouvez essayer de vérifier la planification qui est définie pour le cron. Vous pouvez le faire avec la syntaxe que vous avez vue dans les sections ci-dessus.

2. **Vérifiez les journaux cron.**

Tout d'abord, vous devez vérifier si le cron a été exécuté à l'heure prévue ou non. Vous pouvez vérifier cela à partir des journaux cron situés à `var/log/cron`. Dans certaines distributions, les journaux peuvent être trouvés à `/var/log/syslog`

S'il y a une entrée dans ces journaux à l'heure correcte, cela signifie que le cron a été exécuté selon la planification que vous avez définie.

Voici les journaux de notre exemple de tâche cron. Notez la première colonne qui montre l'horodatage. Le chemin du script est également mentionné à la fin de la ligne.

![Journaux des tâches cron](https://www.freecodecamp.org/news/content/images/2021/11/image-69.png)
_Journaux des tâches cron._

**3. Redirigez la sortie cron vers un fichier.**

Vous pouvez rediriger la sortie d'un cron vers un fichier et vérifier le fichier pour d'éventuelles erreurs.

```bash
# Rediriger la sortie cron vers un fichier
* * * * * sh /path/to/script.sh &> log_file.log
```

## Conclusion

Automatiser des tâches, comme avec les tâches cron, réduit le travail répétitif que vous devez faire. Cela permet également aux machines de s'auto-réparer et de travailler en continu sans intervention humaine. 

L'automatisation sous Linux repose fortement sur les tâches cron, vous devriez donc définitivement apprendre les crons et expérimenter avec eux.

Merci d'avoir lu jusqu'à la fin. Les commentaires sont toujours les bienvenus.

Si vous avez trouvé cet article utile, partagez-le avec vos amis.

Restons en contact sur [Twitter](https://twitter.com/hira_zaira)!