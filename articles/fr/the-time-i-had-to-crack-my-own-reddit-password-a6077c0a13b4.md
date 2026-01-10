---
title: Cette fois où j'ai dû craquer mon propre mot de passe Reddit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-06T07:04:21.000Z'
originalURL: https://freecodecamp.org/news/the-time-i-had-to-crack-my-own-reddit-password-a6077c0a13b4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZAFlM8eSiuGVRo9P-8L6MQ.jpeg
tags:
- name: humor
  slug: humor
- name: Ruby
  slug: ruby
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Cette fois où j'ai dû craquer mon propre mot de passe Reddit
seo_desc: 'By Haseeb Qureshi

  (Kinda.)


  Hack the planet, everybody.

  I have no self-control.

  Luckily, I know this about myself. This allows me to consciously engineer my life
  so that despite having the emotional maturity of a heroin-addicted lab rat, I’m
  occasion...'
---

Par Haseeb Qureshi

#### (En quelque sorte.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZAFlM8eSiuGVRo9P-8L6MQ.jpeg)
_Piratez la planète, tout le monde._

Je n'ai aucun self-contrôle.

Heureusement, je le sais de moi-même. Cela me permet de concevoir consciemment ma vie de sorte que, malgré la maturité émotionnelle d'un rat de laboratoire accro à l'héroïne, je sois occasionnellement capable de faire des choses.

Je perds beaucoup de temps sur Reddit. Si je veux procrastiner sur quelque chose, j'ouvre souvent un nouvel onglet et plonge dans un trou de Reddit. Mais parfois, il faut mettre les œillères et réduire les distractions. 2015 était l'une de ces périodes — j'étais uniquement concentré sur l'amélioration en tant que programmeur, et Reddit devenait un handicap.

J'avais besoin d'un plan d'abstinence.

Alors, une idée m'est venue : et si je me bloquais moi-même de mon compte ?

**Voici ce que j'ai fait :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Zpw3ipnu92ehqA_6T-o8w.gif)

J'ai défini un mot de passe aléatoire sur mon compte. Ensuite, j'ai demandé à un ami de m'envoyer ce mot de passe par e-mail à une certaine date. Avec cela, j'aurais un moyen infaillible de me bloquer de Reddit. (J'ai également changé l'e-mail de récupération de mot de passe pour couvrir toutes les bases.)

Cela aurait dû fonctionner.

Malheureusement, il s'avère que les amis sont très sensibles à l'ingénierie sociale. Le terme technique pour cela est qu'ils sont « gentils avec vous » et vous rendront votre mot de passe si vous les « suppliez ».

Après quelques rounds de ce mode d'échec, j'avais besoin d'une solution plus robuste. Une petite recherche sur Google, et je suis tombé sur ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*iMtDCzvNYVF9UOeiIbU7Ww.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7QCLp-4HnnDwgj1FSnRstw.png)
_Ça a l'air légitime._

Parfait — une solution automatisée, sans ami ! (J'en avais aliené la plupart à ce moment-là, donc c'était un gros point de vente.)

Un peu louche, mais bon, dans la tempête, tout port est bon.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TOUIDOIRHiVySUWt46n3mw.gif)

Pendant un moment, j'ai mis en place cette routine — pendant la semaine, je m'envoyais mon mot de passe par e-mail, le week-end je recevais le mot de passe, je faisais le plein de malbouffe internet, et ensuite je me bloquais à nouveau une fois la semaine commencée. Cela fonctionnait assez bien, de ce que je me souviens.

Finalement, j'ai été si occupé avec la programmation que j'ai complètement oublié cela.

### **Passons à deux ans plus tard.**

Je suis maintenant gainement employé chez Airbnb. Et Airbnb, il se trouve, a une grande suite de tests. Cela signifie attendre, et attendre signifie bien sûr des trous de lapin sur internet.

Je décide de retrouver mon ancien compte et de trouver mon mot de passe Reddit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sAr_MYJtJVkNq6uHiVQxtQ.gif)

Oh non. Ce n'est pas bon.

Je ne me souvenais pas avoir fait cela, mais je devais être si exaspéré par moi-même que **je m'étais bloqué jusqu'en 2018**. Je l'avais également réglé pour « cacher », donc je ne pouvais pas voir le contenu de l'e-mail avant qu'il ne soit envoyé.

Que faire ? Dois-je simplement créer un nouveau compte Reddit et recommencer à zéro ? Mais c'est _tellement de travail_.

Je pourrais écrire à LetterMeLater et expliquer que je ne voulais pas faire cela. Mais ils mettraient probablement un certain temps à me répondre. Nous avons déjà établi que je suis extrêmement impatient. De plus, ce site ne semble pas avoir une équipe de support. Sans parler du fait que ce serait un échange d'e-mails embarrassant. J'ai commencé à imaginer des explications élaborées impliquant des parents décédés pour expliquer pourquoi j'avais besoin d'accéder à l'e-mail...

Toutes mes options étaient compliquées. Je rentrais chez moi ce soir-là du bureau en réfléchissant à mon predicament, quand soudain, une idée m'est venue.

**La barre de recherche.**

J'ai ouvert l'application sur mon téléphone portable et j'ai essayé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DvLUtm_ZGOaTGKy1bOuyYQ.gif)

Hmm.

D'accord. Donc, il indexe clairement le sujet. Et le corps ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*esw6gkV0G-M1JKaPAqipLA.gif)

J'essaie quelques lettres, et voilà. Le corps est définitivement indexé. Rappelez-vous : le corps était entièrement composé de mon mot de passe.

_Essentiellement, on m'a donné une interface pour effectuer des requêtes de sous-chaînes._ En entrant une chaîne dans la barre de recherche, les résultats de recherche confirmeront si mon mot de passe contient cette sous-chaîne.

**Nous sommes en affaires.**

Je me précipite dans mon appartement, pose mon sac et sors mon ordinateur portable.

Problème d'algorithme : vous avez une fonction `substring?(str)`, qui retourne vrai ou faux selon qu'un mot de passe contient une sous-chaîne donnée. _Étant donné cette fonction, écrivez un algorithme qui peut déduire le mot de passe caché._

### L'Algorithme

Alors réfléchissons à cela. Quelques choses que je sais sur mon mot de passe : je sais que c'était une longue chaîne avec quelques caractères aléatoires, probablement quelque chose comme `asgoihej2409g`. Je _n'ai probablement_ pas inclus de caractères majuscules (et Reddit n'impose pas cela comme contrainte de mot de passe), alors supposons pour l'instant que je ne l'ai pas fait — au cas où je l'aurais fait, nous pouvons simplement élargir l'espace de recherche plus tard si l'algorithme initial échoue.

Nous avons également une ligne de sujet qui fait partie de la chaîne que nous interrogeons. Et nous savons que le sujet est « password ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*XvaVCyWtSdqKSz59HKnNDw.png)

Prétendons que le corps fait 6 caractères de long. Donc nous avons six emplacements de caractères, dont certains peuvent apparaître dans la ligne de sujet, et d'autres certainement non. Donc si nous prenons tous les caractères qui ne sont pas dans le sujet et essayons de rechercher chacun d'eux, nous savons avec certitude que nous tomberons sur une lettre unique qui est dans le mot de passe. Pensez à un jeu de la Roue de la Fortune.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LOzh--_Ujutrh_OKhjfNaw.png)

Nous continuons à essayer des lettres une par une jusqu'à ce que nous trouvions une correspondance pour quelque chose qui n'est pas dans notre ligne de sujet. Disons que nous l'avons trouvé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fdoVAq3t5naQ5G9yARr0RA.png)

Une fois que j'ai trouvé ma première lettre, je ne sais pas exactement où je me trouve dans cette chaîne. Mais je sais que je peux commencer à construire une sous-chaîne plus grande en ajoutant différents caractères à la fin de celle-ci jusqu'à ce que je trouve une autre correspondance de sous-chaîne.

Nous devrons potentiellement parcourir chaque caractère de notre alphabet pour le trouver. Chacun de ces caractères pourrait être correct, donc en moyenne, il tombera quelque part autour du milieu, donc étant donné un alphabet de taille `A`, cela devrait donner en moyenne `A/2` suppositions par lettre (supposons que le sujet est petit et qu'il n'y a pas de motifs répétitifs de 2+ caractères).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GJ5xKZzTe0F5un-Iz11pXg.png)

Je continuerai à construire cette sous-chaîne jusqu'à ce qu'elle atteigne la fin et qu'aucun caractère ne puisse l'étendre davantage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E9ri3Rf8LBPxUTjgs5BvPQ.png)

Mais ce n'est pas suffisant — très probablement, il y aura un préfixe à la chaîne que j'ai manqué, parce que j'ai commencé à un endroit aléatoire. Facile à faire : tout ce que j'ai à faire est de répéter le processus, mais en allant en arrière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F_n0WGRP_8RJdFtR-v0b1g.png)

Une fois le processus terminé, je devrais être en mesure de reconstruire le mot de passe. Au total, je devrai déterminer `L` caractères (où `L` est la longueur), et je devrai dépenser en moyenne `A/2` suppositions par caractère (où `A` est la taille de l'alphabet), donc le nombre total de suppositions = `A/2 * L`.

Pour être précis, je dois également ajouter un autre `2A` au nombre de suppositions pour m'assurer que la chaîne s'est terminée à chaque extrémité. Donc le total est `A/2 * L + 2A`, que nous pouvons factoriser comme `A(L/2 + 2)`.

Supposons que nous avons 20 caractères dans notre mot de passe, et un alphabet composé de `a-z` (26) et `0–9` (10), donc une taille d'alphabet totale de 36. Donc nous cherchons une moyenne de `36 * (20/2 + 2) = 36 * 12 = 432` itérations.

Damn.

C'est en fait faisable.

### L'Implémentation

D'abord, je dois écrire un client qui peut interroger la boîte de recherche de manière programmatique. Cela servira d'oracle de sous-chaîne. Évidemment, ce site n'a pas d'API, donc je devrai scraper le site web directement.

Il semble que le format d'URL pour la recherche soit simplement une chaîne de requête, `www.lettermelater.com/account.php?**qe=#{query_here}**`. C'est assez facile.

Commençons à écrire ce script. Je vais utiliser le gem Faraday pour faire des requêtes web, car il a une interface simple que je connais bien.

Je vais commencer par créer une classe API.

Bien sûr, nous ne nous attendons pas à ce que cela fonctionne encore, car notre script ne sera pas authentifié dans un compte. Comme nous pouvons le voir, la réponse retourne une redirection 302 avec un message d'erreur fourni dans le cookie.

```
[10] pry(main)> Api.get("foo")
```

```
=> #<Faraday::Response:0x007fc01a5716d8
```

```
...
```

```
{"date"=>"Tue, 04 Apr 2017 15:35:07 GMT",
```

```
"server"=>"Apache",
```

```
"x-powered-by"=>"PHP/5.2.17",
```

```
"set-cookie"=>"msg_error=You+must+be+signed+in+to+see+this+page.",
```

```
"location"=>".?pg=account.php",
```

```
"content-length"=>"0",
```

```
"connection"=>"close",
```

```
"content-type"=>"text/html; charset=utf-8"},
```

```
status=302>
```

Alors, comment nous connectons-nous ? Nous devons envoyer nos [cookies](http://stackoverflow.com/questions/17769011/how-does-cookie-based-authentication-work) dans l'en-tête, bien sûr. En utilisant l'inspecteur Chrome, nous pouvons facilement les récupérer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PSxZtW4wppyzRXMdBWgGWw.gif)

(Je ne vais pas montrer mon vrai cookie ici, évidemment. Intéressant, il semble qu'il stocke `user_id` côté client, ce qui est toujours un bon signe.)

Par élimination, je réalise qu'il a besoin à la fois de `code` et de `user_id` pour m'authentifier... soupir.

Alors, je les ajoute au script. (C'est un faux cookie, juste pour l'illustration.)

```
[29] pry(main)> Api.get("foo")=> "\n<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n<html>\n<head>\n\t<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\" />\n\t<meta name=\"Description\" content=\"LetterMeLater.com allows you to send emails to anyone, with the ability to have them sent at any future date and time you choose.\" />\n\t<meta name=\"keywords\" content=\"schedule email, recurring, repeating, delayed, text messaging, delivery, later, future, reminder, date, time, capsule\" />\n\t<title>LetterMeLater.com — Account Information</title>…
```

```
[30] pry(main)> _.include?("Haseeb")=> true
```

Il y a mon nom, donc nous sommes définitivement connectés !

Nous avons réussi le scraping, maintenant nous devons simplement analyser le résultat. Heureusement, c'est assez facile — nous savons que c'est un succès si le résultat de l'e-mail apparaît sur la page, donc nous devons simplement chercher une chaîne qui est unique lorsque le résultat est présent. La chaîne « password » n'apparaît nulle part ailleurs, donc cela fera très bien l'affaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZT37Ji9j8sm8dobFpiAWQ.png)

C'est tout ce dont nous avons besoin pour notre classe API. Nous pouvons maintenant effectuer des requêtes de sous-chaînes entièrement en Ruby.

```
[31] pry(main)> Api.include?('password')
```

```
=> true
```

```
[32] pry(main)> Api.include?('f')
```

```
=> false
```

```
[33] pry(main)> Api.include?('g')
```

```
=> true
```

Maintenant que nous savons que cela fonctionne, créons un substitut pour l'API pendant que nous développons notre algorithme. Faire des requêtes HTTP va être très lent et nous pourrions déclencher une limitation de débit pendant que nous expérimentons. Si nous supposons que notre API est correcte, une fois que nous aurons le reste de l'algorithme fonctionnel, tout devrait simplement fonctionner une fois que nous aurons remplacé l'API réelle.

Donc voici l'API simulée, avec une chaîne secrète aléatoire :

Nous allons injecter l'API simulée dans la classe pendant que nous testons. Ensuite, pour l'exécution finale, nous utiliserons l'API réelle pour interroger le vrai mot de passe.

Alors, commençons avec cette classe. D'un point de vue général, en rappelant mon diagramme d'algorithme, cela se fait en trois étapes :

1. Tout d'abord, trouver la première lettre qui n'est pas dans le sujet mais existe dans le mot de passe. C'est notre point de départ.
2. Construire ces lettres vers l'avant jusqu'à ce que nous atteignions la fin de la chaîne.
3. Construire cette sous-chaîne vers l'arrière jusqu'à ce que nous atteignions le début de la chaîne.

Ensuite, nous avons terminé !

Commençons par l'initialisation. Nous allons injecter l'API, et à part cela, nous devons simplement initialiser le morceau de mot de passe actuel pour qu'il soit une chaîne vide.

Maintenant, écrivons trois méthodes, en suivant les étapes que nous avons décrites.

Parfait. Maintenant, le reste de l'implémentation peut avoir lieu dans des méthodes privées.

Pour trouver la première lettre, nous devons itérer sur chaque caractère de l'alphabet qui n'est pas contenu dans le sujet. Pour construire cet alphabet, nous allons utiliser `a-z` et `0–9`. Ruby nous permet de faire cela assez facilement avec des plages :

```
ALPHABET = (('a'..'z').to_a + ('0'..'9').to_a).shuffle
```

Je préfère mélanger cela pour éliminer tout biais dans la distribution des lettres du mot de passe. Cela fera en sorte que notre algorithme interroge A/2 fois en moyenne par caractère, même si le mot de passe est distribué de manière non aléatoire.

Nous voulons également définir le sujet comme une constante :

```
SUBJECT = 'password'
```

C'est tout ce dont nous avons besoin pour la configuration. Maintenant, il est temps d'écrire `find_starting_letter`. Cela doit itérer à travers chaque lettre candidate (dans l'alphabet mais pas dans le sujet) jusqu'à ce qu'elle trouve une correspondance.

En testant, cela semble fonctionner parfaitement :

```
PasswordCracker.new(ApiStub).send(:find_starting_letter!) # => 'f'
```

Maintenant, le gros du travail.

Je vais faire cela de manière récursive, car cela rend la structure très élégante.

Le code est surprenamment simple. Voyons si cela fonctionne avec notre API simulée.

```
[63] pry(main)> PasswordCracker.new(ApiStub).crack!
```

```
f
```

```
fj
```

```
fjp
```

```
fjpe
```

```
fjpef
```

```
fjpefo
```

```
fjpefoj
```

```
fjpefoj4
```

```
fjpefoj49
```

```
fjpefoj490
```

```
fjpefoj490r
```

```
fjpefoj490rj
```

```
fjpefoj490rjg
```

```
fjpefoj490rjgs
```

```
fjpefoj490rjgsd
```

```
=> "fjpefoj490rjgsd"
```

Super. Nous avons un suffixe, maintenant il suffit de construire en arrière et de compléter la chaîne. Cela devrait ressembler à ceci.

En fait, il n'y a que deux lignes de différence ici : comment nous construisons le `guess`, et le nom de l'appel récursif. Il y a une refactorisation évidente ici, alors faisons-la.

Maintenant, ces autres appels se réduisent simplement à :

Et voyons comment cela fonctionne en action :

```
Apps-MacBook:password-recovery haseeb$ ruby letter_me_now.rb
```

```
Current password: 9
```

```
Current password: 90
```

```
Current password: 90r
```

```
Current password: 90rj
```

```
Current password: 90rjg
```

```
Current password: 90rjgs
```

```
Current password: 90rjgsd
```

```
Current password: 90rjgsd
```

```
Current password: 490rjgsd
```

```
Current password: j490rjgsd
```

```
Current password: oj490rjgsd
```

```
Current password: foj490rjgsd
```

```
Current password: efoj490rjgsd
```

```
Current password: pefoj490rjgsd
```

```
Current password: jpefoj490rjgsd
```

```
Current password: fjpefoj490rjgsd
```

```
Current password: pfjpefoj490rjgsd
```

```
Current password: hpfjpefoj490rjgsd
```

```
Current password: 0hpfjpefoj490rjgsd
```

```
Current password: 20hpfjpefoj490rjgsd
```

```
Current password: 420hpfjpefoj490rjgsd
```

```
Current password: g420hpfjpefoj490rjgsd
```

```
g420hpfjpefoj490rjgsd
```

Magnifique. Maintenant, ajoutons simplement quelques instructions d'impression et un peu de journalisation supplémentaire, et nous aurons notre `PasswordCracker` terminé.

Et maintenant... le moment magique. Remplaçons le substitut par la vraie API et voyons ce qui se passe.

### Le Moment de Vérité

Croisez les doigts...

`PasswordCracker.new(Api).crack!`

![Image](https://cdn-media-1.freecodecamp.org/images/1*NR-y9WthtHg4DVjLDwikVA.gif)
_(Accéléré 3x)_

Boom. 443 itérations.

Je l'ai essayé sur Reddit, et la connexion a réussi.

Wow.

Cela... a vraiment fonctionné.

Rappelons notre formule originale pour le nombre d'itérations : `A(N/2 + 2)`. Le vrai mot de passe faisait 22 caractères, donc notre formule estimerait `36 * (22/2 + 2) = 36 * 13 = 468` itérations. Notre vrai mot de passe a pris 443 itérations, donc notre estimation était à 5% du temps d'exécution observé.

**Maths.**

**Ça marche.**

E-mail de support embarrassant évité. Plongée dans les trous de lapin de Reddit restaurée. Il est maintenant confirmé : la programmation est, en effet, de la magie.

(Le seul inconvénient est que je vais maintenant devoir trouver une nouvelle technique pour me bloquer de mes comptes.)

Et avec cela, je vais retourner à mes trous de lapin sur internet. Merci d'avoir lu, et donnez un like si vous avez aimé cela !

—Haseeb