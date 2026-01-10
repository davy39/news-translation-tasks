---
title: Bureaux d'enregistrement de domaines, DNS et hébergement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-05T23:59:44.000Z'
originalURL: https://freecodecamp.org/news/domain-registrars-dns-and-hosting-353e4163a19
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KBhZGtrJX3Xiq6P28mkXMw.jpeg
tags:
- name: marketing
  slug: marketing
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Bureaux d'enregistrement de domaines, DNS et hébergement
seo_desc: 'By ᴋɪʀʙʏ ᴋᴏʜʟᴍᴏʀɢᴇɴ

  How to set up your website the right way

  It took me a while to set up the infrastructure that runs my website and email in
  a way that made me happy. There are a lot of crappy domain registrars, DNS providers,
  and web hosts out the...'
---

Par  

#### Comment configurer votre site web de la bonne manière

Il m'a fallu un certain temps pour configurer l'infrastructure qui fait tourner mon site web et mes emails d'une manière qui me rende heureux. Il y a beaucoup de bureaux d'enregistrement de domaines, de fournisseurs DNS et d'hébergeurs web médiocres. Je suis enfin à un stade où je suis satisfait de chaque composant de mon pipeline, alors j'ai pensé partager ma configuration avec le monde.

### Namecheap

À l'époque, comme beaucoup d'autres personnes, j'utilisais GoDaddy comme mon principal bureau d'enregistrement de domaines. J'ai rapidement appris que GoDaddy dépense tout son argent dans des [**publicités tape-à-l'œil**](http://fortune.com/2015/03/30/godaddy-ads-ipo/) au lieu d'embaucher des ingénieurs UX ou des chefs de produit. Leur équipe de support était également médiocre pendant mon passage là-bas.

De nos jours, j'utilise uniquement [**Namecheap**](http://www.namecheap.com/?aff=90584) pour mes besoins en domaines. Namecheap est de loin la meilleure interface que j'ai trouvée pour gérer les domaines et elle s'améliore à chaque fois que je l'utilise. Ils ont également toujours de bonnes affaires sur les [**nouveaux TLD**](https://www.namecheap.com/domains/new-tlds/explore.aspx?aff=90584) et la recherche d'un domaine sur leur site est toujours une expérience fantastique.

### CloudFlare

Chaque bureau d'enregistrement de domaines vous fournira la possibilité de configurer vos paramètres DNS pour votre domaine, mais aucun service de serveur de noms gratuit ne peut vraiment comparer à [**CloudFlare**](https://www.cloudflare.com/). Je ne veux pas passer trop de temps à expliquer toutes les choses incroyables que CloudFlare peut faire pour vous car [**cette vidéo**](https://vimeo.com/14700285) le fait déjà de manière incroyable.

Si vous avez regardé cette vidéo, alors vous connaissez beaucoup des fonctionnalités géniales que CloudFlare offre à ses utilisateurs gratuitement. Ma fonctionnalité absolument préférée, cependant, est étrangement dé-emphasisée sur le site de CloudFlare. La raison numéro un pour laquelle j'utilise CloudFlare est parce que [**je n'ai jamais à attendre la propagation du DNS**](https://blog.cloudflare.com/never-deal-with-dns-propagation-again/).

### GitHub Pages

Héberger un site web peut également être assez pénible. Si vous avez juste besoin d'héberger un site web statique, alors il n'y a [**aucune raison**](https://google.com/search?q=free+static+website+hosting) de payer pour l'hébergement. Ma solution personnelle préférée est [**GitHub Pages**](https://pages.github.com/). J'utilise déjà _git_ pour gérer mon site web, donc GitHub Pages rend la mise à jour de mon site web aussi simple que _git push_. Plus de FTP, SSH, ou tout autre acronyme de trois lettres.

### Installation

À ce stade, vous devriez avoir une bonne vue d'ensemble de haut niveau sur la façon de configurer votre site web, mais il peut y avoir des détails de mise en œuvre qui rendent encore difficile la connexion des points. Voici toutes les étapes que vous devez suivre pour utiliser les services ci-dessus :

#### 1. Obtenez votre domaine sur Namecheap.

Peu importe si vous l'achetez directement ou si vous le transférez, mais obtenez votre domaine sur Namecheap.

#### **2. Ajoutez votre site à CloudFlare.**

Sur CloudFlare, ajoutez votre site, analysez les enregistrements DNS actuels et sélectionnez le plan gratuit. Une fois que vous avez fait cela, vous serez invité avec deux adresses de serveurs de noms. Enregistrez-les pour l'étape suivante.

#### **3. Pointez Namecheap vers CloudFlare.**

Retournez à Namecheap, cliquez sur le bouton "Gérer" correspondant à votre domaine depuis la page principale "Tableau de bord". Sous la section "Serveurs de noms", cliquez sur "Namecheap Basic DNS", puis sélectionnez "DNS personnalisé". À partir de là, entrez les deux serveurs de noms que vous avez obtenus de CloudFlare et cliquez sur la coche verte.

#### **4. Vérifiez les serveurs de noms.**

Super, retournez maintenant à votre site sur CloudFlare et cliquez sur "Recheck Nameservers". Cela peut prendre jusqu'à 24 heures, mais souvent (surtout avec Namecheap) cela ne prend que quelques minutes.

#### 5. Configurez GitHub Pages.

Rendez-vous sur GitHub et créez un [**nouveau dépôt**](https://github.com/new) appelé _username_.github.io, où _username_ est votre nom d'utilisateur sur GitHub. À partir de là, vous pouvez pousser votre site web statique avec les commandes suivantes :

```
# depuis le répertoire de votre site web sur votre machine locale
$ git init
$ git add .
$ git commit -m 'Initial commit'
```

```
# remplacez "<remote-url>" par l'URL sur la page de votre dépôt sur GitHub
$ git remote add origin <remote-url>
$ git push -u origin master
```

#### 6. Pointez votre DNS vers GitHub Pages.

Vous pouvez maintenant retourner à votre site sur CloudFlare et cliquer sur "DNS" en haut. À partir de là, vous allez vouloir ajouter un enregistrement CNAME. La première valeur (nom) sera "@" et la deuxième valeur (nom de domaine) sera _username_.github.io, où username est votre nom d'utilisateur sur GitHub.

Sauf si vous avez des sous-domaines ou d'autres circonstances spéciales, vous pouvez supprimer tous les autres enregistrements CNAME ou A de CloudFlare. Juste pour être sûr, je vous suggère de sauvegarder vos enregistrements DNS en cliquant sur "Avancé" et "Exporter".

Personnellement, je n'aime pas le "www" qui préfixe beaucoup de domaines. Je me débarrasse de cela en ajoutant un autre enregistrement CNAME avec la première valeur "www" et la deuxième valeur _username_.github.io, où username est votre nom d'utilisateur sur GitHub.

#### 7. Ajoutez un fichier CNAME sur GitHub.

La dernière étape de ce processus est d'informer GitHub Pages de notre domaine. Nous faisons cela en ajoutant un fichier appelé "CNAME" au répertoire racine du dépôt de notre site web sur GitHub. Pour ce faire, exécutez les commandes suivantes :

```
# depuis le répertoire de votre site web sur votre machine locale
```

```
$ echo "<my-domain>" > CNAME # où "<my-domain>" est votre domaine
$ git add CNAME
$ git commit -m 'Add CNAME'
$ git push origin master
```

Si vous avez trouvé cet article utile ou si vous avez des recommandations, n'hésitez pas à poster une réponse ici.

Suivez-moi sur Twitter [ici](https://www.twitter.com/_kirbyk).