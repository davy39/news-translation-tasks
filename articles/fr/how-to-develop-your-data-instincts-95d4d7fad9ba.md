---
title: Comment aiguiser vos instincts de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-10T00:05:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-data-instincts-95d4d7fad9ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZO-U46F8hKDPxbPSdW2HCA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Productivity
  slug: productivity
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
seo_title: Comment aiguiser vos instincts de données
seo_desc: 'By Peter Gleeson

  With recent advances in machine learning and AI research making headlines on a regular
  basis these days, it’s little surprise that data science has become an area of real
  mainstream interest.

  It certainly makes a great career choice ...'
---

Par Peter Gleeson

Avec les avancées récentes en apprentissage automatique et en recherche sur l'IA faisant régulièrement la une des journaux ces jours-ci, il n'est pas surprenant que la science des données soit devenue un domaine d'intérêt grand public.

Cela fait certainement un excellent choix de carrière pour les esprits analytiques, nécessitant un mélange de solides compétences en programmation et de connaissances techniques approfondies.

Cependant, derrière les actes spectaculaires de réseaux de neurones en duel et de calcul distribué se cachent certaines pratiques statistiques fondamentales que tout aspirant scientifique des données devrait profondément connaître.

Vous pouvez vous renseigner sur les derniers frameworks de programmation ou les avancées dans la littérature scientifique selon les besoins d'un projet spécifique. Mais il n'y a pas de raccourcis pour acquérir le savoir-faire statistique sous-jacent qui fait un scientifique des données efficace.

Seule la pratique, la patience et peut-être un peu d'apprentissage à la dure affûteront vraiment vos "instincts de données".

### Le principe de parcimonie

C'est répété à un point de cliché dans les cours d'introduction à la statistique, mais les mots du statisticien britannique George Box sont peut-être plus pertinents aujourd'hui que jamais :

> "Tous les modèles sont faux, mais certains sont utiles"

Que signifie réellement cette déclaration ?

Cela signifie que lorsque vous cherchez à modéliser un système du monde réel, vous devez nécessairement simplifier et généraliser au détriment du pouvoir explicatif.

Le monde réel est désordonné, bruyant et difficile à comprendre dans les moindres détails. **La modélisation statistique s'efforce donc de ne pas atteindre un pouvoir prédictif parfait, mais plutôt un pouvoir prédictif maximal avec le modèle minimal nécessaire.**

Ce concept peut sembler contre-intuitif pour ceux qui sont nouveaux dans le monde des données. Pourquoi ne pas inclure autant de termes que possible dans un modèle ? Certes, des termes supplémentaires ne peuvent-ils pas ajouter davantage de pouvoir explicatif au modèle ?

Eh bien, oui... et non. Vous devez vous soucier uniquement des termes qui apportent avec eux une **augmentation statistiquement significative** du pouvoir explicatif.

Considérez les différents types de modèles qui peuvent être ajustés à un ensemble de données donné.

Le plus basique est le modèle nul, qui n'a qu'un seul paramètre — la moyenne globale de la variable de réponse (plus une certaine [erreur distribuée aléatoirement](http://www.abs.gov.au/websitedbs/a3121120.nsf/home/statistical+language+-+types+of+error)).

Ce modèle postule que la variable de réponse ne dépend d'aucune des variables explicatives. Au lieu de cela, ses valeurs sont entièrement expliquées par des fluctuations aléatoires autour de la moyenne globale. Cela limite évidemment quelque peu le pouvoir explicatif du modèle.

Le concept opposé est le modèle saturé, qui a un paramètre pour chaque point de données. Ici, vous avez un modèle parfaitement ajusté, mais qui n'a aucun pouvoir explicatif si vous lui lancez de nouvelles données.

Inclure un terme par point de données néglige également de simplifier de manière significative. Encore une fois — pas exactement utile.

![Image](https://cdn-media-1.freecodecamp.org/images/k5FqxvwXsEctA2ktSMTfcMYsFHPN93r25OVj)
_Ajustement d'un modèle nul, à gauche, et d'un modèle saturé, à droite. Aucun des deux modèles ne permet une interprétation utile._

Clairement, ce sont des cas extrêmes. Vous devriez chercher un modèle quelque part entre les deux — un modèle qui s'ajuste bien aux données et a un bon pouvoir explicatif. Vous pourriez essayer d'ajuster le modèle maximal. Ce modèle inclut des termes pour tous les facteurs et termes d'interaction considérés.

Par exemple, disons que vous avez une variable de réponse _y_ que vous souhaitez modéliser en fonction des variables explicatives _x₁_ et _x₂_, multipliées par des coefficients _β_. Le modèle maximal ressemblerait à ceci :

_y = intercept + β₁x₁ + β₂x₂ + β₃(x₁x₂) + erreur_

Ce modèle maximal devrait, espérons-le, bien s'ajuster aux données et également fournir un bon pouvoir explicatif. Il inclut un terme pour chaque variable explicative et un terme d'interaction, _x₁x₂_.

Supprimer des termes du modèle augmentera la déviance résiduelle globale, ou la proportion de variation observée que les prédictions du modèle ne parviennent pas à expliquer.

Cependant, tous les termes ne sont pas égaux. Vous pourriez être en mesure de supprimer un (ou plusieurs) termes, sans voir une augmentation statistiquement significative de la déviance.

De tels termes peuvent être considérés comme non significatifs et supprimés du modèle. Vous pouvez supprimer les termes non significatifs un par un (en n'oubliant pas de recalculer la déviance résiduelle à chaque étape). Répétez cela jusqu'à ce que tous les termes restants aient une signification statistique.

Vous êtes maintenant arrivé au modèle minimal adéquat. Les estimations pour chaque coefficient de terme _β_ sont significativement différentes de zéro. L'approche éliminatoire étape par étape utilisée pour arriver ici est connue sous le nom de régression "stepwise".

Le principe philosophique sous-jacent à cette recherche de simplicité du modèle est connu sous le nom de **principe de parcimonie**.

Il présente certaines similitudes avec l'heuristique célèbre du philosophe médiéval Guillaume d'Ockham, le [Rasoir d'Ockham](https://en.wikipedia.org/wiki/Occam%27s_razor). Cela va dans le sens de : "étant donné deux ou plusieurs explications également acceptables pour un phénomène, travaillez avec celle qui introduit le moins d'hypothèses."

Ou, en d'autres termes : pouvez-vous expliquer utilement quelque chose de complexe de la manière la plus simple possible ? Arguablement, c'est la quête définissante de la science des données — traduire efficacement la complexité en insight.

### Soyez toujours sceptique

Les [tests d'hypothèses](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing) (comme les [tests A/B](https://en.wikipedia.org/wiki/A/B_testing)) sont un concept important de la science des données.

Simplement dit, les tests d'hypothèses fonctionnent en réduisant un problème à deux hypothèses mutuellement exclusives, et en demandant sous quelle hypothèse la valeur observée d'une statistique de test donnée est la plus probable. La statistique de test est, bien sûr, calculée à partir d'un ensemble approprié de données expérimentales ou observationnelles.

En ce qui concerne les tests d'hypothèses, vous demandez généralement si vous acceptez ou rejetez l'[hypothèse nulle](https://en.wikipedia.org/wiki/Null_hypothesis).

Souvent, vous entendez les gens décrire l'hypothèse nulle comme une sorte de déception, voire une preuve d'échec expérimental.

Peut-être cela vient-il de la manière dont les tests d'hypothèses sont enseignés aux débutants, mais il semble que de nombreux chercheurs et scientifiques des données aient un biais subconscient contre l'hypothèse nulle. Ils cherchent à la rejeter en faveur de l'hypothèse alternative, supposément plus excitante et plus intéressante.

Ce n'est pas seulement un problème anecdotique. Des [articles de recherche entiers](http://thelancet.com/journals/lancet/article/PII0140-6736(91)90201-Y/abstract) ont été écrits sur la question du [biais de publication](https://en.wikipedia.org/wiki/Publication_bias) dans la littérature scientifique. On ne peut que se demander comment cette tendance se manifeste dans un contexte commercial.

Pourtant, le fait est que pour toute expérience bien conçue ou tout ensemble de données suffisamment complet, **accepter l'hypothèse nulle devrait être tout aussi intéressant qu'accepter l'hypothèse alternative.**

En effet, l'hypothèse nulle est une pierre angulaire de la statistique inférentielle. Elle définit ce que nous faisons en tant que scientifiques des données, qui est de transformer les données en insights. Les insights ne valent rien si nous ne sommes pas hyper-sélectifs sur les résultats qui passent l'épreuve, et c'est pour cette raison qu'il est payant d'être ultra-sceptique en tout temps.

Cela est d'autant plus vrai, étant donné la facilité avec laquelle il est possible de "rejeter accidentellement" l'hypothèse nulle (au moins lorsque l'on applique une approche fréquentiste de manière naïve).

Le [data-dredging](https://en.wikipedia.org/wiki/Data_dredging#Examples_in_meteorology_and_epidemiology) (ou "p-hacking") peut produire toutes sortes de résultats sans signification, qui apparaissent néanmoins statistiquement significatifs. Lorsque des comparaisons multiples sont inévitables, il n'y a aucune excuse pour ne pas prendre de mesures afin de minimiser les [erreurs de type I](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) (faux positifs, ou "voir des effets qui ne sont pas vraiment là").

* Pour commencer, en ce qui concerne les tests statistiques, choisissez-en un qui est intrinsèquement prudent. Vérifiez que les hypothèses du test sur vos données sont correctement satisfaites.
* Il est également important de se pencher sur les [méthodes de correction](https://en.wikipedia.org/wiki/Family-wise_error_rate#Controlling_procedures), par exemple, la [correction de Bonferroni](https://en.wikipedia.org/wiki/Bonferroni_correction). Cependant, ces méthodes sont parfois critiquées pour être trop prudentes. Elles peuvent réduire la [puissance statistique](https://en.wikipedia.org/wiki/Statistical_power) en produisant trop d'erreurs de type II (faux négatifs, ou "ignorer des effets qui existent réellement").
* Recherchez des explications "nulles" pour vos résultats. À quel point vos procédures d'échantillonnage/collecte de données étaient-elles appropriées ? Pouvez-vous exclure toute erreur systématique ? Pourrait-il y avoir des effets de [biais de survivant](https://en.wikipedia.org/wiki/Survivorship_bias), d'[autocorrélation](https://en.wikipedia.org/wiki/Autocorrelation), ou de [régression vers la moyenne](https://en.wikipedia.org/wiki/Regression_toward_the_mean) ?
* Et enfin, à quel point les relations potentielles que vous avez trouvées sont-elles plausibles ? Ne prenez jamais rien pour argent comptant, peu importe la valeur de p !

Le scepticisme est sain, et en général, il est bon de toujours garder à l'esprit les explications nulles pour vos données.

Mais évitez la paranoïa ! Si vous avez bien conçu votre expérience et analysé vos données avec prudence, alors allez-y et prenez vos résultats comme réels !

### Connaître vos méthodes

Les avancées technologiques et théoriques récentes ont fourni aux scientifiques des données une gamme de nouveaux outils puissants pour résoudre des problèmes complexes qui n'auraient pas été réalisables il y a même une décennie ou deux.

Il y a beaucoup d'excitation autour de ces avancées en apprentissage automatique, et pour de bonnes raisons. Cependant, il est trop facile de négliger les limitations qu'il pourrait y avoir à les appliquer à un problème donné.

Par exemple, les [réseaux de neurones](https://en.wikipedia.org/wiki/Artificial_neural_network) peuvent être brillants pour classer des images et reconnaître l'écriture manuscrite, mais ils sont loin d'être une solution parfaite pour tous les problèmes. Pour commencer, ils sont très sujets au surapprentissage — c'est-à-dire, devenir trop familiers avec les données d'entraînement et être incapables de généraliser à de nouveaux cas.

Prenez également leur opacité. Le pouvoir prédictif des réseaux de neurones vient souvent au prix de la transparence. Grâce à l'internalisation de la sélection des caractéristiques, même si un réseau fait une prédiction précise, vous ne comprenez pas nécessairement _comment_ il est arrivé à sa réponse.

Dans de nombreuses applications commerciales, comprendre le "comment et pourquoi" est souvent le résultat le plus important d'un projet analytique. Renoncer à cette compréhension pour le bien de la précision prédictive peut ou non être un compromis qui vaut la peine.

De même, il est tentant de se fier à la précision d'un algorithme sophistiqué d'apprentissage automatique, mais ils ne sont absolument pas infaillibles.

Par exemple, l'API [Cloud Vision](https://cloud.google.com/vision/) de Google — qui est généralement très impressionnante — peut [être facilement trompée](https://arxiv.org/pdf/1704.05051.pdf) par même une petite quantité de bruit dans une image. Inversement, un autre article de recherche fascinant a montré comment les réseaux de neurones profonds [peuvent "voir" des images qui ne sont simplement pas là](https://arxiv.org/pdf/1412.1897v1.pdf).

![Image](https://cdn-media-1.freecodecamp.org/images/Unu82IzSCTYuy2W-wFBiCQQ2zssV6oXnkVeG)
_Humains 1 - nil Machines. Ajouter même un peu de bruit à une image peut tromper l'API Cloud Vision de Google. Via [TheRegister.co.uk](https://www.theregister.co.uk/2017/04/19/cloud_vision_api_defeated_by_noise/)._

![Image](https://cdn-media-1.freecodecamp.org/images/3rmbJwk5WuZdOwm5PWt5OElDc5EOz9NctC0M)
_Qu'avez-vous fumé... ?! Les DNN peuvent parfois faire preuve de beaucoup d'imagination. Images via Nguyen et al, 2014. [Lire l'article sur arXiv](https://arxiv.org/pdf/1412.1897v1.pdf)._

Ce ne sont pas seulement les méthodes d'apprentissage automatique de pointe qui doivent être utilisées avec méfiance.

Même avec des approches de modélisation plus traditionnelles, il faut veiller à ce que les hypothèses clés soient satisfaites. Regardez toujours l'extrapolation au-delà de la portée des données d'entraînement, si ce n'est avec suspicion, du moins avec prudence. Avec chaque conclusion que vous tirez, demandez-vous toujours si vos méthodes justifient de le faire.

Ce n'est pas dire de ne faire confiance à aucune méthode — juste d'être conscient à tout moment **pourquoi** vous utilisez une méthode plutôt qu'une autre, et **quels** sont les avantages/inconvénients relatifs.

**En règle générale, si vous ne pouvez pas trouver au moins un inconvénient à une méthode que vous envisagez, faites des recherches supplémentaires avant de continuer. Utilisez toujours l'outil le plus simple qui fera le travail.**

Savoir quand il est approprié ou non d'utiliser une approche donnée est une compétence clé en science des données. C'est une compétence qui s'améliore avec l'expérience et une compréhension réelle des méthodes.

### Communication

La communication est l'essence de la science des données. Contrairement aux disciplines académiques, où votre public cible sera composé d'experts hautement qualifiés dans votre domaine exact d'étude, le public d'un scientifique des données commercial sera probablement composé d'experts dans un large éventail d'autres domaines.

**Même les meilleurs insights du monde ne valent rien s'ils sont mal communiqués.** De nombreux aspirants scientifiques des données viennent de milieux académiques/de recherche et seront habitués à communiquer avec des publics spécialisés sur le plan technique.

Dans un environnement commercial, cependant, on ne peut pas assez insister sur l'importance d'expliquer vos résultats de manière à ce qu'un public général puisse comprendre et travailler avec.

Par exemple, vos résultats peuvent être pertinents pour une gamme de différents départements au sein d'une organisation — du marketing, aux opérations, au développement de produits. Les membres de chacun seront des experts dans leurs domaines de travail respectifs et bénéficieront de résumés clairs, concis et pertinents de vos résultats.

Aussi importants que les résultats réels sont les limitations connues de vos résultats. Assurez-vous que votre public est conscient de toute hypothèse clé, de données manquantes ou de degrés d'incertitude dans votre flux de travail.

Le cliché "une image vaut mille mots" est particulièrement vrai en science des données. À cette fin, les outils de visualisation de données sont inestimables.

Des logiciels comme Tableau, ou des bibliothèques comme [ggplot2 pour R](http://ggplot2.org/) et [D3.js](https://d3js.org/), sont d'excellents moyens de communiquer des données complexes de manière très efficace. Ils valent la peine d'être maîtrisés autant que tout concept technique.

Une certaine connaissance des [principes de design graphique](https://en.wikibooks.org/wiki/Graphic_Design/Principles_of_Design) ira loin pour rendre vos diagrammes intelligents et professionnels.

Assurez-vous également d'écrire clairement. L'évolution a façonné nous, les humains, en créatures impressionnables pleines de biais subconscients, et nous sommes intrinsèquement plus enclins à faire confiance à des informations mieux présentées et bien écrites.

Parfois, la meilleure façon de comprendre un concept est d'interagir avec lui soi-même — il peut donc être utile d'apprendre quelques compétences web front-end pour produire des [visualisations interactives](http://modern-art-graph.herokuapp.com/) avec lesquelles votre public peut jouer. Il n'est pas nécessaire de réinventer la roue. Des bibliothèques et outils comme D3.js et Shiny de R rendent votre tâche beaucoup plus facile.

**Merci d'avoir lu ! Si vous avez des commentaires ou des questions, veuillez laisser une réponse ci-dessous — j'ai hâte de les lire !**