---
title: Comment j'ai commencé mon parcours open source après avoir été démotivée pendant
  deux ans
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T00:00:53.000Z'
originalURL: https://freecodecamp.org/news/how-i-started-my-open-source-journey-after-being-demotivated-for-two-years-db4ebc6ecb84
coverImage: https://cdn-media-1.freecodecamp.org/images/0*goprda8-nuOX0ezK
tags:
- name: JavaScript
  slug: javascript
- name: Mozilla
  slug: mozilla
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai commencé mon parcours open source après avoir été démotivée
  pendant deux ans
seo_desc: 'By Hemakshi Sachdev


  Contributing to open source is very difficult. The people who do are experts with
  years of experience and we are just beginners — it’s not meant for us.


  Those were the exact words of my friends when I first asked them about what...'
---

Par Hemakshi Sachdev

> Contribuer à l'open source est très difficile. Les personnes qui le font sont des experts avec des années d'expérience et nous ne sommes que des débutants — ce n'est pas fait pour nous.

Ce sont les mots exacts de mes amis lorsque je leur ai demandé pour la première fois ce qu'étaient l'open source et le Google Summer of Code et comment nous pouvions y contribuer. Le complexe d'infériorité en moi (ou devrais-je dire la supériorité que je leur accordais pour être un peu plus avancés en codage que moi) m'a fait croire leurs mots pendant deux longues années. J'avais donc totalement abandonné l'idée de contribuer un jour à l'open source.

Mais aujourd'hui, me voilà avec 12 PR soumis avec succès et 3 en cours de révision pour des organisations comme Mozilla, freeCodeCamp et Gatsbyjs. Et devinez quoi ? Je suis toujours à l'université et j'ai presque zéro expérience de travail dans une organisation ou une entreprise !

Alors, si vous êtes quelqu'un qui pense que l'open source n'est pas fait pour vous, comme je le pensais, alors arrêtez tout de suite !

Comment tout a commencé ?

### Un peu de contexte sur moi ??

Mon parcours en codage a commencé il y a trois ans lorsque j'ai appris à coder en langage C. Depuis, j'ai appris le C++, les algorithmes et les structures de données, et j'ai résolu des centaines de problèmes algorithmiques et logiques sur plusieurs sites comme CodeChef, SPOJ, HackerRank et Codeforces.

Plus tard, j'ai passé à l'apprentissage du développement web avec [freeCodeCamp](https://www.freecodecamp.org/). J'ai aimé leur programme et surtout leurs projets. Mais le meilleur était leur communauté libre et ouverte, toujours prête à vous aider. Beaucoup de gens m'ont aidé à clarifier mes doutes sur le forum ou le salon de discussion Gitter, et les réponses étaient toujours encourageantes.

J'ai littéralement senti que je devais quelque chose à la communauté et j'ai toujours cherché des personnes à qui je pouvais apporter de l'aide. Pour être honnête, cela faisait toujours du bien lorsque j'aidais quelqu'un avec ses questions et problèmes sur le salon de discussion de freeCodeCamp. Après un an, l'idée de contribuer à l'open source est revenue dans mon esprit. J'ai discuté de mon souhait de contribuer avec ces mêmes amis, mais tout ce que j'ai obtenu, ce sont les mêmes mots qu'avant. J'ai laissé cette pensée s'envoler pour la deuxième fois.

### Cette petite étincelle de confiance en soi et de courage ?

Après avoir réussi mon stage et obtenu un emploi, j'étais totalement libre pendant ma dernière année de licence. L'idée du Google Summer of Code est à nouveau venue dans mon esprit. Comme c'était probablement ma dernière chance de participer au GSoC, et que je ne voulais pas avoir de regrets après avoir quitté l'université et avant d'entrer dans le monde réel, je me suis enfin dit :

> Essayons simplement. Au pire, je pourrais échouer, mais au moins je saurai que j'ai essayé ! Je ne veux pas laisser passer une opportunité juste parce qu'une personne m'a dit que je ne pouvais pas le faire !

J'ai tout recherché sur l'open source, quelles organisations commencer, comment trouver quelque chose à contribuer, chaque petite chose !

Enfin, j'ai décidé de choisir Mozilla car c'était l'organisation la plus adaptée aux débutants. Comme Mozilla est une très grande organisation, elle a beaucoup de produits sous son égide, et à nouveau cette grande question est venue : quel produit devrais-je choisir ?

Avec l'aide de leur [page d'introduction](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Introduction) et en apprenant mes propres intérêts, j'ai choisi Firefox DevTools. Pourquoi DevTools ? Parce que pour moi, il n'y a rien de mieux que d'aider les autres à apprendre, à s'améliorer et à grandir. Et le fait que quelque chose développé ou implémenté par moi pourrait aider les autres à apprendre était le meilleur sentiment que je pouvais imaginer.

### La vraie lutte commence ?

Je vais être honnête ici, avant de commencer, tout semblait intimidant. Mais une fois que tout est fait, vous commencez à trouver que tout est un jeu d'enfant. La première et plus importante étape est d'obtenir et de construire le code. Presque toutes les organisations ont un guide très détaillé étape par étape pour cela. J'ai eu beaucoup de mal à obtenir le code. La base de code de Firefox est É N O R M E ! Et grâce à la connexion internet lente qui a empiré les choses. Après trois jours de lutte, j'ai enfin pu obtenir le code et j'ai pu construire Firefox localement en suivant attentivement les étapes mentionnées dans la documentation.

Maintenant que j'avais tout fait fonctionner, l'étape suivante était de trouver quelque chose sur quoi travailler ! J'ai parcouru tous les `[good-first-bugs](https://bugs.firefox-dev.tools/?easy&tool=all)` et j'ai commenté ceux que je trouvais intéressants en me présentant et en montrant mon intérêt à résoudre le problème. J'ai été assignée à l'un d'eux.

Chaque mentor sait que nous sommes nouveaux dans l'open source. Trouver cet endroit où nous devons faire des changements est comme chercher une aiguille dans une botte de foin. Ils nous guident donc vers les fichiers de code et parfois même vers les numéros de ligne où nous devons analyser le problème et faire les changements demandés. Et même s'ils ne le font pas, vous avez tout à fait le droit de leur demander et ils vous aideront avec plaisir.

Pendant les 10 jours suivants, tout ce que j'ai fait a été d'étudier le code, de déboguer, de construire, d'exécuter et d'analyser... mais je n'ai pas pu trouver de solution ou de conclusions ! ? Finalement, j'ai décidé de prendre toutes mes analyses et résultats et de demander de l'aide à mon mentor. Parfois, vous devez demander de l'aide parce que sans cela, vous ne pouvez pas avancer ! Tout le code est nouveau pour vous et personne n'est censé le comprendre en quelques jours.

Mon mentor a réalisé que ce n'était pas un problème de type `good-first-bugs` et l'a résolu lui-même. Pour être honnête, c'était un peu déprimant. Mais mon mentor m'a donné un autre problème à résoudre qui était comparativement assez facile et je l'ai finalement résolu après un jour ou deux d'analyse ! Oui, j'ai enfin pu soumettre mon premier patch (PR) ! Mais le faire accepter n'était vraiment pas si facile, tant d'erreurs mineures et d'erreurs ESLint qui étaient littéralement frustrantes. Finalement, après 3 à 4 tours de révisions, mon patch a été accepté ! Youpi ! ?

Après avoir soumis mon premier patch, j'ai rapidement commencé à chercher d'autres problèmes à résoudre. J'ai continué à résoudre quelques autres `good-first-bugs` mais j'ai vite réalisé que je voulais résoudre des problèmes qui impliquaient plus que de simples changements mineurs et qui étaient un peu plus complexes. Je n'étais toujours pas sûre de mes intérêts et je voulais donc explorer quelques autres organisations. J'ai donc résolu quelques problèmes sur les Taskclusters de Mozilla, freeCodeCamp et Gatsbyjs également. Mais très vite, j'ai réalisé que Firefox DevTools était celui que je préférais ? et j'ai continué à y contribuer.

Voici à quoi ressemble le processus de contribution à l'open source :

1. Trouver un problème sur lequel travailler.
2. Étudier la base de code et comprendre ce qui doit être fait.
3. Coder. Poser des questions. Commiter.
4. Soumettre un patch.
5. Résoudre les commentaires de révision et faire accepter le patch.
6. Retour à l'étape 1.

### Notes finales

À toutes les personnes qui lisent ceci, j'espère avoir pu vous motiver et vous faire réaliser que vous êtes capable de contribuer à l'open source — parce que la vérité est que vous l'êtes ! En fait, il n'est même pas nécessaire de connaître un langage de programmation particulier, car vous pouvez toujours aider avec la documentation ou signaler des bugs détaillés et vous pouvez toujours apprendre en cours de route.

Oui, je sais que nous ne faisons peut-être pas de grandes contributions à la base de code ou que nous ne lançons pas de grands projets open source, mais ces petites contributions sont tout aussi importantes que les plus grandes. Et il est juste de dire que _les petites gouttes d'eau font les grands océans_. Vous ne savez jamais quand votre petite contribution pourrait se révéler si utile pour les autres et un jour vous pourriez aussi vous retrouver avec ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Bgl9xDj3ta2X2NQEmDYCuyDiopyE4AgMVo18)

Oui ! J'ai été reconnue par Firefox DevTools pour l'une de mes contributions. ✨ Voici le [tweet](https://twitter.com/FirefoxDevTools/status/1116361470500057088).

Alors à tous les débutants en open source ou à ceux qui veulent commencer avec l'open source, je veux juste dire ceci : oubliez ce que les autres pensent et croient et souvenez-vous seulement de ce que vous voulez faire. Vous êtes capable, et c'est tout ce qui compte à la fin. Faites simplement ce premier pas sans crainte et le monde vous guidera plus loin — ou devrais-je dire que les mentors vous guideront plus loin. ?

Enfin, j'aimerais remercier tous mes mentors et les mainteneurs open source qui m'ont aidée dans mon parcours et qui continueront à le faire à l'avenir. Un remerciement spécial à [Jan Honza Odvarko](https://github.com/janodvarko) et [Nicolas Chevobbe](https://github.com/nchevobbe) pour m'avoir aidée, répondu et clarifié tous mes doutes et questions, et fait preuve de tant de patience en me mentorant. **Merci beaucoup ! ❤️**

Toute personne qui a besoin d'aide pour commencer avec l'open source ou la programmation, n'hésitez pas et envoyez-moi un email à sachdev.hemakshi[at]gmail[dot]com. J'adore recevoir des emails ?.

Merci à l'équipe de freeCodeCamp pour avoir publié cet article. ?