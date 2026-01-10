---
title: Comment accélérer votre ancien ordinateur portable - en utilisant des choses
  que vous avez chez vous
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-28T23:21:47.000Z'
originalURL: https://freecodecamp.org/news/speed-up-old-laptop
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/20191029_080609.jpg
tags:
- name: performance
  slug: performance
seo_title: Comment accélérer votre ancien ordinateur portable - en utilisant des choses
  que vous avez chez vous
seo_desc: 'By Jackson Bates

  I''m extremely proud of my laptop. It''s about 7 years old, but was pretty well
  equipped in its heyday, with a core i7 processor and 6GB RAM it was excellent for
  everything I was using it for. It''s also survived many knocks and drops -...'
---

Par Jackson Bates

Je suis extrêmement fier de mon ordinateur portable. Il a environ 7 ans, mais il était assez bien équipé à son apogée, avec un processeur core i7 et 6 Go de RAM, il était excellent pour tout ce que je faisais avec. Il a également survécu à de nombreux chocs et chutes - je suis presque sûr qu'il est à l'épreuve des balles.

Récemment, il a commencé à ralentir chaque fois que j'essaie d'avoir quelques onglets Chrome, VSCode et l'application Slack ouverts - vous savez, _tout ce qu'un développeur a ouvert tout le temps_ !

J'ai vérifié l'utilisation de la RAM et du CPU sur ma machine et tout était normal. Même si ces applications sont notoirement gourmandes en ressources, un CPU décent et une quantité modérée de RAM auraient dû suffire.

Cependant, il y avait un autre problème qui me tracassait. Le port VGA sur le côté devenait si chaud que lorsque je posais absentement mes doigts dessus, ils se brûlaient légèrement.

Mon CPU surchauffait - et par mesure de sécurité, mon ordinateur se bridait pour ne pas fondre. En effet, lorsque j'ai installé quelques utilitaires de ligne de commande de capteurs sur ma machine pour vérifier la température, il a rapporté que la température était élevée et dangereusement proche du niveau critique :

```
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +95.0°C  (high = +87.0°C, crit = +105.0°C)
Core 0:        +95.0°C  (high = +87.0°C, crit = +105.0°C)
Core 1:        +98.0°C  (high = +87.0°C, crit = +105.0°C)
Core 2:        +92.0°C  (high = +87.0°C, crit = +105.0°C)
Core 3:        +91.0°C  (high = +87.0°C, crit = +105.0°C)

```

J'ai un aveu à faire : En 7 ans de possession de cet ordinateur portable bien-aimé, je ne l'ai jamais nettoyé !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/20191029_073715.jpg)
_Votre ventilateur d'ordinateur portable est le vrai MVP, traitez-le bien._

En effet, lorsque j'ai ouvert le boîtier de l'ordinateur portable, le problème était clair - 7 ans de poussière accumulée obstruant le ventilateur.

Alors, comment accélérer votre ancien ordinateur portable ? Nettoyez-le !

## Ce dont vous aurez besoin

* Des outils pour ouvrir votre ordinateur portable (dans mon cas, juste un tournevis cruciforme de bijoutier) ;
* De l'alcool de nettoyage (j'ai utilisé de l'alcool méthylé) ;
* Une petite brosse propre ; et/ou
* Une bombe d'air comprimé ;
* Optionnel : De la pâte thermique (OK - vous n'avez peut-être pas cela chez vous, mais c'est [c'est bon marché](https://www.amazon.com/Arctic-Silver-AS5-3-5G-Thermal-Paste/dp/B0087X728K))

## Méthode

Le principe de base est simple - votre CPU surchauffe parce que votre dissipateur thermique et votre ventilateur ne peuvent pas dissiper la chaleur assez rapidement.

Nous allons faire deux choses - nettoyer le ventilateur et appliquer une nouvelle pâte thermique sur votre CPU pour améliorer le transfert de chaleur.

Comme chaque marque et modèle d'ordinateur portable est construit différemment, vous devrez consulter les instructions du fabricant pour démonter votre machine en toute sécurité. Alternativement, recherchez des vidéos pour votre marque et modèle exact. Les images et la méthode précise de cet article concernent mon propre ThinkPad E530.

**ATTENTION : Si vous n'êtes pas sûr de ce que vous faites, envisagez de faire réviser votre ordinateur portable par un professionnel. Procédez à vos propres risques - nous ne sommes pas responsables si vous grillez votre ordinateur portable ou si vous vous électrocutez !**

### Étape 1

Retirez votre ordinateur portable de l'alimentation, retirez la batterie et maintenez le bouton d'alimentation enfoncé pendant environ 5 secondes pour décharger toute puissance résiduelle.

### Étape 2

Retirez le boîtier qui abrite le CPU, les dissipateurs thermiques et le ventilateur. Voir les instructions du fabricant pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/before-1.jpg)
_L'intérieur d'un ThinkPad E530_

### Étape 3

Dévissez les composants que vous devez entretenir. Dans mon cas, cela signifiait dévisser le dissipateur thermique et le ventilateur. N'oubliez pas de débrancher délicatement votre ventilateur en tirant ou en soulevant le connecteur en plastique - ne tirez pas sur les fils.

### Étape 4

Nettoyez l'ancienne pâte thermique du CPU et du dissipateur thermique (et de toute autre zone où elle a été appliquée précédemment - comme le GPU dans mon cas). Je l'ai fait en 2 étapes - en grattant délicatement la pâte séchée des zones où elle avait adhéré, puis en utilisant l'alcool de nettoyage sur un chiffon sans peluches pour enlever le reste. Sur l'image ci-dessous, ces parties grises et collantes sur le dissipateur thermique sont l'ancienne pâte thermique.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/20191029_074237.jpg)
_L'unité de dissipateur thermique et de ventilateur du ThinkPad E530_

### Étape 5

Nettoyez toute poussière visible de l'intérieur du boîtier de l'ordinateur portable avec votre brosse. Nettoyez soigneusement le ventilateur avec votre brosse et utilisez votre air comprimé pour souffler la poussière des évents. Assurez-vous de ne pas souffler la poussière dans le boîtier ouvert de l'ordinateur portable !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/20191029_081117.jpg)
_Comme neuf !_

### Étape 6 (Optionnel)

Appliquez de la pâte thermique sur votre processeur (et sur d'autres parties si nécessaire). Une petite quantité suffit. Je vous recommande fortement de lire les instructions détaillées fournies en ligne par le fabricant de votre pâte thermique. J'ai utilisé la marque [Arctic Silver 5](https://www.amazon.com/Arctic-Silver-AS5-3-5G-Thermal-Paste/dp/B0087X728K).

### Étape 7

Remettez tout en place, en n'oubliant pas de rebrancher le ventilateur (aveu : je l'ai oublié !)

## Résultats

Dès que j'ai rallumé mon ordinateur portable, il semblait plus réactif. Et une vérification rapide des capteurs a confirmé que le petit effort en valait la peine pour le bien de mon pauvre ordinateur portable :

```
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +45.0°C  (high = +87.0°C, crit = +105.0°C)
Core 0:        +45.0°C  (high = +87.0°C, crit = +105.0°C)
Core 1:        +38.0°C  (high = +87.0°C, crit = +105.0°C)
Core 2:        +43.0°C  (high = +87.0°C, crit = +105.0°C)
Core 3:        +40.0°C  (high = +87.0°C, crit = +105.0°C)

```

Le port VGA ne brûle plus !

---

Si vous avez aimé cet article et évité de griller votre CPU, suivez [@JacksonBates](https://twitter.com/JacksonBates) sur Twitter pour plus de divagations informelles liées à la technologie.