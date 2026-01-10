---
title: Comment les cybercriminels piratent vos mots de passe (et comment rester une
  longueur d'avance)
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-05-19T13:59:12.071Z'
originalURL: https://freecodecamp.org/news/how-cybercriminals-crack-your-passwords-and-how-to-stay-one-step-ahead
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747663111032/84a5cdc6-3d13-49e9-bc65-f2b7d0a51ad9.png
tags:
- name: Security
  slug: security
- name: cybersecurity
  slug: cybersecurity
seo_title: Comment les cybercriminels piratent vos mots de passe (et comment rester
  une longueur d'avance)
seo_desc: "Passwords are the keys to your digital life  –  email, bank accounts, social\
  \ media, and even your workplace systems. Unfortunately, they’re also one of the\
  \ weakest links in cybersecurity. \nEvery year, billions of credentials are stolen\
  \ and sold on th..."
---

Les mots de passe sont les clés de votre vie numérique : e-mail, comptes bancaires, réseaux sociaux et même les systèmes de votre lieu de travail. Malheureusement, ils sont aussi l'un des maillons les plus faibles de la cybersécurité.

**Chaque année, des milliards d'identifiants sont volés et vendus sur le dark web.**

Les cybercriminels n'ont pas toujours besoin de techniques avancées pour pirater votre compte. Souvent, ils s'appuient sur des méthodes simples et automatisées qui exploitent les habitudes humaines, comme la réutilisation des mots de passe ou le choix de mots de passe prévisibles.

Voici cinq des méthodes les plus courantes utilisées par les attaquants pour craquer les mots de passe et comment vous pouvez vous protéger.

## **Attaques par force brute**

Les attaques par force brute sont l'une des plus anciennes techniques de piratage encore utilisées aujourd'hui.

Dans cette approche, les attaquants utilisent un programme informatique pour essayer toutes les combinaisons possibles de caractères jusqu'à trouver le bon mot de passe.

Bien que cela puisse sembler fastidieux, des outils comme Hydra, Medusa ou [John the Ripper](https://www.freecodecamp.org/news/crack-passwords-using-john-the-ripper-pentesting-tutorial/) peuvent tenter des milliers, voire des millions, de devinettes par seconde.

Par exemple, si votre mot de passe est "test123", un outil de force brute le craquera probablement en quelques secondes. Un mot de passe de 6 caractères avec uniquement des lettres minuscules a 308 millions de combinaisons possibles, que les GPU modernes peuvent traiter en quelques minutes ou moins.

Votre meilleure défense contre la force brute est la longueur et la complexité du mot de passe.

Un mot de passe aléatoire de 16 caractères avec des lettres majuscules et minuscules, des chiffres et des symboles est pratiquement immunisé contre les attaques par force brute avec le matériel actuel.

L'utilisation d'un gestionnaire de mots de passe comme NordPass, Bitwarden ou 1Password facilite la génération et le stockage de tels mots de passe et offre une [protection solide des mots de passe](https://nordpass.com/secure-password/).

## **Attaques par dictionnaire**

Contrairement à la force brute, une attaque par dictionnaire réduit l'espace de recherche en essayant des mots de passe à partir d'une liste précompilée de mots et de phrases couramment utilisés.

Ces listes incluent souvent des mots de passe divulgués lors de précédentes violations de données, des équipes sportives populaires, des motifs de clavier comme "qwerty" ou "123456", et même des noms ou des jurons. Elles sont également appelées [wordlists](https://www.freecodecamp.org/news/the-power-of-wordlists-why-every-ethical-hacker-needs-one/).

Beaucoup de gens croient à tort que modifier un mot de passe courant, par exemple en changeant "password" en "P@ssw0rd!", le rend sécurisé. Mais les outils d'attaque par dictionnaire tiennent compte de ces variations.

Par exemple, l'outil [Crunch](https://www.kali.org/tools/crunch/) permet aux attaquants de générer des wordlists avec des règles basées sur des motifs, ce qui signifie que "Welcome@123" reste une supposition probable.

"123456", "password" et "qwerty" sont toujours parmi les mots de passe les plus courants au monde. Même des mots de passe comme "iloveyou" et "dragon" apparaissent régulièrement.

Pour vous protéger, n'utilisez jamais de mots réels, de noms ou de motifs prévisibles dans vos mots de passe. Essayez plutôt d'utiliser des phrases de passe longues, aléatoires et uniques, comme "camion-oreiller-café-skyline" ou une chaîne complètement aléatoire comme "g6D@!rXplQ8#1zVn".

Encore une fois, un gestionnaire de mots de passe est le moyen le plus simple de maintenir ce niveau d'aléatoire et d'unicité.

## **Bourrage d'identifiants (Credential Stuffing)**

Le bourrage d'identifiants est l'une des méthodes d'attaque les plus réussies et les moins sophistiquées. Il exploite un fait simple : les gens réutilisent les mots de passe sur plusieurs comptes.

Lorsque des sites comme LinkedIn ou Dropbox sont piratés et que les mots de passe fuient en ligne, les attaquants prennent ces identifiants volés et les essaient sur d'autres sites web : votre e-mail, Facebook, Netflix, ou même les portails bancaires.

Cette technique est hautement automatisée. Les attaquants utilisent des bots pour tester des milliers de combinaisons nom d'utilisateur-mot de passe sur des dizaines de sites jusqu'à trouver une correspondance.

Supposons que vous ayez utilisé votre mot de passe Gmail pour vous inscrire sur un petit forum il y a des années. Ce forum est piraté, et vos détails de connexion sont exposés. Si vous utilisez toujours ce même mot de passe sur Gmail, les attaquants ont maintenant une clé pour votre boîte de réception, ce qui signifie qu'ils peuvent également accéder à tous vos autres comptes via les liens de réinitialisation de mot de passe.

Pour vous défendre contre le bourrage d'identifiants, utilisez un mot de passe unique pour chaque compte. Vous n'avez pas besoin de tous les mémoriser : utilisez simplement un gestionnaire de mots de passe réputé.

Activez également l'authentification multifactorielle (MFA) partout où c'est possible, afin que même si quelqu'un a votre mot de passe, il ne puisse pas se connecter sans le deuxième facteur.

## **Attaques par hameçonnage (Phishing)**

L'hameçonnage n'est pas une exploitation technique, c'est une exploitation psychologique.

Au lieu de deviner votre mot de passe, les attaquants vous trompent pour que vous le donniez.

Le [phishing](https://www.freecodecamp.org/news/how-to-recognize-phishing-email/) se présente souvent sous la forme de faux e-mails, messages texte ou sites web qui semblent légitimes mais sont conçus pour voler vos identifiants.

Par exemple, vous pourriez recevoir un e-mail qui semble provenir de votre banque, vous demandant de "vérifier votre compte". Le lien vous mène à une fausse page de connexion qui capture votre nom d'utilisateur et votre mot de passe dès que vous les entrez.

Des outils comme Evilginx et Modlishka peuvent même contourner la MFA en interceptant les jetons en temps réel.

Le phishing est répandu parce qu'il fonctionne. Selon la [CISA](https://www.cisa.gov/), le phishing était le vecteur d'attaque initial le plus courant en 2022. Et il devient de plus en plus convaincant avec l'utilisation de l'IA pour rédiger des e-mails, usurper des adresses d'expéditeur et créer des sites web réalistes.

Pour rester en sécurité, ne cliquez jamais sur des liens suspects ou n'entrez pas vos identifiants sur un site que vous avez atteint via un e-mail. Tapez toujours les URL manuellement ou utilisez les favoris du navigateur pour les sites sensibles comme les banques ou les e-mails.

Entraînez-vous à repérer les signaux d'alerte, comme une mauvaise grammaire, un sentiment d'urgence ou des noms d'expéditeur qui ne correspondent pas.

## **Ingénierie sociale et réinitialisation de mot de passe**

Parfois, les pirates n'ont pas besoin de compétences techniques du tout, ils doivent simplement être convaincants.

L'[ingénierie sociale](https://www.freecodecamp.org/news/modern-social-engineering-cyberattacks/) consiste à manipuler les personnes pour qu'elles divulguent des informations confidentielles. Une tactique courante consiste à appeler le service client en prétendant être vous. Si le représentant n'est pas prudent, il pourrait réinitialiser votre mot de passe ou donner accès à votre compte.

C'est exactement ce qui est arrivé au [journaliste technologique Mat Honan en 2012](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/), lorsque des pirates ont utilisé l'ingénierie sociale pour prendre le contrôle de son compte Apple. Ils l'ont ensuite utilisé pour effacer son téléphone, le bloquer de son e-mail et accéder à d'autres services connectés.

Une autre astuce consiste à exploiter les systèmes de réinitialisation de mot de passe faibles. Si un service vous permet de réinitialiser votre mot de passe en répondant à des questions comme "Quel est le nom de votre animal de compagnie ?" ou "Où êtes-vous né ?", les attaquants peuvent déjà connaître les réponses grâce à vos réseaux sociaux ou à des fuites de données.

Pour éviter ce risque, limitez les informations personnelles que vous partagez en ligne.

Utilisez de fausses réponses pour les questions de réinitialisation de mot de passe et stockez-les dans votre gestionnaire de mots de passe.

Et partout où c'est possible, activez l'authentification à deux facteurs en utilisant une application comme Authy ou Google Authenticator au lieu de vous fier aux SMS, qui peuvent être interceptés via le swap de SIM.

## **La défense est plus facile que la récupération**

Les cybercriminels n'ont pas toujours besoin de "pirater" pour entrer, ils ont juste besoin que vous fassiez une erreur.

La bonne nouvelle est que la plupart des attaques de mots de passe reposent sur des erreurs humaines et des habitudes prévisibles. En utilisant un gestionnaire de mots de passe, en activant l'authentification multifactorielle et en restant vigilant face aux tentatives de phishing, vous pouvez bloquer presque toutes ces menaces.

Considérez votre vie numérique comme une maison. Utiliseriez-vous la même clé pour votre maison, votre voiture, votre bureau et votre casier ? La laisseriez-vous sous le tapis ? C'est exactement ce que font les mots de passe faibles ou réutilisés en ligne.

Restez une longueur d'avance. Verrouillez correctement vos portes numériques et ne donnez pas la clé aux attaquants.

Rejoignez la [**Newsletter Stealth Security**](https://newsletter.stealthsecurity.sh/) pour plus d'articles sur la cybersécurité.