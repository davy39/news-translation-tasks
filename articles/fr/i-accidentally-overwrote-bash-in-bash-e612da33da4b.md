---
title: Cette fois où j'ai accidentellement écrasé Bash… dans Bash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-13T04:04:01.000Z'
originalURL: https://freecodecamp.org/news/i-accidentally-overwrote-bash-in-bash-e612da33da4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FIjDPNm9zRO_ESbUiGmCXA.png
tags:
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Cette fois où j'ai accidentellement écrasé Bash… dans Bash
seo_desc: 'By Jacob Evelyn

  “I know what I’m doing.”

  Five years ago, a few weeks into my very first Programming Job™, I was tinkering
  around in bash trying to get some code to run.

  I was becoming increasingly frustrated. Why wasn’t that file in my $PATH? It shou...'
---

Par Jacob Evelyn

### _"Je sais ce que je fais."_

Il y a cinq ans, quelques semaines après le début de mon tout premier emploi de programmeur, je bidouillais dans `bash` en essayant de faire fonctionner un code.

Je devenais de plus en plus frustré. Pourquoi ce fichier n'était-il pas dans mon `$PATH` ? Il aurait dû y être, j'en étais certain.

Mais, devenant de plus en plus désespéré pour faire fonctionner _quelque chose_, j'ai déplacé le fichier vers un dossier que je _savais_ être dans le `$PATH` :

```
> mv ./file.whatever /bin
```

En tout cas, c'est ce que je _voulais_ taper. En réalité, j'ai tapé :

```
> mv ./file.whatever /bin/bash
```

Mon MacBook Pro fourni par l'employeur m'a crié dessus, comme tout bon système UNIX :

```
mv: rename ./file.whatever to /bin/bash: Operation not permitted
```

Et comme tout bon programmeur, j'ai aveuglément ajouté un `sudo` et tapé mon mot de passe aussi vite que possible. _Stupid computer, thinking it knows better than me._

Venant d'écraser sans le savoir le shell que j'utilisais, j'ai été choqué de constater que mon code ne fonctionnait toujours pas.

### "Je ne sais pas ce que je fais, mais ce n'est pas grave."

J'ai ouvert un nouvel onglet Terminal OS X pour essayer une nouvelle approche pour faire fonctionner mon code, et j'ai plutôt vu ceci :

```
> permission denied: ./file.whatever
```

```
[Process completed]
```

_Hmm, c'est bizarre. Je ne suis pas sûr pourquoi `bash` ne fonctionne pas, mais au moins il fait quelque chose avec mon fichier !_

Je suis revenu à mon shell `bash` précédemment ouvert et j'ai continué à essayer quelques commandes. Elles fonctionnaient toujours, bien sûr, parce que le programme `bash` était déjà en mémoire au moment où j'ai écrasé son exécutable.

_Donc certains onglets Terminal ne fonctionnent pas, mais d'autres oui. Probablement des fantômes dans la machine._

Pour régler ce comportement bizarre mais définitivement probablement pas grave de `bash`, j'ai décidé de faire le remède universel : quitter l'application (Terminal) et la rouvrir.

### "Oh mon dieu ! Qu'ai-je fait ?"

Sans prévenir, la réalité de ce qui s'était passé m'a frappé comme une boule de neige en pleine figure. _Oh non oh non oh non j'ai juste écrasé Bash._

![Image](https://cdn-media-1.freecodecamp.org/images/4Mt5wOpqo6cWWlPWw-uY-bUFZw6kxWpRVEQL)

Je ne me souciais plus de faire fonctionner mon code. Tout ce que je voulais, c'était revenir à la situation précédente.

### "C'est probablement réparable…"

J'ai passé beaucoup de temps à chercher sur Google des choses comme "deleted bash" et "download new bash OS X" sans résultat. J'étais trop paniqué pour penser à utiliser d'autres shells — que je connaissais vaguement, mais dont je ne réalisais pas qu'ils étaient déjà installés sur ma machine. (Et je ne réalisais certainement pas que ces shells étaient également utilisables en changeant simplement un paramètre dans l'application Terminal. #facepalm)

Finalement, j'ai avoué timidement à quelques collègues ce que j'avais fait et après que nous ayons tous bien rigolé, l'un d'eux m'a envoyé une copie de son programme `bash` pour que je puisse le déplacer manuellement dans le dossier `/bin` dans Finder. (Hourra pour les interfaces point-and-click !)

Sauf que… Finder ne me permettait pas d'aller dans le dossier `/bin`. OS X (cette version, en tout cas) cachait `/bin` et d'autres dossiers système qu'il jugeait dangereux pour les utilisateurs comme moi. _Stupid computer, thinking it knows better than me._

J'ai donc cherché à nouveau sur Google, cette fois pour des choses comme "view hidden folders in Finder". J'ai trouvé plusieurs façons de le faire, mais _chacune d'entre elles_ nécessitait que je tape une commande magique… dans `bash`, que je ne pouvais plus ouvrir. Les enfants : si vous supprimez votre shell mais que vous en avez une instance ouverte, ne la fermez pas !

### "OK… c'est peut-être réparable…"

À court d'idées, j'ai trouvé un ancien système interne de questions-réponses de l'entreprise et j'ai posté une description rapide de mon problème, essayant de trouver le bon ton entre _heh quelle situation drôle mais probablement pas rare, n'est-ce pas tout le monde ?_ et _s'il vous plaît quelqu'un n'importe qui aidez-moi je panique_. Le site semblait ne plus être utilisé, mais j'espérais que quelqu'un recevrait un email lorsqu'une question était postée.

Et voilà, mon Hail Mary a rapidement obtenu une réponse : quelqu'un a recommandé de démarrer à partir d'un CD Live Linux (c'était à l'époque où les ordinateurs avaient des lecteurs CD), puis, depuis Linux, d'accéder à mon système de fichiers OS X pour remettre `bash` à sa place. J'ai compris environ un tiers de la suggestion, mais j'ai continué quand même — quelles autres options avais-je ? J'ai trouvé un CD Linux, fait un tas de choses que je ne comprenais pas pour le faire fonctionner, et j'ai attendu impatiemment que la machine passe par toutes les étapes de configuration jusqu'à ce que — _voilà !_ Un bureau est apparu !

J'ai cherché sur Google jusqu'à ce que je trouve comment monter le système de fichiers OS X, et j'ai ouvert `bash` avec empressement (quelle bonne sensation !) pour copier l'exécutable `bash` de cette machine vers OS X… pour tomber sur un message d'erreur : la partition OS X était en lecture seule depuis Linux. J'ai trouvé un moyen de la rendre accessible en écriture, mais cela nécessitait de redémarrer sous OS X et — vous l'aurez deviné — d'exécuter une commande dans `bash`.

J'ai essayé quelques CD Live Linux différents (chacun prenant environ quarante minutes de marche impatiente pour démarrer), mais chacun avait le même résultat. Une fois de plus : si vous supprimez votre shell mais que vous en avez une instance ouverte, **_ne_** la fermez pas !

### "Que signifie réparable de toute façon ?"

Incertain de la marche à suivre, j'ai de nouveau demandé de l'aide à mes collègues et _eureka !_ — quelqu'un savait comment naviguer vers n'importe quel dossier — même ceux cachés — dans Finder. Tout ce que j'avais à faire était de redémarrer sous OS X, copier l'exécutable `bash` envoyé par email dans `/bin`, et tout serait réglé. J'ai donc éteint Linux, retiré le CD Live, redémarré sous OS X, et…

Hmm. Je ne pouvais pas me connecter, parce que, eh bien, le processus de connexion OS X utilise un shell en arrière-plan, et devinez quel shell c'est ?

Étais-je condamné à passer le reste de ma carrière à vivre avec des CD Live Linux ? Je m'imaginais des années plus tard, un ermite balbutiant gardé pour faire peur aux nouveaux : _"Ne supprimez pas bash ou vous finirez comme le vieux Jake fou."_

![Image](https://cdn-media-1.freecodecamp.org/images/L3idR4cUHdlM2acBE01yx7PyhgsuELGt38j8)

### "Je n'ai jamais été aussi heureux de voir un message d'erreur"

J'avais perdu tout espoir, quand un autre collègue (bon sang, ces gens en savaient beaucoup !) m'a parlé du [mode mono-utilisateur](https://en.wikipedia.org/wiki/Single_user_mode), un mode de démarrage spécial OS X qui aide à résoudre les erreurs de connexion (et autres). Le mode mono-utilisateur m'a permis de démarrer une version minimaliste, en ligne de commande de OS X via un autre shell (`/bin/sh`, je pense). À partir de là, il ne restait plus qu'à trouver les bonnes incantations pour remettre l'exécutable `bash` dans `/bin` et hors d'une clé USB (où je l'avais mis dans une autre itération douloureusement lente du démarrage du CD Live Linux).

Une fois cela fait, j'ai redémarré le Mac et tout était enfin rentré dans l'ordre ! Enfin, sauf que bien sûr mon code ne fonctionnait toujours pas.