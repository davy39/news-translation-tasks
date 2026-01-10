---
title: La Chute et la Résurrection de Code Radio
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-07-08T17:36:33.000Z'
originalURL: https://freecodecamp.org/news/the-fall-and-rise-of-code-radio
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/maxresdefault--3-.jpg
tags:
- name: music
  slug: music
- name: General Programming
  slug: programming
- name: youtube
  slug: youtube
seo_title: La Chute et la Résurrection de Code Radio
seo_desc: 'Code Radio is an internet radio station run by the freeCodeCamp community.
  We play music designed to help you focus while you''re coding.

  Over the past year, Code Radio had grown to be one of the largest music streams
  on YouTube. People played it in t...'
---

Code Radio est une station de radio internet gérée par la communauté freeCodeCamp. Nous diffusons de la musique conçue pour vous aider à vous concentrer pendant que vous codez.

Au cours de l'année passée, Code Radio est devenue l'une des plus grandes diffusions musicales sur YouTube. Les gens l'écoutaient dans leurs cafés et espaces de coworking. Partout où les gens codent, le groove familier de Code Radio pouvait être entendu non loin.

Rien que dans les 28 derniers jours, les développeurs ont écouté Code Radio pendant plus de 14 millions de minutes. (Cela équivaut à un impressionnant 27 ans de musique et de codage.)

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Channel_Analytics_-_YouTube_Studio-2.png)

# La Chute

L'une des 1 250+ chansons de Code Radio contenait un court échantillon audio d'un anime qui passait sur un beat à la fin d'une chanson.

Il s'avère qu'une société médiatique japonaise - à travers une série d'acquisitions - possédait les droits de cet anime. Et ils ont utilisé une sorte de système automatisé pour parcourir YouTube et identifier les flux contenant des échantillons de leur vaste catalogue de propriété intellectuelle.

L'un de ces flux était Code Radio. Et mercredi matin, leur système a déposé une demande de retrait automatisée auprès de YouTube.

Ainsi, les stéréos de 1 000 cafés, bureaux et hackerspaces à travers le monde se sont tus. Notre flux Code Radio a été remplacé par ce message de YouTube :

![1__Code_Radio%F0%9F%8E%A7___%F0%9F%92%BB_24_7_concentration_music_for_programmers_%F0%9F%94%A5_jazzy_beats_from_freeCodeCamp_org_-_YouTube|690x422](https://www.freecodecamp.org/news/content/images/2019/07/_1__Code_Radio_--___--_24_7_concentration_music_for_programmers_--_jazzy_beats_from_freeCodeCamp_org_-_YouTube.png)

Nous avons immédiatement contacté le support de YouTube. Cela devait être une erreur.

Les représentants du service client que nous avons contactés étaient aimables. Mais ils ne savaient pas comment le réparer. Ils ne savaient même pas comment nous pourrions retrouver l'accès aux contrôles de diffusion de notre chaîne. Au lieu de cela, ils ont dit qu'ils "allaient examiner cela et nous recontacter".

(À ce jour, lundi après-midi, nous n'avons toujours pas eu de réponse de leur part.)

Ainsi, dans les profondeurs de cette confusion - dans un océan de tweets et d'e-mails de la part d'auditeurs dévoués de Code Radio demandant ce qui se passait - j'ai fini par voir la vérité : **Code Radio avait besoin d'une nouvelle maison - une maison où une simple demande de retrait automatisée ne pourrait pas l'effacer de l'existence.**

# Code Radio renaît

![Image](https://media1.tenor.com/images/3637aa31124d333fa35935548ffb7996/tenor.gif)

> "Pourquoi tombons-nous, Mr. Wayne ? Pour apprendre à nous relever." - Alfred dans Batman Begins

Ah - une version auto-hébergée de Code Radio ! Cela présenterait plusieurs avantages :

1. Regarder YouTube utilise beaucoup de données. Beaucoup de gens ont des forfaits de données limités. Si nous auto-hébergeons Code Radio, nous pourrions simplement servir les fichiers MP3 eux-mêmes, plutôt qu'un flux vidéo. Nous pourrions même offrir une version légère des musiques avec un débit binaire plus faible.
2. YouTube est bloqué dans de nombreux pays où freeCodeCamp est populaire - y compris la Chine. Une version auto-hébergée de Code Radio serait accessible à tous, partout dans le monde.
3. Avec YouTube, vous devez garder l'application YouTube ouverte ou la musique s'arrêtera (sauf si vous payez 12 $ US par mois pour YouTube Premium). Une version auto-hébergée de Code Radio pourrait continuer à jouer en arrière-plan sur votre téléphone - même lorsque vous changez d'application ou verrouillez votre téléphone.
4. Avec une version auto-hébergée, nous pourrions développer des applications mobiles Code Radio, des compétences Alexa pour que vous puissiez facilement écouter Code Radio sur un Amazon Echo - le ciel est la limite.

Mais comment implémenter une version auto-hébergée ? Ne serait-ce pas coûteux de servir 14 millions de minutes d'audio chaque mois ? C'est beaucoup de données.

# Construire Code Radio

Il s'avère que la communauté de la radio internet est assez active. Nous avons immédiatement trouvé un projet open source génial pour une radio internet auto-hébergée appelé AzuraCast.

J'ai contacté le mainteneur du projet via Twitter, et en quelques minutes, nous l'avions en appel avec nous. C'était un ancien professionnel de la radio terrestre. Il nous a mis à jour sur l'écosystème des outils de radio internet.

Oui - diffuser de l'audio numérique à travers le monde est beaucoup plus coûteux que de simplement servir nos données de curriculum de codage. Mais avec des dons supplémentaires de la part de nos supporters, nous devrions pouvoir le faire.

Avec AzuraCast, plus quelques outils de relais supplémentaires, nous pourrions gérer une station de radio internet auto-hébergée à notre échelle précédente pour moins de 100 $ US par mois.

_Note de côté : Si vous n'êtes pas encore un supporter, nous accueillerions votre soutien. Chaque petit peu aide : [https://donate.freecodecamp.org](https://donate.freecodecamp.org) - Et oui, nous acceptons les dons ponctuels, les cryptomonnaies, les dons correspondants des employeurs, et plus : [https://donate.freecodecamp.org/other-ways-to-donate/](https://donate.freecodecamp.org/other-ways-to-donate/))_

# Code Radio est en direct. Aidez-nous à le tester en charge et donnez-nous votre avis.

Vous pouvez commencer à écouter Code Radio dès maintenant : [Écouter Code Radio](https://coderadio.freecodecamp.org)

Nous travaillons sur de nombreuses fonctionnalités supplémentaires que nous déploierons au cours des prochains jours :

* contrôles de débit binaire (pour que vous puissiez économiser vos données mobiles en écoutant à 64 kbps)
* une forme de chat - de préférence avec les comptes de forum existants et les modérateurs de forum
* un chatbot (peut-être Nightbot à nouveau)
* des raccourcis clavier
* une meilleure expérience mobile
* le retour de l'animation classique de Saron Yitbarek pour Code Radio

Je tiens à remercier @abdolsa, @beaucarnes, @raisedadead, @askmp, @scissorsneedfoodtoo, et bien sûr le DJ et curateur de Code Radio [Lawrence Yeo AKA Trebles and Blues](https://twitter.com/TreblesandBlues). Ils se sont tous rassemblés et, en 24 heures, ont aidé à mettre en place ce prototype.

# YouTube, le vrai MVP

En toute sincérité, je tiens également à remercier YouTube. Par leur propre maladresse, ils nous ont involontairement forcés à faire un pas en arrière et à envisager la possibilité d'auto-héberger Code Radio.

Nous continuerons à publier des tutoriels de codage approfondis et des cours de programmation gratuits sur YouTube. Nous ne leur en voulons pas de leur propre incompétence. Nous leur sommes reconnaissants d'exister et de fournir l'infrastructure pour que des organisations à but non lucratif comme la nôtre puissent servir des vidéos HD à 1 million+ d'abonnés gratuitement.

Ce n'est que le dernier chapitre de la transition progressive de notre communauté des plateformes propriétaires comme Medium et Facebook vers nos propres outils comme Developer News et ce forum.

Merci d'avoir lu, merci d'écouter, et bon codage !