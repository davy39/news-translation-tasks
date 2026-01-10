---
title: Comment choisir une police – Un guide approfondi pour les développeurs
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2023-09-13T11:18:31.000Z'
originalURL: https://freecodecamp.org/news/things-to-consider-when-picking-fonts
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/markus-spiske-f81ym3dE5N4-unsplash.jpg
tags:
- name: fonts
  slug: fonts
- name: performance
  slug: performance
- name: UI Design
  slug: ui-design
seo_title: Comment choisir une police – Un guide approfondi pour les développeurs
seo_desc: 'Fonts are not always free. If you''re fetching a font that is not already
  on your user''s phone or computer, they will have to download it. And this will
  impact performance.

  In documents and subtitles, embedding fonts can easily increase the file size ...'
---

Les polices ne sont pas toujours gratuites. Si vous récupérez une police qui n'est pas déjà sur le téléphone ou l'ordinateur de votre utilisateur, celui-ci devra la télécharger. Et cela impactera les performances.

Dans les documents et les sous-titres, l'incorporation de polices peut facilement multiplier par dix la taille du fichier. En ce qui concerne le web, voici quelques polices populaires et leur impact potentiel sur le réseau :

| Police | Taille | Wi-Fi | 4G/LTE standard | 3G standard |
| --- | --- | --- | --- | --- |
| [Roboto](https://fonts.google.com/specimen/Roboto) | 168,3 Ko | 0,05 s | 0,36 s | 1,90 s |
| [Montserrat](https://fonts.google.com/specimen/Montserrat) | 198,0 Ko | 0,05 s | 0,42 s | 2,21 s |
| [Inter](https://fonts.google.com/specimen/Inter) | 309,8 Ko | 0,08 s | 0,64 s | 3,40 s |
| [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) | 556,2 Ko | 0,15 s | 1,13 s | 6,03 s |
| [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) | 187,9 Ko | 0,05 s | 0,40 s | 2,10 s |

Les vitesses de réseau estimées et la latence sont tirées de [Throttling - Firefox Source Docs](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/throttling/index.html).

Sur le web moderne, nous avons normalisé la récupération de polices côté client, ou l'incorporation de polices dans les ressources servies aux utilisateurs. Bien que cela puisse être tentant, cela a en réalité peu de sens pour la plupart des cas d'utilisation.

Cela ne suggère pas de ne jamais utiliser de polices externes. Juste un rappel que les polices ne sont pas gratuites, et qu'il est bon de vérifier si cela vaut la peine d'incorporer ou de récupérer des polices externes lorsque cela peut être évité.

Au lieu de cela, je vous recommande de considérer une sélection étendue de polices, présentant des caractères disponibles sur différents systèmes d'exploitation. Il y a des moments où nous devons récupérer des polices externes, mais cela ne devrait pas être l'attitude par défaut dans tout ce que nous construisons.

En bref, vous avez peut-être juste besoin d'une police arbitraire pour afficher du texte arbitraire sur votre site web. C'est bien. Mais il vaut la peine de s'en tenir à la large gamme de polices déjà installées sur le système d'exploitation du client.

En d'autres termes… ne récupérez une police externe que lorsqu'elle améliore réellement l'expérience utilisateur !

## Pourquoi ?

Étant donné le nombre de polices disponibles sur tous les systèmes d'exploitation, il existe probablement de nombreuses options adaptées à votre cas d'utilisation.

Il n'est pas nécessaire de récupérer spécifiquement Roboto, Inter, ou une autre police similaire aux options préinstallées.

Cela est particulièrement pertinent pour les sites web corporatifs, les blogs, les forums et les applications web.

L'utilisateur est là pour consulter du contenu ou accomplir une tâche. À moins que vous ne cherchiez à être créatif, l'utilisateur moyen ne sait pas, et ne se soucie pas, de la police utilisée tant qu'elle est lisible.

Pendant ce temps, il peut se soucier d'autres choses impactées par vos choix de polices…

### Performance

Que nous parlions d'incorporer des polices dans des documents hors ligne, ou de récupérer des polices sur le web, cela augmente la taille globale et le temps de chargement des ressources.

Les polices peuvent atteindre plus de 160 Ko par style de police. L'impact de cela peut être significatif sur les réseaux plus lents ou les anciens appareils mobiles.

Particulièrement sur le web, vous tirerez plus de valeur en construisant une expérience utilisateur ultra-rapide, plutôt qu'en récupérant une police que l'utilisateur n'a pas demandée.

Jusqu'à ce que la police ait fini de se charger, les sites peuvent choisir de bloquer le rendu ou de permuter, ce qui n'est pas idéal.

La permutation de police se produit lorsque la police change peu après la visite du site, entraînant un scintillement et une augmentation du [Cumulative Layout Shift](https://web.dev/cls/).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/mdn-font-swap.gif align="left")

*Une démonstration du blocage et de la permutation de police sur le site MDN. J'ai actualisé avec le cache désactivé sur un laptop haut de gamme connecté au Wi-Fi sans limitation.*

![Image](https://www.freecodecamp.org/news/content/images/2023/09/out.gif align="left")

*Une démonstration du site MDN utilisant Nimbus Sans, basé sur Helvetica, au lieu de polices externes. J'ai actualisé dans les mêmes conditions.*

Abandonner les polices externes est assez simple, mais peut améliorer le temps de chargement, réduire l'utilisation de la bande passante et éviter la permutation de police, ce qui améliore tous vos [Core Web Vitals](https://web.dev/vitals/) et votre SEO.

### Vie privée

Lorsque vous récupérez des polices depuis un serveur tiers tel que Google Fonts, des informations client sont divulguées au tiers. Cela inclut l'[Adresse IP](https://developer.mozilla.org/en-US/docs/Glossary/IP_Address), le [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), et le [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer), parmi d'autres en-têtes.

Chaque site web qui charge une police depuis Google Fonts a donné à Google le potentiel de suivre le visiteur. Le domaine que vous avez visité, l'heure à laquelle vous y avez accédé, quel navigateur et système d'exploitation vous utilisez, etc. Ils peuvent établir une chronologie des sites que vous visitez à partir des polices seules.

Google déclare qu'ils ne suivent ni ne stockent ces informations. Cependant, étant donné la nature d'Internet, ils les reçoivent inévitablement.

L'Allemagne a effectivement statué que les sites web chargeant Google Fonts violent le RGPD :

%[https://thehackernews.com/2022/01/german-court-rules-websites-embedding.html]

Ce problème peut être évité en servant soi-même les polices. Si vous allez utiliser une police externe, veuillez considérer cela.

Cependant, sachez également que certains utilisateurs [désactivent les polices personnalisées](https://support.mozilla.org/en-US/kb/change-fonts-and-colors-websites-use#w_custom-fonts) ou [bloquent les polices tierces](https://github.com/gorhill/uBlock/wiki/Per-site-switches#no-remote-fonts), donc vous devriez toujours spécifier au moins un nom de famille générique quoi qu'il en soit.

> "Vous devriez toujours inclure au moins un nom de famille générique dans une liste `font-family`, car il n'y a aucune garantie qu'une police donnée soit disponible. Cela permet au navigateur de sélectionner une police de repli acceptable lorsque nécessaire." (Source : [Documentation MDN pour font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#try_it))

### Familiarité

Les utilisateurs sont familiers avec l'expérience de leur système d'exploitation.

Peut-être pas avec son fonctionnement interne, ou même comment effectuer des opérations simples, mais ils rencontrent régulièrement l'écran de bienvenue, les menus contextuels et leurs applications préinstallées.

Il est plus sûr de rester avec les polices auxquelles l'utilisateur a déjà accès car ce sont les polices auxquelles l'utilisateur est déjà habitué à lire.

Cet argument est similaire à pourquoi il est bon d'utiliser le sélecteur de date système, le sélecteur de couleur, ou les boîtes de dialogue/modales au lieu d'en créer des personnalisées.

Les utilisateurs sont familiers avec leur système !

D'après mon expérience, souvent l'une des situations suivantes se produit :

* L'utilisateur n'a pas remarqué qu'une police externe était utilisée, la rendant largement redondante. La plupart des non-spécialistes vivent cela tous les jours, il est difficile de dire que les sites web utilisent des polices différentes les unes des autres à moins d'y être conscient.

* L'utilisateur a pu le remarquer, et a donc une expérience de lecture différente de ce à quoi il est habitué. Le potentiel de perturbation dépend des besoins de l'utilisateur, mais ce risque est souvent inutile.

À moins d'avoir une raison de la changer, il est préférable de rester avec ce que l'utilisateur connaît.

## Qui d'autre fait cela ?

Wikipedia est l'exemple le plus notable, et ils ont même une page élaborant sur le sujet : [Page Meta sur l'utilisation de la typographie par Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Typography).

Certains des sites les plus populaires ne chargent aucune police sur leur page d'accueil, préférant utiliser uniquement des polices système :

| Site | Sélecteur de police |
| --- | --- |
| Facebook | `SFProDisplay-Regular, Helvetica, Arial, sans-serif` |
| Instagram | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` |
| Cloudflare | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif` |
| Wikipedia | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, Helvetica, Arial, sans-serif` |
| Reddit | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif` |
| Bing | `"Segoe UI", Segoe, Tahoma, Arial, Verdana, sans-serif` |

Vous pouvez vérifier par vous-même en inspectant le site avec les outils de développement de votre navigateur.

Il n'y a aucune requête réseau sortante pour les polices, et les propriétés `font-family` sont définies sur des polices système uniquement.

## Exceptions

Il y a des moments où charger et incorporer des polices a du sens, particulièrement si l'apparence que vous recherchez est significativement différente des polices système courantes :

* Vous ciblez un environnement qui n'a pas de polices disponibles.

* Pour correspondre à une marque existante, comme une police interne.

* Un design créatif ou unique, particulièrement pertinent pour les sites de jeux et artistiques.

* Les polices d'icônes comme [OpenMoji](https://openmoji.org/), mais notez que la plupart des clients ont déjà des emojis.

* Un site web qui est littéralement pour distribuer, afficher et tester des polices.

## Conséquences

Si vous appliquez une pile de polices locales, votre contenu textuel peut ne pas avoir l'air identique pixel par pixel sur tous les clients. Cependant, le succès devrait être mesuré par l'expérience utilisateur.

Il est important que le site semble familier, mais il existe déjà des changements plus significatifs entre les clients, comme l'interface humaine, les résolutions et le DPI.

Comparé à cela, ce n'est pas grave si l'arche du `a` a un rayon légèrement différent, ou si la barre du `l` est quelques pixels plus longue. En fait, cela est peu susceptible d'être remarqué, donc il est peu probable que cela impacte l'expérience utilisateur.

Les utilisateurs auraient plus tôt des problèmes avec la différence de vitesse ou un scintillement, avant la différence entre des polices similaires.

Un autre argument est que permettre différentes polices peut rendre la mise en page difficile à gérer. Les glyphes peuvent avoir différentes largeurs, et donc occuper un espace variable.

Cependant, les sites modernes devraient suivre le [design responsive](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design), donc vous devriez prendre le temps de rendre les pages fluides de toute façon.

Pour minimiser l'impact, vous pouvez utiliser des [polices web sûres](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals#web_safe_fonts).

Si vous n'aimez pas à quel point cela est limitant, choisissez une police incluse avec votre système d'exploitation, et trouvez des polices similaires sur d'autres systèmes d'exploitation.

Mieux encore si vous pouvez choisir des [polices métriquement compatibles](https://en.wikipedia.org/wiki/Typeface#metrics).

### Comparaison

Visons un site web et voyons à quoi cela ressemble de désactiver les polices téléchargeables.

Je vais également remplacer tous les sélecteurs de police, pour utiliser Helvetica.

Notez que mon ordinateur n'a pas réellement Helvetica installé, donc mon système d'exploitation le traduit automatiquement en Nimbus Sans, qui est basé sur Helvetica. Nimbus Sans est préinstallé sur [Debian](https://www.debian.org/).

Dans le cas de MDN, la deuxième version est-elle vraiment si indésirable que nous devons charger une police de 325 Ko, étant donné les pénalités et démonstrations soulevées ci-dessus ? En fin de compte, cela dépend des préférences de l'utilisateur, donc je vous laisse décider.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1.png align="left")

*MDN, avec la police Inter récupérée côté client.*

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-1.png align="left")

*MDN, avec la font-family remplacée pour utiliser Helvetica.*

D'un autre côté, cela ne signifie pas de ne jamais récupérer de polices. Il existe des exemples où l'esthétique peut être plus précieuse pour l'expérience utilisateur que la pénalité de performance.

Regardons [Framasoft](https://framasoft.org/). Ils ont opté pour un look et une sensation plus créatifs, mettant également en avant de nombreuses illustrations de [David Revoy](https://www.davidrevoy.com/).

Utiliser Tovari Sans était un choix de design qui améliore l'expérience utilisateur, et n'est pas facilement remplaçable par une pile de polices locales.

Si nous devions supprimer cette police, la page semble incohérente et non polie. Même si nous nettoyions le CSS, nous détériorerions toujours le thème du site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-2.png align="left")

*Framasoft, avec la police Tovari Sans récupérée côté client.*

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-4.png align="left")

*Framasoft, avec la font-family remplacée pour utiliser Helvetica.*

## Ressources

Que vous souhaitiez utiliser des polices locales, ou que vous ayez simplement besoin de spécifier quelques polices de repli, voici quelques ressources utiles pour choisir votre pile de polices :

* [Liste des polices incluses avec les systèmes d'exploitation Apple](https://developer.apple.com/fonts/system-fonts/)

* [Liste des polices incluses avec Windows](https://learn.microsoft.com/en-us/typography/fonts/windows_11_font_list#introduction)

* [Polices principales incluses avec ChromeOS](https://en.wikipedia.org/wiki/Croscore_fonts)

* [Documentation pour les polices web sûres](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals#web_safe_fonts)

## Piles de polices multiplateformes

Il existe d'innombrables articles et ressources en ligne qui proposent des listes de polices prédéfinies que vous pouvez utiliser. Celles-ci sont appelées "*piles de polices*".

En particulier, je souhaite mettre en avant une ressource de [Dan Klammer](https://danklammer.com/), un designer et développeur web qui a créé [Modern Font Stacks](https://modernfontstacks.com/) ([Dépôt GitHub](https://github.com/system-fonts/modern-font-stacks)), un site qui vous aide à choisir des piles de polices natives pour votre projet.

Modern Font Stacks propose une liste de polices pour une variété de styles comme Neo-Grotesque (un style de sans-serif) ou Monospace Code (un style de monospace) et offre une visualisation de leur apparence sur différents systèmes d'exploitation. Il passe en revue une description de chaque pile, le CSS à utiliser, les métadonnées comme les poids disponibles, et quelles polices vous avez personnellement installées.

Certaines classifications de polices n'incluent pas explicitement une police de chaque système d'exploitation existant, mais rappelez-vous que la famille de polices générique (`sans-serif`, `serif`, `monospace`, `cursive`, etc.) à la fin vous couvrira.

Si vous aimez la pile, vous pouvez l'utiliser. Mais ne vous sentez pas limité non plus, vous pouvez également l'utiliser comme point de départ et ajuster la pile de polices selon vos besoins.

J'ai inclus des images du dépôt GitHub (au moment de l'écriture), présentant des piles de polices proposées pour deux des styles les plus courants utilisés sur Internet aujourd'hui :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/neo-grotesque.png align="left")

*Pile de polices de base proposée par Modern Font Stacks pour le style Neo-Grotesque, un type de police sans-serif.*

![Image](https://www.freecodecamp.org/news/content/images/2024/05/monospace-code.png align="left")

*Pile de polices de base proposée par Modern Font Stacks pour le style Monospace Code, un type de police monospace.*

## Conclusion

En fin de compte, l'expérience utilisateur est ce qui compte le plus. Parfois, cela signifie privilégier le design visuel, d'autres fois, cela signifie privilégier la performance.

J'espère que cela a valu votre temps, et qu'avec ces connaissances vous pourrez prendre une décision éclairée lors du choix des polices pour votre prochain projet.

Les retours et questions sont les bienvenus, vous pouvez me contacter sur [GitHub](https://github.com/SethFalco), [Mastodon](https://fosstodon.org/@sethi), ou [LinkedIn](https://www.linkedin.com/in/sethfalco/)!