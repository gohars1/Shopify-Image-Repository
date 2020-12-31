# Shopify-Image-Repository
Shopify Backend and SRE Intern Challenge 
For the Shopify Backend Developer and SRE Intern challenge, I created an "Image-Repository", where a user can create an account and purchase images. I used Django to serve the web application and sqlite3 to store user and image data. The default store is made up of images of my hobbies, so when you use the application you get to know a bit about me :).

### Setup

To run this application you must have python installed.

To use Django, you can install it globally on your machine or install it in a python virtual environment.

Once you have Django installed, you should be able to move on to Usage.

### Usage
To get started clone the repo with the following command:

```
git clone https://github.com/gohars1/Shopify-Image-Repository.git
```
Once the repo is cloned, enter the directory imagerepository. You can do this with the following command:
```
cd imagerepository
```
Finally, you can run the server with the following command:
```
python manage.py runserver
```
Once the server is run, you can begin using the web application with the following URL: http://127.0.0.1:8000/

Here you should encounter the following screen:

![alt text](https://github.com/gohars1/Shopify-Image-Repository/readme-snapshots/login.JPG)

If you have already created an account, you can click "login". Otherwise, you can create a new user with the button "Create new user"

From here, you will be redirected to this login page, where you enter your credentials.

Once you are signed in, you will see the following screen:
`screen shot`

Click on "View Store" to buy images.

Once you buy the images you like, click the Home Button on the navbar.

Now, click on the button "Your photos" and you should see a collection of the photos you purchased in your store.
