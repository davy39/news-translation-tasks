---
title: Comment construire des ponts de communication cross-origin dans iOS et Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-08-01T18:15:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-cross-origin-communication-bridges-in-ios-and-andriod-7baef82b3f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVKPXp6zfjMErb99NPZfKw.jpeg
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment construire des ponts de communication cross-origin dans iOS et
  Android
seo_desc: 'I was working on a certain project at work, in which I needed to connect
  several varying components via messages. Each had its own logic and code language.
  This made me want to understand all the ways different platforms enable communication.

  This ar...'
---

Je travaillais sur un certain projet au travail, dans lequel je devais connecter plusieurs composants variés via des messages. Chacun avait sa propre logique et son propre langage de code. Cela m'a donné envie de comprendre toutes les façons dont différentes plateformes permettent la communication.

L'objectif de cet article est d'expliquer ces ponts de communication cross-origin et de présenter des exemples simples, mais informatifs, pour les réaliser.

Il y aura aussi beaucoup de jeux de mots sur les ponts ?

VOUS AVEZ ÉTÉ PRÉVENUS.

Si vous voulez simplement mettre la main à la pâte avec le code, il y a des liens vers les dépôts GitHub en bas de cet article.

Typiquement, le JavaScript que vous écrivez s'exécutera à l'intérieur d'un navigateur. Sur **iOS**, il peut s'agir d'un UIWebView ou d'un WKWebView. Sur **Android**, d'un WebView.

Puisque iOS peut être la plateforme la plus exaspérante, je vais décrire le pont de communication là en premier.

### London Bridge is Falling Down (iOS)

À partir d'iOS 8, Apple recommande d'utiliser WKWebView au lieu de UIWebView, donc ce qui suit ne traitera que du pont sur un **WKWebView**.

Pour une référence UIWebView, veuillez consulter [ici](https://stackoverflow.com/questions/5671742/send-a-notification-from-javascript-in-uiwebview-to-objectivec).

Pour envoyer des messages du WKWebView à JavaScript, vous utilisez la méthode suivante :

```android

- (void)evaluateJavaScript:(NSString *)javaScriptString 
         completionHandler:(void (^)(id, NSError *error))completionHandler;
```

Pour recevoir des messages de JavaScript à l'intérieur de votre WKWebView, vous devez faire ce qui suit :

1. Créer une instance de [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebview/1414979-configuration?language=objc)
2. Créer une instance de [WKUserContentController](https://developer.apple.com/documentation/webkit/wkusercontentcontroller?language=objc)
3. Ajouter un gestionnaire de messages de script à votre configuration (cette partie comble l'écart). Cette action enregistre également votre gestionnaire de messages sur l'objet window sous le chemin suivant : **window.webkit.messageHandlers.MSG_HANDLER_NAME**
4. Faire en sorte que la classe implémente le protocole du gestionnaire de messages en ajoutant <WKScriptMessageHandler> en haut du fichier
5. Implémenter [userContentController:didReceiveScriptMessage](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler/1396222-usercontentcontroller?preferredLanguage=occ) (cette méthode gère la réception des messages de JavaScript)

### Construire des ponts

Supposons que nous avons la page HTML suivante configurée :

```html
<html>
  
  <head>
    <title>Communication Javascript-iOS</title>
  </head>
  
  <body>
    
    <script>
      window.webkit.messageHandlers.myOwnJSHandler.postMessage("Hello World!");
    </script>
  </body>
  
  
</html>
```

Et dans notre code natif, nous implémentons les étapes décrites ci-dessus :

```android
#import <UIKit/UIKit.h>
#import <WebKit/WebKit.h>

// 4
@interface ViewController : UIViewController <WKScriptMessageHandler>

@property(nonatomic, strong) WKWebView *webview;


```

Et voilà ! Vous avez maintenant une communication JavaScript - iOS complète !

![Image](https://cdn-media-1.freecodecamp.org/images/1*EosjstTDed_5cYeD7Fa-mQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/OHMg0Hgetn4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Todd Diemer</a> sur <a href="https://unsplash.com/search/photos/bridge?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Traverser le pont (Android)

Les choses sont beaucoup plus simples et plus conviviales ici. Pour configurer notre pont de communication, il n'y a que quelques étapes :

1. Créer une instance d'un objet [WebView](https://developer.android.com/reference/android/webkit/WebView)
2. Activer JavaScript à l'intérieur de cette WebView (**setJavaScriptEnabled**)
3. Définir votre propre interface JavaScript (qui contiendra des méthodes visibles pour votre JavaScript)
4. Toute méthode que vous souhaitez exposer à votre JavaScript doit avoir l'annotation **@JavascriptInterface** avant sa déclaration

Comme avant, supposons que nous avons créé ce fichier HTML :

Et nous avons créé l'application Android simple suivante :

Et voilà !

Vous pouvez maintenant vous considérer comme un Ninja de la Communication Native !

Voici les liens vers les dépôts :

<a href="https://github.com/TomerPacific/MediumArticles/tree/master/AndroidtoJSNativeCommunicator">Dépôt AndroidtoJS</a>

<a href="https://github.com/TomerPacific/MediumArticles/tree/master/iOStoJSNativeCommunicator">Dépôt iOStoJS</a>

### ⚠️ Note importante concernant iOS ⚠️

Lorsque vous en arrivez au point où vous voulez détruire votre WKWebView, il est **impératif** que vous supprimiez votre gestionnaire de messages de script. Si vous ne le faites pas, le gestionnaire de messages de script conservera toujours une référence à votre WKWebView et des fuites de mémoire en résulteront lors de la création de nouveaux WKWebViews.