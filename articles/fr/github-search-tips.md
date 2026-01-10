---
title: Conseils de recherche GitHub – Comment rechercher des problèmes, des dépôts
  et plus efficacement sur GitHub
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2022-10-17T19:27:10.000Z'
originalURL: https://freecodecamp.org/news/github-search-tips
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Search--2-.png
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: search
  slug: search
seo_title: Conseils de recherche GitHub – Comment rechercher des problèmes, des dépôts
  et plus efficacement sur GitHub
seo_desc: "When I was a beginner to open-source contributions, one of my greatest\
  \ challenge was finding the correct projects/issues to work on. \nFor the longest\
  \ time I relied on resources curated by different writers on the internet (which\
  \ were good, by the way..."
---

Lorsque j'étais débutant dans les contributions open-source, l'un de mes plus grands défis était de trouver les bons projets/problèmes sur lesquels travailler.

Pendant longtemps, je me suis appuyé sur des ressources compilées par différents auteurs sur Internet (qui étaient bonnes, soit dit en passant). Mais j'ai toujours voulu trouver un moyen de contourner ce problème – une façon de rechercher et de suivre des projets adaptés à mes compétences.

Mettons-nous d'accord sur une chose : contrairement à Google, rechercher sur GitHub n'est pas facile. Mais en tant que développeur, il est probable que vous interagissiez avec GitHub ou GitLab au quotidien.

Maintenant, la question n'est pas de savoir ce pour quoi vous utilisez ces systèmes de contrôle de version, mais comment vous les utilisez. Tout comme maîtriser les compétences de recherche Google est essentiel pour tout utilisateur régulier d'Internet, je crois qu'il est également essentiel pour les développeurs d'apprendre à rechercher efficacement sur GitHub.

Dans cet article, nous allons examiner différentes techniques que vous pouvez utiliser pour rechercher correctement sur GitHub. Vous apprendrez comment rechercher à travers :

* Les problèmes et les demandes de tirage (Pull Requests)
* Les dépôts (Repositories)
* Les utilisateurs
* Les sujets (Topics)

Et plus encore. Commençons.


## Requêtes de recherche GitHub

Pour trouver des informations détaillées sur quelque chose sur Internet, vous devez avoir les bonnes compétences de recherche. Ce n'est pas différent avec GitHub – pour trouver des informations détaillées, vous pouvez utiliser des filtres, des tris et des techniques de recherche courants pour trouver facilement des problèmes et des demandes de tirage spécifiques d'un projet donné.

Même si vous avez plusieurs ressources répertoriées sur Internet pour différents projets, le principal problème survient lorsque vous souhaitez effectuer une recherche par vous-même. Comment commencez-vous ? Quels mots-clés devez-vous utiliser pour trouver les résultats corrects ?

La plupart des mainteneurs ont tendance à étiqueter leurs projets avec des problèmes, ce qui facilite la recherche de projets adaptés pour les contributeurs. Voici quelques astuces qui pourraient vous aider lorsque vous utilisez GitHub.

### Comment rechercher des problèmes et des demandes de tirage sur GitHub

L'une des méthodes les plus courantes pour trouver des projets auxquels contribuer est de rechercher à travers les problèmes et les PR associés. Voici quelques astuces que vous pouvez utiliser pour trouver facilement des réponses fiables :

1. **[is:issue is:open label:beginner](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3Abeginner&type=issues)** - Cette requête particulière listera tous les projets avec des problèmes ouverts et étiquetés `beginner`.
2. **[is:issue is:open label:easy](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3Aeasy&type=issues)** - Cela listera tous les problèmes ouverts étiquetés `easy`.
3. **[is:issue is:open label:first-timers-only](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3Afirst-timers-only&type=issues)** - Cela liste tous les problèmes ouverts qui accueillent les contributions des débutants.
4. **[is:issue is:open label:good-first-bug](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3Agood-first-bug&type=issues)** - Cela liste les projets avec des problèmes ouverts étiquetés `good-first-bug`, pour attirer les contributeurs à travailler dessus.
5. **[is:issue is:open label:"good first issue"](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22&type=issues)** - Cela listera tous les problèmes ouverts avec l'étiquette `good first issue`, ce qui signifie que c'est un bon endroit pour que les débutants commencent.
6. **[is:issue is:open label:starter](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3Astarter&type=issues)** - Cela liste tous les problèmes ouverts à travers GitHub qui sont étiquetés `starter`.
7. **[is:issue is:open label:up-for-grabs](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3Aup-for-grabs&type=issues)** - Cela liste les problèmes ouverts qui sont prêts à être travaillés si vous avez les compétences nécessaires.
8. **[no:project type:issue is:open](https://github.com/search?q=no%3Aproject+type%3Aissue+is%3Aopen&type=issues)** - Cela listera tous les problèmes ouverts qui ne sont pas assignés à un projet spécifique.
9. **[no:milestone type:issue is:open](https://github.com/search?q=no%3Amilestone+type%3Aissue+is%3Aopen&type=issues)** - Souvent, les projets sont suivis avec des jalons. Mais si vous voulez trouver des problèmes qui ne sont pas suivis, cette requête de recherche les listera pour vous.
10. **[no:label type:issue is:open](https://github.com/search?q=no%3Alabel+type%3Aissue+is%3Aopen&type=issues)** - Cela liste tous les problèmes ouverts qui ne sont pas étiquetés.
11. **[is:issue is:open no:assignee](https://github.com/search?q=is%3Aissue+is%3Aopen+no%3Aassignee&type=issues)** - Cela montre tous les problèmes ouverts qui n'ont pas encore été assignés à une personne.


### Comment rechercher des dépôts

Par défaut, pour effectuer une recherche, vous taper le nom du dépôt dans la barre de recherche et voilà ! Vous obtenez des résultats de recherche.

Mais les chances que vous tombiez sur le dépôt exact que vous visiez sont très faibles.

Examinons quelques façons de réduire votre recherche :

#### Comment trouver par nom, description/README

Une chose à noter lorsque vous recherchez par nom et description du fichier README est que votre phrase de recherche doit commencer par le qualificatif `in`. Cela permet de rechercher "à l'intérieur" de ce que vous cherchez.

**Exemple**

* Utilisation de `in:name`. Supposons que vous cherchez des ressources pour en savoir plus sur la science des données. Dans ce cas, vous pouvez utiliser la commande `Data Science in:name` qui listera les dépôts avec Data Science dans le nom du dépôt.

* Utilisation de `in:description`. Si vous voulez trouver des dépôts avec une certaine description, par exemple des dépôts où le terme "freeCodeCamp" est inclus dans la description, notre recherche sera : `freecodecamp in:description`

* Utilisation de `in:readme`. Vous utilisez cela pour rechercher dans un README d'un fichier une certaine phrase. Si nous voulons trouver des dépôts où le terme freecodecamp est inclus dans le README, notre recherche sera : `freecodecamp in:readme`.

* Utilisation de `in:topic`. Vous utilisez cela pour trouver si une certaine phrase ou un mot est étiqueté dans les sujets. Par exemple, pour trouver tous les dépôts où freecodecamp est listé dans le sujet, notre recherche sera : `freecodecamp in:topic`

Vous pouvez également combiner plusieurs requêtes de recherche pour affiner davantage la recherche.

#### Comment trouver par étoiles, forks

Vous pouvez également rechercher un dépôt en fonction du nombre d'étoiles et de forks que le projet a. Cela vous permet de savoir à quel point le projet est populaire.

**Exemples**

* Utilisation de `stars:n`. Si vous recherchez un dépôt avec 1000 étoiles, alors votre requête de recherche sera `stars:1000`. Cela listera les dépôts avec exactement 1000 étoiles.

* Utilisation de `forks:n`. Cela spécifie le nombre de forks qu'un dépôt doit avoir. Si vous voulez trouver des dépôts qui ont moins de 100 forks, votre recherche sera : `forks:<100`.

Le bon côté est que vous pouvez toujours utiliser des opérateurs relationnels comme `<`, `>`, `<=`, `>=` & `..` pour vous aider à affiner davantage votre recherche.

#### Comment trouver par langage

Une autre façon cool de rechercher sur GitHub est par langage. Cela vous aide à filtrer les dépôts pour un langage spécifique.

**Exemple :**

* Utilisation de `language:LANGUAGE`. Par exemple, si vous voulez trouver des dépôts écrits en PHP, votre recherche sera : `language:PHP`

#### Comment trouver par nom d'organisation

Vous pouvez également rechercher des dépôts/projets qui sont maintenus ou créés par une organisation spécifique. Pour cela, vous devez commencer votre recherche avec le mot-clé `org:...` suivi du nom de l'organisation.

Par exemple, si vous recherchez `org:freecodecamp`, cela listera les dépôts qui correspondent à freeCodeCamp.

#### Comment trouver par date

Si vous voulez vos résultats basés sur une date spécifique, vous pouvez rechercher en utilisant l'un de ces mots-clés : `created`, `updated`, `merged` et `closed`. Ces mots-clés doivent être accompagnés d'une date au format `YYYY-MM-DD`.

**Exemple :**

* Utilisation de `keyword:YYYY-MM-DD`. Prenons un cas où nous voulons faire une recherche de tous les dépôts avec le mot freeCodeCamp qui ont été créés après le 2022-10-01. Alors notre recherche sera : `freecodecamp created:>2022-10-01`

Vous pouvez également utiliser `<`, `>`, `>=` et `<=` pour rechercher des dates après, avant et à la date spécifiée. Pour rechercher dans une plage, vous pouvez utiliser `...`.

#### Comment trouver par licence

Les licences sont très importantes lorsque vous cherchez un projet auquel contribuer. Différentes licences donnent différents droits quant à ce qu'un contributeur peut faire ou ne pas faire.

Pour vous faciliter la recherche de projets avec les bonnes licences, vous devez avoir une bonne compréhension des licences. Vous pouvez en lire plus à ce sujet [ici](https://www.freecodecamp.org/news/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94/).

**Exemple :**

* Utilisation de `license:LICENSE_KEYWORD`. C'est une bonne façon de rechercher des projets avec des licences spécifiques. Pour rechercher des projets avec la licence MIT, par exemple, vous feriez `license:MIT`.

#### Comment trouver par visibilité

Vous pouvez également effectuer votre recherche en termes de visibilité du dépôt. Dans ce cas, vous pouvez utiliser public ou privé. Cela correspondra aux problèmes et PR qui sont soit dans un dépôt public ou privé, respectivement.

**Exemples :**

* Utilisation de `is:public`. Cela affichera une liste de dépôts publics. Prenons un cas où nous voulons rechercher tous les dépôts publics détenus par freeCodCamp. Alors notre recherche sera : `is:public org:freecodecamp`.
* Utilisation de `is:private`. Cette requête est destinée à lister tous les dépôts privés sous la requête de recherche donnée.

## Conclusion

Même si nous avons couvert de nombreuses requêtes de recherche ici, vous pouvez toujours être créatif pour affiner davantage votre recherche en combinant plusieurs paramètres ensemble.

Pour des ressources supplémentaires et plus de paramètres de recherche, vous pouvez toujours vous référer à la [Documentation GitHub](https://docs.github.com/en/search-github/searching-on-github) ou utiliser la [Recherche Avancée GitHub](https://github.com/search/advanced?). Ces méthodes seront toujours utiles car elles offrent plus d'options de filtrage.

Il existe une tonne de paramètres de recherche que vous pouvez utiliser pour faciliter votre activité quotidienne autour de GitHub. Espérons que cela vous aidera à utiliser la plateforme plus facilement et efficacement.