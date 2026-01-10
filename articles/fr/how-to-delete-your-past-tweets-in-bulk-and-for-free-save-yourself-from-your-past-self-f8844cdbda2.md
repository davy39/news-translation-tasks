---
title: Comment supprimer vos anciens tweets — en masse et gratuitement — et sauver
  votre carrière de votre ancien moi
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2018-07-22T14:24:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-your-past-tweets-in-bulk-and-for-free-save-yourself-from-your-past-self-f8844cdbda2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JU7deLCU5l54IDbLwO5M2A.jpeg
tags: []
seo_title: Comment supprimer vos anciens tweets — en masse et gratuitement — et sauver
  votre carrière de votre ancien moi
seo_desc: '“He who controls the past controls the future. He who controls the present
  controls the past.” — George Orwell


  James Gunn was on top of the world. He’d just directed two of the best action-comedy
  movies of the past decade. Both of his Guardians of t...'
---

> « Celui qui **contrôle le passé contrôle le futur**. Celui qui **contrôle** le présent **contrôle le passé**. » — George Orwell

James Gunn était au sommet du monde. Il venait de réaliser deux des meilleurs films d'action-comédie de la dernière décennie. Ses deux films Guardians of the Galaxy ont été bien accueillis par les critiques et le public.

![Image](https://cdn-media-1.freecodecamp.org/images/-r3W9nzAsguP1bt89slbASRnkhBJVVm33O3Z)

Mais cela n'a pas suffi à le sauver de son ancien moi.

Il s'avère qu'au début de sa carrière, Gunn avait tweeté quelques "blagues" plutôt choquantes sur Twitter. (Je ne les partagerai pas ici — vous êtes probablement mieux sans les lire.)

À l'époque, Gunn était un réalisateur obscur de films d'horreur à petit budget. Et les tweets en question sont restés dormants pendant des années dans son historique Twitter, sans que personne ne les lise ou ne s'en soucie.

C'est-à-dire, jusqu'à ce que quelques reporters décident de déterrer des informations sur lui et exhument les tweets pour que le monde entier les voie.

Ses patrons chez Disney ont immédiatement décidé de "rompre leur relation professionnelle" avec Gunn.

Ainsi, en l'espace de quelques heures, Gunn est passé de réalisateur star à paria d'Hollywood. Tout cela à cause de quelques tweets de 2012.

### Contrôlez votre passé

Dans ce tutoriel, je vais vous montrer comment télécharger tous vos anciens tweets depuis Twitter, puis supprimer rapidement autant de ces tweets que vous le souhaitez — le tout sans partager vos données avec qui que ce soit.

Je l'ai fait moi-même il y a quelques minutes.

Bien sûr, j'aime l'idée que les futurs historiens scrutent mes tweets en se demandant : « À quoi ressemblait vraiment Quincy Larson ? » Mais pas autant que je déteste l'idée qu'un hater fouille dans mon fil Twitter et choisisse un tweet où j'avais l'air d'un imbécile.

Il existe de nombreux services que vous pouvez trouver pour supprimer vos tweets si vous leur donnez accès à votre compte Twitter (et peut-être un peu d'argent aussi).

Je ne me sentais pas à l'aise de partager l'accès à mes comptes Twitter avec l'un de ces services. En fait, créer un tel service de "suppression de tweets" m'a semblé être une idée de génie maléfique. « Oh, vous avez quelque chose à cacher, n'est-ce pas ? »

Mais nous pouvons laisser ce sale boulot aux paparazzi numériques.

À la place, ce tutoriel vous montrera comment supprimer tous vos tweets antérieurs à une certaine date vous-même — gratuitement et en masse — en utilisant un simple script Python.

Il peut sembler que chaque tweet de votre passé soit un flocon de neige spécial et unique. Si vous pensez ainsi, vous voudrez peut-être passer manuellement en revue vos anciens tweets et supprimer uniquement ceux qui vous embarrassent.

Mais si vous avez des milliers de tweets comme moi, cela va vous prendre des heures et des heures.

Notez que la suppression des anciens tweets n'affectera en rien vos abonnés Twitter, si ce n'est en supprimant des choses qu'ils sont franchement trop occupés pour aller relire. (Il y a 350 000 nouveaux tweets créés chaque minute sur Twitter. Personne n'a le temps pour ça !)

Commençons !

### Étape 1 : Comment créer une sauvegarde personnelle de tous vos tweets

La première chose à faire est de créer une sauvegarde de tous vos tweets. Twitter vous permet d'exporter facilement tous vos anciens tweets dans un fichier CSV pratique.

Rendez-vous dans la section « Vos données Twitter » des paramètres de Twitter. [Voici un lien direct](https://twitter.com/settings/your_twitter_data).

Twitter vous demandera de confirmer votre mot de passe. Ensuite, cliquez sur « demander les données » en bas de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/bTEKJOohOMH0klHEMP7z0AkJ228foEx7HE8H)

Twitter m'a envoyé un joli fichier zip en quelques minutes.

Si vous pensez que vous voudrez un jour relire les anciens tweets que vous êtes sur le point de supprimer, assurez-vous de sauvegarder ce fichier zip en lieu sûr.

Ensuite, décompressez le dossier. Voici à quoi ressemble le dossier :

![Image](https://cdn-media-1.freecodecamp.org/images/PVuZ9EvjKXsD0Mywm2MeiT8GxnsWSVAsObA6)

Vous pouvez ouvrir index.html dans un navigateur et vous verrez une belle interface utilisateur où vous pouvez faire défiler vos tweets par mois et par année.

Notez que vous aurez besoin du fichier `tweets.csv` pour la dernière étape de ce tutoriel.

### Étape 2 : Installer la bibliothèque Python

Pour cette étape, je vais supposer que vous utilisez MacOS. Si quelqu'un veut créer une liste claire d'instructions étape par étape pour Linux ou Windows, partagez-les dans un commentaire ci-dessous. Je les ajouterai ici et vous créditerai. ?

Allez dans votre ligne de commande et exécutez cette commande pour cloner le dépôt :

```
git clone git@github.com:QuincyLarson/delete-tweets.git
```

Allez dans le répertoire nouvellement créé :

```
cd delete-tweets
```

Assurez-vous d'avoir PIP (un gestionnaire de paquets Python) installé :

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Maintenant, vous pouvez installer toutes les dépendances de la bibliothèque :

```
pip install -r requirements.txt
```

Notez que vous devrez peut-être exécuter certaines de ces commandes avec « sudo » au début pour qu'elles fonctionnent correctement. Et vous pourriez obtenir des messages du type « impossible de trouver la bibliothèque xyz ». J'ai pu ignorer ces messages et cela a tout de même fonctionné.

### Étape 3 : Créer des clés API Twitter

Rendez-vous sur [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new) et remplissez le formulaire comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/a1gWcgtupB6bBxWNkZKHtSmsfKf1jIO450ps)

Vous pouvez mettre à peu près n'importe quoi ici — la seule personne qui utilisera cette application Twitter, c'est vous.

Maintenant, dans votre nouvelle application Twitter, cliquez sur « Keys and Access Tokens » puis, en bas, cliquez sur « Create my access token ».

![Image](https://cdn-media-1.freecodecamp.org/images/-A2x3QqJ6RcjUIO2jOHHp0i6ZJgWQkYqgTQ8)

Maintenant, utilisez votre éditeur de texte préféré et ouvrez `deletetweets.py`.

![Image](https://cdn-media-1.freecodecamp.org/images/1irYIAk3F7SIZUeaPRjK7oAcpDHNkScvFA1H)

Faites défiler jusqu'à la ligne 54. Vous allez copier/coller manuellement vos clés ici.

![Image](https://cdn-media-1.freecodecamp.org/images/BdmnWKyZYJwMXfno0NVbjLEUjQ5vtaqeYjZK)

Enregistrez le fichier et quittez.

### Étape 4 : Copier votre fichier tweets.csv

À l'étape 1, vous avez téléchargé une sauvegarde personnelle de tous vos anciens tweets. Copiez le fichier `tweets.csv` de ce dossier vers votre nouveau dossier delete-tweets. Il remplacera le fichier tweets.csv de remplissage.

### Étape 5 : Supprimer les tweets

Maintenant, vous devez simplement décider d'une « date de coupure » — une date avant laquelle tous vos tweets seront supprimés.

Par exemple, si cette date était le 1er octobre 2013, vous utiliseriez la commande suivante dans votre terminal :

```
python deletetweets.py -d 2013-10-01
```

Le script commencera alors par cette date et ira en ordre chronologique inverse, supprimant un tweet chaque seconde jusqu'à ce qu'il ait terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/UG4b1mVeLdcsDRrgOSZSKC1vdHXLglID3F4x)

À la fin, il vous indiquera combien de tweets il a supprimés.

Félicitations — vous avez contrôlé votre passé.

Et maintenant, vous avez une chose en moins à vous soucier pour l'avenir.

Maintenant, fermez votre terminal et continuez votre vie.

Vous devriez [me suivre sur Twitter](https://www.twitter.com/ossia) pour des trucs tech pratiques qui valent votre temps.