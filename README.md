# EOL lambda - An example of Amazon Lambda function written in Python

## Overview

I made this easy function to create a simple Amazon Lambda demo that cast a common news [Elotrolado.net webpage](https://www.elotrolado.net/) into a json file. It respects the pagination of the original page and returns posts with this structure:

```json
{
    "results": [
        {
            "title": "Post Title",
            "link": "/post_link",
            "comments": "0",
            "summary": "Post summary",
            "datetime": "2018-10-08T16:47:35+00:00",
            "author": "Nickname",
            "category": "/category/subcategory",
            "thumbnail": "https://path-to-image.jpg"
        },
        "..."
    ]
}
```

Query params:
* Page: the number of page to get their news

## How to deploy

To deploy that, you have to pack it in a *.zip with their dependencies. It means that if you need to use an external library, you have to pack it with the script.

Create a virtualenv and install the requirements. Then zip it with all of files and folder placed in <virtualenv_folder>/Lib/site-packages. Then, upload the result zip file to Amazon Lambda.
