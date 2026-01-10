---
title: Qu'est-ce que le Fuzzing ? Explication des tests de fuzzing avec des exemples
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-02-18T16:00:40.000Z'
originalURL: https://freecodecamp.org/news/whats-fuzzing-fuzz-testing-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Fuzzing.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Software Testing
  slug: software-testing
seo_title: Qu'est-ce que le Fuzzing ? Explication des tests de fuzzing avec des exemples
seo_desc: 'I was recently looking through some of Google''s open source repositories
  on their GitHub. And I saw that they had a repository for continuous fuzzing. I
  had no idea what fuzzing even was, let alone continuous fuzzing.

  So What is Fuzzing?

  Fuzzing (som...'
---

Je regardais récemment certains des dépôts open source de Google sur leur [GitHub](https://github.com/google). Et j'ai vu qu'ils avaient un dépôt pour le fuzzing continu. Je n'avais aucune idée de ce qu'était le fuzzing, et encore moins le fuzzing continu.

# Qu'est-ce que le Fuzzing ?

Le **Fuzzing** (parfois appelé **test de fuzzing**) est un moyen de tester automatiquement un logiciel. Généralement, le **fuzzer** fournit de nombreuses entrées invalides ou aléatoires dans le programme. Le test tente de provoquer des plantages, des erreurs, des fuites de mémoire, etc.

Normalement, le **fuzzing** fonctionne mieux sur les programmes qui prennent des entrées, comme les sites web qui pourraient demander votre nom et votre âge comme entrée. 

Nous pourrions essayer toutes sortes de chaînes différentes pour tenter de provoquer des problèmes, peut-être quelque chose comme : "Power\u0644\u064f\u0644\u064f\u0635\u0651\u0628\u064f\u0644\u064f\u0644\u0635\u0651\u0628\u064f\u0631\u0631\u064b \u0963 \u0963h \u0963 \u0963\u5197" (cela a déjà fait planter iOS), "\u1e6e\u0324\u034d\u0325\u0347\u0348h\u0332\u0301e\u034f\u0353\u033c\u0317\u0319\u033c\u0323\u0354 \u0347\u031c\u0331\u0320\u0353\u034d\u0345N\u0355\u0360e\u0317\u0331z\u0318\u031d\u031c\u033a\u0359p\u0324\u033a\u0339\u034d\u032f\u035ae\u0320\u033b\u0320\u035cr\u0328\u0324\u034d\u033a\u0316\u0354\u0316\u0316d\u0320\u031f\u032d\u032c\u031d\u035fi\u0326\u0356\u0329\u0353\u0354\u0324a\u0320\u0317\u032c\u0349\u0319n\u035a\u035c \u033b\u031e\u0330\u035a\u0345h\u0335\u0349i\u0333\u031ev\u0322\u0347\u1e19\u034e\u035f-\u0489\u032d\u0329\u033c\u0354m\u0324\u032d\u032bi\u0355\u0347\u031d\u0326n\u0317\u0359\u1e0d\u031f \u032f\u0332\u0355\u035e\u01eb\u031f\u032f\u0330\u0332\u0359\u033b\u031df \u032a\u0330\u0330\u0317\u0316\u032d\u0318\u0358c\u0326\u034d\u0332\u031e\u034d\u0329\u0319\u1e25\u035aa\u032e\u034e\u031f\u0319\u035c\u01a1\u0329\u0339\u034es\u0324.\u031d\u031d \u0489Z\u0321\u0316\u031c\u0356\u0330\u0323\u0349\u031ca\u0356\u0330\u0359\u032c\u0361l\u0332\u032b\u0333\u034d\u0329g\u0321\u031f\u033c\u0331\u035a\u031e\u032c\u0345o\u0317\u035c.\u031f", "\ud83d\ude0d" ou "undefined".



L'idée derrière le **fuzzing** est de tenter de trouver des cas limites dans une base de code. Vous l'utilisez pour vous assurer que tout le parsing que vous faites, l'acceptation des données, le stockage des données et la lecture des données ne causent aucun bug. 

C'est un test assez intégré, car vous pouvez tester le flux complet de stockage de quelque chose comme un [espace de largeur nulle](https://en.wikipedia.org/wiki/Zero-width_space) (U+200B en Unicode) sur votre site pour vérifier les problèmes. 

Certaines personnes tentent d'injecter du code dans les champs d'entrée (c'est une partie du **fuzzing** appelée **injection de code**) comme `<script>alert(123)</script>` en tant qu'entrée de nom.

Les hackers malveillants ne veulent pas que vous testiez les entrées non standard, car vous pourriez avoir des bugs qui cassent l'application – et ils peuvent utiliser cela pour voler des données ou faire planter votre application/serveurs de manière répétée.

Jetez un œil à [ce](https://github.com/minimaxir/big-list-of-naughty-strings) GitHub appelé la **Grande Liste de Chaînes Malveillantes**. C'est une liste de chaînes qui ont une forte probabilité de causer des problèmes. 

Vous pouvez consulter certains des fichiers `.json` et `.txt` pour voir ce qui a causé des problèmes par le passé, et lire certains des commentaires pour apprendre _exactement_ pourquoi ils sont problématiques.

Par exemple, il y a des chaînes qui sont écrites à l'envers "u\u028dop\u01ddp\u1d09sd\u2229" que vous pouvez faire [ici](http://www.upsidedowntext.com). Il y a des chaînes qui peuvent être signalées comme obscènes ou inappropriées mais qui sont en réalité inoffensives (c'est ce qu'on appelle le [problème de S[cunt](https://en.wikipedia.org/wiki/Scunthorpe_problem)horpe](null)). Ou même des chaînes qui peuvent révéler des fichiers système si elles sont analysées par un parseur XML mal configuré.

# Qui utilise le Fuzzing ?

Le **Fuzzing** a des utilisations dans les **Tests Logiciels** pour trouver des bugs dans vos programmes, comme je l'ai déjà mentionné. Mais il a aussi des applications en cybersécurité et en hacking.

Dans son application en cybersécurité, les hackers cherchent à franchir une **frontière de confiance**. Une **frontière de confiance** est un endroit dans les systèmes informatiques où les données sont transmises d'une zone à une autre, d'une source de confiance. 

Par exemple, imaginez dans votre front-end que vous recevez le nom d'un utilisateur, vous assurez qu'il est valide, puis vous le transmettez à votre back-end. Votre **frontière de confiance** ici est la ligne imaginaire où les données sont transmises du front-end au back-end.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/trust-boundary.png)

Si votre back-end fait simplement confiance aux données sans les valider (car le front-end les valide déjà !) cela pourrait poser un problème. Tant que les hackers peuvent contourner vos vérifications front-end, ils sont alors des entrées **de confiance** et peuvent essayer d'insérer des chaînes malveillantes comme entrée. 

C'est là que le **fuzzing** peut aider à vérifier que vous attrapez ces types de problèmes.

Supposons que quelqu'un veuille **fuzzer Google Chrome**, par exemple. Une façon de le faire serait d'exécuter le navigateur dans un outil de débogage afin qu'ils puissent suivre les commandes que Chrome exécute et profiler sa gestion de la mémoire.

Les hackers pointeraient ensuite le programme Chrome qu'ils observent vers l'un de leurs serveurs. Les serveurs des hackers créeraient alors des millions de pages web différentes que **Chrome** chargerait, toutes avec des JS, CSS et HTML légèrement différents dans les pages web pour essayer de faire planter le Chrome que les hackers profilent. 

Ces hackers pourraient raisonnablement continuer à exécuter ces tests automatisés pendant des mois, collecter une énorme liste de logs de Chrome (comme des plantages, des débordements de mémoire, etc.) et essayer de comprendre ce qui a causé le plantage.

Faire planter le navigateur n'est pas le but final ici. Une fois que ces hackers savent quels types d'entrées provoquent des plantages, ils peuvent enquêter sur pourquoi ces choses provoquent des plantages et voir s'ils peuvent utiliser ces exploits pour faire quelque chose de sinistre, ou accéder à quelque chose auquel ils ne devraient pas avoir accès. Vous pouvez lire plus sur l'exemple ci-dessus [ici](https://www.wired.com/2016/06/hacker-lexicon-fuzzing/).

Google [actuellement](https://google.github.io/clusterfuzz/) **fuzze** ses propres applications sur 30 000 VM ! Vous n'êtes donc pas susceptible d'avoir des progrès en raison de l'étendue avec laquelle ils **fuzzent** déjà.

Le [OSS-Fuzz](https://github.com/google/oss-fuzz) de Google a trouvé plus de 25 000 bugs dans le code de Google Chrome, et environ 22 500 bugs dans d'autres bases de code open source qui utilisent OSS-Fuzz.

Donc, pour revenir à mon titre principal. Qui utilise le **fuzzing** ? Je parierais que presque toutes les entreprises qui doivent protéger leurs actifs numériques ou leurs informations emploient des testeurs pour **fuzzer** leurs produits ou le font elles-mêmes.

# **Conclusion**

J'espère que cela a expliqué ce qu'est le **fuzzing** et certaines de ses applications.

Si vous souhaitez approfondir vos recherches sur ce sujet, vous pouvez trouver une énorme liste de ressources [ici](https://github.com/secfigo/Awesome-Fuzzing) sur GitHub. Il y a tout, des cours, articles, vidéos et outils pour vous aider à apprendre à **fuzzer**.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.