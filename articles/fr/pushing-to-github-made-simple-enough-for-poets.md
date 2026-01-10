---
title: Pousser vers Github - rendu assez simple pour les Poètes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/pushing-to-github-made-simple-enough-for-poets
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca19c740569d1a4ca4f9d.jpg
tags:
- name: Git
  slug: git
- name: Inspiration
  slug: inspiration
- name: learning to code
  slug: learning-to-code
seo_title: Pousser vers Github - rendu assez simple pour les Poètes
seo_desc: 'By Usheninte Dangana

  When I started actively pushing content to Github, I did not push Open Source contributions,
  Components or anything of the like - I pushed poetry. I did this, because it is
  what I love the most, after coding. I remain ever gratef...'
---

Par Usheninte Dangana

Quand j'ai commencé à pousser activement du contenu vers Github, je n'ai pas poussé des contributions Open Source, des Composants ou quoi que ce soit de similaire - j'ai poussé de la poésie. Je l'ai fait, parce que c'est ce que j'aime le plus, après le codage. Je reste éternellement reconnaissante d'avoir pris l'initiative de faire mon premier `git commit`.

Maintenant, je veux décomposer le processus pour les nouveaux codeurs (et les poètes - espérons-le 😊), afin qu'ils puissent devenir à l'aise avec le travail sur Github aussi. Je vais décomposer plusieurs façons de pousser du contenu vers Github. Pour les besoins de cet article, je vais supposer que les lecteurs sont familiers avec l'utilisation du Terminal (GitBash ou autre).

---

### Pousser vers un nouveau dépôt avec un fichier README

Il y a juste quelques étapes essentielles à cela :

* Cliquez sur le bouton vert Clone or download sur la page du dépôt.  
![Git Clone](http://res.cloudinary.com/poetrique/image/upload/v1535965331/allbuy-i-ng/gallery/git-clone.png)

* Utilisez l'option Clone with HTTPS, et copiez le lien fourni.
![Git Clone 2](http://res.cloudinary.com/poetrique/image/upload/v1535965671/allbuy-i-ng/gallery/git-clone2.png)

* Exécutez `git clone https://github.com/UserProfile/repository.git` dans le terminal. Ici, **_UserProfile_** et **_repository_** seront remplacés par les valeurs fournies dans le lien copié.
* Exécutez `git init` dans le terminal. Cela initialisera le dossier/dépôt que vous avez sur votre système informatique local.
* Exécutez `git add .` dans le terminal. Cela suivra les changements apportés au dossier sur votre système, depuis le dernier commit. Si c'est la première fois que vous commitez le contenu du dossier, cela ajoutera tout.
* Exécutez `git commit -m"insérer Message ici"`. Cela préparera les changements ajoutés/suivis du dossier sur votre système pour les pousser vers Github. Ici, **_insérer Message ici_** peut être remplacé par n'importe quel message de commit pertinent de votre choix.
* Exécutez `git push origin master`. Notez que le dernier mot dans la commande **_master_**, n'est pas une entrée fixe lors de l'exécution de `git push`. Il peut être remplacé par n'importe quel nom de "branch_name" pertinent.

---

### Comment pousser du Code Existant vers un nouveau dépôt Github

> _"Coder est une belle chose. Tout le monde peut apprendre à coder !"_ 

Ce que vous devez faire :

* Copiez le lien `HTTPS` fourni.  
![Exemple de Dépôt Vide](http://res.cloudinary.com/poetrique/image/upload/c_scale,w_700/v1536217259/allbuy-i-ng/gallery/github-example.png)

* Exécutez `git init` dans le terminal. Cela initialisera le dossier/dépôt que vous avez sur votre système informatique local.
* Exécutez `git add .` dans le terminal. Cela suivra les changements apportés au dossier sur votre système, depuis le dernier commit. Comme c'est la première fois que vous commitez le contenu du dossier, cela ajoutera tout.
* Exécutez `git commit -m"insérer Message ici"`. Cela préparera les changements ajoutés/suivis du dossier sur votre système pour les pousser vers Github. Ici, **_insérer Message ici_** peut être remplacé par n'importe quel message de commit pertinent de votre choix.
* Exécutez `git remote add origin https://github.com/Usheninte/example.git` dans le terminal. Ici, **_Usheninte_** et **_example_** seront remplacés par les valeurs fournies dans le lien copié. Cela poussera le dossier existant sur votre système informatique local, vers le **nouvellement créé** dépôt Github.
* Exécutez `git remote -v`. Cela fait un peu de magie **_git pull_** et **_git push_**, pour s'assurer que le contenu de votre nouveau dépôt Github, et le dossier sur votre système local sont les mêmes.
* Exécutez `git push origin master`. Notez que le dernier mot dans la commande **_master_**, n'est pas une entrée fixe lors de l'exécution de `git push`. Il peut être remplacé par n'importe quel nom de "branch_name" pertinent.

---

Alors, c'est tout ! Je crois honnêtement que tout le monde peut apprendre à coder. J'ai passé l'année dernière à tutorer des étudiants de premier cycle au Nigeria, sur le Développement Logiciel. Bientôt, je commencerai mon voyage en tant qu'[Entrepreneur-in-Training](https://meltwater.org/training-program/) à la **Meltwater Entrepreneurial School of Technology.**

> Commencez à coder dès aujourd'hui !