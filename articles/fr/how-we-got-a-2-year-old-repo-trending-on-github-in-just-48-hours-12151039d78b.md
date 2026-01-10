---
title: Comment nous avons fait tendre notre dépôt de 2 ans sur GitHub en seulement
  48 heures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-27T20:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D2NgKZ1T7LYXrFPAXnorTg.jpeg
tags:
- name: open source
  slug: open-source
- name: Python
  slug: python
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment nous avons fait tendre notre dépôt de 2 ans sur GitHub en seulement
  48 heures
seo_desc: 'By Abhinav Suri

  Github has made it easy for millions of developers to publicize their projects so
  they can attract users and collaborators. But these developers often find themselves
  spending hundreds of hours building a project, only to push it to G...'
---

Par Abhinav Suri

GitHub a facilité la tâche pour des millions de développeurs de publiciser leurs projets afin qu'ils puissent attirer des utilisateurs et des collaborateurs. Mais ces développeurs se retrouvent souvent à passer des centaines d'heures à construire un projet, pour finalement le pousser sur GitHub et n'obtenir qu'une ou deux étoiles.

Je me suis retrouvé dans cette situation en construisant un projet pour l'organisation à but non lucratif pour laquelle je travaille, [Hack4Impact](http://hack4impact.org). C'est un groupe d'étudiants qui réalise des [projets techniques](http://hack4impact.org/projects) pour des organisations communautaires.

Ensemble, nous avons construit **flask-base**, qui sert de code boilerplate pour tous nos produits. Il contient quelques éléments de base d'une application web Flask : SQLAlchemy, une file d'attente Redis et une authentification utilisateur (entre autres fonctionnalités).

Vous pouvez consulter notre dépôt [ici](http://github.com/hack4impact/flask-base).

![Image](https://cdn-media-1.freecodecamp.org/images/BLHOInuJm2T8C3krWCqvAf6DofNf9bGGvhpi)
_Une démo du backend admin sur flask-base_

Le grand avantage de flask-base est qu'il est "plug and play". Vous n'avez pas besoin de faire beaucoup de configuration pour obtenir une version exécutable sur votre machine (et il est très facile de le faire fonctionner sur des services d'hébergement comme Heroku). De plus, il est assez minimaliste par rapport à beaucoup d'autres applications boilerplate, ce qui laisse beaucoup de place pour la personnalisation.

Flask-base est en développement depuis deux ans, et il nous a aidés à former le boilerplate pour environ 90 % des projets techniques que nous entreprenons. Ce projet a permis de créer des produits pour des organisations comme [Kiva](http://hack4impact.org/projects/kiva), [OSET](http://hack4impact.org/projects/oset), [Juvenile Law Center](http://hack4impact.org/projects/m4a-jlc-sp2) et [Givology](http://hack4impact.org/projects/givology).

Flask-base nous a permis d'aider des organisations communautaires à travers les États-Unis à atteindre l'impact social qu'elles recherchent. Mais malgré nos efforts pour publiciser notre code sur divers canaux, flask-base est resté inconnu de tous, sauf d'une poignée de personnes qui y travaillaient.

![Image](https://cdn-media-1.freecodecamp.org/images/jgcNier6G38GNjs2uMv0emQP4NR5WyCyAZ6v)
_Les vieux jours_

Nos efforts infructueux nous ont menés à la frustration parce que nous avions l'impression que d'autres développeurs et petites organisations pourraient utiliser flask-base pour des projets tout aussi impactants. Mais nous n'arrivions tout simplement pas à comprendre comment faire connaître le produit. En conséquence, nous avons commencé à remettre en question l'équité d'un médium open source **qui était censé faire émerger les grandes idées**.

![Image](https://cdn-media-1.freecodecamp.org/images/ctLZIFvr99pz8PPii8zPbShb8IshmgEktsMl)
_Comment se sent le fait de rendre un projet open source. ([source](http://gifrific.com/wp-content/uploads/2012/04/gob-letter-throw.gif" rel="noopener" target="_blank" title="))_

Mais ensuite, nous avons découvert ce qui n'allait pas dans notre approche. Nous avons examiné attentivement comment l'open source fonctionne du point de vue de l'_utilisateur_. Nous avons remarqué des domaines clés à corriger et amélioré notre projet pour le rendre prêt à être utilisé dans le monde réel.

**Ensuite, nous avons eu notre moment.** J'ai posté notre projet sur le subreddit [/r/Python](http://reddit.com/r/python), et il a obtenu un peu de traction. Nous avons décidé de continuer. En l'espace de 48 heures, notre dépôt est passé de 9 étoiles à plus de 200. Et il a continué à croître.

Soudainement, nous avons commencé à recevoir des commentaires et des suggestions de personnes intéressées par le projet. **C'était incroyable.**

![Image](https://cdn-media-1.freecodecamp.org/images/54Nj8ZBBDDVUK8Hc-qgZbNtArt12gcHPQOoF)
_les vieux jours += 544 étoiles, 74 forks et 16 watches_

Cet article explique comment nous avons fait connaître flask-base. Si vous avez un projet impactant à partager, vous pouvez mettre en œuvre nos suggestions, (espérons-le) vous faire remarquer dans l'univers open source et en tirer le meilleur parti.

### Tout commence par la recherche

Nous avons commencé à examiner des exemples de succès. Les dépôts populaires sur GitHub ont tendance à avoir quelques caractéristiques en commun :

* Un README avec des images/gifs du produit en action
* De la documentation
* Une analyse statique du code
* Des instructions pour contribuer
* Une section de configuration bien définie
* _Un logo (complètement optionnel)_

![Image](https://cdn-media-1.freecodecamp.org/images/pZgAcHMkfMEVcx2GnGERZfvqDKVU4hKShxIT)
_Découpage des premières lignes d'un README_

Quelques excellents exemples de dépôts GitHub à examiner :

* [React-Router](https://github.com/ReactTraining/react-router) : 19k+ étoiles, 4,5k+ forks. En plus d'être utile pour gérer les applications web monopage, React Router est l'un des rares dépôts avec un tutoriel dédié sur l'utilisation du framework. Il dispose également d'un guide de configuration complet ainsi que des références aux erreurs que les utilisateurs peuvent rencontrer.
* [Webpack](https://github.com/webpack/webpack) : 23,5k+ étoiles, 2,7k+ forks. Webpack est sans doute l'un des meilleurs outils pour le développement web front-end moderne en raison de sa fiabilité et de sa capacité à couvrir la construction pour de nombreuses versions de navigateurs différentes. Le README témoigne certainement de cela avec des dizaines de badges et des cas d'utilisation exemples ainsi que des liens vers la documentation. Webpack met également l'accent sur le rôle de la communauté dans le maintien du projet (notamment en ayant des sections dédiées aux sponsors et aux soutiens).

Et un mauvais exemple de dépôt GitHub :

* [abhisuri97/leARn](https://github.com/abhisuri97/leARn) : Oui... Je cite l'un de mes propres dépôts comme mauvais exemple. Ce dépôt était pour un projet de hackathon que j'ai réalisé et qui a remporté le PennApps XIII VR/AR et a été classé dans le Top 10. C'était ma première et seule fois en développement avec Unity, d'où le grand nombre de fichiers qui sont superflus et n'ont pas besoin d'être commités. Bien qu'il y ait une excellente explication de ce que fait le projet, il n'explique pas comment le faire fonctionner sur le système de quelqu'un ou quelles sont les fonctionnalités.

Après avoir examiné plusieurs dizaines de dépôts et surveillé les tendances pendant quelques jours, nous avons saisi une idée cruciale que tous les dépôts populaires abordaient : **Si je suis un développeur qui regarde votre dépôt, donnez-moi une raison d'utiliser votre projet et rendez-le aussi simple que possible à configurer.**

### L'A.G.D. (Dispositif d'Attention)

![Image](https://cdn-media-1.freecodecamp.org/images/fIRQNOiQASCICiLLanvQLP2mBhaur61Ti47v)
_[Source de l'image](https://media.licdn.com/mpr/mpr/p/5/005/08b/07a/348caff.jpg" rel="noopener" target="_blank" title=")_

#### Éloquence et README :

À l'époque où je participais à des compétitions d'éloquence au lycée, je participais à un événement appelé Original Oratory. C'était un discours de 10 minutes que vous écriviez et performiez devant un juge. Chaque oratoire que je donnais commençait par un A.G.D. (dispositif d'attention) de 2 minutes. Habituellement, c'était une histoire suivie d'une thèse pour le discours, et un aperçu des points que j'allais aborder.

Eh bien... **Les README sont l'A.G.D. de votre projet !**

Les README sont la première chose que votre visiteur verra en regardant votre dépôt. Vous devriez donc vous assurer que votre README contient des informations essentielles sur votre projet.

Mais qu'est-ce qui est crucial ? Comment attirer l'attention de votre visiteur ?

Lorsque quelqu'un regarde votre projet, il veut savoir :

* ce que c'est
* à quel point le code est bon
* combien de support est disponible
* ce qui est inclus
* à quoi cela ressemble
* et comment ils doivent procéder pour le configurer.

Abordons chacune de ces questions.

#### Qu'est-ce que c'est ?

![Image](https://cdn-media-1.freecodecamp.org/images/GUHe211hrVkMcCTtmCbP8GvmXBOS6RPe4DBR)
_Un grand logo répondra rapidement à la question de savoir ce qu'est le dépôt_

C'est une question assez simple à répondre pour la plupart des dépôts, mais beaucoup de gens se trompent. Votre projet est l'un parmi des millions. Vous avez peu de temps pour faire une impression.

**Décrivez votre projet en un tweet (environ 140 caractères).** Il est acceptable de laisser de côté les détails. C'est à cela que sert la section des fonctionnalités. Un logo aide également, car il distinguera le nom de votre projet du texte noir et blanc du README (et montre également que vous avez fait un effort pour créer un logo).

#### À quel point le code est-il bon ?

Cette question est probablement celle à laquelle 90 % des dépôts ne répondent pas. Bien que la définition de "bon" code soit subjective, il y a quelques aspects sur lesquels les gens peuvent s'accorder.

* Il est bien testé
* Il passe les vérifications de style (ESLint, etc.)
* Il peut compiler dans son état actuel (et il y a relativement peu de problèmes)
* Il passe une forme d'analyse statique (via des services tels que Code Climate)

![Image](https://cdn-media-1.freecodecamp.org/images/2zBTWhTh6Z7oTG0Y-HYaVRstkoRPrDbf4pkg)
_Le tableau de bord de Code Climate vous donne une moyenne pour la qualité du code_

![Image](https://cdn-media-1.freecodecamp.org/images/P4vqfjXlQswYYiYpeCRCbP-AKYXBewYIM1A9)
_Les badges GitHub sur flask-base_

Aucun développeur ne va regarder votre code ligne par ligne pour voir s'il est bon _avant_ de décider d'utiliser votre projet. D'où les "badges" qui apparaissent sur la première ligne d'un projet. Le grand avantage de ces badges est qu'ils sont ridiculement faciles à configurer et donnent beaucoup de crédibilité à votre projet sans que les visiteurs aient à regarder votre code du tout.

#### Combien de support est disponible ?

Le support se présente sous deux formes : le support pour les problèmes et le support pour apprendre à utiliser le projet.

Le support pour les problèmes peut être résolu via une FAQ. Mais pour les nouveaux projets, les gens ne savent pas quels bugs peuvent se cacher dans les profondeurs du vieux code (et donc peuvent ne pas avoir de contenu pour une FAQ). La seule façon de démontrer ce type de support est de traiter les problèmes au fur et à mesure qu'ils se présentent et de les résoudre rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/7GIYlJSDEVlCwAjQEsrls--pcJdMNwoLm5KP)
_La documentation de flask-base générée avec mkdocs. [Voir nos docs](http://hack4impact.github.io/flask-base" rel="noopener" target="_blank" title=")._

La deuxième forme de support peut être abordée via la documentation. Cette tâche est un point de douleur majeur pour les développeurs, mais elle est **critique** pour la popularité de votre projet (et elle devrait être faite à un moment donné de toute façon).

Les docs sont faciles à créer avec [mkdocs](http://www.mkdocs.org/), et vous pouvez générer un site gh-pages à partir de la CLI mkdocs, que vous pouvez ensuite héberger gratuitement sur GitHub.

Une bonne documentation donnera à vos utilisateurs des exemples de comment utiliser le programme et expliquera les composants difficiles. Elle devrait également donner un guide détaillé de comment lancer le projet (s'il s'agit d'une application web).

#### Qu'est-ce qui est inclus ?

![Image](https://cdn-media-1.freecodecamp.org/images/fiGY9TEwS1hsrFbKUXAWC3X0jWiVm2MD4Zjx)
_X pour Y_

Une liste de fonctionnalités ne doit pas être exhaustive, mais doit lister les fonctionnalités qui sont centrales à votre application et qui sont accessibles (et démontrables). Au maximum, cette liste doit comporter 10 fonctionnalités et être au format "(Utilisé) X pour la fonctionnalité Y."

#### À quoi cela ressemble-t-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/a-30NemlCoow2pE1HNweUjEIhfOVqINzTbvF)
_Démonstration de la fonctionnalité d'édition de la page admin de flask-base_

Si une image vaut mille mots, alors un .gif vaut un million. Montrez **comment** votre application fonctionne — même si cela signifie montrer la sortie de la ligne de commande. Cette information donne au développeur qui regarde votre projet une idée de a) à quoi il est censé ressembler, et b) s'il répond à leurs besoins.

**Ne sous-estimez jamais combien une bonne image convaincra un développeur d'utiliser votre projet.**

#### Comment le configurer ?

![Image](https://cdn-media-1.freecodecamp.org/images/N6ehmetn6-yGeNXcTiKuw8S1wRjq52p1EuGM)
_Nos instructions de configuration_

Lors du développement, il est probable que vous travailliez sur le projet sur un seul ordinateur avec tout installé. **Mais vous devez fournir un moyen de permettre à un utilisateur de se configurer et de fonctionner avec votre projet en 3-4 étapes.** Si cela signifie créer un MakeFile, faites-le. Assurez-vous également de mentionner tous les outils "globaux" que vous avez utilisés, comme _babel-cli_ et _babel-core_.

En règle générale, si vous avez dû l'installer, il est probable que quelqu'un d'autre doive le faire également. Assurez-vous également de compresser tous vos scripts en un seul fichier d'installation (pour Python, ce serait _requirements.txt_ et pour Node/JavaScript, ce serait _package.json_). En bref, quelqu'un devrait pouvoir faire fonctionner votre projet en moins de 5 minutes.

### Atteindre les tendances :

Ainsi, un excellent dispositif d'attention (aka README) vous aidera à retenir vos visiteurs. Mais comment attirer des visiteurs vers votre projet en premier lieu ?

Il existe 3 principaux canaux que vous pouvez utiliser :

![Image](https://cdn-media-1.freecodecamp.org/images/0mLp1vKDsrZU0fNaT3IGfLXlRs6t9n5rNvOH)

![Image](https://cdn-media-1.freecodecamp.org/images/kK-7J5Qd-vFdYK2xk1WvorfGZLyhK6lpVjgc)

![Image](https://cdn-media-1.freecodecamp.org/images/g9rM6F6R0pPBKi4Dx-9dTbYnnMLHHLsZ6aQ6)
_Hacker News, Product Hunt, Reddit (images provenant de leurs kits de presse respectifs)_

**Hacker News/Product Hunt :** Les deux offrent d'excellents moyens d'exposer le projet à une communauté engagée de développeurs (et vous pouvez obtenir une couverture médiatique). Mais le problème est que pour que votre publication atteigne le sommet de l'un ou l'autre, cela nécessite une planification significative et quelques utilisateurs prêts à aider à promouvoir votre publication dès le début.

**Reddit :** De loin la meilleure façon de lancer un dépôt avec quelques étoiles. **Mais vous devez trouver la bonne communauté.** Pour flask-base, cette communauté était [/r/Python](http://reddit.com/r/python), où nous avons atteint le sommet des publications du jour sans trop d'efforts.

La clé est de rejoindre une communauté qui se souciera de votre projet (et qui l'utilisera). Mais vous devriez être prudent lorsque vous publiez dans des subreddits très génériques comme /r/Programming où il y a des tonnes de publications concurrentes qui noieront la vôtre.

![Image](https://cdn-media-1.freecodecamp.org/images/f0kSgxadmXWkGda8W6DhBDlDlva57OUA5wqu)
_[Veronica Wharton](undefined" rel="noopener" target="_blank" title=") et moi enseignant un atelier Flask à PennApps XV_

**Ateliers :** C'est aussi un "secret", mais les ateliers sont un excellent moyen d'obtenir vos premières dizaines d'étoiles sur votre dépôt. Donnez un atelier sur la façon dont vous avez créé votre projet, ce qu'il fait, et **surtout**, montrez comment l'utiliser (avec un exemple).

Nous l'avons fait à PennApps XV en enseignant un atelier sur la façon de créer des applications web avec Flask. La participation était d'environ 40 personnes, et nous avons présenté flask-base comme un exemple d'application Flask qu'ils pouvaient utiliser pendant le hackathon. Cinq minutes après la fin de notre atelier, nous avons vérifié le dépôt et avons découvert qu'**il avait obtenu 17 étoiles et huit forks**. Ce sentiment était incroyable :)

### Surveillance du statut

![Image](https://cdn-media-1.freecodecamp.org/images/HrttJjG5ip25iZx29wogVzfgJ4JMYQUXrBcS)
_Adresser les commentaires d'amélioration. Soyez gentil, justifiez vos opinions et accueillez les contributions des autres._

Inévitablement, il y aura quelqu'un qui signalera un bug/incohérence après le lancement. Assurez-vous simplement de répondre à ces personnes, de répondre à tous les commentaires et de prendre en compte tous les retours. **Rester engagé avec votre audience est la clé pour vous assurer que l'audience est investie dans votre projet.**

Une fois que vous obtenez une croissance initiale de 30 à 40 étoiles en peu de temps (1-2 heures), votre projet aura une bonne chance d'apparaître dans les tendances. (Bien sûr, je ne peux pas parler des spécificités du fonctionnement de l'algorithme de tendance de GitHub.)

![Image](https://cdn-media-1.freecodecamp.org/images/hXTZFMMbtiUOJIE6lfqaqfmWSuYhq4s-69sC)
_Flask-base en tête des tendances pour les dépôts Python sur GitHub après 24 heures_

### Quelques-unes de nos réalisations

Flask-base a atteint le **top des tendances quotidiennes** pour les dépôts Python, le **top 3 des tendances globales** et le **top de /r/Python** de la semaine.

Hack4Impact est devenu le **4ème développeur Python le plus en tendance** et le **5ème développeur global le plus en tendance**.

De plus, nous avons eu **80+ clones** et **40+ forks** à ce jour.

En tant qu'étudiant en informatique, c'est incroyable de voir que les gens utilisent le code que j'ai aidé à écrire.

![Image](https://cdn-media-1.freecodecamp.org/images/uikuXB9fqthd7TyOWp-Hmq8d0yN0TMVBRftK)
_Une lettre de remerciement que j'ai reçue._

![Image](https://cdn-media-1.freecodecamp.org/images/rAhGSXvJx5F6mU6w-xBRkGnxRc2VcIjhzu3u)
_Nos analyses sur GitHub. Reddit a été vraiment utile._

Si vous n'atteignez pas votre objectif de devenir tendance, ne vous inquiétez pas. Il suffit de recommencer. Parfois vous aurez de la chance, parfois non.

Si vous faites un effort pour créer du code open source que vous pensez que les autres trouveront utile, vous contribuerez au monde de l'open source. Vous tirerez le meilleur parti de tout ce que l'open source a à offrir.

### Remerciements

Un grand merci à [Alex Piatski](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), [Veronica Wharton](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), [Emmett Neyman](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), Stephanie Shi et [Ben Sandler](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined) pour leurs contributions à cet article. Merci aux développeurs de flask-base ([Ben Sandler](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), [Yoni Nachmany](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), [Max McCarthy](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), [Veronica Wharton](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined), Alex Harelick, Nancy Wong et [Annie Meng](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined)) pour avoir fait de ce projet un grand projet.

Enfin, merci à [Hack4Impact](https://www.freecodecamp.org/news/how-we-got-a-2-year-old-repo-trending-on-github-in-just-48-hours-12151039d78b/undefined) de m'avoir permis de faire partie d'une communauté aussi socialement impactante.

Si vous souhaitez en savoir plus sur flask-base, [**visitez le dépôt**](http://github.com/hack4impact/flask-base)**.**

Si vous souhaitez découvrir certains des projets réalisés avec flask-base, [**visitez la page des projets de Hack4Impact**](http://hack4impact.org/projects).

Si vous souhaitez en savoir plus sur Hack4Impact (aka l'organisation qui a créé flask-base), [**visitez notre site web**](http://hack4impact.org).

Si vous souhaitez en savoir plus sur moi, visitez mon [**site personnel**](http://abhinavsuri.com), mon [**GitHub**](http://github.com/abhisuri97), ou envoyez-moi un email à [**suria@seas.upenn.edu**](mailto:suria@seas.upenn.edu).