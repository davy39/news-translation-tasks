---
title: How to Backup Squarespace-Managed Styles using AWS Cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-14T19:19:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-backup-squarespace-managed-styles-using-aws-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/backup-with-aws-cloud.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
seo_title: null
seo_desc: 'By Adham El Banhawy

  A while ago, I was doing side gig for a client who had a website hosted on Squarespace.
  They asked me to implement an advanced design for a page that wasn''t possible with
  the site''s current DIY tools.

  For an experienced and battle...'
---

By Adham El Banhawy

A while ago, I was doing side gig for a client who had a website hosted on Squarespace. They asked me to implement an advanced design for a page that wasn't possible with the site's current DIY tools.

For an experienced and battle-tested web developer like me, this was a simple task even though I'd never worked with website-making tools before. All I had to do was write my custom CSS and JavaScript and inject them into the site while referencing Squarespace's developer docs.

But despite my experience, I ran into a problem that brought me to my knees and made me doubt myself as a developer (oh hi imposter syndrome – long time no see!). This is the story of how I encountered that problem, how I debugged it, and finally how I fixed it using AWS cloud.

## Where Did the Site's Styles Go?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-132.png)
_A broken site === A broken heart_

I remember just changing the margin of a class in the site's CSS editor using a variable. When I clicked save on the styles editor in the admin site, I saw the live preview just blank out. I opened the live site in a new tab, and I was greeted with a broken website on all routes.

Weird...that simple change shouldn't have broken the site. Maybe their styles editor doesn't support variables? I deleted the CSS variable I created and used normal pixels. Site still broken. Console shows no error.

Fine! I removed all my custom CSS from the styles editor. Same problem. At this point I start panicking. How did I break the site? Why was the website refusing to load ANY styles?

Wait. I just asked the right question. Why wasn't the site **loading** my styles? I realized I didn't know if all my custom and Squarespace CSS were embedded into the HTML or if they were delivered over the network. 

I inspected the HTML for any linked stylesheets, and found a suspect in the header called _site.css_

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-133.png)
_An externally linked stylesheet_

I confirmed the culprit when I switched to the Network tab to see if the request to this particular CSS file was successful.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-134.png)

It wasn't. It was returning a 5xx error. In the screenshot I manually blocked the request to replicate the issue so the status is different from the original, but the effect is the same: our site is requesting the main stylesheet from Squarespace and that request was failing which broke the site's styling.

Phew! I stopped panicking and regained my confidence. This wasn't my mistake, it was Squarespace's.

To confirm, I looked up and visited Squarespace's status page. Indeed, their status page indicated that they were experiencing some problems on their servers that, among other things, caused styles not to load for many users. Nothing more I could do. I just waited until the issue was resolved.

It took 15 **minutes** for Squarespace to fix the problem. I thought maybe this was a rare issue, and I got lucky it happened at a very late hour past midnight. I was so wrong...

## We Needed a Solution

A few days later, my client tried and failed to reach me to alert me that the site was, you guessed it, BROKEN. By the time we got in touch later that day, I found out that the same issue happened again. And it happened in the middle of the day for a longer period close to **30 minutes.**

The client understandably freaked out and deleted all custom CSS (thankfully I had a local copy), and prayed for the best (while probably thinking I broke their website and vanished).

In hindsight, I should have communicated better and informed them of that problem when I first faced it. It wasn't Squarespace's mistake this time (although it totally was), it was mine for not coming up with a solution when I encountered it.

The problem here, as I saw it, was that our stylesheets were hosted on a server that wasn't under our control. How do I remove that external dependency from the website?

To answer that question I looked to the cloud...

## My Initial AWS Solution

In my original development, I would put my custom CSS code in Squarespace's custom CSS editor. The site editor accepted SASS, so I wrote my styles in SASS, and always stored a copy on a local Git folder I have on my machine to have some sort of versioning.

As I mentioned before, the stylesheets are hosted on Squarespace's servers, so I needed my own hassle-free way to host these stylesheets. So I came up with the following solution.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-135.png)

In this scenario, I, the website developer, would write my code on Squarespace's custom CSS editor, then copy/paste the SASS to my local machine. The following flow would then take place:

* I push my code to CodeCommit
* The push event would trigger a Lambda function 
* The Lambda function would pull the latest SASS file, and convert it to a CSS stylesheet.
* The Lambda function would store the CSS stylesheet in a publicly available S3 bucket
* A custom inline script on the website would check if the expected stylesheet from Squarespace was loaded. If it's not, it requests the fallback stylesheet from the S3 bucket and injects it into the page.

And so I implemented this solution as quickly as I could before the site broke again. The very next day, the new flow was set up and working as expected.

### How to Configure the CodeCommit Trigger

After I pushed the code to my CodeCommit repository, I went to repository's Settings, then to the Triggers tab, and clicked the "Create trigger" button.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-136.png)

I named the trigger, selected the "Push to existing branch" as the event type, and master as my branch to listen on. Then I selected AWS Lambda as the service to use, and pointed to my Lambda function, then created the trigger. 

This Lambda now runs right after any code is pushed to the master branch on CodeCommit.

### Lambda Logic

Here's the JS code for the invoked lambda:

```js
const {
    S3,
    CodeCommit,
} = require('aws-sdk')
const sass = require('node-sass');

const getFileFromCodeCommit = (filePath) => new Promise((resolve, reject) => {
    const ccClient = new CodeCommit({ region: "us-east-1" })
    const ccParams = {
        filePath,
        repositoryName: 'mebbels-assets'
    }

    ccClient.getFile(ccParams, (err, data) => {
        if (err) reject(err)
        console.log(data)
        let stringData = new TextDecoder().decode(data.fileContent);
        resolve(stringData)
    })

})

const sendStylesheetToS3 = (fileData, fileName) => new Promise((resolve, reject) => {
    const s3Client = new S3({ region: "eu-south-1" })
    let putObjectBody = {
        Bucket: 'mebbels-assets',
        Key: fileName,
        ACL: 'public-read',
        Body: fileData,
        ContentType: 'text/css'
    }
    s3Client.putObject(putObjectBody, (err, data) => {
        if (err) reject(err)
        resolve(data)
    })
})

const processSASS = (fileData) => new Promise((resolve, reject) => {
    sass.render({
        data: fileData
    }, (err, data) => {
        if (err) reject(err)
        resolve(data)
    })
})
exports.handler = async (event) => {
    const sassFile = await getFileFromCodeCommit('mebbels-sass.scss')
    const processedSass = await processSASS(sassFile)
    await sendStylesheetToS3(processedSass.css, 'fallbackStyles.css')
    const response = {
        statusCode: 200,
        body: JSON.stringify("Done"),
    };

    return response;
};

```

In short, it pulls the SASS stylesheet (mebbels-sass.scss), converts it to CSS using the node-sass package, and then puts the output CSS file into a public S3 bucket.

Of course, for this lambda to run without issues related to accessing our resources on CodeCommit and S3 it needs the right permissions.

Here's IAM Role policy attached to the function:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "codecommit:GitPull",
                "s3:PutObjectAcl",
                "codecommit:GetFile"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::mebbels-assets",
                "arn:aws:codecommit:us-east-1:6653912857032:mebbels-assets"
            ]
        }
    ]
}

```

### How to Configure the S3 Bucket:

The target S3 bucket that will store the fallback CSS stylesheets needs to be public. I made sure it was so during bucket creation, and double checked in the "Permissions" tab of my S3 bucket in the Block public access section:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-137.png)

The bucket also needs to have [CORS enabled](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cors.html) and setup, because we're going to request it from a different domain, namely [mebbels.com](http://mebbels.com).

On the same "Permissions" tab, under the Cross-origin resource sharing (CORS) section, I added the following CORS configuration:

```json
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "https://www.mebbels.com"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]

```

## Site Script

And finally, here's the little inline script at the site's header that checks for the loaded state of the stylesheet requested from Squarespace. If it's not loaded after 20 milliseconds, then the script injects link into our site's header to our hosted fallback style in our S3 bucket.

```js
var isSiteCssLoaded = false;
var siteCssLink = document.querySelector("link[href*='/site.css']")
siteCssLink.addEventListener('load', () => {
    console.log('site.css loaded')
    isSiteCssLoaded = true;
})

const fallBackIfNeeded = () => {
    if (!isSiteCssLoaded) {
        console.log('site.css not loaded')
        var headID = document.getElementsByTagName('head')[0];
        var link = document.createElement('link');
        link.type = 'text/css';
        link.rel = 'stylesheet';
        link.href = '<https://mebbels-assets.s3.eu-south-1.amazonaws.com/fallbackStyles.css>'
        headID.appendChild(link);
		console.log('fallback styles loaded')
    }
}
setTimeout(fallBackIfNeeded, 20)

```

## How to Test this Solution

Well, I couldn't wait for Squarespace's servers to mess up again to test my solution. Here's how I tested it.

As I hinted at the beginning of the article, I can simulate a failed request to fetch our site's stylesheet from Squarespace by going to the browser's Network tab (making sure I disable the cache to avoid cached stylesheets), and then blocking the CSS request's URL:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-138.png)

After clicking "Block request URL", and refreshing the page, we should see my script kicking in after 20 milliseconds. And it should print out "site.css not loaded" and "fallback styles loaded" in the console, then add our fallback stylesheet from S3. And the site should work without breaking!

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-140.png)

## A Better Solution

Honestly, I was kind of proud of this quick solution and seeing it work was a joy. It's a cheap and serverless option that's not too complicated.

But this solution _is_ more complicated than it needs to be. And it's not without its caveats.

The downside of this solution is that the fallback style is still dependent on the website developer to keep the fallback styles that are in the CodeCommit repository up to date at all times. 

Also, there are other site admin users (like the designers) who sometimes edit the site's custom styles themselves. So this solution relies on perfect communication between team members to let the developer with AWS access know of custom changes so they can update the repository.

As I was reading more about AWS services available for use, I came across an awesome service called [CloudWatch Events](https://docs.amazonaws.cn/en_us/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html). This service allows you to trigger workflows in your AWS account based on monitored metrics OR on a scheduled basis.

So I decided to use CloudWatch Events as a serverless cronjob that triggers a Lambda function that scrapes our website's stylesheet on a daily basis, and stores it in the S3 bucket.

The modified solution now looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-142.png)

In this modified flow, we removed the dependency on the website developer to manually update the stylesheet and push to CodeCommit for the fallback styles to be created.

In this case, we have a daily scheduled CloudWatch Event that triggers a Lambda function.

Our Lambda function then scrapes our website for externally linked stylesheets, merges them into one fallback CSS file, and stores it in the publicly available S3 bucket. The website script stays the same as it checks for default stylesheets and requests it from our S3 bucket if not found.

### Lambda Code

Let's start with the new lambda function.

```python
import sys, os
import urllib.request as req
from bs4 import BeautifulSoup
import logging
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    fallback_css_filename = 'fallbackStyles.css'
    fallback_css_path = '/tmp/' + fallback_css_filename
    url = '<https://www.mebbels.com>'
    
    html = req.urlopen(url) # request the initial page
    soup = BeautifulSoup(html, 'html.parser') 
    fallback_styles = open(fallback_css_path, 'ab')
    
    for link in soup.find_all('link', type='text/css'): # get links to external style sheets
        address = link['href'] # the address of the stylesheet
        if address.startswith('/'): # relative link
            address = url + address
        css_file_name, headers = req.urlretrieve(address) # make a request to download the stylesheet from the address, returns bytes
        css = open(css_file_name, 'rb')
        fallback_styles.write(css.read())
        css.close()
    
    try:
        s3_client.upload_file(
            fallback_css_path,
            'mebbels-assets',
            fallback_css_filename,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': 'text/css'
                }
        )
        return True
    except ClientError as e:
        logging.error(e)
        return False

```

In this lambda, I use the BeautifulSoup library to web scrape our website. I download every single externally linked stylesheet and wrote them to a file in the temporary folder (AWS Lambdas allows you to store files temporarily in a folder called 'tmp' during runtime).

After writing all the styles to a single fallbackStyles.css file, I uploaded that to our S3 bucket using the AWS SDK just like before.

But unlike before, I now backed up ANY externally linked stylesheet, so I could back up an externally linked Google fonts stylesheet or or Bootstrap CSS CDN, for example.

## How to Use Scheduled CloudWatch Events

This was a new service for me that I was very excited to try out in a practical use case like this. It's incredible how amazingly simple and easy to use it is, with only two steps.

In the AWS console, under CLoudWatch > Events > Rules, I created a new rule and defined my settings.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-143.png)

In the Event Source section , I chose the "Schedule" option and chose a period of 6 hours. That meant that this event would be triggered automatically and consistently every six hours. There is even an option for a custom cron expression if you want a very specific custom interval.

But what does this event do? We need to tell it that in the Targets section. I picked "Lambda function" from the dropdown list and picked my available Lambda function. Then I clicked "Configure details" to progress.

In the next and last step, I just entered the name and description of the event rule I created.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-144.png)

Thankfully, that screen answered a burning question I had about permissions: "Will this event be allowed to trigger my Lambda function? Or will I have to assign it an IAM role?"

And, as shown in the screenshot, CloudWatch completely handles assigning the required permission for the event to function on its target, so I didn't have to worry about extra work and testing.

# Final Words

I hope this article was useful to you in some way, whether you're interested in cloud development, website makers, or just programming in general. 

If you own and manage a Squarespace website (or any website maker) that has mysteriously broken and are reading this in panic mode, I advise you to visit their status page for updates. Outages like these usually get resolved within an hour.

I am planning to build a cloud native web application too that will implement and automate this solution so I can offer it to my future and existing clients. You can follow me for updates as I build it in public. 👨‍💻  
  
For more tips and insights on cloud and web development follow me on Twitter [@adham_benhawy](https://twitter.com/adham_benhawy).

