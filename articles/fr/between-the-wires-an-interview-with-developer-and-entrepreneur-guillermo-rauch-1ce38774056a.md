---
title: 'Entre les fils : Une interview avec le développeur et entrepreneur Guillermo
  Rauch'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-16T16:01:01.000Z'
originalURL: https://freecodecamp.org/news/between-the-wires-an-interview-with-developer-and-entrepreneur-guillermo-rauch-1ce38774056a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q2YEyS0BkehpBQ7yfSxIMQ.jpeg
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Entre les fils : Une interview avec le développeur et entrepreneur Guillermo
  Rauch'
seo_desc: 'By Vivian Cromwell

  I interviewed Guillermo Rauch, the founder of zeit.co. Zeit’s mission is to make
  cloud deployment simple, global, and real time. Rauch also built socket.io and founded
  two startups previously: LearnBoost and CloudUp.

  This article w...'
---

Par Vivian Cromwell

_J'ai interviewé Guillermo Rauch, le fondateur de [zeit.co](http://zeit.co). La mission de Zeit est de rendre le déploiement cloud simple, global et en temps réel. Rauch a également construit [socket.io](http://socket.io/) et fondé deux startups auparavant : LearnBoost et CloudUp._

_Cet article a été [originalement](https://medium.com/between-the-wires/between-the-wires-guillermo-rauch-2819177beedc) publié sur [Between the Wires](http://betweenthewires.org), une série d'interviews mettant en vedette ceux qui construisent des produits pour développeurs._

#### Parlez-nous un peu de votre enfance et de l'endroit où vous avez grandi.

J'ai grandi dans une petite ville en Argentine, juste à l'extérieur de Buenos Aires. C'est une petite communauté résidentielle avec très peu d'accès à Internet et très peu de moyens d'acquérir un ordinateur.

Mon père était vraiment passionné par l'ingénierie en général et Star Trek, alors il voulait toujours acheter de nouvelles choses cool pour la famille. Nous avons eu un ordinateur quand j'avais environ sept ans. Je me souviens encore du premier jour où nous l'avons eu et du démarrage de Windows 95. C'est à ce moment-là que tout a commencé.

#### Qu'est-ce qui vous a spécifiquement attiré vers la programmation ?

Il y a eu plusieurs choses qui se sont produites tôt. L'une d'elles a été l'exposition précoce à des systèmes d'exploitation alternatifs. Lorsque j'ai entendu parler de Linux pour la première fois, par exemple, c'était très difficile à utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RgTaOHeiq7rSxyeKXF949g.jpeg)
_Guillermo, 12 ans, expliquant à Richard Stallman que vi > emacs_

La programmation a vraiment cliqué pour moi grâce à mon exposition aux terminaux, et au très petit nombre d'étapes qu'il fallait pour écrire un fichier, puis exécuter GCC et obtenir le binaire.

Il y a cette idée que le shell lui-même est en quelque sorte un langage de programmation aussi, n'est-ce pas ? Tout cela s'emboîte très bien.

> « Je pouvais réellement extraire tant d'excitation de ces quelques caractères sur un écran noir. »

Je pense que c'était mon premier moment où j'ai su que la programmation était extrêmement excitante pour moi. Je pouvais réellement extraire tant d'excitation de ces quelques caractères sur un écran noir. L'excitation avec la programmation a beaucoup à voir avec cela, car il y a tellement de feedback négatif impliqué dans le processus, que les victoires doivent vous exciter extrêmement. Ce sont les petites choses — comme un test qui passe avec une série de points verts à l'écran — qui m'ont vraiment excité.

#### Cela semble être l'influence de [Hyper.app](https://hyper.is/), n'est-ce pas ?

Définiment. [Hyper.app](https://hyper.is/) est pour moi une sorte de continuation de cette idée.

Aussi, à un moment donné, j'ai découvert l'open source à travers de nombreux projets écrits en PHP MySQL. Avec PHP, j'ai eu un premier aperçu de ce que c'était que d'avoir une base de code gigantesque écrite par des personnes bien plus expérimentées que moi. Lorsque j'ai pu modifier ce travail et obtenir un feedback immédiat, j'ai été fasciné.

#### MooTools était-il votre premier projet Open Source majeur auquel vous avez contribué de manière significative ?

[MooTools](http://mootools.net/) est une collection d'utilitaires JavaScript conçus pour les développeurs JavaScript intermédiaires à avancés.

Je me souviens de ce site web très simple que je construisais pour un catalogue de musique. Il y avait une série de lignes, chacune avec trois boutons sur le côté droit : Inspecter, Éditer et Supprimer. Je voulais que le bouton de suppression supprime simplement cette ligne côté client. Je ne voulais pas recharger tout le site web. Nous avons donc utilisé un iFrame caché auquel nous pouvions poster et détecter l'événement de retour de l'iFrame. Plus tard, j'ai découvert que cette chose avec l'iFrame était un hack. C'est ce qui m'a vraiment attiré vers MooTools.

C'était mon premier rôle vraiment important dans l'open source, ce qui m'a conduit à mon premier emploi. J'avais 16 ans à ce moment-là, quand j'ai été nommé développeur principal pour MooTools.

Ensuite, l'année suivante, j'ai été invité en Suisse parce qu'une startup avait décidé de miser sur MooTools pour tout leur code d'applications frontales. L'un des autres développeurs principaux consultant pour cette entreprise, son nom est Aaron Newton, m'a recommandé. Je pense que c'est pourquoi il est si important d'avoir des personnes qui misent sur vous tôt.

Une semaine plus tard, ils m'ont fait venir en Suisse. Je me souviens avoir rencontré le PDG à la gare. Il était comme, « attendez une seconde. Ce gamin est-il perdu ? Êtes-vous vraiment notre nouveau ingénieur ? » J'ai répondu « oui, allons-y. Faisons cela. »

Ensuite, ils ont ouvert un bureau ici à San Francisco, et c'est à ce moment-là que j'ai décidé de passer à autre chose et de créer ma propre entreprise, parce que pourquoi pas ?

#### Votre première startup LearnBoost a produit tant de projets open source et a aidé à pousser l'adoption de Node JS dans les premiers jours, comment avez-vous fait cela, ou était-ce un effet secondaire ?

[Learnboost](https://www.learnboost.com/) était ma première startup, nous voulions aider les enseignants à gérer leur classe en un seul endroit en utilisant un registre de notes numérique.

C'est intéressant, car c'est un effet secondaire, mais ensuite beaucoup d'effets secondaires dans les startups deviennent vos effets principaux. C'est une histoire classique que vous entendez, où l'une des fonctionnalités de l'entreprise est devenue la plus grande activité de l'entreprise.

Je pense que nous avons commencé avec l'intention d'utiliser Node. Lorsque nous avons commencé à écrire la base de code, c'était un mélange d'un langage pour le backend et JavaScript pour le frontend. Ensuite, lorsque Node est sorti, nous avons décidé de miser 100 % de chaque ligne de code en JavaScript. Pourquoi pas ?

Le bémol était que cela impliquait d'utiliser beaucoup de choses qui étaient en cours de développement, comme l'une des toutes premières versions d'Express. Parfois, nous utilisions des versions précoces de logiciels et trouvions qu'elles n'étaient pas assez bonnes, alors nous construisions les nôtres et les rendions open source.

L'open source était la seule façon pour nous de faire cela, car nous utilisions beaucoup d'open source en interne. Nous recrutions parmi les personnes qui créaient ces projets open source, et ensuite nous donnions en retour comme moyen de stimuler la croissance sur cette plateforme.

C'est aussi ce pour quoi nous sommes devenus connus, l'open source.

#### Nous avons beaucoup parlé des bons côtés avec LearnBoost et Cloudup, voulez-vous partager un peu les défis que vous avez rencontrés ?

Beaucoup de défis. Pour commencer, j'étais vraiment passionné par la construction d'un produit éducatif, mais comme je viens de raconter ma propre histoire, je n'ai pas terminé le lycée et je ne suis pas allé à l'université.

Donc, je pense que nous construisions un produit qui n'incarnait pas vraiment la manière dont j'avais construit ma carrière jusqu'à ce point. Si je devais construire ou recommander un outil éducatif à nouveau, je recommanderais en fait ceux qui m'ont rendu réussi.

J'ai appris presque tout sur Internet. Comment j'ai appris l'anglais en est un bon exemple. J'ai appris en lisant beaucoup de la documentation que j'ai trouvée en ligne, qui était souvent seulement en anglais. Donc, je n'avais pas d'autre choix que d'apprendre à le lire.

Apprendre à coder en est un autre exemple. Vous pouvez apprendre à coder seul chez vous. Vous pouvez obtenir un feedback immédiat si vous utilisez les bons outils. C'est le genre de chose que j'aurais aimé que nous essayions de construire avec le produit pour les autres. Pas seulement créer un outil éducatif général.

Au début, nous demandions aux enseignants, « okay, qu'est-ce que vous pensez de ce plan de classe ? Qu'est-ce que vous pensez de cela ? » Au lieu de cela, je pense que les meilleures startups ont un moyen de dire à tout le monde, « okay, pourquoi ne pas essayer cela ? C'est une nouvelle façon de faire les choses », et de prendre un risque avec cela, aussi.

En revenant à « comment aurais-je pu améliorer cela à l'époque ? », j'aurais aussi essayé d'encourager les personnes qui apprennent à poser des questions comme : Que faites-vous avec toutes ces choses que vous avez apprises ? Comment obtenez-vous un salaire et faites cela à plein temps dans le futur ?

Je pense que pour beaucoup de choses qui ont à voir avec l'acquisition de connaissances, vous obtenez un meilleur retour pour vous-même si vous essayez de l'obtenir gratuitement, puis vous mettez votre créativité par-dessus, et ensuite vous remettez cela sur le marché. C'est essentiellement 100 % de profit.

Je pense que nous pouvons faire beaucoup de cela avec l'open source aussi. Nous devons continuer à trouver des moyens pour que les gens puissent apprendre et contribuer à l'open source, puis en faire un système complet. Pas un système basé sur l'espoir d'une donation qui pourrait ne jamais arriver, mais quelque chose qui redonne vraiment ce pouvoir au créateur, basé sur son utilisation.

> « C'est l'une des choses qui nous manquent actuellement dans la communauté open source. Il y a eu des personnes qui ont fait des contributions vastes au monde que nous avons construit, mais à cause d'un certain ensemble de décisions qu'elles ont prises, elles n'ont pas été en mesure de maintenir. »

Cela a en fait fini par être le cas pour Open SSL. Open SSL, l'une des infrastructures les plus répandues et les plus importantes au monde. Elle était sous-financée et pleine de vulnérabilités de sécurité.

#### En dehors des défis liés au produit, y a-t-il eu des défis d'équipe ou émotionnels ?

Je pense qu'il y a deux types de défis émotionnels. L'un est celui auquel vous êtes directement confronté — peut-être que vous essayiez de vendre votre produit et on vous a refusé parce qu'ils sont allés avec votre concurrent, ou peut-être qu'un investisseur vous a rejeté. Ce type de défi est un feedback très direct de « oh, cela a mal tourné ».

L'autre, moins subtil, lorsque vous entreprenez ces projets de plusieurs années, c'est qu'il n'y a pas de fin en vue.

Il pourrait arriver que demain vous soyez racheté pour un montant que vos pairs considéreraient comme ridicule. Il pourrait arriver que vous deviez passer vingt ans à construire solidement une entreprise, puis trouver une sorte de rétribution pour vos collègues et employés à la fin.

C'est subtil et vous portez ce bagage émotionnel alors que vous combattez constamment une bataille difficile, chaque jour. Je pense que c'est à cela que je faisais référence lorsque, peut-être, l'idée que vous poursuiviez n'est pas complètement alignée avec votre identité ou votre vision du monde, mais vous sentez qu'il est trop tard pour la changer.

Je pense que pour nous, la grande chose que nous avons faite, c'est que nous n'avons pas senti qu'il était trop tard pour la changer. Nous avons simplement dit du jour au lendemain, voici notre nouveau focus. C'est difficile, et ensuite vous faites face à beaucoup de feedback négatif direct, parce que tous vos employés sont comme, « pourquoi ? Pourquoi changeons-nous tout ? J'aimais bien ce sur quoi je travaillais avant. Nous nous en sortions bien. »

Je pense que tout est question d'essayer d'aligner la mission de l'entreprise et votre vision de celle-ci. C'est aussi pourquoi il est important de ne pas être trop attaché aux mauvaises idées. Parfois, c'est délicat, car il y a de l'argent en jeu. Il y a l'argent des autres en jeu.

Je pense que c'est l'une des grandes leçons pour l'open source aussi. Vous investissez beaucoup dans une certaine solution, mais vous devez réaliser à un moment donné qu'elle épuisera son évolution et ne pourra plus croître. La chose intelligente à faire est de la laisser tranquille et de recommencer à zéro.

#### Intéressant. Évidemment, vous êtes revenu avec ZEIT et HyperTerm, donc la première startup ne vous a pas découragé. Je suis curieux de savoir, maintenant que vous êtes en train de la construire, quel est pour vous un résultat à long terme réussi pour ZEIT et HyperTerm ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*H18xgGNRo9YE2nqjJuQY6A.png)

> « L'un de mes rêves est que le prochain Facebook ou le prochain Snapchat soit créé par quelqu'un qui n'a pas eu à suivre toute cette éducation ou qui a dû développer toutes ces connexions et embaucher toutes ces personnes brillantes. Vraiment, ce peut être une fille en Afrique. Ce peut être un garçon au Bangladesh. »

Notre mission est de permettre à tout le monde dans le monde de déployer des applications et des services très facilement. Nous pensons que tout le tissu de l'internet est très, très difficile à saisir. Il y a tant de couches et tant de technologies et tant de jargon impliqués, du DNS au SSL en passant par l'IP, le TCP, le HTTP et les différentes façons d'atteindre la performance. La façon dont nous mesurons notre succès est évidemment d'amener plus de personnes à mettre leur travail en ligne et à être plus productives en changeant ces choses plus fréquemment.

Notre vision est que n'importe qui dans une entreprise sera en mesure de compléter un produit ou une expérience entier et de le déployer par lui-même. Vous donnez le pouvoir à une personne, ce qui autrement aurait pris une équipe entière de personnes. Vous leur donnez un feedback en 100 millisecondes au lieu de quelque chose qui prenait des minutes, des heures ou des semaines.

Il a fallu une personne pour créer Facebook, et c'était un homme assez éduqué dans un dortoir de Harvard, puis ils ont pris un certain nombre d'années pour atteindre leur premier million d'utilisateurs. Vous pouvez voir comment cela change très rapidement, n'est-ce pas ? Le niveau d'éducation des personnes qui ont lancé les prochaines grandes révolutions n'est pas nécessairement aussi élevé et le temps qu'il leur faut pour atteindre un million d'utilisateurs est de plus en plus court. L'une des choses que nous faisons particulièrement bien est que nous prenons votre déploiement et nous le mettons à l'échelle pour vous.

L'un de mes rêves est que le prochain Facebook ou le prochain Snapchat soit créé par quelqu'un qui n'a pas eu à suivre toute cette éducation ou qui a dû développer toutes ces connexions et embaucher toutes ces personnes brillantes pour l'aider à mettre à l'échelle l'entreprise ou la technologie pour lui. Vraiment, ce peut être une fille en Afrique. Ce peut être un garçon au Bangladesh.

Ce serait le scénario de rêve pour nous, donner ce niveau de pouvoir à l'individu. C'est un pouvoir que je pense que notre industrie et cette technologie nous ont donné. Parce qu'il est si difficile de partir de zéro et de construire la tour Trump.

#### Zeit a une équipe très distribuée, y compris vos cofondateurs. Pouvez-vous parler de vos meilleures pratiques en matière de productivité et de communication d'équipe ? Quels outils utilisez-vous ?

> « Les équipes distribuées, à mon avis, sont la seule voie à suivre, car sinon vous passez à côté de toute cette créativité incroyable et de toute cette diversité qui vient de personnes qui ne sont pas avec vous dans le même espace physique. »

![Image](https://cdn-media-1.freecodecamp.org/images/1*t3UFr8sntJi51plbPl4PJg.jpeg)
_L'équipe Zeit et leur plus grand client en Europe_

Je vais vous donner un exemple de ce que je pense être le plus grand avantage des équipes distribuées :

Nous avons lancé Hyper.app, sur lequel j'ai principalement travaillé moi-même pendant environ deux semaines. Ensuite, je l'ai ouvert au monde. Ce qui s'est passé ensuite va vous souffler l'esprit. Une semaine après le lancement, nous avions déjà 50 contributeurs qui avaient soumis des pull requests. Nous avions 100 plugins écrits sur celui-ci.

Je pense que quelque chose qui a aidé à cela, c'est que nous avons rendu les thèmes très simples à créer. C'était très gratifiant de voir cette réponse car vous créez la plateforme sur laquelle nous contribuerons une combinaison de blocs Lego.

Imaginez l'équivalent physique ou en personne d'une telle entreprise ? Comment coordonnez-vous 50 êtres humains autour d'un projet, autour d'un espace de bureau ? Comment les recrutez-vous si rapidement ? Comment leur parlez-vous même individuellement ou réglez les détails de la façon dont ils vont travailler, etc. ?

Je pense que l'open source nous montre ce que cette augmentation dramatique et exponentielle de la productivité peut être. Il n'y a pas d'autre moyen que de le faire sur Internet car la collaboration physique est lente.

Nous avons également mis en place Slack, où tout le monde a rejoint et commencé à échanger des idées. Encore une fois, cette main-d'œuvre massive d'inconnus s'est assemblée presque spontanément et avait tous ces outils pour collaborer. Pour moi, cela s'est passé du jour au lendemain. Pour moi, je veux reproduire cela avec ma propre entreprise. Je ne veux pas que ma capacité à créer de vraiment grands produits soit limitée par la physicalité. Je ne veux pas accabler les gens avec des protocoles inutiles et des routines inutiles qui pourraient leur être inconfortables.

Les équipes distribuées, à mon avis, sont la seule voie à suivre, car sinon vous passez à côté de toute cette créativité incroyable et de toute cette diversité qui vient de personnes qui ne sont pas avec vous dans le même espace physique.

#### Quel est le plus grand défi auquel votre startup est confrontée en ce moment ?

Je pense qu'il y a beaucoup de défis qui ont à voir avec l'éducation du produit. La meilleure chose à faire est de ne pas créer un produit qui a toutes les fonctionnalités pour chaque type de workflow existant. Au lieu de cela, nous voulons éduquer les utilisateurs sur la meilleure façon d'utiliser le produit.

Parfois, vous obtenez des clients enthousiastes, peut-être de très grands clients, qui ont peut-être des idées différentes sur la façon d'utiliser le produit ou la plateforme. Pour nous, il s'agit de trouver un équilibre entre l'ajout de fonctionnalités au fil du temps, tout en conservant la simplicité et en conservant la croyance dans le meilleur modèle pour le développement d'API. Cela revient à dire non à beaucoup de choses, même lorsque c'est extrêmement tentant d'un point de vue financier.

#### Qui sont certains de vos héros de la programmation ?

[Leslie Lamport](https://en.wikipedia.org/wiki/Leslie_Lamport), numéro un. Il est un héros de l'informatique car l'ampleur et la profondeur de ses contributions sont inégalées par quiconque dans notre domaine. Dans mon esprit, il est comparable à [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing), en ce sens qu'il a ouvert un domaine complètement nouveau, à savoir les systèmes distribués. Nous travaillons encore à saisir l'ampleur de ses contributions et continuons à étudier ses idées, spécifiquement avec des travaux récents comme Raft et Flexible Paxos. Ironiquement pour cette question, il [pense](http://research.microsoft.com/en-us/um/people/lamport/pubs/state-machine.pdf) que nous mettons trop l'accent sur les **langages** de programmation alors que des outils mathématiques simples (ensembles, fonctions et logique de base) sont suffisants pour exprimer n'importe quel programme.

[Dan Bernstein](https://en.wikipedia.org/wiki/Daniel_J._Bernstein) est inégalé dans le domaine de la cryptographie et de la sécurité. Contributions théoriques et systèmes de bas niveau extensives, mais aussi connu pour des logiciels esthétiques, pratiques, accessibles et largement utilisés comme Qmail.

Je suis aussi un grand fan des héros moins connus derrière les logiciels que nous utilisons tous les jours. [Junio Hamano](https://github.com/gitster), mainteneur principal de git, me vient à l'esprit. Git était un projet très court terme de Linus qui a été magistralement conduit depuis.

#### Passons à des questions plus générales, quels sont certains de vos passe-temps ou intérêts en dehors de la programmation ?

La programmation est mon principal passe-temps. À part cela, j'aime le fitness au poids de corps, également connu sous le nom de calisthenics, qui est l'exercice de son propre corps sans poids ni salles de sport ou choses de ce genre. C'est une forme de méditation pour moi. C'est aussi un moyen de se fixer des défis presque inatteignables.

J'ai un Shiba Inu. Oui, j'ai appris beaucoup de mon chien parce qu'il a cette vie incroyable qu'il s'est organisée. Il est très zen. C'est un chien du Japon qui a une personnalité incroyable. Je pense qu'il y a beaucoup de choses que nous faisons pour eux, mais il y a aussi beaucoup de choses que nous obtenons d'eux, comme une grande appréciation pour une vie différente, je pense.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CEIMwxWSvQwRZMj1y-gccA.jpeg)
_Dei, si zen._

Je suis aussi passionné par le design, je pense toujours aux petites applications ou projets que je peux créer en parallèle et qui peuvent avoir un impact énorme.

[Faire un don pour soutenir ce projet](https://opencollective.com/betweenthewires).

Ce projet est rendu possible grâce aux parrainages de [frontendmasters.com](https://frontendmasters.com/), [egghead.io](https://egghead.io/), [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge) et [Google Developers](https://developers.google.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*bMdgkbz1ZwgKR-Wp.png)
_Nos sponsors._

Pour suggérer un créateur que vous aimeriez entendre, veuillez remplir ce [formulaire](https://goo.gl/forms/XhR1IyLXJHNMljcp1).

Vous pouvez également envoyer des commentaires à [betweenthewires](https://twitter.com/betweenthewires) sur Twitter.