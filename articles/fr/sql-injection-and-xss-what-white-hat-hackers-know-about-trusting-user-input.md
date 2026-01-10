---
title: 'Injections SQL et XSS : ce que les hackers white hat savent sur la confiance
  accordée aux entrées utilisateur'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-09-03T12:34:00.000Z'
originalURL: https://freecodecamp.org/news/sql-injection-and-xss-what-white-hat-hackers-know-about-trusting-user-input
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/cover-1.png
tags:
- name: Application Security
  slug: application-security
- name: bug bounty
  slug: bug-bounty
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Security
  slug: security
- name: Web App Security
  slug: web-app-security
seo_title: 'Injections SQL et XSS : ce que les hackers white hat savent sur la confiance
  accordée aux entrées utilisateur'
seo_desc: 'Software developers have a lot on their minds. There are are myriad of
  questions to ask when it comes to creating a website or application: What technologies
  will we use? How will the architecture be set up? What functions do we need? What
  will the U...'
---

Les développeurs de logiciels ont beaucoup de choses en tête. Il y a une myriade de questions à se poser lors de la création d'un site web ou d'une application : *Quelles technologies allons-nous utiliser ? Comment l'architecture sera-t-elle mise en place ? Quelles fonctions avons-nous besoin ? À quoi ressemblera l'interface utilisateur ?*

Surtout dans un marché du logiciel où le lancement de nouvelles applications semble plus être une course à la réputation qu'un processus bien réfléchi, l'une des questions les plus importantes tombe souvent au bas de la colonne "Urgent" : comment notre produit sera-t-il sécurisé ?

Si vous utilisez un framework robuste et open-source pour construire votre produit (et s'il en existe un applicable et disponible, pourquoi ne pas l'utiliser ?), alors certaines préoccupations de sécurité de base, comme les jetons CSRF et le chiffrement des mots de passe, peuvent déjà être gérées pour vous.

Néanmoins, les développeurs rapides seraient bien avisés de se rafraîchir la mémoire sur les menaces et les pièges courants, ne serait-ce que pour éviter certaines erreurs embarrassantes de débutant. Habituellement, le point le plus faible dans la sécurité de votre logiciel, c'est *vous*.

Je me suis récemment intéressé à la sécurité de l'information en général, et à la pratique du piratage éthique en particulier. Un hacker éthique, parfois appelé un hacker "white hat", et parfois simplement un "hacker", est quelqu'un qui recherche les vulnérabilités de sécurité possibles et les signale de manière responsable (et privée) aux propriétaires de projets.

En revanche, un hacker malveillant ou "black hat", également appelé un "cracker", est quelqu'un qui exploite ces vulnérabilités pour son amusement ou son gain personnel.

Les hackers white hat et black hat peuvent utiliser les mêmes outils et ressources, et essaient généralement d'accéder à des endroits où ils ne sont pas censés être. Mais les white hats le font avec permission, et avec l'intention de renforcer les défenses au lieu de les détruire. Les black hats sont les méchants.

En ce qui concerne l'apprentissage de la recherche de vulnérabilités de sécurité, il n'est pas surprenant que j'aie dévoré toutes les informations que je pouvais obtenir. Cet article est une distillation de certains domaines clés qui sont spécifiquement utiles aux développeurs lors de la gestion des entrées utilisateur. Ces leçons ont été collectivement glanées à partir de ces excellentes ressources :

* Les guides du [Projet Open Web Application Security](https://www.owasp.org/index.php/Main_Page)
* La playlist Hacker101 de la [chaîne YouTube de HackerOne](https://www.youtube.com/channel/UCsgzmECky2Q9lQMWzDwMhYw/)
* [Web Hacking 101](https://leanpub.com/web-hacking-101) par Peter Yaworski
* Le [blog de Brute Logic](https://brutelogic.com.br/blog/)
* La chaîne YouTube [Computerphile](https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA)
* Les vidéos mettant en vedette Jason Haddix ([@jhaddix](https://github.com/jhaddix/)) et Tom Hudson ([@tomnomnom](https://github.com/tomnomnom/)) (deux hackers éthiques accomplis avec des méthodologies différentes, mais toutes deux efficaces)

Vous êtes peut-être familier avec le slogan, "sanitize your inputs !" Cependant, comme je l'espère, cet article le démontre, développer une application avec une sécurité robuste n'est pas si simple.

Je suggère une phrase alternative : faites attention à vos entrées. Élaborons en examinant les attaques les plus courantes qui tirent parti des vulnérabilités dans ce domaine : les injections SQL et les scripts inter-sites.

# Attaques par injection SQL

Si vous n'êtes pas encore familier avec les attaques par injection SQL (Structured Query Language), ou SQLi, voici une excellente [vidéo explicative sur SQLi](https://www.youtube.com/watch?v=_jKylhJtPmI). Vous connaissez peut-être déjà cette attaque grâce à [Little Bobby Tables de xkcd](https://xkcd.com/327/).

Essentiellement, des acteurs malveillants peuvent être en mesure d'envoyer des commandes SQL qui affectent votre application via une entrée sur votre site, comme une boîte de recherche qui extrait des résultats de votre base de données. Les sites codés en PHP peuvent être particulièrement sensibles à ces attaques, et une attaque SQL réussie peut être dévastatrice pour un logiciel qui dépend d'une base de données (comme dans, votre table Utilisateurs est maintenant un pot de pétunias).

![Un moniteur avec une commande SQL Select qui obtient toutes vos bases](https://www.freecodecamp.org/news/content/images/2020/11/sqli.png)
_Vous n'avez aucune chance de survivre, faites votre temps._

Vous pouvez tester votre propre site pour voir si vous êtes vulnérable à ce type d'attaque. (Veuillez ne tester que les sites que vous possédez, car exécuter des injections SQL là où vous n'avez pas la permission de le faire est, possiblement, illégal dans votre localité ; et définitivement, universellement, pas très drôle.) Les charges utiles suivantes peuvent être utilisées pour tester les entrées :

* `' OR 1='1` évalue à un vrai constant, et lorsqu'il est réussi, retourne toutes les lignes de la table.
* `' AND 0='1` évalue à un faux constant, et lorsqu'il est réussi, ne retourne aucune ligne.

[Cette vidéo démontre les tests ci-dessus](https://www.youtube.com/watch?v=ciNHn38EyRc), et fait un excellent travail pour montrer à quel point une attaque par injection SQL peut être impactante.

Heureusement, il existe des moyens de mitiger les attaques par injection SQL, et ils se résument tous à un concept de base : ne faites pas confiance aux entrées utilisateur.

# Mitigation des injections SQL

Pour mitiger efficacement les injections SQL, les développeurs doivent empêcher les utilisateurs de pouvoir soumettre avec succès des commandes SQL brutes à n'importe quelle partie du site.

Certains frameworks feront la majeure partie du travail pour vous. Par exemple, Django implémente le concept de [Mapping Objet-Relationnel](https://en.wikipedia.org/wiki/Object-relational_mapping), ou ORM, avec son utilisation de [QuerySets](https://docs.djangoproject.com/en/2.2/topics/db/queries/). Nous pouvons les considérer comme des fonctions d'enveloppement qui aident votre application à interroger la base de données en utilisant des méthodes pré-définies qui évitent l'utilisation de SQL brut.

Pouvoir utiliser un framework, cependant, n'est jamais une garantie. Lorsque vous traitez directement avec une base de données, il existe d'autres méthodes que nous pouvons utiliser pour abstraire en toute sécurité nos requêtes SQL des entrées utilisateur, bien qu'elles varient en efficacité. Ce sont, par ordre de préférence, du plus au moins préféré, et avec des liens vers des exemples pertinents :

1. Les instructions préparées avec liaison de variables (ou [requêtes paramétrées](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)),
2. Les [procédures stockées](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-2-stored-procedures) ; et
3. La [liste blanche](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-3-whitelist-input-validation) ou l'[échappement](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-4-escaping-all-user-supplied-input) des entrées utilisateur.

Si vous souhaitez implémenter les techniques ci-dessus, les fiches de référence liées sont un excellent point de départ pour creuser plus profond. Il suffit de dire que l'utilisation de ces techniques pour obtenir des données au lieu d'utiliser des requêtes SQL brutes aide à minimiser les chances que SQL soit traité par une partie de votre application qui prend des entrées des utilisateurs, mitigant ainsi les attaques par injection SQL.

La bataille, cependant, n'est que moitié gagnée...

# Attaques par scripts inter-sites (XSS)

Si vous êtes un codeur malveillant, JavaScript est pratiquement votre meilleur ami. Les bonnes commandes feront tout ce qu'un utilisateur légitime pourrait faire (et même certaines choses qu'ils ne sont pas censés pouvoir faire) sur une page web, parfois sans aucune interaction de la part d'un utilisateur réel.

Les attaques par [scripts inter-sites](https://en.wikipedia.org/wiki/Cross-site_scripting), ou XSS, se produisent lorsque du code JavaScript est injecté dans une page web et modifie le comportement de cette page. Ses effets peuvent aller de simples occurrences de farces à des contournements d'authentification plus graves ou au vol de données d'identification. [Ce rapport d'incident d'Apache en 2010](https://blogs.apache.org/infra/entry/apache_org_04_09_2010) est un bon exemple de la manière dont XSS peut être enchaîné dans une attaque plus large pour prendre le contrôle de comptes et de machines.

![Une fête de danse HTML avec un peu de JS qui s'incruste](https://www.freecodecamp.org/news/content/images/2020/11/xss-1.png)
_Le concours annuel de danse DOM reçoit un invité inattendu_

XSS peut se produire sur le serveur ou sur le côté client, et se présente généralement sous trois formes : basé sur le DOM ([Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)), stocké et réfléchi. Les différences résident dans l'endroit où la charge utile de l'attaque est injectée dans l'application.

## XSS basé sur le DOM

Le [XSS basé sur le DOM](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting) se produit lorsque une charge utile JavaScript affecte la structure, le comportement ou le contenu de la page web que l'utilisateur a chargée dans son navigateur. Ces attaques sont le plus souvent exécutées via des URL modifiées, comme dans le phishing.

Pour voir à quel point il serait facile pour du JavaScript injecté de manipuler une page, nous pouvons créer un exemple fonctionnel avec une page web HTML. Essayez de créer un fichier sur votre système local appelé `xss-test.html` (ou ce que vous voulez) avec le code HTML et JavaScript suivant :

```html
<html>
    <head>
        <title>Mon exemple XSS</title>
    </head>
    <body>
        <h1 id="greeting">Bonjour à tous !</h1>
            <script>
                var name = new URLSearchParams(document.location.search).get('name');
                if (name !== 'null') {
                    document.getElementById('greeting').innerHTML = 'Bonjour ' + name + ' !';
                }
            </script>
        </h1>
</html>
```

Cette page web affichera le titre « Bonjour à tous ! » sauf si elle reçoit un [paramètre d'URL d'une chaîne de requête](https://en.wikipedia.org/wiki/Query_string) avec une valeur pour `name`. Pour voir le script fonctionner, ouvrez la page dans un navigateur avec un paramètre d'URL ajouté, comme suit :

`file:///path/to/file/xss-test.html?name=Victoria`

Amusant, n'est-ce pas ? Notre page non sécurisée (au sens de la sécurité, pas de l'émotion) prend la valeur du paramètre d'URL pour `name` et l'affiche dans le DOM. La page s'attend à ce que la valeur soit une chaîne amicale, mais que se passe-t-il si nous la changeons en autre chose ? Puisque la page nous appartient et n'existe que sur notre système local, nous pouvons la tester autant que nous le souhaitons. Que se passe-t-il si nous changeons le paramètre `name` en, par exemple, `<img+src+onerror=alert("pwned")>` ?

![Une capture d'écran de l'exemple de page XSS](https://www.freecodecamp.org/news/content/images/2020/11/pwned.png)

Ce n'est qu'un exemple, largement basé sur un exemple de [l'article de Brute](https://brutelogic.com.br/blog/dom-based-xss-the-3-sinks/), qui démontre comment une attaque XSS pourrait être exécutée. Les alertes pop-up amusantes peuvent être divertissantes, mais JavaScript peut faire beaucoup de mal, y compris aider les attaquants malveillants à voler des mots de passe et des informations personnelles.

## XSS stocké et réfléchi

Le [XSS stocké](https://en.wikipedia.org/wiki/Cross-site_scripting#Persistent_(or_stored)) se produit lorsque la charge utile de l'attaque est stockée sur le serveur, comme dans une base de données. L'attaque affecte une victime chaque fois que ces données stockées sont récupérées et rendues dans le navigateur. Par exemple, au lieu d'utiliser une chaîne de requête d'URL, un attaquant pourrait mettre à jour sa page de profil sur un site social pour inclure un script caché dans, par exemple, sa section "À propos de moi". Le script, stocké de manière incorrecte sur le serveur du site, s'exécuterait avec succès à un moment ultérieur lorsque qu'un autre utilisateur consulterait le profil de l'attaquant.

L'un des exemples les plus célèbres de cela est le [ver Samy](https://en.wikipedia.org/wiki/Samy_(computer_worm)) qui a presque pris le contrôle de MySpace en 2005. Il s'est propagé en envoyant des requêtes HTTP qui le répliquaient sur la page de profil d'une victime chaque fois qu'un profil infecté était consulté. En seulement 20 heures, il s'était répandu à plus d'un million d'utilisateurs.

Le [XSS réfléchi](https://en.wikipedia.org/wiki/Cross-site_scripting#Non-persistent_(reflected)) se produit de manière similaire lorsque la charge utile injectée voyage vers le serveur, cependant, le code malveillant ne se retrouve pas stocké dans une base de données. Il est plutôt immédiatement renvoyé au navigateur par l'application web.

Une attaque comme celle-ci pourrait être exécutée en incitant la victime à cliquer sur un lien malveillant qui envoie une requête au serveur du site web vulnérable. Le serveur enverrait alors une réponse à l'attaquant ainsi qu'à la victime, ce qui pourrait permettre à l'attaquant d'obtenir des mots de passe, ou de perpétrer des actions qui semblent provenir de la victime.

# Mitigation des attaques XSS

Dans tous ces cas, les attaques XSS peuvent être mitigées avec deux stratégies clés : la validation des champs de formulaire et l'évitement de l'injection directe des entrées utilisateur sur la page web.

## Validation des champs de formulaire

Les frameworks peuvent à nouveau nous aider à nous assurer que les formulaires soumis par les utilisateurs sont conformes. Un exemple est les classes `Field` intégrées de [Django](https://docs.djangoproject.com/en/2.2/ref/forms/fields/#built-in-field-classes), qui fournissent des champs qui valident certains types couramment utilisés et spécifient également des valeurs par défaut sensées. Le `EmailField` de Django, par exemple, utilise un ensemble de règles pour déterminer si l'entrée fournie est un email valide. Si la chaîne soumise contient des caractères qui ne sont pas typiquement présents dans les adresses email, ou si elle n'imite pas le format courant d'une adresse email, alors Django ne considérera pas le champ valide et le formulaire ne sera pas soumis.

Si s'appuyer sur un framework n'est pas une option, nous pouvons implémenter notre propre validation d'entrée. Cela peut être accompli avec quelques techniques différentes, y compris la [conversion de type](https://en.wikipedia.org/wiki/Type_conversion), par exemple, en s'assurant qu'un nombre est de type `int()` ; en vérifiant les valeurs minimales et maximales pour les nombres et les longueurs pour les chaînes ; en utilisant un tableau pré-défini de choix qui évite les entrées arbitraires, par exemple, les mois de l'année ; et en vérifiant les données par rapport à des [expressions régulières](https://en.wikipedia.org/wiki/Regular_expression) strictes.

Heureusement, nous n'avons pas besoin de partir de zéro. Des ressources open source sont disponibles pour aider, comme le [Dépôt de Regex de Validation OWASP](https://www.owasp.org/index.php/OWASP_Validation_Regex_Repository), qui fournit des motifs à faire correspondre pour certaines formes courantes de données. De nombreux langages de programmation offrent des bibliothèques de validation spécifiques à leur syntaxe, et nous pouvons trouver [beaucoup de celles-ci sur GitHub](https://github.com/search?q=validation+library). De plus, la [Fiche de Référence pour l'Évasion des Filtres XSS](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet) a quelques suggestions pour les charges utiles de test que nous pouvons utiliser pour tester nos applications existantes.

Bien que cela puisse sembler fastidieux, une validation d'entrée correctement implémentée peut protéger notre application contre les vulnérabilités XSS.

## Éviter l'injection directe

Les éléments d'une application qui renvoient directement les entrées utilisateur au navigateur peuvent ne pas être évidents lors d'une inspection superficielle. Nous pouvons déterminer les zones de notre application qui peuvent être à risque en explorant quelques questions :

* Comment les données circulent-elles dans notre application ?
* Que s'attend à ce qu'il se passe un utilisateur lorsqu'il interagit avec cette entrée ?
* Où sur notre page les données apparaissent-elles ? Deviennent-elles intégrées dans une chaîne ou un attribut ?

Voici quelques charges utiles d'exemple que nous pouvons utiliser pour tester les entrées sur notre site (encore une fois, seulement notre propre site !) grâce à [Hacker101](https://www.hacker101.com/). L'exécution réussie de l'un de ces exemples peut indiquer une possible vulnérabilité XSS due à une injection directe.

* `"><h1>test</h1>`
* `'+alert(1)+'`
* `"onmouserover="alert(1)`
* `http://"onmouseover="alert(1)`

En règle générale, si vous pouvez concevoir autour de l'injection directe d'entrée, faites-le. Alternativement, assurez-vous de bien comprendre l'effet des méthodes que vous choisissez ; par exemple, utiliser `innerText` au lieu de `innerHTML` en JavaScript garantira que le contenu sera défini comme du texte brut au lieu de HTML (potentiellement vulnérable).

# Faites attention à vos entrées

Les développeurs de logiciels sont à un désavantage marqué lorsqu'il s'agit de rivaliser avec les hackers black hat, ou malveillants. Pour tout le travail que nous faisons pour sécuriser chaque entrée qui pourrait potentiellement compromettre notre application, un attaquant doit seulement trouver celle que nous avons manquée. C'est comme installer des verrous sur toutes les portes, mais laisser une fenêtre ouverte !

En apprenant à penser comme un attaquant, cependant, nous pouvons mieux préparer notre logiciel à résister aux mauvais acteurs. Excitant que cela puisse être de livrer des fonctionnalités aussi rapidement que possible, nous éviterons d'accumuler beaucoup de dettes de sécurité si nous prenons le temps au préalable de réfléchir au flux de notre application, de suivre les données et de faire attention à nos entrées.