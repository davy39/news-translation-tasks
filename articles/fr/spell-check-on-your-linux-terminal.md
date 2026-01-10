---
title: Comment utiliser la vérification orthographique sur votre terminal Linux
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-20T16:17:10.000Z'
originalURL: https://freecodecamp.org/news/spell-check-on-your-linux-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/BB
seo_title: Comment utiliser la vérification orthographique sur votre terminal Linux
---

Spell-Check-in-Linux-Terminal.png
étiquettes:
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "Saviez-vous que vous pouvez utiliser le terminal pour vérifier l'orthographe d'un passage que vous avez écrit ? Le terminal dispose de nombreuses commandes utilitaires, mais la plupart des gens ignorent beaucoup d'entre elles. J'ai vu des gens utiliser Microsoft Word ou Google pour vérifier l'orthographe d'un mot..."
---

Saviez-vous que vous pouvez utiliser le terminal pour vérifier l'orthographe d'un passage que vous avez écrit ?

Le terminal dispose de nombreuses commandes utilitaires, mais la plupart des gens ignorent beaucoup d'entre elles.

J'ai vu des gens utiliser Microsoft Word ou Google pour vérifier l'orthographe d'un mot. Mais cette commande utilitaire est un outil pratique pour les développeurs afin de vérifier leur orthographe. Le fait qu'elle soit préinstallée avec le terminal est un avantage supplémentaire.

## Comment utiliser la commande de vérification orthographique sous Linux

`ispell` et `aspell` sont les 2 commandes que vous pouvez utiliser pour vérifier l'orthographe d'un mot. Parmi ces 2, `ispell` est l'ancien correcteur orthographique de GNU qui a une capacité limitée à lire différents types de fichiers encodés.

`aspell` est un correcteur orthographique interactif qui vérifie l'orthographe via l'entrée standard ou en lisant le fichier. Il vérifie l'orthographe des fichiers encodés en UTF-8. Il peut également lire et vérifier l'orthographe des fichiers markdown.

`aspell` dispose de nombreuses options. L'exécution de `--help` avec la commande affiche la liste de toutes les options disponibles.

```bash
aspell --help
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-146.png)
_Sortie de la commande `aspell --help`_

Si vous rencontrez des erreurs lors de l'exécution de la commande ci-dessus, cela signifie que vous ne l'avez pas installée. Exécutez la commande suivante pour installer `aspell` sur votre machine :

```bash
sudo apt install aspell
```

## Comment vérifier l'orthographe des mots un par un de manière interactive ?

Passez le drapeau `-a` avec la commande `aspell` pour l'ouvrir en mode interactif.

```bash
aspell -a
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-147.png)
_Commande `aspell -a` pour ouvrir `aspell` en mode interactif_

Dans ce mode, vous pouvez entrer les mots avec une orthographe éventuellement incorrecte un par un et vous obtiendrez une liste de mots avec l'orthographe correcte qui sont les plus proches du mot saisi.

Voici un exemple de capture d'écran :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-156.png)
_Suggestions de mots corrects de la commande `aspell`_

D'après la capture d'écran ci-dessus, vous pouvez voir que `aspell` suggère plusieurs mots pour chaque mot mal orthographié que j'ai saisi.

Les alternatives proches pour le mot `sampee` sont `sample`, `simper`, `sampler`. De même, vous pouvez voir les suggestions pour d'autres mots également (waier, calendrr, moble, bqttle).

Cela peut être assez pratique pour les développeurs, car ils peuvent rapidement passer au terminal et trouver l'orthographe correcte d'un mot pendant leur développement. Le fait qu'il ne nécessite pas Internet est un avantage supplémentaire.

## Comment vérifier l'orthographe des mots à partir d'un fichier

Utiliser le terminal pour vérifier l'orthographe des mots à partir d'un fichier est la meilleure approche alternative si vous n'avez pas accès à Internet. Grammarly et Google Docs vous assisteront au mieux avec une bonne connexion Internet.

Vous pouvez écrire le passage dans un fichier texte et passer le chemin du fichier comme argument au drapeau `-c` dans la commande `aspell`. Cela accepte également un fichier HTML ou Markdown.

```bash
aspell -c <nom_du_fichier>
```

J'ai créé un fichier nommé `computer.txt` et ajouté le contenu suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-157.png)
_Contenu du fichier `computer.txt`_

J'ai fait quelques fautes d'orthographe au milieu. Vous pourriez être en mesure de les repérer facilement. Certaines d'entre elles sont macine au lieu de machine, intrenet au lieu de internet, etc.

Demandons à `aspell` de trouver les fautes d'orthographe dans ce passage.

```bash
aspell -c computer.txt
```

Une fois que vous exécutez la commande ci-dessus, vous verrez un écran similaire à la capture d'écran suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-158.png)
_Commande `aspell` pour trouver les fautes d'orthographe dans un fichier_

Cela signifie que `aspell` a détecté quelques fautes d'orthographe dans notre passage. Il mettra en surbrillance les mots mal orthographiés un par un avec les alternatives correctement orthographiées appropriées en bas.

Il y aura 10 options affichées avec un numéro de ligne. Vous pouvez choisir le mot correctement orthographié en entrant le numéro de ligne correspondant.

Par exemple, dans la capture d'écran ci-dessus, le mot "macine" est mis en surbrillance et le bon remplacement pour ce mot mal orthographié est "machine", qui est la 1ère option. Donc, j'appuie sur 1.

Immédiatement après avoir appuyé sur 1, la correction a été effectuée et aspell passe au mot suivant mal orthographié.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-159.png)
_La commande `aspell` corrige et passe au mot suivant mal orthographié dans le fichier_

En plus des 10 options, `aspell` montre 8 options différentes. Vous pouvez choisir l'une d'entre elles si vous n'avez pas trouvé le bon mot parmi les 10 options alternatives ci-dessus.

Comprenons chaque option que vous pouvez utiliser avec `aspell` :

<table><tbody><tr><td><strong>Caractère</strong></td><td><strong>Action</strong></td><td><strong>Description</strong></td></tr><tr><td>i</td><td>Ignorer</td><td>Ignorer cette occurrence et passer au mot suivant mal orthographié</td></tr><tr><td>r</td><td>Remplacer</td><td>Remplacer ce mot en entrant manuellement un nouveau mot</td></tr><tr><td>a</td><td>Ajouter</td><td>Ajouter ce mot au dictionnaire</td></tr><tr><td>b</td><td>Abandonner</td><td>Abandonner cette opération (les modifications que vous avez appliquées ne seront pas enregistrées)</td></tr><tr><td>I</td><td>Ignorer tout</td><td>Ignorer toutes les occurrences de ce mot</td></tr><tr><td>R</td><td>Remplacer tout</td><td>Remplacer toutes les occurrences de ce mot en entrant manuellement un nouveau mot</td></tr><tr><td>l</td><td>Ajouter en minuscules</td><td>Ajouter le mot au dictionnaire</td></tr><tr><td>x</td><td>Quitter</td><td>Quitter l'opération (les modifications que vous avez appliquées seront enregistrées)</td></tr></tbody></table>

Le tableau ci-dessus décrit l'action pour chaque caractère dans la commande `aspell check`.

Une fois que vous avez terminé la correction de l'orthographe de tous les mots mal orthographiés, le fichier sera automatiquement enregistré par `aspell`.

En plus de cela, un nouveau fichier sera créé avec le nom **<nom_du_fichier_existant>.bak**, qui est une sauvegarde du même fichier sans appliquer la vérification orthographique.

## Comment ignorer la création d'un nouveau fichier lors de la correction de l'orthographe dans un fichier

Cela est assez simple et peut être facilement réalisé en passant un drapeau avec la commande `aspell`. Le drapeau est `--dont-backup`.

Regardons un exemple de commande :

```bash
aspell check --dont-backup computer.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-160.png)
_Ignorer la création d'un fichier de sauvegarde en passant le drapeau `--dont-backup`_

D'après la capture d'écran ci-dessus, vous pouvez voir que j'ai supprimé le fichier `computer.txt.bak` existant et exécuté la vérification orthographique en passant le drapeau `--dont-backup`. Aucun nouveau fichier `.bak` n'a été créé après que j'ai terminé la vérification orthographique.

Vous pouvez également remarquer un autre changement par rapport à l'exemple précédent et à la commande ci-dessus. Il s'agit de `check` et `-c`. Dans ma commande précédente, j'ai utilisé `-c`, mais dans la commande ci-dessus, j'ai utilisé `check` pour passer le nom du fichier.

Vous pouvez utiliser soit `-c` soit `check` pour passer le nom du fichier. Les deux font le même travail.

## Peut-on vérifier l'orthographe sur d'autres fichiers ?

Absolument oui. `aspell` vérifie l'orthographe en lisant les fichiers Markdown et HTML également. Vous devez passer le mode du fichier comme argument séparé ( `--mode` ).

Voici la syntaxe,

```bash
aspell check --mode=<type_de_mode> nom_du_fichier
```

Les modes pris en charge sont `none`, `url`, `email`, `markdown`, `html`, `tex`, `texinfo`, et `nroff`.

Regardons un exemple rapide de correction des fautes d'orthographe dans un fichier markdown.

```bash
aspell check --dont-backup --mode=markdown spellcheck.md
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-161.png)
_Exécution de `aspell` avec le fichier markdown_

Il a ouvert une interface similaire, mais il a compris le format markdown et a mis en surbrillance uniquement le mot mal orthographié.

Je veux attirer votre attention sur un point important. Vous pouvez trouver un mot mal orthographié (blok) au milieu du bloc de backticks (``` ... ```). Le contenu à l'intérieur de ce bloc ne sera pas évalué par la commande aspell. Vous ne pourrez donc pas repérer et corriger les mots mal orthographiés à l'intérieur du bloc.

De même, vous pouvez évaluer l'orthographe dans les fichiers HTML en changeant le mode en html.

## Conclusion

Dans cet article, vous avez appris à vérifier l'orthographe en utilisant votre terminal Linux. J'espère que vous avez apprécié sa lecture.

Abonnez-vous à ma newsletter en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_spell_check) et consultez également la liste consolidée de tous mes blogs.