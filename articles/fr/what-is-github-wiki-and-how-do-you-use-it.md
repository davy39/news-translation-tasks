---
title: Qu'est-ce qu'un Wiki GitHub et comment l'utiliser ?
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2024-04-15T20:46:02.000Z'
originalURL: https://freecodecamp.org/news/what-is-github-wiki-and-how-do-you-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/What-is-GitHub-Wiki-and-How-Do-You-Use-it.png
tags:
- name: documentation
  slug: documentation
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Qu'est-ce qu'un Wiki GitHub et comment l'utiliser ?
seo_desc: 'A GitHub wiki is a great place for your project''s documentation. You can
  use the wiki to create, manage, and host documentation for your repository so others
  can use and contribute to your project.

  GitHub wikis are easy to start using without install...'
---

Un wiki GitHub est un excellent endroit pour la documentation de votre projet. Vous pouvez utiliser le wiki pour créer, gérer et héberger la documentation de votre dépôt afin que d'autres puissent utiliser et contribuer à votre projet.

Les wikis GitHub sont faciles à utiliser sans installer de logiciel supplémentaire. Le meilleur, c'est que le wiki est intégré à votre dépôt GitHub. 

Vous n'avez besoin d'aucun autre outil – vous devez simplement savoir utiliser le markdown, car vous l'utiliserez pour écrire votre wiki. (Vous pouvez [tout lire à ce sujet dans mon autre article ici](https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/).)

## Comment commencer à utiliser le Wiki GitHub

Vous pouvez commencer votre wiki GitHub en un seul clic. Chaque dépôt GitHub a un onglet Wiki dans le menu en haut de la page. Pour commencer, cliquez dessus.

![Page du dépôt GitHub](https://www.freecodecamp.org/news/content/images/2024/04/github-wiki.png)
_Page du dépôt GitHub_

L'onglet wiki n'est parfois pas affiché par défaut dans la barre de navigation du dépôt GitHub. Tout d'abord, vous devez activer les wikis dans les paramètres de votre dépôt.

![Aucun onglet wiki n'est affiché.](https://www.freecodecamp.org/news/content/images/2024/04/no-wiki.png)
_Aucun onglet wiki n'est affiché._

Pour ce faire, allez dans la page des paramètres de votre dépôt, faites défiler vers le bas et trouvez la section des fonctionnalités. Ensuite, activez les wikis en cochant la case "Wikis".

![Activer le wiki dans GitHub](https://www.freecodecamp.org/news/content/images/2024/04/Wiki-enable.png)
_Activer le wiki_

Pour initialiser le wiki dans votre dépôt GitHub, créez la page d'accueil dans votre wiki.

![Initialiser le wiki dans GitHub.](https://www.freecodecamp.org/news/content/images/2024/04/first-page.png)
_Initialiser le wiki dans GitHub._

Lorsque vous cliquez sur le bouton "**Créer la première page**", vous serez redirigé vers la page de l'éditeur où vous pourrez créer une page d'accueil dans le wiki.

![Créer une page d'accueil et initialiser le wiki.](https://www.freecodecamp.org/news/content/images/2024/04/Home-wiki-Page.png)
_Créer une page d'accueil et initialiser le wiki._

Votre page d'accueil du wiki devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Your-wiki-is-look-like-this.png)
_Page d'accueil du wiki_

## Comment cloner un Wiki GitHub localement

Parfois, les nouveaux développeurs sont confus sur la façon de cloner le wiki localement. Pour ce faire, copiez simplement le lien où il est écrit « Clone this wiki locally », comme vous pouvez le voir dans l'image ci-dessous :

![Copier le lien pour cloner le wiki GitHub.](https://www.freecodecamp.org/news/content/images/2024/04/clone.png)
_Copier le lien pour cloner le wiki GitHub._

Copiez ce lien et clonez le dépôt du wiki GitHub localement sur votre ordinateur portable ou votre machine.

Maintenant, vous pouvez apporter des modifications au wiki, telles que l'édition, la mise à jour ou la modification de la documentation localement. Après avoir terminé les modifications de la documentation, vous pouvez pousser votre documentation locale du wiki vers le dépôt du wiki GitHub.

```bash
$ git clone https://github.com/officialrajdeepsingh/github-wiki-tutorial.wiki.git
Cloning into 'github-wiki-tutorial.wiki'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
Resolving deltas: 100% (1/1), done.

```

## Comment personnaliser votre Wiki

Les wikis ont des options de personnalisation limitées pour la barre latérale, la page d'accueil et le pied de page. Mais vous pouvez étendre ces options en utilisant HTML, CSS et Markdown.

Nous avons déjà discuté de la page d'accueil, et maintenant nous allons discuter du pied de page et de la barre latérale.

Le pied de page et la barre latérale affichent ou contiennent des liens utiles tels que des informations de contact, des liens de navigation, des liens vers les réseaux sociaux, etc.

Le pied de page est affiché en bas de chaque page de votre site, et la barre latérale est généralement une colonne verticale sur le côté gauche ou droit d'une page web. Les deux sont visibles sur toutes les pages du wiki.

### Comment créer une barre latérale personnalisée

Il existe deux façons de créer une barre latérale dans le wiki GitHub.

1. Avec l'interface utilisateur de GitHub
2. Localement dans votre IDE

Nous allons examiner chaque méthode ici afin que vous puissiez choisir celle qui vous convient le mieux.

#### Avec l'interface utilisateur de GitHub

![Créer une barre latérale](https://www.freecodecamp.org/news/content/images/2024/04/sidebar-1.png)
_Créer une barre latérale_

Allez à la page d'accueil du wiki et cliquez sur le bouton « Ajouter une barre latérale personnalisée » pour créer une barre latérale dans votre wiki.

Ensuite, vous serez redirigé vers la page de l'éditeur pour créer une page de barre latérale. Dans le fichier de la barre latérale, vous pouvez écrire du contenu en markdown tel que des liens de navigation, etc. Après cela, cliquez sur le bouton **enregistrer**.

![Créer un fichier _Sidebar.md dans le wiki GitHub.](https://www.freecodecamp.org/news/content/images/2024/04/create-sidebar-page.png)
_Créer un fichier `_Sidebar.md`._

#### Localement dans votre IDE

La deuxième façon est de cloner votre wiki localement, puis de créer un fichier `_Sidebar.md` 
à la racine de votre wiki en utilisant VS Code ou tout autre IDE que vous préférez. 

### Comment créer un pied de page personnalisé

Vous suivrez essentiellement les mêmes étapes que dans la section de la barre latérale pour créer votre pied de page de wiki personnalisé.

#### Avec l'interface utilisateur de GitHub

![Image](https://www.freecodecamp.org/news/content/images/2024/04/footer.png)

Allez à votre page de wiki et cliquez sur le bouton « Ajouter un pied de page personnalisé » pour créer un pied de page dans votre wiki.

Ensuite, vous serez redirigé vers la page de l'éditeur pour créer un pied de page. Dans le fichier du pied de page, vous pouvez écrire du contenu en markdown tel que des liens de navigation, etc. Après cela, cliquez sur le bouton **enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/footer-editor.png)
_Créer un pied de page_

#### Localement dans votre IDE

La deuxième façon est de cloner votre wiki localement, puis de créer un fichier `_Footer.md` 
à la racine de votre wiki en utilisant VS Code ou tout autre IDE que vous préférez. 

## Qu'est-ce qu'une Page ? Comment créer une nouvelle Page dans le Wiki ?

Dans un wiki, une page a une fonctionnalité similaire à celle des autres CMS, vous donnant le pouvoir de gérer votre contenu et votre documentation.

Avec la page du wiki, vous pouvez diviser votre contenu ou vos documents en différentes sections telles que l'installation, la configuration, etc.

Pour créer une nouvelle page, cliquez sur le bouton de nouvelle page.

![Créer une nouvelle page de wiki](https://www.freecodecamp.org/news/content/images/2024/04/create-a-page.png)
_Créer une nouvelle page de wiki_

Cela vous redirige vers la page de l'éditeur, où vous pouvez ajouter un titre et du contenu. Après avoir terminé votre écriture, cliquez sur le bouton enregistrer.

![Créer une page de wiki](https://www.freecodecamp.org/news/content/images/2024/04/create-a-new-page-with-wiki.png)
_Créer une page de wiki_

Votre page ressemble à ceci dans le wiki après sa publication :

![La page du wiki ressemble à ceci dans le navigateur après la publication.](https://www.freecodecamp.org/news/content/images/2024/04/your-installation-page.png)
_La page du wiki ressemble à ceci dans le navigateur après la publication._

Tout le monde peut accéder à votre section de pages. Chaque page que vous publiez est affichée dans la section des pages de votre wiki.

![La section des pages montre la liste des pages publiées.](https://www.freecodecamp.org/news/content/images/2024/04/access-the-page.png)
_La section des pages montre la liste des pages publiées._

## Comment activer et désactiver la collaboration dans le Wiki

Pour activer la collaboration pour tout le monde dans le wiki, allez dans la page des paramètres de votre dépôt GitHub, faites défiler vers le bas, trouvez les fonctionnalités et décochez la case "Restreindre l'édition aux collaborateurs uniquement".

![Activer la collaboration dans le Wiki GitHub.](https://www.freecodecamp.org/news/content/images/2024/04/access-to-eveyone-in-wiki.png)
_Activer la collaboration dans le Wiki GitHub._

Vous pouvez désactiver la collaboration pour tout le monde, afin que vous et votre équipe soyez les seuls responsables de la mise à jour, de la suppression et de l'édition du wiki.

Pour ce faire, vous devez restreindre l'édition pour les autres utilisateurs. L'activation de l'option **Restreindre l'édition aux collaborateurs uniquement** permet de le faire rapidement.

Après qu'il n'y ait eu aucune édition, invitez votre équipe et donnez-leur accès. Ensuite, cliquez simplement sur la case à cocher "Restreindre l'édition aux collaborateurs uniquement".

![Désactiver la collaboration dans le Wiki GitHub.](https://www.freecodecamp.org/news/content/images/2024/04/enable-it.png)
_Désactiver la collaboration dans le Wiki GitHub._

## Pourquoi le Wiki GitHub est-il si utile ?

Les wikis GitHub peuvent être utiles pour tout le monde. Vous pouvez commencer votre documentation avec un wiki en moins d'une minute. Vous n'avez besoin de rien pour commencer à écrire votre documentation, sauf une connaissance de base de la syntaxe Markdown. 

En utilisant les wikis GitHub, vous pouvez vous concentrer sur l'écriture de la documentation de base et sur le projet lui-même. GitHub wiki gère le reste de votre documentation, comme les préoccupations d'hébergement, la recherche, etc. Plus important encore, pour les wikis de dépôts publics, c'est [totalement gratuit](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages). 

De nombreux projets open source célèbres utilisent Wiki de nos jours, tels que [hhvm](https://github.com/facebook/hhvm/wiki), [neovim](https://github.com/neovim/neovim/wiki), [guard](https://github.com/guard/guard/wiki), [foundation db](https://github.com/apple/foundationdb/wiki), et d'autres.

Consultez la [liste des projets utilisés dans Wiki](https://github.com/MyHoneyBadger/awesome-github-wiki).

## Conclusion

Il existe de nombreux frameworks de documentation sur le marché, tels que Nextra, Lume, Starlight et Docusaurus. Mais ils prennent un certain temps à apprendre, configurer et installer. 

De plus, si vous travaillez encore sur vos compétences en codage et que vous n'êtes pas à l'aise avec des outils comme React, MDX, etc., vous devrez prendre un certain temps pour les apprendre avant d'utiliser ces frameworks de documentation plus avancés.

Avec GitHub Wiki, vous pouvez commencer à créer votre documentation immédiatement, et vous n'avez pas besoin de vous soucier du déploiement et de l'hébergement gérés par GitHub.

GitHub Wiki est un excellent choix pour les petits projets et les projets en phase de démarrage. Vous et votre équipe pouvez vous concentrer sur le projet tout en composant une documentation simple.