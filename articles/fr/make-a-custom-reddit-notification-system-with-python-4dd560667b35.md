---
title: Comment créer un système de notification Reddit personnalisé avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T16:27:21.000Z'
originalURL: https://freecodecamp.org/news/make-a-custom-reddit-notification-system-with-python-4dd560667b35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jwiUzuo1t9kRdDdqTdoYbw.png
tags:
- name: Heroku
  slug: heroku
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: reddit
  slug: reddit
- name: 'tech '
  slug: tech
seo_title: Comment créer un système de notification Reddit personnalisé avec Python
seo_desc: 'By Kelsey Wang

  Don’t you just love automated emails? I know I do. I mean, who doesn’t enjoy waking
  up to 236 new messages from Nike, Ticketmaster, and Adobe Creative Cloud every morning?
  What a fantastic way to start my day! ??

  Anyway, today I’ll be ...'
---

Par Kelsey Wang

N'aimez-vous pas simplement les emails automatisés ? Je sais que je les adore. Je veux dire, qui n'aime pas se réveiller avec 236 nouveaux messages de Nike, Ticketmaster et Adobe Creative Cloud chaque matin ? Quelle façon fantastique de commencer ma journée ! 💡

En tout cas, aujourd'hui je vais vous montrer comment noyer votre boîte de réception dans encore plus de désordre, pour une raison que Dieu seul connaît. Nous allons **utiliser Python pour créer un système de notification par email personnalisé pour Reddit.** Cela signifie que nous allons écrire un script qui recherche des publications Reddit correspondant à certains mots-clés et qui nous envoie ensuite un email lorsque de telles publications apparaissent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jwiUzuo1t9kRdDdqTdoYbw.png)
_Voulez-vous du contenu email de qualité comme celui-ci ? Lisez la suite !_

Il y a quelques raisons pour lesquelles vous pourriez faire cela. Peut-être êtes-vous vraiment passionné par un sujet sur Reddit. Peut-être essayez-vous de découvrir une nouvelle technique de collecte de karma parce que les points Internet sont importants pour vous. Peut-être voulez-vous envoyer des emails ennuyeux à vos amis. Ou peut-être voulez-vous simplement plus d'emails dans votre boîte de réception pour faire face à votre solitude paralysante. Oups, désolé — je suis allé trop loin. Commençons.

### Parcourir Reddit

Reddit dispose d'une [belle API](https://www.reddit.com/dev/api/) avec laquelle vous pouvez faire beaucoup de choses. Pour faciliter encore plus les choses, nous allons utiliser [PRAW](https://praw.readthedocs.io/en/latest/), le wrapper Python pour l'API Reddit.

Vous aurez d'abord besoin d'un compte Reddit. Une fois que vous en avez un, allez [ici](https://www.reddit.com/prefs/apps) pour créer une application. Donnez-lui n'importe quel nom et assurez-vous que « script » est sélectionné. Comme indiqué dans la documentation, vous pouvez simplement mettre `[http://localhost:8080](http://localhost:8080)` pour votre URI de redirection.

Maintenant, vous êtes prêt à commencer ce script génial ! Dans le code ci-dessous, **je parcours un subreddit, en sélectionnant les publications qui correspondent à mes besoins.**

Je considère qu'une publication est une _correspondance_ si elle est suffisamment pertinente et suffisamment populaire. Plus précisément, la publication est suffisamment pertinente lorsque son `keyword_count` n'est pas -1 (je vais expliquer cela ci-dessous) et suffisamment populaire lorsque son `weighted_score` est supérieur à un `MIN_RELEVANT_WEIGHTED_SCORE` prédéfinie. Le score pondéré tient simplement compte du score de la publication et du nombre de commentaires sur la publication. En tout cas, c'est ce qui correspondait le mieux à mes besoins, alors n'hésitez pas à mieux définir ce qu'une correspondance signifie pour vous.

Maintenant, je vous ai promis de parler de la fête du `keyword_count`. Spoiler : ce n'est pas vraiment une fête. J'ai simplement imaginé cette façon simple d'évaluer la pertinence : il y a des termes requis et des termes secondaires. Une publication est pertinente si et seulement si tous les termes requis sont dans le titre, et au moins X nombre de termes secondaires sont dans le titre (où X est un nombre prédéfini). Encore une fois, cette partie peut être réimaginée de manière infiniment différente, mais c'est simplement ce que j'ai fait.

Maintenant, nous avons tout pour parcourir notre subreddit et extraire les bonnes informations sur les conspirations ou autre. Cool. Donc, comme le dit mon pote Ariana, « thank u, next. »

### Envoyer des notifications par email

Il est temps de commencer à spammer. Dans le code ci-dessous, j'utilise [smtplib](https://docs.python.org/3/library/smtplib.html) (le client Simple Mail Transfer Protocol) pour m'aider à envoyer mes emails. Je crée ensuite le bel email avec HTML, en utilisant les informations de Reddit que nous avons obtenues ci-dessus pour le remplir. Et la meilleure (ou pire ?) partie est que, si vous voulez informer tout le monde que vous connaissez des dernières et meilleures publications Reddit, vous pouvez simplement ajouter plus d'adresses email à la `email_list`.

Note importante : assurez-vous que l'email que vous utilisez pour envoyer les emails a [l'accès aux applications moins sécurisées](https://support.google.com/accounts/answer/6010255?hl=en) activé si c'est une adresse Gmail, sinon cela ne fonctionnera pas.

### Le faire fonctionner pour toujours

Si vous n'avez pas le temps de parcourir continuellement Reddit, vous n'avez pas le temps de faire fonctionner ce script continuellement. J'ai utilisé Heroku Scheduler pour exécuter ce script toutes les 10 minutes, comme suggéré par cette [réponse Stack Overflow](https://stackoverflow.com/questions/39139165/running-simple-python-script-continuously-on-heroku). C'est assez facile à suivre : ajoutez quelques fichiers supplémentaires et un serveur web factice, poussez vers Heroku, ajoutez l'add-on Heroku Scheduler, et _BAM !_ Vous êtes prêt jusqu'à ce que vous épuisiez vos heures dyno gratuites. ✨

Est-ce la meilleure solution ? Non. Mais est-elle suffisante pour mes besoins ? Oui. Si vous connaissez une méthode tout aussi triviale pour faire cela, faites-le moi savoir !

### En conclusion

C'est à peu près tout pour ce projet. Ce [dépôt GitHub](https://github.com/kelseyywang/reddit-notifs) contient tout mon code. Grâce à tout le travail que tout le monde a déjà fait, c'est une tâche assez simple de construire ce système de notification Reddit personnalisé. Il faut aimer la ⭐ magie ⭐ du développement logiciel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bhzl5sep8VGmZTjM7bWe8Q.jpeg)
_Moi après avoir configuré mes notifications Reddit personnalisées_

Si vous êtes arrivé jusqu'ici, veuillez commenter « Le Dakota du Nord est le premier producteur d'orge aux États-Unis » dans la boîte ci-dessous.

Merci d'avoir lu !