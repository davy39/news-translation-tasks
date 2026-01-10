---
title: Comment utiliser les Tooltips dans Jetpack Compose
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-10-02T13:57:57.679Z'
originalURL: https://freecodecamp.org/news/how-to-use-tooltips-in-jetpack-compose
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727813989960/b0a7ab29-d87c-4d87-9847-70b7e1c341b1.jpeg
tags:
- name: Android
  slug: android
- name: Jetpack Compose
  slug: jetpack-compose
- name: tooltip
  slug: tooltip
- name: UI
  slug: ui
seo_title: Comment utiliser les Tooltips dans Jetpack Compose
seo_desc: 'When I wrote my last article about Jetpack Compose, I stated there that
  Jetpack Compose is missing some (in my opinion) basic components, and one of them
  is the tooltip.

  At the time, there was no built-in composable to display tooltips and there were...'
---

Lorsque j'ai écrit mon [dernier article sur Jetpack Compose](https://medium.com/better-programming/is-jetpack-compose-ready-for-you-eae6c93ad3f8), j'y affirmais que Jetpack Compose manquait de certains composants de base (à mon avis), et l'un d'eux est le tooltip (info-bulle).

À l'époque, il n'y avait pas de composable intégré pour afficher des tooltips et plusieurs solutions alternatives circulaient en ligne. Le problème avec ces solutions était qu'une fois que Jetpack Compose publiait de nouvelles versions, ces solutions pouvaient cesser de fonctionner. Ce n'était donc pas idéal et la communauté espérait qu'à l'avenir, le support des tooltips serait ajouté.

Je suis heureux de dire que depuis la [version 1.1.0 de Compose Material 3](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.1.0), nous disposons désormais d'un support intégré pour les tooltips. 👏

Bien que cela soit excellent en soi, plus d'un an s'est écoulé depuis la sortie de cette version. Et avec les versions suivantes, l'API liée aux tooltips a également radicalement changé.

Si vous parcourez le journal des modifications (changelog), vous verrez comment les API publiques et internes ont évolué. Gardez donc à l'esprit qu'au moment où vous lisez cet article, les choses ont pu continuer à changer car tout ce qui concerne les Tooltips est toujours marqué par l'annotation **ExperimentalMaterial3Api::class**.

❗️ La version de Material 3 utilisée pour cet article est la 1.2.1, publiée le 6 mars 2024.

## Types de Tooltips

Nous avons désormais en charge deux types différents de tooltips :

1. Tooltip simple (Plain tooltip)
    
2. Tooltip multimédia riche (Rich media tooltip)
    

### Tooltip simple

Vous pouvez utiliser le premier type pour fournir des informations sur un bouton d'icône qui ne seraient pas claires autrement. Par exemple, vous pouvez utiliser un tooltip simple pour indiquer à un utilisateur ce que représente le bouton d'icône.

![Exemple de tooltip de base](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602449314/94cf84bf-dec0-462c-a8a0-6f878e0d5db3.gif align="center")

Pour ajouter un tooltip à votre application, vous utilisez le composable **TooltipBox**. Ce composable prend plusieurs arguments :

```kotlin
fun TooltipBox(
    positionProvider: PopupPositionProvider,
    tooltip: @Composable TooltipScope.() -> Unit,
    state: TooltipState,
    modifier: Modifier = Modifier,
    focusable: Boolean = true,
    enableUserInput: Boolean = true,
    content: @Composable () -> Unit,
)
```

Certains d'entre eux devraient vous être familiers si vous avez déjà utilisé des Composables. Je vais souligner ceux qui ont un cas d'utilisation spécifique ici :

* positionProvider - De type **PopupPositionProvider**, il est utilisé pour calculer la position du tooltip.
    
* tooltip - C'est ici que vous pouvez concevoir l'interface utilisateur (UI) de l'apparence du tooltip.
    
* state - Ceci contient l'état associé à une instance spécifique de Tooltip. Il expose des méthodes comme l'affichage/la fermeture du tooltip et, lors de l'instanciation d'une instance, vous pouvez déclarer si le tooltip doit être persistant ou non (c'est-à-dire s'il doit rester affiché à l'écran jusqu'à ce que l'utilisateur effectue un clic en dehors du tooltip).
    
* content - C'est l'UI au-dessus ou en dessous de laquelle le tooltip s'affichera.
    

Voici un exemple d'instanciation d'une **BasicTooltipBox** avec tous les arguments pertinents remplis :

```kotlin
@OptIn(ExperimentalFoundationApi::class, ExperimentalMaterial3Api::class)
@Composable
fun BasicTooltip() {
    val tooltipPosition = TooltipDefaults.rememberPlainTooltipPositionProvider()
    val tooltipState = rememberBasicTooltipState(isPersistent = false)

    BasicTooltipBox(positionProvider = tooltipPosition,
        tooltip =  { Text("Hello World") } ,
        state = tooltipState) {
        IconButton(onClick = { }) {
            Icon(imageVector = Icons.Filled.Favorite, 
                 contentDescription = "Description de votre icône")
        }
    }
}
```

![Un tooltip de base](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602558759/e00e0bed-6a95-489e-af5c-a7d9dcc33fe6.gif align="center")

Jetpack Compose possède une classe intégrée appelée TooltipDefaults. Vous pouvez utiliser cette classe pour vous aider à instancier les arguments qui composent une TooltipBox. Par exemple, vous pourriez utiliser **TooltipDefaults.rememberPlainTooltipPositionProvider** pour positionner correctement le tooltip par rapport à l'élément d'ancrage.

### Tooltip riche

Un tooltip multimédia riche prend plus d'espace qu'un tooltip simple et peut être utilisé pour fournir plus de contexte sur la fonctionnalité d'un bouton d'icône. Lorsque le tooltip est affiché, vous pouvez y ajouter des boutons et des liens pour fournir des explications ou des définitions supplémentaires.

Il s'instancie de manière similaire à un tooltip simple, à l'intérieur d'une TooltipBox, mais vous utilisez le composable RichTooltip.

```kotlin
TooltipBox(positionProvider = tooltipPosition,
        tooltip = {
                  RichTooltip(
                      title = { Text("RichTooltip") },
                      caretSize = caretSize,
                      action = {
                          TextButton(onClick = {
                              scope.launch {
                                  tooltipState.dismiss()
                                  tooltipState.onDispose()
                              }
                          }) {
                              Text("Fermer")
                          }
                      }
                  ) {
                        Text("C'est ici qu'irait une description.")
                  }
        },
        state = tooltipState) {
        IconButton(onClick = {
            /* Événement de clic du bouton d'icône */
        }) {
            Icon(imageVector = tooltipIcon,
                contentDescription = "Description de votre icône",
                tint = iconColor)
        }
    }
```

Quelques points à noter concernant un tooltip riche :

1. Un tooltip riche prend en charge un caret (pointe).
    
2. Vous pouvez ajouter une action (c'est-à-dire un bouton) au tooltip pour donner aux utilisateurs la possibilité de trouver plus d'informations.
    
3. Vous pouvez ajouter une logique pour fermer le tooltip.
    

![Tooltip riche sans caret](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602624042/40160d88-4e8a-4487-835d-1b74a9dd7c72.png align="center")

![Tooltip riche avec un caret](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602651265/f3e6f7fe-c4e1-4f98-972d-b20a273900b4.png align="center")

### Cas particuliers

Lorsque vous choisissez de marquer votre **état de tooltip comme persistant**, cela signifie qu'une fois que l'utilisateur interagit avec l'UI qui affiche votre tooltip, il restera visible jusqu'à ce que l'utilisateur appuie n'importe où ailleurs sur l'écran.

Si vous avez regardé l'exemple d'un tooltip riche ci-dessus, vous avez peut-être remarqué que nous avons ajouté un bouton pour fermer le tooltip une fois qu'il est cliqué.

Il y a un problème qui survient une fois qu'un utilisateur appuie sur ce bouton. Étant donné que l'action de fermeture est effectuée sur le tooltip, si un utilisateur souhaite effectuer un autre appui long sur l'élément d'interface qui invoque ce tooltip, le tooltip ne s'affichera plus. Cela signifie que l'état du tooltip reste sur l'état "fermé". Alors, comment résoudre cela ?

![Le deuxième appui long ne déclenche pas le tooltip](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602690256/a31b56bb-77c4-4444-bab6-7ffcca3f5207.gif align="center")

Afin de « réinitialiser » l'état du tooltip, nous devons appeler la méthode **onDispose** qui est exposée via l'état du tooltip. Une fois que nous faisons cela, l'état du tooltip est réinitialisé et le tooltip s'affichera à nouveau lorsque l'utilisateur effectuera un appui long sur l'élément d'interface.

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun RichTooltip() {
    val tooltipPosition = TooltipDefaults.rememberRichTooltipPositionProvider()
    val tooltipState = rememberTooltipState(isPersistent = true)
    val scope = rememberCoroutineScope()

    TooltipBox(positionProvider = tooltipPosition,
        tooltip = {
                  RichTooltip(
                      title = { Text("RichTooltip") },
                      caretSize = TooltipDefaults.caretSize,
                      action = {
                          TextButton(onClick = {
                              scope.launch {
                                  tooltipState.dismiss()
                                  tooltipState.onDispose()  /// <---- ICI
                              }
                          }) {
                              Text("Fermer")
                          }
                      }
                  ) {

                  }
        },
        state = tooltipState) {
        IconButton(onClick = {  }) {
            Icon(imageVector = Icons.Filled.Call, contentDescription = "Description de votre icône")
        }
    }
}
```

![onDispose résout le problème](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602730404/60f31668-ea66-4127-b6fc-41f3aca952ae.gif align="center")

Un autre scénario où l'état du tooltip ne se réinitialise pas est si, au lieu d'appeler nous-mêmes la méthode de fermeture suite à une action de l'utilisateur, celui-ci clique en dehors du tooltip, provoquant sa fermeture. Cela appelle la méthode dismiss en coulisses et l'état du tooltip est défini sur fermé. Un appui long sur l'élément d'interface pour revoir notre tooltip ne donnera rien.

![Le tooltip ne s'affiche plus](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602758707/60387e08-72e6-45d4-bd47-ffb2708e0efe.gif align="center")

Notre logique qui appelle la méthode onDispose du tooltip n'est pas déclenchée, alors comment pouvons-nous réinitialiser l'état du tooltip ?

Actuellement, je n'ai pas réussi à trouver de solution à cela. Cela pourrait être lié au [MutatorMutex](https://developer.android.com/reference/kotlin/androidx/compose/foundation/MutatorMutex) du tooltip. Peut-être qu'avec les prochaines versions, il y aura une API pour cela. J'ai remarqué que si d'autres tooltips sont présents à l'écran et qu'ils sont pressés, cela réinitialise le tooltip précédemment cliqué.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727602790121/25a81994-a508-4c71-8424-c45370a7999d.gif align="center")

Si vous souhaitez voir le code présenté ici, vous pouvez consulter [ce dépôt GitHub](https://github.com/TomerPacific/MediumArticles/tree/master/TooltipExample)

Si vous souhaitez voir des tooltips dans une application concrète, vous pouvez la consulter [ici](https://play.google.com/store/apps/details?id=com.tomerpacific.laundry).

#### Références

* [Aperçu du Tooltip Material3](https://m3.material.io/components/tooltips/overview)
    
* [Tooltip Defaults](https://developer.android.com/reference/kotlin/androidx/compose/material3/TooltipDefaults)
    
* [Code source du Tooltip](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/Tooltip.kt)