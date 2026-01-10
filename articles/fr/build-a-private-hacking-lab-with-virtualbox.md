---
title: Comment construire votre propre laboratoire de piratage privé avec VirtualBox
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-10-24T15:11:30.544Z'
originalURL: https://freecodecamp.org/news/build-a-private-hacking-lab-with-virtualbox
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729751281544/6500642d-4c1e-4dba-b5d0-ab97f9f10003.jpeg
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: Security
  slug: security
- name: ethicalhacking
  slug: ethicalhacking
- name: 'VirtualBox '
  slug: virtualbox
seo_title: Comment construire votre propre laboratoire de piratage privé avec VirtualBox
seo_desc: 'Ethical hacking involves testing and finding vulnerabilities in systems.
  But doing this on live networks or public servers can lead to accidental damage.

  Setting up a virtual lab for hacking is a great way to sharpen your skills in a
  safe environment...'
---

Le piratage éthique implique de tester et de trouver des vulnérabilités dans les systèmes. Mais le faire sur des réseaux en direct ou des serveurs publics peut entraîner des dommages accidentels.

Configurer un laboratoire virtuel pour le piratage est un excellent moyen d'affûter vos compétences dans un environnement sûr. Un laboratoire privé garantit que toutes vos activités restent isolées, il n'y a donc aucun risque d'endommager des systèmes réels ou de violer des limites légales. Il vous permet de faire des erreurs et d'apprendre d'elles sans causer de tort.

## Configuration du projet

Ce guide vous apprendra à configurer votre propre laboratoire privé. Pour ce faire, nous aurons besoin de trois choses :

* Logiciel de virtualisation

* Machine d'attaque

* Machine cible

Le logiciel de virtualisation permet à un ordinateur physique d'exécuter plusieurs machines virtuelles (VM). Une machine virtuelle agit comme un ordinateur séparé avec son propre système d'exploitation et ses programmes, mais fonctionne sur le même matériel que l'ordinateur hôte.

VirtualBox est un logiciel de virtualisation populaire. VMware est une autre alternative.

Pour pratiquer le piratage, vous avez besoin de deux machines : une machine d'attaque et une machine cible.

Vous pouvez utiliser votre propre système comme machine d'attaque. Mais il est préférable d'utiliser une machine comme [Kali](https://www.kali.org/) ou [Parrot](https://parrotsec.org/) qui vient préinstallée avec tous les outils dont vous aurez besoin.

Pour la machine cible, nous pouvons utiliser un dépôt comme Vulnhub. Il contient plusieurs VM conçues pour que vous puissiez pratiquer vos compétences. Chacune est conçue pour avoir une vulnérabilité que vous pouvez pratiquer à exploiter.

Les téléchargements nécessaires pour cette configuration sont assez volumineux, je vous recommande donc de les télécharger et de les garder prêts.

* [Télécharger VirtualBox](https://www.virtualbox.org/wiki/Downloads) (téléchargez également le pack d'extension)

* [Télécharger Kali](https://www.kali.org/get-kali/#kali-virtual-machines) (image Virtualbox 64 bits)

* [Télécharger la machine vulnérable Mr Robot](https://www.vulnhub.com/entry/mr-robot-1,151/)

Commençons 449

## Comment installer VirtualBox

Pour télécharger VirtualBox, rendez-vous sur la [page de téléchargements](https://www.virtualbox.org/wiki/Downloads). Selon votre système d'exploitation, téléchargez le package et installez-le.

Une fois l'installation terminée, vous devriez voir une page similaire selon votre système d'exploitation.

![Accueil Virtualbox](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751323730/84912f77-6c90-49d0-8b07-b856247b3723.png align="center")

Double-cliquez sur le pack d'extension et assurez-vous qu'il est également installé.

## Comment installer Kali Linux

Maintenant, installons notre machine d'attaque. Extrayez le fichier .7z du téléchargement de Kali Linux. Ensuite, cliquez sur l'icône verte "Ajouter" sur l'interface de VirtualBox et pointez vers le fichier .vbox.

![Fichier .vbox de Kali Linux](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751345791/f84dd422-e99c-4c6d-b2e5-2381cf12933c.png align="center")

Tous les paramètres par défaut seront appliqués et vous devriez avoir la machine d'attaque installée. Si vous êtes bloqué, vous pouvez [trouver des instructions détaillées ici](https://www.kali.org/docs/virtualization/import-premade-virtualbox/).

Ne démarrez pas encore la machine. Ajoutons également la machine cible, suivi de la modification de quelques paramètres de réseau. Ensuite, nous pourrons commencer le piratage.

## Comment installer une machine cible VM

Maintenant, installons la cible. Double-cliquez sur le fichier `mrRobot.ova` téléchargé. Utilisez les paramètres par défaut et cliquez sur "Terminer".

![Machine cible Mr Robot VM](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751365289/a3ce9b1c-7daa-4a16-959b-139d4239bae2.png align="center")

Une fois les machines d'attaque et cible configurées, vous devriez les voir toutes les deux dans la liste des machines.

![Accueil Virtualbox avec machines d'attaque et cible](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751388993/7c3510bb-0d9d-42b7-bdec-68a70b09b7d4.png align="center")

Maintenant, mettons à jour les paramètres de réseau pour nous assurer que nos VM sont sécurisées.

## Mettre à jour les paramètres de réseau

Il existe de nombreuses façons de configurer un réseau dans VirtualBox. Mais dans notre cas, nous voulons isoler notre laboratoire de l'internet public. La meilleure façon de faire cela est de configurer un réseau hôte uniquement.

Dans un réseau hôte uniquement, les VM peuvent communiquer entre elles mais pas avec l'internet public. Configurons-le.

Dans l'interface de Virtualbox, cliquez sur "Outils" et cliquez sur "Réseaux hôte uniquement". Ensuite, cliquez sur "Créer". Il créera automatiquement un réseau hôte uniquement avec une plage d'IP. Pour simplifier, changeons le nom du réseau en "MyHackingLabNetwork".

![Réseau hôte uniquement Virtualbox](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751416579/0f16b374-33d0-444d-8d09-1edd22b389c1.png align="center")

Cliquez sur "Appliquer". Maintenant, nous avons un réseau hôte uniquement. Ensuite, configurons nos machines virtuelles pour qu'elles se connectent à ce réseau.

Cliquez sur la machine virtuelle et cliquez sur l'icône "Paramètres". Sous "Réseau", choisissez "réseau hôte uniquement" et choisissez le nom "MyHackingLabNetwork". Cliquez sur "OK" une fois terminé.

![Paramètres réseau Virtualbox](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751437795/c700b9be-0885-45fc-b0d1-70a6227167fa.png align="center")

Faites de même pour la machine cible. Les adresses IP de ces machines virtuelles seront automatiquement attribuées par notre réseau "hôte uniquement".

## Scanning de la cible

Maintenant, nous sommes prêts à commencer. Allumez les deux machines.

**Note :** Les deux machines afficheront une option par défaut pour démarrer – appuyez simplement sur Entrée. Si la VM semble petite sur votre écran, cliquez sur Affichage -> Mode mis à l'échelle dans le menu supérieur.

Le nom d'utilisateur et le mot de passe pour la machine Kali sont "kali".

Vous devriez voir l'interface utilisateur de Kali Linux comme ci-dessous.

![Accueil Kali](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751456625/e63b0190-2e8d-481b-903f-faac4c2fec3f.png align="center")

Pour la boîte Mr.Robot, vous devriez voir l'interface utilisateur suivante :

![Accueil cible](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751469522/71ce0dcd-595c-4f67-8ff4-716ffb1e8216.png align="center")

Maintenant, trouvons les adresses IP de ces machines.

Dans Kali, ouvrez un terminal et tapez `ifconfig | grep inet`.

![Affichage réseau](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751487309/6ec69770-ead6-44f0-a590-7a6afb563614.png align="center")

Vous devriez voir une adresse IP similaire à 192.168.56.x. C'est l'IP de la machine cible.

Maintenant, utilisons nmap pour scanner d'autres machines dans ce réseau. Si vous ne savez pas ce qu'est Nmap, [voici un tutoriel](https://www.stealthsecurity.sh/p/nmap-tutorial).

Faisons un scan ping depuis Kali pour rechercher d'autres machines dans le réseau. Exécutez la commande suivante :

```plaintext
nmap -sn 192.168.56.0/24
```

Cette commande ping toutes les adresses IP de `192.168.56.1` à `192.168.56.254` pour voir ce qui est en cours d'exécution. Vous devriez voir trois résultats similaires.

![Scan ping Nmap](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751508093/204e5805-3b1e-485b-8e2e-bece23c3d781.png align="center")

Le premier résultat est généralement l'IP de l'adaptateur. Nous pouvons donc l'ignorer. Parmi les deux autres, l'une est l'IP de notre machine d'attaque. Nous nous intéressons à la troisième. Dans ce cas, c'est 192.168.56.3.

Faisons un scan de version de service de cette IP et voyons ce qui apparaît.

```plaintext
nmap -sV 192.168.56.3
```

Vous devriez voir un résultat similaire à celui ci-dessous si vous scannez la machine virtuelle Mr.Robot :

![Scan de version de service Nmap](https://cdn.hashnode.com/res/hashnode/image/upload/v1729751531886/bf6eec03-4393-4610-84ff-61dceb24edcc.png align="center")

L'image ci-dessus montre qu'il y a trois ports sur le serveur. L'un d'eux est ssh, qui est fermé. Les deux autres sont des ports de serveur web – 80 pour http et 443 pour https.

## Conclusion

Félicitations ! Vous avez réussi à configurer votre propre laboratoire de piratage en utilisant VMware. Ce laboratoire vous offre la flexibilité de pratiquer le piratage éthique dans un environnement contrôlé et isolé.

Pour plus de tutoriels gratuits sur la cybersécurité, [inscrivez-vous à notre newsletter](https://www.stealthsecurity.sh/). Pour apprendre à pirater la boîte Mr.Robot et d'autres, rejoignez notre communauté privée [Hacker's Hub](https://www.skool.com/hackershub). Si vous débutez en cybersécurité, consultez le [Hacker's Handbook](https://book.stealthsecurity.sh/).

À bientôt avec un autre article.