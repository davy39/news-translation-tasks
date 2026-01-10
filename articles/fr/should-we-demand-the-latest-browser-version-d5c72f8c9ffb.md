---
title: Pourquoi nous devrions convaincre nos utilisateurs de mettre à jour leurs navigateurs
  — c'est gagnant-gagnant.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-09T09:38:10.000Z'
originalURL: https://freecodecamp.org/news/should-we-demand-the-latest-browser-version-d5c72f8c9ffb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g_V-TonQvcm5_8ob7sSFgw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi nous devrions convaincre nos utilisateurs de mettre à jour leurs
  navigateurs — c'est gagnant-gagnant.
seo_desc: 'By Alex Ewerlöf

  Unless you’ve been living under a rock recently, you’re aware of Meltdown and Spectre
  — two of the most widely deployed security vulnerabilities in computer history.
  You may also know that this is not just limited to OS-level applicat...'
---

Par Alex Ewerlöf

Sauf si vous avez vécu sous une pierre récemment, vous êtes au courant de [Meltdown](https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)) et [Spectre](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)) — deux des vulnérabilités de sécurité les plus largement déployées dans l'histoire de l'informatique. Vous savez peut-être aussi que cela ne se limite pas aux applications au niveau du système d'exploitation, et sur le web, c'est aussi grave que possible :

> Un site web peut lire les données stockées dans le navigateur pour un autre site web, ou la mémoire du navigateur elle-même. — Microsoft Vulnerability Research

![Image](https://cdn-media-1.freecodecamp.org/images/ZwbB4iJ05raoq-OmAlX9m89pCRMRPdsJ3i-A)

* **Firefox 57.0.4** ([sorti le 4 janvier](https://www.mozilla.org/en-US/firefox/57.0.4/releasenotes/)) [a corrigé](https://www.mozilla.org/en-US/security/advisories/mfsa2018-01/) cela.
* **Microsoft** [a publié une mise à jour](https://support.microsoft.com/en-us/help/4056890/windows-10-update-kb4056890) pour IE et Edge le 5 janvier.
* **Safari** [a sorti la version 11.0.2](https://support.apple.com/en-us/HT208403) le 8 janvier, qui protège supposément les utilisateurs contre ces problèmes.
* Les utilisateurs de **Chrome** doivent attendre la v64 (sortie vers le 23 janvier) ; mais [voici](https://www.chromium.org/Home/chromium-security/ssca) une liste de ce **que vous pouvez faire maintenant** pour limiter l'étendue des dégâts pour vos utilisateurs.

Mise à jour : 2018-01-31 : jusqu'à présent, les chercheurs en sécurité ont identifié au moins 130 logiciels malveillants basés sur ces problèmes : http://www.securityweek.com/malware-exploiting-spectre-meltdown-flaws-emerges

#### _Notes rapides_

1. Toutes ces mises à jour ne corrigent pas toutes les vulnérabilités de sécurité, mais elles sont le premier point d'action.
2. Mettre à jour le navigateur n'est que la première étape. Vous devez mettre à jour votre système d'exploitation mobile/desktop pour vous protéger contre une surface d'attaque différente mais plus large : les applications à mise à jour automatique. Veuillez lire plus [ici](https://spectreattack.com/).
3. À mesure que nous comprenons mieux l'ampleur de ces vulnérabilités, d'autres correctifs arriveront. Cette histoire est loin d'être terminée.

Maintenant, la grande question pour nous, développeurs web, est : devons-nous continuer à supporter les utilisateurs avec des navigateurs plus anciens qui sont vulnérables, ou devons-nous exiger que les utilisateurs aient les dernières versions des navigateurs ?

Je travaille dans l'équipe Identity d'une entreprise internationale avec des millions d'utilisateurs. Aucun travail que je fais pour sécuriser nos services ne peut empêcher l'utilisateur de partager les données sur notre site avec un site malveillant ou infecté ouvert dans un autre onglet.

Cela pourrait être l'effet secondaire le plus important de ces vulnérabilités de sécurité : nous avons peut-être une raison parfaitement valable de casser le web pour les personnes utilisant des navigateurs plus anciens.

L'histoire du développement front-end pourrait se souvenir de ce moment comme celui où nous sommes passés de l'ère du développement "hippie" (je supporte toutes les versions de navigateurs) à l'ère du développement "hipster" (je ne supporte que les dernières versions de navigateurs). ?

![Image](https://cdn-media-1.freecodecamp.org/images/TOh3oFs1zrwQ2bMIvJwc5jLbejEEse3aP4TG)

C'est un _changement énorme_ dans la façon de penser, surtout pour nous, développeurs web, puisque nous faisons traditionnellement de notre mieux pour inclure tout le monde : design responsive, amélioration progressive et dégradation élégante.

Cette fois, c'est différent. À l'ère post-Snowden, nous devons prendre la sécurité au sérieux. Supporter des versions de navigateurs vulnérables revient à promouvoir une vie en ligne dangereuse. C'est notre travail en tant qu'experts d'éduquer les utilisateurs et de les défendre contre les méchants. Si les sites ne supportent pas les anciens navigateurs, les utilisateurs **doivent** les mettre à jour.

C'est une situation gagnant-gagnant :

* Les développeurs se débarrassent du support des navigateurs obsolètes pour de bon
* Les utilisateurs sont forcés de prendre une décision de sécurité importante (espérons-le pour le bien).

Si nous ne réagissons pas rapidement, les exploits de ces problèmes seront déployés massivement et l'effet sera hors de contrôle. Le génie est sorti de la bouteille.

![Image](https://cdn-media-1.freecodecamp.org/images/ljBa-NHW13pB8xQhsrEUMqwWtkomR2biJSlZ)

#### C'est le scandale VW des processeurs

En 2015, [Volkswagen a été pris en flagrant délit de tricherie](https://en.wikipedia.org/wiki/Volkswagen_emissions_scandal) sur les émissions de leurs moteurs diesel. Ils ont triché pour rendre leurs voitures plus attrayantes pour les acheteurs. Dans ce cas, les fabricants de processeurs ont "négligé" certaines préoccupations de sécurité dans leurs processeurs afin qu'ils aient des métriques de performance plus élevées.

Je travaille dans une entreprise internationale qui construit les _pages de connexion_. Des millions d'utilisateurs utilisent notre connexion pour accéder aux services d'une large gamme d'entreprises. Naturellement, mon équipe est très préoccupée par la sécurité. Nous faisons de notre mieux pour garder le système aussi sécurisé que possible, mais aucun effort ne peut atténuer ce type de vulnérabilité dans les navigateurs. Par exemple :

* Les cookies `httpOnly` ne sont plus inaccessibles depuis JavaScript.
* Le cookie de session est super facile à voler pour d'autres sites (usurpation de session).
* Les extensions Chrome qui gardent les mots de passe fuient maintenant potentiellement.
* Le HTML contenant la balise `<scri`pt> est vulnérable, donc XSS est un jeu d'enfant.

Voici un exercice : voyez combien des [10 principales vulnérabilités OWASP](https://www.owasp.org/index.php/Top_10-2017_Top_10) sont maintenant **impossibles à corriger** dans les versions antérieures à 2018 de tout navigateur majeur.

**Voulons-nous vraiment servir des utilisateurs qui n'ont pas un navigateur récent avec le risque que les données de l'utilisateur ou notre entreprise soient compromises ?** Ou devons-nous (en tant que professionnels et experts) prendre position et éduquer les utilisateurs sur les dangers et les guider pour atténuer le risque ?

![Image](https://cdn-media-1.freecodecamp.org/images/a4PHQNmILvijCkXy0kEqQwA4vicZukBBewto)

Nous devons abandonner le support des navigateurs vulnérables. Cela rencontrera probablement beaucoup de résistance dans un marché qui a traditionnellement été très flexible et indulgent envers la pile utilisateur (tant qu'ils utilisent nos services, nous sommes bons). Mais quelqu'un doit commencer le changement.

### Le côté positif

Dans chaque crise, il y a une opportunité. Je soutiens que c'est la chose la plus cool qui soit arrivée à la communauté du développement web depuis ES2015. Nous connaissons tous la douleur et le coût du support des anciens navigateurs (surtout les navigateurs qui ne sont pas [evergreen](https://www.techopedia.com/definition/31094/evergreen-browser)) :

* Nous devons alourdir le code pour simuler des fonctionnalités que les navigateurs modernes ont déjà
* Déboguer un ancien navigateur en utilisant ses outils de débogage old-school n'est pas loin de l'expérience de conduire une voiture de la casse après avoir conduit une voiture moderne
* Nous ne pouvons pas compter sur l'intégrité du navigateur ([IE, je te regarde](https://www.microsoft.com/en-us/windowsforbusiness/end-of-ie-support)), donc nous ne pouvons pas servir certaines informations sensibles du tout à certains navigateurs.
* Nous devons gérer divers problèmes de rendu CSS/SVG
* Nous devons tester les cas limites pour différents navigateurs juste parce que nous les supportons ! Il y a des [entreprises](https://www.browserstack.com/) [développées](https://saucelabs.com/) autour de l'idée d'automatiser cette tâche fastidieuse avec divers ratios de succès/effort.
* Le système de modules est maintenant supporté par tous les principaux navigateurs. Abandonner le support des navigateurs vulnérables a l'avantage supplémentaire de simplifier et de moderniser nos canaux de déploiement. [**Vous n'avez peut-être pas besoin de transpiler votre code du tout !**](https://medium.freecodecamp.org/you-might-not-need-to-transpile-your-javascript-4d5e0a438ca)

### Que signifie-t-il vraiment ?

Cela signifie que vous pouvez totalement compter sur le fait que [async/await est disponible](https://caniuse.com/#feat=async-functions) sur votre navigateur client et que vous n'avez pas besoin de transpiler. Cela signifie que vous pouvez supposer que `class` est [supporté](https://caniuse.com/#feat=es6-class) et que les générateurs [sont utilisables](https://caniuse.com/#feat=es6-generators) **SANS TAXE** ! Cela signifie [template literals](https://caniuse.com/#feat=template-literals), [rest params](https://caniuse.com/#feat=rest-parameters), … sans transpilation, polyfill ou tout type de chaîne d'outils complexe ! Le développement web est soudainement simple.

Enfer, cela signifie que [vous avez les modules ES6 **MAINTENANT**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) sans Rollup, Webpack, Browserify…

Cela signifie une toute nouvelle ère. Je sais que c'est trop tôt et que chaque cellule de votre existence crie que c'est un mensonge, mais non ! Cela arrive. Si vous voulez supporter les utilisateurs avec des navigateurs anciens, faites-le à vos propres risques. Si vous vous souciez de la sécurité de vos utilisateurs et de l'intégrité de votre entreprise, vous obtenez tout cela ? en récompense !

**Une chose de plus : HTTP/2 est maintenant [officiellement utilisable](https://caniuse.com/#feat=http2) !**

OK, cela semble comme si j'étais une sorte de héros maintenant, mais la plupart de ces choses sont déjà disponibles dans la _majorité_ des navigateurs. C'est juste que pour une raison bizarre, de nombreux développeurs et chefs de produit ont supposé que [2,7 % des utilisateurs](http://gs.statcounter.com/browser-version-partially-combined-market-share#monthly-201712-201801-bar) (qui utilisent IE) génèrent en réalité la majorité de leurs revenus et qu'ils devraient faire de grands efforts pour les supporter. Ne transpirez plus. Même si vous le voulez, il y a maintenant une énorme raison de ne pas le faire !

### Comment ?

Cet essai parle plus du POURQUOI que du COMMENT, mais voici quelques idées rapides :

* [La détection de navigateur](https://en.wikipedia.org/wiki/Browser_sniffing) peut être utilisée pour détecter si les utilisateurs utilisent un navigateur vulnérable. Vous pouvez ensuite refuser de servir des données critiques aux utilisateurs avec des navigateurs qui ne peuvent pas les garder en sécurité. La détection de navigateur n'a traditionnellement pas été très fiable.
* Afficher une barre de notification pour avertir subtilement les utilisateurs ; mais qui lirait ou réagirait à cela ? Dans l'UE, nous avons l'habitude d'ignorer les notifications de cookies !
* Écrire un code de test qui tente réellement l'attaque. Si cela réussit, il affiche un avertissement (je suis sûr qu'un module NPM apparaîtra bientôt, si ce n'est déjà fait ?).

### Conclusion

Souvenez-vous de notre réaction lorsque React.js a "mélangé template et code" dans JSX ? Parfois, nous devons désapprendre les "meilleures pratiques", car l'alternative a plus de sens. Je ne parle pas de casser le web ! Je demande de protéger nos utilisateurs avant que tout l'enfer ne se déchaîne. Veuillez y réfléchir.

Mise à jour 1 (2018-01-16) : [Security Now #645](https://twit.tv/shows/security-now/episodes/645?autostart=false) entre dans les détails de Spectre et Meltdown et présente [un petit utilitaire pratique (speccheck)](https://github.com/ionescu007/SpecuCheck) pour tester la vulnérabilité du système.

Lisez [Vous n'avez peut-être pas besoin de transpiler votre JavaScript](https://medium.freecodecamp.org/you-might-not-need-to-transpile-your-javascript-4d5e0a438ca), [Quand devrais-je utiliser TypeScript ?](https://medium.freecodecamp.org/when-should-i-use-typescript-311cb5fe801b) ou [La programmation est le meilleur travail au monde](https://medium.com/@alexewerlof/what-s-cool-about-being-a-programmer-5a1e58efeee6).