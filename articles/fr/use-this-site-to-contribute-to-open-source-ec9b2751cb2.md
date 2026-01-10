---
title: Utilisez ce site pour contribuer à l'open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T18:03:11.000Z'
originalURL: https://freecodecamp.org/news/use-this-site-to-contribute-to-open-source-ec9b2751cb2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6RUQ0iJ582gOm5HY
tags:
- name: coding
  slug: coding
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: Web Development
  slug: web-development
seo_title: Utilisez ce site pour contribuer à l'open source
seo_desc: 'By Jerry Muzsik

  When I began the transition into being a software developer, I knew that contributing
  to open source projects would greatly assist my job search.

  So, I jumped onto GitHub looking for issues that I could take on. Little did I know
  that...'
---

Par Jerry Muzsik

Lorsque j'ai commencé ma transition pour devenir développeur logiciel, je savais que contribuer à des projets open source m'aiderait grandement dans ma recherche d'emploi.

J'ai donc sauté sur GitHub à la recherche de problèmes que je pourrais résoudre. Je ne savais pas que *ce serait une entreprise misérable*.

### La Réalisation

Au début, je pensais que je pourrais simplement aller sur la page du dépôt de React (ou d'un autre dépôt extrêmement populaire) et trouver un problème.

Mais ces dépôts sont littéralement assaillis par des personnes à la recherche d'un problème. Et il est très chronophage de cliquer à travers les dépôts.

Ma deuxième pensée était d'utiliser la [recherche d'issues de GitHub](https://github.com/issues), mais j'ai rencontré plusieurs problèmes ici :

1. Vous ne pouvez pas filtrer les issues en fonction du nombre d'étoiles d'un dépôt
2. Vous ne pouvez filtrer par langue que si l'issue est littéralement étiquetée avec cette langue. (Donc, si le projet est principalement un dépôt JavaScript et que l'issue n'est pas étiquetée JavaScript, vous n'avez aucun moyen de la rechercher par langue.)

#### Comment regarder les issues axées sur les projets populaires ?

En gros, vous devez les connaître et les rechercher manuellement.

#### Comment trouver une issue d'un projet populaire dans la langue que vous connaissez le mieux ?

1. Comme dit précédemment, allez sur la page GitHub d'un projet en *apprenant son existence d'une manière ou d'une autre*
2. Parcourez les issues. Maintenant, vous pouvez filtrer un peu par étiquette (pensez bug, fonctionnalité, good-first-issue)
3. Si vous ne trouvez pas quelque chose que vous pouvez faire, vous devez recommencer ce processus avec un nouveau dépôt !

Inutile de dire que cela m'a pris une éternité pour trouver une issue que je voulais résoudre.

Quelques mois plus tard. J'ai commencé à créer un site web pour faciliter la contribution à l'open source.

### Le Processus de Création

![Image](https://cdn-media-1.freecodecamp.org/images/AAV4wgF5o3N1LUEYejtGeXOvW8KhYyrKQJa4)
_Photo par [Unsplash](https://unsplash.com/@luca_tism?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Luca Laurence</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Le principal défi était d'obtenir les données que je voulais. Je savais que je devais utiliser l'API GitHub.

Comme je l'ai dit plus tôt, lorsque vous recherchez une issue sur GitHub, vous ne pouvez pas rechercher par étoiles ou par langue. Cela vient du fait que la requête API Repo de GitHub ne fournit pas cette option.

Ma première pensée était que je devrais me concentrer sur la recherche de dépôts d'intérêt. Par exemple, les mille dépôts les plus étoilés en JavaScript, Python, et une variété d'autres langues.

*Eh bien... vous ne pouvez pas rechercher les dépôts par langue ni par nombre d'étoiles.*

Récupérer des données dynamiquement, c'est bien, mais comment pourrais-je le faire ? Voici une vue condensée de pourquoi c'est ridiculement difficile avec l'API GitHub.

#### Se Familiariser avec l'API GitHub

Une chose à commencer : vous avez une limite de 5000 requêtes par heure à l'API GitHub.

C'est la seule façon d'obtenir un tas de dépôts à la fois : [https://api.github.com/repositories](https://api.github.com/repositories) qui vous donnera environ 35 dépôts mais *aucune de ces lignes n'a de langue ou de nombre d'étoiles.*

Cependant, vous pouvez interroger chacun de ces dépôts retournés par la requête API initiale (ex. [https://api.github.com/repos/facebook/react](https://api.github.com/repos/facebook/react)) et **ensuite vous obtenez ces données !**

Mais attendez... je dois passer par chaque dépôt sur GitHub... il y a environ **90 millions** de dépôts.

#### **Un Peu de Maths**

90 257 000 (nombre de dépôts avec nombre de requêtes pour obtenir les dépôts) / 5000 (limite de taux horaire) ≈ 18 000 heures ou 750 jours ou environ 2 ans... ?

![Image](https://cdn-media-1.freecodecamp.org/images/lXGjTRFCUmD2w3-FP0p0EqrTGAuop07sldba)
_Photo par [Unsplash](https://unsplash.com/@kaip?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Kai Pilger</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### La Décision Prise à Contrecœur

J'ai donc dû trouver les dépôts manuellement... ?. Merci à ce site : h[ttps://gitstar-ranking.com/](https://gitstar-ranking.com/) mais quand même, quelques heures de clics à travers les dépôts...

Mais, j'y suis arrivé ! Et voici le site ! ?

### [FindanIssue.org](https://findanissue.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/LCdHAEC6UExXLxVSF6ojXRyWZcjmgAMcWA6O)
_Le site web incroyable_

Je l'ai rendu aussi simple que possible. Recherchez par dépôt exact, par langue spécifique (exacte et sensible à la casse), par étiquette, ou par l'âge de l'issue. Ainsi, vous pouvez aller à la racine de ce que vous cherchez.

Si vous êtes débutant, recherchez par des étiquettes telles que *good first issue* ou *docs/documentation* ainsi qu'en spécifiant votre langage de programmation de choix.

![Image](https://cdn-media-1.freecodecamp.org/images/Kapd7zRmeB0Ih47xJ-thgI-wleyKTo47lBfv)
_Exemple d'Issue pour Débutants_

Si vous êtes un développeur expérimenté à la recherche d'un défi, recherchez par des étiquettes telles que *feature*, *help wanted*, *bug*, ou d'autres étiquettes de votre choix.

![Image](https://cdn-media-1.freecodecamp.org/images/DZ6U9O8kPo0Q1zhANvILm2-bWno1ZOGtexGI)
_Recherche d'Issue Plus Avancée_

Pour le moment, les données sont actualisées deux fois par jour afin que les anciennes issues soient supprimées et que les issues qui ont été étiquetées reçoivent leur étiquette appropriée.

### Réflexions Finales

Il reste encore beaucoup de travail à faire :

* Le problème le plus flagrant est que seulement environ 900 projets sont présentés. Il y a donc un large éventail de projets incroyables qui ne sont pas mis en avant.
* Améliorer le backend et ajouter quelques éléments au frontend ferait vraiment la différence

En fin de compte, j'ai fait cela parce que je crois que c'est une étape vers la satisfaction d'un besoin dans la communauté open source de lier les issues aux développeurs. **Plutôt que de partir à l'aventure pour trouver une issue à résoudre, le site vise à en faire quelques minutes de recherche dans un tableau.**

J'espère que vous l'utiliserez et que vous vous retrouverez à redonner au monde de l'open source, dont vous, en tant que développeur, dépendez chaque jour.

![Image](https://cdn-media-1.freecodecamp.org/images/q9MweeUDqyg9Ucyvzvsp5x1Z3U7T5D9WMqoX)
_Photo par [Unsplash](https://unsplash.com/@pavement_special?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Riccardo Annandale</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> Voici le dépôt : [https://github.com/jMuzsik/find-an-issue](https://github.com/jMuzsik/find-an-issue)  
>   
> Et voici le site : [https://findanissue.org](https://findanissue.org/)

Et merci pour la lecture !