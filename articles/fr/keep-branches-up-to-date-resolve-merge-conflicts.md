---
title: Comment maintenir les branches à jour et résoudre les conflits de fusion dans
  GitHub et VS Code
subtitle: ''
author: Ayu Adiati
co_authors: []
series: null
date: '2023-11-22T23:23:20.000Z'
originalURL: https://freecodecamp.org/news/keep-branches-up-to-date-resolve-merge-conflicts
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/How-to-Keep-Branches-Up-to-Date-and-Resolve-Merge-Conflicts-in-GitHub-and-VS-Code.png
tags:
- name: beginner
  slug: beginner
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: Visual Studio Code
  slug: vscode
seo_title: Comment maintenir les branches à jour et résoudre les conflits de fusion
  dans GitHub et VS Code
seo_desc: 'Hey {username}, we''ve merged a PR before yours. Please resolve the merge
  conflicts so we can review and merge your PR.


  Have you ever received that kind of message from a maintainer while waiting for
  your pull request to be reviewed and merged? And t...'
---

> Hey {username}, nous avons fusionné une PR avant la vôtre. Veuillez résoudre les conflits de fusion afin que nous puissions examiner et fusionner votre PR.

Avez-vous déjà reçu ce type de message d'un mainteneur pendant que vous attendiez que votre pull request soit examinée et fusionnée ? Et puis, vous paniquez parce que vous ne savez pas quoi faire ? Ou peut-être pensez-vous à fermer votre pull request, tout refaire depuis le début et ouvrir une nouvelle pull request ?

Eh bien, la bonne nouvelle est que vous n'êtes pas seul.

Dans cet article, je vais vous montrer comment maintenir vos branches locales et distantes à jour. Je vais également vous guider à travers la résolution des conflits de fusion dans GitHub et VS Code.

## Table des matières

<ul>
    <li><a href="#prerequis">Prérequis</a></li>
    <li><a href="#comprendre-les-conflits-de-fusion">Comprendre les conflits de fusion</a></li>
    <li>
        <a href="#comment-maintenir-les-branches-a-jour">Comment maintenir les branches à jour</a>
        <ul>
        	<li><a href="#comment-mettre-a-jour-la-branche-main-dans-votre-depot-fork">Comment mettre à jour la branche <code>main</code> dans votre dépôt fork</a></li>
            <li><a href="#comment-mettre-a-jour-votre-branche-locale">Comment mettre à jour votre branche locale</a></li>
        </ul>
    </li>
    <li>
        <a href="#comment-resoudre-les-conflits-de-fusion">Comment résoudre les conflits de fusion</a>
        <ul>
            <li><a href="#1-resoudre-les-conflits-de-fusion-sur-github">1. Résoudre les conflits de fusion sur GitHub</a></li>
            <li><a href="#2-resoudre-les-conflits-de-fusion-dans-vs-code">2. Résoudre les conflits de fusion dans VS Code</a></li>
        </ul>
    </li>
    <li><a href="#mots-de-la-fin">Mots de la fin</a></li>
</ul>

## **Prérequis**

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* Un compte [GitHub](https://github.com/).
* [VS Code](https://code.visualstudio.com/) installé sur votre machine.

## Comprendre les conflits de fusion

Les conflits de fusion se produisent généralement lorsque deux commits ont des modifications dans la ou les mêmes lignes du ou des mêmes fichiers provenant de deux branches différentes. Parfois, cela peut également se produire lorsqu'une personne modifie un fichier et qu'une autre personne le supprime.

Le problème est que Git ne peut pas résoudre le conflit lui-même. Il a besoin de votre aide pour décider quelles modifications doivent être conservées.

Lorsqu'il y a un conflit de fusion, vous verrez une notification dans votre pull request sur GitHub indiquant que la branche a des conflits qui doivent être résolus. Les mainteneurs ne peuvent pas fusionner une pull request lorsque des conflits de fusion se produisent. C'est parce que le bouton de fusion est désactivé jusqu'à ce que les conflits soient résolus.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/branch-has-conflicts.png)
_Avertissement sur une pull request GitHub : Cette branche a des conflits qui doivent être résolus_

## Comment maintenir les branches à jour

Maintenir vos branches à jour est crucial. Il est fortement recommandé de mettre à jour régulièrement vos branches distantes et locales `main` et de travail.

Les meilleurs moments pour mettre à jour vos branches sont :

* avant de créer une nouvelle branche pour travailler sur un problème,
* après avoir validé vos dernières modifications et avant de les pousser vers le dépôt distant,
* pendant que vous attendez que votre pull request soit examinée.

Lorsqu'une pull request est fusionnée pendant que vous attendez que la vôtre soit examinée, il y aura un avertissement dans votre pull request. Il vous indique que votre branche est en retard par rapport à la branche `main` du dépôt `upstream` (original).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/branch-out-of-date.png)
_Avertissement sur une pull request GitHub : Cette branche n'est pas à jour avec la branche de base._

### Comment mettre à jour la branche `main` dans votre dépôt fork

1. Allez dans votre dépôt fork sur GitHub.
2. Cliquez sur le bouton "Sync fork".
3. Cliquez sur le bouton vert "Update branch".

![Image](https://www.freecodecamp.org/news/content/images/2023/11/update-branch.png)
_Boutons "Sync fork" et "Update branch" sur GitHub._

Après avoir mis à jour la branche, vous verrez une notification en haut indiquant que votre branche est à jour.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/up-to-date-branch-github.png)
_Une notification sur GitHub : Cette branche est à jour avec organization-name/repository-name:main._

### Comment mettre à jour votre branche locale

Maintenant, votre branche `main` distante a été mise à jour. Mettons à jour votre branche locale depuis votre terminal.

#### Étape #1 - Allez dans votre branche de travail

Dans votre terminal, naviguez vers votre branche de travail avec cette commande :

```bash
git checkout nom-de-la-branche
```

#### Étape #2 - Récupérez les modifications

Récupérez les dernières modifications de la branche `main` de votre dépôt `origin` (fork) vers votre branche locale.

```bash
git pull origin main
```

#### Étape #3 - Poussez les modifications

Poussez ces modifications vers votre branche distante. Si vous devez résoudre des conflits, vous devez les corriger avant de pouvoir pousser vos modifications.

```bash
git push
```

## Comment résoudre les conflits de fusion

Vous ne pouvez commencer à résoudre les conflits de fusion qu'après avoir mis à jour votre branche de travail. Il existe deux façons de résoudre les conflits :

1. Sur GitHub
2. Dans votre VS Code

### 1. Résoudre les conflits de fusion sur GitHub

Résoudre les conflits directement sur GitHub n'est possible que lorsque la cause des conflits est qu'il y a des modifications dans la ou les mêmes lignes du ou des mêmes fichiers provenant de deux branches différentes. Pour tout autre type de conflits, vous devez les résoudre localement dans votre éditeur de code.

Suivez ces étapes pour résoudre les conflits directement sur GitHub :

#### Étape #1 - Cliquez sur le bouton "Resolve conflicts"

Tout d'abord, allez dans le dépôt `upstream` sur GitHub. Ensuite, cliquez sur l'onglet "Pull request". Trouvez et ouvrez votre pull request, puis faites défiler vers le bas.

Vers la fin, vous trouverez le bouton "Resolve conflicts".

![Image](https://www.freecodecamp.org/news/content/images/2023/11/resolved-conflicts-button.png)
_Une notification de "Cette branche a des conflits qui doivent être résolus" et un bouton "Resolve conflicts" sur GitHub._

#### Étape #2 - Examinez de plus près les conflits

Après avoir cliqué sur le bouton "Resolve conflicts", vous serez redirigé vers l'éditeur de conflits de GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/github-resolve-conflict-2.png)
_Éditeur de conflits de GitHub_

Vous pouvez voir le ou les fichiers qui ont des conflits dans la barre latérale de gauche. Dans la barre supérieure, vous pouvez trouver le nombre de conflits dans le fichier. Et dans le fichier lui-même, il y a des marqueurs de conflit `<<<<<<<`, `=======`, et `>>>>>>>`.

Les lignes entre `<<<<<<< nom-de-la-branche` et `=======` sont vos modifications. Tout ce qui se trouve entre `=======` et `>>>>>>> main` sont les modifications de la branche `main` du dépôt `upstream`.

Vous devez examiner les conflits et décider ceux que vous souhaitez conserver ou si vous devez apporter des modifications entièrement nouvelles.

#### Étape #3 - Résoudre les conflits

Après avoir décidé comment vous souhaitez résoudre les conflits, supprimez les marqueurs de conflit `<<<<<<<`, `=======`, `>>>>>>>`. Ensuite, vous pouvez apporter les modifications. S'il y a plusieurs conflits dans le fichier, faites défiler vers le bas et résolvez-les avant de les marquer comme résolus.

Une fois que vous avez résolu tous les conflits, cliquez sur le bouton "Mark as resolved" dans la barre supérieure.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/mark-as-resolved.png)
_Bouton "Mark as resolved" sur GitHub._

S'il y a des conflits dans un autre ou d'autres fichiers, allez dans le fichier en cliquant sur le nom du fichier dans la barre latérale de gauche. Ensuite, répétez les mêmes étapes pour résoudre les conflits.

#### Étape #4 - Cliquez sur le bouton "Commit merge"

Après que tous les conflits dans tous les fichiers en conflit ont été marqués comme résolus, un bouton vert "Commit merge" apparaîtra en haut à droite. Cliquez sur le bouton pour valider vos modifications.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/commit-merge-btn.png)
_Un bouton "Commit merge" sur GitHub._

### 2. Résoudre les conflits de fusion dans VS Code

Après avoir récupéré les dernières modifications de la branche `main` de votre dépôt fork, vous verrez des lignes entre les marqueurs de conflit `<<<<<<<`, `=======`, et `>>>>>>>`.

Vous verrez également les options pour résoudre les conflits :

* **Accepter la modification actuelle** : Lorsque vous souhaitez conserver uniquement vos modifications.
* **Accepter la modification entrante** : Lorsque vous souhaitez conserver uniquement les modifications de la branche `main`.
* **Accepter les deux modifications** : Lorsque vous souhaitez conserver les vôtres et les modifications entrantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/merge-conflicts-vscode.png)
_Conflits de fusion dans VS Code._

Les lignes entre `<<<<<<< HEAD (Modification actuelle)` et `=======` sont vos modifications. Et tout ce qui se trouve entre `=======` et `>>>>>>> numéros-de-hachage (Modification entrante)` sont des modifications de la branche `main` de votre dépôt fork.

Suivez ces étapes pour résoudre les conflits dans VS Code :

#### Étape #1 - Résoudre les conflits

Examinez de plus près les conflits entre les marqueurs de conflit. Ensuite, vous devez décider comment vous souhaitez résoudre les conflits.

* Vous pouvez supprimer manuellement les marqueurs `<<<<<<<`, `=======`, `>>>>>>>` et apporter les modifications.

**OU**

* Vous pouvez choisir et cliquer sur l'une des options d'acceptation en haut et modifier les changements en fonction de vos besoins.

##### Annuler la fusion

Si à un moment donné vous vous sentez confus et souhaitez annuler la fusion et tout refaire depuis le début, exécutez la commande `git merge --abort` avant de valider vos modifications. Cela annulera la fusion et restaurera votre fichier à l'état précédent les conflits.

#### Étape #2 - Valider vos modifications

Une fois que vous avez terminé de résoudre les conflits, vous devez valider vos modifications. Exécutez cette commande pour mettre automatiquement en scène et valider les modifications :

```bash
git commit -am "Votre message"
```

##### Comprendre la commande `git commit -am`

La commande `git commit -am` est différente de l'exécution de `git add .` suivie de `git commit -m`.

L'exécution de `git add .` ajoutera _tous_ les fichiers (y compris les fichiers nouvellement créés) à la zone de staging. Alors qu'en ajoutant le drapeau `-a` à `git commit`, il mettra automatiquement en scène tous les fichiers que vous avez déjà validés. Cela inclut la mise en scène des fichiers suivis supprimés mais ne mettra pas en scène les fichiers nouvellement créés.

Ainsi, combiner le `-a` avec le drapeau `-m` à `git commit` vous permet de sauter la phase de staging et d'écrire directement le message pour le commit.

#### Étape #3 - Poussez vos modifications

Maintenant, vous pouvez pousser vos modifications vers la branche distante avec la commande suivante :

```bash
git push
```

## Mots de la fin

Si vous avez aimé cet article et l'avez trouvé utile, veuillez le partager avec d'autres. Vous pouvez trouver d'autres travaux sur mon [blog](https://adiati.com/), et connectons-nous sur [X (anciennement Twitter)](https://twitter.com/@AdiatiAyu) ou [LinkedIn](https://www.linkedin.com/in/adiatiayu/).