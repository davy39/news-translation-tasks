---
title: Comment compresser des fichiers en ".gz" sur le système d'exploitation Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-03-01T19:15:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-files-to-gzip-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/freeCodeCamp
seo_title: Comment compresser des fichiers en ".gz" sur le système d'exploitation
  Windows
---

Fahim.png
tags:
- name: compression
  slug: compression
- name: Windows
  slug: windows
seo_title: null
seo_desc: "Vous pouvez souvent avoir besoin de compresser des fichiers et des dossiers pour diverses raisons. Et la compression \"Gzip\" est un bon choix pour de nombreux scénarios. \nRécemment, j'ai été confronté à un problème où je devais compresser beaucoup de fichiers individuellement, et l'intervention manuelle pour compresser chaque fichier un par un en utilisant 7zip traditionnel est devenu fastidieux.\n---

Vous pouvez souvent avoir besoin de compresser des fichiers et des dossiers pour diverses raisons. Et la compression "Gzip" est un bon choix pour de nombreux scénarios. 

Récemment, j'ai été confronté à un problème où je devais compresser beaucoup de fichiers individuellement, et l'intervention manuelle pour compresser chaque fichier un par un en utilisant 7zip traditionnel est devenu fastidieux.

Si vous êtes amoureux du système d'exploitation Windows comme je le suis (je sais, je sais, parfois Windows peut devenir assez pénible. Peut-être que j'aime la douleur et aussi résoudre les problèmes tout seul, qui sait !), alors vous pourriez également rencontrer des problèmes lors du traitement par lots de la compression de plusieurs fichiers au format `.gzip`.

Il existe plusieurs façons de compresser un fichier au format `.gzip`. Le problème principal est que la plupart des méthodes ne prennent pas en charge le traitement par lots de la conversion. Dans cet article, je vais parler de deux méthodes décents que vous pouvez utiliser pour cela.

## Méthode 1 : Utilisation de 7zip (Pas de traitement par lots)

[7zip](https://www.7-zip.org/) est un logiciel gratuit disponible pour Windows, Linux et ARM64. L'installation de 7zip dans le système d'exploitation Windows est très simple et directe.

Si vous souhaitez simplement compresser un fichier unique au format `.gzip`, vous devez simplement sélectionner ce fichier et l'ajouter à l'archive 7zip. Dans l'interface graphique, vous pouvez sélectionner le format d'archive comme "gzip" et c'est tout !

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-21_12-36.png)
_gzip dans 7zip_

## Méthode 2 : Utilisation de `gzip` depuis Chocolatey (Le traitement par lots est le principal avantage de ceci)

Il existe plusieurs outils que nous pouvons utiliser pour compresser des fichiers et des dossiers sur nos ordinateurs. Cependant, les systèmes d'exploitation basés sur Linux viennent avec beaucoup d'outils et il existe de nombreux outils de type CLI (Interface de Ligne de Commande) que nous pouvons également utiliser pour compresser plusieurs fichiers ensemble en lot. 

Si vous utilisez un système d'exploitation basé sur Linux, alors vous avez peut-être également utilisé GZip. Gzip est un format de fichier et une application logicielle qui compresse et décompresse des fichiers. Il réduit également la taille des fichiers et permet des transferts réseau plus rapides. Cependant, il n'existe pas d'installateurs officiels de GZip pour le système d'exploitation Windows.

Mais, nous pouvons installer "gzip" directement sur Windows et travailler comme si nous étions dans un système d'exploitation Linux. Je préfère télécharger GZip via [Chocolatey](https://chocolatey.org/), un très bon gestionnaire de paquets pour le système d'exploitation Windows. 

> Chocolatey est un gestionnaire de paquets et un installateur de logiciels au niveau machine, en ligne de commande, pour Microsoft Windows. Il utilise l'infrastructure de packaging NuGet et Windows PowerShell pour simplifier le processus de téléchargement et d'installation de logiciels.

Si vous utilisez Chocolatey pour la première fois, alors vous devez d'abord l'installer. Toutes les méthodes sont expliquées en détail sur leur site officiel : [https://chocolatey.org/install](https://chocolatey.org/install).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-21_12-48.png)
_Installation de Chocolatey_

Ouvrez votre terminal et exécutez la commande pour installer "gzip".

```powershell
choco install gzip
```

Écrivez "Yes" lorsqu'il demande votre permission. Après quelques secondes, vous devriez être prêt à l'utiliser.

Supposons que je veux compresser en lot beaucoup de fichiers en ".gzip". Je peux ouvrir mon terminal et aller dans ce répertoire (où se trouvent mes fichiers bruts que je veux compresser en utilisant gzip) en utilisant la commande `cd path/to/where/I/have/the/files`. 

Ou, je peux simplement ouvrir mon terminal directement en utilisant le menu contextuel "Ouvrir dans le terminal" dans ce répertoire spécifique où se trouvent les fichiers que je veux compresser en utilisant gzip. Ensuite, je peux simplement utiliser la commande suivante.

```powershell
gzip * -r
```

Cela va parcourir chaque dossier et sous-dossier dans cet emplacement spécifique et compresser tous les fichiers en `.gzip` de manière récursive (le drapeau `-r`). Gardez à l'esprit que cela va **remplacer** tous vos fichiers par `.gzip` dans ce répertoire.

**Mais**, si vous souhaitez également conserver les fichiers originaux côte à côte pendant le processus de compression par lots, vous pouvez utiliser la commande suivante.

```bash
gzip * -r -k
```

Ici, le drapeau `-k` indique l'option `--keep` pour conserver les fichiers originaux.

**Si** vous souhaitez utiliser tous vos cœurs CPU en parallèle, alors suivez la commande suivante.

```bash
parallel gzip ::: *
```

Vous devez ajouter les suffixes nécessaires pour répondre à vos besoins évidemment dans ce processus.

C'est tout !

## Conclusion

J'espère que vous avez acquis quelques informations précieuses à partir de cet article.

Si vous avez apprécié les procédures étape par étape, alors n'oubliez pas de me le faire savoir sur [Twitter/X](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/). Je vous serais reconnaissant si vous pouviez m'endosser pour certaines de mes compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) si vous êtes intéressé par l'open source. Assurez-vous de vérifier [mon site web](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) également.

Merci beaucoup !