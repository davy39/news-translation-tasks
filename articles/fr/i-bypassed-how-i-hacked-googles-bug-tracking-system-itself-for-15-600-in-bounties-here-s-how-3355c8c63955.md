---
title: J'ai contourné « Comment j'ai piraté le système de suivi de bugs de Google
  lui-même pour 15 600 $ de primes. » Voici comment.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T18:09:35.000Z'
originalURL: https://freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FnYAmegCjYie3tJD31dW7A.jpeg
tags:
- name: bug bounty
  slug: bug-bounty
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: J'ai contourné « Comment j'ai piraté le système de suivi de bugs de Google
  lui-même pour 15 600 $ de primes. » Voici comment.
seo_desc: 'By Gopal Singh

  Hello Everyone!

  I was reading some write-ups, and I came across this bug which I liked: “Getting
  a Google employee account.” It was a nice find by Alex Birsan. I started testing
  the issue tracker, and I was trying to see if I could get...'
---

Par Gopal Singh

Bonjour à tous !

Je lisais quelques write-ups, et je suis tombé sur ce bug qui m'a plu : [« Obtenir un compte employé de Google »](https://medium.freecodecamp.org/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5). C'était une belle trouvaille de [Alex Birsan](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined). J'ai commencé à tester le suivi des problèmes, et j'ai essayé de voir si je pouvais obtenir un compte Google. Ensuite, en regardant autour du suivi des problèmes, j'ai remarqué dans les composants de navigation qu'il y avait deux suiveurs de problèmes publics. J'ai donc cliqué sur Android Public Tracker.

Je pouvais voir les bugs signalés à Android là. Pour signaler un bug dans le suivi public des problèmes Android, vous pouvez envoyer un email à :

**buganizer-system+**_componentID_**@google.com**

où l'ID de composant d'Android est 190923.

Je pouvais voir que mon problème était listé dans le suivi public des problèmes. J'ai reçu un email de confirmation de **buganizersystem+my_email@google.com**. Une réponse à cet email serait dirigée vers :

**buganizer-system+**_componentID**+**issueID_**@google.com**

J'ai répondu à cet email, et un commentaire a été posté dans la conversation. J'ai pu ajouter un email Google pour voir si je pouvais obtenir un code de confirmation. Pour tester cela, j'ai cliqué sur [Transfert et POP/IMAP](https://mail.google.com/mail/u/0/#settings/fwdandpop) dans les paramètres Gmail et j'ai ajouté l'email Google à l'adresse email de transfert. J'ai été surpris de voir que j'ai obtenu un code de confirmation dans le suivi public des problèmes Android.

Il y a deux parties ici pour obtenir un compte Google : **Inscription** et **vérification**. Je pouvais vérifier un compte Google, mais je ne pouvais pas m'inscrire pour un compte @google.com, donc mon rapport a été fermé comme « Won't Fix ». J'ai presque abandonné, car après la correction initiale, je ne pouvais plus utiliser mon email google.com. Mais j'ai décidé de donner un dernier essai.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VPKKHkJihwBU5EGmiCO87Q.jpeg)

Ensuite, j'ai commencé à visiter chaque sous-domaine de Google pour voir si je pouvais utiliser un email google.com pour m'inscrire. Cette nouvelle page d'inscription est apparue (voir ci-dessous). Initialement, je ne pouvais pas trouver « Utiliser mon adresse email actuelle à la place » pour accéder à [https://partnerissuetracker.corp.google.com/](https://partnerissuetracker.corp.google.com/). Ensuite, vous cliqueriez sur Créer un compte, et vous pourriez voir qu'il y avait une option pour utiliser votre adresse email actuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FnYAmegCjYie3tJD31dW7A.jpeg)

Mon rythme cardiaque a augmenté après avoir vu la nouvelle page d'inscription. J'ai commencé à m'inscrire en utilisant l'email **buganizer-system+**_componentID**+**issueID_**@google.com** et ensuite il m'a demandé de vérifier en entrant le code.

#### Vérifiez votre adresse email

J'attendais le code de vérification dans la conversation, et ensuite j'ai reçu le code de vérification dans l'email et la conversation dans le suivi des problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2V5EtNmYL9dLuWzzE5Pahg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*i3SoADa-WPpR624Nr9BPyA.jpeg)

Après m'être inscrit avec succès pour le compte Google, j'ai rouvert le problème. L'impact ici était que vous pouvez accéder à [https://google.ridecell.com](https://google.ridecell.com) qui nécessite un compte Google. En plus de cela, j'ai essayé de mettre à niveau mon compte vers Gmail maintenant que j'avais un compte Google. Je l'ai ajouté à mon Gmail, et j'ai pu envoyer un email en utilisant **buganizer-system+**_componentID**+**issueID_**@google.com**

Si vous essayez de falsifier un email google.com, votre mail atterrira dans les spams. Mais mon email est apparu dans la boîte de réception, et il provenait de @google.com, donc un attaquant pourrait prétendre qu'il était un employé de Google.

#### Belle prise !

![Image](https://cdn-media-1.freecodecamp.org/images/1*OM8Cx-NTdPsFxkGJgMcqxQ.jpeg)

Il était 21h50 quand je cherchais des bugs, et enfin, l'email tant attendu est arrivé : je recevais **3133,70 $**. Je n'ai pas pu dormir de toute la nuit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cp_Noolq5VnWPNf3NqgNGg.jpeg)

Regardez cette vidéo pour en savoir plus :

Merci à [Alex Birsan](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) — cela n'aurait pas été possible sans son write-up. J'ai beaucoup appris en lisant son write-up. Merci également à [Avinash Jain](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) et [Alex Birsan](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) pour avoir pris le temps de réviser le brouillon.

Merci d'avoir lu !

[Gopal Singh](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) ([https://twitter.com/gopalsinghcse](https://twitter.com/gopalsinghcse))