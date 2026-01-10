---
title: 'L''épidémie de nouveau coronavirus en Chine : comment aider les chercheurs
  en utilisant l''alignement de séquences sur le 2019-nCoV avec MAFFT'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T11:04:41.000Z'
originalURL: https://freecodecamp.org/news/china-novel-coronavirus-epidemic-sequence-alignment-2019-ncov-mafft
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/image-64-1.png
tags:
- name: mafft
  slug: mafft
- name: Genetics
  slug: genetics
- name: Python
  slug: python
seo_title: 'L''épidémie de nouveau coronavirus en Chine : comment aider les chercheurs
  en utilisant l''alignement de séquences sur le 2019-nCoV avec MAFFT'
seo_desc: 'By Shen Huang

  Novel Coronavirus (2019-nCoV) is a deadly virus that seems to have originated in
  Wuhan, China. As of January 26, the virus has already caused 76 deaths.

  As a coronavirus targeting human respiratory systems, 2019-nCoV is highly infectiou...'
---

Par Shen Huang

Le nouveau coronavirus (2019-nCoV) est un virus mortel qui semble avoir pris naissance à Wuhan, en Chine. Au 26 janvier, le virus a déjà causé 76 décès.

En tant que coronavirus ciblant les systèmes respiratoires humains, le 2019-nCoV est hautement infectieux – surtout pendant les saisons humides et froides.

Lorsque les gens éternuent, ils peuvent projeter des pathogènes liés au système respiratoire à grande vitesse. Ceux-ci peuvent infecter les humains de nombreuses manières – le plus souvent en touchant la bouche, le nez et les yeux.

Pour éviter les infections, vous devriez éviter les activités en extérieur – surtout dans les zones bondées. Il est également important de désinfecter vos mains souvent et de ne pas vous frotter les yeux avec vos mains.

Je suis en Chine, et mes plans pour le Nouvel An lunaire sont maintenant ruinés. J'ai donc décidé de rester à la maison et de créer ce tutoriel sur la façon d'obtenir des données de séquence génétique du 2019-nCoV et de réaliser un alignement de séquences avec MAFFT.

J'espère que cet article éveillera votre intérêt pour la recherche en bioinformatique, afin que vous puissiez aider les scientifiques à lutter contre ces épidémies virales.

## Qu'est-ce que l'alignement de séquences ? Et qu'est-ce que MAFFT ?

**L'alignement de séquences** est une méthode d'arrangement de l'ADN, de l'ARN ou des protéines pour identifier des régions de similarité qui peuvent révéler des relations fonctionnelles, structurelles ou évolutives entre les séquences. Une publication récente a suggéré une transmission inter-espèces du serpent à l'homme à l'aide de l'alignement de séquences via MAFFT.

**MAFFT** (**M**ultiple **A**lignment using **F**ast **F**ourier **T**ransform) est un programme d'alignement multiple de séquences publié en 2002. Vous pouvez l'utiliser pour effectuer l'alignement de séquences pour les séquences d'ARN. Les **coronavirus** sont, par exemple, des virus avec un ARN simple brin enveloppé dans une coque dérivée des membranes cellulaires de l'hôte.

## Où pouvez-vous obtenir des données de séquence d'ARN ?

La dernière mise à jour du 2019-nCoV peut être trouvée sur [NGDC](https://bigd.big.ac.cn/ncov#about) (National Genomics Data Center of China). Dans ce tutoriel, nous allons analyser le virus [2019-nCoV](https://www.ncbi.nlm.nih.gov/nuccore/MN938384) et le virus [SARS-CoV](https://www.ncbi.nlm.nih.gov/nuccore/MK062184) trouvés dans la banque de données du NCBI (National Center for Biotechnology Information).

Le SARS-CoV, infamement connu sous le nom de SARS (Syndrome Respiratoire Aigu Sévère), a causé 774 décès dans 17 pays rapportés autour de l'année 2020.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-65.png)
_Exemple de données de séquence d'ARN de [NCBI](https://www.ncbi.nlm.nih.gov/)_

J'ai copié et collé les données dans un fichier avec le nom du virus. Cela devrait ressembler à quelque chose comme les données dans la capture d'écran ci-dessus, avec un numéro d'index suivi de codes en lots de 10, pour un total de 60 codes par ligne, séparés par des espaces.

## Comment effectuer un alignement de séquences sur le 2019-nCoV avec MAFFT

Tout d'abord, vous devez installer MAFFT. Vous pouvez l'installer via Anaconda avec les commandes suivantes.

L'installation manuelle pour différents systèmes d'exploitation peut être trouvée sur le [site officiel de MAFFT](https://mafft.cbrc.jp/alignment/software/).

```bash
conda install mafft
```

MAFFT est assez facile à utiliser, mais il traite les données dans un format spécial. Vous devrez pré-traiter vos données obtenues afin qu'elles puissent être alignées par MAFFT.

Voici le script Python qui fait cela :

```python
import sys
import re
output = ""
for filename in sys.argv[1:]:
	infile = open(filename)
	data = infile.read()
	data = " ".join(re.split("[^atcg\n]", data))
	data = data.replace(" ", "")
	output = output + ">" + filename + "\n" + data + "\n"
print(output)
outfile = open('SEQUENCES.txt', 'w+')
outfile.write(output)
```

Vous pouvez enregistrer le code Python ci-dessus dans un fichier appelé "preprocess.py", dans le même dossier que mes données d'ARN de virus. Ensuite, nous pouvons exécuter la commande bash suivante dans le dossier pour pré-traiter les données.

```bash
python3 preprocess.py 2019-nCoV_HKU-SZ-002a_2020 icSARS-C7-MA
```

Le fichier de sortie appelé "SEQUENCES.txt" devrait maintenant ressembler à quelque chose comme ci-dessous. Le nom du virus est ajouté en haut du fichier. Les espaces blancs et les numéros d'index sont également supprimés.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-66.png)

Maintenant, vous pouvez effectuer l'alignement de séquences avec MAFFT dans votre terminal avec les étapes suivantes :

1. Localisez votre dossier de travail.
2. Appelez "mafft" dans votre terminal.
3. Pour le fichier d'entrée, mettez "SEQUENCES.txt".
4. Pour le fichier de sortie, mettez "output.txt".
5. Sélectionnez "1" pour "Clustal format" comme format de sortie.
6. Sélectionnez "1" pour "auto" comme stratégie.
7. Laissez tous les autres arguments vides.

Voici un gif de moi en train d'exécuter cela dans mon terminal :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Jan-27-2020-18-46-10.gif)

Après avoir appuyé sur Entrée, vous n'avez plus qu'à attendre que MAFFT aligne vos codes d'ARN.

Le produit fini devrait ressembler à quelque chose comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-67.png)

Notez que le "-" est utilisé pour décaler les codes et "*" est utilisé pour mettre en évidence les similitudes entre les séquences.

Félicitations, vous venez d'apprendre à effectuer un alignement de séquences avec MAFFT ! Maintenant, vous pouvez jouer avec le code génétique et tirer parti des informations d'alignement comme vous le souhaitez.

Aidez Wuhan à lutter contre la maladie mortelle en tant que développeur, scientifique des données et plus :

[https://github.com/wuhan2020/wuhan2020](https://github.com/wuhan2020/wuhan2020)

Un peu plus sur moi : je suis un développeur qui s'intéresse à toutes sortes de choses. J'ai écrit d'autres tutoriels amusants comme ceux-ci :

[Comment créer de belles LANTERNES qui S'ORGANISENT en mots](https://www.freecodecamp.org/news/ghost/#/editor/post/5ceb787ee17b4228e0185dbf/)

[Comment laisser tomber des CHAPEAUX DE LEPRECHAUN dans votre site web avec la VISION PAR ORDINATEUR](https://www.freecodecamp.org/news/ghost/#/editor/post/5ceb767ee17b4228e01833b7/)

Vous voulez que j'écrive un tutoriel sur quelque chose ? Faites-le moi savoir. Bon codage.