---
title: Leçons de ma première année de codage en direct sur Twitch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-07T17:24:42.000Z'
originalURL: https://freecodecamp.org/news/lessons-from-my-first-year-of-live-coding-on-twitch-41a32e2f41c1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*EyRimlrHNEKeFmS4.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
seo_title: Leçons de ma première année de codage en direct sur Twitch
seo_desc: 'By Suz Hinton

  I gave streaming a go for the first time last July. Instead of gaming, which the
  majority of streamers on Twitch do, I wanted to stream the open source work I do
  in my personal time. I work on NodeJS hardware libraries a fair bit (most ...'
---

Par Suz Hinton

J'ai essayé le streaming pour la première fois en juillet dernier. Au lieu de jouer, comme le font la majorité des streamers sur Twitch, je voulais diffuser le travail open source que je fais pendant mon temps personnel. Je travaille beaucoup sur des bibliothèques matérielles NodeJS (la plupart sont les miennes). Étant déjà dans une niche sur Twitch, pourquoi ne pas être dans une niche encore plus petite, comme le matériel alimenté par JavaScript ;) Je me suis inscrite sur [ma propre chaîne](https://www.twitch.tv/noopkat), et je diffuse régulièrement depuis.

Bien sûr, je ne suis pas la première à faire cela. [Handmade Hero](https://www.twitch.tv/handmade_hero) était l'un des premiers programmeurs que j'ai regardés coder en ligne, rapidement suivi par les développeurs de Vlambeer qui ont [développé Nuclear Throne en direct sur Twitch](http://nuclearthrone.com/twitch/). J'étais particulièrement fascinée par Vlambeer.

Ce qui m'a poussée à passer du stade de _souhaiter_ pouvoir le faire à celui de _le faire réellement_ est attribué à [Nolan Lawson](https://twitter.com/nolanlawson), un ami à moi. Je l'ai regardé [diffuser son travail open source un week-end](https://www.youtube.com/watch?v=9FBvpKllTQQ), et c'était génial. Il expliquait tout ce qu'il faisait en cours de route. Tout. Répondre aux problèmes sur GitHub, trier les bugs, déboguer le code dans les branches, vous l'appelez. J'ai trouvé cela fascinant, car Nolan maintient des bibliothèques open source qui sont beaucoup utilisées et actives. Sa vie open source est très différente de la mienne.

Vous pouvez même voir ce commentaire que j'ai laissé sous sa vidéo :

![Image](https://cdn-media-1.freecodecamp.org/images/0*tm8xC8CJV9ZimCCI.png)

J'ai essayé moi-même une semaine ou deux plus tard, après avoir configuré ma chaîne Twitch et m'être débrouillée avec OBS. Je crois que j'ai travaillé sur [Avrgirl-Arduino](https://github.com/noopkat/avrgirl-arduino), sur lequel je travaille encore fréquemment en streaming. C'était un premier stream difficile. J'étais très nerveuse, et j'avais veillé tard pour répéter tout ce que j'allais faire la veille.

Le petit nombre de spectateurs que j'ai eus ce samedi-là étaient vraiment encourageants, alors j'ai continué. Aujourd'hui, j'ai plus d'un millier de followers, et un sous-ensemble adorable d'entre eux sont des visiteurs réguliers que j'appelle « la famille noopkat ».

Nous nous amusons beaucoup, et j'aime appeler les parties de codage en direct « massivement multijoueur en ligne pair programming ». Je suis vraiment touchée par la gentillesse et l'esprit de tous ceux qui me rejoignent chaque week-end. L'un des moments les plus drôles que j'ai eus était lorsque l'un des membres de la famille a souligné que ma carte Arduino ne fonctionnait pas avec mon logiciel parce que la puce était manquante sur la carte :

J'ai souvent quitté un stream pour trouver dans ma boîte de réception que quelqu'un avait envoyé une pull request pour un travail que j'avais mentionné ne pas avoir le temps de commencer. Je peux honnêtement dire que mon travail open source a été changé pour le mieux, grâce à la générosité et à l'encouragement de ma communauté Twitch.

J'ai tellement plus à dire sur les avantages que le streaming sur Twitch m'a apportés, mais cela fera probablement l'objet d'un autre article de blog. Au lieu de cela, je veux partager les leçons que j'ai apprises pour toute autre personne qui aimerait essayer le codage en direct de cette manière. Récemment, quelques développeurs m'ont demandé comment ils pouvaient commencer, alors je publie les mêmes conseils que je leur ai donnés !

Tout d'abord, je vous dirige vers un guide intitulé [« Streaming and Finding Success on Twitch »](https://www.reddit.com/r/Twitch/comments/4eyva6/a_guide_to_streaming_and_finding_success_on_twitch/) qui m'a beaucoup aidée. Il est axé sur Twitch et les streams de gaming spécifiquement, mais il y a encore des sections pertinentes et de bons conseils. Je recommande de lire cela en premier avant de considérer d'autres détails sur le démarrage de votre chaîne (comme le choix de l'équipement ou des logiciels).

Mes propres conseils sont ci-dessous, que j'ai acquis de mes propres erreurs et de la sagesse des autres streamers (vous savez qui vous êtes !).

### Logiciel

Il existe de nombreux logiciels de streaming gratuits. J'utilise [Open Broadcaster Software (OBS)](https://obsproject.com). Il est disponible sur la plupart des plateformes. Je l'ai trouvé très intuitif pour commencer, mais d'autres mettent parfois un certain temps à apprendre comment il fonctionne. Votre expérience peut varier ! Voici une capture d'écran de ce à quoi ressemble ma configuration de 'scène de bureau' OBS aujourd'hui (cliquez pour une image plus grande) :

![Image](https://cdn-media-1.freecodecamp.org/images/0*s4wyeYuaiThV52q5.png)

Vous basculez essentiellement entre des 'scènes' pendant le streaming. Une scène est une collection de 'sources', superposées et composées les unes avec les autres. Une source peut être des choses comme une caméra, un microphone, votre bureau, une page web, du texte en direct, des images, la liste est longue. OBS est très puissant.

Cette scène de bureau ci-dessus est l'endroit où je fais tout mon codage en direct, et j'y reste principalement pendant toute la durée du stream. J'utilise iTerm et vim, et j'ai également une fenêtre de navigateur à portée de main pour basculer afin de consulter la documentation et trier les choses sur GitHub, etc.

Le rectangle noir en bas est ma webcam, afin que les gens puissent me voir travailler et avoir une connexion plus personnelle.

J'ai une poignée d'étiquettes pour mes scènes, dont beaucoup concernent les statistiques et les infos dans la bannière du haut. La bannière ajoute simplement de la personnalité, et est une source persistante d'informations pendant le streaming. C'est une image que j'ai créée dans [GIMP](https://www.gimp.org/), et vous l'importé comme une source dans votre scène. Certaines étiquettes sont des statistiques en direct qui proviennent de fichiers texte (comme le dernier follower). Une autre étiquette est [une étiquette personnalisée que j'ai créée](https://github.com/noopkat/study-temp) qui montre la température et l'humidité en direct de la pièce d'où je diffuse.

J'ai également configuré des 'alertes' dans mes scènes, qui montrent des bannières mignonnes par-dessus mon stream chaque fois que quelqu'un me suit ou fait un don. J'utilise le service web [Stream Labs](https://streamlabs.com/) pour cela, en l'important comme une source de page web dans la scène. Stream Labs crée également mon fichier texte de followers récents pour afficher dans ma bannière.

J'ai aussi un écran de veille que j'utilise lorsque je suis sur le point d'être en direct :

![Image](https://cdn-media-1.freecodecamp.org/images/0*cbkVjKpyWaWZLSfS.png)

J'ai également besoin d'une scène lorsque je saisis des jetons secrets ou des clés API. Elle me montre sur la webcam mais cache mon bureau avec une page web divertissante, afin que je puisse travailler en privé :

![Image](https://cdn-media-1.freecodecamp.org/images/0*gbhowQ37jr3ouKhL.png)

Comme vous pouvez le voir, je ne prends pas les choses trop au sérieux lorsque je diffuse, mais j'aime avoir une bonne configuration pour que mes spectateurs tirent le meilleur parti de mon stream.

Mais voici un vrai secret : j'utilise OBS pour rogner les bords inférieur et droit de mon écran, tout en gardant le même ratio de taille vidéo que ce que Twitch attend. Cela me laisse de l'espace pour surveiller mes événements (follows, etc.) en bas, et regarder et répondre à ma boîte de chat de chaîne sur la droite. Twitch vous permet de « pop out » la boîte de chat dans une nouvelle fenêtre, ce qui est vraiment utile.

Voici à quoi ressemble vraiment mon bureau complet :

![Image](https://cdn-media-1.freecodecamp.org/images/0*sENLkp3Plh7ZTjJt.png)

J'ai commencé à faire cela il y a quelques mois et je n'ai pas regardé en arrière. Je ne suis même pas sûre que mes spectateurs réalisent que c'est ainsi que fonctionne ma configuration. Je pense qu'ils prennent pour acquis que je peux tout voir, même si je ne peux pas voir ce qui est réellement diffusé en direct lorsque je suis occupée à programmer !

Vous vous demandez peut-être pourquoi j'utilise un seul moniteur. C'est parce que deux moniteurs étaient tout simplement trop à gérer en plus de tout le reste que je faisais pendant le streaming. J'ai compris cela rapidement et je suis restée avec un seul écran depuis.

### Matériel

J'ai utilisé du matériel moins cher pour commencer, et j'ai lentement acheté du matériel plus performant en réalisant que le streaming allait être quelque chose que je continuerais. Utilisez ce que vous avez lorsque vous commencez, même si c'est le microphone et la caméra intégrés de votre ordinateur portable.

De nos jours, j'utilise une webcam Logitech Pro C920, et un microphone Blue Yeti sur un bras de microphone avec un support anti-vibrations. Cela vaut vraiment le coût si vous avez les moyens. Cela a fait une différence dans la qualité de mes streams.

J'utilise un grand moniteur (27"), car comme je l'ai mentionné précédemment, utiliser deux moniteurs ne fonctionnait tout simplement pas pour moi. Je manquais des choses dans le chat parce que je ne regardais pas assez souvent le deuxième écran de l'ordinateur portable, etc. Votre expérience peut varier ici, mais avoir tout sur un seul écran était la clé pour que je puisse prêter attention à tout ce qui se passait.

C'est à peu près tout pour le matériel ; je n'ai pas une configuration très compliquée.

Si vous êtes intéressé, mon bureau semble assez normal à l'exception du microphone imposant :

![Image](https://cdn-media-1.freecodecamp.org/images/0*EyRimlrHNEKeFmS4.jpg)

### Conseils

Cette dernière section contient quelques conseils généraux que j'ai appris, qui ont rendu mon stream meilleur et plus agréable dans l'ensemble.

#### Panneaux

Prenez le temps de créer de superbes panneaux. Les panneaux sont les petites boîtes de contenu en bas de la page de chaîne de tout le monde. Je les vois comme les nouvelles boîtes de profil MySpace (lol mais vraiment). Les idées de panneaux pourraient être des choses comme les règles de chat, des informations sur quand vous diffusez, quel ordinateur et équipement vous utilisez, votre race de chat préférée ; tout ce qui crée une touche personnelle. Regardez d'autres chaînes (surtout les populaires) pour des idées !

Un exemple de l'un de mes panneaux :

![Image](https://cdn-media-1.freecodecamp.org/images/0*HlLs6xlnJtPwN4D6.png)

#### Chat

Le chat est vraiment important. Vous allez recevoir les mêmes questions encore et encore lorsque les gens rejoignent votre stream à moitié, donc avoir des 'macros' de chat peut vraiment aider. « Qu'est-ce que tu fais ? » est la question la plus courante posée pendant que je code. J'ai des raccourcis de chat 'commandes' pour cela, que j'ai créés avec [Nightbot](https://beta.nightbot.tv/). Cela affichera une explication de quelque chose que j'ai entré à l'avance, en tapant une petite commande d'un mot comme _!questcequeje fais_

Lorsque les gens posent des questions ou laissent des commentaires sympas, parlez-leur ! Dites merci, dites leur pseudo Twitch, et ils apprécieront vraiment l'attention et la reconnaissance. C'est SUPER difficile de rester à jour lorsque vous commencez à streamer, mais le multitâche deviendra plus facile à mesure que vous le ferez plus. Essayez de prendre quelques secondes toutes les quelques minutes pour regarder le chat pour de nouveaux messages.

Lorsque vous programmez, _expliquez ce que vous faites_. Parlez beaucoup. Faites des blagues. Même lorsque je suis bloquée, je dis : « oh, zut, j'ai oublié comment utiliser cette méthode, laissez-moi la chercher sur Google hahaha » et les gens sont toujours sympas et parfois ils lisent même avec vous et vous aident. C'est amusant et engageant, et cela garde les gens à regarder.

Je perds rapidement l'intérêt lorsque je regarde des streams de programmation où le streamer est assis en silence à taper du code, ignorant le chat et les alertes de nouveaux followers.

Il est très probable que 99 % des personnes qui trouvent leur chemin vers votre chaîne soient amicales et curieuses. J'ai parfois des trolls, mais les outils de modération offerts par Twitch et Nightbot aident vraiment à décourager cela.

#### Temps de préparation

Automatisez votre configuration autant que possible. Mon terminal est iTerm, et il vous permet d'enregistrer les arrangements de fenêtres et les tailles de police afin de pouvoir les restaurer plus tard. J'ai un arrangement de fenêtre pour le streaming et un pour le non-streaming. C'est un gain de temps énorme. Je tape une commande et tout est de la taille parfaite et à la bonne position, prêt à partir.

Il existe d'autres applications qui automatisent toutes les placements de vos fenêtres d'applications, jetez un coup d'œil pour voir si l'une d'entre elles pourrait également aider.

Rendez la taille de votre police vraiment grande dans votre terminal et votre éditeur de code afin que tout le monde puisse voir.

#### Régularité

Soyez régulier avec votre emploi du temps. Je ne diffuse qu'une fois par semaine, mais toujours à la même heure. Faites savoir aux gens si vous n'êtes pas en mesure de diffuser pendant un moment attendu où vous le faites normalement. Cela m'a valu un public régulier. Certaines personnes aiment la routine et c'est exactement comme retrouver un ami. Vous êtes dans un cercle social avec votre communauté, alors traitez-la de cette manière.

Je veux diffuser plus souvent, mais je sais que je ne peux pas m'engager à plus d'une fois par semaine à cause des voyages. J'essaie de trouver un moyen de diffuser en haute qualité lorsque je suis sur la route, ou peut-être simplement avoir des discussions informelles et garder la programmation pour mon stream régulier du dimanche. Je suis encore en train de comprendre cela !

#### Gêne

Cela va sembler bizarre lorsque vous commencez. Vous allez vous sentir nerveux à l'idée que des gens vous regardent coder. C'est normal ! J'ai ressenti cela très fortement au début, même si j'ai de l'expérience en prise de parole en public. J'avais l'impression qu'il n'y avait nulle part où me cacher, et cela m'a fait peur. Je pensais : « tout le monde va penser que mon code est mauvais, et que je suis une mauvaise développeuse ». C'est un schéma de pensée qui m'a hantée toute ma carrière, ce n'est pas nouveau. Je savais qu'avec cela, je ne pouvais pas refactoriser discrètement le code avant de le pousser sur GitHub, ce qui est généralement beaucoup plus sûr pour ma réputation en tant que développeuse.

J'ai beaucoup appris sur mon style de programmation en codant en direct sur Twitch. J'ai appris que je suis définitivement du type « fais-le fonctionner, puis rend-le lisible, puis rend-le rapide ». Je ne répète plus la veille (j'ai abandonné cela après 3 ou 4 streams tout au début), donc j'écris un code assez brut sur Twitch et je dois être d'accord avec cela. J'écris mon meilleur code lorsque je suis seule avec mes pensées et que je ne regarde pas une boîte de chat + parle à voix haute, et c'est bien. J'oublie les signatures de méthodes que j'ai utilisées des milliers de fois, et je fais des erreurs 'bêtes' dans presque chaque stream. Pour la plupart, ce n'est pas un environnement productif pour être à son meilleur.

Ma communauté Twitch ne me juge jamais pour cela, et ils m'aident beaucoup. Ils comprennent que je fais du multitâche, et sont vraiment géniaux pour les conseils et suggestions pragmatiques. Parfois ils me sauvent, et d'autres fois je dois leur expliquer pourquoi leur suggestion ne fonctionnera pas. C'est vraiment comme du pair programming régulier !

Je pense que l'approche 'avec tous les défauts' de ce média est une force, pas une faiblesse. Cela vous rend plus accessible, et il est important de montrer qu'il n'y a pas de programmeur parfait, ni de code parfait. C'est probablement assez rafraîchissant pour les nouveaux codeurs à voir, et humiliante pour moi en tant que codeuse plus expérimentée.

### Conclusion

Si vous avez envie de vous lancer dans le codage en direct sur Twitch, je vous encourage à essayer ! J'espère que cet article vous a aidé si vous vous demandiez par où commencer.

Si vous souhaitez me rejoindre le dimanche, vous pouvez [suivre ma chaîne sur Twitch](https://www.twitch.tv/noopkat) :)

Pour finir, je tiens à remercier personnellement [Mattias Johansson](https://twitter.com/mpjme) pour sa sagesse et son encouragement au début de mon parcours de streaming. Il a été incroyablement généreux, et sa [chaîne YouTube FunFunFunction](https://www.youtube.com/channel/UCO1cgjhGzsSYb1rsB4bFe4Q) est une source continue d'inspiration.

**Mise à jour :** plusieurs personnes ont demandé des informations sur mon clavier et d'autres parties de mon poste de travail. [Voici la liste complète de ce que j'utilise](https://gist.github.com/noopkat/5de56cb2c5917175c5af3831a274a2c8). Merci pour l'intérêt !