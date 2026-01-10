---
title: Vulnérabilités en cybersécurité – Comment les attaquants peuvent obtenir vos
  données
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-14T18:47:55.000Z'
originalURL: https://freecodecamp.org/news/cybersecurity-vulnerabilities
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-38275.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Vulnérabilités en cybersécurité – Comment les attaquants peuvent obtenir
  vos données
seo_desc: "In order to understand potential threats hanging over your organization,\
  \ you'll need to understand two things: what dangerous stuff is out there on the\
  \ internet right now, and what impact it could have were it to actually hit you.\
  \ \nOnce you have that..."
---

Pour comprendre les menaces potentielles qui pèsent sur votre organisation, vous devez comprendre deux choses : quels sont les dangers actuels sur Internet et quel impact ils pourraient avoir s'ils vous touchaient réellement.

Une fois que vous aurez ces informations, vous serez en mesure d'évaluer intelligemment vos risques.

Cela peut, à son tour, vous aider à décider à la fois _combien_ investir dans la sécurité et _où_ votre investissement sera le plus utile. Ces chiffres sont importants, car vous pourriez être tenté de dire simplement : « Donnez-moi juste une liste de tous les outils d'atténuation de sécurité disponibles et j'en achèterai un de chaque. »

Mais compte tenu du nombre d'outils existants et de ce qu'il vous en coûterait pour construire l'infrastructure et les connaissances institutionnelles nécessaires pour les déployer tous, acheter « un de chaque » n'est pas une option réaliste. Au lieu de cela, vous allez devoir choisir et faire le meilleur usage des ressources limitées dont vous disposez.

Presque tous ceux qui s'attaquent aux ressources numériques d'autrui sont motivés par l'un des deux objectifs suivants : prendre le contrôle non autorisé de vos serveurs et de votre équipement informatique, ou empêcher vos serveurs de fonctionner comme prévu.

Les attaquants peuvent être des voleurs cherchant à dérober votre argent, des concurrents ou même des États-nations cherchant à voler votre propriété intellectuelle ou à vous empêcher de fonctionner comme vous le souhaitez, ou des activistes essayant de faire passer un message en cassant des choses. Quels qu'ils soient, c'est soit le contrôle, soit la destruction qu'ils recherchent.

Cet article est tiré de mon [cours d'introduction à la cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://www.youtube.com/watch?v=fhkL2NM8rHc&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO]

## Différents vecteurs d'attaque en cybersécurité

En termes très généraux, une attaque peut se produire via l'un des quatre vecteurs suivants.

### Accès physique

Les attaques physiques, en personne, peuvent impliquer le vol ou la duplication non autorisée de disques de données non chiffrés. Cela peut arriver parce que quelqu'un a accidentellement laissé un ordinateur portable ou un téléphone dans un café ou parce que quelqu'un a oublié de verrouiller la porte de votre salle de serveurs.

Je suppose que ces attaques de proximité deviennent de plus en plus rares. Après tout, si je devais choisir entre tenter une infiltration physique compliquée, coûteuse et hautement risquée des bureaux de ma cible, ou m'asseoir sur le canapé de mon salon et lancer un script de malware téléchargé quelque part, je sais quel serait mon choix.

Et c'est sans compter le fait que de plus en plus d'appareils mobiles utilisés en entreprise sont chiffrés, ce qui rend l'exploitation de leur contenu très difficile, même s'ils sont volés.

Mais il existe un autre type d'attaque physique beaucoup plus difficile à prévenir : les vulnérabilités de type backdoor intégrées à votre matériel ou à vos systèmes d'exploitation. Une backdoor (porte dérobée) est une faiblesse non documentée dans le profil de sécurité d'un système.

Des backdoors peuvent avoir été ajoutées à l'insu des fournisseurs avant l'expédition du produit dans le cadre d'une opération criminelle. Ou elles peuvent avoir été intentionnellement incorporées dans un système pour permettre un accès secret à des organismes chargés de l'application de la loi.

Le terme peut également être utilisé pour décrire des défauts de conception accidentels que les pirates peuvent exploiter plus tard. Mais quelle que soit leur origine, les backdoors peuvent être très difficiles à identifier et à refermer.

**Que devriez-vous faire ?**

* Chiffrer les disques de tous les appareils mobiles
* Suivre des fils d'actualité fiables sur la sécurité en ligne
* Verrouiller vos portes (dites-moi que vous n'y aviez pas déjà pensé !)

### Connectivité réseau

Le _deuxième_ vecteur d'attaque est Internet lui-même. Ce qui, quand on considère que presque tous les appareils que vous utilisez ont besoin de connectivité, peut être une source courante de problèmes.

Ne pas configurer correctement votre pare-feu et vos paramètres système – et ne pas intégrer de services d'atténuation des menaces dans le cloud comme Cloudflare – peut vous rendre inutilement vulnérable aux attaques par déni de service (DoS). C'est là que votre infrastructure est inondée de suffisamment de requêtes factices simultanées pour rendre votre service indisponible.

De même, les connexions réseau non chiffrées risquent de voir leurs communications privées interceptées et volées. Pire encore, ces connexions peuvent être victimes d'attaques de l'homme du milieu (man-in-the-middle). Dans ces attaques, des tiers peuvent non seulement lire les données privées circulant entre un site Web et son client distant, mais ils peuvent même usurper l'identité des participants légitimes et insérer leur propre contenu à la place de ce qui était prévu.

Imaginez le plaisir qu'un « homme du milieu » pourrait avoir avec des clients se connectant à leurs comptes bancaires en ligne.

Enfin, alors qu'il y a des décennies, la plupart des virus étaient transmis par des disquettes physiques, il est désormais beaucoup plus efficace de distribuer des malwares en ligne, et en particulier sous forme de pièces jointes à des e-mails.

**Que devriez-vous faire ?**

* Assurez-vous que toutes les connexions réseau sont chiffrées
* Apprenez-en plus sur la [sécurité réseau](https://www.freecodecamp.org/news/free-computer-networking-course/)

### Vulnérabilités de l'OS

D'une certaine manière, le _troisième_ vecteur par lequel les attaques peuvent arriver est votre système d'exploitation (OS). Quand je dis cela, je ne veux pas dire que votre noyau Linux va soudainement se réveiller et contacter des gangs de plateformes malveillantes partageant les mêmes idées pour que, je ne sais pas, ils vendent vos données sur des marchés aux puces virtuels le dimanche matin.

C'est peu probable. Ce que je veux dire, c'est que des faiblesses de configuration au sein de votre système d'exploitation peuvent être découvertes et exploitées par des pirates.

Les paquets logiciels non corrigés (unpatched) sont de loin la vulnérabilité la plus dangereuse et la plus courante. Laissez-moi illustrer cela avec une vieille histoire. Vous vous souvenez peut-être comment le service de bureau de crédit Equifax a subi une violation de sécurité en mai 2017. Des données personnelles et financières privées concernant plus de 160 millions de personnes ont été exposées lors de cette violation.

Qu'est-ce qui a mal tourné ? Les pirates ont exploité un bug dans le Framework open source Apache Struts. Apache avait publié un correctif pour le bug en mars 2017. Le problème est que les administrateurs d'Equifax n'ont jamais pris le temps d'installer le correctif gratuit. Et le reste appartient à l'histoire.

En plus d'exécuter des logiciels anciens et buggés, de mauvaises configurations peuvent également vous causer des ennuis. L'attribution de permissions trop larges aux fichiers d'administration système et aux fichiers binaires pourrait permettre des opérations non autorisées. Et, plus généralement, les exploits d'escalade de privilèges peuvent utiliser des failles de code ou de conception pour accéder à des ressources censées être restreintes.

**Que devriez-vous faire ?**

* Corrigez (patchez) votre OS et vos logiciels
* Auditez périodiquement vos journaux système

### Erreur humaine

Le quatrième et dernier vecteur de mon modèle est ce qu'on appelle le « bio-logiciel » (bio-ware) assis devant les claviers de votre bureau. En d'autres termes, les « êtres humains ».

En tant qu'espèce, nous sommes assez doués pour identifier visuellement les méchants. Après tout, ils portent généralement des chapeaux noirs et des imperméables au col relevé, n'est-ce pas ? Mais lorsqu'il s'agit de menaces qui se cachent derrière des interactions sociales ordinaires, nous échouons généralement tôt et souvent.

Les attaques de phishing (hameçonnage), par exemple, peuvent prendre la forme d'e-mails contenant des liens conçus pour _sembler_ mener au site Web de votre banque ou à un service gouvernemental officiel. Mais ils vous redirigeront en réalité vers un site pirate qui enregistrera puis réutilisera les identifiants d'authentification légitimes que vous saisirez innocemment.

De même, l'usurpation d'e-mail (email spoofing) consiste à falsifier l'adresse de l'expéditeur réel d'un message électronique pour faire croire qu'il provient d'une source familière ou de confiance.

Les techniques d'ingénierie sociale (social engineering) peuvent inclure des appels téléphoniques prétendant provenir du département informatique de votre organisation. Ils pourraient vous demander d'épeler votre mot de passe afin de corriger rapidement un problème dans le système d'arrière-plan.

Naturellement, aucun véritable administrateur n'aurait besoin de votre mot de passe ni ne vous le demanderait. Mais tout aussi naturellement, il faut de la vigilance et de l'assurance pour s'opposer lors d'une conversation directe inattendue avec un véritable être humain.

Beaucoup — peut-être la plupart — des attaques de ransomware (rançongiciels) les plus dévastatrices de ces dernières années ont commencé par un simple ensemble d'identifiants volés. Une fois qu'un gang de ransomware entre en possession d'identifiants valides, il se connecte à vos systèmes et passe tout le temps nécessaire — parfois plusieurs mois — à se déplacer dans votre réseau privé et à comprendre le fonctionnement de votre organisation.

Lorsqu'ils estiment en avoir appris assez, ils chiffrent autant de vos données que possible et exigent une grosse somme d'argent sous forme de cryptomonnaie avant de restaurer votre accès.

Bien sûr, s'agissant de criminels, il est difficile de se fier à leur parole. Historiquement, ils ont été tout aussi susceptibles de prendre votre argent et de vous laisser sans rien au lieu de tenir leur promesse. Et même s'ils vous envoient les clés de déchiffrement, vous ne pouvez pas savoir s'ils n'ont pas fait des copies de vos données qu'ils sont en train de vendre sur le dark web.

Nous parlerons des méthodologies de prévention et de récupération ailleurs. Mais pour l'instant, il suffit de garder à l'esprit que d'innombrables histoires de catastrophes ont commencé par un individu qui, pendant un court instant, a glissé, révélant accidentellement des identifiants précieux aux mauvaises personnes.

**Que devriez-vous faire ?**

* Tenez-vous au courant de l'évolution des techniques des attaquants
* Sauvegardez régulièrement vos données

_Cet article et la vidéo qui l'accompagne sont extraits de mon [cours d'introduction à la cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Et il y a bien d'autres ressources technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com)_