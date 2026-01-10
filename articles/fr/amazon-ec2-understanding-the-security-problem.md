---
title: Amazon EC2 – Comprendre et résoudre le problème de sécurité
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-18T19:07:42.000Z'
originalURL: https://freecodecamp.org/news/amazon-ec2-understanding-the-security-problem
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-pixabay-277574.jpg
tags:
- name: AWS
  slug: aws
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
seo_title: Amazon EC2 – Comprendre et résoudre le problème de sécurité
seo_desc: "Hi there. Great to have you here. But I'm afraid I'm going to have to start\
  \ off with some bad news. \nBefore you can really improve the security of your Amazon\
  \ EC2 instances, you'll need to get a handle on all the stuff that can go wrong.\
  \ And I'll giv..."
---

Bonjour. Je suis ravi de vous avoir ici. Mais je crains de devoir commencer par de mauvaises nouvelles. 

Avant de pouvoir vraiment améliorer la sécurité de vos instances Amazon EC2, vous devrez comprendre tout ce qui peut mal tourner. Et je vais vous donner un petit aperçu de ce "hall of shame" dans un instant. 

## Quel est le problème ?

Mais d'abord, à titre d'introduction, je veux vous raconter une histoire vraiment effrayante. Tellement effrayante que vous devriez peut-être vous préparer en allumant toutes les lumières de votre pièce et en attrapant une couverture douce pour vous réconforter.

Voici ce qui s'est passé. Basé sur mes propres expériences passées, je viens de mener une brève expérience. J'ai lancé une instance EC2 exécutant Ubuntu dans l'un de mes comptes AWS. L'instance n'exécutait rien de plus que ce que Ubuntu m'a donné par défaut et elle n'était associée à aucune adresse DNS.

Sa seule connexion avec le monde extérieur était via l'adresse IP publique que AWS lui a assignée. En fait, la seule différence entre cette instance et celle que vous ou moi pourrions normalement exécuter est que j'ai ouvert son groupe de sécurité pour permettre tout le trafic entrant.

Puisque Ubuntu, par défaut, n'exécute pas de pare-feu actif, il n'y aurait donc rien entre l'instance et le grand méchant internet.

Cet article provient de mon [cours sur la sécurisation de vos instances AWS EC2](https://www.udemy.com/course/securing-amazon-ec2-instances/?referralCode=E3ACB9DC5E3B77853E63). Si vous le souhaitez, vous pouvez suivre la version vidéo de cette section ici :

%[https://www.youtube.com/watch?v=femqe6OIJGk&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

Alors, que s'est-il passé ? Eh bien, les entrées du `auth.log` sur l'hôte étaient stupéfiantes. Selon ces journaux, le système s'est lancé pour la première fois vers 14h56. Voici un peu de ce que j'ai vu seulement 35 minutes plus tard :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ec2_security1-f004258.png)

Quelqu'un essayait de se connecter à mon système via SSH en utilisant le nom d'utilisateur `root`. Bien sûr, par défaut, la connexion root est désactivée - et vous devriez la laisser ainsi. Mais cela n'a pas empêché cet individu d'essayer.

Remarquez comment ils n'ont pas seulement utilisé le port SSH standard 22, mais ont également testé d'autres numéros de port (y compris `51912`). Cela suggère que cette tentative faisait partie d'un script automatisé qui teste diverses combinaisons de noms d'utilisateur, de mots de passe et de ports :

```
Aug 10 15:31:17 ip-172-30-1-186 sshd[2777]: error: maximum authentication attempts exceeded for root from 20.210.53.189 port 51912 ssh2 [preauth]

```

Mais ils n'avaient pas fini. Au cours des 75 secondes suivantes, 30 autres tentatives de connexion sont venues de cette même adresse IP. Elles ciblaient différents ports dans la plage des 50 000 et utilisaient différents noms d'utilisateur comme admin, oracle, test, test1, test2, ftpuser et pi.

Le fait qu'ils aient essayé `pi` me dit qu'ils ne réalisaient pas que c'était une instance cloud, mais que, pour autant qu'ils savaient, cela aurait pu être un Raspberry Pi fonctionnant dans un laboratoire domestique.

Je ne sais pas pour vous, mais je trouve cela vraiment effrayant. Bien sûr, quel administrateur ouvrirait délibérément un groupe de sécurité à tout le trafic entrant ? Mais le vrai problème est qu'il existe tant de scripts qui scannent constamment les adresses IP actives et tentent de forcer les connexions système que n'importe quelle adresse IP aléatoire peut s'attendre à des attaques en quelques minutes.

Et, encore une fois, ce n'est pas la première fois que je vois cela en action, et SSH n'est pas le seul service public qui attire de telles attaques. Au minimum, nous devrions prendre cela comme un avertissement pour renforcer nos configurations SSH - ce que je discuterai plus tard.

Mais voici le point. Il est possible d'atteindre une sécurité parfaite - c'est vraiment possible - mais cela impliquerait de verrouiller complètement vos serveurs et de bloquer tout accès depuis l'extérieur. Quel est l'intérêt de faire fonctionner des serveurs de cette manière ? L'objectif est de trouver le meilleur équilibre possible entre la fonctionnalité de l'application et la sécurité de l'infrastructure.

Établir cet équilibre peut inclure l'incorporation de toutes les bases générales de la sécurité informatique comme le durcissement du système et la surveillance, ainsi que l'utilisation intelligente des principales fonctionnalités de sécurité AWS comme les rôles IAM, les groupes de sécurité, les architectures VPC appropriées et, le cas échéant, l'utilisation de VPN.

Alors, qu'est-ce qui attend pour s'en prendre à vos opérations AWS ? Eh bien, il y a des outils de hackers pour accéder à votre système, des exploits pour prendre le contrôle et abuser de vos ressources, et des méthodologies pour faire tomber vos services par la force. Examinons cela un par un.

## Acquisition d'accès

Comme vous l'avez peut-être remarqué à partir du contenu `maximum authentication attempts exceeded` de ces entrées de journal que je vous ai montrées plus tôt, le hacker a essayé d'entrer plusieurs mots de passe pour chaque nom de connexion.

Cela est connu sous le nom d'attaque par force brute, où les hackers parcourent un dictionnaire de mots de passe courants, espérant que l'un d'eux s'avérera correct.

La raison pour laquelle mon système a complètement coupé ces tentatives est que les images Linux EC2 officielles ont un paramètre de configuration SSH par défaut - `MaxAuthTries` - défini à six. Même si vous autorisiez les connexions par mot de passe pour SSH - et même si vous utilisiez de manière irresponsable un mot de passe faible - les chances qu'un hacker le devine en six tentatives sont assez minces.

Si vous le souhaitez, vous pouvez suivre la version vidéo de la deuxième partie de l'article ici :

%[https://www.youtube.com/watch?v=Ajwoe9sSjuo&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

Bien sûr, si un hacker peut obtenir des identifiants réels et actifs, il n'aura pas besoin de deviner. C'est pourquoi vous devez être conscient des attaques de phishing où les hackers utilisent la manipulation sociale pour amener les victimes à révéler involontairement leurs informations de connexion.

Ils peuvent également profiter des communications qui ont lieu à l'aide d'appareils compromis ou qui sont envoyées sur des connexions non cryptées pour renifler vos identifiants lorsque vous les utilisez.

En termes de cloud, imaginez simplement combien de plaisir quelqu'un pourrait avoir une fois qu'il a obtenu vos identifiants de compte AWS. Cela leur permettrait de facturer rapidement des centaines de milliers de dollars sur votre carte de crédit, en déployant des ressources AWS presque illimitées au service de leurs propres besoins criminels. En plus de devoir couvrir ces factures, vous pourriez également être tenu responsable de tout crime commis avec ces ressources.

## Exploits

Une fois que les hackers ont accès à votre système, les choses ne peuvent que s'aggraver. Qu'ils fassent quelque chose de méchant tout de suite ou qu'ils traînent pendant des mois en planifiant quelque chose de particulièrement néfaste, si vous ne les attrapez pas, ils installeront finalement leur malware.

Cela pourrait prendre la forme de keyloggers qui enregistrent chaque caractère que vous et vos collègues entrez dans une session shell. Il ne faudra que peu de temps avant que ces keyloggers ne capturent des identifiants qui leur permettront d'élever leurs propres permissions.

Le malware pourrait également prendre la forme d'opérations de minage de cryptomonnaie qui utilisent de manière intensive - et coûteuse - vos ressources système afin que les hackers puissent en profiter. Ou - et c'est le plus effrayant - ils pourraient décider de crypter des données clés sur vos disques et exiger des paiements élevés avant de vous permettre de les décrypter et de retrouver l'accès.

Cela, bien sûr, est connu sous le nom de ransomware, et c'est actuellement le plus gros problème auquel sont confrontés les systèmes de niveau entreprise. Cela coûte des milliards de dollars chaque année aux gouvernements et aux entreprises.

## Perturbation du service

Même s'ils n'entrent pas dans votre système, les méchants peuvent encore causer beaucoup de dégâts depuis l'extérieur. Si, par exemple, ils détectent des mauvaises configurations sur vos serveurs - comme des ports d'écoute réseau inutiles ouverts, des points de terminaison de base de données mal écrits, ou des logiciels obsolètes comme FTP ou telnet, ils peuvent vous causer beaucoup de problèmes.

Et, pour ces criminels ayant accès à des réseaux de serveurs zombies piratés, ils pourraient submerger la capacité de votre réseau avec des attaques par déni de service distribué - empêchant vos utilisateurs légitimes d'accéder à vos services.

Heureusement, AWS offre une protection sérieuse contre les DDoS dès la sortie de la boîte, donc ce n'est probablement pas une grande préoccupation pour vous en tant qu'administrateur.

En parlant d'ingénierie AWS, c'est probablement le bon moment pour discuter de leur [Modèle de responsabilité partagée](https://aws.amazon.com/compliance/shared-responsibility-model/). La façon dont l'entreprise le formule, AWS est responsable de la sécurité du cloud, tandis que leurs clients - c'est-à-dire vous et moi - sont responsables de la sécurité de ce que vous mettez dans le cloud.

En pratique, cela signifie que vous n'avez pas à vous soucier des choses terribles qui pourraient arriver aux serveurs physiques et aux dispositifs de stockage utilisés par vos instances EC2. AWS protégera ses entrepôts et son matériel réseau contre les intrusions et les dommages non autorisés. Ils prendront également la responsabilité du logiciel alimentant leurs services gérés - comme l'API et les tableaux de bord que vous utilisez pour configurer l'activité du compte.

Mais vous êtes responsable de tout le reste. Cela inclut les données que vos instances pourraient générer et les systèmes d'exploitation eux-mêmes. Vous êtes donc responsable de la mise à jour de votre système d'exploitation et de vos logiciels d'application, et de la réalisation de sauvegardes appropriées de toutes les données et fichiers de configuration que vous générez.

Vous êtes également responsable de faire les bons choix de configuration au niveau AWS, comme obtenir les bons paramètres de groupe de sécurité et de réseau. Selon l'industrie et la juridiction nationale dans laquelle vous opérez, vous pourriez également être tenu de respecter une ou plusieurs normes de conformité réglementaire.

AWS fournit une documentation indiquant quelles normes chaque service respecte. Si vous ouvrez la page web montrée ci-dessous, vous pourriez développer la section Payment Card Industry - PCI, par exemple, et ensuite rechercher EC2. Vous verrez que l'infrastructure EC2 est effectivement conforme à la norme PCI ;

![Image](https://www.freecodecamp.org/news/content/images/2023/03/services_in_scope.png)

Nous avons vu à quel point vos instances EC2 sont vulnérables lorsqu'elles sont laissées sans protection adéquate. Mais nous avons également vu certaines des meilleures pratiques de l'industrie pour les maintenir en sécurité. Vous savez ce que vous devez faire ensuite.

_Cet article provient de mon [cours sur la sécurisation de vos instances AWS EC2](https://www.udemy.com/course/securing-amazon-ec2-instances/?referralCode=E3ACB9DC5E3B77853E63). Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_