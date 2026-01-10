---
title: L'emoji le plus utilisé par les développeurs — basé sur mon analyse de 3,5
  Go de journaux de chat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T18:26:31.000Z'
originalURL: https://freecodecamp.org/news/and-the-most-popular-developer-emoji-is-d660a9687be7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RtN1V6RYVVbGp4s4cXjdhQ.png
tags:
- name: Data Science
  slug: data-science
- name: education
  slug: education
- name: social media
  slug: social-media
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: L'emoji le plus utilisé par les développeurs — basé sur mon analyse de
  3,5 Go de journaux de chat
seo_desc: 'By Evaristo Caraballo

  Emoji have drastically changed the way we communicate in social media.

  There are numerous studies suggesting differences in the way people use emoji on
  different social media platforms. For example, the lists of the top emoji in...'
---

Par Evaristo Caraballo

Les emojis ont radicalement [changé notre façon de communiquer](https://digiday.com/marketing/digiday-guide-things-emoji/) sur les réseaux sociaux.

Il existe de [nombreuses études](https://www.socialpilot.co/blog/how-to-use-emojis-to-boost-your-social-media-posts) suggérant des différences dans la manière dont les gens utilisent les emojis sur différentes plateformes de réseaux sociaux. Par exemple, les listes des emojis les plus populaires sur [Instagram](https://blog.hubspot.com/marketing/instagram-emojis-infographic), [Twitter](http://emojitracker.com/), ou [Facebook](http://metro.co.uk/2017/07/17/facebook-reveals-which-emojis-are-sent-the-most-for-world-emoji-day-6785309/) présentent certaines similitudes mais aussi des schémas très distinctifs. Ces différences s'accentuent lorsque l'on descend dans la liste.

La possibilité que la dynamique des plateformes sociales puisse affecter l'utilisation des emojis m'a rendu curieux de savoir comment les gens pourraient les utiliser sur une plateforme sociale pour apprendre à coder.

Dans cet article, j'examine comment les nouveaux développeurs utilisent les emojis, spécifiquement dans la salle de chat principale de freeCodeCamp sur Gitter.

Il existe au moins deux façons d'afficher des emojis dans Gitter :

* Utiliser des _alias_ (comme ceux listés par les [aides-mémoire en ligne](https://gist.github.com/rxaviers/7360908)).
* Utiliser la _forme UTF-8_ en écrivant directement l'emoji depuis votre clavier ou en copiant/collant le caractère depuis des ressources en ligne.

Les deux méthodes s'affichent différemment dans le message, la première affichant des images existantes de Gitter et la seconde selon la configuration de votre machine. La première méthode, « utiliser des alias », est la plus populaire et sera le principal sujet de cette discussion.

Pour vous donner une idée rapide de ce que je cherchais, je voulais explorer rapidement des réponses à des questions comme :

* Y a-t-il un schéma distinctif dans l'utilisation des emojis ?
* Quels sont les emojis les plus populaires alors ?
* Combien de personnes utilisent des emojis ?
* À quel point les utilisateurs maîtrisent-ils le vocabulaire des emojis ?

Alors, commençons et répondons à ces questions.

### Parlons un peu emoji

Après avoir mené mon analyse, j'ai découvert qu'environ 23 % des participants actifs au chat utilisaient également des emojis. Je définis un **participant actif** comme une personne ayant envoyé au moins 10 messages. Si nous comparons plutôt les utilisateurs d'emojis actifs et non actifs à tous les participants actifs, ce chiffre monte à 45 %.

Le nombre d'utilisateurs d'emojis peut sembler faible par rapport à d'autres plateformes. Cependant, il est important de noter que :

* de nombreux utilisateurs de la salle de chat étaient éphémères
* certains utilisateurs préféraient une communication conservatrice
* certains utilisateurs ne connaissaient peut-être pas les alias des emojis

Au total, nos utilisateurs d'emojis ont affiché au moins 753 000 emojis (600 000 lorsque les emojis étaient comptés une seule fois par message) avec une moyenne de 32 emojis pour 100 messages.

![Image](https://cdn-media-1.freecodecamp.org/images/DPL0IGIoIRdpB5vPiWKDd1uxUx8QBute-dCW)
_Représentation d'un graphique en essaim d'abeilles avec la date approximative à laquelle les emojis ont été vus pour la première fois dans la salle de chat principale. Il y avait environ 800 enregistrements avec des données complètes. (D3.js v4, mon bl.ock)._

Dans l'ensemble, nos utilisateurs d'emojis ont montré une maîtrise collective d'environ 800 alias, soit environ 25 % de la [liste complète des emojis utilisés](https://unicode.org/emoji/charts-11.0/full-emoji-list.html). [J'ai esquissé une visualisation en essaim d'abeilles](https://bl.ocks.org/evaristoc/d5531fb65c599370f777370e44f14242) sur D3.js montrant que beaucoup d'entre eux ont été introduits pour la première fois dans la salle de chat entre juillet 2015 et juillet 2016 avec un taux de croissance de 10 à 20 nouveaux emojis par semaine.

Cependant, lorsqu'on les considère individuellement, nos utilisateurs d'emojis maîtrisaient un vocabulaire d'environ 3 emojis différents en moyenne. Cette différence était due à quelques utilisateurs championnant l'utilisation des emojis, avec un maître des emojis en particulier montrant une maîtrise d'environ 500 emojis différents. ?

### Utilisation « atypique » des emojis dans la salle de chat ?

Pour avoir une meilleure idée de la manière dont les gens utilisaient les emojis dans la salle de chat, j'ai comparé mes résultats avec un [rapport](https://www.scribd.com/doc/262594751/SwiftKey-Emoji-Report) réalisé par SwiftKey en 2015. Il y a eu des mises à jour substantielles de la liste des emojis depuis la publication du rapport, mais il semble toujours être la meilleure référence gratuite disponible, encore [utilisée](http://edition.cnn.com/2017/01/18/health/emoji-use-personality-traits-study/index.html). Il n'a pas été possible de trouver les catégorisations d'emojis utilisées par SwiftKey. J'ai utilisé les catégories et sous-catégories données par [unicode.org](http://unicode.org/emoji/charts/emoji-list.html) comme approximation :

![Image](https://cdn-media-1.freecodecamp.org/images/yo3a6Y0bgEsqbRS1USdFU9Lh3JUX3mrdG9lp)
_Catégories d'emojis de SwiftKey en pourcentage de l'utilisation totale des emojis (source : Rapport SwiftKey 2015)_

J'ai d'abord évalué l'utilisation des emojis au niveau des catégories et les résultats étaient très similaires à ceux du rapport SwiftKey. La plupart des emojis postés dans la salle de chat de freeCodeCamp appartenaient à la catégorie « Smileys & People », qui inclut les visages, les gestes, les rôles des personnes, les parties du corps et les cœurs.

![Image](https://cdn-media-1.freecodecamp.org/images/Q8ooxx93MEYI9BOTTUlfiO8WCWkoJnoUvbjk)
_Catégories d'emojis de freeCodeCamp en proportions de comptage par message. Les utilisateurs d'emojis ❤️ « Smileys & People »._

Étant donné que les comparaisons basées sur des catégorisations de haut niveau sont généralement trop superficielles, j'ai essayé une autre comparaison en me concentrant sur les 25 emojis les plus utilisés de 2015 à 2017 en utilisant leurs **sous-catégories**. Ensemble, ces 25 emojis représentaient environ 15 % de tous les emojis postés pendant cette période.

La liste des emojis et des sous-catégories suggère que nos utilisateurs d'emojis pourraient encore bien correspondre au schéma typique des utilisateurs d'emojis. L'utilisation extensive dans la salle de chat d'icônes de la sous-catégorie « face-positive » coïncidait avec l'utilisation des « happy faces » du rapport SwiftKey.

Il en va de même pour la sous-catégorie « face-negative », très similaire aux « sad faces » du rapport SwiftKey. Un peu à part était l'utilisation de « :trollface: », qui est une icône disponible sur GitHub et généralement associée à des messages de spam et de sabotage, mais aussi utilisée comme une blague dans la salle de chat de freeCodeCamp, probablement de la même manière que ? (« :poop: » ou « :hankey: »), également listé dans les 25 plus utilisés.

![Image](https://cdn-media-1.freecodecamp.org/images/dTneYIbhVEn7MRBMv7tp4bWw9D4PyiD5G2Qy)
_Deux graphiques sur les 25 emojis les plus utilisés dans la salle de chat de 2015 à 2017, et leurs sous-catégories. Remarquez l'utilisation extensive des gestes de la main comme ? (« :wave: »), ? (« :thumbsup: »), ✋️ (« :point_up: »), ou ? (« :clap: »), mais pas de bisous._

Cependant, c'est dans l'utilisation extensive des gestes de la main positifs et en général des icônes « body » que cette salle de chat pourrait se distinguer des autres références.

Les icônes de gestes les plus utilisées dans la salle de chat de freeCodeCamp sont positives, liées à l'accueil, au soutien, à la validation et à la reconnaissance du succès, valeurs couramment partagées dans la communauté freeCodeCamp.

Une autre différence est l'utilisation moindre d'icônes comme ❤️ « cœurs » ou ? « bisous », suggérant que « partager de l'affection » n'était pas le principal objectif de cette salle de chat. Avec une démographie de genre d'environ 70-80 % d'hommes, cela pourrait être encore plus difficile. Cette démographie pourrait également expliquer certaines icônes liées aux hommes dans les plus utilisées, comme ? (« :gun: »).

Bien que nous puissions repérer quelques écarts par rapport au schéma général, il est trop tôt pour tirer une conclusion définitive. En fait, il est probable que les écarts les plus importants se trouvent dans la manière dont les gens utilisaient les emojis _moins populaires_.

De plus, il se pourrait que les différences les plus importantes ne soient pas en termes de nombres, mais de _significations_ ou de la manière dont l'iconographie pourrait être interprétée par le groupe selon son contexte. Un bon exemple de ce à quoi je fais référence est la [svastika](https://en.wikipedia.org/wiki/Swastika). Un exemple bien connu pour les emojis est l'[aubergine](https://emojipedia.org/aubergine/). Je me demande si, dans notre liste des 25 plus utilisés, ? (« :fire: ») n'aurait pas une signification distinctive pour ce groupe, comme une façon d'exprimer « l'engagement à une tâche ». Dans tous les cas, c'est un sujet plus pertinent pour ceux qui s'intéressent à la communication sur les réseaux sociaux et aux emojis, comme dans [cet article](https://medium.com/@catherineannemoore/emoji-as-visual-literacy-cbebe37cb99c).

### Et le gagnant est...

En bonus, j'ai créé [une visualisation D3.js des 5 emojis les plus populaires chaque mois](http://bl.ocks.org/evaristoc/663eca9722c37bd7c0d254edfb0c9d00). Faire partie de la liste des emojis les plus comptés ne signifie pas que l'emoji a atteint le top 5 mensuel une fois, ou vice versa. Comme dans le [Tour de France](http://www.letour.fr/en/), un coureur pourrait être constamment en sixième position pendant toute la compétition sans jamais gagner une étape et ensuite figurer dans les plus comptés. De même, un coureur pourrait gagner une étape et ensuite rester dernier le reste du temps. C'est pourquoi cette liste semble un peu différente.

Donc, le gagnant du Top 5 mensuel est...

![Image](https://cdn-media-1.freecodecamp.org/images/alQ9jt2wSO6sWerf9fMs-xTKKGEBlyjqwjnH)
_Image Apple/iOS de « Visage souriant avec bouche ouverte et yeux souriants », son vrai nom CLRD, ou simplement ? (source : [http://www.iemoji.com](http://www.iemoji.com" rel="noopener" target="_blank" title="))_

![Image](https://cdn-media-1.freecodecamp.org/images/hglfKUEQtIiuQ48KrqbC9LIKKxqEXNk10tPE)
_Représentation de la visualisation que j'ai créée montrant ? gagnant la première place plusieurs fois mois après mois entre 01-2015 et 11-2017. Pas de doute sur sa popularité (D3.js v4, mon bl.ock)._

Franchement, je ne m'attendais pas à ce que ? (« :smile: ») soit l'emoji le plus populaire. Je pensais que c'était ? (« :joy: »), étant donné qu'Apple l'a récemment révélé comme étant [son emoji le plus populaire en 2017](http://fortune.com/2017/11/03/apple-most-popular-emoji/).

Les 8 emojis suivants sont également apparus dans la salle de chat informelle de freeCodeCamp. Tout est question de sourires :). Pensez-vous être un fan d'emojis ? Devinez leurs alias ! (Observation : les noms/mots-clés peuvent varier selon la plateforme...)

![Image](https://cdn-media-1.freecodecamp.org/images/9ytewgop1dwDkm7Mo3HDfPKmbhJW-NdbYiNW)
_Images d'emojis Apple/iOS_

J'ai utilisé Python et l'[API Gitter](https://developer.gitter.im/docs/welcome) pour obtenir les messages de la salle de chat principale de freeCodeCamp. Des bibliothèques Python comme [multiprocessing](https://docs.python.org/3.5/library/multiprocessing.html) et [emoji](https://github.com/carpedm20/emoji/) ont été utilisées pour transformer les données. Une partie des transformations a également nécessité des données disponibles en ligne, pour lesquelles j'ai créé des scrapers personnalisés avec des bibliothèques Python (requests, [urllib](https://docs.python.org/3/library/urllib.html), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)). Pour analyser les données, j'ai utilisé Python standard et un peu de [pandas](https://pandas.pydata.org/). Les visualisations exploratoires ont été réalisées avec [matplotlib](https://matplotlib.org/) tandis que les visualisations interactives ont été créées avec [D3.js](https://d3js.org/).

Les versions du code seront disponibles sur mon [dépôt GitHub](https://github.com/evaristoc/fCC_emojis) ainsi que quelques jeux de données finaux. Concernant les jeux de données brutes utilisés pour ce projet, ils sont désormais disponibles sur le compte [Kaggle](https://www.kaggle.com/free-code-camp) de freeCodeCamp.

La motivation de ce projet adhère à la mission de l'[Initiative Open Data](https://github.com/freeCodeCamp/open-data) de freeCodeCamp. Un grand merci aux personnes de la salle de chat DataScience de freeCodeCamp et surtout à [mstellaluna](https://github.com/mstellaluna) pour ses commentaires !

Et n'oubliez pas, si vous avez trouvé les informations de cet article utiles ou si vous avez simplement aimé le contenu, n'oubliez pas de laisser quelques applaudissements ? ? avant de partir ! Merci et bon codage ! ?