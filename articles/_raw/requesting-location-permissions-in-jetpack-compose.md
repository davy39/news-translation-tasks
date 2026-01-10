---
title: How to Request Location Permissions in Jetpack Compose
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2023-10-05T19:28:42.000Z'
originalURL: https://freecodecamp.org/news/requesting-location-permissions-in-jetpack-compose
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/andrew-stutesman-l68Z6eF2peA-unsplash.jpg
tags:
- name: Jetpack Compose
  slug: jetpack-compose
- name: user experience
  slug: user-experience
seo_title: null
seo_desc: "Getting a user’s location can be a bit of hassle. Over the years, the permissions\
  \ required to do this and the logic associated with it have changed quite drastically.\
  \ \nIf your application depends on getting the user’s location, you want to ensure\
  \ tha..."
---

Getting a user’s location can be a bit of hassle. Over the years, the permissions required to do this and the logic associated with it have changed quite drastically. 

If your application depends on getting the user’s location, you want to ensure that the user has a good experience when the application requests this info. So it's crucial to handle all the edge cases and allow the user to select the option the they're most comfortable with.

With Jetpack Compose, the logic associated with getting the user’s location has changed a bit, and it’s important to know the in’s and out’s of how it can be done.

As with most things, there is a library you can use to handle getting permissions. It’s from Accompanist (read Google) and you can find it [here](https://google.github.io/accompanist/permissions/#:~:text=A%20library%20which%20provides%20Android%20runtime%20permissions%20support%20for%20Jetpack%20Compose.&text=The%20permission%20APIs%20are%20currently,marked%20with%20the%20%40ExperimentalPermissionsApi%20annotation.). **But you are here to learn how to do things yourself,** right? So read on. 🕵️‍♀️

Before we get into the code and the logic, it is important to understand that requesting a permission from a user is a path that can have many decision points. As such, it is best described by having states that represent the current status of the permission (approved/rejected/denied) and the current status of the operating system. 

The diagram below illustrates this flow:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/location.png)

Later on in this article, you will see how we will represent these states in variables in our code.

## Save Our Souls (S.O.S)

Before we get to the logic of asking for a permission, we’ll take care of the boilerplate around it. As always, add the necessary permissions to your AndroidManifest.xml file:

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

Then, we’ll create a composable screen where we ask for the necessary location permissions. The first step in this screen is to check whether the user has previously granted the required permissions. You can do this with something that is not new to Jetpack Compose – using the checkSelfPermission method:

```kotlin
val locationPermissionsAlreadyGranted = ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED
```

If the permission is not granted, we have to request it. We will use the [rememberLauncherForActivityResult](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#rememberlauncherforactivityresult) object to do this. This allows us in Jetpack Compose to get a result from an Activity.

```kotlin
val locationPermissions = arrayOf(
    Manifest.permission.ACCESS_FINE_LOCATION,
    Manifest.permission.ACCESS_COARSE_LOCATION)

val locationPermissionLauncher = rememberLauncherForActivityResult(
                contract = ActivityResultContracts.RequestMultiplePermissions(),
                onResult = { permissions ->
                    val permissionsGranted = permissions.values.reduce { acc, isPermissionGranted ->
                        acc && isPermissionGranted
                    }
             
                    if (!permissionsGranted) {
                       //Logic when the permissions were not granted by the user
                    }
                })
```

The arguments that we need to pass to `rememberLauncherForActivityResult` are:

1. An [ActivityResultContract](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContract) – specifies the input of the activity and the output
2. onResult – a callback when the result is received

In the code snippet above, we are using a multiple permissions contract, since we are requesting several location permissions. There is also a contract for requesting just one permission, **ActivityResultContracts.RequestPermission().**

This piece of code doesn’t not run immediately as we need to request the permissions. To do that we use the launch method to start the activity:

```kotlin
locationPermissionLauncher.launch(locationPermissions)
```

In the case the user gave all or several of the required permissions, we can continue the logic of the application. 

But, if the user did not approve any of the permissions, we need to find a way to make the user understand why these permissions are necessary.

## Explaining the Rationale

In case the user declined the permission, but did not select the “Deny And Don’t Ask Me Again” option, we have a way of giving the user a brief explanation on why they should grant the required permission(s). 

To figure out if we should present this rationale, we use the [shouldShowRequestPermissionRationale](https://developer.android.com/reference/androidx/core/app/ActivityCompat#shouldShowRequestPermissionRationale(android.app.Activity,java.lang.String)) from the Activity class:

```kotlin
val shouldShowPermissionRationale: Boolean = shouldShowRequestPermissionRationale(Manifest.permission.ACCESS_COARSE_LOCATION)

```

Once we know that we can display this explanation, there are two ways to go about it:

1. We can present it to the user with an AlertDialog
2. We can use the Snackbar

Presenting an alert dialog is pretty straightforward. All we have to do is make sure we describe clearly to the user why it is required to approve this permission:

```kotlin
@Composable
    fun ShowLocationPermissionRationale() {
        AlertDialog(
            onDismissRequest = {
               //Logic when dismiss happens
            },
        title = {
            Text("Permission Required")
                },
        text = {
            Text("You need to approve this permission in order to...")
        },
        confirmButton = {
            TextButton(onClick = {
              //Logic when user confirms to accept permissions
            }) {
                Text("Confirm")
            }
        },
        dismissButton = {
            TextButton(onClick = {
              //Logic when user denies to accept permissions
            }) {
                Text("Deny")
            }
        })
    }
```

If we want to present the Snackbar, we need to be aware that we have to use a Scaffold container since that is the only container that supports showing a Snackbar. If we don’t use one, a Snackbar won’t appear. 

Below is a snippet that shows you how to do this:

```kotlin
val scope = rememberCoroutineScope()
val snackbarHostState = remember { SnackbarHostState() }

Scaffold(snackbarHost = {
        SnackbarHost(hostState = snackbarHostState)
    }) { contentPadding ->
        if (shouldShowPermissionRationale) {
            LaunchedEffect(key1 = shouldShowPermissionRationale, block = {
                scope.launch {
                    val userAction = snackbarHostState.showSnackbar(
                        message ="Please authorize location permissions",
                        actionLabel = "Approve",
                        duration = SnackbarDuration.Indefinite,
                        withDismissAction = true
                    )
                    when (userAction) {
                        SnackbarResult.ActionPerformed -> {
                            //User approved to grant the permission
                            //Ask for permissions again
                        }
                        SnackbarResult.Dismissed -> {
                            //User dismissed snackbar
                        }
                    }
                }
            })
        }
}
```

We allowed the Snackbar itself to be dismissible using the withDismissAction attribute and listened in to the action performed by the user.

## Lifecycle Observer

One thing we have glossed over is the fact that we need to make sure our permission request adheres to the composable lifecycle. This means that once a user chooses their preferences regarding the permission request, we need the UI to adapt accordingly. 

If you try and put the code above inside the activity’s onCreate method, you will be surprised with the outcome, since the application will crash with the following exception:

> _java.lang.IllegalStateException: Launcher has not been initialized_

This is because Composable functions are supposed to be side effect free. What is a side effect? According to [Google’s documentation](https://developer.android.com/jetpack/compose/side-effects) it is:

> … a change to the state of the app that happens outside the scope of a composable function

So, in our use case, launching an activity for the permissions is the side effect happening here. 

To circumvent this scenario, we need to use one of the side effect options. Since we don’t want to ask the user for permissions without remembering what their choices were previously, we can’t use the general **SideEffect**. And **LaunchedEffect** is used for calling suspend methods inside of a Composable, which is not our use case here. 

So we are left with **DisposableEffect**. Reading the [documentation](https://developer.android.com/jetpack/compose/side-effects#disposableeffect), we can see that [DisposableEffect](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#DisposableEffect(kotlin.Any,kotlin.Function1)) can be combined with Lifecycle events, which is what we are after.

```kotlin
val lifecycleOwner = LocalLifecycleOwner.current
            DisposableEffect(key1 = lifecycleOwner, effect = {
                val observer = LifecycleEventObserver { _, event ->
                    if (event == Lifecycle.Event.ON_START && !locationPermissionsAlreadyGranted) {
                        locationPermissionLauncher.launch(locationPermissions)
                       }
                    }
                    lifecycleOwner.lifecycle.addObserver(observer)
                    onDispose {
                        lifecycleOwner.lifecycle.removeObserver(observer)
                    }
                }
            )
```

In the code snippet above, we are adding a lifecycle observer that runs only in the case of the onStart lifecycle event. We also combine it with the boolean we have declared at the start of this section, locationPermissionsAlreadyGranted. This is so we won’t show the dialog for asking permissions if they are already granted. 

As with all lifecycle observers, we need to remove our observer once the composition ends. We have that logic inside DisposableEffect’s onDispose clause.

## Location Not Found

The last case we need to deal with is when the user chooses the “Deny And Don’t Ask Me Again” option. When this happens, we cannot ask the user to grant the required permissions. 

The only way the user can revert their choice is to go to the settings screen of our application and change the permissions there. So we need to direct the user to go there. 

To open the settings screen of our application, we need to use an intent with the action of **ACTION_APPLICATION_DETAILS_SETTINGS.**

```kotlin
Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.fromParts("package", packageName, null)).also {
            startActivity(it)
        }
```

Taking the logic above, we can add it to our code when we know that the user has chosen to deny the permissions and not be asked again. This happens inside our request for permissions when the user has not granted the permissions and the option to show the rationale is false.

## Location Confirmed

If we take everything we discussed in this article and put it inside one file, we will get the following code:

```kotlin
class MainActivity : ComponentActivity() {

    @OptIn(ExperimentalMaterial3Api::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {

            var locationPermissionsGranted by remember { mutableStateOf(areLocationPermissionsAlreadyGranted()) }
            var shouldShowPermissionRationale by remember {
                mutableStateOf(
                    shouldShowRequestPermissionRationale(Manifest.permission.ACCESS_COARSE_LOCATION)
                )
            }

            var shouldDirectUserToApplicationSettings by remember {
                mutableStateOf(false)
            }

            var currentPermissionsStatus by remember {
                mutableStateOf(decideCurrentPermissionStatus(locationPermissionsGranted, shouldShowPermissionRationale))
            }

            val locationPermissions = arrayOf(
                Manifest.permission.ACCESS_FINE_LOCATION,
                Manifest.permission.ACCESS_COARSE_LOCATION
            )

            val locationPermissionLauncher = rememberLauncherForActivityResult(
                contract = ActivityResultContracts.RequestMultiplePermissions(),
                onResult = { permissions ->
                    locationPermissionsGranted = permissions.values.reduce { acc, isPermissionGranted ->
                        acc && isPermissionGranted
                    }

                    if (!locationPermissionsGranted) {
                        shouldShowPermissionRationale =
                            shouldShowRequestPermissionRationale(Manifest.permission.ACCESS_COARSE_LOCATION)
                    }
                    shouldDirectUserToApplicationSettings = !shouldShowPermissionRationale && !locationPermissionsGranted
                    currentPermissionsStatus = decideCurrentPermissionStatus(locationPermissionsGranted, shouldShowPermissionRationale)
                })

            val lifecycleOwner = LocalLifecycleOwner.current
            DisposableEffect(key1 = lifecycleOwner, effect = {
                val observer = LifecycleEventObserver { _, event ->
                    if (event == Lifecycle.Event.ON_START &&
                        !locationPermissionsGranted &&
                        !shouldShowPermissionRationale) {
                        locationPermissionLauncher.launch(locationPermissions)
                    }
                }
                lifecycleOwner.lifecycle.addObserver(observer)
                onDispose {
                    lifecycleOwner.lifecycle.removeObserver(observer)
                    }
                }
            )

            val scope = rememberCoroutineScope()
            val snackbarHostState = remember { SnackbarHostState() }

            LocationPermissionsTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    Scaffold(snackbarHost = {
                        SnackbarHost(hostState = snackbarHostState)
                    }) { contentPadding ->
                        Column(modifier = Modifier.fillMaxSize(),
                        verticalArrangement = Arrangement.Center,
                        horizontalAlignment = Alignment.CenterHorizontally){
                            Text(modifier = Modifier
                                .padding(contentPadding)
                                .fillMaxWidth(),
                                text = "Location Permissions",
                                textAlign = TextAlign.Center)
                            Spacer(modifier = Modifier.padding(20.dp))
                            Text(modifier = Modifier
                                .padding(contentPadding)
                                .fillMaxWidth(),
                                text = "Current Permission Status: $currentPermissionsStatus",
                                textAlign = TextAlign.Center,
                                fontWeight = FontWeight.Bold
                            )
                        }
                        if (shouldShowPermissionRationale) {
                            LaunchedEffect(Unit) {
                                scope.launch {
                                    val userAction = snackbarHostState.showSnackbar(
                                        message ="Please authorize location permissions",
                                        actionLabel = "Approve",
                                        duration = SnackbarDuration.Indefinite,
                                        withDismissAction = true
                                    )
                                    when (userAction) {
                                        SnackbarResult.ActionPerformed -> {
                                            shouldShowPermissionRationale = false
                                            locationPermissionLauncher.launch(locationPermissions)
                                        }
                                        SnackbarResult.Dismissed -> {
                                            shouldShowPermissionRationale = false
                                        }
                                    }
                                }
                            }
                        }
                        if (shouldDirectUserToApplicationSettings) {
                            openApplicationSettings()
                        }
                    }
                }
            }
        }
    }

    private fun areLocationPermissionsAlreadyGranted(): Boolean {
        return ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED
    }

    private fun openApplicationSettings() {
        Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.fromParts("package", packageName, null)).also {
            startActivity(it)
        }
    }

    private fun decideCurrentPermissionStatus(locationPermissionsGranted: Boolean,
                                              shouldShowPermissionRationale: Boolean): String {
        return if (locationPermissionsGranted) "Granted"
        else if (shouldShowPermissionRationale) "Rejected"
        else "Denied"
    }
}
```

And this is how it looks like:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/location2.gif)

I have put all the logic in one file just for the purpose of this article. It is by no means the most esthetic and correct approach to handling the logic with requesting permissions. 

You could easily refactor out the logic variables associated with holding the different state of the request for permissions to a view model class that is attached to this screen.

You can see all of the code described in this article by going to this project:

%[https://github.com/TomerPacific/MediumArticles/tree/master/LocationPermissions]

And if you would like to read more of my articles, you can go view them below:

%[https://github.com/TomerPacific/MediumArticles]

I have also used this logic in an application that you can try out [here](https://play.google.com/store/apps/details?id=com.tomerpacific.scheduler).

Thank you for reading!


