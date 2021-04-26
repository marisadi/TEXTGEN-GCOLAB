# Text-Generator-GPT-2
A Text Generator with OpenAI GPT and Python using Flask and Heroku to deploy

Built from follwing this tutorial:
https://www.youtube.com/watch?v=WRVx8vGDKf4

Model trained using google colab:
https://colab.research.google.com/drive/1_wDbvZdWkFPrJluHmb3_0MWDfY5G8Lz9?authuser=2#scrollTo=8DKMc0fiej4N

Deployment:
https://stackabuse.com/deploying-a-flask-application-to-heroku/

Deploying this project with a model to Heroku does not work:
-----> Compressing...
 !     Compiled slug size: 572.9M is too large (max is 500M).
 !     See: http://devcenter.heroku.com/articles/slug-size
 !     Push failed
 
Fine-tuned model is too large to upload to Git
I could not get Git LFS to work.
Could try using DVC with a heroku and dvc packpack but I don't think that will change that it's too large to deploy with Heroku

Also using for google colab:
- removed from requirements text:
 - google-auth==1.29.0
 - google-auth-oauthlib==0.4.4
 - google-pasta==0.2.0
