---
title: Comment suivre rapidement l'accès aux PDF sur un serveur web Linux
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-12-02T17:17:52.000Z'
originalURL: https://freecodecamp.org/news/quickly-track-pdf-access-linux-web-server
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/calculator.jpg
tags:
- name: analytics
  slug: analytics
- name: Google Analytics
  slug: google-analytics
- name: Linux
  slug: linux
- name: metrics
  slug: metrics
- name: pdf
  slug: pdf
seo_title: Comment suivre rapidement l'accès aux PDF sur un serveur web Linux
seo_desc: 'Is it possible to track how many times your website''s users click to download
  binary files like PDFs or JPGs? Yes it is possible. Is it easy? I didn''t originally
  think so. I was wrong.

  The story began while I was optimizing a landing page on my Boots...'
---

Est-il possible de suivre le nombre de fois où les utilisateurs de votre site web cliquent pour télécharger des fichiers binaires comme des PDF ou des JPG ? Oui, c'est possible. Est-ce facile ? Je ne le pensais pas au début. Je me trompais.

L'histoire a commencé alors que j'optimisais une page de destination sur mon site [Bootstrap IT](https://bootstrap-it.com/davidclinton/keeping-up) pour mon nouveau livre, *Keeping Up: Backgrounders to all the big technology trends you can't afford to miss*.

Je voulais donner accès au fichier PDF d'un chapitre d'exemple du livre. Mais je voulais aussi un moyen de savoir combien de personnes l'avaient réellement téléchargé.

Faisons un pas en arrière. [Google Analytics](https://analytics.google.com/analytics/web/) est un service gratuit qui utilise des extraits de code insérés dans vos fichiers HTML pour collecter et afficher des données sur la fréquence d'accès à vos fichiers.

La magie - et le problème - de Google Analytics réside dans la quantité d'informations sur vos utilisateurs qui peut être révélée. J'ai discuté de certaines des préoccupations en matière de confidentialité liées à ce service dans le livre Keeping Up. J'ai également mentionné comment je me sens au moins un peu coupable d'utiliser ce service moi-même sur mes propres sites.

En tout cas, à lui seul, Google Analytics n'est pas en mesure de vous dire grand-chose sur la manière dont vos PDF basés sur le web sont utilisés. Bien sûr, il existe des astuces pour contourner le problème.

Les approches traditionnelles incluent la configuration du [Google Tag Manager](https://marketingplatform.google.com/about/tag-manager/), la personnalisation de la syntaxe des URL de requête que vous utilisez ou, si votre site utilise le logiciel WordPress, le travail avec le [plugin Monster Insights](https://www.monsterinsights.com/). Chacune de ces méthodes peut fonctionner, mais nécessitera une courbe d'apprentissage assez raide.

Mais je suis un administrateur système Linux. Et, comme je ne manque jamais de le rappeler aux gens qui m'entourent, les meilleurs administrateurs système sont paresseux. Courbe d'apprentissage ? Cela ressemble étrangement à du travail. Pas question que cela arrive sous ma surveillance.

Voici donc l'affaire. Mon serveur web, évidemment, fonctionne sous Linux. Et, sous le capot, le trafic HTTP est géré par Apache. Cela signifie que tout ce qui se passe sur mes sites web sera enregistré par Apache.

Tout. Il ne faudra qu'une seule ligne de Bash exécutée depuis ma station de travail locale pour me donner ce que je dois savoir sur ce que mon chapitre d'exemple PDF a fait :

```
echo "cd /var/log/apache2 && grep -nr KeepingUpSampleChapter" \
   | ssh -i PrivateKey.pem LoginName@bootstrap-it.com

```

Décortiquons cela. La première des deux commandes entre guillemets (`cd /var/log/apache2`) nous déplacera vers le répertoire /var/log/apache2/ sur le serveur Linux où Apache écrit ses journaux. Ce n'est pas de la science-fiction.

Il y aura plusieurs fichiers d'intérêt dans ce répertoire. Cela est dû au fait que les messages pertinents pour l'accès régulier et les erreurs sont enregistrés dans différents fichiers, et parce que les politiques de rotation des fichiers signifient qu'il pourrait y avoir plus d'une version de chacun de ces fichiers. Je vais donc utiliser `grep` pour rechercher dans tous les fichiers non compressés la chaîne `KeepingUpSampleChapter`. `KeepingUpSampleChapter` fait, bien sûr, partie du nom de fichier du PDF.

Je transmets ensuite cette commande à SSH, qui se connectera à mon serveur distant et exécutera la commande. Voici à quoi ressemblerait une seule entrée après une exécution réussie (j'ai supprimé l'adresse IP du demandeur pour des raisons de confidentialité) :

```
other_vhosts_access.log.1:12200:bootstrap-it.com:443 <adresse IP du demandeur> - - [01/Déc/2020:16:39:36 -0500] "GET /davidclinton/KeepingUpSampleChapter.pdf?pdf=SamplePDF HTTP/1.1" 200 65146 "https://bootstrap-it.com/davidclinton/keeping-up/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

```

Nous pouvons voir :

* Le fichier journal où l'entrée est apparue (`other_vhosts_access.log.1`)
* L'adresse IP du demandeur (masquée)
* Le timestamp nous indiquant exactement quand le fichier a été accédé
* L'emplacement relatif du fichier sur le système de fichiers du serveur (`/davidclinton/KeepingUpSampleChapter.pdf`)
* L'URL à partir de laquelle la requête a été faite (`https://bootstrap-it.com/davidclinton/keeping-up/`)
* Et le navigateur que l'utilisateur utilisait

C'est beaucoup d'informations. Si nous sommes simplement curieux de savoir combien de *fois* le fichier a été téléchargé, nous pouvons simplement transmettre la sortie à la commande `wc` qui nous dira trois choses sur la sortie : le nombre de lignes, de mots et de caractères qu'elle contenait. Cette commande ressemblerait à ceci :

```
echo "cd /var/log/apache2 && grep -nr KeepingUpSampleChapter | wc" \
   | ssh -i PrivateKey.pem LoginName@bootstrap-it.com

```

Il y a une limitation possible avec cette méthode. Si votre site web est très fréquenté, les fichiers journaux seront souvent renouvelés, souvent plus d'une fois par jour. Par défaut, après le premier renouvellement, les fichiers sont compressés à l'aide de l'algorithme `gz`, qui ne peut pas être lu par `grep`.

La commande `zgrep` n'aura aucun problème à gérer de tels fichiers, mais le processus pourrait finir par prendre beaucoup de temps. Vous pourriez envisager d'écrire un simple script personnalisé pour décompresser chaque fichier `gz` puis exécuter `grep` contre son contenu. Ce sera votre projet.

*Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com/davidclinton).*