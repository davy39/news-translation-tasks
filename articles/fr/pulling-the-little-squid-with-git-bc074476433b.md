---
title: Tirer le petit calmar avec Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:46:17.000Z'
originalURL: https://freecodecamp.org/news/pulling-the-little-squid-with-git-bc074476433b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XTKufkr__czE7CF_VUGIMw.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Tirer le petit calmar avec Git
seo_desc: 'By Iago Rodrigues

  Have you ever changed something directly in your project’s repository? Have you
  ever merged a branch into master? Then wanted to pull the changes to your local
  repository and had some trouble with it?

  If you don’t know what the mean...'
---

Par Iago Rodrigues

Avez-vous déjà changé quelque chose directement dans le dépôt de votre projet ? Avez-vous déjà fusionné une branche dans master ? Ensuite, vous avez voulu tirer les changements vers votre dépôt local et vous avez eu quelques problèmes avec cela ?

Si vous ne savez pas ce que signifie « tirer un dépôt », vous êtes au bon endroit. Voulez-vous une tasse de café ?

### Une brève introduction

Dans cet article, nous allons couvrir les différents événements qui peuvent se produire lorsque vous tirez des commits qui sont en avance sur vos commits locaux.

Par « en avance sur les vôtres », je veux dire des commits qui existent sur votre dépôt distant (celui sur les serveurs GitHub). Ces commits n'existent pas sur votre dépôt local (celui sur votre machine).

Alors, prenons un café chaud — je vous en ai offert un — et essayons de comprendre ces choses.

Pour l'apprentissage, créons un dépôt sur GitHub sans aucun fichier ajouté — nous couvrirons cela plus tard. Vous pouvez le nommer comme vous voulez.

Maintenant, nous pouvons aller dans un répertoire de notre machine pour cloner notre projet. Si nous n'avons pas encore créé un répertoire qui sert de Hub, nous pouvons en créer un afin de pouvoir stocker nos projets de GitHub. Choisissez pair ou impair pour décider.

Si vous ne savez pas de quoi je parle, veuillez consulter [cet article](https://medium.freecodecamp.org/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba).

Maintenant, examinons les événements qui peuvent se produire lorsque nous devons faire `git pull`.

### Tirer lorsque nous n'avons pas de changements locaux

C'est la situation la plus facile. Cela se produit lorsque nous avons créé le dépôt distant et ajouté des fichiers que nous n'avons pas encore localement. Nous n'avons pas non plus de changements sur notre dépôt local.

D'accord. D'abord, allons dans le dossier créé lorsque nous avons cloné le projet. Il a le même nom.

Il est temps de créer quelques fichiers sur GitHub. Sur la page de notre projet, créez un fichier README. Facile !

Sur notre ordinateur, ouvrons l'invite de commande ou une application de terminal (comme cmder) et tapons `git pull origin master`. Vous verrez la magie opérer.

![Image](https://cdn-media-1.freecodecamp.org/images/2K5RaCUk7rZolYY8Z5z7-VBl6DytGbqtLuEP)
_Tirer sans changements locaux._

Maintenant, nous avons aussi ces changements localement. Plutôt cool, n'est-ce pas ?

### Tirer lorsque nous avons des changements locaux qui n'ont pas encore été validés

Super. Créons quelques fichiers. Vous pouvez ouvrir le dossier de votre projet local dans votre éditeur de code préféré. Je recommande d'utiliser [VSCode](https://code.visualstudio.com/).

Avec cela, créez un fichier `.gitignore` et ajoutez-y quelques éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/Ae6zrXTktQT2jwd9bk5uk6jQcoyviB19-pMK)
_Création d'un fichier .gitignore local._

Maintenant, nous avons des changements locaux, mais nous n'avons pas validé ces changements. Nous ne allons pas le faire tout de suite.

Allons dans notre dépôt distant. Créez un autre fichier là-bas. Il peut s'agir d'un LICENSE.md. Faites comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/tLr1vGeHXPAAU1YhnrfrbbCUYNHcQTIvxXnZ)

1. Tapez LICENSE dans le champ de saisie.
2. Cliquez sur **choisir un modèle de licence**.

![Image](https://cdn-media-1.freecodecamp.org/images/junhzv57ioV9K7TsQYdWsPK3IUfuuEgBtOOU)
_Création d'un fichier LICENSE._

Sur la page suivante, choisissez **MIT License** et cliquez sur **Review and Submit**. N'hésitez pas à lire la licence si vous le souhaitez.

Votre fichier devrait maintenant ressembler à celui de l'image, avec votre nom GitHub, bien sûr.

Maintenant, nous pouvons valider cela. Descendez la page et cliquez sur **Commit new file**. Assurez-vous que la première option est sélectionnée.

![Image](https://cdn-media-1.freecodecamp.org/images/TDjiHa9txi1YZbmhgXpGPdnZJhmWT4barFmy)

Vous pouvez laisser les champs vides (il utilise le même texte que le texte de l'espace réservé) ou taper autre chose si vous le souhaitez.

Jusqu'à présent, nous avons modifié à la fois à distance et localement. Cependant, nous n'avons pas validé nos changements locaux. Laissez cela tel quel.

Tirons les changements et voyons ce qui se passe ?

![Image](https://cdn-media-1.freecodecamp.org/images/SbqBazR5L5rsFxeoZfsSfW8dDt1J4kSUeQto)
_Tirer les changements distants lorsque nous avons également des changements locaux non validés._

Cool ! Nous avons pu tirer sans problèmes. Cela se produit parce que nous avons modifié des fichiers différents. Plus loin, nous verrons ce qui se passe lorsque nous modifions le même fichier. Accrochez-vous !

### Tirer lorsque nous avons des commits locaux qui n'ont pas encore été poussés

D'accord. Maintenant, validons ces changements locaux. Si vous tapez `git status`, vous verrez que nous avons un fichier **non suivi**. Cela signifie que nous n'avons pas ajouté le fichier et que Git ne le suit pas.

Alors, ajoutons et validons le fichier. Ne faites pas `git push` tout de suite !

![Image](https://cdn-media-1.freecodecamp.org/images/JTqpt9wiBl0BzhvGHpxpJjcDqryVL91pi5pu)
_Validation des changements locaux._

Ajoutons un autre changement au dépôt distant et validons-le également. Il pourrait s'agir d'un fichier `index.html`.

Si vous tapez `git status`, vous verrez que notre dépôt local et distant a divergé. Ils ont tous les deux 1 (un) commit différent.

![Image](https://cdn-media-1.freecodecamp.org/images/DYuIo8wyl6fHY6aXeazKsTOAZEjoxKuE-mKi)
_Commits divergents sur les deux dépôts._

Essayons de tirer ces changements maintenant et voyons le statut.

![Image](https://cdn-media-1.freecodecamp.org/images/7qjDaxbt-gO1P64uK6u22WbNzPJDqWwH5rHg)

Regardez cela ! Git a tiré les changements de manière récursive sur le dépôt distant et les a fusionnés automatiquement dans notre pile de commits locaux. Nous sommes donc en sécurité pour tirer les changements de cette manière également.

#### Que se passe-t-il si nous avons des changements sur le même fichier ?

Bien. Nous avons vu que lorsque nous modifions des fichiers différents, nous pouvons utiliser `git pull` sans problèmes.

Cependant, que se passe-t-il lorsque nous modifions le même fichier sur les deux dépôts ?

Avant de continuer, nous devrions faire `git push origin master` sur les modifications locales que nous avons faites précédemment. De cette façon, nous n'avons aucune modification, et nous sommes égaux avec le dépôt distant.

Nous pouvons maintenant modifier quelque chose. Disons, modifier le fichier README localement et valider les changements. Ne le poussez pas encore.

Allez dans le fichier README distant et modifiez-le également. Validez-le.

Nous sommes dans la même situation qu'avant, avec un commit différent de chaque côté.

Si vous essayez de faire `git pull` sur le dépôt distant, voici ce que nous voyons :

![Image](https://cdn-media-1.freecodecamp.org/images/U7PCDo4Uidp1O3u9F2KuGKMjJRQhqrQ3Ki2A)
_Tirer des commits divergents sur le même fichier._

![Image](https://cdn-media-1.freecodecamp.org/images/ZfMX05KfWzblDyI6oyxL62D9vCrARsuwIG9H)

Git essaiera de fusionner les changements automatiquement, mais comme nous avons des changements différents sur le même fichier, cela échoue.

Nous devons fusionner les commits distants dans nos commits locaux manuellement, afin de pouvoir continuer notre travail.

Tout d'abord, nous devons corriger les conflits dans le fichier. Si vous utilisez VSCode, nous pouvons aller dans l'onglet **Contrôle de code source** et gérer cela là-bas.

![Image](https://cdn-media-1.freecodecamp.org/images/L67xfS6-UYxx-xujc4PMyXRZ-vBgOcwnhi-r)
_Gestion des conflits dans VSCode_

C'est très simple ici. **Accepter les changements actuels** signifie que nous acceptons uniquement les changements distants. **Accepter les changements entrants** signifie que nous acceptons uniquement nos changements locaux. Nous pouvons également accepter les deux changements avec l'option **accepter les deux changements**.

Avec cela, nous pouvons ajouter et valider le fichier. Si nous vérifions le statut maintenant, nous voyons que nous avons 2 commits d'avance sur le dépôt distant. Cela signifie que nous avons fusionné avec succès le fichier.

Nous pouvons maintenant le pousser et vérifier le fichier modifié sur GitHub.

Ouf ! Eh ! Celui-ci nous a donné un peu de travail. Mais ce n'est pas de la science-fiction, n'est-ce pas ?

Louez le soleil ☀️ mon ami. Maintenant, nous allons travailler.

### Que faire si nous avons déjà un projet à envoyer sur GitHub et un dépôt distant avec des fichiers ?

D'accord ! C'est une longue question. Mais c'est une question importante. C'est une autre situation à laquelle nous devons nous intéresser.

Disons que nous avons installé un modèle avec du code. Un [modèle](https://github.com/vuejs-templates) dans le monde du développement est un ensemble de code pré-écrit que nous pouvons utiliser pour démarrer notre projet et le modeler à notre façon.

Donc, maintenant nous avons un répertoire avec du code, et nous allons faire `git init` ce dossier afin que Git commence à écouter nos changements.

Cool. Maintenant, nous voulons envoyer ce projet sur GitHub. Plutôt simple, n'est-ce pas ? Il suffit de créer un dépôt distant. Mais, disons que nous avons créé ce dépôt et que nous avons ajouté un readme, une licence, un index.html et un fichier .gitignore.

Hmmm … nous n'avons pas fait attention que notre modèle a déjà mis ces mêmes fichiers dans notre dépôt local.

Donc, si nous essayons de tirer, nous avons le même problème qu'avant — des changements différents des deux côtés.

Pour l'article, disons que nous allons tirer ces changements de toute façon. Mais avant de gérer cela, nous devons lier notre projet local à celui sur GitHub.

Exécutez le code suivant : `git remote add origin <lien du projet GitHub>`

Le **lien du projet GitHub** est le même que celui que nous utilisons pour cloner le dépôt. Si vous ne savez pas ce que c'est, veuillez lire [cet article](https://medium.freecodecamp.org/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba?source=activity---post_recommended).

D'accord. Maintenant que nous avons fait cela, nous pouvons commencer à tirer et pousser des fichiers. Mais si nous essayons de tirer les changements maintenant, vous savez ce qui se passe, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/IeVwSPmPniKFqoHv7aHFAoK-eEgjETo4q8XJ)

C'est assez simple à contourner. Il suffit d'ajouter et de valider nos changements locaux. Comme il s'agit de notre premier commit local, nous pouvons faire ceci :

```
git add --all
git commit -m "first commit"
```

Avec cela, nous pouvons essayer de tirer à nouveau. Gardez à l'esprit que nous devons utiliser `git pull origin master` car c'est le premier pull que nous faisons sur ce dépôt.

Nous devrions obtenir le message suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/bGp82lzUrVEMiaLMwt1Yjz0n7spkVxkEMsj4)

Nous ne pouvons pas tirer les changements, car Git ne veut pas. ? ? Super ! Merci, Git !!! ?

Pour résoudre cela, nous devons fusionner les fichiers. Mais nous avons une méthode beaucoup plus efficace. Exécutez le code `git rebase origin/master`.

Nous recevons le message suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/OewthvVVeubJFduxbdTnBVdMesvgpdtOI5Rl)
_Exécution de git rebase._

Le rebase est assez génial. C'est une meilleure alternative à `git merge`. Il fait la même chose mais de manière plus efficace. Vous pouvez en savoir plus à ce sujet [ici](https://git-scm.com/book/pt-br/v1/Ramifica%C3%A7%C3%A3o-Branching-no-Git-Rebasing), mais ne vous inquiétez pas trop. Dans les articles suivants, je l'expliquerai.

Nous devons résoudre les conflits maintenant. Nous pouvons aller dans VSCode pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/EOztFE2j4VPI9rA9dQNLSQ3gNVQLVTvacR4a)

Faites attention à quelques choses ici.

Tout d'abord, les fichiers qui ont des conflits sont ceux sous l'onglet **modifications de fusion**.

Deuxièmement, lorsque nous avons exécuté `git rebase`, il a ajouté à nouveau tous nos fichiers à la phase de staging — la même étape où nous nous trouvons après avoir exécuté `git add` — mais ceux avec des conflits.

Troisièmement, dans la barre inférieure gauche de VSCode, nous pouvons voir une série de nombres. Eh bien, **git rebase** a créé cette branche. Ne vous inquiétez pas, cependant. Nous reviendrons à la **master** dans un instant.

D'accord. Maintenant que nous avons résolu les conflits, nous pouvons ajouter les fichiers. Si vous voulez éviter les conflits, vous pouvez supprimer les fichiers, mais je ne pense pas que ce soit une bonne façon de résoudre cela. Sauf si vous n'en avez pas besoin.

Nous pouvons ajouter plus d'un fichier avec cette commande : `git add .gitignore index.html README.md`.

Après cela, nous allons rebase les commits distants avec nos commits locaux. Nous pouvons accomplir cela avec la commande `git rebase --continue`.

![Image](https://cdn-media-1.freecodecamp.org/images/uti5MpL2fURrhCUGKJMk7Vh1M3Jv3vcUWORN)
_Ajout des conflits résolus et rebase des commits._

Maintenant, tous les commits sur le dépôt distant sont fusionnés ou rebasés avec nos commits locaux. Nous sommes également de retour sur la branche master.

Nous pouvons vérifier les commits avec `git log`.

![Image](https://cdn-media-1.freecodecamp.org/images/afoDMA6PHO8X8obLUbYpTeE87IE38f8syi15)
_Vérification du journal avec tous les commits rebasés._

Plutôt cool, n'est-ce pas ? Ce sont les événements que nous pouvons rencontrer lorsque nous tirons des changements de dépôts distants sur GitHub.

Eh bien, c'est tout pour l'instant, les gars. J'espère que cet article vous a aidé d'une manière ou d'une autre.

Je prévois de faire une série d'articles pour les débutants concernant Git et GitHub. Alors restez à l'écoute pour plus.

À la prochaine. Paix ! ✌️ ✌️ ✌️

Je suis Iago Rodrigues, Brésilien de Belém, Pará. Je suis étudiant en systèmes d'information, stagiaire en développement logiciel et freelance. Je suis au début de ma carrière et je voulais simplement partager avec vous quelques connaissances que j'ai acquises.

Vous pouvez me suivre sur les réseaux sociaux. Toujours un plaisir d'aider là où je peux.

[**Iago Rodrigues - Estágio Analista de Software - W3 Automação e Sistemas | LinkedIn**](https://www.linkedin.com/in/iago-rodrigues/)  
[_View Iago Rodrigues' profile on LinkedIn, the world's largest professional community. Iago has 3 jobs listed on their…_www.linkedin.com](https://www.linkedin.com/in/iago-rodrigues/)[**Iago Rodrigues (@iagokv) | Twitter**](https://twitter.com/iagokv)  
[_The latest Tweets from Iago Rodrigues (@iagokv). Front-End Developer | Vue.js padawan | Noob on life. Belém, Brasil_twitter.com](https://twitter.com/iagokv)

Oui ! Je sais. Ma photo Twitter est quelque chose …