---
title: Comment configurer un VPN sur Linux en 5 minutes gratuitement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-24T16:57:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-vpn-for-free-or-paid-on-linux-62e1a93d04f3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ki9vH87FbtYJeQP29IM3fA.png
tags:
- name: Life lessons
  slug: life-lessons
- name: Linux
  slug: linux
- name: privacy
  slug: privacy
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer un VPN sur Linux en 5 minutes gratuitement
seo_desc: 'By CodeDraken

  In this short and overdue tutorial, we will set up a virtual private network (VPN)
  to help protect your online anonymity. I will not be covering much on what a VPN
  is or what these settings are. We’re going to set one up. Let’s get stra...'
---

Par CodeDraken

Dans ce tutoriel court et attendu, nous allons configurer un réseau privé virtuel (VPN) pour vous aider à protéger votre anonymat en ligne. Je ne vais pas trop m'étendre sur ce qu'est un VPN ou sur ce que ces paramètres signifient. Nous allons en configurer un. Commençons sans plus tarder.

**Version Windows :**

[**Comment configurer un VPN sur Windows gratuitement en 5 minutes**](https://medium.com/@codedraken/how-to-setup-a-vpn-on-windows-for-free-in-5-minutes-1210bce9a46d)
[_Dans ce tutoriel, nous allons configurer un VPN et remplacer notre DNS pour protéger notre vie privée._medium.com](https://medium.com/@codedraken/how-to-setup-a-vpn-on-windows-for-free-in-5-minutes-1210bce9a46d)

#### Mise à jour :

Cela fonctionne sur **Ubuntu <=16**.xx et la plupart des autres distributions. Si vous êtes sur Ubuntu 18+, alors v[oyez cet article pour les étapes mises à jour](https://medium.com/@codedraken/ah-youre-on-ubuntu-18-f256cf8a1d9f).

Si vous rencontrez des problèmes, exécutez un test sur [ipleak.net](https://ipleak.net/) pour découvrir quelles informations fuient, puis [consultez cette réponse](https://medium.com/@codedraken/hello-i-apologize-for-the-late-reply-77ad8ad1a11f) et celle qui y est liée. Si cela ne résout pas votre problème, postez un commentaire avec autant d'informations que possible.

Vous aurez besoin de :

* Un ordinateur avec un système d'exploitation Linux. J'utilise Ubuntu. Les commandes peuvent être différentes si vous n'êtes pas sur une distribution basée sur Debian.
* Des privilèges Admin/Sudo
* Des compétences informatiques de base
* Une connaissance de base de ce qu'est un VPN

Prenez note de toutes les modifications que vous apportez et faites des sauvegardes au cas où quelque chose se passerait mal. Pour information, je ne suis affilié à aucun des sites liés ici. Suivez ce tutoriel à vos propres risques, car vous pourriez modifier certains paramètres.

### Partie 1 : Changer votre DNS

Votre serveur de noms de domaine (DNS) peut révéler certaines informations sur vous, nous allons donc vouloir le changer. Commencez par utiliser un outil tel que [DNS leak test](https://www.dnsleaktest.com) pour voir quelles informations sont visibles. Ensuite, travaillez à les masquer.

1. Nous allons utiliser OpenDNS. Rendez-vous sur leur site web et récupérez leurs deux adresses IP de serveur de noms que vous pouvez trouver sur leur [Page de Guide d'Installation](https://www.opendns.com/setupguide)

* 208.67.222.222
* 208.67.220.220

2. Éditez : /etc/dhcp/dhclient.conf

Dans votre terminal, tapez ou copiez/collez la commande ci-dessous. Nano est un éditeur de texte dans le terminal. Si le fichier est situé ailleurs sur votre machine, cherchez-le ou utilisez Google pour le trouver.

```
sudo nano /etc/dhcp/dhclient.conf
```

Cherchez la ligne qui dit « prepend domain-name-servers. » Si elle est commentée avec un symbole # au début de la ligne, décommentez-la en supprimant le #. Modifiez maintenant la ligne pour qu'elle utilise les adresses IP d'OpenDNS, et ajoutez une autre adresse 8.8.8.8 comme dans mon exemple ci-dessous. **Votre internet peut temporairement cesser de fonctionner à ce stade !**

```
prepend domain-name-servers 208.67.222.222, 208.67.220.220, 8.8.8.8;
```

Cette ligne signifie qu'il utilisera la première adresse, puis la deuxième si la première échoue, et enfin 8.8.8.8 si les deux premières échouent. Cela n'arrive généralement pas. Nous ajoutons 8.8.8.8 car par défaut, il utilise 3 adresses. Si nous n'ajoutons pas la troisième et que les deux premières échouent, votre vraie adresse sera utilisée. Sauvegardez et quittez comme indiqué ci-dessous :

Appuyez sur CTRL + O
Appuyez sur ENTRÉE
Appuyez sur CTRL + X

Cela sauvegardera et fermera le fichier. Maintenant, nous devons redémarrer network-manager avec la commande suivante.

```
sudo service network-manager restart
```

Vous devriez maintenant vérifier si cela fonctionne. Entrez la commande ci-dessous et voyez si les serveurs de noms apparaissent. Faites un test de fuite DNS sur le site lié ci-dessus.

```
cat /etc/resolv.conf
```

![Image](https://cdn-media-1.freecodecamp.org/images/NAPB3f48SQnp8IewjzDWYOK9B67XUaO1rs9w)

**Problèmes potentiels**

> **J'ai suivi les étapes, mais la commande cat ne montre que nameserver 127.0.1.1**
> Merci à [Dietmar](https://medium.com/@dlichota?source=post_header_lockup) et [AnalyzeTrades](https://medium.com/@analyzetrades?source=post_header_lockup) pour ce problème/solution
> _Essayez de commenter/supprimer **dns=dnsmasq** de **/etc/NetworkManager/NetworkManager.conf**_

### Partie 2 : Configurer un VPN

**Corriger une fuite DNS dans le navigateur web :**

1. Dans **Firefox**, tapez about:config dans la barre d'adresse et appuyez sur Entrée.
2. Sur la page de configuration, recherchez : media.peerconnection.enabled
3. Changez-le en false en double-cliquant dessus.
4. Redémarrez Firefox.

Je ne sais pas comment cela se fait dans les autres navigateurs.

**Obtenir un VPN gratuit**

1. Recherchez sur Google un VPN gratuit et assurez-vous qu'il est bon. Je vais utiliser [VPNBook](http://www.vpnbook.com/freevpn) pour le reste des étapes.
2. Sur VPNBook, vous téléchargez simplement le fichier de configuration pour le VPN que vous voulez. Copiez le nom d'utilisateur et le mot de passe. Le mot de passe change périodiquement, vous devrez donc le récupérer à nouveau plus tard. Peu importe où vous vous trouvez lorsque vous choisissez votre fichier de configuration. Vous pouvez être aux États-Unis, télécharger celui de l'Euro et apparaître comme étant en Europe.

![Image](https://cdn-media-1.freecodecamp.org/images/HchTObMrt8AW80L6ym8DZsDVa3ozXUYKt4cC)

3. Après avoir extrait le fichier zip téléchargé, ouvrez à nouveau votre terminal. Changez de répertoire où vous l'avez extrait, ou faites un clic droit et choisissez « Ouvrir dans le Terminal ». Nous n'avons plus que quelques étapes maintenant.

4. Installez OpenVPN pour utiliser la configuration.

```
sudo apt-get install openvpn
```

5. Fermez votre navigateur et tout ce qui est connecté à Internet. Pour utiliser OpenVPN, entrez la commande ci-dessous pour exécuter la configuration que vous voulez. Une fois qu'il dit « Initialisation terminée », vous êtes prêt. Vous devriez garder le terminal ouvert. Si cela échoue, essayez un autre VPN, ou lisez l'erreur et essayez de la résoudre.

```
sudo openvpn vpnbook-ca1-tcp443.ovpn
```

6. Enfin, testez si cela fonctionne en faisant un autre test de fuite DNS.

![Image](https://cdn-media-1.freecodecamp.org/images/LqnoSqqFtiI9sJ1GeDKJpf7X4YAOZ8J4cHQk)

![Image](https://cdn-media-1.freecodecamp.org/images/wjW6bJS4FWl1cZN1uBifZbaWTdl1xirUYkmf)

Félicitations si vous êtes arrivé jusqu'ici et que cela fonctionne ! Voici un bonus, un script bash simple que vous pouvez exécuter. Vous devez simplement changer le mot de passe lorsque c'est nécessaire.

**Script Bash 1**
_credits à_ [Adnan Rahić](https://medium.com/@adnanrahic?source=post_header_lockup)

```
#!/bin/bash
```

```
cd /path/to/VPNBook.com-OpenVPN-Euro1username="vpnbook"password="he2qv5h"read -sp "Enter Sudo Password: " sudopassword
```

```
/usr/bin/expect << EOF
```

```
spawn sudo openvpn vpnbook-euro1-tcp443.ovpnexpect "password for $USER: "send "$sudopassword\r"expect "Enter Auth Username: "send "$username\r"expect "Enter Auth Password: "send "$password\r"expect "$ "
```

```
EOF
```

> Cela démarrera le VPN sans avoir besoin de saisir manuellement le nom d'utilisateur et le mot de passe. Le VPN continuera également à fonctionner en arrière-plan. Voici un script pour l'arrêter si nécessaire.

```
#!/bin/bashsudo pkill vpn
```

**Script Bash 2**

```
#!/bin/bashecho "user: vpnbook"echo "pass: 5VHZEps"sudo openvpn vpnbook-ca1-tcp443.ovpn
```

Il suffit de mettre cela dans un nouveau fichier, clic droit > propriétés > permissions, et autoriser l'exécution du fichier en tant que programme. Cet exemple utilise la configuration tcp 443 du Canada.

### Lectures complémentaires

Voici quelques excellents articles de Quincy Larson qui parlent des VPN, de la vie privée sur Internet et de la sécurité.

[**Comment configurer un VPN en 10 minutes gratuitement (et pourquoi vous en avez urgemment besoin)**](https://medium.freecodecamp.com/how-to-set-up-a-vpn-in-5-minutes-for-free-and-why-you-urgently-need-one-d5cdba361907)
[_"Un ordinateur vous permet de faire plus d'erreurs plus rapidement que toute autre invention, avec les exceptions possibles des pistolets et de..._medium.freecodecamp.com](https://medium.freecodecamp.com/how-to-set-up-a-vpn-in-5-minutes-for-free-and-why-you-urgently-need-one-d5cdba361907)[**Comment chiffrer toute votre vie en moins d'une heure**](https://medium.freecodecamp.org/tor-signal-and-beyond-a-law-abiding-citizens-guide-to-privacy-1a593f2104c3)
[_"Seuls les paranoïaques survivent." — Andy Grove_medium.freecodecamp.org](https://medium.freecodecamp.org/tor-signal-and-beyond-a-law-abiding-citizens-guide-to-privacy-1a593f2104c3)

Si vous êtes intéressé par le hacking éthique et la sécurité, il y a un [cours gratuit de 15 heures](https://www.youtube.com/watch?v=vg9cNFPQFqM) sur YouTube.