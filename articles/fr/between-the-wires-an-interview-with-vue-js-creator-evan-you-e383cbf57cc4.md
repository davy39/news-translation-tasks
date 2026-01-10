---
title: 'Entre les fils : Une interview avec Evan You, créateur de Vue.js'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-30T13:01:12.000Z'
originalURL: https://freecodecamp.org/news/between-the-wires-an-interview-with-vue-js-creator-evan-you-e383cbf57cc4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xkJgg-6HskYrQ3N7.jpeg
tags:
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Entre les fils : Une interview avec Evan You, créateur de Vue.js'
seo_desc: 'By Vivian Cromwell

  I interviewed Evan You, the creator of vuejs.org which is a popular progressive
  JavaScript framework. Evan works on Vue full time with the funding from the Patreon
  campaign. Previously, he worked at Google and Meteor.

  This article ...'
---

Par Vivian Cromwell

_J'ai interviewé Evan You, le créateur de [vuejs.org](http://vuejs.org) qui est un framework JavaScript progressif populaire. Evan travaille sur Vue à temps plein grâce au financement de la campagne Patreon. Auparavant, il travaillait chez Google et Meteor._

_Cet article a été [originalement](http://betweenthewires.org/2016/11/03/evan-you/) publié sur [Between the Wires](http://betweenthewires.org), une série d'interviews mettant en vedette ceux qui construisent des produits pour développeurs._

#### Parlez-nous un peu de votre enfance et de l'endroit où vous avez grandi.

D'accord, je suis né en Chine, ma ville natale s'appelle Wuxi. C'est une ville de taille moyenne, qui est juste à côté de Shanghai. En fait, je suis allé à Shanghai pour le lycée pendant trois ans et je faisais la navette. Après le lycée, je suis allé aux États-Unis pour l'université. Je pense que j'ai eu accès tôt aux ordinateurs, mais je ne me suis pas vraiment mis à la programmation. J'étais plus intéressé par les jeux, et j'ai beaucoup joué avec Flash quand j'étais au lycée, parce que j'aimais vraiment créer ces expériences de narration interactives.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4JPr5veRTbx8YOFXX2BPYw.jpeg)
_Evan avec son premier ordinateur, 1996_

#### Quelle a été votre première expérience de programmation ?

> « J'ai été attiré par JavaScript à cause de la capacité à simplement construire quelque chose et à le partager instantanément avec le monde. Vous le mettez sur le web, et vous obtenez une URL, vous pouvez l'envoyer à n'importe qui avec un navigateur. C'est la partie qui m'a attiré vers le web et vers JavaScript. »

Quand je suis allé à l'université aux États-Unis, honnêtement, je ne savais pas ce que je voulais faire et je faisais des études en arts plastiques et en histoire de l'art. Quand j'étais sur le point de terminer, j'ai réalisé qu'il était assez difficile de trouver un emploi dans les arts plastiques et l'histoire de l'art.

J'ai pensé que peut-être je pourrais aller dans un programme de master qui correspondait mieux à mes intérêts et développer plus de compétences. Je suis allé à Parsons et j'ai étudié le Master of Fine Arts pour le Design et la Technologie. C'était un programme vraiment cool parce que tout le monde était moitié designer et moitié développeur. Ils vous enseignaient des choses comme openFrameworks, processing, des animations algorithmiques, et vous deviez aussi concevoir des applications et des interfaces.

Parsons n'enseignait pas vraiment beaucoup de JavaScript, mais j'ai été attiré par JavaScript à cause de la capacité à simplement construire quelque chose et à le partager instantanément avec le monde. Vous le mettez sur le web, et vous obtenez une URL, vous pouvez l'envoyer à n'importe qui avec un navigateur. C'est la partie qui m'a attiré vers le web et vers JavaScript.

À l'époque, [Chrome experiments](https://www.chromeexperiments.com/) venait d'être lancé, et j'ai été totalement impressionné. Je me suis immédiatement plongé dans JavaScript et j'ai commencé à l'apprendre par moi-même, et j'ai commencé à construire des choses similaires aux Chrome experiments. J'ai mis ces choses dans mon portfolio et puis il a été repéré par le recruteur du Google Creative Lab. J'ai rejoint en tant que partie de [the Five program](https://www.creativelab5.com/). Chaque année, Creative Lab recrute cinq nouveaux diplômés. C'est essentiellement une petite équipe avec un rédacteur, un technologue créatif, un designer graphique, un stratège et un joker.

#### D'accord, quand ou comment avez-vous découvert le problème actuel que vous essayez de résoudre avec Vue.js ?

Mon travail chez Google impliquait beaucoup de prototypage dans le navigateur. Nous avions cette idée et nous voulions obtenir quelque chose de tangible le plus rapidement possible. Certains des projets utilisaient [Angular](https://angular.io/) à l'époque. Pour moi, Angular offrait quelque chose de cool qui est la liaison de données et une manière pilotée par les données de gérer le DOM, donc vous n'avez pas à toucher le DOM vous-même. Cela a également introduit tous ces concepts supplémentaires qui vous forçaient à structurer le code de la manière dont il voulait que vous le fassiez. Cela semblait trop lourd pour le cas d'utilisation que j'avais à l'époque.

Je me suis dit, et si je pouvais simplement extraire la partie que j'aimais vraiment dans Angular et construire quelque chose de vraiment léger sans tous les concepts supplémentaires impliqués ? J'étais également curieux de savoir comment fonctionnait sa mise en œuvre interne. J'ai commencé cette expérience en essayant simplement de reproduire cet ensemble minimal de fonctionnalités, comme la liaison de données déclarative. C'est ainsi que Vue a commencé.

J'ai travaillé dessus, et j'ai senti qu'il avait du potentiel, parce que j'aimais l'utiliser moi-même. J'ai mis un peu plus de temps dessus et je l'ai bien emballé, je lui ai donné un nom, je l'ai appelé [Vue.js](http://vuejs.org). C'était en 2013. Plus tard, je me suis dit, « Hé, j'ai mis tant de temps là-dedans. Peut-être devrais-je le partager avec les autres pour qu'ils puissent au moins en bénéficier, ou peut-être qu'ils le trouveront intéressant. »

En février 2014, c'est ainsi que je l'ai publié pour la première fois en tant que projet réel. Je l'ai mis sur Github et j'ai envoyé un lien à Hacker News, et il a été voté en première page. Il y est resté pendant quelques heures. Plus tard, j'ai [écrit](http://blog.evanyou.me/2014/02/11/first-week-of-launching-an-oss-project/) un article pour partager les données d'utilisation de la première semaine et ce que j'ai appris.

C'était ma première expérience de voir des gens aller sur Github et étoiler un projet. Je pense que j'ai obtenu plusieurs centaines d'étoiles dans la première semaine. J'étais super excité à l'époque.

#### Si vous deviez lister quelques éléments clés qui définissent Vue par rapport à d'autres frameworks, que diriez-vous ?

Je pense que, parmi tous les frameworks existants, Vue est probablement le plus similaire à [React](https://facebook.github.io/react/), mais dans un sens plus large, parmi tous les frameworks, le terme que j'ai inventé moi-même est un framework progressif. L'idée est que Vue est composé de ce noyau qui est simplement la liaison de données et les composants, similaire à React. Il résout un ensemble de problèmes très ciblés et limités. Comparé à React, Vue met un peu plus l'accent sur l'accessibilité. S'assurer que les personnes qui connaissent les bases telles que : HTML, JavaScript et CSS peuvent l'adopter le plus rapidement possible.

Au niveau du framework, nous avons essayé de le construire avec un noyau très léger et minimal, mais à mesure que vous construisez des applications plus complexes, vous avez naturellement besoin de résoudre des problèmes supplémentaires. Par exemple, le routage, ou comment vous gérez la communication entre les composants, partagez les états dans une application plus grande, et vous avez également besoin de ces outils de construction pour modulariser votre base de code. Comment organisez-vous les styles et les différents actifs de votre application ? Beaucoup des frameworks plus complets comme [Ember](http://emberjs.com/) ou [Angular](https://angularjs.org/), ils essaient d'être prescriptifs sur tous les problèmes que vous allez rencontrer et essaient de tout intégrer dans le framework.

C'est un peu un compromis. Plus vous faites d'hypothèses sur le cas d'utilisation de l'utilisateur, moins le framework sera flexible. Ou laisser tout à l'écosystème comme React — l'écosystème React est très, très vibrant. Il y a beaucoup de bonnes idées qui émergent, mais il y a aussi beaucoup de changements. Vue essaie de choisir un juste milieu où le noyau est toujours exposé comme un ensemble de fonctionnalités très minimal, mais nous offrons également ces pièces adoptables de manière incrémentielle, comme une solution de routage, une solution de gestion d'état, une chaîne d'outils de construction et le CLI. Ils sont tous maintenus officiellement, bien documentés, conçus pour fonctionner ensemble, mais vous n'êtes pas obligé de tous les utiliser. Je pense que c'est probablement la plus grande chose qui rend Vue en tant que framework différent des autres.

#### Comment avez-vous réussi à devenir financièrement durable avec Vue.js ?

> « Je crée de la valeur pour ces personnes, donc théoriquement, si je peux collecter ces valeurs sous une forme financière, alors je devrais être capable de subvenir à mes besoins. »

Je crée de la valeur pour ces personnes, donc théoriquement, si je peux collecter ces valeurs sous une forme financière, alors je devrais être capable de subvenir à mes besoins. Cela se complique parce qu'un framework JavaScript est relativement difficile à faire payer d'avance, étant donné le fonctionnement de l'écosystème JavaScript.

Vue a une base d'utilisateurs très dynamique. Beaucoup d'utilisateurs de Vue viennent de la communauté [Laravel](https://laravel.com/) et ils sont également des personnes vraiment enthousiastes et gentilles. Je me suis dit, est-ce que le crowdfunding fonctionnerait ? Je voulais juste essayer cette idée sur [Patreon](https://www.patreon.com/). En fait, [Dan Abramov](https://twitter.com/dan_abramov), le créateur de React-Hot-Loader et Redux, a également fait une petite campagne sur Patreon auparavant. C'est en fait ce qui m'intéresse. J'ai une idée approximative du nombre de personnes utilisant Vue. Disons qu'il y a 10 000 utilisateurs. Si peut-être 1 % d'entre eux est prêt à me donner dix dollars par mois, c'est quelque chose.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wMQeCCJqxyvzDNmmMVnraQ.png)
_Campagne Patreon d'Evan_

En février, j'ai lancé une [campagne Patreon](https://www.patreon.com/evanyou), et c'est une chose en deux parties. Une partie est ciblée vers les particuliers qui utilisent Vue. Typiquement, ils sont simplement prêts à donner une petite somme, un peu comme m'offrir un café. Ensuite, il y a l'autre camp avec des entités commerciales réelles, comme des start-ups ou des cabinets de conseil, qui ont construit des choses avec Vue. Il est important pour eux de voir que Vue est maintenu à long terme. Cela leur donne la tranquillité d'esprit de savoir que leur soutien financier rendra Vue plus durable et qu'ils peuvent se sentir en sécurité en l'utilisant à long terme.

Un autre aspect est les récompenses Patreon. Si les entreprises sont prêtes à nous sponsoriser, alors je pourrais mettre leur logo sur une page de sponsors sur vuejs.org. Cela augmente la sensibilisation de la communauté. La moitié des fonds Patreon provient de particuliers et l'un d'eux sponsorise 2000 $ par mois. Je ne savais pas si cela fonctionnerait lorsque je l'ai essayé, mais il s'avère que cela fonctionne. Je pense que j'ai fait le saut à temps plein lorsque j'avais 4000 $ par mois sur Patreon, et maintenant cela a augmenté à plus de 9800 $ par mois.

#### Avez-vous mis longtemps à les convaincre de vous sponsoriser ? Étaient-ils sceptiques, comme, vous êtes juste un jeune framework, vous ne durerez peut-être pas six mois ?

Lorsque j'ai lancé la campagne Patreon, Vue montrait déjà une croissance vraiment forte. Début 2015, Vue était largement encore juste un projet open source aléatoire, mais la communauté Laravel a commencé à adopter massivement Vue. J'ai eu l'impression que si je ne pouvais pas vraiment gagner d'argent avec cela, cela n'aurait pas de sens.

Je dois remercier particulièrement [Strikingly](https://www.strikingly.com), qui est une start-up basée à Shanghai. Ils sont vraiment activement impliqués dans les communautés JavaScript et Ruby en Chine. Ils n'utilisent pas vraiment beaucoup Vue, mais ils ont ce fonds mensuel qu'ils utilisent pour sponsoriser des projets open source. Ils ont été les premiers à sponsoriser 2000 $ par mois pendant six mois.

Cela a considérablement aidé dans la phase initiale. De plus, [Taylor Otwell](http://taylorotwell.com/), créateur de Laravel, sponsorise également Vue. Il a commencé avec 100, puis l'a augmenté à 200, et 500 avec le temps.

#### Vous avez mentionné que vous avez pu obtenir des sponsors parce que cela a grandi si rapidement. Avez-vous fait du marketing ? Ou est-ce que cela a grandi organiquement ?

Je dirais qu'il n'y a pas d'argent réel impliqué dans le marketing. Je n'ai pas acheté de publicités ou quoi que ce soit. C'est surtout juste écrire quelques articles de blog. Beaucoup de fois, je gérais simplement le compte Twitter. Je pense que c'est à peu près tout. Occasionnellement, j'écrivais un article sur Medium.

#### Vous avez fini par obtenir une grande traction sur les marchés internationaux, ce qui est probablement assez unique. Nous aimerions savoir comment cela s'est passé et quelques-uns des défis et meilleures pratiques pour engager les développeurs en dehors des États-Unis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JTnV4p9Y-6f-Yc3h8qYovQ.jpeg)
_JSConf Chine, 2015_

Le marché chinois est unique. Je suis chinois et je suis assez impliqué dans la communauté JavaScript chinoise. Beaucoup de gens connaissaient Vue parce qu'ils me connaissaient. Nous avions cette traduction complète de la documentation de Vue en chinois très bien écrit, ce qui a beaucoup aidé à l'adoption de Vue en Chine. Beaucoup d'utilisateurs savent aussi, « Hé, l'auteur de cette bibliothèque est chinois. » Ils se sentent naturellement enclins à au moins le vérifier, mais je pense que cela a beaucoup aidé dans les phases initiales. Vue a simplement commencé à être utilisé par de plus en plus d'entreprises en Chine, y compris des équipes chez Alibaba, Tencent et Baidu. Ce sont toutes des entreprises valorisées à plusieurs milliards de dollars en Chine. React a également une très grande part d'esprit en Chine.

Il y a un clone de Quora en Chine nommé [Zhihu](http://zhihu.com), les gens y posent toutes sortes de questions aléatoires et j'y réponds à beaucoup de questions sur JavaScript et Vue.js.

#### Avez-vous des suggestions pour les entreprises, les startups ou les projets open source qui ne peuvent pas facilement engager ou communiquer avec les communautés internationales ?

Je pense que la barrière de la langue est probablement la partie la plus difficile. L'idée est que si vous ne mettez pas vraiment d'efforts dédiés à promouvoir quelque chose en Chine, alors personne ne va le remarquer, à moins que vous ne soyez aussi grand que React. Vous avez besoin de quelqu'un qui peut parler chinois, quelqu'un qui peut parler chinois natif pour le faire.

Une autre chose intéressante est qu'il y a en fait de nombreux autres utilisateurs d'autres régions du monde comme l'Italie, l'Espagne, le Portugal et le Japon. Certains des contributeurs les plus actifs viennent du Japon. Ils sont vraiment, vraiment méticuleux dans la traduction des documentations.

#### Avez-vous fait des erreurs en construisant Vue que vous espérez ne plus jamais faire ?

> « Je dois complètement repenser le problème d'une certaine manière, mais je pense que c'est juste comme ça que se passe le développement logiciel parce que vous n'obtiendrez jamais rien de juste dès le premier essai. »

Hm, je sais, il y en a probablement quelques-unes. À ce jour, Vue a été réécrit de zéro deux fois. Évidemment, je l'ai réécrit parce que l'implémentation originale avait des problèmes qui ne pouvaient tout simplement pas être résolus par un refactoring progressif. C'est comme tous les six mois je regarde la base de code de six mois auparavant. Je vais être comme, wow. Comment cela a-t-il même fonctionné ?

Je dois complètement repenser le problème d'une certaine manière, mais je pense que c'est juste comme ça que se passe le développement logiciel parce que vous n'obtiendrez jamais rien de juste dès le premier essai.

Le voyage de la construction de Vue est aussi un voyage de croissance en tant que développeur, parce qu'avec le temps j'ai dû ajouter de nouvelles fonctionnalités, le maintenir, corriger des bugs et m'assurer que tout l'écosystème fonctionnait correctement ensemble. Cela vous expose naturellement à tous les problèmes que vous rencontreriez en tant qu'ingénieur logiciel. C'est juste un processus d'apprentissage.

#### Y a-t-il eu des difficultés émotionnelles ou non techniques que vous avez rencontrées avec Vue ?

> « Il n'y aura pas ce framework unique qui rendra tout le monde heureux. La partie la plus importante est de l'améliorer pour les personnes qui apprécient vraiment votre framework. Concentrez-vous sur ce que vous croyez être la chose la plus précieuse dans votre framework et assurez-vous simplement que vous faites un excellent travail, plutôt que de vous soucier de la façon dont vous vous comparez aux autres. »

Il y en a définitivement eu. Il y a beaucoup de pression en termes de compétition. Lorsque Vue était encore relativement inconnu, cette pression n'était pas là parce que toute exposition est bonne. Les gens ne vont pas vous tenir à un certain standard. Mais à mesure que Vue a grandi de plus en plus, naturellement les gens ont commencé à comparer Vue à des choses comme Angular ou React, et ils pointent des choses comme, « hé, React fait cela mieux. Angular fait cela mieux. »

Cela met beaucoup de pression sur vous et cela peut être stressant de devoir rivaliser avec tous les grands. Surtout maintenant que je fais cela à temps plein. La viabilité de Vue dans l'écosystème est directement liée à la qualité de mon travail.

Mais récemment, j'ai regardé une conférence de [Evan Czaplicki](https://twitter.com/czaplic), l'auteur d'Elm, où il parlait de la façon dont il avait une pression similaire lorsqu'il travaillait sur Elm. Il y avait [Om](https://github.com/omcljs/om), l'interface ClojureScript sur React. Il y avait [PureScript](http://www.purescript.org/), il y a d'autres langages fonctionnels qui compilent en JavaScript, il s'inquiétait aussi de la façon dont Elm pouvait rivaliser avec ces bibliothèques.

Plus tard, il a parlé à [Guido](https://twitter.com/gvanrossum), l'auteur de Python, et Guido lui a donné des conseils, il a dit, « fais simplement du bon travail ». L'idée derrière cela est que Python avait aussi ce problème. Il rivalise avec beaucoup de langages dynamiques, comme Ruby, JavaScript, Perl, et il est aussi dans le même domaine de problème. Il en résulte que tous ces langages qui réussissent à leur manière, et ils ont leur propre communauté dédiée qui les utilise et les apprécie.

Les gens préfèrent différents langages pour une raison. De même pour les frameworks JavaScript, les gens préfèrent différents frameworks pour une raison. Il n'y aura pas ce framework unique qui rendra tout le monde heureux. La partie la plus importante est de l'améliorer pour les personnes qui apprécient vraiment votre framework. Concentrez-vous sur ce que vous croyez être la chose la plus précieuse dans votre framework et assurez-vous simplement que vous faites un excellent travail, plutôt que de vous soucier de la façon dont vous vous comparez aux autres.

#### Que considéreriez-vous comme un résultat réussi pour Vue.js ?

C'est une question difficile parce que la portée de Vue.js a définitivement augmenté avec le temps. Nous avons maintenant tout cet écosystème de framework, et nous explorons également des choses comme [Weex](https://alibaba.github.io/weex/) qui rend les composants Vue dans une interface utilisateur native.

Je me soucie également beaucoup de la partie accessibilité de Vue, qui est enracinée dans la croyance que la technologie devrait permettre à plus de personnes de construire des choses.

#### Les prochaines questions sont juste des questions amusantes en dehors de la programmation. Quels sont vos autres hobbies ou intérêts en dehors de la programmation ?

Les anime, je lis beaucoup de manga. Au cas où vous ne l'auriez pas remarqué, les versions de Vue sont nommées avec des noms d'anime. Cela a commencé avec la version 0.09, chaque version majeure est nommée avec une lettre incrémentielle. La 2.0 est G qui est Ghost in the Shell. F est en fait réservé pour la 1.1. La 1.0 était Evangelion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hvV2aJXo9vKsNXjYTzODWQ.png)
_Illustration dessinée par un utilisateur japonais de Vue pour célébrer la sortie de la version 1.0 (nom de code Evangelion)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ea4hEK1X64TSYAu7Xlf-Kw.jpeg)
_Illustration de célébration pour Vue 2.0 (nom de code Ghost in the Shell)_

J'aime vraiment le karaoké.

#### Quelles sont les technologies ou tendances qui vous enthousiasment le plus ?

La technologie en général. C'est étrange parce que je ne suis pas super excité par la réalité augmentée ou virtuelle. Je veux vraiment parler de quelque chose qui est plus proche des développeurs. Quelque chose comme ce que Guillermo fait avec [Now](https://zeit.co/now). Les développeurs construisent des outils pour les développeurs, et l'expérience des développeurs avec ces outils, c'est aussi l'expérience utilisateur mais pour les outils de développement.

#### Qui sont vos héros de la programmation ? Si vous en avez.

Évidemment [TJ Holowaychuck](https://twitter.com/tjholowaychuk) et [Guillermo Rauch](https://twitter.com/rauchg). Je ne suis pas un majeur en informatique. J'ai essentiellement appris la programmation à travers des ressources en ligne aléatoires et des livres, mais une manière importante dont j'ai appris était simplement en lisant le code des autres. Quand je lis le code de TJ, j'ai toujours l'impression qu'il est vraiment élégant. C'est le mot qui me vient à l'esprit et cela m'a beaucoup affecté. TJ est définitivement un héros pour moi.

Ce projet est rendu possible grâce aux sponsors de [frontendmasters.com](https://frontendmasters.com/), [egghead.io](https://egghead.io/), [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge) et [Google Developers](https://developers.google.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*bMdgkbz1ZwgKR-Wp.png)
_Nos sponsors._

[Faire un don pour soutenir ce projet](https://opencollective.com/betweenthewires).

Pour suggérer un créateur que vous aimeriez entendre, veuillez remplir ce [formulaire](https://goo.gl/forms/XhR1IyLXJHNMljcp1).

Vous pouvez également envoyer des commentaires à [betweenthewires](https://twitter.com/betweenthewires) sur Twitter.