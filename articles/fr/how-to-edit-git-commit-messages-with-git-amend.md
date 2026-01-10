---
title: Git Change Commit Message – Comment modifier les messages de commit avec Git
  Amend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-09T17:58:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-edit-git-commit-messages-with-git-amend
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Shittu-Olumide-Git-Change-Commit-Message
seo_title: Git Change Commit Message – Comment modifier les messages de commit avec
  Git Amend
---

How-to-Edit-Commit-Messages-with-Git-Amend.png
tags:
- name: Git
  slug: git
- name: contrôle de version
  slug: version-control
seo_title: null
seo_desc: "Par Shittu Olumide\nLes messages de commit jouent un rôle crucial dans le contrôle de version Git.\
  \ Ils fournissent un historique des changements apportés à un dépôt. \nClairs et\
  \ descriptifs, les messages de commit vous aident à mieux collaborer avec les membres de l'équipe, à\
  \ maintenir plus facilement..."
---

Par Shittu Olumide

Les messages de commit jouent un rôle crucial dans le contrôle de version Git. Ils fournissent un historique des changements apportés à un dépôt. 

Des messages de commit clairs et descriptifs vous aident à mieux collaborer avec les membres de l'équipe, à maintenir plus facilement votre code et à comprendre le fonctionnement du projet. 

Mais il arrive que vous deviez modifier un message de commit en raison de fautes de frappe, d'inexactitudes ou d'informations insuffisantes. C'est là que Git **amend** entre en jeu.

Dans cet article, nous explorerons la puissance de Git amend et sa capacité à modifier les messages de commit. Nous aborderons tout, depuis l'identification du commit à modifier jusqu'à l'enregistrement et le push des changements. Je partagerai également les meilleures pratiques, conseils et directives pour vous aider à prendre des décisions éclairées sur le moment et la manière de modifier les messages de commit.

En comprenant et en utilisant efficacement Git amend, vous pouvez maintenir un historique de commit propre et précis.

## Qu'est-ce que Git amend ?

Git amend est une commande dans Git qui vous permet d'apporter des modifications au commit le plus récent de votre dépôt sans créer de commits supplémentaires. Elle est particulièrement utile pour éditer les messages de commit, bien que vous puissiez également l'utiliser pour ajouter ou supprimer des fichiers du commit précédent.

Lorsque vous utilisez Git amend, il modifie le commit le plus récent et le remplace par un nouveau commit qui inclut les modifications que vous avez apportées. Cela vous permet de corriger ou d'améliorer le message de commit ou le contenu du commit lui-même.

Git amend offre un moyen pratique de corriger de petites erreurs ou omissions dans vos commits sans avoir à créer un nouveau commit. Il aide à maintenir un historique de commit propre en vous permettant de faire des ajustements sans encombrer le dépôt avec des commits inutiles.

## Comment modifier les messages de commit Git

### Étape 1 : Identifier le commit à modifier.

Utilisez la commande suivante pour afficher l'historique des commits et identifier le message de commit que vous souhaitez modifier :

```bash
git log
```

Recherchez le hash de commit spécifique ou le message de commit que vous souhaitez modifier.

### Étape 2 : Modifier le message de commit.

Une fois que vous avez identifié le commit, utilisez la commande suivante pour modifier le message de commit sans changer aucun autre détail :

```bash
git commit --amend --no-edit
```

Cette commande ouvrira l'éditeur de texte par défaut (généralement Vim ou nano) avec le message de commit existant. Apportez les modifications nécessaires au message.

Ensuite, enregistrez et quittez l'éditeur de texte.

### Étape 3 : Enregistrer les modifications.

Après avoir modifié le message de commit, Git mettra à jour le commit avec le message modifié. Mais il est crucial de vérifier les modifications avant de les enregistrer.

Vous pouvez utiliser la commande suivante pour vérifier les modifications apportées au message de commit :

```bash
git show HEAD
```

Cela affichera les modifications que vous avez apportées au message de commit. Assurez-vous que les modifications sont correctes et reflètent le message souhaité.

### Étape 4 : Pousser le commit modifié.

Pousser des commits modifiés peut être problématique si vous avez déjà poussé le commit original vers un dépôt partagé. Il est généralement déconseillé de modifier des commits qui ont été poussés et partagés avec d'autres, car cela peut entraîner des conflits.

Si le commit n'a pas encore été poussé ou si vous travaillez dans un dépôt local, vous pouvez pousser le commit modifié en utilisant la commande suivante :

```bash
git push --force origin <nom-de-la-branche>
```

Soyez prudent lorsque vous utilisez l'option `--force`, car elle écrase la branche distante avec vos modifications locales. Assurez-vous de communiquer avec les membres de l'équipe avant d'utiliser cette option.

C'est tout ! Vous avez réussi à apprendre comment utiliser Git amend pour modifier un message de commit.

## Pourquoi les messages de commit clairs et descriptifs sont importants

Les messages de commit clairs et descriptifs sont essentiels dans les systèmes de contrôle de version comme Git pour plusieurs raisons :

1. **Communication** : Les messages de commit servent de forme de communication entre les développeurs. Lors de la collaboration sur un projet, des messages de commit clairs et descriptifs aident les membres de l'équipe à comprendre le but et l'intention derrière les changements apportés à la base de code. 
2. **Compréhension des changements** : Les messages de commit fournissent un contexte et une clarté sur les changements apportés dans un commit particulier. Ils aident à répondre à des questions telles que pourquoi un changement a été fait, quel problème il aborde et comment il affecte la base de code. 
3. **Débogage et suivi des problèmes** : Lors de la rencontre d'un bug ou d'un problème, les messages de commit peuvent fournir des informations cruciales pour le débogage et la recherche de la source du problème. En examinant les messages de commit, les développeurs peuvent identifier les changements spécifiques qui ont pu introduire le bug ou causer le problème, ce qui facilite la localisation et la correction du problème.
4. **Documentation et référence historique** : Les messages de commit servent de forme de documentation pour l'historique du projet. Ils fournissent un enregistrement chronologique des changements apportés à la base de code, documentant l'évolution du projet au fil du temps.
5. **Maintenance du code et transmission de la maintenance** : Des messages de commit bien rédigés rendent la maintenance du code plus gérable. Lors de la maintenance d'un projet, les développeurs peuvent se référer aux messages de commit pour comprendre la logique derrière les changements précédents et prendre des décisions éclairées concernant les modifications ultérieures. 

## Conclusion

Git amend est un outil puissant qui permet aux développeurs de modifier les messages de commit et d'améliorer la clarté et l'exactitude de leur historique de contrôle de version. En suivant le guide étape par étape décrit dans cet article, vous pouvez facilement modifier les messages de commit dans votre dépôt Git.

Cependant, il est important d'utiliser Git amend avec discernement. Bien qu'il puisse être bénéfique de corriger de petites fautes de frappe ou d'ajouter des détails manquants, une utilisation excessive de Git amend peut entraîner de la confusion et perturber l'intégrité de l'historique des commits. 

Il est important de trouver un équilibre entre le maintien d'informations précises et la préservation de l'ordre chronologique et du contexte des commits.

Pour approfondir vos connaissances sur les messages de commit Git et les meilleures pratiques de contrôle de version, vous pouvez explorer des ressources supplémentaires telles que la documentation Git, des tutoriels et des communautés en ligne.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !