---
title: Comment apprendre le terminal Linux en tant que débutant – Conseils et exemples
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-11-07T21:25:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-linux-terminal-as-a-beginner
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/10.-Linux-basic-commands
seo_title: Comment apprendre le terminal Linux en tant que débutant – Conseils et
  exemples
---

Brief.png
tags:
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "En 2017, j'ai acheté un nouvel ordinateur portable et je suis passé à Linux. J'ai commencé avec Ubuntu (mais je suis passé à Elementary plus tard), car la plupart des gens suggéraient qu'il était adapté aux débutants. \nLes gens suggéraient également que je devrais m'habituer à utiliser le clavier et le terminal plutôt que la souris pour profiter de la puissance ultime de Linux. \nJ'ai donc commencé à apprendre diverses commandes de terminal et raccourcis clavier. Le fait que je pouvais taper assez rapidement était un bonus."
---

En 2017, j'ai acheté un nouvel ordinateur portable et je suis passé à Linux. J'ai commencé avec Ubuntu (mais je suis passé à [Elementary](https://elementary.io/) plus tard), car la plupart des gens suggéraient qu'il était adapté aux débutants. 

Les gens suggéraient également que je devrais m'habituer à utiliser le clavier et le terminal plutôt que la souris pour profiter de la puissance ultime de Linux. 

J'ai donc commencé à apprendre diverses commandes de terminal et raccourcis clavier. Le fait que je pouvais taper assez rapidement était un bonus. 

Dans cet article, je vais vous guider à travers les expériences que j'ai eues en apprenant à gérer les opérations de fichiers et de dossiers sous Linux. 

## Prérequis

Avant de commencer à utiliser le terminal, vous devez vous familiariser avec deux commandes. Elles vous seront utiles pour toutes les opérations que vous tenterez de faire. 

Ce sont les commandes `cd` et `ls`. 

* `**cd**` est une commande qui vous permet de naviguer vers un chemin ou un dossier différent dans le terminal
* `**ls**` est une commande qui vous permet de lister tous les fichiers et dossiers dans un répertoire

## Comment j'ai commencé à apprendre quelques commandes Linux de base

J'aime télécharger et lire des fichiers et des livres depuis Internet. Mais j'avais une mauvaise habitude de télécharger tous les fichiers dans le dossier `Téléchargements`. 

Un jour, j'étais pressé de rechercher un document, car je devais faire une présentation. Mais ouvrir et rechercher dans la longue liste de fichiers dans mon dossier `Téléchargements` était vraiment frustrant pour moi, car il contenait plus de 1000 fichiers. 

Je voulais trouver un raccourci pour identifier le fichier. Le seul indice que j'avais était qu'il s'agissait d'un document PDF. J'ai donc prévu de copier tous les fichiers PDF dans un autre dossier temporaire. 

### Comment copier uniquement les fichiers PDF d'un dossier à un autre

`cp` est la commande pour copier les fichiers. Heureusement, le terminal Linux supporte `regex` presque partout. Mon travail est donc devenu assez simple. Voici le code pour copier les fichiers PDF dans un autre dossier :

```bash
cp <fichier(s)_à_copier> <dossier_de_destination>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-252.png)
_Comment copier uniquement les fichiers PDF d'un dossier à un autre ?_

D'après la capture d'écran ci-dessus, vous pourriez être confus quant à la commande `mkdir Temp_PDF_Files`. Vous utilisez la commande `mkdir` pour créer un nouveau répertoire.    
  
Certains d'entre vous pourraient également être confus avec `_./_*.pdf` dans la commande `cp`. En fait, dans le monde de la programmation, nous appelons cela une **Regex**. Regex signifie **Expression Régulière**, et nous les utilisons pour filtrer des éléments en correspondant à des motifs. Dans notre cas, ce sont les fichiers se terminant par l'extension `.pdf`.

Après avoir exécuté la commande, il y avait moins de 50 fichiers PDF. J'ai pu trouver le fichier en quelques minutes. 

Comme vous pouvez le voir, il est toujours conseillé de catégoriser vos fichiers téléchargés. 

Super, j'avais terminé ma présentation. Mais je voulais que le fichier soit nommé correctement, afin de pouvoir le retrouver plus rapidement à l'avenir. 

### Comment renommer un fichier sous Linux

J'ai cherché sur Google comment faire cela, mais j'ai été surpris de voir la même réponse partout, que je trouvais incorrecte. Il s'agissait de la commande `mv`, que j'utilisais idéalement pour déplacer un fichier/répertoire d'un chemin à un autre. 

Après avoir creusé davantage, j'ai découvert que c'était la même commande `mv` pour renommer le fichier. 

```bash
mv <nom_de_fichier_existant> <nouveau_nom_de_fichier>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-253.png)
_Comment renommer un fichier sous Linux ?_

J'ai terminé de renommer le fichier. Mais je ne voulais plus du dossier temporaire que j'avais créé pour copier tous les fichiers PDF. 

### Comment supprimer un dossier complètement sous Linux (y compris ses fichiers et sous-dossiers)

Avant de me lancer dans cela, j'ai copié le fichier renommé dans un endroit sûr que je pourrais facilement me rappeler à l'avenir. J'étais un peu nerveux car j'allais supprimer tout le dossier. J'ai généralement ce sentiment chaque fois que je supprime quelque chose. 

Vous pouvez supprimer des fichiers et des dossiers avec la commande `rm -rf` que j'avais utilisée plusieurs fois auparavant. 

```bash
rm -rf <nom_de_dossier>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-254.png)
_Comment supprimer un dossier complètement sous Linux ?_

Mais soyez prudent car c'est une commande **dangereuse**. Elle ne demandera aucune confirmation avant de supprimer le dossier. Récupérer un dossier supprimé avec cette commande est presque impossible. 

## Comment créer et lire des fichiers sous Linux

Les gens ont tendance à stresser lorsqu'ils sont en retard, et c'est pire pour les réunions importantes ou les cours en ligne. Cela m'est arrivé – et cela m'a conduit à une grande expérience d'apprentissage sur la gestion des opérations de fichiers via le terminal. 

C'était un matin ensoleillé et mon cours en ligne avait déjà commencé – et j'avais deux minutes de retard. Je voulais commencer à prendre des notes, mais j'avais mis mon carnet et mon stylo quelque part la veille au soir et je ne me souvenais plus exactement où. 

La première chose qui m'est venue à l'esprit a été d'ouvrir Google Docs. Mais ce site prendrait un certain temps à charger. 

"Pourquoi ne pas créer un fichier texte sur ma machine et commencer à prendre des notes ?", c'est la question qui m'est venue à l'esprit ensuite. 

### Comment créer un fichier sous Linux

Je me souvenais qu'un de mes amis m'avait dit que vous pouvez utiliser la commande `touch` pour créer un fichier instantanément. Mais je ne l'avais pas encore essayé. J'ai donc fait :

```bash
touch notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-266.png)
_touch - Commande Linux pour créer un fichier_

Mais... Mais... Mais...  

Cette commande crée un fichier et ne l'ouvre pas en mode édition pour que vous puissiez commencer à prendre des notes. C'est là que vous pouvez utiliser votre éditeur de texte préféré pour ouvrir un fichier. 

**vim** et **nano** sont les deux éditeurs de texte bien connus disponibles sous Linux. 

**vim** est un éditeur de texte avancé et puissant que vous pouvez utiliser pour effectuer des **opérations de fichiers complexes** et c'est ce que beaucoup d'administrateurs système Linux utilisent.

**nano**, en revanche, est un éditeur de texte simple que vous pouvez utiliser pour effectuer des **opérations de fichiers simples**. 

J'utilisais nano, donc j'ai exécuté la commande `nano notes.txt`. Cela ouvre le fichier texte en mode édition instantanément. J'ai commencé à prendre des notes de la session. 

Enfin, j'ai atteint la fin du cours, mais je ne savais pas comment sauvegarder le fichier. Je n'ai pas osé essayer des commandes avant d'avoir une sauvegarde de mes notes. J'ai donc pris mon téléphone et j'ai fait une photo de mes notes. 

Après une rapide recherche sur Google, j'ai découvert que la commande était "CTRL + X" pour sauvegarder le fichier (ce qui demandera Oui / Non pour sauvegarder le fichier, et appuyer sur "Y" et presser "Enter" le sauvegardera). 

Après avoir sauvegardé le fichier, j'étais curieux de vérifier si je l'avais sauvegardé correctement. 

### Comment lire le contenu d'un fichier sous Linux

Après avoir fait une recherche sur Google, j'ai découvert qu'il existe plusieurs façons de lire un fichier. `cat`, `head` et `tail` sont quelques commandes que vous pouvez utiliser pour lire un fichier, et chacune a ses propres cas d'utilisation. 

* La commande `**cat**` affiche l'intégralité du contenu du fichier
* La commande `**head**` affiche les premières lignes du fichier, généralement utilisées pour vérifier si vous êtes sur le point d'ouvrir le bon fichier
* Et la commande `**tail**` affiche les dernières lignes du fichier, généralement utilisées pour lire les logs de n'importe quel processus.

Voici un exemple de la commande `cat` :

```bash
cat notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-268.png)
_Lecture du contenu de mon fichier de notes avec la commande **cat**_

Et voici le résultat des commandes `**head**` et `**tail**` :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-269.png)
_Résultat de la commande **head** affichant les premières lignes du fichier de notes_

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-270.png)
_Résultat de la commande **tail** affichant les dernières lignes du fichier de notes_

### Comment lire le contenu d'un fichier avec les numéros de ligne sous Linux

Un jour, un de mes collègues m'a demandé : "Hey ! Sais-tu comment afficher le contenu d'un fichier avec leurs numéros de ligne dans le terminal ?"

Je n'avais pas rencontré de commandes explicitement disponibles pour cela. Je savais que je pourrais écrire un script qui lit le fichier ligne par ligne, puis les imprime sur la console en préfixant les numéros de ligne pour chaque ligne.

Il voulait explorer cette option.

Nous avons tous les deux commencé à travailler sur ce problème. Intéressamment, au milieu, nous avons trouvé une commande simple et directe. 

Oui – je parle de la commande `nl`. Vous l'utilisez comme ceci :

```bash
nl notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-271.png)
_La commande `nl` affiche le contenu du fichier avec les numéros de ligne_

C'est incroyable, n'est-ce pas ? Comme vous pouvez le voir dans le code ci-dessus, la commande `nl` affiche le contenu du fichier avec les numéros de ligne.

## Commandes Linux que j'ai apprises de mon équipe

Mon équipe et moi avions l'habitude de nous asseoir ensemble et de travailler en groupe. Nous posions des questions sur n'importe quel sujet technique aléatoire et nous essayions d'explorer des solutions pour les problèmes qui survenaient. Je voulais donc faire un résumé rapide de certaines des choses que j'ai apprises de mes collègues ici. 

La plupart d'entre elles tournent autour de nombreuses commandes utilitaires de fichiers disponibles sous Linux dont la plupart des gens ignorent l'existence. Pendant notre temps de développement, nous rencontrons plusieurs scénarios qui ont à voir avec la gestion des fichiers. 

Mon collègue **Naras** a posé cette question : 

### Quelle est la commande pour trouver les propriétés d'un fichier ? 

Eh bien, la commande `stat` affiche les propriétés du fichier telles que le nom, la taille, les permissions, créé par l'utilisateur, la date et l'heure de création et de mise à jour, et ainsi de suite. Cela ressemble à ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-272.png)
_`stat` - Commande de terminal pour afficher les propriétés du fichier_

### Y a-t-il une commande pour trouver le nombre de mots dans un fichier ? 

C'était une question géniale de **Udhaya.** 

Oui. Mais, pas seulement des mots – vous pouvez également compter les lignes et les octets en utilisant la commande `wc`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-273.png)
_La commande `wc` affiche le nombre de lignes, de mots et d'octets d'un fichier_

Le fichier affiché ci-dessus a 23 lignes et 121 mots. Sa taille est de 809 octets. 

### Peut-on trouver le type de document avec une commande ? 

Il y a quelques semaines, j'ai rencontré une question extraordinaire de **Kumar** :

"La plupart des documents sont créés avec leur extension. Mais récemment, j'ai trouvé que certains documents PDF ne sont pas créés avec l'extension .pdf. Avons-nous une commande pour trouver le type de document ?"

Oui, nous en avons une. La commande `file` affiche le type de document, comme ceci :

```bash
file notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-275.png)
_La commande `file` affichant le type de fichier `notes.txt`_

Pour répondre à sa question, voici la preuve montrant le type de document PDF avant et après avoir supprimé l'extension du nom de fichier :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-274.png)
_La commande `file` affichant le type de fichier sans l'extension_

### Comment puis-je trouver les occurrences d'un mot dans un fichier ? 

Mon collègue **Divad** a demandé si nous pouvions trouver toutes les lignes où un mot particulier était disponible dans un fichier.

Et j'ai réalisé que cela était possible avec la commande `grep`.

Alors, qu'est-ce que `grep` ? 

`**grep**` signifie **G**lobal search for **R**egular **E**xpression and **P**rint out. C'est essentiellement un outil de recherche qui correspond à un motif Regex et les imprime. 

```bash
grep -i "Linux" notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-276.png)
_La commande `**grep**` affiche les lignes contenant **Linux** du fichier **notes.txt**_

Le drapeau `**-i**` indique d'effectuer une recherche **insensible à la casse**. Pour effectuer une recherche **sensible à la casse**, **supprimez** le drapeau `-i` de la commande. 

### Et si je veux trouver toutes les lignes qui ne contiennent pas un mot particulier ? 

**Raman** a posé la question : "Et si je veux trouver toutes les lignes qui ne contiennent pas le mot donné ?"

C'est possible en utilisant la même commande `grep` mais en appliquant l'argument `-v`, comme ceci : 

```bash
grep -v "Linux" notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-277.png)
_La commande `**grep -v**` affiche les lignes ne contenant pas le mot **Linux** du fichier **notes.txt**_

Comme vous pouvez le voir, en discutant de nos questions et en travaillant ensemble, nous avons beaucoup appris.

# Conclusion

Dans cet article, j'ai partagé mon expérience d'utilisation de Linux lorsque j'étais débutant. J'espère que vous avez apprécié la lecture de cet article. 

Vous pouvez me contacter [ici](https://www.linkedin.com/in/arunachalamb/). 

Vous pouvez me suivre sur [Instagram](https://www.instagram.com/5minslearn/), [Twitter](https://twitter.com/5minslearn), [LinkedIn](https://www.linkedin.com/in/5minslearn/) et [Medium](https://5minslearn.medium.com/).