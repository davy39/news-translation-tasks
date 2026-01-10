---
title: Le système de noms de domaine (DNS) est l'épine dorsale d'Internet. Voici comment
  tout cela fonctionne.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-26T19:29:33.000Z'
originalURL: https://freecodecamp.org/news/the-domain-name-system-dns-is-the-backbone-of-the-internet-heres-how-it-all-works-5706d0afa0fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_aojoKJJSZRCADzj9N06uA.jpeg
tags:
- name: politics
  slug: politics
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le système de noms de domaine (DNS) est l'épine dorsale d'Internet. Voici
  comment tout cela fonctionne.
seo_desc: 'By Nikolas O''Donnell

  The Domain Name System (DNS) is often referred to as the backbone of the internet.
  It’s run by many engineers and their organizations, it ultimately shapes the future
  of the internet.

  I recently attended ICANN58 in Copenhagen. It...'
---

Par Nikolas O'Donnell

Le système de noms de domaine (DNS) est souvent appelé l'épine dorsale d'Internet. Il est géré par de nombreux ingénieurs et leurs organisations, et il façonne finalement l'avenir d'Internet.

J'ai récemment assisté à l'ICANN58 à Copenhague. Ce fut une semaine incroyable de tables rondes sur l'avenir d'Internet. Cela comprenait :

* des séminaires sur le développement de politiques pour le DNS
* des ateliers sur le fonctionnement de l'architecture d'Internet
* où se trouvent les plus grandes vulnérabilités d'Internet

Ce fut très amusant, et j'en ai tiré une énorme valeur.

Pour revenir un peu en arrière, je suis relativement nouveau dans le monde des domaines et les rouages de l'architecture Internet. Depuis que j'ai rejoint cet espace en tant que développeur avec [iwantmyname](https://iwantmyname.com), j'ai dû apprendre énormément. Il y a un labyrinthe massif qui se cache sous la surface du navigateur. J'ai donc écrit ce guide pour vous accompagner à travers certaines des infrastructures qui se cachent derrière ces noms de domaine et ces nombres que nous utilisons tous quotidiennement.

### Comment fonctionne Internet ?

> « C'est une question très courante en entretien : que se passe-t-il lorsque vous allez sur Google.com, entrez une requête et appuyez sur Entrée ? » — [Quincy Larson](https://www.freecodecamp.org/news/the-domain-name-system-dns-is-the-backbone-of-the-internet-heres-how-it-all-works-5706d0afa0fa/undefined)

Vous ouvrez donc votre navigateur et allez sur [freecodecamp.com](http://freecodecamp.com), et ce site génial se charge en un clin d'œil devant vous. Vous savez déjà que ce site est rendu à partir d'une série de fichiers compilés qui se trouvent sur un serveur quelque part. Mais comment votre navigateur trouve-t-il son chemin vers ces fichiers dans l'Internet en expansion infinie ? Vous pourriez commencer à vous demander...

**Qu'est-ce qui vient de se passer ?**

La toute première fois que vous êtes allé sur freecodecamp.com, votre navigateur ne savait pas quelle était l'adresse IP de freecodecamp.com, donc il ne pouvait pas se connecter et récupérer ces fichiers. Ni d'ailleurs ne savait-il où se trouvaient les serveurs réels sur lesquels ces fichiers sont hébergés. Et par conséquent, il n'avait aucune idée d'où tirer ces fichiers pour commencer à rendre la page.

Voici donc ce qui se passe : (place aux graphiques !)

> [DNS Chat](https://imgur.com/a/xj0fP)

### **D'accord, laissez-moi développer un peu**

1. Un utilisateur demande à son navigateur de visiter freecodecamp.com
2. Le navigateur interroge un résolveur DNS (généralement leur FAI) « où est freecodecamp.com ? »
3. Le résolveur DNS interroge les serveurs racine (qui ont une grande liste importante qui conserve ces informations) « où est .COM ? » Répond avec Verisign.
4. Le résolveur DNS interroge ensuite Verisign — « où est freecodecamp.com ? » Verisign répond avec les serveurs de noms ns1.cloudflare.com et l'adresse IP 192.168.178.1
5. Les serveurs d'hébergement sont interrogés avec l'adresse IP. « Donnez-moi les fichiers pour l'adresse IP 192.168.178.1 (s'il vous plaît) »
6. Les fichiers du site web sont livrés et rendus sur la page afin que l'utilisateur puisse apprendre à coder... ou quoi que ce soit qu'il faisait.

J'ai récupéré cette capture d'écran de [Verisign](https://www.verisign.com/en_US/website-presence/online/how-dns-works/index.xhtml), de loin le plus grand registre au monde gérant .com .net .cc .tv et .name. Elle vous montre le processus de manière agréable comment le protocole fonctionne à travers les requêtes et réponses séquentielles à travers la structure DNS.

Ne vous inquiétez pas trop d'essayer de lire tout le texte, mais regardez simplement les échanges et le flux d'informations pour réitérer ce que nous avons discuté ci-dessus (c'est en boucle donc cela redémarrera).

> [DNS Chat](https://imgur.com/a/MnXeU)

### Qui le fait fonctionner ?

En bref, l'IANA, et en long, l'ICANN (je vais expliquer ces organisations dans un instant et tout cela aura plus de sens, je vous le promets !)

La raison d'expliquer comment cela fonctionne était de découvrir qui le fait fonctionner — la vraie question et le but de cet article. Il est facile de penser que les choses fonctionnent simplement. Mais bien sûr, ce n'est pas un accident, la raison pour laquelle Internet fonctionne est due aux protocoles et politiques qui ont été créés et ont obtenu suffisamment de consensus pour devenir des normes universelles, mais qui est d'accord avec ceux-ci et comment ?

En bref, et en ce qui concerne spécifiquement la manière dont les noms de domaine et les adresses IP sont mappés, cette fonction relève de la compétence de l'IANA (Internet Assigned Numbers Authority). Ils ont le mandat de s'assurer que les procédures techniques correctes sont en place pour avoir un système de noms de domaine sûr et stable. Ce qui nous amène à l'ICANN (Internet Corporation for Assigned Names and Numbers). Il n'y a pas de discussion sur l'IANA sans l'ICANN :

> _En plus de fournir les opérations techniques des ressources DNS vitales, l'ICANN définit également les politiques pour le fonctionnement des « noms et nombres » de l'Internet. Le travail avance dans un style que nous décrivons comme le « modèle multipartite, basé sur le consensus et piloté par les parties prenantes » — ICANN.COM_

En septembre 2015, la fonction IANA, qui est gérée par l'ICANN depuis 1998, a définitivement transféré de la tutelle d'un contrat avec le Département du Commerce des États-Unis au contrôle autonome de l'ICANN \o/ L'ICANN dispose d'un conseil d'administration et, en tant qu'organisme, est divisé en différents groupes de membres, explorons le modèle multipartite :

> _« L'approche inclusive de l'ICANN traite le secteur public, le secteur privé et les experts techniques comme des pairs. Dans la communauté ICANN, vous trouverez des registres, des bureaux d'enregistrement, des fournisseurs de services Internet (FAI), des défenseurs de la propriété intellectuelle, des intérêts commerciaux et économiques, des intérêts non commerciaux et à but non lucratif, une représentation de plus de 100 gouvernements, et un éventail mondial d'utilisateurs individuels d'Internet. Tous les points de vue sont pris en considération pour leurs propres mérites. La conviction fondamentale de l'ICANN est que tous les utilisateurs d'Internet méritent d'avoir leur mot à dire sur la manière dont il est géré. » — ICANN.COM_

![Image](https://cdn-media-1.freecodecamp.org/images/1*bmNP6V25oKJkvCuQwEsshw.png)
_Modèle multipartite de l'ICANN — crédit image ICANN.com_

Bien qu'il soit juste de dire que tous ces groupes sont « représentés », je soutiendrais que tous ne sont pas représentés de manière égale. Il est naturel de s'attendre à ce que ceux qui ont plus d'enjeux financiers et d'argent à brûler tentent de tirer la conversation dans une certaine direction. Par exemple, les télécoms comme AT&T, Comcast, Charter, Verizon, Vodafone, T-Mobile, Orange.

Ils nous tireront probablement dans une direction rétrograde, où ils pourront regrouper les sites web comme ils l'ont fait avec les chaînes de télévision par câble, et les vendre aux utilisateurs finaux, facturer le trafic sur les câbles qu'ils contrôlent, et généralement triple-dip sur un Internet plus fermé afin qu'ils puissent réaliser encore plus de profits.

Certains gouvernements tenteront également d'influencer dans une direction conforme à leur propre intérêt national, tandis que d'autres essaieront d'être des citoyens plus globaux. Les défenseurs de la propriété intellectuelle (organisations généralement composées d'avocats en propriété intellectuelle) veulent que les choses soient plus axées sur la propriété intellectuelle et la sécurité des marques, afin qu'ils puissent protéger les droits lucratifs de leurs clients bien payés.

Les fournisseurs de services dans le secteur commercial comme Google et Facebook sont visibles dans le tableau, et tendent à plaider — en partie au moins — pour la confidentialité de leurs utilisateurs, tout en maintenant leur propre domination du web.

Les registres comme Verisign ont un intérêt à concevoir des résultats politiques favorables auxquels ils sont tenus de se conformer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bE_Pg084IxjShX8qsgk-Mw.jpeg)
_iCANN est comme ça, mais bien moins adorable..._

Intéressamment, selon mon expérience, ce sont les bureaux d'enregistrement — où vous pouvez enregistrer des noms de domaine (comme [iwantmyname](https://iwantmyname.com)) — qui fournissent une voix de raison dans la mêlée. Ils doivent équilibrer leurs obligations envers l'ICANN et les registres contre celles de leurs clients. Et en conséquence, ils doivent souvent résister à divers membres ou groupes d'intérêt, ou parfois même au conseil d'administration de l'ICANN lui-même.

### Parlons des utilisateurs finaux

Hé ! C'est nous !

Il y a un manque significatif d'engagement des utilisateurs finaux dans ce processus. Eh bien, nous serions tous mieux lotis si les utilisateurs finaux d'Internet commençaient à prêter plus attention.

Rappelez-vous qu'il y a environ 3,7 milliards d'utilisateurs d'Internet, mais qu'il n'y a que quelques personnes qui possèdent des parts dans les télécoms, les registres ou les plateformes web. La communauté freeCodeCamp à elle seule compte plus d'un million d'utilisateurs, et ensemble nous partageons tant de choses qui sont en jeu.

Cela dit, le nombre de personnes actuellement engagées dans cette discussion est très faible — peut-être seulement quelques milliers de personnes. Pour être honnête, je pense qu'il y a un besoin croissant pour que plus de développeurs comme nous prennent une voix plus active dans la conversation.

C'est, après tout, notre gagne-pain. C'est là que nous avons tendance à passer notre temps. C'est l'espace qui consomme une grande partie de notre concentration, de notre énergie et de notre passion. Et en plus d'être des utilisateurs très avertis et intensifs d'Internet, nous avons également des perspectives uniques sur nos propres audiences. Nous pouvons parler avec une voix empathique qui résonne avec une base d'utilisateurs finaux encore plus large.

### Que pouvez-vous faire ?

Vous pouvez prendre place à la table (ou sur le sol). Il y a plusieurs façons de vous impliquer, selon le degré de formalité que vous souhaitez donner à votre implication. Vous pouvez rejoindre [At-Large](https://atlarge.icann.org).

![Image](https://cdn-media-1.freecodecamp.org/images/1*4eN2KqJF1BSj9I_0aKEuPA.png)
_Image par [At-Large](https://atlarge.icann.org/news/announcement-12-2014-08-07-en" rel="noopener" target="_blank" title=")_

[At-Large](https://atlarge.icann.org) fait partie du contingent des utilisateurs finaux du modèle multipartite de l'ICANN. Il est divisé en groupes de sensibilisation régionaux At-Large (RALOs). Voici la liste complète : NARALO (Amérique du Nord), EURALO (Europe), APRALO (Asie-Pacifique), LACRALO (Amérique latine et îles des Caraïbes) et AFRALO (Nations africaines).

Ces différents RALOs transmettent leurs contributions au Comité consultatif At-Large (ALAC... les acronymes ne sont-ils pas amusants !) qui, à son tour, rend compte à l'ICANN.

Au sein de ces organes représentatifs des utilisateurs finaux, il existe des organisations plus petites auxquelles vous pouvez adhérer au niveau universitaire ou municipal.

Une autre façon de vous impliquer est de devenir membre non affilié, c'est-à-dire en dehors d'une structure At-Large, et directement avec votre groupe régional At-Large. (Notez que actuellement seuls les RALOs d'Amérique du Nord, d'Europe et d'Asie-Pacifique permettent de tels membres — [voici où vous pouvez en savoir plus et postuler](https://atlarge.icann.org/get-involved/individual-member).)

Il y a encore une autre façon, et c'est en postulant en tant que collectif pour devenir une [ALS](https://atlarge.icann.org/alses). Cela nécessite quelques efforts de votre part. Vous devriez organiser et diriger les personnes qui rejoignent votre groupe. Mais le gain est une place à la table et une [voix pour tous ceux que votre ALS représente](https://atlarge.icann.org/get-involved/about-als).

Sur une note secondaire, j'aimerais avoir votre avis sur le fait de savoir si la communauté freeCodeCamp elle-même devrait envisager de postuler pour devenir une structure At-Large. Cela donnerait à tous ses membres un chemin vers le groupe des utilisateurs finaux de l'ICANN.

En dehors de la structure At-Large, il y a encore une autre façon de participer. Lorsque l'ICANN ouvre des sujets à commentaires publics, vous pouvez donner votre avis sur ceux-ci. [Voici où les trouver](https://www.icann.org/public-comments).

Vous pouvez également assister à une réunion de l'ICANN comme je l'ai fait. L'ICANN se réunit trois fois par an — chaque fois dans une partie différente du monde. J'ai assisté à l'ICANN58, qui s'est tenue à Copenhague. La prochaine est [l'ICANN59 à Johannesburg](https://meetings.icann.org/en/johannesburg59).

C'est une expérience très enrichissante que d'assister à l'un de ces événements d'une semaine. Ils sont gratuits et ouverts au public. Vous devez simplement vous inscrire et postuler. Ils [offrent également des bourses](https://www.icann.org/fellowshipprogram) pour vous aider à assister si vous avez besoin de soutien pour le faire.

Il existe de nombreuses façons d'exprimer vos opinions et d'aider à façonner l'avenir de notre Internet libre et ouvert.

> « Tous les utilisateurs d'Internet méritent d'avoir leur mot à dire sur la manière dont il est géré. »

> — ICANN

**Je vous invite donc à vous engager et à prendre place à la table.**

> $USER Nous avons réussi \o/ c'était beaucoup à assimiler et à traiter

> Réponse : Vous, les humains, avec votre petit CPU, LOL :)