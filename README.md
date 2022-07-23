# Bimmerreviewer
Bimmerreviewer is a social media web application where users can create post reviews about their cars. Users will be able to create an account and upload information about their car with a picture. Users will be able to comment on a post and like the review post with a counter that displays the upvotes. The target group here is users that drive a BMW car, the goal with this site is that users will be able to display pro and cons about a specific car model that will be shared on the site.
![Responsiv image frontpage](docs/homepage.png)

# User stories

## site users
* As a user I would like to be able to create/delete and edit a post.

* As a user I would like to be able to create an personal account on the site.

* As a user I would likt to be able to comment on a post/review.

* As a user I would likt to be able to like a post/review and to know how many other have alredy liked the same post.

* As a user I would like to be able to search on the site after a certain title in the review.

* As a user I would like a certain car model to be categorized so that I can click on the car model

* As a user I would like to be able to upload a picture on the post review.

* As a user I would like to be get notified if I click like on a post or if a comment have been successfully created.

* As a user I would like a map where meetups can be shown and displayed.

## admin
* As admin i would like to inspect a post before it is approved and published on the site.

* As admin I would like to delete a comment/post if it is inappropriate.


# Features and functionality 

## Frontpage
The user will be welcomed with a intro and animation on the front page, on the top is a navigation menu and on the left top is a search bar. The user will be able to search after post with a certain title with the help of the search bar. The intro text will present with a button that takes the user to a register page. If the user is alredy logged in then the register button wont be displayed.
![Frontpage](docs/home-3.png)

On the bottom there is a Google map along with a footer, the map is only for development purpose for this project.
![Google map page](docs/home-2.png)

## Account
If the user is not logged in to the page then the following will be displayed:

![Account not logged in](docs/home-4.png)

if the user is logged in to the page then the following will be displayed:

![Account choiches](docs/home-5.png)


## The register page: 
Here the user can register to create an account. After filling in the information the user will get a conformation email so that the user can confirm the account. If the user types in an email or username that alredy exist then the user gets a message display informing that.

![Register page](docs/register.png)

## Verify email:
After the user have registered an account the following page will be displayed and an email will be sent to verify the email to the account that the user typed in:
![Verify](docs/verify.png)

## Confirm email:
Afte the user have recived the email and clicked on the link the user will be directed to this page below to confirm their email account:
![Confirm](docs/confirm.png)

## Sign in:
After clicking confirm email adress the user will be directed to the sign in page, a message will be displayed telling the user that the email adress have been confirmed:
![Confirmed](docs/confirmed.png)


Everytime the user sign in a message will be showing displaying the username:
![Sign in message](docs/sign-message.png)

## Create review:

![Create review](docs/create-review.png)

This is where the magic happens, the user will be presented with a text explaining what to do. The title here must be unique and it the user tries to type in a title that alredy exist then a message will be displayed. If the user tries to upload a image to big or another format then a picture the page will display an "500" error. The price can't go below 0 and the year along with the fueltype only have prepopulated choiches thanks to the model that I created. If no image is uploaded then a default image will be uploaded instead of an empty file.


After the user have clicked "upload review" the message below will be displayed:

![Review message](docs/review-message.png)

Admin needs to approve the post before it can be seen on the webpage.On this page admin can review the created post and see all the data that have been posted by the user.
![Admin approve](docs/admin-approve.png)






