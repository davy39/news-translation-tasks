---
title: Comment gérer votre projet open source avec GitHub
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2024-09-05T11:52:11.080Z'
originalURL: https://freecodecamp.org/news/how-to-manage-your-open-source-project-with-github
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725180872053/0ea74f81-dc72-4f09-976f-4199c2e3893b.png
tags:
- name: GitHub
  slug: github
- name: Open Source
  slug: opensource
seo_title: Comment gérer votre projet open source avec GitHub
seo_desc: 'Managing your repository is one of the most important tasks for every open-source,
  individual, or proprietary software project.

  Small open-source project repositories are easily maintained without using additional
  functionality because few developers...'
---

La gestion de votre dépôt est l'une des tâches les plus importantes pour tout projet logiciel open source, individuel ou propriétaire.

Les dépôts de petits projets open source sont facilement maintenus sans utiliser de fonctionnalités supplémentaires, car peu de développeurs y travaillent.

Cependant, lors de la gestion de projets open source de taille moyenne ou grande, le problème principal réside dans la manière de les organiser.

Avec de nombreux développeurs contribuant en même temps et une communauté de développeurs s'étendant rapidement jour après jour, cela devient un défi significatif.

GitHub, GitLab, Gitea, etc., disposent de fonctionnalités similaires qui vous aident, vous et votre équipe, à gérer votre projet plus efficacement. Sans dépendre d'autres logiciels et outils, vous pouvez gérer votre projet directement avec votre dépôt.

Dans ce tutoriel, nous aborderons trois fonctionnalités de base de GitHub qui peuvent vous aider à gérer votre dépôt plus efficacement sans utiliser d'outils ou de services supplémentaires :

1. Labels
    
2. Projects
    
3. Milestones
    

GitHub, Gitlab ou Gitea ont tous des fonctionnalités similaires portant le même nom.

## Comment utiliser les Labels sur GitHub

![Exemple de Label dans GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1725176936595/be0c22c3-d182-40a9-917a-2b0b3f2ba87b.png align="center")

Le [label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) aide à catégoriser les issues, les pull requests et les discussions. Par défaut, GitHub est livré avec quelques labels intégrés.

![Liste des labels GitHub par défaut](https://cdn.hashnode.com/res/hashnode/image/upload/v1725177106112/5ceb58b0-985b-4582-bb67-e4313dd833b4.png align="center")

Vous pouvez également créer un label personnalisé. Vous pouvez utiliser le label sur n'importe quelle issue, pull request ou discussion au sein de votre dépôt.

Vous pouvez trouver la liste des [labels par défaut dans la documentation GitHub](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#about-default-labels).

### Comment créer un Label dans votre dépôt

Créer un label personnalisé dans le dépôt est très simple. Il existe différentes façons de créer un label. Vous devez suivre ces étapes communes :

Allez dans votre dépôt &gt; allez ensuite dans les issues &gt; puis cliquez sur le bouton labels.

![Aller à la page des Labels.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725177276807/85a102cf-0817-4d96-a353-6675272f6d0b.png align="center")

Ensuite, cliquez sur le bouton New Label et saisissez le nom, la description et la couleur de votre label.

![Créer le label dans Github.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725177420526/1a6b3752-ce12-4d01-a241-4fe469ec9f44.png align="center")

### Comment supprimer et modifier des Labels sur GitHub

Pour modifier et supprimer un label, allez sur la page des issues et cliquez sur le bouton **Label**. Sur la page des labels, vous devriez voir tous les labels existants.

Cliquez sur le bouton **Edit** pour modifier un label, et cliquez sur le bouton **Delete** pour supprimer un label.

![Modifier et supprimer le Label](https://cdn.hashnode.com/res/hashnode/image/upload/v1725177545826/62926118-df86-4e82-ab05-539ca14c136b.png align="center")

> Vous ne pouvez pas supprimer plusieurs labels à la fois avec GitHub.

## Comment utiliser GitHub Projects

![Page Project](https://www.freecodecamp.org/news/content/images/2024/08/project.png align="center")

L'outil [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects) est un outil polyvalent et flexible pour planifier et gérer le travail de votre dépôt dans un emplacement central.

Il fonctionne de manière similaire à une feuille de calcul, un tableau de tâches et une feuille de route, vous permettant de planifier et de suivre le travail de votre dépôt en un seul endroit. GitHub Projects est entièrement intégré à GitHub.

Vous pouvez créer et personnaliser plusieurs vues, filtrer, trier et grouper vos issues et pull requests, visualiser le travail avec des graphiques et ajouter des champs personnalisés pour suivre des métadonnées spécifiques.

Vous pouvez assigner des utilisateurs à des issues spécifiques, vérifier le statut des issues et assigner des réviseurs, entre autres fonctions.

Les GitHub Projects existent en deux types : publics et privés.

* Les projets **Publics** sont visibles par tous, et l'équipe de gestion peut y apporter des modifications.
    
* Les projets **Privés**, en revanche, ne sont pas visibles par les autres, et seule l'équipe de gestion peut les modifier.
    

Par défaut, les projets sont privés sur GitHub.

### Comment créer des Projects sur GitHub

Créer un project est une tâche simple. Dans certains cas, l'onglet Projects peut ne pas être visible sur votre dépôt. Tout d'abord, allez dans les paramètres de votre dépôt et activez la fonctionnalité Project.

![Activer l'onglet Project dans GitHub.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725178051832/fac9c92e-8527-4c28-94ea-daf102a6ba93.png align="center")

Après avoir activé les projects sur votre dépôt, vous devriez maintenant voir un onglet Projects. Cliquez sur cet onglet.

![Cliquer sur l'onglet Project](https://cdn.hashnode.com/res/hashnode/image/upload/v1725178167552/383a3f8d-d4e6-4994-a4f3-c556bc4e25f4.png align="center")

Votre page de projet par défaut ressemble à ceci. Pour créer un nouveau projet, cliquez sur l'icône de la liste déroulante et sélectionnez **New Project**, puis cliquez à nouveau sur l'option **New Project**.

![Créer un nouveau project](https://cdn.hashnode.com/res/hashnode/image/upload/v1725178437699/eec3dbff-8715-4d3b-805c-83cdfb149c06.png align="center")

Ensuite, sélectionnez le modèle pour le projet selon vos besoins. Cliquez sur le bouton **view all** pour voir tous les modèles disponibles, ou commencez avec un modèle vide.

Le modèle est livré avec une préconfiguration basée sur votre choix.

![Sélectionner le modèle pour votre project.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725178566692/29932135-3e90-42d8-8b71-092eac00d9ea.png align="center")

J'ai sélectionné le modèle « feature release » pour ce tutoriel. Ensuite, entrez le nom de votre projet et cliquez sur le bouton **Create Project**.

![Créer un projet avec le modèle sélectionné.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725178693346/211597d1-309d-4ccf-a0bd-c6fbed891111.png align="center")

Votre projet devrait être créé sur la base du modèle choisi. La page de votre tableau de bord de projet peut varier selon le modèle.

![Votre tableau de bord de projet ressemble à ceci.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179016256/91a10481-874b-4441-9038-0686675ca7ae.png align="center")

### Comment supprimer et modifier des Projects sur GitHub

Pour modifier et supprimer un projet, rendez-vous sur la page des projets.

![Page GitHub projects](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179133210/2526dec0-e354-48db-b6a9-a607f644ccf7.png align="center")

Cliquez ensuite sur le projet que vous souhaitez modifier ou supprimer. Cliquer sur le titre du projet devrait vous mener à la page des paramètres du projet.

![Page Project](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179213957/ef9aa361-3f2b-41d5-bb4a-660886120f9b.png align="center")

Dans la page des paramètres du projet, vous pouvez modifier le titre et la description du projet, supprimer le projet, fermer le projet et également changer la visibilité de votre projet de privé à public.

![Page des paramètres du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179309181/5533fb7a-9dc5-42c1-81ae-9b1ee7a60b46.png align="center")

## Comment utiliser les Milestones sur GitHub

![Milestones dans GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179667880/661d75ba-1212-4987-a4db-1344cf8fb487.png align="center")

La [fonctionnalité Milestone](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones) vous permet de suivre la progression des issues ou des pull requests dans un dépôt. Avec les milestones, vous pouvez prioriser les issues et pull requests ouvertes et définir une date d'échéance pour un groupe d'éléments liés.

En termes simples, les milestones fonctionnent comme une liste de tâches, où vous pouvez détailler la quantité de travail terminé ou en attente. Cela fonctionne comme une barre de progression, aidant votre équipe à gérer le projet plus efficacement et à communiquer l'importance d'issues spécifiques à votre équipe ainsi qu'à la communauté open source.

Les milestones permettent à la communauté open source et à votre équipe de comprendre l'état d'avancement du travail et le calendrier des versions à venir.

### Comment créer des Milestones sur GitHub

Tout d'abord, allez dans le dépôt puis sur la page des issues. Cliquez sur le bouton milestones.

![Cliquer sur le bouton Milestones.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179807807/d9b3aeeb-b244-4165-af99-10eb395d5e71.png align="center")

Maintenant, vous devriez voir votre liste de milestones actuelle. Pour créer un milestone, cliquez sur le bouton **new milestones**.

![Cliquer sur le bouton New Milestones pour créer un Milestone.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725179917831/f4e186c6-3bf7-4058-8de4-9a3d470c96ca.png align="center")

Saisissez le titre du milestone, la date d'échéance et la description, puis cliquez sur le bouton **Create milestones** pour finaliser la création.

![Créer un nouveau milestone dans GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180035699/e3a7d784-a33c-45a0-a2d0-4cd53d33a251.png align="center")

Par défaut, votre milestone créé devrait ressembler à ceci :

![Saisir des informations sur les milestones.](https://www.freecodecamp.org/news/content/images/2024/08/bydefault-your-milestone-look-like-this.png align="center")

Notre tâche suivante consiste à assigner une issue au milestone. Allez dans l'issue concernée et assignez-lui un milestone.

![Assigner le milestone à une issue](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180104276/ad15123a-acf9-4577-90cb-3aa294f03d8a.png align="center")

Si vous avez plusieurs milestones, vous pouvez sélectionner celui de votre choix.

![Sélectionner le milestone](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180261186/4e506d15-613b-4d10-818c-2ff8168a6459.png align="center")

Vérifiez si l'issue est bien rattachée au milestone.

![Vérifier si l'issue est attachée ou non au milestone.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180354959/4c7a3127-df19-49bb-89dc-3409eae8e23a.png align="center")

Désormais, vous pouvez attacher ou assigner plusieurs issues à un seul milestone. Lorsque vous consultez le milestone, vous pouvez voir la liste de toutes les issues assignées.

![Listes des milestones assignés.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180446204/149dc05e-8e6f-4db1-816d-8b1b179b5a47.png align="center")

Si vous ou vos collaborateurs fermez l'issue, votre barre de progression augmente automatiquement. Cela aide votre équipe et votre communauté à visualiser la quantité de travail accomplie.

![La barre de progression augmente automatiquement dans les milestones.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180561440/6133c4c6-e60f-4176-88dc-80beb916ea30.png align="center")

### Comment supprimer et modifier des Milestones sur GitHub

Pour modifier et supprimer les milestones, rendez-vous sur la **page des issues** et cliquez sur le bouton milestones pour afficher les milestones disponibles.

Pour modifier un milestone, cliquez sur le bouton **edit**, et pour le supprimer, cliquez sur le bouton **delete**.

![Modifier et supprimer le milestone](https://cdn.hashnode.com/res/hashnode/image/upload/v1725180673832/1b71ecd9-fadb-4feb-9b62-2c1a4fcf597c.png align="center")

# Conclusion

Les Labels, les Projects et les Milestones sont des fonctionnalités de base essentielles pour gérer un projet sur GitHub. En les utilisant, vous apprendrez naturellement à les maîtriser.

Les Milestones et les Projects sont différents, et ils ne sont pas directement comparables car ils offrent des fonctionnalités et des modes de fonctionnement distincts.

Comme je l'ai mentionné, un Milestone est utilisé pour suivre la progression des issues ou des pull requests dans un dépôt. D'un autre côté, un Project est utilisé pour planifier et gérer votre dépôt depuis un emplacement central.

Pour les petites équipes, je recommande les Milestones, et pour les grandes équipes, l'utilisation des Projects. Vous pouvez également combiner l'usage des Projects et des Milestones pour une meilleure productivité.

J'ai écrit d'autres articles liés à GitHub que vous pouvez consulter ici :

* [https://www.freecodecamp.org/news/what-is-github-wiki-and-how-do-you-use-it/](https://www.freecodecamp.org/news/what-is-github-wiki-and-how-do-you-use-it/)
    
* [https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/](https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/)
    
* [https://www.freecodecamp.org/news/how-to-run-github-actions-locally/](https://www.freecodecamp.org/news/how-to-run-github-actions-locally/)