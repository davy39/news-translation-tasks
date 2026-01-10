---
title: Est-ce qu'un diplôme en informatique booste vraiment votre salaire ? J'ai analysé
  les chiffres pour le savoir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T23:48:48.000Z'
originalURL: https://freecodecamp.org/news/does-an-undergrad-computer-science-education-affect-a-web-developer-s-salary-80711fff9298
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QAU9qepvrMDis8FJuX0Pdw.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Est-ce qu'un diplôme en informatique booste vraiment votre salaire ? J'ai
  analysé les chiffres pour le savoir.
seo_desc: 'By Leigh Silverstein

  I was in the middle of writing an article about the correlation of specialization
  to salary in the software industry. I had worked out the theory of why and how specialization
  affects salary, and where specialization tends to occ...'
---

Par Leigh Silverstein

J'étais en train d'écrire un article sur la corrélation entre la spécialisation et le salaire dans l'industrie du logiciel. J'avais élaboré la théorie sur le pourquoi et le comment de l'influence de la spécialisation sur le salaire, et là où la spécialisation a tendance à se produire. La seule chose dont j'avais besoin était une preuve statistique.

J'ai donc pris les [données de l'enquête Stack Overflow 2017](https://insights.stackoverflow.com/survey/2017), je les ai nettoyées et j'ai commencé à introduire des variables issues d'analyses précédentes qui étaient [connues pour affecter le salaire final](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/).

L'une des parties les plus délicates de l'analyse de données est de comprendre quelles variables vous voulez tester et lesquelles vous ne voulez pas. De cette façon, vous pouvez contrôler leur comportement.

Par exemple, je pourrais tester si l'utilisation de PHP au travail augmente votre salaire. Mais si je ne tenais pas compte du pays des répondants, je ne pourrais pas rendre compte fidèlement de l'influence de PHP.

Comme je testais la spécialisation, je devais simplifier le jeu de données et améliorer la sensibilité aux changements de spécialisation. J'ai choisi d'utiliser uniquement des développeurs web professionnels des États-Unis et, pour tenir compte de la spécialisation, je cherchais à tester les salaires des spécialistes frontend et backend par rapport aux généralistes full-stack.

J'ai progressivement ajouté des variables : Expérience, Éducation, Type de développeur web. Les résultats n'étaient pas parfaits. Je m'attendais à ce que l'éducation formelle ait une influence plus positive, mais j'étais optimiste et je voyais déjà quelques preuves de l'avantage de la spécialisation.

Et c'est là que quelque chose d'inattendu s'est produit.

Je suis développeur web de métier et je fais du développement full-stack. J'ai toujours supposé que si j'avais été un peu plus mature et que j'avais obtenu un diplôme en informatique (CS) au lieu d'un diplôme en beaux-arts, je gagnerais peut-être beaucoup plus d'argent.

L'un de mes frères cadets a un diplôme en informatique, et nos salaires semblent être sur deux échelles différentes, et ces échelles ne se rejoindront jamais. À tous ceux que je rencontre et qui s'intéressent à la programmation, je dis toujours qu'un diplôme d'informatique de premier cycle vaut au minimum une différence de salaire de 20 000 $ à perpétuité, et je pense être conservateur.

Vous pouvez donc imaginer mon choc lorsque j'ai effectué l'analyse pour les diplômés de premier cycle en informatique par rapport à tous les autres. **Il n'y avait pas de différence significative.**

« J'ai sûrement fait une erreur », ai-je pensé. La première fois que j'ai lancé l'analyse, j'avais regroupé les diplômés en informatique avec les ingénieurs, les mathématiciens et les diplômés en technologies de l'information. Clairement, l'informatique devait être séparée dans sa propre division.

J'ai donc relancé l'analyse.

Mais encore une fois, il n'y avait pas de différence significative.

![Image](https://cdn-media-1.freecodecamp.org/images/9gus9Ht0EpJUUXSr336yImPd3Z1cC7TdDrQg)
_Régression linéaire sur les facteurs qui affectent le salaire des développeurs web américains professionnels_

### Laissez-moi vous expliquer exactement ce qui se passait ici.

Lorsque j'ai pris en compte l'éducation formelle, l'expérience, le type de développeur web et la majeure de premier cycle, **il n'y avait aucune corrélation** entre le fait d'avoir une majeure en informatique — ou une majeure en ingénierie ou en mathématiques — et le salaire.

J'ai donc commencé à supprimer des variables. « Peut-être que les majors en informatique s'orientent généralement vers le backend », ai-je pensé. J'ai donc supprimé le type « développeur web ». Aucune corrélation.

J'ai supprimé l'éducation formelle complètement. Pas de vérification pour une licence, un master ou un doctorat. Aucune corrélation.

### J'ai essayé toutes les combinaisons imaginables. Et je n'ai pas pu trouver de lien significatif entre le fait d'avoir un diplôme de premier cycle en informatique et un salaire plus élevé.

Il existe plusieurs explications possibles à l'absence de pertinence statistique concernant le diplôme de premier cycle en informatique et le salaire. La première chose qui vient à l'esprit est que les données sont mauvaises. Ce n'était pas un échantillonnage correct de la population, ou les gens ont menti, ou les gens n'ont pas rempli l'enquête.

Nous savons, par exemple, que les femmes étaient sous-représentées dans les [conclusions initiales](https://medium.com/@glitterwitch/stack-overflow-s-developer-survey-analysis-hurts-women-ec4d568e2352). Nous pouvons également voir que seul un tiers des répondants développeurs web professionnels américains ont réellement inclus leur salaire, et parmi ceux qui l'ont inclus, la majorité se situait dans la fourchette de salaire annuel de 90 000 $ à 130 000 $ US.

Nous savons que le salaire moyen national d'un développeur web est [plus proche de 70 000 $](https://www.bls.gov/oes/current/oes151134.htm). Il y a donc un biais possible ici, où les gens ne signaleraient leur salaire que s'ils en étaient fiers.

J'ai donc testé cette hypothèse en attribuant à tous les salaires N/A un salaire inférieur à la moyenne de 40 000 $. J'ai découvert que cela brisait toutes les corrélations précédentes et n'entraînait aucune nouvelle révélation.

Une autre possibilité était que les diplômés de premier cycle formés en informatique s'orientent vers autre chose que le développement web, laissant les traînards pour le développement web. C'est tiré par les cheveux, je sais, mais j'essaie vraiment d'aller au fond des choses.

Les statistiques sont autant un art qu'une science. Il est assez facile de faire des régressions sur des données et de trouver des corrélations, mais parfois cela revient simplement à la logique de l'ensemble. Entre des mains malhonnêtes, les statistiques peuvent être utilisées pour transmettre des contrevérités.

> « Il y a trois sortes de **mensonges** : les **mensonges**, les **sales mensonges et les statistiques**. » — Mark Twain

En repensant à la première régression linéaire, j'ai remarqué une question concernant les répondants qui étaient allés à l'université, mais n'avaient pas obtenu de diplôme. Un pourcentage impressionnant de 14 % des répondants étaient des étudiants qui n'avaient pas terminé leurs études.

La variable était insignifiante, mais l'effet estimé était fortement négatif. Et si certains des étudiants qui abandonnaient le collège et l'université étaient des majors en informatique ?

J'ai créé deux variables d'interaction : une pour les étudiants en informatique ayant terminé leur licence, et une autre pour les étudiants en informatique ayant terminé leur master. Les résultats étaient significatifs et très positifs. Il semblait qu'avoir un diplôme de premier cycle en informatique affectait bel et bien le salaire.

![Image](https://cdn-media-1.freecodecamp.org/images/0vl-VGnI1J3I7PYLVg6TE6FAXXNjXliZrcE5)
_Régression linéaire sur les facteurs qui affectent le salaire des développeurs web américains professionnels avec des variables d'interaction informatique_

Ou est-ce le cas ? Regardez les effets d'avoir fait une majeure en informatique et d'avoir terminé une licence en informatique. Les signes sont presque équivalents. À peine mille points de différence.

D'un autre côté, avoir un diplôme de premier cycle en informatique avec un master valait 10 000 $ de plus. **Donc, si vous êtes intéressé par le développement web et que vous avez déjà un diplôme de premier cycle en informatique, vous pourriez envisager de faire un master.**

Je suis donc presque revenu à mon point de départ. Avoir un diplôme en informatique affecte le salaire, mais les effets sont loin de mon hypothèse initiale d'un boost de 20 000 $.

Au lieu de cela, c'est plus proche de 1 000 $ — ce qui, pour la plupart des développeurs ayant répondu à l'enquête avec leur salaire, signifie **une différence de moins de 2 % du revenu total.**

Maintenant, peut-être que cela me choque parce que je suis Canadien, et que nous avons tendance à être un peu plus réservés lorsqu'il s'agit de passer au crible les CV. Peut-être qu'un diplôme en informatique vaut plus ici. Et peut-être qu'il vaut plus dans beaucoup d'endroits dans le monde. Mais les diplômes en informatique ne semblent pas affecter les salaires des développeurs web professionnels aux États-Unis.