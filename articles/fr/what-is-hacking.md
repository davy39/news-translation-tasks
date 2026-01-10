---
title: Qu'est-ce que le Hacking ? La méthodologie du hacker expliquée
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2022-09-22T15:21:49.000Z'
originalURL: https://freecodecamp.org/news/what-is-hacking
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/hacker-methodology-image.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Qu'est-ce que le Hacking ? La méthodologie du hacker expliquée
seo_desc: "Time to learn the basics of the splendid art of hacking \U0001F468‍\U0001F4BB\
  \U0001F469‍\U0001F4BB. \nIn this article, you will learn what the hacking process\
  \ really looks like. And hopefully one day, you'll get to say those famous words:\
  \ “I’m in”.\nDisclaimer: This is for educationa..."
---

Il est temps d'apprendre les bases du splendide art du hacking 👨‍💻👩‍💻. 

Dans cet article, vous apprendrez à quoi ressemble réellement le processus de hacking. Et avec un peu de chance, vous pourrez un jour prononcer ces mots célèbres : « Je suis dedans ».

**Avertissement : Ceci est uniquement à des fins éducatives.** S'il vous plaît (avec une cerise sur le gâteau), n'utilisez pas ces connaissances pour mener des activités illégales. Je pourrais être l'un des white hats qui vous mettra en prison un jour 🙃. Merci.

## Comment les hackers hackent-ils ?

![Image](https://miro.medium.com/max/1050/1*jHEa9VlHhb1cRF0szm_HRw.jpeg)
_Tony Stark tentant de hacker le S.H.E.I.L.D | Crédit : animatedtimes.com_

Puisque vous lisez cet article, je suppose que vous connaissez déjà les bases de ce qu'est le hacking, alors entrons directement dans le vif du sujet. 

Il n'y a pas vraiment de processus de hacking universellement reconnu, en partie parce qu'il existe plusieurs [types de hackers](https://www.freecodecamp.org/news/white-hat-black-hat-red-hat-hackers/). Mais, je vais vous présenter les étapes que la majorité des hackers (et moi-même) suivent. 

Elles sont :

1. Reconnaissance
2. Énumération
3. Exploitation
4. Élévation de privilèges
5. Post-exploitation
6. Effacement des traces
7. Rédaction de rapport

Nous allons passer en revue chacune d'elles en détail afin que vous puissiez bien appréhender le processus.

Si vous souhaitez approfondir vos connaissances et en savoir plus sur ce que font les hackers white hat (éthiques), [consultez ce cours](https://www.freecodecamp.org/news/linux-essentials-for-hackers/).

## Reconnaissance

![A neon themed hollywood hacker](https://miro.medium.com/max/1050/1*r4786dLhJKeD4X9Eh-tqdg.jpeg)
_Un hacker hollywoodien au thème néon | Crédit : Wallpaperflare.com_

La Recon (alias footprinting) est la première étape, la plus longue et la plus importante. Cela consiste à obtenir autant d'informations que possible sur la cible sans interagir directement avec elle. 

Les compétences de base en OSINT (Open Source Intelligence) sont ici les meilleures amies d'un hacker.

Leçon rapide : l'OSINT est la collecte et l'analyse d'informations provenant de sources publiques afin d'obtenir des renseignements exploitables. Les agences de sécurité nationale, les journalistes d'investigation et les hackers rassemblent légalement ces informations afin de créer respectivement des mesures, des articles et des dossiers sur des cibles. 

Vous pouvez trouver le guide du Framework OSINT [ici](https://osintframework.com/).

La plus grande ressource pour la reconnaissance est Internet, et le meilleur outil est le moteur de recherche Google. Pour faciliter grandement les choses, le [Google dorking](https://www.techopedia.com/definition/30938/google-dorking) serait un bon point de départ. Le « dorking » dans ce sens signifie l'utilisation de techniques de recherche avancées pour trouver plus d'informations sur une cible que vous ne pourriez normalement pas trouver en utilisant des méthodes classiques.

D'autres ressources pour la reconnaissance incluent :

1. Wikipedia (La plus grande encyclopédie à ce jour)
2. Les réseaux sociaux tels qu'Instagram, Twitter et Facebook (La meilleure ressource pour les ingénieurs sociaux)
3. who.is (Pour obtenir des informations sur un site web)
4. sublist3r (Répertorie les sous-domaines accessibles publiquement)
5. Les médias tels que les journaux, la radio et la télévision

## Énumération

![Magnifying glass over binary ID fingerprint](https://miro.medium.com/max/1050/1*XbORSf1nFpWBKEu285-Azg.jpeg)
_Loupe sur une empreinte digitale d'identifiant binaire | Crédit : Wallpaperflare.com_

C'est comme la reconnaissance, sauf que vous obtenez des informations sur la cible en interagissant avec elle dans le but de rechercher une vulnérabilité. 

Notez cependant que les choses peuvent devenir beaucoup plus risquées car la cible pourrait découvrir que vous essayez d'obtenir des informations sur elle et pourrait mettre en place des contre-mesures pour vous entraver.

L'énumération réseau implique le scan de ports et la cartographie réseau. Cela vous aide à en savoir plus sur le système d'exploitation de la cible, les ports ouverts et les services en cours d'exécution, ainsi que leur version. Nmap (network mapper), Burp Suite et exploit-db/searchsploit sont des outils courants que vous pouvez utiliser pour l'énumération réseau.

Conseil : Connaître la version des services est un excellent moyen de trouver une vulnérabilité. Les anciennes versions de logiciels peuvent présenter une vulnérabilité connue qui pourrait figurer sur le site exploit-db. Vous pourriez ensuite l'utiliser pour effectuer une exploitation.

L'énumération physique consiste à obtenir des informations par des moyens physiques. Cela peut se faire via le « dumpster diving » (récupérer des identifiants et des informations confidentielles dans les poubelles) et l'[ingénierie sociale](https://www.freecodecamp.org/news/social-engineering-the-art-of-hacking-humans/). 

L'ingénierie sociale est un sujet assez vaste qui fera l'objet d'un article ultérieur. Cependant, en termes simples, cela signifie hacker des humains en utilisant des compétences sociales manipulatrices.

## Exploitation

![A fake terminal access](https://miro.medium.com/max/1050/1*mJMn9jW6b0S4-EhX1fnk2g.jpeg)
_Un faux accès terminal | Crédit : Wallpaperflare.com_

L'exploitation consiste à réussir à accéder à la cible en utilisant une vulnérabilité découverte lors de l'énumération. 

Une technique courante d'exploitation consiste à délivrer un Payload après avoir profité de la vulnérabilité. En termes simples, il s'agit de trouver une faille dans la cible, puis d'exécuter un code ou un logiciel qui vous permet de manipuler le système, comme un shell bash.

Les vulnérabilités célèbres qui sont couramment exploitées sont EternalBlue (Windows) et les vulnérabilités Apache log4j (serveurs web).

Outils courants que vous pouvez utiliser pour l'exploitation :

1. Metasploit (Le gros calibre 🔫)
2. Burp Suite (Pour les applications web)
3. Sqlmap (Pour les bases de données)
4. Msfvenom (Utilisé pour créer des Payloads personnalisés)

Leçon rapide : Un Payload est un logiciel exécuté après l'exploitation d'une vulnérabilité. Une fois exploitée, l'ordinateur cible n'a rien pour vous donner accès. Vous avez donc besoin d'un Payload pour vous donner accès et vous permettre de manipuler la cible. 

Un Payload très courant utilisé par de nombreux hackers est Meterpreter. C'est un Payload de Metasploit qui vous permet de naviguer facilement dans l'ordinateur hacké.

## Élévation de privilèges

![Random Text with “Administrator”](https://miro.medium.com/max/1050/1*dga9Ef2bvTg0BtG5_u5VxA.jpeg)
_Texte aléatoire avec « Administrator » | Crédit : Wallpaperflare.com_

Afin de comprendre l'élévation de privilèges, vous devez saisir deux concepts :

1. Comptes utilisateurs
2. Privilèges

Un compte utilisateur est un profil sur un ordinateur ou un réseau qui contient des informations accessibles via un nom d'utilisateur et un mot de passe. 

Il existe deux types de comptes utilisateurs : le compte Administrateur et le compte Standard. Les utilisateurs d'ordinateurs personnels n'ont généralement qu'un seul compte utilisateur, qui est l'administrateur. En revanche, les organisations disposent de plusieurs comptes sur un réseau ou un ordinateur, un administrateur système ayant le compte administrateur et les employés de base ayant divers comptes standards.

Les privilèges sont les permissions qui vous permettent d'écrire, de lire et d'exécuter des fichiers et des applications. Un utilisateur standard n'a pas de privilèges (permissions) sur les fichiers et applications critiques que nous voulons. Cependant, un compte administratif aura des privilèges pour tout.

L'escalade est le passage d'un compte utilisateur à un autre. Cela peut être vertical ou horizontal. 

L'escalade verticale se produit lorsqu'un hacker passe d'un compte avec moins de privilèges (compte standard) à un compte avec plus de privilèges (compte administratif).

L'escalade horizontale se produit lorsqu'un hacker passe d'un compte utilisateur à un compte similaire de même niveau de privilège dans l'espoir d'effectuer une escalade verticale avec le nouveau compte compromis (de compte standard à compte standard).

Les comptes utilisateurs administratifs que vous voudriez cibler sont root (Linux) ou Administrator/System (Windows). Ces comptes ont **tous** les privilèges et sont pratiquement une mine d'or si vous y accédez, car vous pouvez prendre le contrôle absolu de l'ordinateur.

Les techniques pour effectuer une élévation de privilèges incluent :

1. Password spraying (Réutilisation de mots de passe)
2. Craquage de hachages de mots de passe (Trouver les mots de passe d'autres utilisateurs)
3. Recherche de clés SSH (Utilisées pour l'escalade horizontale)
4. Abus de binaires SUID (Profiter de privilèges mal configurés dans Linux)
5. Exécution de scripts d'outils pour rechercher des voies d'escalade ([enum4linux](https://www.kali.org/tools/enum4linux/) est efficace et [PEASS-ng](https://github.com/carlospolop/PEASS-ng) possède une excellente suite)

## Post-exploitation

![Image](https://miro.medium.com/max/1050/1*qidw-Mivgag6dqiyU2-y9g.jpeg)
_Code avec le texte « malicious virus » | Crédit : Wallpaperflare.com_

Généralement, les white hats passent directement à la toute dernière étape. Mais j'inclurai celle-ci et la suivante par souci de connaissance. 

La post-exploitation est l'utilisation d'outils dans le but d'obtenir une persistance et d'extraire des informations sensibles de l'ordinateur cible.

Cela peut se faire de plusieurs manières, notamment :

1. Installation d'une backdoor permanente, d'un listener ou d'un rootkit
2. Installation de malwares tels que des virus et des trojans
3. Téléchargement de propriété intellectuelle, d'informations sensibles et d'informations personnellement identifiables (PII)

## Effacement des traces

![Image](https://miro.medium.com/max/1050/1*be1OfXU8MoaoqvhM_X6ecw.jpeg)
_Un arrière-plan sur le thème Anonymous | Crédit : Wallpaperflare.com_

C'est aussi simple que cela puisse paraître, mais cela peut être incriminant s'il y a la moindre erreur. Un hacker malveillant doit faire attention à ne pas laisser derrière lui des fichiers, des scripts ou quoi que ce soit qui puisse être utilisé par un expert en criminalistique numérique pour remonter jusqu'à lui. 

Certaines choses de base à faire seraient de supprimer les fichiers de log et le fichier d'historique dans Linux. Le Payload Meterpreter dispose même d'une fonctionnalité pour supprimer tous les logs sur le gestionnaire d'événements Windows.

## Rédaction de rapport

![Image](https://miro.medium.com/max/1050/1*kpf_vAmFagqzk5nevBwgUg.jpeg)
_Rédaction de rapport numérique | Crédit : Wallpaperflare.com_

Il s'agit de l'étape finale de la méthodologie du hacker. Elle consiste à rédiger un compte rendu de l'ensemble du processus décrit ci-dessus. 

Il existe différents formats, mais un format de base comprendra :

1. Les vulnérabilités trouvées et leur niveau de risque
2. Une brève description de la manière dont les vulnérabilités ont été découvertes
3. Des recommandations sur la façon de remédier aux vulnérabilités

Conseil : La prise de notes lors du hacking est très importante. Je l'ai personnellement appris à mes dépens lors de CTF (Capture The Flag). 

Non seulement cela facilite la rédaction des rapports, mais cela vous permet également d'éviter de répéter des tentatives infructueuses et de trier facilement les informations. Cela vous permet aussi de revenir sur ce que vous avez fait plus tard. Prendre des captures d'écran est également une excellente idée.

## Conclusion

Très bien, faisons un récapitulatif rapide de la méthodologie du hacker :

1. Reconnaissance
2. Énumération
3. Exploitation
4. Élévation de privilèges
5. Post-exploitation
6. Effacement des traces
7. Rédaction de rapport

### Ressources pour vous aider à pratiquer :

1. [Testez vos connaissances](https://tryhackme.com/room/hackermethodology) sur la méthodologie du hacker
2. Conseils sur [la façon de vous protéger des hackers](https://www.cybervie.com/blog/hackers-methodology-cyber-security/)
3. [Plus d'informations sur l'OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence)

### Remerciements

Merci à [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), et ma famille pour l'inspiration, le soutien et les connaissances utilisés pour monter cet article. Vous êtes les meilleurs.