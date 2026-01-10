---
title: Comment partager des liens qui ancrent à n'importe quel texte sur une page
  web
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2022-08-09T19:54:25.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-share-links-that-anchor-to-any-text-on-a-webpage
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/untitled.png
tags:
- name: url
  slug: url
- name: Web Development
  slug: web-development
seo_title: Comment partager des liens qui ancrent à n'importe quel texte sur une page
  web
seo_desc: 'Did you know that there''s an unofficial draft specification for a feature
  that would allow arbitrary text to be passed to the fragment (#) of a URL?

  This would allow users to share links that point to any particular text on a webpage!

  What''s a URI fr...'
---

Saviez-vous qu'il existe une [ébauche non officielle](https://wicg.github.io/scroll-to-text-fragment/) de spécification pour une fonctionnalité qui permettrait de passer du texte arbitraire au fragment (`#`) d'une URL ?

Cela permettrait aux utilisateurs de partager des liens qui pointent vers n'importe quel texte particulier sur une page web !

## Qu'est-ce qu'un fragment URI ?

Le [fragment URI](https://en.wikipedia.org/wiki/URI_fragment) est la partie facultative à la fin d'une URL qui commence par un caractère dièse (`#`). Il vous permet de faire référence à une partie spécifique du document que vous avez consulté.

Par exemple, si vous visitez le lien suivant, vous ferez automatiquement défiler jusqu'au haut de la section que vous lisez en ce moment !

[Qu'est-ce qu'un fragment URI ?](#heading-quest-ce-quun-fragment-uri)

En supposant que vous consommez cet article dans le navigateur, vous remarquerez que l'URL change également. Elle est maintenant suivie de `#quest-ce-quun-fragment-uri`, qui est l'ID que le [Ghost CMS](https://ghost.org/) a attribué à l'en-tête.

## Qu'est-ce qui change ?

Auparavant, la principale façon d'ancrer des liens à une partie d'une page était de spécifier l'ID d'un élément HTML dans le fragment ([source](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)).

Cela mettait les lecteurs à la merci du développeur web ou du rédacteur de contenu. Si les rédacteurs ne fournissaient pas d'IDs appropriés, il n'y aurait aucun moyen d'ancrer des liens à cette section.

Certains sites web ou outils fournissent une méthode non standard pour gérer cela, notamment la mise en surbrillance. Par exemple, dans [Read the Docs](https://readthedocs.org/), vous pouvez passer le paramètre de requête `highlight` pour mettre en surbrillance n'importe quel texte particulier sur la page.

Vous pouvez l'essayer dans la [documentation de Weblate](https://docs.weblate.org/en/latest/).

![La documentation de Weblate ouverte sur la page des traductions automatiques. Le paramètre de requête highlight est spécifié, donc toutes les instances du mot "LibreTranslate", non sensibles à la casse, sont mises en surbrillance.](https://www.freecodecamp.org/news/content/images/2022/08/image-186.png align="left")

[*Voici ce que vous voyez lorsque vous spécifiez le* paramètre de requête `highlight` sur la documentation de Weblate.](https://docs.weblate.org/en/latest/admin/machine.html?highlight=libretranslate#libretranslate)

Les fragments de texte sont une proposition relativement nouvelle qui étend l'utilisabilité des fragments URI pour interroger et mettre en surbrillance n'importe quel texte arbitraire également.

## Pourquoi cela serait-il utile ?

Pouvez-vous vous identifier à un ou plusieurs de ces scénarios ?

* Lorsque vous sourcez des informations, vous pouvez lier directement à la citation ou au contenu que vous avez cité.

* En tant que membre du personnel de support, vous pouvez lier et mettre en surbrillance un extrait particulier de la documentation ou de la FAQ pour l'utilisateur.

* Les fragments de texte peuvent être utilisés avec n'importe quel document texte arbitraire qui ne peut pas stocker de métadonnées d'ancrage, comme des fichiers texte brut ou de configuration.

* Vous êtes un développeur web qui a implémenté une solution personnalisée pour cela, mais qui peut maintenant laisser le navigateur s'en charger pour vous.

Si c'est le cas, cela pourrait aider à mieux attribuer le contenu sur le web, à mettre en évidence les informations dont vos utilisateurs ont besoin, ou à soulager certains efforts de maintenance pour les développeurs.

## La proposition

Vous pouvez spécifier soit du texte littéral, soit le début et la fin d'une plage de texte. La spécification inclut un pseudo-diagramme qui démontre à quoi ressemble la syntaxe :

```plaintext
:~:text=[prefix-,]textStart[,textEnd][,-suffix]

         context  |-------match-----|  context
```

Ou alternativement, une version plus digeste :

| Section | Requis | Description | Notes |
| --- | --- | --- | --- |
| `prefix` | false | La valeur doit apparaître avant le texte, mais ne sera pas mise en surbrillance. | Doit se terminer par `-`. |
| `textStart` | true | Si `textEnd` n'est pas spécifié, correspond littéralement, sinon utilisé en combinaison avec `textEnd` pour correspondre à une plage. |  |
| `textEnd` | false | Utilisé en combinaison avec `textStart` pour correspondre à une plage de texte. |  |
| `suffix` | false | La valeur doit apparaître après le texte, mais ne sera pas mise en surbrillance. | Doit commencer par `-`. |

Les sections `prefix` et `suffix` sont utilisées pour le contexte, donc si le texte que vous souhaitez correspondre apparaît plusieurs fois sur une page, vous pouvez les utiliser pour indiquer au navigateur quelle instance vous souhaitez correspondre.

Pour fournir quelques exemples, supposons que nous ouvrons le site web de Web Monetization qui inclut le texte suivant.

> Une API de navigateur JavaScript qui permet la création d'un flux de paiement de l'agent utilisateur vers le site web
> 
>  [https://webmonetization.org/](https://webmonetization.org/)

| Exemple | Mise en surbrillance |
| --- | --- |
| `:~:text=javascript` | JavaScript |
| `:~:text=api,stream` | API qui permet la création d'un flux de paiement |
| `:~:text=javascript-,browser` | browser |
| `:~:text=a-,javascript,api` | JavaScript browser API |
| `:~:text=that-,allows,stream,-from` | allows the creation of a payment stream |

Pour les extraits de texte plus longs, une plage est préférée pour éviter de gonfler l'URL. Habituellement, les développeurs visent à garder la longueur totale des URLs en dessous de 2 000 caractères environ. Cela évite les problèmes potentiels avec les anciens agents utilisateurs, surtout après avoir tenu compte de la longueur du domaine et des paramètres de requête.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-1.png align="left")

[*Voici à quoi ressemble la mise en surbrillance sur Chromium lorsque vous visitez une page web avec un fragment de texte.*](https://en.wikipedia.org/wiki/Matrix_(protocol)#:~:text=KDE,client%20Konversation)

### Détails de l'implémentation

D'après la lecture de la spécification et les tests manuels dans un navigateur Chromium, voici quelques détails plus fins concernant l'interrogation de contenu dans un fragment de texte.

* Les sections ne sont pas sensibles à la casse, et les accents sont ignorés ([source](https://wicg.github.io/scroll-to-text-fragment/#finding-ranges-in-a-document))

* Toutes les sections correspondent uniquement à des mots entiers, donc vous ne pouvez pas correspondre partiellement

* Seule la première correspondance sera mise en surbrillance s'il y en a plusieurs ([source](https://wicg.github.io/scroll-to-text-fragment/#syntax))

## Compatibilité

Les fragments de texte sont disponibles dans la plupart des navigateurs Chromium, car cela a été implémenté dans [Chromium lui-même en 2020](https://chromestatus.com/feature/4733392803332096).

Les fragments de texte ne sont pas encore disponibles dans Firefox. Mozilla espère avoir cela implémenté dans le futur  en février 2022, ils [ont ouvert un ticket pour suivre les progrès](https://bugzilla.mozilla.org/show_bug.cgi?id=1753933).

%[https://caniuse.com/url-scroll-to-text-fragment] 

## Vie privée et sécurité

Certaines préoccupations ont été soulevées avec les spécifications, notamment que le défilement automatique vers des parties de la page peut révéler certains détails sur l'utilisateur.

Une chose intéressante à propos des fragments URI est qu'ils ne devraient pas être envoyés aux serveurs web pour traitement. Les fragments URI sont destinés à être un mécanisme côté client/agent utilisateur uniquement, à traiter localement par le navigateur ou l'application web.

Pour vérifier cela, nous pouvons exécuter un petit serveur Express qui enregistre simplement l'URL. Nous verrons s'il inclut le fragment :

```js
const express = require('express');
const app = express();
const port = 3000;

app.get('*', (req, res) => {
   console.log('URL:', req.url);
   res.status(204).send();
});

app.listen(port, () => {
   console.log(`Listening on port ${port}.`); 
});
```

![Exécution d'un serveur web et exécution de commandes curl pour le frapper. Lorsque nous spécifions un fragment dans l'URL dans curl, le serveur web ne le reçoit pas.](https://www.freecodecamp.org/news/content/images/2022/08/Peek-2022-08-06-18-12.gif align="left")

*Les résultats de chaque requête via curl. Les mêmes chaînes auraient été imprimées si j'avais exécuté les requêtes dans un navigateur.*

Certains sites web profitent de cela pour améliorer la confidentialité et réduire la bande passante envoyée aux serveurs web.

Par exemple, si vous regardez [TypeScript Playground](https://www.typescriptlang.org/play), vous remarquerez qu'au lieu d'utiliser des paramètres de requête ou de construire une URL courte, ils encodent simplement le TypeScript et le stockent dans le fragment URI.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled.png align="left")

*Observez comment l'URL inclut un fragment URI. C'est en fait juste* `console.log('Hello, World!');` mais encodé.

Avec une implémentation comme celle-ci, vous pouvez mettre en signet ou partager le lien avec n'importe qui, et leur serveur web ne saura pas ou ne se souciera pas du code. Cependant, tout service que vous utilisez pour partager le lien pourrait, bien sûr, le décoder et le lire.

Cependant, la préoccupation soulevée avec les fragments de texte est que, si un agent utilisateur fera automatiquement défiler vers une section donnée d'une page, alors que le fragment de texte n'aurait pas été partagé avec le serveur web, des requêtes réseau peuvent avoir été induites telles que le chargement d'images sur cette partie du site. Cela permettrait au serveur web de déduire que vous avez été lié à cette section de la page ([source](https://github.com/WICG/scroll-to-text-fragment/issues/76)).

Malgré ces préoccupations, il semble que les fragments URI dans leur ensemble aient été sensibles à cela depuis longtemps, pas seulement les fragments de texte.

Quoi qu'il en soit, c'est une bonne chose à garder à l'esprit jusqu'à ce que les développeurs de navigateurs et les chercheurs en sécurité y réfléchissent davantage.

## Extension de lien vers le fragment de texte

Google a également développé une [extension](https://github.com/GoogleChromeLabs/link-to-text-fragment) qui fournit une interface utilisateur pour lier n'importe quel texte arbitraire en tant qu'URL.

L'extension ajoute "Copier le lien vers le texte sélectionné" au menu contextuel lorsque vous sélectionnez du texte et cliquez dessus avec le bouton secondaire. Vous pouvez le voir en action dans la vidéo suivante.

%[https://www.youtube.com/watch?v=Y5DmGqnzvBI] 

%[https://chrome.google.com/webstore/detail/link-to-text-fragment/pbcodcjpfjdpcineamnnmbkkmkdpajjg] 

L'extension est également disponible pour Firefox et polyremplit une implémentation de fragments de texte dans chaque page web, donc elle fera même défiler et mettre en surbrillance le texte correspondant.

%[https://addons.mozilla.org/en-US/firefox/addon/link-to-text-fragment/] 

## Conclusion

J'espère que cela donne plus d'informations sur les fragments URI dans leur ensemble, et surtout sur les fragments de texte.

Si vous avez des idées pour améliorer la spécification, n'hésitez pas à consulter les problèmes ouverts sur les dépôts des navigateurs et du WICG et à fournir vos réflexions.

J'ai hâte de voir plus de navigateurs supporter cela, car cela rend l'expérience de citation, d'attribution et de lien vers le contenu sur le web beaucoup plus pratique.