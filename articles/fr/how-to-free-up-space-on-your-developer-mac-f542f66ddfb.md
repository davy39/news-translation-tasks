---
title: Comment libérer de l'espace sur votre Mac de développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T16:36:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-free-up-space-on-your-developer-mac-f542f66ddfb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iNNdLGh5TORjiWIHp5l0Ng.png
tags:
- name: Git
  slug: git
- name: JavaScript
  slug: javascript
- name: mac
  slug: mac
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment libérer de l'espace sur votre Mac de développeur
seo_desc: "By Gant Laborde\nClean up your dev environment you filthy animal!\nI love\
  \ cleaning software? PLZ! Remove duplicates, find old OS cruft etc. But it never\
  \ cleans a development machine as I can. \nSure, for general maintenance, nothing\
  \ beats CleanMyMac. Bu..."
---

Par Gant Laborde

#### Nettoyez votre environnement de développement, espèce d'animal malpropre !

J'adore les logiciels de nettoyage ? SVP ! Supprimez les doublons, trouvez les vieux fichiers du système d'exploitation, etc. Mais aucun ne nettoie une machine de développement aussi bien que moi. 

Bien sûr, pour l'entretien général, rien ne vaut [CleanMyMac](https://macpaw.com/cleanmymac). Mais une fois par an, les développeurs devraient exécuter quelques commandes manuelles, car les nettoyeurs automatiques ne sauront pas comment prendre soin d'une machine de développeur.

Avant de commencer, voyons combien d'espace libre vous avez au départ :

![Image](https://cdn-media-1.freecodecamp.org/images/y4j1aRSyr4UvT8Ns14UgTww17s6D7Ndr7wu1)

Le mien indique 132,2 Go avant le nettoyage. C'est parti !

### Utilisateurs de Homebrew sur Mac

Celui-ci permet généralement d'économiser des centaines de mégaoctets de données. Mettez à jour, améliorez, puis nettoyez ces fichiers que vous n'allez pas utiliser.

**Mettez à jour puis supprimez les anciennes formules et leurs dossiers :**

```
brew update && brew upgrade && brew cleanup
```

Vous avez peut-être utilisé `brew prune` par le passé, mais cela a été abandonné. Cleanup s'en charge pour vous !

#### Maintenance générale de Brew

Brew est un système complexe, et personne ne le connaît mieux que les mainteneurs. Vous pouvez donc exécuter `brew doctor` et obtenir quelques tâches supplémentaires à effectuer pour qu'il fonctionne correctement.

### Utilisateurs de Git

Git est génial, mais il est facile de laisser traîner un tas de branches fusionnées sur votre machine locale ! Ces branches ne sont plus utiles et peuvent parfois causer des conflits de nommage pour les futures branches.

**Vous pouvez supprimer toutes les branches fusionnées d'un seul projet avec cette commande :**

```
git branch --merged master | grep -v "\* master" | xargs -n 1 git branch -d
```

WOW, quelle bouche pleine pour un seul projet ! Rendons les choses pires. ?

**Ce code va se déplacer dans tous les dossiers du répertoire de travail actuel, puis exécuter la commande pour nettoyer les branches fusionnées pour chacun !**

```
for d in */; do cd $d; echo WORKING ON $d; git branch --merged master | grep -v "\* master" | xargs -n 1 git branch -d; cd ..; done
```

### Développeurs JavaScript

#### Supprimer les anciens `node_modules` intégrés dans les projets

La commande suivante trouve tous les dossiers `node_modules` plus anciens que 120 jours et les supprime. Cela signifie que vous devrez à nouveau exécuter `npm i` ou `yarn` dans ces anciens projets. _C'est généralement un énorme nettoyage !_

**Supprime tous les dossiers `node_modules` plus anciens que 4 mois :**

```
find . -name "node_modules" -type d -mtime +120 | xargs rm -rf
```

Si vous vous sentez particulièrement agressif, vous pouvez simplement supprimer TOUS les dossiers `node_modules` et réinstaller au besoin, en supprimant le drapeau `mtime`.

**Supprime tous les dossiers `node_modules` :**

```
find . -name "node_modules" -type d | xargs rm -rf
```

#### Supprimer les anciennes versions de Node

Supprimez les anciennes versions de Node. Cela varie en fonction de votre gestionnaire de Node. J'utilise 'n', donc c'est facile pour moi. Consultez la désinstallation pour votre gestionnaire de version spécifique.

> **Utilisez-vous `n` ?**

> Listez toutes les versions de Node + celles installées avec `n ls`, puis supprimez celles que vous souhaitez avec `n rm <version>`.

> **Utilisez-vous `nvm` ?**

> Listez vos versions installées avec `nvm ls`, puis supprimez celles que vous souhaitez avec `nvm uninstall <version>`.

> **Utilisez-vous `asdf` ?**

> Listez vos versions installées avec `asdf list nodejs`, puis supprimez celles que vous souhaitez avec `asdf uninstall nodejs <version>`.

### Développeurs Ruby

Nettoyez les anciennes versions de Gems avec la commande `cleanup`. Si vous êtes inquiet, vous pouvez voir les résultats d'abord avec "dryrun".

```
gem cleanup --dryrun
```

Ensuite, lorsque vous êtes confiant, vous pouvez supprimer le paramètre "dryrun" et l'exécuter pour de vrai.

```
gem cleanup
```

#### Supprimer les anciennes versions de Ruby

Cela dépend spécifiquement de votre gestionnaire de versions de Ruby. Nous allons couvrir deux versions populaires pour vous aider.

> **Utilisez-vous `rbenv` ?**

> Listez vos versions installées avec `rbenv versions`, puis supprimez celles que vous souhaitez avec `rbenv uninstall <version>`.

> **Utilisez-vous `rvm` ?**

> Listez vos versions installées avec `rvm list`, puis supprimez celles que vous souhaitez avec `rvm uninstall <version>`.

### Développeurs Xcode

Xcode adore mettre en cache des choses partout sur votre machine, et certaines d'entre elles font des centaines de mégaoctets. Il est temps de les nettoyer, et si vous devez les reconstruire, pas de problème !

**Nettoyer les caches de CocoaPods :**

```
rm -rf "${HOME}/Library/Caches/CocoaPods"
```

**Supprimer les anciens simulateurs Xcode :**

```
xcrun simctl delete unavailable
```

**Nettoyer divers archives, logs et dossiers de données dérivées :**

```
rm -rf ~/Library/Developer/Xcode/Archives
rm -rf ~/Library/Developer/Xcode/DerivedData
rm -rf ~/Library/Developer/Xcode/iOS Device Logs/
```

Consultez les informations sur vos appareils connectés dans `~/Library/Developer/Xcode/iOS Device Logs/` et supprimez tout ce qui concerne les anciens appareils iOS que vous avez connectés.

### Docker

Vous pouvez supprimer tous les volumes non utilisés par au moins un conteneur. Parce que... pourquoi voudriez-vous les garder ?!

Cela peut être énorme ou cela peut ne rien supprimer. Cela vaut le coup d'essayer, non ?

**Supprimer les volumes locaux inutilisés**

```
docker volume prune
```

### RÉSULTATS ?!

N'oubliez pas de vider votre corbeille et de vérifier ce que nous avons accompli !

![Image](https://cdn-media-1.freecodecamp.org/images/eVUvMYYTdZvKkHcbItSd-cR3ZSEmWoydQHz8)

> 30 GO ! récupérés sur ma machine ! Et vous ?

Votre succès est probablement très différent, mais j'adorerais le savoir. Commentez ou [tweetez-moi](https://twitter.com/GantLaborde?lang=en) vos résultats, ainsi que d'autres endroits de développeur que vous recommandez de nettoyer ! Je serai ravi d'ajouter vos conseils à l'article.

---

[Gant Laborde](https://www.freecodecamp.org/news/how-to-free-up-space-on-your-developer-mac-f542f66ddfb/undefined) est le Chief Technology Strategist chez [Infinite Red](http://infinite.red), auteur publié, professeur adjoint, conférencier international et un scientifique fou en formation. Applaudissez/suivez/[tweetez](https://twitter.com/GantLaborde) ou rendez-lui visite [lors d'une conférence](http://gantlaborde.com/).

[**5 Choses qui ne vont pas avec le travail à distance**](https://shift.infinite.red/5-things-that-suck-about-remote-work-506b98dd38f9)  
[_Les pièges du travail à distance + solutions proposées_shift.infinite.red](https://shift.infinite.red/5-things-that-suck-about-remote-work-506b98dd38f9)[**React Native vs. Native**](https://shift.infinite.red/react-native-vs-native-ccac6f05346a)  
[_Dois-je apprendre React Native ou Native?_shift.infinite.red](https://shift.infinite.red/react-native-vs-native-ccac6f05346a)