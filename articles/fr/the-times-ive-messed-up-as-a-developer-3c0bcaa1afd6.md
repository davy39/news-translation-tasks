---
title: Un bref plongeon dans deux moments où je n'avais clairement aucune idée de
  ce que je faisais en tant que développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T11:36:37.000Z'
originalURL: https://freecodecamp.org/news/the-times-ive-messed-up-as-a-developer-3c0bcaa1afd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6dix1lxlAXUO7Gg4EPjgBg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Un bref plongeon dans deux moments où je n'avais clairement aucune idée
  de ce que je faisais en tant que développeur
seo_desc: 'By Zachary Kuhn

  Last week I had a short conversation with coworkers about how we had messed up in
  our careers. Being so far removed from those mistakes, it was easy to laugh. More
  than laughs, though, these screw-ups served as powerful lessons for us...'
---

Par Zachary Kuhn

La semaine dernière, j'ai eu une courte conversation avec des collègues sur la façon dont nous avions fait des erreurs dans nos carrières. Étant si éloignés de ces erreurs, il était facile d'en rire. Plus que des rires, cependant, ces erreurs ont servi de leçons puissantes pour nous.

Il est important que nous partagions nos erreurs afin que les autres puissent en tirer des leçons et peut-être se sentir plus à l'aise avec les leurs. Voici donc quelques-unes de mes erreurs les plus récentes.

### Pourquoi tant de bases de données de production supprimées ?

![Image](https://cdn-media-1.freecodecamp.org/images/6Scwn1EYrNsLjS9YXCF0ZaiO600eVCqUp-8F)
_Source : [pexels.com](https://www.pexels.com/photo/interior-of-office-building-325229/" rel="noopener" target="_blank" title=")_

Il y a quelques mois, il y avait [un post sur Reddit](https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/) d'un développeur de niveau débutant qui a supprimé la base de données de production dès son premier jour. Nous frémissons tous en lisant des histoires comme celle-ci de ceux qui font ces grandes erreurs inoubliables. Nous réalisons qu'il n'en faudrait pas beaucoup pour que cela nous arrive à nous — la plupart d'entre nous ont eu des appels proches.

Lors de mon premier emploi, un administrateur de base de données senior a supprimé la base de données de production dès son premier jour. Ces histoires sont partout. L'équipe a restauré son erreur à partir d'une sauvegarde d'une semaine et l'a gardé. Dix ans plus tard, ils se moquaient encore de lui pour cela.

Un matin, plus tôt cette année, on m'a appelé pour examiner un problème de production pour un client. Ils commençaient à tester leur site en version bêta avec un petit public lorsque, du jour au lendemain, la page d'accueil de leur site ne contenait plus rien. Je me suis demandé s'il y avait un bug ou une vulnérabilité qui avait conduit à cela.

Je me suis connecté à la machine de production et j'ai ouvert la base de données. La table des articles était vide. D'accord, cela confirmait ce que nous voyions sur le site web.

La table des utilisateurs contenait toujours des utilisateurs. Bizarre. Donc nous avons perdu tous nos articles, mais au moins leurs utilisateurs bêta avaient toujours leurs comptes. Nous pouvions expliquer que c'était une bêta et que ces choses arrivent.

Les quelques moments suivants furent flous. Je ne me souviens pas exactement de ce que j'ai fait. Je ne _pense_ pas avoir été assez stupide pour taper `drop table users` dans la console. Mais me voilà, maintenant sans articles et sans table d'utilisateurs. Je suis resté là, choqué, pendant un moment.

Ensuite, mon esprit s'est emballé sur la façon de réparer cela. Avais-je vraiment supprimé la table des utilisateurs ? Oui. Avions-nous fait des sauvegardes ? Non. Comment allons-nous dire cela au client ? Je ne sais pas.

Je me souviens être allé voir le chef de projet, m'être assis à côté d'elle et avoir expliqué ce qui s'était passé. Nous n'avions pas de données dans notre table d'articles, c'est pourquoi le site semblait vide. Et oh oui, j'ai aussi supprimé la table des utilisateurs. Ils allaient maintenant devoir réinviter tous ces utilisateurs — s'ils pouvaient découvrir qui ils étaient tous. Aïe.

Je suis retourné à mon bureau en me sentant vaincu.

**Cependant, quelque chose ne me semblait pas juste.** Comment avions-nous perdu tous ces articles en premier lieu ?

J'ai continué à creuser. En partie par déni, en partie par envie de sauver la face. Peu après, j'ai remarqué quelque chose d'important.

Il y avait cinq autres bases de données sur le serveur. L'une d'elles avait un nom similaire à la base de données que je venais de consulter.

Lorsque je l'ai vérifiée, tous les articles y étaient. La table des utilisateurs était intacte. Il s'avère qu'un changement de configuration avait été inadvertamment déployé en production, faisant pointer le site vers une toute nouvelle base de données. Ces utilisateurs que j'ai vus ? Des données de seed.

Quel soulagement ! Une matinée de nerfs et d'acide gastrique me rendant malade, mais nous avons pu "récupérer" toutes les données et j'avais trouvé le vrai problème avant de communiquer la mauvaise nouvelle.

Beaucoup de leçons tirées de cet épisode. L'une des plus simples : maintenant, nous faisons toujours des sauvegardes... peut-être l'antiacide le plus efficace d'un développeur.

### Se précipiter et ne jamais avancer

![Image](https://cdn-media-1.freecodecamp.org/images/f8o2lgSjOXUuocF8dbdEjcdLZHKDE4qFfDtF)
_Source : [pexels.com](https://www.pexels.com/photo/time-lapse-cars-on-fast-motion-134643/" rel="noopener" target="_blank" title=")_

L'une de mes autres erreurs récentes qui se distingue n'était pas aussi dramatique. En fait, c'était une petite erreur après une autre qui a conduit à un désastre à la fin.

Notre défi était un projet avec un calendrier serré. (Ne le sont-ils pas tous, cependant ?)

Lors de notre première réunion, nous avons convenu en tant qu'équipe que cela prendrait deux fois plus de temps que ce que nous avions. Avec la date limite qui nous pesait dès le début, j'ai rapidement parcouru la partie authentification afin que nous puissions passer à la fonctionnalité qui intéressait vraiment le client.

Je n'avais implémenté l'authentification qu'une seule fois auparavant dans une application monopage et je ne comprenais toujours pas pleinement comment elle était censée s'assembler.

Quelle erreur de la bricoler aussi vite que possible. **J'ai manqué quelques choses importantes :**

1. L'utilisateur était chargé à partir d'un cookie après la connexion, mais la page essayait de se charger sans attendre. Selon l'ordre de ces événements, vous obteniez des réponses du serveur disant que vous n'étiez pas autorisé. L'erreur était rare et difficile à reproduire parce que _la plupart_ du temps, les choses se terminaient dans le bon ordre.
2. L'authentification ne vérifiait jamais si le jeton avait expiré. Si vous ne visitiez pas souvent le site, lorsque vous reveniez, le site ne fonctionnait pas et vous deviez vous déconnecter et vous reconnecter.
3. Le jeton était censé se mettre à jour avec chaque requête, mais je n'ai jamais eu le temps de comprendre les règles qui l'entouraient. Donc cela a une fois de plus produit un problème de timing. Si nous envoyions plusieurs requêtes en même temps, selon l'ordre dans lequel elles revenaient, vous obteniez le mauvais jeton utilisé dans les requêtes futures.

Nous nous sommes précipités et nous avons tout de même fini par prendre deux fois le temps imparti. La différence était beaucoup plus de bugs, puis passer encore plus de temps à traquer et corriger ces bugs.

Mon travail m'a embarrassé. Ensuite, être honteux en public pour cela a rendu toute l'expérience encore pire.

Je dirai une chose : depuis, j'ai pris le temps d'apprendre l'authentification. Je comprends maintenant OAuth, JWT, les jetons de rafraîchissement et les expirations. J'ai étudié le code d'authentification que d'autres avaient écrit dans un certain nombre de bibliothèques. J'ai construit des flux d'authentification dans quelques langages et frameworks différents.

### Transformer les échecs en succès futurs

C'est la seule chose que je retire de tout ce qui va mal. Presque toujours, quelque chose de bon en ressort si vous le voulez.

Si quelqu'un apprend de son erreur, il est maintenant meilleur qu'avant. J'essaie de ne pas être dur avec un coéquipier qui fait une erreur la première fois. Ils savent généralement déjà qu'ils ont fait une erreur.

Je travaille à ne pas être si dur avec ceux qui répètent la même erreur encore et encore, cependant. Ils méritent toujours de la compassion.

Vous allez continuellement grandir si vous pouvez faire quatre choses avec les erreurs :

1. rire d'en avoir fait une
2. en tirer des leçons
3. déstigmatiser le fait de les faire
4. et partager votre erreur afin que les autres puissent en bénéficier également

Je vous laisse avec une dernière anecdote sur la valeur des erreurs. Le PDG d'IBM au début des années 1900, Thomas J Watson, a un jour rencontré un employé dont une série de mauvaises décisions avait coûté cher à l'entreprise. Lorsqu'on lui a demandé si Watson allait licencier cet employé, Watson a répondu :

> "Non, je viens de dépenser 600 000 $ pour le former. Pourquoi voudrais-je que quelqu'un embauche son expérience ?"

Avez-vous une erreur intéressante dans votre passé ? Partagez-la !

Merci d'avoir lu l'article ! Si vous le trouvez utile et souhaitez montrer votre soutien, alors veuillez le partager et n'oubliez pas de cliquer sur ce bouton ?. Pour plus d'articles comme celui-ci, suivez [la publication](https://twitter.com/freeCodeCamp) et [l'auteur](https://twitter.com/zacharykuhn) sur Twitter.

[_Zach Kuhn_](https://www.linkedin.com/in/zacharykuhn/) _est Directeur du Développement chez Smashing Boxes, une agence numérique basée à Durham, en Caroline du Nord. Il construit des applications web et mobiles depuis plus d'une décennie et est impliqué dans des startups et des technologies émergentes comme la blockchain, l'IoT et l'apprentissage automatique._