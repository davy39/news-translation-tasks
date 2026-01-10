---
title: How to Setup a Contact Page in Laravel With and Without Attachments
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-07-29T16:26:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-contact-page-in-laravel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c997d740569d1a4ca2005.jpg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: null
seo_desc: 'I recently struggled a bit when trying to set up a contact page in Laravel.
  So I figured that I should blog about my experience, as it might help someone who
  wants to do the same.

  Laravel is an open source PHP framework used to develop web applicatio...'
---

I recently struggled a bit when trying to set up a contact page in Laravel. So I figured that I should blog about my experience, as it might help someone who wants to do the same.

Laravel is an [open source](https://opensource.com/resources/what-open-source) PHP framework used to develop web applications. It follows the model-view-controller architectural pattern.

## Prerequisites

1. [Install composer](https://getcomposer.org/download/)
2. Set up your local server ([xampp](https://www.apachefriends.org/download.html), [wamp](https://www.wampserver.com/en/download-wampserver-64bits/))
3. Make sure you have a code editor installed ([sublime text](https://www.sublimetext.com/3), [vs code](https://code.visualstudio.com/download), [atom](https://atom.io/) etc)
4. Install [Git](https://git-scm.com/downloads) (enables source control & versioning)

## Getting Started 

With Git installed you have access to Git bash. With bash open you can work with the terminal to run commands that lets you install and use Laravel and its packages easily. 

## Install Laravel via composer

Once you have satisfied all the above conditions, we will use the below command to set up the Laravel installer:

```
composer global require laravel/installer
```

The above command lets us download the Laravel installer using composer that we installed earlier.

```
laravel new project_name

```

This installation process takes a while so just be patient. **Note** that the installation will be done in the directory you specify in your bash terminal or any terminal you choose to use.

## Generating a basic authentication scaffold 

Once we have a copy of the Laravel app installed we should generate a basic authentication scaffold.

```
cd project_name

composer require laravel/ui

php artisan ui vue --auth
```

The above command will install layout view, registration view, and login view, as well as routes for all user authentication.

## Setting up environment variables in the .env file 

Next we need to set up our environment variables and establish a connection to our database (**in this article we'll use a shared dummy ip address**).

```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=server_username
DB_PASSWORD=server_password


MAIL_DRIVER=smtp
MAIL_HOST=domain.com
MAIL_PORT=465
MAIL_USERNAME=noreply@domain.com
MAIL_PASSWORD=domain_password
MAIL_ENCRYPTION=ssl
MAIL_FROM_ADDRESS=noreply@domain.com
MAIL_FROM_NAME="${APP_NAME}"
```

Now we're done setting up the database connection. In my case I work with Xampp where I have `DB_USERNAME=root` and `DB_PASSWORD=`. Also don't forget to start your local server as shown below. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/xampp.PNG)
_Image of xampp server_

## Versioning the database and starting the development server 

Before you can run migrations in Laravel you need to establish a connection to your database. Since I have specified  `your_database_name` in the .env configuration above I can click "create" and phpMyAdmin will build an empty database.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/your_database_name.PNG)
_Adding a database name_

In Git bash, navigate or cd into the `project_name` directory and run the below command:

```
cd project_name

php artisan migrate 
```

 This will run all default Laravel migrations in our application as long as you have created a matching `DB_DATABASE` which we created above. 

```
php artisan serve
```

We can now start our development server: 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/php-artisan-serve.PNG)
_Starting development server_

## Creating a contact.blade.php file

Set up a contact page in the **resources > views folder** like this:

```php
@extends('layouts.client.app')

@section('content')

<!-- contact section -->
    <div class="contact">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-7 col-lg-8 col-md-8">
                    <div class="section-title">
                        <h2>Contact Us</h2>
                    </div>
                </div>
            </div>

            @if(session('status'))
            <div class="row justify-content-center">
                <div class="col-xl-8 col-lg-8 col-md-8">
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Success ! </strong>  &nbsp; {{ session('status') }}
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                </div>
            </div>
            @endif
        </div>
    </div>
@endsection

```

The above code snippet will extend a layouts file containing the header section. It also contains the section title "Contact Us" along with a message that's been returned and displayed to the User if and only if the mail message was successfully sent.  

The main focus here is on the form section that you can see in the next code snippet:

```php
<div class="row justify-content-center">
    <div class="col-xl-8 col-lg-8">
        <div class="login-form">
            <form method="POST" action="{{ route('addContact') }}" enctype="multipart/form-data">
                @csrf
                <div class="row">

                    <div class="col-6">
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Full Name') }}</label>

                            <input type="text" class="form-control @error('fullname') is-invalid @enderror" name="fullname" value="{{ isset(Auth::user()->firstname) ? Auth::user()->firstname : '' }} {{ isset(Auth::user()->lastname) ? Auth::user()->lastname : '' }}" required autocomplete="Fullname" autofocus>

                            @error('fullname')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>
                    
                    <div class="col-6">

                        <div class="form-group">
                            <label for="email" class="col-form-label text-md-right">{{ __('Email Address') }}</label>

                            <input type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ isset(Auth::user()->email) ? Auth::user()->email : '' }}" required autocomplete="email" autofocus>

                            @error('email')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    
                    </div>

                    <div class="col-6">
                        
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Phone Number') }}</label>

                            <input type="text" class="form-control @error('phone_number') is-invalid @enderror" name="phone_number" value="{{ isset(Auth::user()->phone_number) ? Auth::user()->phone_number : '' }}" required autocomplete="phone_number" autofocus>

                            @error('phone_number')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>

                    <div class="col-6">
                
                    
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Subject') }}</label>

                            <input type="text" class="form-control @error('subject') is-invalid @enderror" name="subject" required autofocus>

                            @error('subject')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>

                    <div class="col-6">
                        <div class="form-group">

                            <label for="password" class="col-form-label text-md-right">{{ __('Message') }}</label>

                            <textarea class="form-control @error('message') is-invalid @enderror" name="message" required></textarea>

                            @error('message')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>

                    <div class="col-6">
                
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Attach Screenshot') }}</label>

                            <input type="file" accept="image/*" class="form-control @error('screenshot') is-invalid @enderror" name="screenshot" autofocus>

                        </div>
                    </div>
                </div>

                <div class="form-group row mb-0">
                    <div class="col-md-6 offset-md-4">
                        <button type="submit" class="btn btn-primary">
                            {{ __('Send Message') }}
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
```

The snippet above contains the various input fields that we will use in processing user information. The fields include FULLNAME, EMAIL ADDRESS, PHONE NUMBER , SUBJECT or PURPOSE , MESSAGE , IMAGE UPLOAD (if any) and finally a SEND MESSAGE button to process the submission of the form. 

Next we will merge both code snippets together to make them lot more meaningful.

```php
@extends('layouts.client.app')
@section('content')
<div class="contact">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-xl-7 col-lg-8 col-md-8">
                <div class="section-title">
                    <h2>Contact Us</h2>
                </div>
            </div>
        </div>

        @if(session('status'))
        <div class="row justify-content-center">
            <div class="col-xl-8 col-lg-8 col-md-8">
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Success ! </strong>  &nbsp; {{ session('status') }}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </div>
        </div>
        @endif
        <div class="row justify-content-center">
                <div class="col-xl-8 col-lg-8">
                    <div class="login-form">
                        <form method="POST" action="{{ route('addContact') }}" enctype="multipart/form-data">
                            @csrf
                            <div class="row">

                                <div class="col-6">
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Full Name') }}</label>

                                        <input type="text" class="form-control @error('fullname') is-invalid @enderror" name="fullname" value="{{ isset(Auth::user()->firstname) ? Auth::user()->firstname : '' }} {{ isset(Auth::user()->lastname) ? Auth::user()->lastname : '' }}" required autocomplete="Fullname" autofocus>

                                        @error('fullname')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>
                                
                                <div class="col-6">

                                    <div class="form-group">
                                        <label for="email" class="col-form-label text-md-right">{{ __('Email Address') }}</label>

                                        <input type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ isset(Auth::user()->email) ? Auth::user()->email : '' }}" required autocomplete="email" autofocus>

                                        @error('email')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                
                                </div>

                                <div class="col-6">
                                    
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Phone Number') }}</label>

                                        <input type="text" class="form-control @error('phone_number') is-invalid @enderror" name="phone_number" value="{{ isset(Auth::user()->phone_number) ? Auth::user()->phone_number : '' }}" required autocomplete="phone_number" autofocus>

                                        @error('phone_number')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>

                                <div class="col-6">
                            
                                
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Subject') }}</label>

                                        <input type="text" class="form-control @error('subject') is-invalid @enderror" name="subject" required autofocus>

                                        @error('subject')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>

                                <div class="col-6">
                                    <div class="form-group">

                                        <label for="password" class="col-form-label text-md-right">{{ __('Message') }}</label>

                                        <textarea class="form-control @error('message') is-invalid @enderror" name="message" required></textarea>

                                        @error('message')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>

                                <div class="col-6">
                            
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Attach Screenshot') }}</label>

                                        <input type="file" accept="image/*" class="form-control @error('screenshot') is-invalid @enderror" name="screenshot" autofocus>

                                    </div>
                                </div>
                            </div>

                            <div class="form-group row mb-0">
                                <div class="col-md-6 offset-md-4">
                                    <button type="submit" class="btn btn-primary">
                                        {{ __('Send Message') }}
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
        </div>
    </div>
</div>
@endsection
```

The image below is a simple layout of what the contact page looks like right now. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Contact-us-2.PNG)
_Contact us page_

## Add routes to enable GET & POST requests 

First, we'll set up the routes in **routes > web.php** to render the contact page via a **GET** request and send mails via the **POST** request (which has been specified in the form attribute above).

```php
Route::get('/contact', 'HomeController@index')->name('contact');

Route::post('/contact', 'HomeController@send_mail')->name('addContact');
```

## Adding logic within the HomeController  

In **app > Http > Controllers,** Laravel scaffold generated a HomeController. 

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
	public function index()
    {
        return view('template.client.contact'); //renders the contact page
    }
   
}
```

The Controller file is where the logic of the application resides. Laravel Scaffold already generated the default HomeController. So we will make do with that and create a function named `index`. We will use it to render the contact us page each time the user visits the route or URL in the application.

```php
<?php

use Illuminate\Support\Facades\Mail;

use App\Mail\ContactFormMail;

class HomeController extends Controller
{
    public function send_mail(Request $request)
    {
        $this->validate($request, [
            'fullname' => ['required', 'string', 'max:255' ], 
            'email' => ['required', 'string', 'email', 'max:255' ],
            'phone_number' => ['string', 'max:255'],
            'subject' => ['required', 'string', 'max:255'],
            'message' => ['required', 'string', 'max:255']
        ]);

        $contact = [
            'fullname' => $request['fullname'], 
            'email' => $request['email'],
            'phone_number' => $request['phone_number'],
            'subject' => $request['subject'],
            'message' => $request['message'],
            'screenshot' => $request->file('screenshot')->store('contact', 'public')
        ];

    
        Mail::to('receipent@domain.com')->send(new ContactFormMail($contact));
        
        return redirect()->route('contact')->with('status', 'Your Mail has been received');
    }
}
```

In the same HomeController, we need to create another function named `send_mail` . The function will validate all user input and check to make sure fields are not left empty and the right data is parsed. 

Next create a variable called `$create` to store the array values of all user data including image uploads. 

Laravel ships with a filesystem that lets us work with images easily. The `Mail::to(....)`and `send` ship with Illuminate\Support\Facade which I included at the top of the snippet. I have also included a Mailable, which I will explain soon. 

We now need to alert users when the message has been dispatched and redirect them. 

Bringing the code snippets together now will make the HomeController look somewhat like this:

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use Illuminate\Support\Facades\Mail;

use App\Mail\ContactFormMail;

class HomeController extends Controller
{
	public function index()
    {
        return view('template.client.contact'); //renders the contact page
    }
    
    public function send_mail(Request $request)
    {
        $this->validate($request, [
            'fullname' => ['required', 'string', 'max:255' ], 
            'email' => ['required', 'string', 'email', 'max:255' ],
            'phone_number' => ['string', 'max:255'],
            'subject' => ['required', 'string', 'max:255'],
            'message' => ['required', 'string', 'max:255']
        ]);

        $contact = [
            'fullname' => $request['fullname'], 
            'email' => $request['email'],
            'phone_number' => $request['phone_number'],
            'subject' => $request['subject'],
            'message' => $request['message'],
            'screenshot' => $request->file('screenshot')->store('contact', 'public')
        ];

    
        Mail::to('receipent@domain.com')->send(new ContactFormMail($contact));
        
        return redirect()->route('contact')->with('status', ' Your Mail has been received');
    }
}
```

Having merged both of the above functions, we are done with the logic for the HomeController. Now let's proceed to the next step. 

## Generating [Laravel Mailable](https://laravel.com/docs/7.x/mail) 

Each mail sent within the Laravel application is represented as a "mailable" just in case you're wondering about the name. Let's create a markdown mailable for contact information that we want to process:

```php
php artisan make:mail ContactFormMail --markdown=template.client.contactform
```

The command above will generate a markdown file in the **resources > views > template > client** directory and also create a mailable file in **app > Mail > ContactFormMail.php**.

In ContactFormMail.php we have the following code snippet that lets us send mails **without** an attachment:

```php
<?php

namespace App\Mail;
use App\User;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class ContactFormMail extends Mailable
{
    use Queueable, SerializesModels;

    /**
    * Create a new message instance.
    *
    * @return void
    */

    public function __construct($data)
    {
        $this->user = $data;
    }

    /**
     * Build the message.
     *
     * @return $this
     */
    public function build()
    {
        return $this->from('noreply@domain.com')
                ->markdown('template.client.contactform')
                ->with([
                        'subject' => $this->user['subject'],
                        'message' => $this->user['message'],
                        'email' => $this->user['email'],
                        'phone_number' => $this->user['phone_number'],
                        'fullname' => $this->user['fullname'],
                    ]);
    }
}

```

Let's break this code down a bit.

In the `**_construct**` method I'm parsing all user data as a parameter and reassigning it. In the `**build**` method, all of the mailable class configuration is done.

The `**from**` **Method** specifies the mail sender, that is who the mail is coming from (in my case **noreply@domain.com**).

The `**with**`  **Method** lets you choose to customize how mails will be rendered to the markdown which was generated. In this article we will assign all the fields to key and value pairs within the array so that within the markdown we can access each value with its own unique key.

The `**markdown**` **Method** accepts the name the of markdown template to be rendered with an optional data parameter (if we weren't making use of the `**with**` method).

And lastly, the `**to**` **Method** specifies the recipient of the mail. In the HomeController above, change 'receipent@domain.com' to the actual recipient's address.

## Add Data to the Markdown File  

Now we need to configure the markdown file in the **resources > views > template > client** directory. Since we have key value pairs in place already, it's easier to reference with keys in the markdown file as shown below:

```php
@component('mail::message')
# {{$subject}}

## {{$message}}

Feel free to contact me via {{$phone}} or {{$email}}

Thanks,<br>
{{$fullname}}

{{ config('app.name') }}
@endcomponent
```

At this point we're almost done ???. Kudos for following along with the process this far.  You have now learned how to send an email without attachment. Now let's look at how to do it with an attachment.

## Sending Mails with an Attachment

Laravel already ships with a powerful [filesystem](https://laravel.com/docs/7.x/filesystem), so sending mails with an attachment isn't too difficult. We will leverage this feature and create storage for users where we will store their attached files within the application.  

```php
php artisan storage:link
```

**NOTE** : In HomeController above I already specified a storage directory for the uploads. You should do same by creating a folder (called **contact**) in **storage > app > public > contact** .

Also in the **config > filesystems.php** check and make sure the default filesystem disk is set to `return ['default' => 'public']`.

Now the **[Cont](https://www.freecodecamp.org/news/p/7a16e74f-8e36-4e21-9344-feba5c03da08/ContactFormMail.php)actFormMail.php** looks like this. We are now able to use the   `attachFromStorage` method which makes reference to the filepath.

```php
<?php

namespace App\Mail;
use App\User;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class ContactFormMail extends Mailable
{
    use Queueable, SerializesModels;

    /**
    * Create a new message instance.
    *
    * @return void
    */
    public $user;

    public function __construct($data)
    {
        $this->user = $data;
    }

    /**
     * Build the message.
     *
     * @return $this
     */
    public function build()
    {
        return $this->from('noreply@domain.com')
                ->markdown('template.client.contactform')
                ->attachFromStorage($this->user['screenshot'])
                ->with([
                        'subject' => $this->user['subject'],
                        'message' => $this->user['message'],
                        'email' => $this->user['email'],
                        'phone_number' => $this->user['phone_number'],
                        'fullname' => $this->user['fullname']
                    ]);
    }
}

```

The only addition here will be **attachFromStorage.** It is used to process the attached files (either image or pdf) during the entire mailing process. 

In the markdown file that we earlier used, we can slightly rework it to look like what's shown below:

```
<div class="row">
	<h1 class="text-dark">{{$subject}}</h1>

	<h3>{{$message}}</h3> 

	<h4>You can reach me via mail or telephone : {{$email}} or {{$phone_number}}<br/>
	Thanks
	</h4>
</div>



```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_20200724-180046.png)
_Screenshot of successful mail message_

Yaaay we can now do a happy dance because we're finally done ?????

<iframe src="https://giphy.com/embed/zQLjk9d31jlMQ" width="480" height="262" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dancing-dance-woo-zQLjk9d31jlMQ">via GIPHY</a></p>

Now that you've made it through the entire article, you should be able to implement a similar emailing feature in your Laravel applications. 

To learn more you can check out the official [Laravel documentation here.](https://laravel.com/docs/)  

