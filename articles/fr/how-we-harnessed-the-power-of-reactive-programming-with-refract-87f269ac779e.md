---
title: Comment nous avons exploité la puissance de la programmation réactive avec
  Refract
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T16:56:57.000Z'
originalURL: https://freecodecamp.org/news/how-we-harnessed-the-power-of-reactive-programming-with-refract-87f269ac779e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yHmiM0LdthwrK9GnV5MXWw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment nous avons exploité la puissance de la programmation réactive avec
  Refract
seo_desc: 'By Joe McGrath

  Have you ever wondered how open-source libraries built by companies come into existence?

  I’ve always been curious about it. Do they start with the intention of creating
  an internal library? Is open-source the initial goal? If neither, ...'
---

Par Joe McGrath

Vous êtes-vous déjà demandé comment les bibliothèques open-source développées par des entreprises voient le jour ?

J'ai toujours été curieux à ce sujet. Est-ce qu'elles commencent avec l'intention de créer une bibliothèque interne ? L'open-source est-il l'objectif initial ? Si ce n'est ni l'un ni l'autre, comment cela se produit-il ? Maintenant que j'ai eu la chance de voir cela de A à Z, il semble utile de partager l'histoire de la création de [Refract](https://refract.js.org/) !

![Image](https://cdn-media-1.freecodecamp.org/images/zwjEANmYzAbTRpsN5UdKBCeQYwXDcMRPYgBb)

L'une des premières choses que j'ai faites après avoir accepté l'offre d'emploi de [FanDuel](https://www.fanduel.com/careers) a été d'envoyer un e-mail aux ingénieurs qui m'avaient interviewé.

Mon ancien employeur était une startup ambitieuse travaillant sur des idées intéressantes, mais FanDuel était le vrai deal : une licorne technologique avec une réputation de l'une des meilleures entreprises du pays. Comme je n'avais que quelques mois d'expérience avec React/Redux et autres, il semblait judicieux de prendre de l'avance... alors j'ai demandé quelle technologie apprendre.

Parmi les bibliothèques et concepts à la fois familiers et inconnus, une ligne de la réponse a attiré mon attention :

> « xstream — nous sommes très enthousiastes à l'idée d'utiliser la programmation réactive »

J'avais entendu parler de la programmation réactive — c'était exactement le type de technique de programmation puissante et flexible que j'espérais apprendre. Cependant, je savais assez de choses à ce sujet pour que le nom xstream soulève des questions.

Généralement, la combinaison de React et de la programmation réactive signifiait redux-observable, et redux-observable utilisait RxJS. Xstream est une alternative à RxJS. Le fait qu'ils utilisaient xstream signifiait soit un adaptateur, soit une sorte d'intégration personnalisée.

J'espérais que ce soit cette dernière option. Cela correspondait à la réputation d'innovation de l'entreprise, et semblait être quelque chose qui pourrait être immensément intéressant à travailler.

Je ne serais pas déçu.

### Une période d'exploration

Il y a des avantages et des inconvénients à commencer un nouvel emploi à la mi-décembre. Ils sont amplifiés si votre première semaine se trouve être un hackathon.

Il faudrait un certain temps avant que du travail sérieux ne me soit confié, ce qui, dans mon cas, était une bonne chose. Cela signifiait que j'avais le temps d'explorer. Une particularité de mon approche de l'apprentissage est que je suis heureux d'absorber des connaissances et du contexte sur une nouvelle base de code simplement en lisant le code.

Mon objectif principal était de comprendre l'application d'un point de vue général, mais j'avais d'autres questions. Je voulais voir comment ils utilisaient la programmation réactive — et il n'a pas fallu longtemps pour trouver ce que je cherchais.

En creusant à travers plusieurs couches d'abstraction, j'ai découvert une paire de composants d'ordre supérieur : `withSideEffects` et `withPropsSideEffects`.

Le premier vous permettait d'observer un store Redux via des actions ou des sélecteurs. C'était comme redux-observable en concept, mais intégré dans un composant React.

Le second était encore plus intéressant. Il vous permettait d'observer les données circulant à travers React lui-même, quelque chose que je n'avais même jamais entendu comme une possibilité.

Ces deux HoCs généralisés formaient les blocs de construction pour une sélection de HoCs plus spécialisés. Chacun prenait un flux de données et effectuait un effet secondaire spécifique en réponse. Une paire pour envoyer des événements d'analyse, une autre paire pour envoyer au store. Une autre encore pour déclencher des changements de navigation. C'était une limitation évidente : vous ne pouviez observer qu'une seule source à la fois et ne causer qu'un seul type d'effet.

Un autre défaut était que les HoCs avaient une API très cryptique. Pour les configurer, vous deviez passer des tableaux imbriqués, contenant des listes de choses que vous vouliez observer et des effets que vous vouliez causer en réponse.

En conséquence, cette fonctionnalité extrêmement puissante n'était pas utilisée à son plein potentiel. Les idées derrière le code montraient tant de flexibilité, mais ces défauts la retenaient.

Alors, d'où venaient ces défauts ? Quelles batailles ce code avait-il traversées avant de porter ces cicatrices ?

Il s'avère que le code que j'ai rencontré en premier était en fait la quatrième itération. Quelles étaient les itérations précédentes, et comment sont-elles apparues ?

![Image](https://cdn-media-1.freecodecamp.org/images/AZ2XVzgBF9mlhPLnCO7Z7crFmYgKUAa3Lm4V)
_Photo par [Unsplash](https://unsplash.com/@atulvi?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Atul Vinayak</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Il y a bien longtemps

En 2015, FanDuel a pris la décision de créer un nouveau produit pour un potentiel nouveau marché. Cela a été traité comme un nouveau départ — une chance d'essayer quelque chose de nouveau, d'explorer les avantages potentiels que l'écosystème populaire React/Redux pourrait offrir par rapport à l'application Angular existante.

[Thomas](https://twitter.com/tcroch) était l'un des ingénieurs principaux du projet. Il était convaincu que la programmation réactive pouvait débloquer d'énormes avantages, avide de trouver des opportunités pour l'utiliser dans l'application.

Les premières graines de Refract — la première itération — sont venues de la chose absolue préférée de chaque développeur à travailler : l'analyse.

Nous n'explorerons pas cette version ici, car à l'époque Thomas a écrit [un article expliquant la situation](http://troch.github.io/posts/2016/09/27/redux-analytics-without-middleware/) qui reste bien utile à lire. Le cœur de la fonctionnalité impliquait des flux intégrés dans un composant React. Cela vous permettait d'observer des actions et des sélecteurs, et d'envoyer des données aux fournisseurs d'analyse en réponse.

### La marche régulière du progrès

La nouvelle application a été considérée comme un succès, et l'entreprise a décidé de re-platformer le produit phare américain en utilisant la nouvelle technologie brillante.

Comme il est naturel avec de tels changements majeurs pour un produit déjà utilisé à grande échelle, ce serait un projet à long terme. Au moment de l'écriture, plusieurs vues Angular restent en usage, et un certain code hérité encore plus ancien s'accroche à la vie à certains endroits.

Mais cela ne signifie pas que la vie attend que l'ancien code rattrape son retard. Au fil du temps, l'approche des effets secondaires a évolué et s'est améliorée.

La deuxième itération de Refract restera perdue dans le temps. Pour citer Thomas, « J'ai oublié, et je pense que c'est mieux ainsi. »

La troisième itération était similaire à l'approche que j'ai rencontrée en premier. Son API était encore plus difficile à lire, et elle était toujours limitée à l'observation de Redux.

La quatrième itération était un grand bond en avant. La capacité d'observer les props React a été introduite. Des incohérences mineures ont été corrigées. Le code impératif et déclaratif a été divisé en quelque chose de similaire aux réducteurs et créateurs d'actions de Redux.

Cette itération est restée stable pendant plus d'un an. Elle a prouvé sa valeur au fil du temps, et était considérée comme une fonctionnalité mature au moment où j'ai rejoint l'équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/0rUO5jLVkG2DT1C5N9aC2ITt5FoyFmY8AXAK)
_Photo par [Unsplash](https://unsplash.com/@nxvision?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Nigel Tadyanehondo</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Une nouvelle idée

Ainsi, Refract a commencé comme un code propriétaire, considéré comme stable mais difficile à utiliser, construit à l'intérieur d'une grande application. Comment avons-nous transformé cela en une bibliothèque autonome, prête à être utilisée par la communauté élargie ? Quelles étapes ont été franchies en cours de route ?

Le projet a en fait été déclenché par une influence extérieure. FanDuel accueille souvent les rencontres [Edinburgh React](https://www.meetup.com/react-edinburgh/), avec au moins un ou deux ingénieurs présents.

Lors d'une rencontre, une présentation a exploré redux-observable, et cela a frappé l'une des personnes présentes à quel point notre code pouvait faire beaucoup plus en comparaison. Nous en avons parlé au cours des semaines suivantes, sentant que ce serait quelque chose qui vaudrait bien la peine d'être open-source.

Pendant un certain temps, rien ne semblait sortir de ces discussions. Bien que l'entreprise consacre 10 % du temps de chacun au développement professionnel, tout le monde avait d'autres choses qu'il voulait travailler. De plus, le code semblait trop complexe pour qu'il s'agisse d'un projet qui pourrait réellement réussir.

### Cela se passe ?

Puis, un jour à la mi-avril, un nouveau canal Slack est apparu. Le but du canal : `Discussion d'une nouvelle API pour les effets secondaires, avec un plan OSS`. Thomas a publié une esquisse d'une nouvelle API qu'il avait en tête.

L'esquisse était beaucoup plus simple que l'API existante. Elle rendait l'expérience du développeur beaucoup plus propre et plus intuitive, et ajoutait encore plus de flexibilité. Au cours des semaines suivantes, nous avons discuté d'idées d'améliorations, tout en nous attelant à la tâche sérieuse de discuter du nom et du logo du projet.

Pendant un certain temps, nous avons convergé vers le nom **Recoil** sans en être trop heureux, mais ensuite le nom parfait a été suggéré : **Refract**. Des symboles ont été esquissés, puis le logo final a été complété. Progrès !

Avec le travail sérieux terminé, nous pouvions nous atteler aux détails restants — à savoir attendre que Thomas écrive le code.

Il a extrait le code existant de l'application, et l'a modifié pour correspondre à la nouvelle conception de l'API. Nous avons pris le temps de construire quelques projets de test, d'itérer sur les détails, puis d'écrire la documentation et les exemples. Nous avons présenté l'idée à notre CTO et à d'autres cadres, obtenant l'approbation de plusieurs parties prenantes clés.

![Image](https://cdn-media-1.freecodecamp.org/images/uphZh85IkaSVE1mTUJSQt4MEdMSWKchiJZr8)

Donc, voici : au moins dans ce cas, notre bibliothèque a une histoire beaucoup plus longue qu'il n'y paraît. Elle a évolué à travers de nombreuses itérations avant que les premières idées d'open-source ne viennent à l'esprit.

Nous avons publié la version un de Refract à la fin du mois d'août 2018, après l'avoir utilisée en interne pendant un certain temps, et ce fut un plaisir de travailler avec. Mais, comme pour les meilleures histoires d'origine, la fin n'est que le début de quelque chose de plus grand.

### Un nouveau but

Notre expérience précoce avec la bibliothèque nous a conduit à de nouvelles idées. Nous avons mis en œuvre les meilleures d'entre elles, et Refract est devenu quelque chose de beaucoup plus général que ce que nous avions imaginé à l'origine.

Ce n'est plus seulement une bibliothèque pour isoler les effets secondaires de votre logique synchrone. Elle vous permet maintenant de **construire votre application React en utilisant la programmation réactive**. Cela a d'énormes implications pour la façon dont nous pourrions structurer nos applications à l'avenir.

Mais cela est mieux laissé à explorer une autre fois.

Pour l'instant, si vous voulez en savoir plus, [consultez notre documentation](https://refract.js.org/) et nos nombreux [exemples de code en direct](https://refract.js.org/examples) !

Rejoignez-nous dans notre canal [**#refract** sur le serveur Discord Reactiflux](https://discord.gg/fqk86GH) si vous avez des questions ou des commentaires, ou simplement pour parler de la façon dont vous aimeriez utiliser la bibliothèque. Nous avons hâte d'avoir de vos nouvelles !

[**Refract — Documentation**](https://refract.js.org/)  
[_Exploitez la puissance de la programmation réactive pour supercharger vos composants_refract.js.org](https://refract.js.org/)