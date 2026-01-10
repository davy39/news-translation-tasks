---
title: 'Introduction aux alias Git : une méthode plus rapide pour travailler avec
  Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-06T20:10:40.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-git-aliases-a-faster-way-of-working-with-git-b1eda81c7747
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LmBD9OaRAJPnBYBoZwyZMw.jpeg
tags:
- name: Git
  slug: git
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Introduction aux alias Git : une méthode plus rapide pour travailler avec
  Git'
seo_desc: 'By Boudhayan Biswas

  As developers, we know Git very well, as it is a very important part of our daily
  activity. Software developers use it all the time. We can not spend a day without
  interacting with Git. We can run Git from the terminal or use some...'
---

Par Boudhayan Biswas

En tant que développeurs, nous connaissons très bien **Git**, car c'est une partie très importante de notre activité quotidienne. Les développeurs logiciels l'utilisent tout le temps. Nous ne pouvons pas passer une journée sans interagir avec Git. Nous pouvons exécuter Git à partir du terminal ou utiliser des outils tiers comme Sourcetree.

Mais il y a des fans du terminal qui adorent toujours exécuter Git uniquement à partir du terminal. Pour eux, il est parfois difficile de se souvenir et d'écrire ces longues commandes. Ohh non, mon ami !! C'est une tâche très ennuyeuse et chronophage d'écrire de longues commandes tout le temps ???.

Alors, que devrions-nous faire maintenant ???

D'accord, nous devrions commencer à chercher un raccourci pour ces longues commandes.???

Regardez ce que nous avons trouvé : **Git Alias**. Il est venu comme le sauveur pour tous.

Nous savons tous probablement ce qu'est un alias — cela signifie un **faux nom ou surnom**.

Ainsi, en utilisant **git alias**, nous pouvons attribuer un surnom à une longue commande git. C'est parfait. ?

Maintenant, essayons de trouver un endroit où nous pouvons écrire ces surnoms.

_Recherche ? Recherche ? Recherche ?_

_Oui, **_bash_profile_** est l'endroit où nous pouvons les écrire._

#### _Comment ouvrir bash_profile ?_

_À partir du terminal, nous pouvons facilement ouvrir **_bash_profile_** en utilisant la commande suivante :_

_`vim ~/.bash_profile`_

_Entrez maintenant en mode insertion dans votre **_éditeur vim_** en appuyant sur `i` du clavier. ✓_

#### _Créez votre premier alias dans bash_profile :_

_Le premier programme que nous utilisons pour écrire dans un langage de programmation est un programme **Hello World**. Ne brisons pas cette tradition — nous allons écrire notre tout premier **alias** avec une simple commande **hello**._

_Ouvrez **_bash_profile_**, et écrivez la ligne suivante :_

_`alias hello="echo Hello Boudhayan!! Comment ça va?"`_

_Cela dit que nous avons créé un **alias** nommé **hello** et attribue le côté droit comme la commande à exécuter. Ainsi, chaque fois que nous écrivons **hello** dans le terminal, il doit exécuter la commande qui lui est attribuée._

_Enregistrez les modifications et rechargez le **_bash_profile_** en utilisant la commande suivante :_

_`source ~/.bash_profile`_

_Maintenant, si nous tapons `hello` dans le terminal, il imprime `Hello Boudhayan!! Comment ça va?`_

![Image](https://cdn-media-1.freecodecamp.org/images/1*S7sKAFEQuZellxzd1G9L3w.png)

_Génial!! ???_

_Ainsi, nous avons appris comment créer une commande alias dans **_bash_profile_**._

_Si nous regardons de près, nous pouvons nous y identifier. Nous pouvons trouver quelques similitudes avec la _déclaration de variable_ dans n'importe quel langage. Oui, nous savons déjà cela, n'est-ce pas ?_

#### _Venons-en au sujet principal_

_Maintenant, créons quelques alias git pour rendre notre vie quotidienne plus facile et plus rapide. ?_

_`git clone`_

_Nous utilisons cette commande pour cloner un dépôt distant vers un système local._

_Bien que ce soit une commande courte, nous voulons commencer à apprendre les alias git en la rendant encore plus courte. ?_

_Comme ci-dessus, ouvrez bash_profile, écrivez la ligne ci-dessous et rechargez **_bash_profile_**. Voyez la magie. ☀️_

_`alias gc="git clone"`_

_Désormais, pour cloner un dépôt, nous n'avons plus besoin d'écrire ceci :_

_`git clone <url du dépôt distant>`_

_au lieu de cela, nous utiliserons la commande suivante pour le clonage :_

_`gc <url du dépôt distant>`_

_Boum!! Votre dépôt distant est cloné avec succès dans votre système local. ???_

#### _Créez quelques alias supplémentaires_

_Nous poussons nos commits locaux vers la branche de développement ou master en utilisant les commandes suivantes :_

_`git push origin develop`  
`git push origin master`_

_Maintenant, nous pouvons écrire une version plus courte comme ci-dessous :_

_`alias gpd="git push origin develop"`  
`alias gpm="git push origin master"`_

_Désormais, nous utiliserons gpd et gpm pour pousser les commits locaux vers les branches de développement et master respectivement._

_?????? Hourra!! Nous l'avons fait. ??????_

_J'ai créé quelques alias git supplémentaires qui peuvent être vraiment utiles dans notre vie de programmation. Découvrez-les :_

#### _Fonction Shell :_

_Nous pouvons également utiliser la **fonction shell** pour déclarer des alias git plus complexes. Mais pour commencer avec cela, nous devons savoir comment écrire une fonction shell. ?_

_Il est très facile d'écrire une **fonction shell** qui ressemble à une fonction **C** normale. ?_

```
function function_name() {         
  command1         
  command2         
  .......         
  commandn
}
```

_Essayons cela maintenant. Cette fonction créera un répertoire dans le chemin courant et se déplacera immédiatement dans ce répertoire. Nous connaissons déjà les commandes suivantes pour que cela se produise :_

_`mkdir <nom_du_répertoire>`  
`cd <nom_du_répertoire>`_

_Nous pouvons compresser ces deux commandes en créant une simple fonction dans **_bash_profile_** comme ci-dessous :_

_`function mdm() {`  
   `mkdir -p $1   #ici $1 est le premier paramètre de la fonction.`  
   `cd $1`  
`}`_

_Maintenant, rechargez la source **_bash_profile_** une fois et exécutez ce qui suit :_

_`mdm test`_

_Cela créera un répertoire nommé **test** dans le chemin courant et se déplacera dans ce répertoire. Cool!! ?_

#### _Alias Git avancés_

_Pour pousser le code dans la branche distante, nous devons faire un commit avec un message. Seulement alors nous pouvons pousser vers une branche. Donc, en gros, c'est une combinaison de deux commandes (commit et push). Mais nous voulons essayer la même chose avec une seule commande en une ligne en écrivant une fonction shell pour cela. ?_

_Nous pouvons facilement faire cela en écrivant une simple fonction shell. Ouvrez **_bash_profile_** et écrivez la fonction suivante :_

_`function gcp() {`  
      `git commit -am "$1" && git push`  
`}`_

_Rechargez le **_bash_profile_** une fois et utilisez la commande comme suit :_

_`gcp "initial commit"`_

_Cool!! Désormais, nous pouvons utiliser cette commande **gcp** pour commiter et pousser en une seule fois. ?_

_Dans une branche de développement ou de fonctionnalité, tous les membres de l'équipe poussent leurs changements presque tous les jours. Parfois, il est donc très difficile de trouver un commit particulier parmi tous les commits._

_Pour gérer facilement ce type de situation, nous pouvons écrire une fonction qui recherchera les logs de commit pour un message particulier et retournera le commit._

_Pour ce faire, nous allons écrire une fonction comme suit :_

_`function gfc() {`  
         `git log --all --grep="$1"`  
`}`_

_Occasionnellement, si nous voulons rechercher un commit par le message de commit, nous pouvons le faire en utilisant `gfc` :_

_`gfc "<message_du_commit>"`_

#### _Conclusion :_

_Ainsi, nous avons appris comment utiliser des raccourcis pour les commandes git._

_Que ces alias et fonctions vous évitent d'écrire ces longues commandes git et rendent votre vie facile et fluide. Vous pouvez ajouter vos propres alias, fonctions et apporter des modifications — aucune permission n'est requise sauf celle de **_bash_**. ???_

_**??? Santé!!! Merci d'avoir lu!! ???**_