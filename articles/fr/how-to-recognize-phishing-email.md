---
title: Comment reconnaître un e-mail de phishing – Et que faire quand vous en recevez
  un
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-10-12T00:52:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-recognize-phishing-email
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725458523382/ab4b959e-8c84-4e48-88a5-bbc716255d1b.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: phishing
  slug: phishing
seo_title: Comment reconnaître un e-mail de phishing – Et que faire quand vous en
  recevez un
seo_desc: 'You know the drill: you open your email client and there is it an email
  saying that you will be in trouble if you do not follow certain instructions in
  short time, no questions asked.

  All it takes is a single click, and you''re in trouble.

  This kind o...'
---

Vous connaissez la chanson : vous ouvrez votre client de messagerie et vous y trouvez un e-mail affirmant que vous aurez des ennuis si vous ne suivez pas certaines instructions dans un délai court, sans poser de questions.

Un seul clic suffit, et vous voilà dans l'embarras.

Ce type d'e-mail a une [définition très claire](https://www.phishing.org/what-is-phishing) :

> Le [Phishing](https://www.knowbe4.com/phishing?hsLang=en) (ou hameçonnage) est un [cybercrime](https://www.merriam-webster.com/dictionary/cybercrime) dans lequel une ou plusieurs cibles sont contactées par e-mail, téléphone ou SMS par une personne se faisant passer pour une institution légitime afin d'inciter les individus à fournir des données sensibles telles que des informations d'identification personnelle, des coordonnées bancaires et de carte de crédit, ainsi que des mots de passe.

Dans cet article, j'expliquerai ce qu'est le phishing et comment reconnaître les signes indiquant qu'un e-mail n'est peut-être pas légitime. Pour cela, nous apprendrons à faire ce qui suit :

* Reconnaître certains signaux d'alerte évidents d'un e-mail de phishing
    
* Utiliser certains outils en ligne de commande sur Linux pour inspecter soigneusement les liens suspects
    
* Analyser les e-mails suspects avec plusieurs outils en ligne gratuits
    

Tout cela en s'amusant un peu.

## Exemple d'un e-mail de phishing

Laissez-moi partager un exemple d'e-mail assez astucieux (certains détails ont été modifiés pour protéger les innocents) :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/godaddy_phishing_emails.png align="left")

*E-mail de phishing se faisant passer pour GoDaddy*

Laissez-moi vous montrer comment repérer rapidement les escrocs, sans utiliser une seule ligne de code.

Vous aurez besoin des éléments suivants pour suivre certaines étapes de ce tutoriel :

* Une installation Linux, avec [curl](https://curl.se/) installé.
    
* Un navigateur Web (Brave ou Firefox sont de bons choix)
    
* **De la curiosité**
    

Maintenant, passons à la suite et voyons ce que nous avons dans notre boîte aux lettres...

## Signaux d'alerte de phishing basés sur le bon sens

D'emblée, cet e-mail viole deux règles simples, bien qu'il ait une grammaire correcte et une belle présentation :

Premièrement, il **vous force à agir immédiatement pour résoudre un problème** (Action urgente requise), **sans poser de questions** (Cliquez sur le joli bouton).

Pour aggraver les choses, il n'y a aucun moyen de vérifier que la personne qui vous contacte travaille réellement pour l'entreprise. Les entreprises réputées vous demandent de vous connecter à leur site Web et vous proposent un n° de dossier afin que vous puissiez suivre le problème. Aucun de ces éléments n'est présent ici.

Deuxièmement, malgré leurs meilleurs efforts, **les escrocs commettent des erreurs qualitatives**. Voyez-vous ce *n° client* en haut à droite de la capture d'écran ? Je l'ai comparé au mien sur le vrai site Web et devinez quoi ? C'est un numéro différent.

Mais où est le plaisir d'analyser cela si nous ne pouvons pas fouiner un peu ? Eh bien, quand j'ai passé ma souris sur l'image du bouton, j'ai pu voir le lien et il pointait vers une Tiny URL (un service de réduction d'URL) :

```python
https://tinyurl.com/xszszasxdxdxdxdxdxdxdzs?a=xxx@xxxx.com
```

Ainsi, celui qui fait cela essaie de dissimuler la véritable URL. Pas de problème, copiez l'adresse URL (**ne cliquez jamais dessus**), remplacez la partie e-mail de la requête GET par n'importe quoi (?a=xxx@xxx.com) puis exécutez-la via curl. J'ai obtenu ceci :

```html
<table width="75%" bgcolor="#FFFFFF" align="center" cellpadding="10">
        <tr>
            <td>
                <h2>URL résiliée</h2>
                <p>
                    Le TinyURL (xszszasxdxdxdxdxdxdxdzs) que vous avez visité a été utilisé par son créateur en violation de nos conditions d'utilisation.
                    TinyURL a une politique stricte contre les abus et nous nous excusons pour l'intrusion que cet utilisateur vous a causée.
                    De telles violations de nos conditions d'utilisation incluent :
                </p>
                <ul>
                    <li>Spam - E-mail de masse non sollicité</li>
                    <li>Fraude ou escroqueries financières</li>
                    <li>Malware</li>
                    <li>ou toute autre utilisation illégale.</li>
                </ul>
                <p>
```

Ainsi, les bonnes personnes de Tiny URL l'ont remarqué aussi et ont résilié l'URL. Beau travail !

[![asciicast](https://asciinema.org/a/526911.svg align="left")](https://asciinema.org/a/526911)

Utilisons d'autres outils pour confirmer ce que nous savons déjà.

## Outils en ligne pour analyser les URL suspectes

Tiny URL a eu la gentillesse de nous indiquer l'URL d'origine :

```text
https://parasolhealth.org/resources/sass/hgjhgbgb/%20hxghxhgcgzvzvhgxvgzhxgvvgvcgvhgvjhvxhgvzhgvshgvhgvhgvhgwvhgwvhgwvhgwvhgvhgvdshvshgvhgvhgdvhgdsvhgdvhjgdvjhdgdvhgfvhgvf/vhgvjhgvghgvghvhgvghvhgvjlnkjndkjdkjdhbgytdvghdvhvshgvshgvjsvhvahgvhvwgvhwvhvajgvsgshgvhsgvjhsvgavjgvsgvahgvahgvhgsvjgavhgsvhgsvhjvshgvahgvsjvshgvajvshvhgwvhgvehgvehgvehjvegvejhgvhgavhavhs/dhbjhjfhjfkbkjfhbjkbfjbjdbkjbsjhbdjbjkdbhbdjkbjdbjdbjhbdkjbsjbjkdbjkdhbjdbjbsjhbsjbjdkbjhdbkjhbdkjbsbdjbjdbkjhbjhbsjkhbdjbjdbjdbjhsbjhbejhbejhbjwhbjhwbjkwhbjbhbs/jdbhdhdbkjbsjbsjbwjbjwbjkbwhbehbjhbejbebebjebjbejbjhbsjhbshbahbjhsbshbjkhdbjhbjhbdbdjkbdhbjhsbjhbajhbsjbkjshbhbdjhbjdhbjkbshbsjhbsjbdbdhbdhbjehbjhebjhbrrhbjbjekhbjhbjsbjhsbjhbdjhd/jbdjhbdkjbdjhbkjabjhbsjbdjbksjbhsbjhdbjhbjkbdjhbjhbkjbejhbwkhbjkwhbjhwbjkwhbjhwbjhbwhbwkjhbwjhbjhbajhbajhbsjhbsjhbdjkhbdjhbdjhbjdhbjshbjhsbjhbjhsbkjhbdjhbsjbjabjhabjkbs/redirect.php
```

Si vous allez sur le site Virus Total et recherchez l'URL, vous verrez que cela [a également été signalé ici](https://www.virustotal.com/gui/url/1a5a1a3385c2d6c2c76b0ca721138ba9eeae7b8a12cc6e28c206216c103c3fc3?nocache=1) :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/godaddy_virustotal_malicious.png align="left")

Fait intéressant, un seul fournisseur a signalé l'URL comme malveillante. Cela me suffira :-)

De plus, [Abuse IP DB](https://www.abuseipdb.com/report?ip=66.85.143.2) ne sait rien du site Web incriminé. Cependant, gardez cet outil à portée de main car il est connu pour signaler de nombreux autres acteurs.

Y a-t-il autre chose que nous pouvons apprendre du message d'origine ? La plupart des lecteurs d'e-mails vous permettent de copier et coller les en-têtes d'e-mail. Je partage les miens ici (avec quelques modifications) :

```text
Received: from MN2PR19MB4030.namprd19.prod.outlook.com (2603:10b6:208:1e8::11)
 by MW3PR19MB4204.namprd19.prod.outlook.com with HTTPS; Tue, 4 Oct 2022
 16:35:05 +0000
Received: from BN9PR03CA0959.namprd03.prod.outlook.com (2603:10b6:408:108::34)
 by MN2PR19MB4030.namprd19.prod.outlook.com (2603:10b6:208:1e8::11) with
 Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5676.31; Tue, 4 Oct
 2022 16:35:01 +0000
Received: from BN7NAM10FT104.eop-nam10.prod.protection.outlook.com
 (2603:10b6:408:108:cafe::cc) by BN9PR03CA0959.outlook.office365.com
 (2603:10b6:408:108::34) with Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5676.24 via Frontend
 Transport; Tue, 4 Oct 2022 16:34:59 +0000
Authentication-Results: spf=softfail (sender IP is 170.10.162.128)
 smtp.mailfrom=bounce.com; dkim=none (message not signed)
 header.d=none;dmarc=fail action=oreject header.from=godaddy.com;compauth=fail
 reason=000
Received-SPF: SoftFail (protection.outlook.com: domain of transitioning
 bounce.com discourages use of 170.10.162.128 as permitted sender)
Received: from host.solutiononellc.com (170.10.162.128) by
 BN7NAM10FT104.mail.protection.outlook.com (10.13.157.118) with Microsoft SMTP
 Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id
 15.20.5676.17 via Frontend Transport; Tue, 4 Oct 2022 16:34:59 +0000
Received: from ip250.ip-37-187-205.eu ([37.187.205.250]:38823)
	by altar47.supremepanel47.com with esmtpsa  (TLS1.2) tls TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
	(Exim 4.95)
	(envelope-from <postmaster@bounce.com>)
	id 1ofksk-0005Zd-LV
	for xxx@xxxx.com;
	Tue, 04 Oct 2022 16:34:58 +0000
```

L'utilisation de [MXToolbox](https://mxtoolbox.com/Public/Tools/EmailHeaders.aspx?huid=4205dc8f-5147-4da5-a448-d633f2bbca61) montre que 2 des adresses e-mail utilisées dans la chaîne sont **sur liste noire**, un autre signal d'alerte.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/godaddy_scammer_mxtoolbox.png)
_2 e-mails bloqués dans cette liste. Un autre signal d'alerte_

Je pense que c'est suffisant. Supprimez l'e-mail et continuez votre vie, et soyez sûr qu'un nouvel e-mail arrivera (en espérant qu'il atterrisse automatiquement dans le dossier SPAM).

## Et après ?

Il existe de nombreux outils sur Internet que vous pouvez utiliser pour identifier les e-mails de phishing, mais rien ne remplace le bon sens. Si cela semble trop beau pour être vrai, c'est probablement le cas.

Comme d'habitude, ne cliquez pas sur le lien tout de suite ! Faites d'abord une petite enquête, juste pour être sûr.