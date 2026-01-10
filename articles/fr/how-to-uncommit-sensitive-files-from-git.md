---
title: Comment supprimer des fichiers sensibles de Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T20:55:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-uncommit-sensitive-files-from-git
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/IMG_5162.00_00_17_13.Still001-1.jpg
tags:
- name: Git
  slug: git
- name: information security
  slug: information-security
- name: version control
  slug: version-control
seo_title: Comment supprimer des fichiers sensibles de Git
seo_desc: "By Ondrej Polesny\nStage files, add a commit message, push. No – wait!\
  \ Not that file. And now we need to start googling. \nEvery developer has accidentally\
  \ committed sensitive files in the past. So how do we fix the situation and ensure\
  \ it wonʼt happen..."
---

Par Ondrej Polesny

Stage files, add a commit message, push. Non – attendez ! Pas ce fichier. Et maintenant, nous devons commencer à chercher sur Google. 

Chaque développeur a déjà commis par accident des fichiers sensibles dans le passé. Alors, comment corriger la situation et s'assurer que cela ne se reproduise plus ?

Dans cet article, j'expliquerai quoi faire lorsque vous commettez accidentellement un fichier sensible et inclurai les commandes Git nécessaires pour ajuster l'historique.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/illustration.png)
_Comment supprimer des fichiers sensibles de git_

## Contrôle des dommages

Donc, vous avez accidentellement commis un fichier sensible. Appelons-le _.env_. Il y a deux questions importantes à répondre :

* Avez-vous poussé le commit vers un dépôt distant ?
* Le dépôt distant est-il public ?

### Pas encore poussé

Si vous n'avez pas encore poussé, la situation n'est pas du tout critique. Vous pouvez **revenir à un commit précédent** :

```
git reset HEAD^ --soft
```

Vos fichiers resteront dans la copie de travail afin que vous puissiez corriger le fichier/information sensible. Si vous souhaitez **conserver le commit et simplement supprimer le fichier sensible**, faites :

```
git rm .env --cached
git commit --amend
```

Vous pouvez utiliser `--amend` uniquement sur le dernier commit. Si vous avez réussi à ajouter un tas de commits par-dessus, utilisez :

```
git rebase -i HEAD~{combien de commits revenir ?}
```

Cela vous permettra de corriger le commit défectueux et de rejouer tous les commits restants après la correction afin de ne pas les perdre.

### Déjà poussé

Si vous avez poussé, il y a une différence importante entre les dépôts publics et privés.

Si votre dépôt est privé et qu'il n'y a pas de bots ou de personnes à qui vous ne faites pas confiance avec accès à celui-ci, vous pouvez facilement modifier le dernier commit en utilisant les deux commandes ci-dessus. 

Si vous avez poussé un tas de commits par-dessus celui problématique, vous pouvez toujours utiliser [filter-branch](https://git-scm.com/docs/git-filter-branch) ou [BFG repo cleaner](https://rtyley.github.io/bfg-repo-cleaner/) pour **supprimer le fichier sensible de l'historique git** :

```
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
```

Mais gardez à l'esprit deux aspects importants de ces changements :

* **Vous modifiez réellement l'historique**  
Si d'autres personnes, d'autres branches, d'autres forks ou des pull requests ouvertes dépendent de l'état actuel du dépôt, vous les casserez. Dans ces cas, traitez le dépôt comme s'il était public et évitez de modifier l'historique.
* **Vous devez vider le cache**  
Vous devez toujours contacter le support de votre fournisseur de stockage Git et leur demander de vider le cache de votre dépôt. Même si vous avez corrigé le commit problématique ou réécrit l'historique, l'ancien commit avec le fichier sensible reste dans le cache. Vous aurez besoin de connaître son ID pour y accéder, mais il reste accessible jusqu'à ce que vous vidiez le cache.

## Dois-je régénérer les clés si poussé vers un dépôt public ?

En bref, oui. Si votre dépôt est public ou si vous ne pensez pas qu'il s'agisse d'un endroit sûr pour une autre raison, vous devez considérer les informations sensibles comme compromises. 

Même si vous supprimez les données de votre dépôt, vous ne pouvez rien faire contre les bots et les autres forks du dépôt. Alors, quelles sont les prochaines étapes ?

* **Désactivez toutes les clés et/ou mots de passe**  
Faites cela en premier. Une fois que vous avez désactivé les clés, les informations sensibles deviennent inutiles.
* **Ajustez gitignore**  
Ajoutez tous les fichiers sensibles à .gitignore pour vous assurer que git ne les suit pas.
* **Supprimez le fichier sensible**
* **Commitez la correction avec une explication significative**  
N'essayez pas de cacher l'erreur. Les autres collaborateurs et vous dans un mois apprécieront l'explication de ce qui s'est passé et de ce que ce commit corrige.

## Bonnes pratiques pour stocker des données sensibles dans Git

Pour éviter une situation comme celle-ci à l'avenir, voici quelques conseils pour stocker des données sensibles :

### Gardez les données sensibles dans un fichier .env (ou un fichier similaire sur d'autres plateformes)

Gardez les clés API et autres données sensibles dans un seul fichier .env. De cette façon, vous ne commettrez pas accidentellement une nouvelle clé lorsque le fichier .env est déjà exclu de git. 

Un autre grand avantage est que vous obtenez l'accès à toutes les clés en utilisant une variable globale _process_.

### Utilisez des clés API si possible

Les clés API sont faciles à générer et à désactiver si elles sont compromises. Si possible, utilisez-les et évitez d'utiliser des identifiants/mots de passe.

### Ajoutez les clés API à votre outil de build

Les clés API sont généralement nécessaires pendant les builds d'applications. Les outils de build comme Netlify vous permettent d'ajouter ces clés dans les zones sécurisées de leur administration. Ces clés sont automatiquement injectées dans votre application via la variable globale _process_.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify.png)

### Ajoutez le fichier .env à gitignore

Assurez-vous que Git ne suit pas les fichiers contenant des informations sensibles.

### Fournissez un fichier .env.template

Le fichier template indique aux autres collaborateurs d'ajouter les clés API nécessaires sans qu'ils aient besoin de lire de longues documentations.

### Ne modifiez pas l'historique sur le dépôt distant

Utilisez cela comme une règle générale. Si vous avez suivi les règles ci-dessus, vous n'aurez pas besoin de modifier l'historique.

J'espère que ces informations vous ont aidé à rester du bon côté. Avez-vous une expérience personnelle avec la suppression de commits ou peut-être une bonne _leçon apprise_ ? [Parlez-moi sur Twitter](https://twitter.com/ondrabus) :-)