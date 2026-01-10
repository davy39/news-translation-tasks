---
title: Comment construire votre propre VPN WireGuard en cinq minutes
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2022-12-19T20:46:15.000Z'
originalURL: https://freecodecamp.org/news/build-your-own-wireguard-vpn-in-five-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-ibrahim-boran-339814.jpg
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: vpn
  slug: vpn
seo_title: Comment construire votre propre VPN WireGuard en cinq minutes
seo_desc: "You may already understand how important a good VPN can be for maintaining\
  \ the security and privacy of your mobile communications. \nWhether you need to\
  \ use your phone for banking over a public airport or coffee shop WiFi connection,\
  \ or you're worried..."
---

Vous comprenez peut-être déjà à quel point un bon VPN peut être important pour maintenir la sécurité et la confidentialité de vos communications mobiles. 

Que vous ayez besoin d'utiliser votre téléphone pour des opérations bancaires sur un réseau WiFi public d'aéroport ou de café, ou que vous soyez inquiet à l'idée que des personnes mal intentionnées écoutent vos interactions en ligne, le chiffrement par tunnel qu'un bon VPN vous offre peut être inestimable. 

Le défi, cependant, est de trouver un VPN qui soit vraiment "bon" – et qui soit à la fois pratique et abordable.

Il existe de nombreux services VPN commerciaux, et la configuration de l'un d'eux pour votre téléphone ou votre ordinateur portable est généralement assez simple. 

Mais ces services présentent deux inconvénients potentiels : ils sont souvent coûteux, avec des paiements moyennant environ 10 $ par mois, et vous ne pouvez jamais être tout à fait sûr à 100 % qu'ils ne fuient pas ou n'abusent pas de vos données (accidentellement ou intentionnellement). 

De plus, les VPN moins chers limitent souvent votre utilisation de données et le nombre d'appareils que vous pouvez connecter.

Si vous aimez regarder des versions vidéo de tutoriels pour compléter votre apprentissage, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=kxj8GMvnASE]

## Ce que WireGuard offre

Mais si vous avez un serveur Linux basé sur le cloud en cours d'exécution, construire un VPN WireGuard peut être un moyen simple et gratuit d'ajouter une sécurité et une confidentialité sérieuses et sans compromis à votre vie. 

Si vous prévoyez de limiter le VPN à vos appareils et à ceux de quelques amis, vous ne remarquerez probablement même pas de charge supplémentaire sur votre serveur. Même si vous deviez lancer et payer pour une instance réservée AWS EC2 t2.micro dédiée, les coûts annuels devraient toujours être significativement moins chers que la plupart des VPN commerciaux. Et, en bonus, vous aurez un contrôle complet sur vos données.

Je vais vous montrer comment tout cela fonctionne en utilisant le logiciel open source WireGuard sur un serveur Linux Ubuntu. 

Pourquoi WireGuard ? Parce qu'il est vraiment facile à utiliser, conçu pour être particulièrement résistant aux attaques, et il est si bon dans ce qu'il fait qu'il a récemment été intégré au noyau Linux lui-même. 

Le travail réel pour faire cela prendra vraiment seulement cinq minutes - ou moins. Cela dit, la planification, le dépannage pour des problèmes inattendus et, si nécessaire, le lancement d'un nouveau serveur peuvent ajouter un temps significatif au projet.

## Comment configurer votre environnement

Tout d'abord, vous devrez ouvrir le port UDP 51820 dans le pare-feu que vous utilisez. Voici à quoi cela ressemblerait pour le groupe de sécurité associé à une instance AWS EC2 :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/SG_rule-2.png)

Maintenant, sur le serveur Linux, en utilisant un shell sudo, nous commencerons par installer les paquets WireGuard et resolvconf. 

Techniquement, nous n'aurons probablement pas besoin de resolvconf ici, mais comme c'est ce dont vous auriez besoin si vous vouliez configurer une machine Linux comme client WireGuard, j'ai pensé l'inclure ici aussi.

```
apt install wireguard resolvconf
```

## Comment générer des clés de chiffrement

La commande `wg genkey` génère une nouvelle clé privée de chiffrement et l'enregistre comme fichier dans le répertoire /etc/wireguard. Ce répertoire a été créé automatiquement lorsque nous avons installé WireGuard. 

La commande `chmod` définit les permissions restrictives appropriées pour ce fichier de clé privée. 

Comme tout dans Linux, il existe d'autres moyens d'accomplir cela, mais assurez-vous de le faire correctement.

```
wg genkey | sudo tee /etc/wireguard/private.key
chmod go= /etc/wireguard/private.key
```

Ensuite, nous utiliserons la valeur de notre clé privée pour générer une clé publique correspondante – qui sera également enregistrée dans le répertoire /etc/wireguard. L'objectif est d'ajouter la clé _publique_ du serveur à la configuration WireGuard de tous les appareils clients que nous utiliserons, puis d'ajouter les clés publiques de ces clients à la configuration du serveur ici. 

Les clés privées ne doivent jamais quitter les machines pour lesquelles elles sont créées – et doivent toujours être soigneusement protégées.

```
cat /etc/wireguard/private.key | wg pubkey | sudo tee
```

## Comment configurer le serveur WireGuard

Nous sommes maintenant prêts à créer un fichier de configuration serveur. Suivant la convention, je nommerai le fichier wg0.conf, mais vous pouvez lui donner n'importe quel nom que vous souhaitez. Vous pouvez également avoir plusieurs configurations (avec différents noms de fichiers) existant en même temps.

Voici à quoi ressemblera notre configuration :

```
[Interface]
Address = 10.5.5.1/24
ListenPort = 51820
# Utilisez votre propre clé privée, depuis /etc/wireguard/privatekey
PrivateKey = votre_clé

[Peer]
# Clé publique de la station de travail
PublicKey = votre_clé
# Adresse IP du client VPN dans le VPN
AllowedIPs = 10.5.5.2/32

[Peer]
# Clé publique de l'ordinateur portable
PublicKey = votre_clé
# Adresse IP du client VPN dans le VPN
AllowedIPs = 10.5.5.3/32
```

Remarquez que ce fichier comporte trois sections : une Interface et deux pairs. La section Interface définit l'adresse de réseau NAT privée que notre serveur utilisera. C'est l'adresse privée à laquelle les clients se connecteront – après avoir d'abord demandé l'accès via l'adresse IP publique du serveur, bien sûr. 

Vous n'êtes pas obligé de suivre mon adressage, tant que vous utilisez une plage d'IP privée valide qui ne chevauche aucun bloc de réseau utilisé par votre serveur ou votre client. 

En correspondance avec la règle de groupe de sécurité UDP que j'ai configurée précédemment dans AWS, je définis le ListenPort comme 51820. Mais je pourrais choisir une adresse différente pour ajouter un peu plus de sécurité si je le souhaite. 

Enfin, je collerais la clé privée du serveur comme valeur de `PrivateKey` afin que WireGuard puisse authentifier les requêtes entrantes des clients.

La première section `peer` ne contient rien de plus que la clé _publique_ et l'adresse IP privée assignée d'un client. La deuxième section `peer` fait de même pour un deuxième appareil client. 

Obtenir ces clés publiques depuis le client est la tâche la plus manuelle impliquée dans toute cette configuration. Mais, puisque c'est votre propre VPN, vous pouvez généralement trouver un moyen de copier et coller directement dans votre configuration serveur afin de ne pas avoir à taper péniblement tout cela.

Cela devrait être tout. J'utiliserai la commande `wg-quick` pour donner vie au VPN. `up` indique à WireGuard de lire la configuration wg0.conf que nous venons de créer et de l'utiliser pour construire une nouvelle interface VPN. 

```
wg-quick up wg0
```

L'exécution de `wg` nous montrera que cela a fonctionné. Enfin, j'exécuterai `systemctl enable` pour indiquer à Linux de charger cette interface WireGuard automatiquement à chaque redémarrage du serveur.

```
systemctl enable wg-quick@wg0
```

## Comment configurer les clients WireGuard

C'est tout ce dont nous aurons besoin du côté serveur. La configuration de votre appareil client avec WireGuard sera soit beaucoup plus facile, soit plus ou moins la même. 

Que signifie _cela_ ? Eh bien, si vous travaillez avec Windows, macOS, Android ou iOS, il existe des liens vers des applications GUI disponibles depuis [cette page d'installation de wireguard.com](https://www.wireguard.com/install/). Ces applications généreront des paires de clés _pour_ vous. Vous n'aurez besoin que d'entrer l'adresse IP ou le domaine du serveur et sa clé publique. Vous prendrez ensuite la clé publique du client et l'ajouterez au fichier de configuration wg0.conf du serveur comme je vous l'ai montré précédemment.

Cependant, si vous souhaitez ajouter un client PC ou portable Linux, c'est un peu plus compliqué. Vous suivrez essentiellement toutes les étapes que vous avez vues pour la configuration du serveur, y compris la génération de clés. Vous créerez même un fichier de configuration nommé wg0-conf (si c'est le nom que vous préférez). Mais voici à quoi ce fichier de configuration devrait ressembler :

```
[Interface]
# L'adresse que votre ordinateur utilisera sur le VPN
Address = 10.5.5.2/32
DNS = 8.8.8.8
# Chargez votre clé privée depuis un fichier
PostUp = wg set %i private-key /etc/wireguard/privatekey
# Ping également le serveur VPN pour s'assurer que le tunnel est initialisé
PostUp = ping -c1 10.47.47.1
[Peer]
# Clé publique WireGuard du serveur VPN
PublicKey = votre_clé
# Adresse IP publique de votre serveur VPN (UTILISEZ LA VÔTRE !)
Endpoint = 54.160.21.183:51820
# 10.0.0.0/24 est le sous-réseau VPN
AllowedIPs = 10.47.47.0/24
# PersistentKeepalive = 25
```

La section `Interface` représente cette fois la machine cliente, tandis que la section `Peer` ci-dessous fait référence au serveur. Commençons par `Interface`. L'adresse IP privée doit correspondre à l'adresse que vous donnez à ce client particulier dans la configuration sur le serveur. 

Si vous avez besoin que votre client contourne un serveur DNS local, vous pouvez spécifier un serveur DNS personnalisé ici. Celui-ci est fourni par Google.

Au lieu de coder en dur votre clé privée locale dans votre fichier de configuration comme nous l'avons fait sur le serveur, vous pourriez indiquer à WireGuard de lire le fichier privatekey chaque fois qu'il se charge. Cela est probablement une meilleure pratique de sécurité – et nous aurions tout aussi bien pu le faire sur le serveur aussi. Enfin, le script de configuration testera notre connexion avec la commande `PostUp` ping.

La configuration `Peer` – ou serveur – nécessite la clé _publique_ du serveur, qui est ajoutée ici. 

Le `Endpoint` est l'endroit où vous indiquez à WireGuard où trouver le serveur. Rien ne fonctionnera sans cela ! Cela nécessiterait l'IP publique du serveur – ou son nom de domaine – suivi du port que vous avez choisi. Encore une fois, 51820 est le port par défaut de WireGuard. 

Enfin, le paramètre `AllowedIPs` définit la plage d'adresses réseau que vous utiliserez, et la valeur optionnelle `PersistentKeepalive` peut empêcher les déconnexions.

Vous lancez WireGuard sur le client exactement de la même manière que vous l'avez fait sur le serveur, en utilisant `wg-quick up wg0`. Encore une fois, cependant, toutes ces étapes ne seront nécessaires que pour les clients Linux. Vous pouvez utiliser les applications pour les autres plateformes.

## Conclusion

Donc, c'est tout. Comme je l'ai dit, un VPN fonctionnel en environ cinq minutes de travail. Vous avez maintenant une excuse de moins pour protéger votre vie privée en ligne et sécuriser vos communications.

_Pour plus de bonnes choses technologiques, n'oubliez pas de vous abonner à [ma chaîne YouTube](https://www.youtube.com/@davidbclinton) et, lorsque vous aurez un moment, consultez les nombreux livres et cours sur Linux, la sécurité, l'analyse de données et AWS disponibles sur [mon site bootstrap-it.com](https://bootstrap-it.com)._