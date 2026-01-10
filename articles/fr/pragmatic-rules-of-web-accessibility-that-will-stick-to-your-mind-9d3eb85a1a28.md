---
title: Règles pragmatiques de l'accessibilité web qui resteront dans votre esprit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-17T16:00:50.000Z'
originalURL: https://freecodecamp.org/news/pragmatic-rules-of-web-accessibility-that-will-stick-to-your-mind-9d3eb85a1a28
coverImage: https://cdn-media-1.freecodecamp.org/images/1*n8wSWsgY5iNzLCqNOIdRIQ.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Inclusion
  slug: inclusion
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Règles pragmatiques de l'accessibilité web qui resteront dans votre esprit
seo_desc: 'By Tiago Romero Garcia

  I first started to work with web accessibility back in 2015, at an American retail
  giant. It had just gotten a hefty lawsuit, as its website failed to comply with
  the Americans with Disabilities Act (ADA). After that happened, ...'
---

Par Tiago Romero Garcia

J'ai commencé à travailler sur l'accessibilité web en 2015, chez un géant américain de la vente au détail. Il venait de recevoir une lourde amende, car son site web ne respectait pas l'Americans with Disabilities Act (ADA). Après cet événement, mon équipe et moi avons travaillé intensivement sur la conformité ADA, ce qui m'a permis de découvrir de nombreux principes d'accessibilité web.

Cependant, au cours des années suivantes, je me suis rendu compte que je violais constamment ces principes, même si je travaillais régulièrement avec eux. D'une manière ou d'une autre, je ne les retenais jamais correctement pendant que je codais. Je ne voulais pas l'admettre, mais je n'avais clairement pas complètement intériorisé ces principes.

Finalement, j'ai décidé qu'il était temps d'investir mon temps pour simplifier les choses en règles simples et pragmatiques, faciles à retenir. J'ai finalement réussi, et cela fonctionne plutôt bien pour moi depuis.

Cet article comporte 2 sections : [Qu'est-ce que l'accessibilité web ?](#questce-que-laccessibilite-web) et [3 règles pragmatiques de l'accessibilité web](#3-regles-pragmatiques-de-laccessibilite-web). Dans la première section, je fais un rappel sur l'accessibilité web et partage mon expérience. Mais si vous préférez aller droit au but, passez directement à la deuxième section : [3 règles pragmatiques de l'accessibilité web](#3-regles-pragmatiques-de-laccessibilite-web).

### Qu'est-ce que l'accessibilité web ?

Comme je l'ai mentionné, en 2015, mon entreprise a été poursuivie pour non-respect de l'ADA.

L'[ADA](https://www.ada.gov) est une loi sur les droits civiques qui

> « interdit la discrimination contre les personnes handicapées dans tous les domaines de la vie publique, y compris les emplois, les écoles, les transports et tous les lieux publics et privés ouverts au grand public ».

Ainsi, l'ADA exige que les **entreprises, les gouvernements locaux et les prestataires de services à but non lucratif** fassent des aménagements pour que le public handicapé puisse accéder aux mêmes services que les clients valides. De même, les **agences gouvernementales fédérales** sont tenues de se conformer à une loi fédérale appelée [Section 508](https://www.section508.gov).

Dans le contexte du web, tout site public aux États-Unis qui ne respecte pas l'ADA ou la Section 508 exclut en réalité plusieurs groupes d'utilisateurs avec divers degrés de handicaps.

D'un autre côté, la pratique inclusive de rendre le contenu d'un site web accessible à tous et ses fonctionnalités utilisables par chacun est comprise comme [l'accessibilité web](http://en.wikipedia.org/wiki/Web_accessibility), ou simplement [a11y](https://a11yproject.com/posts/a11y-and-other-numeronyms/).

#### Qui peut être soutenu par l'a11y ?

Selon le [Rapport mondial sur le handicap](http://www.who.int/disabilities/world_report/2011/report/en/), publié en 2011 par l'[Organisation mondiale de la santé](http://www.who.int) (OMS), on estime que 15 % de la population mondiale vit avec une forme de handicap. Parmi ceux-ci, 2 à 4 % rencontrent des difficultés importantes dans leur fonctionnement.

Un excellent article de l'excellent [Addy Osmani](https://www.freecodecamp.org/news/pragmatic-rules-of-web-accessibility-that-will-stick-to-your-mind-9d3eb85a1a28/undefined), [Accessible UI Components For The Web](https://medium.com/@addyosmani/accessible-ui-components-for-the-web-39e727101a67), détaille les quatre principaux domaines de handicaps à considérer dans le contexte de l'a11y :

**1. Problèmes visuels :** peuvent aller de l'incapacité à distinguer les couleurs à l'absence totale de vision.

**2. Problèmes auditifs :** signifie qu'un utilisateur peut avoir des difficultés à entendre les sons émis par une page.

**3. Problèmes de mobilité :** peuvent inclure l'incapacité à utiliser une souris, un clavier ou un écran tactile.

**4. Problèmes cognitifs :** signifie qu'un utilisateur peut avoir besoin de technologies d'assistance pour l'aider à lire du texte, il est donc important de s'assurer que des alternatives textuelles existent.

Gardez à l'esprit que ce sont des gammes très larges de handicaps. Cela signifie qu'il n'est pas nécessaire d'avoir un handicap sévère pour avoir besoin d'un soutien a11y.

Pour en savoir plus, je recommande de suivre le cours gratuit [Web Accessibility](https://www.udacity.com/course/web-accessibility--ud891) sur Udacity, par Google. Voici une vidéo du cours qui couvre ces domaines de handicap :

#### Très bien, alors comment pouvons-nous fournir un soutien a11y ?

Au moment où nous avons reçu le procès en 2015, un audit avait révélé plusieurs problèmes d'a11y. Notre équipe a suivi une session de formation sur l'accessibilité d'une journée, où nous avons appris les [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21/) (WCAG, actuellement en version 2.1), qui sont généralement acceptées comme la norme pour la conformité a11y.

Les WCAG sont maintenues par l'[Initiative pour l'accessibilité du Web](https://www.w3.org/WAI/) (WAI) du [World Wide Web Consortium](https://www.w3.org) (W3C). Le même groupe a rédigé les [Applications Internet Riches Accessibles](https://www.w3.org/TR/wai-aria-1.1/) (WAI-ARIA ou simplement ARIA, actuellement en version 1.1), qui est une spécification sur la manière d'augmenter l'a11y des pages web grâce à des ajouts à HTML tels que des rôles et des attributs ARIA.

Ces directives sont catégorisées en trois niveaux de conformité :

* A (doit supporter)
* AA (devrait supporter) et
* AAA (peut supporter).

De nombreuses lois sur l'accessibilité dans le monde sont basées sur les niveaux WCAG. Par exemple, en janvier 2017, la Section 508 a adopté la conformité avec le niveau AA des WCAG 2.0.

Un excellent résumé des directives peut être trouvé dans la [liste de contrôle WCGA 2 de WebAIM](https://webaim.org/standards/wcag/checklist), où chaque critère indique son niveau de conformité correspondant.

#### À quel point est-il difficile d'apprendre les WCAG et WAI-ARIA ?

Je voudrais prendre un moment pour partager mon expérience d'apprentissage de l'a11y.

Bien que notre formation ait été assez complète et donnée par des personnes extrêmement compétentes, nous sommes simplement restés assis pendant des heures alors que nous passions en revue l'ensemble de la spécification WCAG, point par point. Leur présentation était énorme, et nous avons rapidement parcouru les diapositives. Je vais être honnête : c'était fastidieux, car les WCAG ne sont définitivement pas petites.

En résumé, nous avons pu noter de nombreuses actions à entreprendre, et nous avons immédiatement commencé à travailler sur ces corrections. Cependant, cela est rapidement devenu quelque chose de répétitif, mécanique, une réponse à des stimuli. Des histoires en entrée, du code en sortie. Nous étions noyés dans l'océan de l'a11y.

Tout le monde savait à quel point nous étions devenus compétents en a11y, donc personne ne contestait notre travail. Les histoires d'a11y ont cessé d'arriver, et nous avons eu d'autres priorités. L'attente était que nous appliquerions ce que nous avions appris, ce qui s'est effectivement produit pendant un certain temps.

Avec le temps, certaines personnes sont parties, d'autres sont arrivées, et une nouvelle direction est entrée en jeu. Le marché évolue rapidement. Nous avons changé notre focus et notre esprit d'équipe. Inutile de dire que nous nous sommes tellement impliqués dans les nouvelles choses que notre conformité a11y est passée au second plan.

C'était si grave que six mois plus tard, nous avons eu un autre audit, seulement pour découvrir que nous étions toujours assis sur un gros tas de violations d'a11y ! Nous avons rapidement réalisé que même si nous avions corrigé les problèmes audités d'origine, **la plupart du nouveau code que nous écrivions était tout aussi mauvais en termes d'a11y**. Non seulement cela, mais nous n'avons jamais adopté l'a11y comme partie de notre liste de contrôle de développement, et les nouveaux arrivants n'ont jamais été formés sur le sujet.

**Conclusion** : Nous avons simplement permis que cela se produise — l'a11y était négligée, et les idées clés n'étaient pas ancrées en nous.

En d'autres termes, nous créions des **exclusions**, ce qui se produit lorsque nous résolvons des problèmes en utilisant nos propres biais, selon le [Microsoft Inclusive Design](https://www.microsoft.com/design/inclusive/).

#### Expérimenter une exclusion

![Image](https://cdn-media-1.freecodecamp.org/images/1*PrdvH8QWWSO4296p_3eREg.jpeg)
« L'exclusion n'est jamais le chemin à suivre sur nos chemins partagés vers la liberté et la justice. » — Desmond Tutu

Parfois, vous devez expérimenter les choses vous-même pour mieux les comprendre. C'est ce qui m'est heureusement arrivé.

Je donne régulièrement mes plaquettes, car mon groupe sanguin est A+, donc je peux aider plus de personnes de cette manière. Une fois, ma veine a été perforée incorrectement et j'ai eu un gros et douloureux bleu sur mon bras gauche.

Typiquement, les dons de sang réguliers durent 10 minutes ou plus, mais les dons de plaquettes durent environ 90 minutes. Il nous a fallu environ 20 minutes pour remarquer que j'avais une veine éclatée, car mon bras était couvert de couvertures (parce que les retours de sang vous donnent froid).

À ce moment-là, les dégâts étaient faits, et nous avons dû interrompre le don. Mon bras est devenu assez gonflé et très sensible pendant quelques jours. Tellement que je n'avais pas envie d'utiliser mon bras gauche du tout pour travailler.

Maintenant, j'essayais de tout faire avec ma main droite. Tout à coup, j'ai remarqué qu'il n'était pas efficace de continuer à alterner entre le clavier et la souris, et je préférais faire toute la tâche à portée de main en utilisant uniquement le clavier ou la souris.

Bientôt, je me suis retrouvé à préférer utiliser exclusivement le clavier pour tout, et puis j'ai remarqué combien de sites ne sont tout simplement pas là en matière de support clavier. Ensuite, cela m'est venu : j'expérimentais une exclusion, même si ce n'était qu'une exclusion **temporaire**.

Et puis, exactement à ce moment-là, je me suis souvenu du passé moi travaillant avec l'a11y et laissant passer ces exclusions. Oh, mec !

#### Niveaux d'exclusions

Selon le [Microsoft's Inclusive 101 Toolkit](https://www.microsoft.com/design/inclusive/), il existe trois niveaux d'exclusions :

1. **Permanente** : vécue par ceux qui ont un handicap tel que la perte d'un membre, de la vue, de l'ouïe ou de la parole.
2. **Temporaire** : vécue par ceux qui ont une blessure à court terme ou qui traversent certains événements pendant une courte période, comme regarder une lumière vive, porter un plâtre ou commander un dîner dans un pays étranger.
3. **Situationnelle** : vécue par ceux dont les capacités peuvent changer radicalement dans des environnements spécifiques, comme être incapable d'entendre bien dans une foule bruyante, être visuellement handicapé dans une voiture ou de nouveaux parents faisant des tâches à une main.

C'était extrêmement révélateur pour moi d'avoir une exclusion temporaire, car je n'avais jamais été confronté à un tel défi au travail.

Néanmoins, je suis extrêmement privilégié puisque la mienne n'a duré que quelques jours, tandis que des millions de personnes dans le monde vivent des exclusions permanentes toute leur vie.

#### Coder pour le changement

Enfin, cela m'est venu : Implémenter l'a11y signifie contribuer à un **monde plus inclusif** ! Voici quelques choses que nous pouvons faire en tant qu'ingénieurs :

* Apprendre à écrire du code qui supporte l'a11y.
* Ajouter la conformité a11y comme partie de votre liste de contrôle de développement (comme vous travailleriez sur les tests unitaires et la documentation).
* Parler de l'a11y avec votre équipe, pour augmenter la sensibilisation.
* Évaluer si votre équipe produit du code accessible, et enregistrer les problèmes d'a11y comme des défauts à prendre en charge par l'équipe.
* Remettre en question les exigences commerciales qui ne couvrent pas l'a11y et exiger des alternatives accessibles.
* Partager votre expérience, et montrer à vos pairs comment adopter l'a11y de manière pratique, ce qui est la raison même pour laquelle j'écris cet article. :)

### 3 règles pragmatiques de l'accessibilité web

Me voici donc avec ma mission de distiller l'a11y en 3 règles pratiques qui resteront dans votre esprit. À partir de ces règles, vous devriez être en mesure de déduire le reste des connaissances et de trouver des conseils sur la mise en œuvre de l'a11y dans votre projet.

**Avertissement** : Ces règles ne remplacent pas le besoin d'apprendre l'a11y. Elles ne sont pas non plus exhaustives. Elles vous fourniront simplement une base efficace, afin que vous puissiez suivre le reste du chemin par vous-même.

Encore une fois, pour apprendre l'a11y, je recommande vivement de suivre le cours gratuit [Web Accessibility](https://www.udacity.com/course/web-accessibility--ud891) sur Udacity, par Google :

[**Web Accessibility | Udacity**](https://www.udacity.com/course/web-accessibility--ud891)
[_Obtenez une expérience pratique en rendant les applications web accessibles. Vous comprendrez quand et pourquoi les utilisateurs ont besoin d'accessibilité... www.udacity.com_](https://www.udacity.com/course/web-accessibility--ud891)

Passons maintenant aux 3 règles pragmatiques de l'accessibilité web. J'espère que vous pourrez les emporter avec vous et les appliquer chaque jour au travail :

#### 1) Insistez sur les éléments HTML sémantiques, ou faites-le vous-même

![Image](https://cdn-media-1.freecodecamp.org/images/1*YNNi0BjugGN3ouENt2g-Dw.jpeg)
"Le Web sémantique n'est pas intrinsèquement complexe. Le langage du Web sémantique, dans son essence, est très, très simple. Il s'agit simplement des relations entre les choses." — Tim Berners-Lee

Celle-ci est pour moi la **règle d'or de l'accessibilité**, sans conteste.

Les éléments **sémantiques** sont ceux qui transmettent une certaine signification avec le contenu qu'ils représentent, comme `<button>`, `<input>`, `<a>`, `<h1>` et `<p>`. Ils fournissent un certain contexte à l'agent utilisateur (navigateur, appareil ou technologie d'assistance comme un lecteur d'écran), afin qu'il sache comment interagir avec ces éléments et ce qu'il peut en attendre.

Ils sont différents des éléments **neutres**, tels que `<div>` et `<span>`, ou des éléments de **présentation** comme `<center>` et `<big>`, qui ne fournissent pas un tel contexte à l'agent utilisateur.

Les éléments sémantiques sont déjà accessibles (et SEO-friendly) pour la plupart. Cela signifie qu'ils couvrent déjà de nombreux aspects de l'a11y dès la sortie de la boîte, comme :

* la gestion du **focus** correctement via la touche de tabulation.
* la réponse aux **événements du clavier** (comme Entrée, Échap, espace, touches fléchées).
* la représentation d'informations **sémantiques** (Nom, Rôle, État et Valeur) afin que la technologie d'assistance puisse les comprendre.
* la conformité aux exigences de **contraste de couleur** avec le style par défaut.

Cependant, lorsque vous n'utilisez pas un élément sémantique, **vous êtes censé coder manuellement toutes ces choses afin de le rendre accessible**.

Ce qui signifie que vous devrez faire des choses comme :

* ajouter `tabindex="0"` pour que le composant fasse partie de l'ordre de tabulation naturel, et utiliser `focus()`, `display: none` ou `aria-hidden` pour éviter les pièges de focus. Apprenez-en plus sur tabindex sur [Using tabindex](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex).
* attacher des écouteurs pour les **événements du clavier** attendus. Vérifiez les attentes pour votre composant sur [WAI-ARIA Design Patterns and Widgets](https://www.w3.org/TR/wai-aria-practices-1.1/#aria_ex).
* utiliser un **rôle** pour fournir une certaine sémantique et une valeur SEO. Découvrez tous les rôles possibles sur [WAI-ARIA Categorization of Roles](https://www.w3.org/TR/wai-aria-1.1/#roles_categorization).
* fournir des **attributs ARIA** pour décrire l'état et la valeur. Découvrez quels attributs ARIA s'appliquent à chaque rôle sur [WAI-ARIA Definition of Roles](https://www.w3.org/TR/wai-aria-1.1/#role_definitions).
* faire attention au **contraste de couleur** et à l'**indicateur de focus**, surtout si vous utilisez `outline: 0` (ce qui n'est pas recommandé).

Encore sur les éléments sémantiques, voici quelques autres choses à garder à l'esprit :

* utilisez des [balises de sectionnement](https://www.w3.org/TR/wai-aria-practices/examples/landmarks/HTML5.html) pour structurer votre page en sections, sinon vous devez fournir des rôles de repère.
* utilisez des [balises de titre](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) pour organiser votre contenu textuel, afin d'exprimer la relation entre les sections et leur ordre d'importance. Pour l'enregistrement : Il ne doit y avoir qu'un seul `<h1>` sur chaque page.
* utilisez `<label for="...">` avec les champs de formulaire comme `<input>`, `<select>` et `<textarea>`.
* utilisez le bon outil pour le travail, par exemple si c'est un lien, utilisez `<a href="">` et jamais `<span onclick="...">`, et si c'est un bouton, utilisez `<button>` et jamais `<a href="#" onclick="...">`.

Eh bien, les éléments sémantiques semblent bien plus pratiques, ne pensez-vous pas ?

#### 2) Fournissez des alternatives pour les images, les couleurs, les sons et les mouvements

![Image](https://cdn-media-1.freecodecamp.org/images/1*MhrobCU9QTezLtLUFPGHpQ.jpeg)
"La peinture est juste une autre façon de tenir un journal." — Pablo Picasso

La technologie d'assistance gère mieux le texte. Lorsque vous utilisez autre chose, fournissez toujours une alternative textuelle, par exemple :

* Pour les images, fournissez une **alternative textuelle**. Vous pouvez utiliser `alt="description"` pour les **images informatives** (celles qui ont une signification, comme une photo ou une icône autonome) et `alt=""` pour les **images décoratives** (celles qui n'ont pas de signification, comme une icône à l'intérieur d'un bouton et juste à côté de son texte). Cela est particulièrement important pour les liens d'images.
* Toujours sur les images, lorsque vous vous appuyez sur elles pour l'interaction utilisateur, fournissez une **alternative audio**, ou explorez comment arrêter de vous appuyer sur elles. Vous pouvez vérifier [Google reCaptcha](https://www.google.com/recaptcha/intro/v3beta.html), par exemple.
* Pour les couleurs, lorsque vous indiquez un état de validation, une zone désignée ou simplement en distinguant des éléments, ajoutez un **indicateur secondaire** tel qu'un texte informatif, une icône ou même une info-bulle.
* Toujours sur les couleurs, découvrez le **ratio de contraste** de votre texte et vérifiez s'il répond à la norme que vous suivez. Par exemple, le niveau AA des WCAG exige un minimum de 4,5:1 pour le texte régulier et de 3:1 pour le texte grand.
* Pour les pistes audio et vidéo, fournissez des **sous-titres textuels** ou une **transcription** lorsqu'ils sont disponibles. Pour les sons d'action, fournissez une **alternative visuelle**.
* Pour le mouvement de l'utilisateur, chaque fois que nous attendons de l'utilisateur qu'il effectue des gestes spécifiques, rendez-les **optionnels** ou fournissez des **alternatives d'interaction** via le clavier.
* Pour le mouvement automatique, évitez les clignotements, les contenus mobiles et les nouvelles fenêtres. Lorsque c'est inévitable, ajoutez des **contrôles** pour ajuster le temps, mettre en pause ou masquer ce contenu. De plus, utilisez [aria-live](https://www.w3.org/TR/wai-aria-1.1/#aria-live) pour que le lecteur d'écran puisse notifier l'utilisateur chaque fois qu'une interruption se produit.

#### 3) Faites-en une habitude d'utiliser des outils a11y dans votre routine de travail

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tfk2GQ_VqsCsAKHbVnGEYA.jpeg)
"Nous façonnons nos outils, puis nos outils nous façonnent." — Marshall McLuhan

C'est peut-être la règle la plus efficace, donc lorsque vous laissez passer quelque chose des deux règles ci-dessus, celle-ci devrait le rattraper.

Je liste ici plusieurs outils a11y. Essayez-les, exécutez-les sur votre site web, voyez ce que vous en apprenez et essayez de rester avec eux.

Il y a essentiellement 3 types d'outils que je recommande d'adopter :

**a) Pour votre liste de contrôle de développement**

* [aXe chrome plugin](https://chrome.google.com/webstore/detail/lhdoppojpmngadmnindnejefpokejbdd) : Un vérificateur a11y facile à utiliser qui trouve les problèmes et fournit des corrections suggérées.
* [Wave](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh?hl=en-US) : Un outil d'évaluation a11y qui fournit un retour visuel sur l'accessibilité de votre contenu web en injectant des icônes et des indicateurs dans votre page.
* [DevTools (Accessibility pane, Contrast ratio and Audits)](https://developers.google.com/web/updates/2018/01/devtools#a11y) : Ces 3 fonctionnalités de DevTools permettent de naviguer dans l'arborescence d'accessibilité et de voir les propriétés a11y pour chaque élément, de vérifier le ratio de contraste des couleurs pour les éléments de texte, et d'effectuer des audits complets de page sur l'accessibilité (et d'autres métriques).
* [NoCoffee chrome plugin](https://chrome.google.com/webstore/detail/nocoffee/jjeeggmbnhckmgdhmgdckeigabjfbddl) : Simule les problèmes rencontrés par les personnes ayant des problèmes de vision légers à extrêmes.
* [High Contrast chrome plugin](https://chrome.google.com/webstore/detail/high-contrast/djcfdncoelnlbldjfhinnjlhdjlikmph) : Vous permet de naviguer sur le web avec votre choix parmi plusieurs filtres de couleur à haut contraste conçus pour faciliter la lecture du texte, afin que vous puissiez vérifier comment votre site web se comporte pour les utilisateurs ayant besoin d'un support à haut contraste.

**b) Pour les tests manuels avec de vrais lecteurs d'écran**

* Mac [VoiceOver](https://www.apple.com/voiceover/info/guide/_1124.html) (inclus dans macOS).
* Windows [NVDA](https://www.nvaccess.org/download/) (gratuit) et [JAWS](http://www.freedomscientific.com/Products/Blindness/JAWS?gclid=CjwKCAiA8vPUBRAyEiwA8F1oDDzHAjW9-GfooiNT3sCDcTg_7LNXvHz4XL7osONDyf3Y4k9KRbcuihoCKGMQAvD_BwE) (payant).

**c) Pour l'audit automatisé**

* [Google Lighthouse](https://www.npmjs.com/package/lighthouse) : Auditeur automatisé, similaire aux audits DevTools.
* [aXe](https://www.npmjs.com/package/axe-core) : Vérificateur automatisé pour les mêmes règles a11y trouvées sur le plugin chrome aXe.
* [Pa11y Dashboard](https://github.com/pa11y/pa11y-dashboard) : Une interface web qui vous aide à surveiller l'accessibilité de vos sites web.

#### En savoir plus

* [508, ADA, WCAG : Quelle est la différence ?](https://www.logicsolutions.com/508-ada-wcag-accessibility-difference/)
* [Rapport mondial sur le handicap de l'OMS](http://www.who.int/disabilities/world_report/2011/report/en/)
* [Accessible UI Components For The Web](https://medium.com/@addyosmani/accessible-ui-components-for-the-web-39e727101a67)
* [Microsoft Inclusive Design](https://www.microsoft.com/design/inclusive/)
* [Cours gratuit sur l'accessibilité web sur Udacity, par Google](https://www.udacity.com/course/web-accessibility--ud891)
* [Liste de contrôle WCGA 2 de WebAIM](https://webaim.org/standards/wcag/checklist)
* [Utilisation de tabindex](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex)
* [Modèles de conception et widgets WAI-ARIA](https://www.w3.org/TR/wai-aria-practices-1.1/#aria_ex)
* [Catégorisation des rôles WAI-ARIA](https://www.w3.org/TR/wai-aria-1.1/#roles_categorization)
* [Éléments de sectionnement HTML5](https://www.w3.org/TR/wai-aria-practices/examples/landmarks/HTML5.html)