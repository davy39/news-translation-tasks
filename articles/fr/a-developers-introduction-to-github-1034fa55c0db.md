---
title: Introduction à GitHub pour les développeurs
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-28T17:44:48.000Z'
originalURL: https://freecodecamp.org/news/a-developers-introduction-to-github-1034fa55c0db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1xi2ApL_xJQp2oevpEfQqw.png
tags:
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Introduction à GitHub pour les développeurs
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  GitHub is a website that hosts billions of lines of code, and it’s where millions
  of developers gather every day to collaborate on and report issues with open source
  software.

  In shor...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

GitHub est un site web qui héberge des milliards de lignes de code, et c'est là que des millions de développeurs se réunissent chaque jour pour collaborer et signaler des problèmes avec des logiciels open source.

En bref, c'est une plateforme pour les développeurs, et elle est construite autour de Git.

_CONSEIL : Si vous ne connaissez pas encore Git, [consultez mon guide Git](https://flaviocopes.com/git-guide)._

En tant que développeur, **vous ne pouvez pas éviter d'utiliser GitHub ou un autre outil basé sur Git au quotidien** dans le cadre de votre travail. Il est utilisé soit pour héberger votre code, soit pour collaborer sur le code d'autres personnes. Cet article explique quelques concepts clés de GitHub et comment utiliser certaines de ses fonctionnalités pour améliorer votre flux de travail.

### Pourquoi GitHub ?

Maintenant que vous savez ce qu'est GitHub, vous pourriez vous demander pourquoi vous devriez l'utiliser.

GitHub, après tout, est géré par une entreprise privée, qui tire profit de l'hébergement du code des gens. Alors pourquoi l'utiliser plutôt que des plateformes similaires comme BitBucket ou GitLab ?

Outre les préférences personnelles et les raisons techniques, il y a une grande raison : tout le monde utilise GitHub, donc l'effet de réseau est énorme.

Les principales bases de code ont migré au fil du temps depuis d'autres systèmes de contrôle de version vers Git en raison de sa commodité, et GitHub a été historiquement bien positionné et a fait beaucoup d'efforts pour servir les besoins de la communauté Open Source.

Ainsi, aujourd'hui, chaque fois que vous cherchez une bibliothèque, vous la trouverez 99 % du temps sur GitHub.

En dehors du code Open Source, de nombreux développeurs hébergent également des dépôts privés sur GitHub en raison de la commodité de la plateforme.

Maintenant, commençons par les concepts spécifiques à Git importants qu'un développeur doit connaître.

### Problèmes GitHub

Les problèmes GitHub sont l'un des systèmes de suivi de bugs les plus populaires au monde.

Ils offrent aux propriétaires d'un dépôt la possibilité d'organiser, de taguer et d'associer des problèmes à des jalons.

Si vous ouvrez un problème sur un projet géré par quelqu'un d'autre, il restera ouvert jusqu'à ce que vous le fermiez (par exemple, si vous trouvez la solution à votre problème) ou que le propriétaire du dépôt le ferme.

Parfois, vous obtiendrez une réponse définitive, et à d'autres moments, le problème restera ouvert et sera tagué avec des informations qui le catégorisent. Ensuite, le développeur pourra y revenir pour corriger le problème ou améliorer la base de code avec vos commentaires.

La plupart des développeurs ne sont pas payés pour supporter leur code publié sur GitHub, donc vous ne pouvez pas vous attendre à des réponses rapides. Mais certains dépôts open source sont publiés par des entreprises qui fournissent des services autour de ce code, ont des offres commerciales pour des versions avec plus de fonctionnalités, ou utilisent une architecture basée sur des plugins. Et donc ils ont des développeurs payés travaillant sur le projet open source.

### Codage social

![Image](https://cdn-media-1.freecodecamp.org/images/zeKPlxHOUmeK4gjz37spBu8yaOyHFfn0SPn6)
_Crédit image : [https://octodex.github.com](https://octodex.github.com" rel="noopener" target="_blank" title=")_

Il y a quelques années, le logo de GitHub incluait le slogan "social coding".

Que signifiait cela, et est-ce encore pertinent ? Cela l'est certainement.

#### Suivre

Avec GitHub, vous pouvez suivre un développeur ou un dépôt en allant sur le profil de l'utilisateur et en cliquant sur "suivre", ou en cliquant sur le bouton "surveiller" sur un dépôt.

Dans les deux cas, l'activité apparaîtra dans votre tableau de bord. Suivre un utilisateur ou un dépôt est différent de Twitter, où vous voyez ce que les gens **disent** — au lieu de cela, vous voyez ce que les gens **font**.

#### Étoiles

Une grande fonctionnalité de GitHub est la possibilité de **mettre une étoile à un dépôt**. Cette action l'inclura dans votre liste de "dépôts étoilés", ce qui vous permet de suivre les projets que vous trouvez intéressants et de découvrir des projets similaires.

C'est aussi l'un des mécanismes d'évaluation les plus importants, car plus un dépôt a d'étoiles, plus il est généralement populaire et important. Cela se traduit par une apparition plus marquée dans les résultats de recherche.

Les grands projets peuvent avoir des dizaines de milliers d'étoiles.

GitHub dispose également d'une [page des tendances](https://github.com/trending) où il met en avant les dépôts qui obtiennent le plus d'étoiles sur une période déterminée (par exemple, aujourd'hui, cette semaine ou ce mois-ci).

Apparaître dans ces listes de tendances peut entraîner d'autres effets de réseau, comme être mis en avant sur d'autres sites, simplement parce que vous avez plus de visibilité.

#### Fork

Le dernier indicateur réseau important d'un projet est le nombre de forks.

Cela est essentiel pour le fonctionnement de GitHub, car un fork est la base d'une Pull Request (PR), qui est une proposition de changement. Une personne peut fork votre dépôt, apporter des modifications, puis créer une pull request pour vous demander de fusionner ces changements.

Parfois, la personne qui fork un dépôt ne vous demandera jamais de fusionner quoi que ce soit. Elle peut fork votre dépôt simplement parce qu'elle a aimé votre code et a décidé d'ajouter quelque chose par-dessus, qu'elle ne veut pas fusionner dans le dépôt original. Un utilisateur peut également corriger un bug qu'il rencontrait et qui lui était spécifique.

#### Populaire = meilleur

En fin de compte, ce sont tous des indicateurs clés de la popularité d'un projet. Outre les indicateurs ci-dessus, la date du dernier commit et l'implication de l'auteur dans le suivi des problèmes sont des indications utiles pour savoir si vous devez ou non vous appuyer sur une bibliothèque ou un logiciel.

### Pull requests

Dans la section précédente, j'ai introduit ce qu'est une Pull Request (PR). Pour réitérer, une personne peut fork votre dépôt, apporter des modifications, puis créer une pull request pour vous demander de fusionner ces changements.

Un projet peut avoir des centaines de PR, et il est généralement admis que plus un projet est populaire, plus il a de PR, comme le projet React :

![Image](https://cdn-media-1.freecodecamp.org/images/Z3cdqa5H6YpVbiRanpK5KrI7R7ylKFnErRho)

Une fois qu'une personne soumet une pull request, elle doit être examinée par les mainteneurs principaux du projet.

Selon l'**étendue** de votre pull request (le nombre de changements, le nombre de choses affectées par votre changement, ou la complexité du code touché), le mainteneur peut avoir besoin de plus ou moins de temps pour s'assurer que vos changements sont compatibles avec le projet.

Un projet peut avoir un calendrier clair des changements qu'il souhaite introduire. Le mainteneur peut souhaiter garder les choses simples tandis que vous introduisez une architecture complexe dans une pull request.

Cela signifie qu'**une pull request n'est pas toujours acceptée** rapidement, et **il n'y a aucune garantie que la pull request sera jamais acceptée**.

Dans l'exemple que j'ai posté ci-dessus, il y a une pull request dans le dépôt qui date de 1,5 ans. Et cela arrive dans **tous** les projets — c'est tout à fait normal et peut être dû aux raisons que j'ai mentionnées ci-dessus.

### Gestion de projet

En plus des problèmes, qui sont les endroits où les développeurs reçoivent des commentaires des utilisateurs, l'interface de GitHub offre d'autres fonctionnalités visant à fournir quelques outils de gestion de projet.

L'une d'entre elles est **Projects**. C'est très nouveau dans l'écosystème et très rarement utilisé, mais c'est un **tableau Kanban** qui aide à organiser les problèmes et le travail à faire.

Le **Wiki** est destiné à être utilisé comme documentation pour les utilisateurs. L'une des utilisations les plus impressionnantes du Wiki que j'ai vues jusqu'à présent est le [Wiki GitHub du langage de programmation Go](https://github.com/golang/go/wiki).

Un autre outil populaire de gestion de projet est **milestones**. Il fait partie de la page des problèmes, et vous pouvez assigner des problèmes à des jalons spécifiques, qui pourraient être des cibles de publication.

En parlant de publications, GitHub a amélioré la fonctionnalité **Git tag** en introduisant **releases**.

Un Git tag est un pointeur vers un commit spécifique, et s'il est fait de manière cohérente, il vous aide à revenir à une version précédente de votre code sans référencer des commits spécifiques.

Une GitHub release s'appuie sur les Git tags et représente une publication complète de votre code, avec des fichiers Zip, des notes de publication et des actifs binaires qui peuvent représenter une version entièrement fonctionnelle du produit final de votre code.

Alors qu'un Git tag peut être créé de manière programmatique (par exemple, en utilisant le programme `git` en ligne de commande), la création d'une GitHub release est un processus manuel qui se fait via l'interface utilisateur de GitHub. Vous indiquez essentiellement à GitHub de créer une nouvelle release et vous leur dites quel tag vous souhaitez appliquer à cette release.

### Comparaison de commits

GitHub offre de nombreux outils pour travailler avec votre code.

L'une des choses les plus importantes que vous pourriez vouloir faire est de comparer une branche à une autre. Ou vous pourriez vouloir comparer le dernier commit avec la version que vous utilisez actuellement pour voir quels changements ont été apportés au fil du temps.

GitHub vous permet de faire cela avec la **vue de comparaison** : il suffit d'ajouter `/compare` à la fin du nom du dépôt.

Par exemple, [https://github.com/facebook/react/compare](https://github.com/facebook/react/compare)

![Image](https://cdn-media-1.freecodecamp.org/images/GBDt2fNQIOZS17JBdVo2ILLTQdu1wcF9FYxq)

Dans la figure ci-dessous, je compare la dernière **React v15.x** à la dernière version **v16.0.0-rc** disponible au moment de la rédaction de cet article pour voir ce qui a changé.

![Image](https://cdn-media-1.freecodecamp.org/images/NVNSfcKh3bIYmlM0wgG4qgJNLp9wwFcg8mqB)

Cette vue vous montre **les commits effectués** entre deux releases (ou tags ou références de commits) qui ont été modifiés, et **la diff réelle**, **si le nombre de changements est inférieur à une quantité raisonnable**.

### Webhooks et Services

GitHub offre de nombreuses fonctionnalités qui aident le flux de travail des développeurs, comme les webhooks et les services.

#### Webhooks

Les webhooks permettent aux services externes d'être pingés lorsque certains événements se produisent dans le dépôt, par exemple lorsque du code est poussé, qu'un fork est fait, ou qu'un tag a été créé ou supprimé.

Lorsque un événement se produit, GitHub envoie une requête POST à l'URL que nous lui indiquons d'utiliser.

Une utilisation courante de cette fonctionnalité est de pinger un serveur distant pour récupérer le dernier code de GitHub lorsque nous poussons une mise à jour depuis notre ordinateur local.

Nous poussons vers GitHub, GitHub informe le serveur que nous avons poussé, et le serveur tire de GitHub.

#### Services

Les services GitHub, et les nouvelles applications GitHub, sont des intégrations tierces qui améliorent l'expérience des développeurs ou vous fournissent un service.

Par exemple, vous pouvez configurer un exécuteur de tests pour exécuter les tests automatiquement chaque fois que vous poussez de nouveaux commits, en utilisant [TravisCI](https://travis-ci.org/).

Vous pouvez configurer l'intégration continue en utilisant [CircleCI](https://circleci.com/).

Vous pourriez créer une intégration [Codeclimate](https://codeclimate.com/) qui analyse le code et fournit un rapport de "Dette Technique" et de couverture de test.

### Mots de la fin

GitHub est un outil et un service incroyables à utiliser, un vrai joyau dans l'ensemble des outils des développeurs d'aujourd'hui. Ce tutoriel vous aidera à commencer, mais l'expérience réelle de travailler sur des projets GitHub open source (ou closed source) est quelque chose à ne pas manquer.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)