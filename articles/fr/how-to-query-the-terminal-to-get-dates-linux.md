---
title: Commande Linux Date – Comment interroger le terminal pour obtenir des dates
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-11-19T19:06:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-query-the-terminal-to-get-dates-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/10.-Date-Command
seo_title: Commande Linux Date – Comment interroger le terminal pour obtenir des dates
---

Brief-1.png
tags:
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "Linux dispose de nombreux outils utilitaires qui vous aident à trouver rapidement la réponse à vos questions. Mais de nombreux développeurs ne les connaissent pas.\nDans cet article, vous apprendrez une commande qui présente des avantages exceptionnels. \nPar exemple, disons que vous souhaitez consulter votre calendrier pour planifier des vacances. Quelles sont les différentes façons d'ouvrir le calendrier ? Eh bien, il y a Google/Outlook, le calendrier de votre bureau système, le calendrier de votre téléphone mobile, et plus encore.\n"
---

Linux dispose de nombreux outils utilitaires qui vous aident à trouver rapidement la réponse à vos questions. Mais de nombreux développeurs ne les connaissent pas.

Dans cet article, vous apprendrez une commande qui présente des avantages exceptionnels. 

Par exemple, disons que vous souhaitez consulter votre calendrier pour planifier des vacances. Quelles sont les différentes façons d'ouvrir le calendrier ? Eh bien, il y a Google/Outlook, le calendrier de votre bureau système, le calendrier de votre téléphone mobile, et plus encore.

Mais saviez-vous que vous pouvez obtenir un calendrier simplement en tapant trois lettres ? Dans cet article, je vais vous apprendre cette commande utile de trois lettres et partager quelques expériences amusantes d'utilisation de `date` avec mon équipe. 

## Comment interroger votre terminal pour obtenir la date

Je me souviens que j'étais occupé à travailler un jour. J'ai demandé à l'un de mes collègues assis à côté de moi : "Connais-tu la date du vendredi de la semaine prochaine ?" Puis j'ai réalisé qu'il portait des écouteurs et semblait profondément concentré sur son code. 

Je ne voulais pas le déranger davantage, et j'allais demander à mon autre collègue assis juste en face de moi. 

"25 novembre", répondit le collègue que je pensais ne pas pouvoir m'entendre. 

J'étais émerveillé – comment savait-il si vite ? 

"Oh, mec ! Je pensais que tu codais. Comment as-tu obtenu la date ?" lui ai-je demandé, surpris. 

"J'interrogeais le terminal pour trouver la réponse à la question que tu m'as posée", répondit-il, montrant sa fenêtre de terminal. 

La fenêtre de terminal contenait la commande suivante :

```bash
dd "vendredi semaine prochaine"
```

Je n'ai pas compris ce qu'il avait fait, alors j'ai demandé. 

"Eh bien, Linux prend par défaut en charge la commande date pour afficher la date du jour et pour définir la date et l'heure actuelles dans notre système. Elle fournit également un moyen de trouver une date dans le futur et dans le passé aussi simplement que nous parlons. `date` est la commande pour faire tout ce qui est lié à la date et à l'heure", répondit-il. 

J'étais encore plus confus à propos de la commande `dd` et je lui ai demandé de clarifier comment elle fonctionnait.

"Mais si `date` est la commande, qu'est-ce que `dd` ? Est-ce que cela fait partie de la commande `date` ?" 

Il a expliqué que `dd` n'est pas associé à la commande `date`. En fait, c'était simplement une commande de raccourci (j'écrirai à ce sujet dans mes futurs tutoriels) qu'il avait créée. `dd` est l'abréviation de `date --date="<date_donnée>"`.

Donc, la commande réelle est celle-ci :

```bash
date --date="vendredi semaine prochaine"
```

J'ai exécuté la même commande dans mon terminal et j'ai été émerveillé de voir le résultat. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-69.png)
_Commande du terminal Linux pour trouver la date du jour donné_

C'était cool et je l'ai remercié pour son explication super utile. Après des recherches supplémentaires, j'ai découvert que cette commande pouvait répondre à la plupart de mes questions. J'avais l'impression d'interagir avec un système d'IA. 

Je poste ici quelques-unes de mes questions :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-from-2022-11-15-00-05-25.png)
_Interroger le terminal pour une date future ou passée_

## Comment obtenir des informations spécifiques sur une date dans Linux

Jusqu'à présent, nous avons essayé de trouver un jour particulier avec notre requête. Mais, que faire si vous voulez trouver des informations sur une date ? Après un peu plus de recherches, j'ai découvert que vous pouvez trouver le jour de la semaine d'une date en utilisant la même commande. 

La commande suivante affiche le jour de la semaine du 1er août 2015 :

```bash
date --date="2015-08-01"
date --date="08/01/2015"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-82.png)
_Commande du terminal pour trouver le jour d'une date_

## Comment trouver des informations sur une liste de dates dans Linux

Mon collègue avait une liste de dates. Il avait besoin d'un script qui affichait chaque date avec le jour. Il était bloqué en essayant de comprendre comment faire, et il a demandé mon aide. 

Il était clair sur son problème. Mais il s'était trompé dans les étapes qu'il avait suivies pour y parvenir. Après une discussion plus approfondie, j'ai découvert qu'il avait recherché les éléments suivants séquentiellement sur Google.

* Comment ouvrir un fichier en mode lecture ?
* Comment lire ligne par ligne ? 
* Comment analyser la date dans le fichier ? 
* Enfin, comment trouver le jour de cette date ? 

Au milieu de cette discussion, je me suis souvenu que vous pouvez faire cela rapidement avec la commande `date` super puissante. Le fait est que la commande `date` effectue toutes les actions ci-dessus – notre travail est simplement de donner le chemin du fichier. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-83.png)
_Commande du terminal pour analyser les dates d'un fichier_

Le fait qu'elle puisse lire et analyser la date donnée dans n'importe quel format est un avantage supplémentaire. À partir de la capture d'écran ci-dessus, vous serez en mesure de comprendre à quel point il est simple de résoudre le problème de mon collègue. 

En me souvenant de la citation de [Unfiltered: No Shame, No Regrets, Just Me](https://www.goodreads.com/work/quotes/53327688) par Lily Collins

> Demander de l'aide n'est jamais un signe de faiblesse. C'est l'une des choses les plus courageuses que vous puissiez faire. Et cela peut vous sauver la vie.

## Comment la commande Date fonctionne avec les opérations de fichiers

Si vous avez lu mon [tutoriel précédent sur la prise en main de Linux](https://www.freecodecamp.org/news/how-to-learn-linux-terminal-as-a-beginner/), vous vous souvenez peut-être qu'avec la commande `stat`, nous pouvons obtenir certaines informations sur le fichier telles que sa taille, la date de création, la dernière date de modification, et ainsi de suite. 

Eh bien, saviez-vous que vous pouvez trouver l'heure de la dernière modification d'un fichier en utilisant la commande `date` ? 

Oui – en ajoutant le drapeau `-r` avec la commande `date` et le chemin du fichier, vous pouvez trouver l'heure de la dernière modification du fichier. Cela ressemble à ceci :

```bash
date -r install_git.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-84.png)
_Commande du terminal montrant l'heure de la dernière modification d'un fichier_

Il y a un autre endroit où cette commande de date peut être plus familière. Vous l'utilisez pour créer un fichier avec un horodatage. Par exemple, les administrateurs système l'utilisent souvent pour voir les journaux du système et du serveur. J'ai également entendu dire que les personnes dans le trading d'actions comptent également sur la création de fichiers avec des horodatages. 

Voici un exemple rapide de création d'un fichier avec la date et l'heure :

```bash
vi file-$(date "+%Y-%m-%d_%I:%M:%S").txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-85.png)
_Commande du terminal pour créer un fichier avec la date et l'heure_

Pour les premiers utilisateurs, il peut être difficile de comprendre la commande ci-dessus. 

Décortiquons cette commande pour mieux la comprendre :

* `vi` est mon éditeur de texte
* `file-$(date "+%Y-%m-%d_%I:%M:%S").txt` est le nom du fichier

Décortiquons davantage la commande `date` dans le nom du fichier :

* `date "<un_certain_format>"` imprime la date dans le format spécifié
* `%Y` est l'année en cours
* `%m` est le mois en cours
* `%d` est la date du jour
* `%I` est les heures
* `%M` est les minutes
* `%S` est les secondes

## Comment trouver la date et l'heure dans un fuseau horaire différent

L'un de mes autres membres de l'équipe a soulevé cette question intéressante. 

Il est possible de trouver la date et l'heure dans un autre fuseau horaire avec la commande `date`. Mais ce n'est pas très convivial. Vous devez vous souvenir du nom complet du fuseau horaire pour obtenir la date et l'heure. Mais cela fonctionne directement. 

Je suis en Inde et nous suivons l'heure normale de l'Inde (IST). Je peux utiliser la commande ci-dessous pour trouver l'heure à New York. 

```bash
TZ='America/New_York' date
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-86.png)
_Commande du terminal montrant l'heure de New York_

La capture d'écran ci-dessous vous montre la comparaison de l'heure dans différents fuseaux horaires tels que Singapour, l'Amérique et l'Inde. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-87.png)
_Commande du terminal montrant l'heure dans différents fuseaux horaires_

## Quelle est la commande de trois lettres pour obtenir votre calendrier ?

Attendez-vous de connaître la commande de 3 lettres pour afficher le terminal ? 

C'est la commande `cal`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-94.png)
_Commande du terminal pour afficher le calendrier_

Voici un **conseil bonus** pour vous. 

Vous pouvez afficher le calendrier de n'importe quelle année simplement en ajoutant l'année à côté de la commande `cal`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-95.png)
_Commande du terminal montrant le calendrier de l'année 2022_

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-96.png)
_Commande du terminal montrant le calendrier de l'année 2023_

Si vous souhaitez en savoir plus sur la commande `cal`, vous pouvez me contacter sur les réseaux sociaux. 

Note : `date` et `cal` sont préinstallés dans de nombreuses distributions Linux. Si vous rencontrez l'erreur `date: command not found` lors de l'exécution de la commande `date`, vous devez simplement installer le paquet `coreutils` en exécutant la commande suivante :

```bash
sudo apt install coreutils
```

## Conclusion

Dans ce tutoriel, j'ai partagé mon expérience d'utilisation de la commande `date` dans Linux. J'espère que vous avez apprécié la lecture de cet article. 

Pour recevoir des blogs plus instructifs dans votre boîte de réception, abonnez-vous à ma newsletter [ici](https://5minslearn.gogosoon.com/).