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

## Sign out:
When the user clicks log out the following page will be shown, if the user clicks sign out a message will be displayed telling the user that the sign out was completed.

![Sign out](docs/sign-out.png)

![Sign out](docs/sign-message-out.png)


Everytime the user sign in a message will be showing displaying the username:
![Sign in message](docs/sign-message.png)

## Create review:

![Create review](docs/create-review.png)

This is where the magic happens, the user will be presented with a text explaining what to do. The title here must be unique and it the user tries to type in a title that alredy exist then a message will be displayed. If the user tries to upload a image to big or another format then a picture the page will display an "500" error. The price can't go below 0 and the year along with the fueltype only have prepopulated choiches thanks to the model that I created. If no image is uploaded then a default image will be uploaded instead of an empty file.


After the user have clicked "upload review" the message below will be displayed:

![Review message](docs/review-message.png)

Admin needs to approve the post before it can be seen on the webpage.On this page admin can review the created post and see all the data that have been posted by the user.
![Admin approve](docs/admin-approve.png)

## My reviews:
This page shows all the personal user reviews that the user have uploaded, only the post that have the same user id as the user that is logged in is displayed here. And each post have 3 buttons, "update" "delete" and "view". Only authenticated user can see this page. 

![My reviews](docs/my-reviews.png)

## Update review:
When the user clicks the update review button the page below will be shown. Here the user can just update the data and click "update review".
![Update reveiw](docs/update-review.png)

Afte the user have updated the info followin message will be shown:
![Update message](docs/update-message.png)

## Delete review
When the user clicks the "delete review" button the following page will be displayed:

![Delete](docs/delete-review.png)

After the user confirms the delete following message will be displayed and the review is no longer avalible.

![Delete message](docs/delete-message.png)

## View review
This is the page where all the detailed information is shown, all the data that the user inputed in the create review page will be shown on this page below:
![View page](docs/view-page.png)

## Comments
On the same page the user will be able to comment and like a review.
After clicking "add comment" user will be directed to the page below to add a comment. If there are no comments a text will be displayed saying "no comments yet". The user can type in a author and then type in the comment in the bodyfield.

![Comment](docs/comment.png)

After the comment have been posted message will be displayed:

![Comment message](docs/comment-message.png)

The comment will be displayed like the picture below as you can see the name that the user typed before and date is also shown.User can also hide and show the comments with the help of a button.

![Show comment](docs/show-comments.png)

## Like 
The user will be able to like a post and a counter is displaying showing how many have liked the post:

![Like](docs/likes.png)

When the user likes a post the counter will increase and a message will be displayed telling the user that they have liked this post or unliked a post.

![Like message](docs/like-message.png)

## Category
The category page is displaying all the reviews that is in the relevant category. When the user creates a review depending on which category the user chooses in the input field, the review will be displayed on that page that the user have choosen. In the picture below, the user choose 3-SERIES as a category. The review will then be displayed on the 3-SERIES category page. Only the 3-SERIES will be shown on this page.

![Category](docs/category.png)

There are 4 diffrent categories that the user can choose from when creating the review on the create review page. The image below shows all the categories:

![Category nav](docs/category-nav.png)

## Show all reviews
This is the page where all the reviews are displayed from all the users on the site. It dosen't matter what category is choosen all the reviews are collected and shown here. This page is not personal and anyone can view this page

![All reviews](docs/all-reviews.png)

## Search
The user can search after a certain title after clicking search the post that have the same or similar title as the inputed serach word will be displayed. Also whatever the user types in will also be shown on the page.The username is also displayed to the left so that the user will always know who is logged in.

![Search](docs/search.png)

If the user types nothing the following page will be displayed:

![Search empty](docs/search-empty.png)

## Contact us
If the user have any questions there is a contact us page where an email is displayed.

![Search](docs/contact.png)

## Please log in
When the user tries to access a page that requires to log in then the following page will be shown the word log in is also a link that takes the user to the sign in page:

![Please log in ](docs/please-log.png)


## 404 and 500 error page:
If a page is not found or if there is a error the following page will be displayed:
![Error page ](docs/error-page.png)

## Back to top:
A button that will automatically take the user back up to the top of the page when the user clicks it.

![Back to top](docs/back-top.png)


# Future ideas















