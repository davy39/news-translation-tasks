---
title: Comment installer Python sur Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-02-18T16:14:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-python-in-windows-operating-system
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Artboard-1-1.jpg
tags:
- name: Python
  slug: python
- name: Windows
  slug: windows
seo_title: Comment installer Python sur Windows
seo_desc: 'Before trying to run any Python program in your Windows operating system,
  you''ll need to check if you have Python installed and added to the environment''s
  path variable correctly.

  In this article, I will show you how you can check whether you have Py...'
---

Avant d'essayer d'exécuter un programme Python sur votre système d'exploitation Windows, vous devrez vérifier si Python est installé et correctement ajouté à la variable de chemin de l'environnement.

Dans cet article, je vais vous montrer comment vérifier si Python est installé avec succès dans votre système d'exploitation ou non. Si ce n'est pas le cas, je vous montrerai également comment l'installer correctement pour Windows.

Dans cet article, je vais utiliser Windows 11 car c'est la dernière version de Microsoft Windows. Mais la même méthode est également applicable pour les autres versions de Windows. Alors sans plus tarder, commençons.

## Comment vérifier si vous avez Python installé dans votre système d'exploitation Windows

Ouvrez l'**CMD** ou **PowerShell** et vérifiez la version de Python en utilisant cette commande :

```powershell
python --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-150253.png)

Si vous obtenez la version de Python dans la sortie comme vous le voyez ci-dessus, alors votre ordinateur est parfaitement prêt pour exécuter n'importe quel programme Python. Dans votre cas, la version de Python peut être différente.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/2022-02-18-11-45-00.00_00_34_07.Still001.jpg)

Mais si vous obtenez ce type de sortie que vous voyez ci-dessus, cela peut signifier l'une des choses suivantes :

1. Vous n'avez pas Python installé sur votre ordinateur, ou
2. Le répertoire de Python n'a pas été ajouté au chemin des **Variables d'Environnement**.

Pour l'instant, supposons que vous n'avez pas Python installé sur votre ordinateur. Ensuite, je vous montrerai également comment ajouter le répertoire de Python au chemin des Variables d'Environnement plus tard dans cet article.

## Comment installer Python sur Windows

Tout d'abord, nous devons nous rendre sur le [site officiel de Python](https://www.python.org/).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-150905.png)

Cliquez sur la section **Téléchargements**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-151036.png)

Ici, vous obtiendrez la dernière version. Cliquez simplement sur Télécharger `Python 3.10.2`. Au moment où vous lisez cet article, Python a peut-être été mis à jour, auquel cas la version serait différente. Téléchargez simplement la version qui vous est proposée.

Gardez à l'esprit que la dernière version de Python sera toujours affichée en haut.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-151239.png)

Après avoir téléchargé le fichier, nous obtiendrons un fichier exécutable comme celui-ci. Double-cliquez simplement sur ce fichier et l'assistant d'installation s'ouvrira.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/06.png)

Cliquez sur `Personnaliser l'installation`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/07.png)

Assurez-vous de cocher toutes les cases, comme ci-dessus. Ensuite, cliquez sur `Suivant`.

Vous verrez ensuite l'écran ci-dessous. Si vous le souhaitez, vous pouvez cocher toutes les cases. Je n'ai pas besoin des symboles de débogage et des binaires de débogage. Je ne vais donc pas cocher les deux dernières cases.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/08.png)

Je vous recommande également de ne pas changer l'emplacement de l'installation. Rappelez-vous l'emplacement d'installation car vous pourriez en avoir besoin plus tard. Nous ajoutons Python aux variables d'environnement directement ici.

Ensuite, cliquez sur `Installer`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/09.png)

Laissez le processus d'installation se terminer...

![Image](https://www.freecodecamp.org/news/content/images/2022/02/09--1-.png)

Si vous obtenez cette invite pour désactiver la limite de longueur du chemin, cliquez simplement sur cette case. Cela désactive la limite de longueur du chemin en supprimant la limitation sur la variable MAX_PATH.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Fahim-article-image.png)

Ce changement ne cassera rien ni ne provoquera de modifications négatives. Il permettra simplement à Python d'utiliser des noms de chemin longs. Il est recommandé de désactiver la limite de longueur du chemin.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/11-2.png)

L'installation a été terminée avec succès.

## Comment vérifier la version de Python

Maintenant, nous devons vérifier à nouveau si Python a été installé avec succès et ajouté au chemin des variables d'environnement ou non.

Pour cela, nous devons ouvrir l'**CMD** ou le **PowerShell**. Ensuite, nous devons appliquer la commande suivante :

```powershell
python --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-152724.png)

Python a été installé et le chemin a également été ajouté dans les variables d'environnement avec succès !

## Comment vérifier le chemin des variables d'environnement

Si vous souhaitez vérifier les variables de chemin manuellement, vous devez ouvrir les `Paramètres système avancés`. Vous pouvez soit rechercher `Paramètres système avancés`, soit l'ouvrir depuis le **Panneau de configuration**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-152934.png)

Si vous recherchez en utilisant le mot-clé `Paramètres système avancés`, vous l'obtiendrez directement ici comme ceci.

Si vous souhaitez l'ouvrir depuis le **Panneau de configuration**, alors, tout d'abord, vous devez ouvrir le panneau de configuration.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153056.png)

Allez dans `Système et sécurité`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153217.png)

Cliquez sur `Système`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153311.png)

À partir de ici, cliquez sur `Paramètres système avancés`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153400.png)

Cliquez sur `Variables d'environnement`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153439.png)

Cliquez sur `Path` puis cliquez sur `Modifier`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153531.png)

Vous verrez que le répertoire racine de **Python310** et le **répertoire des scripts** de Python310 ont déjà été ajoutés lors du processus d'installation, comme nous avons coché la case pour le faire pendant l'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-18-153614.png)

Si vous vouliez le faire manuellement, vous devriez copier et coller les deux répertoires ici en cliquant sur `Nouveau` et en collant les deux répertoires dans deux cases vides (une case apparaît chaque fois que vous cliquez sur `Nouveau`). Ensuite, cliquez simplement sur `OK` pour toutes les cases ouvertes et fermez toutes les fenêtres ouvertes.

J'ai également réalisé une vidéo où je montre tous les processus mentionnés ci-dessus. Si vous le souhaitez, vous pouvez regarder la vidéo [ici](https://youtu.be/whywQfFdBmo).

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA).

Vous pouvez également [VOUS ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !