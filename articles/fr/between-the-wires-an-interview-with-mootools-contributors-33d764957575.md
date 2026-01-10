---
title: 'Entre les fils : une interview avec les contributeurs de MooTools'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-07T17:43:17.000Z'
originalURL: https://freecodecamp.org/news/between-the-wires-an-interview-with-mootools-contributors-33d764957575
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xlliyjOmrA_L49Q5.
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Entre les fils : une interview avec les contributeurs de MooTools'
seo_desc: 'By Preethi Kasireddy

  If you were doing web development in 2009, MooTools might very well not need an
  introduction! MooTools was a well-known JavaScript utility library for building
  “powerful and flexible code with its elegant, well documented, and co...'
---

Par Preethi Kasireddy

Si vous faisiez du développement web en 2009, [MooTools](http://Mootools.net) n'a probablement pas besoin d'être présenté ! MooTools était une bibliothèque utilitaire JavaScript bien connue pour construire un « code puissant et flexible avec ses API élégantes, bien documentées et cohérentes ». Son [équipe principale de contributeurs](https://mootools.net/developers) était composée d'un ensemble brillant de développeurs, et nous avons la chance aujourd'hui de parler avec trois d'entre eux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zNNFdkpJ1inPkp0-KyQovw.png)
_Sebastian Markbåge (à gauche), Christoph Pojer (au milieu), Tom Occhino (à droite)_

Anciennement contributeurs principaux de MooTools, [Sebastian Markbåge](https://twitter.com/sebmarkbage?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor), [Tom Occhino](https://twitter.com/tomocchino) et [Christoph Pojer](https://twitter.com/cpojer) sont des contributeurs actifs et dynamiques de la communauté [React](https://facebook.github.io/react/) aujourd'hui.

#### Pouvez-vous nous parler un peu de vous et de la façon dont vous vous êtes chacun lancé dans la programmation ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*PrHK3KFAoEmxUZP_bTNN9g.png)

**Sebastian** : Mon père codait des jeux pour le Commodore 64, et je le regardais faire, et je les modifiais. J'avais seulement dix ans quand je me suis vraiment lancé dans la programmation. J'ai commencé à programmer des jeux et à faire de petites bases de données de recherche via Qbasic pour MS-DOS.

**Tom** : Quand j'ai eu mon premier ordinateur, j'utilisais Windows 3.1, puis Windows 95. Je suis devenu obsédé par le re-skinning de fenêtres. Je voulais que mon ordinateur ait un look différent, alors j'ai découvert comment pirater les ressources et changer les images. J'ai commencé avec MS Paint et j'ai changé les couleurs des boutons. Ensuite, il y avait ce programme appelé WindowBlinds qui m'a fait créer mes propres skins. Finalement, j'ai découvert HTML. C'était tellement plus facile et mieux.

**Christoph** : Donc, j'ai commencé à programmer vers l'âge de 12 ans en essayant d'apprendre à créer des sites web. Ensuite, je pense que j'avais 14 ans ou quelque chose comme ça, quand un ami au collège jouait à un jeu en ligne et j'ai parié avec lui que je pouvais le faire, et le faire _mieux_. Après cela, j'ai passé pratiquement chaque jour pendant quatre semaines à construire un jeu en ligne. C'était motivant, construire de petits jeux que beaucoup de gens ont joué ensuite.

#### Intéressant ! Les jeux semblent être le thème ici, surtout pour les personnes qui se sont lancées dans la programmation tôt.

**Tom** : Oui. Vous deviez éditer le HTML dans un Notepad et faire un fichier `.html`. Il n'y avait pas de coloration syntaxique ou quoi que ce soit de ce genre. Je ne savais pas ce qu'était un balisage valide jusqu'à ce que Netscape sorte dans les années 1990, vers 1997.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H4Demn1kbefr2BcBUfYJZA.png)
_Netscape_

**Christoph** : Exactement ! Je faisais des sites web et quelqu'un m'a dit qu'un site que j'avais fait ne fonctionnait pas dans Firefox. Je ne savais même pas ce qu'était Firefox. C'était en 2001.

**Tom** : Je pense que c'était probablement en 1998 pour moi si je dois deviner parce que j'avais 13 ans. Cela semble être plus tôt.

**Sebastian** : Oui, c'était en 1993 pour moi. J'ai commencé avec Netscape 2 je pense. Le CSS n'existait pas du tout. Le HTML existait, mais JavaScript n'était pas encore sur la scène, donc vous ne pouviez pas vraiment programmer beaucoup sur le client. Vous deviez tout faire côté serveur. Tout était en Perl et CGI.

**Tom** : Tu es un dinosaure. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*smxcdYTdzqEdGm3LczmjZQ.png)

#### En revenant à l'origine, savez-vous pourquoi Valerio a commencé MooTools, et comment cela a commencé ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*lyN_1KiIZN9AlTJxMNzEgA.png)
_MooTools en 2007_

**Tom** : Valerio s'est toujours frustré quand il voyait quelque chose qui pouvait être fait mieux. Il utilisait Prototype, et plus spécifiquement, [script.aculo.us](http://script.aculo.us/). Il y avait un problème commun où si vous créiez un gestionnaire d'événements de clic pour démarrer une animation, et que vous cliquiez dessus deux fois, cela redémarrerait l'animation — en déclenchant essentiellement de nouvelles animations à chaque fois sans la possibilité de choisir de reprendre, d'en mettre une autre en file d'attente ou de remplacer.

Ce n'était en fait pas MooTools qu'il créait au début. Tout son prémisse pour [Moo.fx](https://moofx.mad4milk.net/) était juste de pouvoir conserver cette instance, et de pouvoir faire quelque chose de mieux que ce que [Script.aculo.us](http://script.aculo.us/) faisait par défaut. Prototype était assez grand à l'époque, donc il a créé `prototype.lite.js`, qui était essentiellement juste le système de classes plus quelques utilitaires. Finalement, il a construit Moo.fx sur cela. Cela doit encore exister quelque part aujourd'hui, mais c'est ainsi que cela est né. De Moo.fx, il y avait une fondation pour une alternative — Prototype plus [Script.aculo.us](http://script.aculo.us/) — qui est devenu [MooTools](http://mootools.net/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*0i_2IyN6luUR-wD12fauWg.png)
_Tom (à gauche) et Valerio (à droite), l'auteur original de la bibliothèque MooTools_

### Comment chacun d'entre vous a-t-il commencé à contribuer à MooTools ?

**Tom** : Je créais une application d'album photo pour un studio de photographie, et nous avions besoin d'un moyen de trier les photos. À l'époque, [MySpace](https://myspace.com/) avait une grille des huit premiers. Ils l'avaient implémentée comme un one-off, et nous voulions construire un meilleur support pour cela.

[Script.aculo.us](http://script.aculo.us/) avait quelque chose de similaire intégré, mais j'ai essentiellement étendu la bibliothèque de glisser-déposer de MooTools, et créé [Sortable.js](https://docs111.mootools.net/Plugins/Sortables.js). Je l'ai montré à Valerio, et il a décidé qu'elle devait être dans le cœur de MooTools.

**Interviewer** : Quel âge aviez-vous ? Puisqu'il n'y avait pas de Github à l'époque, comment avez-vous même accédé au dépôt ?

**Christoph** : Nous utilisions [Trac](https://trac.edgewall.org/) et [Subversion](https://subversion.apache.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*mBfoaAB5Io_w4SQLyTVWyw.png)
_MooTools Trac_

**Tom** : Obtenir l'accès à Trac et Subversion était une grande affaire. Quand Valerio m'a demandé de contribuer, il n'y avait pas de revues de code. Vous le vérifiiez simplement.

**Christoph** : J'ai eu une expérience similaire à celle de Valerio. Je n'aimais pas Prototype et script.aculo.us. J'ai vu Moo.Fx puis MooTools sortir. C'était en septembre 2006 — j'avais 16 ou 17 ans.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pe_kUckiLTEUVdGgZxzlqg.png)
_Christoph avec des dreadlocks ?_

J'étais dans mes années d'adolescence et j'étais un peu rebelle. Je voulais que mon code soit parfait, et MooTools était simplement écrit si parfaitement. C'était si petit mais faisait tout ce que je voulais. J'étais très idéaliste.

**Tom** : Te souviens-tu de tes premières contributions ? Je ne m'en souviens pas vraiment.

**Christoph** : J'ai commencé à l'utiliser début 2006 pour des jeux. J'ai littéralement construit une version allemande de [Facebook](https://facebook.com) pour mes amis, même si je ne savais pas ce qu'étaient [Facebook](https://facebook.com) ou [MySpace](https://myspace.com/). Ensuite, j'ai construit quelques autres jeux avec. Je ne contribuais pas beaucoup.

Je ne connaissais pas très bien l'anglais, mais j'essayais de l'apprendre. Je suis devenu un contributeur principal en 2009, presque au moment exact où Tom a été embauché par Facebook. Il nous a essentiellement dit de prendre le relais après cela. C'est à ce moment-là que j'ai commencé à contribuer au cœur, et ensuite nous avons commencé à faire un hackathon à Londres, où nous nous rencontrions une fois par an. C'était assez cool.

**Sebastian** : Je suis arrivé à peu près en même temps que Christoph, mais mon expérience était différente. Cela s'est passé pendant ma deuxième période avec JavaScript. J'ai commencé avec JavaScript à la fin des années 1990, quand il était pratiquement inutile. Ensuite, il a connu un regain vers 2005 et j'ai commencé à revenir vers le client après avoir passé cinq ans uniquement sur le serveur. Je regardais tous les frameworks, et j'avais besoin de plus d'aide. Je voulais comprendre davantage, et MooTools m'a aidé à apprendre comment fonctionnait le langage. Il était écrit de manière très propre, vous pouviez étudier la base de code elle-même, mais j'étais frustré par certains détails. Contrairement à ces gars, je construisais en fait des applications assez complexes à l'époque. Je construisais cet éditeur WYSIWYG complexe.

**Tom** : Je construisais un CMS. Ce n'était pas _si_ trivial, voyons.

**Sebastian** : J'ai fait une tirade sur la liste de diffusion publique. Il y avait deux listes de diffusion — une liste interne privée, uniquement pour les développeurs, et la liste publique. Sur la liste publique, il y avait un gars nommé Aaron Newton, et il était en quelque sorte le père de MooTools. Il était l'adulte parce qu'il construisait en fait des startups à l'époque, et essayait de créer une communauté parce qu'il comprenait la valeur de cela. Il passait beaucoup de temps dans les forums publics à aider les nouveaux venus et à les faire entrer dans le cercle intérieur. J'ai fait ces longues tirades sur la liste de diffusion publique, et il m'a invité dans le cercle fermé.

**Tom** : Je pense que nous avons tous commencé sur les forums. La première étape était d'obtenir des droits de modérateur sur les forums — pour pouvoir fermer les sujets et répondre aux questions de manière autoritaire. Nous avions de petites icônes à côté de nos noms indiquant que nous étions modérateurs. Mon premier contact avec Valerio a été quand il m'a contacté pour me remercier de mon aide sur les forums. À partir de ce moment, j'ai commencé à contribuer au code.

**Christoph** : C'est drôle parce que j'ai toujours cet e-mail. Mon premier échange avec Valerio n'était en fait pas vraiment à propos de MooTools lui-même. Il avait construit ce bundler ou cet outil de compression dont j'avais vraiment besoin, et il n'y avait pas vraiment autre chose de similaire. Nous avions l'habitude d'envoyer environ 30 fichiers JavaScript, et ce site MooTools avait ce bundler où vous pouviez concaténer vos fichiers ensemble.

> « Le bundler de MooTools. Donc en avance sur son temps. »

**Tom** : Donc en avance sur son temps, mec, le bundler de MooTools. Donc en avance sur son temps. Vous sélectionniez les choses que vous vouliez, et il créait un script personnalisé pour vous. Vous enregistriez simplement le fichier et le mettiez sur votre serveur web. C'était incroyable.

**Sebastian** : C'était ingénieux parce qu'il n'y avait pas de JS commun.

**Tom** : Il n'y avait rien. Tout était global.

**Sebastian** : Il n'y avait aucun moyen de savoir à partir du code de quelqu'un quels modules étaient requis, donc vous deviez vérifier vous-même, mais parce que c'était juste un site web, vous pouviez le faire facilement sans essayer d'obtenir un standard autour de cela.

#### MooTools a une marque si distincte et mémorable autour de lui. Quelles étaient certaines de ses valeurs fondamentales qui l'ont fait se démarquer initialement, et pourquoi pensez-vous que les gens s'en souviennent si positivement aujourd'hui ?

**Sebastian** : Nous accordions beaucoup de valeur à la lisibilité de la base de code, car c'est ainsi que nous avons appris.

Nous voyions jQuery comme l'opposé, où tout était en ligne. Il n'y avait pas d'abstractions réutilisables, et ils essayaient de supporter chaque cas d'utilisation existant. Finalement, cela rendait le code plus difficile à comprendre et à maintenir. C'est pourquoi nous avons choisi de ne pas supporter autant de cas d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ez90JE2z1LQZSWMeGBOEFw.png)

**Christoph** : C'était intéressant parce que nous étions tous très semblables. Nous construisions quelque chose de grand, mais nous ne faisions aucune sensibilisation. Nous avons assisté à peut-être 3-5 conférences sur une période de sept ans. Nous ne l'avons pas vraiment construit pour les autres. Nous essayions de construire le framework parfait, quelque chose que nous pourrions utiliser. Ce n'est peut-être pas la meilleure façon de faire grandir un projet open source, mais nous étions juste notre petite communauté essayant de construire quelque chose de parfait.

**Sebastian** : Il y avait aussi le chaînage. Le chaînage était très explicite, et tout était conçu autour de la lisibilité et de la grammaire — le chaînage devait imiter une phrase anglaise.

**Tom** : Nous avons constamment itéré pour affiner et améliorer l'API. L'un des principes directeurs était que le code construit sur MooTools devait être lisible, facile à comprendre et facile à étendre. Nous avions un guide de style très strict dans nos têtes que nous suivions tous. C'était presque académique en un sens.

**Christoph** : Je pense qu'académique est une très bonne description. Nous étions tellement concentrés sur la conception de l'API, plutôt que sur la construction de quelque chose que les gens pourraient réellement utiliser et adopter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e8VfMuUFURLsX6rB_U6-_Q.png)
_L'équipe MooTools en train de coder_

#### Selon vous, quelle a été la chose la plus impactante ou la plus importante que vous avez apprise en travaillant sur MooTools ?

**Sebastian** : La collaboration, comme nous l'avons dit, est vraiment importante pour créer une équipe très soudée — une équipe qui partage les mêmes valeurs en termes de la façon dont vous écrivez du code et ce que vous devez prioriser. C'est une chose que nous avons maîtrisée et qui nous a permis d'avancer.

D'un autre côté, le pragmatisme est quelque chose que nous n'avons pas bien fait, mais nous avons appris depuis.

**Christoph** : Pour moi, comme c'était le premier projet open source sur lequel j'ai travaillé, j'ai appris beaucoup sur l'implication dans la communauté et le travail sur l'open source. Cette expérience peut vous épuiser. Les gens vous détestent pour avoir apporté des changements à l'API qu'ils ne comprennent pas, ou vous devez traiter avec des gens qui vous questionnent tout le temps. Mais, faire connaissance avec la communauté, rencontrer des gens avec qui je travaillais tous les jours, c'était l'une des meilleures choses pour moi.

**Tom** : Pour moi, apprendre JavaScript a été énorme. Il y avait une tonne d'expérimentation, essayer de résoudre des problèmes de manière cross-navigateur, et j'avais l'impression de porter trop de poids sur les incompatibilités cross-navigateur. J'ai vraiment l'impression d'avoir appris JavaScript et les concepts de programmation fonctionnelle d'une manière que je n'aurais pas pu à l'école.

**Sebastian** : Je pense que c'est un point vraiment sous-estimé au cours de la dernière décennie. Il y avait une communauté grandissante de jeunes comme nous sans expérience préalable, et nous avons été embauchés parce que nous pouvions résoudre de vrais problèmes commerciaux en utilisant JavaScript. JavaScript était méprisé au début, avait stagné et avait des problèmes de performance, mais il nous permettait de construire quelque chose de productif.

Pendant ce temps, il y avait beaucoup de projets académiques — la sagesse commune était qu'ils allaient réussir. Que ces outils commerciaux soutenus par de grandes entreprises allaient remplacer JavaScript. Mais ce n'est pas tout à fait ce qui s'est passé. Cela montre que vous devez prêter attention à ce qui attire les gens. Ils sont attirés par cela pour une raison.

#### MooTools était probablement l'une de vos premières grandes contributions et projets open source. Comment diriez-vous qu'il a impacté votre carrière ?

**Tom** : Pour moi, c'était assez facile, en fait. Quelqu'un organisait une conférence aux Pays-Bas appelée [Fronteers](https://youtu.be/4atCNDQ_qbs?t=92) et ils utilisaient et adoraient MooTools. Donc ils ont contacté Valerio pour voir s'il voulait parler de MooTools et de JavaScript orienté objet. Valerio les a dirigés vers moi. J'étais assez jeune, au début de la vingtaine, et je n'avais jamais parlé à une conférence. Je ne savais pas vraiment de quoi je parlais. Je remercie mes étoiles chanceuses tous les jours que ce n'était pas enregistré car c'était si embarrassant. Cependant, à la suite de cela, un recruteur de Facebook m'a contacté et m'a dit qu'ils essayaient de faire plus avec JavaScript et m'a demandé de venir pour un entretien.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UoMP-4eZNNw-NOIJiIDeGw.png)
_Tom à React.js Conf_

**Christoph** : Mon histoire est assez similaire à celle de Tom. J'ai aussi fait une [conférence publique](https://youtu.be/6nOVQDMOvvE). C'était vraiment difficile parce que, bien que j'étais habitué à parler en public, je n'étais pas habitué à parler en public en anglais dans un pays étranger. Je n'ai pas eu autant de chance que Tom, ma conférence est toujours en ligne. J'avais un accent autrichien très lourd, comme Arnold Schwarzenegger.

Après la conférence, un recruteur de Facebook m'a contacté, et j'ai fini par faire un stage chez Facebook. Tom était en fait mon manager de stage, donc cela a plutôt bien fonctionné. Ensuite, j'ai dû retourner à l'université et terminer mon diplôme avant de pouvoir rejoindre Facebook à temps plein. À mon retour, il y avait tous ces gens de MooTools comme Sebastian qui travaillaient à temps plein chez Facebook.

**Sebastian** : Je travaillais en Europe. Thomas Aylott était chez Cloudera puis a travaillé chez Sencha dans la région de la Baie. Il a commencé à me parler de déménager ici. À l'époque, je ne voulais pas déménager en Californie, surtout pas dans la région de la Baie. Mais, un autre gars de MooTools m'a recommandé à Apple, donc j'ai passé un entretien là-bas. Je n'aimais pas vraiment l'attitude de l'entreprise. Franchement, je ne pensais pas que je déménagerais ici du tout. Enfin, cependant, Aylott a quitté Sencha et a commencé à travailler pour Facebook. Après cela, il m'a recommandé à nouveau, donc j'ai finalement pris l'avion, passé un entretien, et cela avait une ambiance différente. Tous mes amis de MooTools étaient là, donc j'ai décidé de me lancer.

**Tom** : Les gens ne comprenaient pas pourquoi je voulais travailler chez Facebook. J'ai dû les convaincre que nous faisions des choses intéressantes. Après un certain temps, cela a fait partie de ce qui a alimenté notre résurgence dans le monde du front-end et de l'open source. Nous voulions partager certaines des choses auxquelles nous pensions et sur lesquelles nous travaillions. Même après 2011, nous étions toujours considérés comme une entreprise PHP. Hack n'est arrivé qu'en 2013.

**Christoph** : Les gens pensaient en fait que nous ne connaissions pas JavaScript.

**Tom** : C'est drôle parce que tous les problèmes que nous résolvions à l'époque sont devenus les principales préoccupations deux, trois ans plus tard. Des systèmes comme Bootloader et Primer. Primer était le précurseur des applications web progressives, et Bootloader était un précurseur de la division des bundles. Les gens résolvaient des problèmes très différents de ceux que nous résolvions à l'époque.

#### Pouvez-vous parler de MooTools 2 ?

**Christoph** : Oh, mec.

**Sebastian** : MooTools 2 était une réécriture qui devait être encore plus propre.

**Sebastian** : Je pense que le problème qu'il a créé était qu'il essayait d'être si propre que tout avait une abstraction associée. Je pense que cela a influencé ma [conférence JSConf EU sur l'évitement de l'abstraction](https://www.youtube.com/watch?v=4anAwXYqLG8). Finalement, cela atteint un point où personne ne peut le comprendre.

**Tom** : Avec le recul, cela semble si peu pratique.

**Christoph** : C'est drôle que tu fasses référence à MooTools 2. C'était en fait quelque chose qui n'était jamais atteignable. C'était toujours un objectif hypothétique, aspirationnel — l'état final parfait de MooTools. MooTools 2 a été essentiellement livré en tant que 1.2, ce qui a tout cassé.

**Sebastian** : C'est ainsi que nous avons appris l'importance des chemins de mise à niveau.

> « Par ailleurs, nous étions simplement des idéalistes construisant un framework dans le vide. Nous avons appris beaucoup de cela, et nous avons appliqué beaucoup de ce que nous avons appris au développement de React. »

**Tom** : C'est en fait pourquoi React aujourd'hui est si incrémental, et pourquoi chaque version fournit des étapes détaillant comment vous êtes passé de la précédente à celle-ci. Create React App a des instructions pour la mise à niveau à partir d'une version précédente, parce que nous n'avons pas fourni un ensemble à l'époque, et c'était un cauchemar pour tous ceux qui utilisaient le framework. Par ailleurs, nous étions simplement des idéalistes construisant un framework dans le vide. Nous avons appris beaucoup de cela, et nous avons appliqué beaucoup de ce que nous avons appris au développement de React.

**Christoph** : C'est peut-être la conclusion. MooTools nous a définitivement appris beaucoup de leçons qui nous aident maintenant avec des projets comme React ou autre chose sur lequel nous travaillons en open source.

#### Pensez-vous que vos apprentissages de MooTools sont l'une des raisons pour lesquelles l'open source a été si réussi chez Facebook ?

**Tom** : Oui, j'ai commencé ce projet appelé Project Perception. Je voulais changer la perception de Facebook dans la communauté front-end, en parlant plus ouvertement de ce que nous faisions. [James Pearce](https://twitter.com/jamespearce) a rejoint Facebook à peu près à cette époque, et a commencé à gérer une équipe open source pour travailler dessus. Nous collaborons depuis.

Ensuite, [Jordan Walke](https://twitter.com/jordwalke) nous a remis React. C'était la solution à notre problème. C'était une manière très différente de construire des applications web.

**Sebastian** : L'open source aide également à être intellectuellement honnête avec soi-même. Si vous mettez des idées en avant, les gens trouveront des défauts, ils auront d'autres idées. Vous ne pouvez pas simplement dire qu'il existe de meilleures solutions en interne. Vous pouvez le comparer à d'autres solutions dans l'écosystème. Cela vous force à être honnête avec vous-même, et cela aide également l'entreprise.

**Tom** : Il y avait en fait beaucoup de résistance contre l'open sourcing de React. Beaucoup pouvaient énumérer les coûts, mais ils ne comprenaient pas vraiment les avantages. Même si nous avons essayé de vendre le recrutement comme un avantage, c'était toujours une chose intangible, impossible à mesurer. Je ne pense pas que nous ayons pris en compte le fait que nous aurions la capacité de faire avancer toute l'industrie — de voir les idées et les concepts de React se répandre dans d'autres frameworks.

Je ne pense pas que React était en concurrence directe avec une autre bibliothèque JavaScript à l'époque. Je pense qu'il était en concurrence avec une manière traditionnelle de construire des interfaces utilisateur. Pour une raison quelconque, il y a vingt ans, les jeux sont allés dans une direction avec le rendu en mode immédiat et la programmation fonctionnelle, et les applications sont allées dans l'autre direction avec la programmation impérative et orientée objet. Ensuite, nous avons commencé à voir, comme avec React, un retour à la programmation déclarative, asynchrone et fonctionnelle, et maintenant, chaque framework, chaque système de vue sur chaque plateforme a pris ces idées en compte. Je pense que nous allons commencer à voir cela de plus en plus, avec le temps.

**Christoph** : C'est aussi lié à MooTools, c'est quelque chose que nous avons appris à la dure. Le déclin de MooTools, si vous voulez l'appeler ainsi, était parce que nous n'avons pas collaboré avec beaucoup de gens en dehors de notre équipe. Dans jQuery, ils ont adopté une partie de notre code d'animation, et nous en avons été offensés. Même si c'était open source, nous pensions savoir comment construire le système parfait par nous-mêmes. Je pense que l'avantage de l'open sourcing d'un projet est qu'il commence par un niveau de compétition et finit par mener à la collaboration.

#### Comparé à MooTools, ou simplement votre expérience avec l'open source initialement comparé à aujourd'hui, qu'est-ce qui a changé ?

**Sebastian** : J'ai été à la périphérie de quelques communautés open source, et je pense qu'il y a beaucoup de structures de gestion variées. Avec React, nous encourageons certaines personnes en qui nous avons confiance à rester en travaillant étroitement avec elles. C'est principalement dirigé par une équipe centrale plutôt que par des RFC par exemple.

Mais c'est un processus que nous évaluons constamment, comme en regardant comment [Ember le fait avec des RFC](https://github.com/emberjs/rfcs).

**Tom** : Je pense que nous aimons tous vraiment le processus RFC d'Ember. Nous en parlons en interne tout le temps, et nous l'avons appliqué au projet GraphQL et à quelques autres projets.

**Christoph** : Yarn aussi.

**Tom** : De plus, pour MooTools, le financement était géré par nous-mêmes. Avec React, c'est différent parce que Facebook s'appuie fortement sur React. Nous avons quelque chose comme 36 000 composants React vérifiés dans notre base de code, et nous soutenons des dizaines d'applications existantes en production. Nous ne pouvons pas simplement faire des changements massifs et radicaux comme MooTools 2. Nous devons penser aux choses de manière incrémentielle. Nous devons penser aux chemins de mise à niveau.

Vous pouvez être quelque peu assuré que si React continue de bien fonctionner pour nous, il continuera de bien fonctionner pour vous. Nous devons nous mettre à niveau en même temps que vous. Si nous arrêtons de l'utiliser, si nous arrêtons d'investir dedans, vous le saurez tôt, et nous devrons avoir un chemin vers l'avant. C'est un peu une couverture de sécurité.

**Sebastian** : Avec MooTools, beaucoup de grandes entreprises en dépendaient, mais nous ne travaillions pas pour elles. Les gens continuaient à contribuer aux versions plus anciennes parce qu'ils ne pouvaient pas mettre à niveau — il n'y avait pas de chemin de mise à niveau sain à l'époque. Donc je pense maintenant, nous hésitons à être un fork dans l'écosystème. Nous le voyons encore et encore dans l'open source, tout le monde doit travailler ensemble parce que sinon vous créez un écosystème beaucoup plus petit et bifurqué.

#### Et du point de vue du contributeur ? Trouvez-vous que c'est plus facile ou plus difficile ?

**Christoph** : Il y a toujours, pour chaque projet, une personne associée à celui-ci. Le créateur. Sur Twitter, ils font toujours référence à cette personne. J'ai l'impression que c'est ce qui épuise les gens. La seule raison pour laquelle ces projets sont si grands est qu'il y a toute une équipe de personnes qui y contribuent, pas seulement une personne. En tant que cette personne, il y a encore beaucoup de gens qui vous attaqueront, ou créeront des problèmes qui sont difficiles, sinon impossibles, à gérer. J'ai l'impression que cela n'a pas changé. Je souhaite honnêtement aussi que les gens soient plus gentils en général. C'est quelque chose qui est difficile à gérer. Peut-être que c'est juste moi qui mets tant de cœur dans ce projet open source.

> « ... vous ne pouvez pas enlever l'émotion de l'open source parce que l'open source, et cette communauté, est motivée par la passion, c'est beaucoup d'émotion. »

**Sebastian** : Je pense que [Dan Abramov](https://twitter.com/dan_abramov?lang=en) l'a mieux dit quand il a dit, vous ne pouvez pas enlever l'émotion de l'open source parce que l'open source, et cette communauté, est motivée par la passion, c'est beaucoup d'émotion. Ma plus grande recommandation à ceux qui commencent dans l'open source est de ne pas être trompé par le statut de fondateur. Commencez par vous rendre remplaçable. Vous construisez un écosystème, il devrait pouvoir fonctionner sans vous, sinon vous allez vous épuiser. C'est une chose que [John Resig](https://twitter.com/jeresig) a très bien faite. Il a été capable de faire grandir jQuery au point où il ne contribuait plus beaucoup.

**Tom** : jQuery, à mon avis, a fait significativement mieux que MooTools à cet égard, et mieux que ce que React fait actuellement. Il y avait tellement de contributeurs principaux à jQuery qui auraient tous pu le faire avancer dans la bonne direction pour le long terme. C'est pourquoi je pense qu'il est encore si prévalent. La plupart des sites web ont encore jQuery, et c'est encore la solution de référence pour tous les problèmes cross-navigateur.

En ce qui concerne le côté émotionnel, vous devez être capable de vous séparer. Séparer-vous des retours, et de la communauté, afin de pouvoir réellement faire le travail. Dan Abramov fait cela le mieux. Chaque fois qu'il y a de l'angoisse, de la colère ou de la négativité, il la combat avec une gentillesse vicieuse. Il est simplement si gentiment écrasant qu'il veut aller à la racine de pourquoi vous ressentez une certaine façon. Il a la peau plus épaisse que la plupart, certainement plus épaisse que la mienne.

> « Séparer-vous des retours, et de la communauté, afin de pouvoir réellement faire le travail. »

**Christoph** : Cela s'est totalement transformé en une séance de thérapie de groupe. Merci pour cela.

#### Pour quelqu'un qui est peut-être dans la programmation depuis un an, ou deux ans, et qui commence tout juste dans l'open source aujourd'hui, quel est le conseil que vous leur donneriez ?

**Tom** : Tout le monde se sent intimidé lorsqu'il aborde un projet pour la première fois. Ils ne savent pas comment ils peuvent aider, mais ils veulent être impliqués. Tout ce que vous avez à faire est de demander comment vous pouvez aider, et de trouver le projet.

Trouvez quelque chose qui est un fardeau pour les mainteneurs. Cela peut être quelque chose de simple, comme fermer les problèmes en double, ou répondre aux questions, ou aider à prioriser les éléments. Ne vous présentez pas en voulant tout réécrire. Restez humble, et commencez petit.

**Sebastian** : Ne vous découragez pas.

**Tom** : Oui, ne vous découragez pas.

> « Sachez toujours que les mainteneurs et les équipes principales voient presque tout et se souviendront de vous. Vous n'êtes pas invisible, donc plus vous continuez à contribuer, même s'ils ne répondent jamais à votre problème, ils sauront qui vous êtes. »

**Sebastian** : Parce qu'il y a souvent beaucoup de contexte, surtout sur les projets de longue durée, et tout n'est pas documenté.

Il peut également y avoir très peu de mainteneurs pour examiner les problèmes ou les demandes de portage. C'est quelque chose sur lequel nous travaillons activement. Nous avons des métriques qui suivent cela, et nous essayons de nous améliorer, mais il y a encore des problèmes. Sachez toujours que les mainteneurs et les équipes principales voient presque tout et se souviendront de vous. Vous n'êtes pas invisible, donc plus vous continuez à contribuer, même s'ils ne répondent jamais à votre problème, ils sauront qui vous êtes. Quand ils auront besoin de votre aide, ils sauront ce que vous avez contribué, et quel contexte vous avez. Ne vous découragez pas tôt.

**Christoph** : Oui, je veux dire que je pense que les gens intimidés reviennent au statut de héros fondateur que certaines personnes ont ou perçoivent. Souvent, il aide simplement de rencontrer des gens lors de conférences. Vous réaliserez qu'ils sont simplement des personnes réelles, ils ne sont pas les personnes les plus intelligentes du monde. Ils sont simplement des personnes normales qui ont travaillé sur ce projet. Vous pouvez commencer à contribuer et atteindre ce point également.

#### Nous sommes tous ici aujourd'hui parce que nous sommes très passionnés par le web, donc nous sommes curieux de savoir ce qui vous tient en haleine et vous excite à continuer de contribuer à rendre le web meilleur ?

**Tom** : Pour moi, je veux vraiment faciliter la construction de logiciels. Je pense que c'est simplement extraordinairement difficile de construire des logiciels dans n'importe quelle capacité. Je ne pense pas que vous deviez apprendre 3 000 technologies différentes afin de construire une application simple. Le web est la façon dont je suis entré dans le logiciel, et je pense que c'est finalement la façon dont la plupart des gens pourraient et devraient entrer dans le logiciel. La meilleure chose à propos de la technologie web est la très faible barrière à l'entrée. Ce sentiment de haute productivité et d'itération rapide avec tout le développement de logiciels, que vous construisiez un service backend de décodeur d'images, ou que vous construisiez un jeu ou une application simple, ou un jeu VR complexe. Je pense que les complexités d'une plateforme particulière pour laquelle vous voulez construire, devraient être divulguées au fil du temps lorsque vous les rencontrez.

**Christoph** : Oui, c'est pourquoi nous sommes tous ici, n'est-ce pas ?

**Sebastian** : J'ajouterais que l'une des raisons pour lesquelles je suis excité par le web en général, est qu'il y a une tendance pour notre communauté à diverger lorsque nous avons de nouvelles idées, mais nous devons nous unifier à un moment donné. Nous savons tous qu'avec trop de fragmentation, vous ne pouvez rien faire, et finalement vous finissez par vous rejoindre. J'espère que nous serons en mesure de nous rejoindre aussi rapidement que possible. Nous ne voulons pas perdre de vue la couche suivante car la technologie est fondamentalement une question de construction de couches, sur des couches, sur des couches d'abstraction. Nous pouvons être concentrés sur la couche supérieure, mais quelqu'un construit la couche suivante, et ils ne peuvent pas le faire si notre couche est trop fragmentée. Nous devons être en mesure de nous unifier et de collaborer.

**Christoph** : Je suppose qu'une grande chose est que tous ces outils sont également écrits en JavaScript. Donc, bien qu'il soit génial que nous essayions de faciliter la construction de logiciels, la barrière à l'entrée en général est beaucoup plus faible. Tout est écrit en JavaScript, donc quoi que vous vouliez travailler, vous pouvez aller travailler sur cette pièce et l'améliorer. La perspective que tout pourrait être écrit dans un seul langage est en fait vraiment cool. Votre framework React, votre code utilisateur, votre framework de test, votre bundler JavaScript, votre gestionnaire de paquets — ils sont tous écrits dans le même langage. Donc, si vous avez un problème avec l'un d'eux, il est assez facile de le résoudre. C'est ce qui m'excite.

Faites un don pour soutenir ce projet : [https://opencollective.com/betweenthewires](https://opencollective.com/betweenthewires)

Ce projet est rendu possible grâce au parrainage de [frontendmasters.com](https://frontendmasters.com/), [egghead.io](https://egghead.io/) et [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge).

![Image](https://cdn-media-1.freecodecamp.org/images/1*41zvkkwJhGLkPBZ_6UCxEw.png)

Pour suggérer un créateur que vous aimeriez entendre, veuillez remplir ce [formulaire](https://goo.gl/forms/XhR1IyLXJHNMljcp1).

Envoyez vos commentaires à @[betweenthewires](https://twitter.com/betweenthewires) sur Twitter !