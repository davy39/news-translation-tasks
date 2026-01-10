---
title: Qu'est-ce que le XSS ? Comment protéger votre site web contre les attaques
  par script inter-sites basées sur le DOM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-03T19:51:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-protect-against-dom-xss-attacks
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/xss-code-case.jpg
tags:
- name: Application Security
  slug: application-security
- name: DOM
  slug: dom
- name: information security
  slug: information-security
- name: Web Security
  slug: web-security
seo_title: Qu'est-ce que le XSS ? Comment protéger votre site web contre les attaques
  par script inter-sites basées sur le DOM
seo_desc: 'By Andrej Kovacevic

  Website security issues and vulnerabilities are a global problem as cyber security
  vulnerabilities are increasing. We have seen a major rise in the average number
  of these cases in the past few years, and 2021 saw an all-time high...'
---

Par Andrej Kovacevic

**Les problèmes de sécurité des sites web** et les vulnérabilités sont un problème mondial, car les vulnérabilités en matière de cybersécurité augmentent. Nous avons observé une hausse majeure du nombre moyen de ces cas au cours des dernières années, et 2021 a connu un niveau record.

Dans ce tutoriel, nous allons donc parler des problèmes de sécurité liés au XSS basé sur le DOM et de l'impact qu'ils peuvent avoir sur vos données. Assurez-vous de lire jusqu'à la fin. Commençons par nous rafraîchir la mémoire sur quelques bases concernant la sécurité des scripts inter-sites basés sur le DOM.

## Qu'est-ce que le Cross-Site Scripting ?

Le cross-site scripting, également appelé XSS, est un [problème de sécurité des sites web](https://www.wix.com/blog/2022/01/website-security/) qui compromet les informations et les données des utilisateurs lorsque ces personnes utilisent une application vulnérable. L'attaquant peut utiliser cela pour contourner la politique d'origine, qui sépare deux sites web l'un de l'autre.

Les attaquants peuvent utiliser le XSS pour se faire passer pour un utilisateur, effectuer des actions qu'un utilisateur ferait et accéder aux informations de l'utilisateur. Cela peut également permettre aux attaquants d'obtenir un accès complet aux informations de l'utilisateur s'ils ont les permissions et les privilèges. Cela peut également prendre le contrôle des actions et des performances complètes du site web si cela continue.

Pour vous aider à mieux comprendre ces types d'attaques, nous allons discuter de quelques fondamentaux sur le fonctionnement du XSS et ce qu'il fait.

## Comment fonctionne le XSS ?

Le cross-site scripting utilise la technologie pour manipuler un site vulnérable afin qu'il envoie du JavaScript dangereux aux utilisateurs. Cela permet à l'attaquant d'obtenir un accès complet au site lorsque le script accède au système de l'utilisateur. Mais l'utilisateur doit d'abord exécuter le JavaScript.

### Types d'attaques XSS

#### XSS réfléchi :

Ce script malveillant provient de la requête HTTP. Il s'agit du type d'attaque XSS le plus basique, où une application pourrait recevoir des données malveillantes et les réfléchir immédiatement vers l'utilisateur.

La charge utile de l'attaquant doit faire partie de la requête envoyée à un serveur, qui est ensuite réfléchie et exécutée sur l'application de l'utilisateur.

Un exemple de cela serait un attaquant convainquant quelqu'un de cliquer sur un lien de phishing avant qu'il ne prenne effet.

#### XSS stocké :

Ce script malveillant provient de la base de données du site web. L'attaquant saisit la requête malveillante sur le serveur où elle pourrait rester de manière permanente sauf si elle est traitée manuellement.

Par exemple, l'attaquant pourrait insérer un script malveillant dans un champ de commentaire, qui serait affiché pour tout le monde qui visite la page. Même sans interagir directement avec le script, les visiteurs de la page pourraient être victimes de cette attaque.

#### XSS basé sur le DOM :

Cette vulnérabilité plus avancée existe dans le code client et non dans le code serveur. Le XSS basé sur le DOM n'est ni réfléchi ni stocké sur le serveur, mais existe dans le Document Object Model (DOM) d'une page. L'application web lit le code malveillant et l'exécute dans le navigateur dans le cadre du DOM, ce qui est plus difficile à détecter car il ne passe pas par le serveur.

Les **vulnérabilités de sécurité** impliquées dans les attaques XSS basées sur le DOM sont une préoccupation sérieuse pour la plupart des sites web. Nous allons parler de certains des risques les plus courants que vous rencontrez sur les plateformes de construction web open source telles que WordPress en ce qui concerne les piratages DOM - XSS.

Cela permet à l'attaquant d'exécuter du code JavaScript malveillant dans le navigateur de la victime, permettant potentiellement à l'attaquant de voler des informations sensibles ou d'effectuer d'autres actions nuisibles au nom de la victime.

Voici un exemple d'une attaque XSS basée sur le DOM :

```javascript
<script>
 // Cette fonction est destinée à prendre une URL fournie par l'utilisateur et à l'afficher sur la page
 function displayURL(url) {
  // L'URL est passée via innerHTML, qui peut exécuter du code JavaScript
  document.getElementById("display").innerHTML = url;
 }
</script>

<!-- L'entrée fournie par l'utilisateur est passée à la fonction displayURL -->
<p>Entrez une URL à afficher : <input type="text" id="user-input" /></p>
<button onclick="displayURL(document.getElementById('user-input').value)">
 Afficher l'URL
</button>

<!-- L'URL est affichée dans cette div -->
<div id="display"></div>
```

Rappelez-vous que ce tutoriel est purement à des fins éducatives, pour vous aider à reconnaître et à vous défendre contre le XSS. Vous ne devriez pas utiliser ces informations pour effectuer ce genre d'attaques.

## Vulnérabilités DOM XSS - WordPress

La principale cible des attaques DOM XSS sur WordPress est ses utilisateurs. Les utilisateurs entrent leurs détails, comptes et identifiants de site pour accéder à leurs sites WordPress et c'est ce que les attaques DOM XSS visent à compromettre en ligne. Les attaquants peuvent utiliser le DOM XSS pour accéder aux informations et détails des utilisateurs en un seul clic.

Cela inclut également vos cookies, informations et autres, ce qui en fait l'une des **vulnérabilités de sécurité WordPress** les plus courantes.

Voici quelques-uns des principaux problèmes de sécurité des sites web WordPress que vous devez garder à l'esprit pour assurer une meilleure sécurité des scripts inter-sites.

### Accéder aux informations privées d'un utilisateur

L'une des vulnérabilités de sécurité WordPress les plus courantes impliquées dans les attaques DOM XSS est que les attaquants peuvent obtenir des informations utiles et même prendre complètement le contrôle du site d'un utilisateur. Cela peut souvent faire escalader les choses rapidement et causer une compromission complète des données.

### Usurper l'identité d'un utilisateur

Les attaquants peuvent se faire passer pour l'utilisateur, pour interagir avec les utilisateurs en ligne, clients et clients de la victime afin d'obtenir leurs informations.

### Compromettre un site

Un autre problème de sécurité courant des scripts inter-sites avec les sites web est que ces attaques peuvent compromettre le site web et prendre l'accès de l'utilisateur. Cela inclut l'affichage de contenu déviant sur le site (ou de contenu qui n'est pas originaire du site).

D'autres cas peuvent impliquer de changer l'apparence de WordPress en ligne. D'autres personnes peuvent également exploiter le site web en installant du contenu explicite.

### Ingénierie sociale

Dans des cas plus graves, les attaquants peuvent impacter le site WordPress par le biais de tentatives de phishing. Il s'agit d'une préoccupation courante pour les vulnérabilités de sécurité des constructeurs web que nous allons discuter brièvement.

L'impact des problèmes de sécurité des scripts inter-sites varie pour chaque site web. Cependant, les sites WordPress sont généralement plus à risque de ces types de compromissions car les utilisateurs enregistrent leurs informations personnelles sur le site web. Le risque augmente davantage si l'utilisateur est un administrateur, car l'attaquant peut compromettre l'ensemble du site WordPress.

## DOM XSS et plateformes de construction web à code fermé

Les constructeurs de sites web tels que Weebly, Squarespace, Webflow et Wix, contrairement à WordPress, sont des plateformes non open source. Ils permettent aux utilisateurs de créer intuitivement des sites web pour leurs entreprises via des fonctionnalités de glisser-déposer sans aucune expérience en codage ou en design. Ils travaillent également dur pour protéger la sécurité de leurs utilisateurs.

Il existe de nombreux outils utiles, options, tableaux de bord faciles à intégrer et opportunités d'hébergement disponibles pour les utilisateurs, instaurant leur confiance dans ces plateformes. Les problèmes de sécurité des sites web sont bien sûr une préoccupation majeure pour la majorité des utilisateurs sur ces plateformes.

De nombreux constructeurs de sites web font de leur mieux pour protéger les sites de leurs utilisateurs contre les [menaces des pirates](https://techbullion.com/how-to-secure-your-online-store-from-hackers/). Mais parmi tous les constructeurs de sites web disponibles, je crois que Wix suit le mieux le cadre NIST pour la cybersécurité et est devenu un contributeur majeur aux améliorations dans ce domaine.

Wix protège les utilisateurs sur leurs sites contre la vulnérabilité à ces types d'attaques en ligne avec des outils tels que :

* Mises à jour tierces qui protègent contre les attaques DOM XSS
* Une couche de sockets sécurisée qui protège contre les accès non désirés pour les utilisateurs sur le site
* Hébergement web sécurisé 24h/24 qui protège les utilisateurs contre toute tentative de connexion ou de phishing non désirée.
* Accorder à ses utilisateurs des privilèges d'administrateur, qui restreignent l'accès et le contrôle du site au seul propriétaire original
* Mettre en évidence les mots de passe faibles et suggérer des mots de passe plus difficiles à déchiffrer.

## Façons de se protéger contre les attaques XSS

Déendre votre système et vos utilisateurs contre les attaques XSS nécessite souvent une approche multifacette pour garantir que vos serveurs et applications sont protégés contre divers types d'attaques.

La meilleure façon de se défendre contre les attaques XSS est de bien assainir les entrées utilisateur. Cela signifie s'assurer que toute entrée utilisateur est correctement encodée afin qu'elle ne puisse pas être interprétée comme du code par le navigateur.

De plus, vous pouvez utiliser un pare-feu d'application web (WAF) pour aider à identifier et bloquer les attaques XSS. Il est également bon de garder vos logiciels et applications web à jour, car de nombreuses vulnérabilités XSS peuvent être atténuées en appliquant simplement les derniers correctifs de sécurité.

### Validation des entrées

Cette technique de programmation garantit que seules les données correctement formatées peuvent entrer dans un système logiciel. Les sites web peuvent soit autoriser, soit bloquer certaines valeurs pour s'assurer qu'aucun XSS ne peut pénétrer leurs serveurs.

### Échappement ou encodage des entrées utilisateur

L'encodage et l'échappement modifient les entrées utilisateur pour les rendre plus sûres pour le système. L'encodage remplace les caractères spéciaux par des équivalents plus inoffensifs (par exemple, traduire < en &lt;), tandis que l'échappement ajoute des caractères spéciaux pour se protéger contre les attaques par injection.

### Mise en œuvre d'une politique de sécurité du contenu (CSP)

Les politiques de sécurité du contenu aident les administrateurs à atténuer les attaques XSS en restreignant les ressources qu'une page peut charger à un moment donné. Ces ressources peuvent inclure des scripts et des images qui pourraient potentiellement nuire aux clients et aux serveurs.

## Conclusion

Les problèmes de sécurité des scripts inter-sites basés sur le DOM sont une préoccupation sérieuse pour les utilisateurs des sites web. Mais les plateformes de construction web à code fermé offrent des fonctionnalités comme les privilèges d'administrateur, les meilleures pratiques en matière de mots de passe, les mises à jour tierces, et bien plus encore. Ces fonctionnalités en font une option de construction de sites web plus sécurisée que de nombreuses plateformes à code ouvert.

Vous pouvez également prévenir les attaques XSS en filtrant les entrées dès leur arrivée. Vous pouvez le faire en vous assurant que seules les entrées valides sont acceptées.

Lors de l'encodage des données en sortie, le processus doit être effectué dans les réponses HTTP afin qu'il ne soit pas lu comme du contenu actif. Un codage plus complexe peut être nécessaire, comme l'application de combinaisons d'encodage URL, JavaScript, CSS et HTML, selon le contexte de sortie.

Gardez les en-têtes de réponse sous contrôle afin que les navigateurs aient une interprétation appropriée du contenu.

Enfin, utilisez la politique de sécurité du contenu (CSP) pour minimiser la gravité des attaques XSS.

```
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';">
```

Cette CSP permettra à votre site web de charger des scripts et des styles à partir de la même origine (c'est-à-dire votre propre site web), mais elle bloquera les scripts et les styles provenant de sources externes. Elle permettra également l'utilisation de scripts et de styles en ligne, mais elle bloquera les instructions eval(), qui peuvent être utilisées pour exécuter du code arbitraire.

Bien sûr, ce n'est qu'un exemple simple, et vous pouvez personnaliser votre CSP pour répondre à vos besoins spécifiques. Pour plus d'informations sur la façon d'utiliser les CSP pour se défendre contre les attaques XSS, vous pouvez vous référer à la spécification Content Security Policy Level 2.

_Image de présentation via Unsplash (Florian Olivo)._