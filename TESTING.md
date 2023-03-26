# The Good Reader

[Main README.md file](/README.md)

[View live project here](https://the-good-reader.herokuapp.com/)

[View GitHub repository](https://github.com/pagioro/The_Good_Reader)

***
## Contents
* [Test User Stories](#Test-user-stories)
* [Manual Testing](#Manual-testing)
* [Code Validation](#Code-validation)
    * [HTML](#HTML)
    * [CSS](#CSS)
    * [Python](#Python)
    * [Javascript](#Javascript)
* [Lighthouse](#Lighthouse)
* [Browser Validation](#Browser-validation)
* [User Testing](#User-testing)


***

## **Test User Stories**

1. As a customer I can view a list of products so that I can select some purchases.
- Any customer can access directly from the Shop Now link in the Home nav bar where all the books are displayed by category or from the All Products view in the Books dropdown link in the nav bar.

2. As a customer I can view a specific product category so that I can find products I'm interested in without having to search through all products.
- Any customer can access each category directly from the Shop Now link in the Home nav bar where all the categories are displayed or from the Books dropdown link in the nav bar or from the All Products view, where buttons link to all the different categories.

3. As a customer I can view individual product details so that I can identify the author, name, price, description and image.
- Any customer can click the image of a certain book to get redirected to a detailed view. The customer gets all information about that specific book, such as image, author, name, price and description.

4. As a customer I can view the total of my purchases so that I can define my investment at any time.
- Any customer can click the shopping bag icon in the nav bar to get a full overview of their Shopping bag. The Keep Shopping button can be clicked if the Shopping bag is empty. If there are items in the bag, the user will see the bag total, delivery, grand total, image, name, sku, price each, subtotal, quantity, total cost and also has the option to change the quantity or remove the item. The customer can keep shopping or proceed to secure checkout.

5. As a customer I can view the about option so that I can view the description, email and phone number of the about option.
- Any customer can access the About link in the nav bar and gets information about the description, email and phone number.

6. As a customer I can view the author's option so that I can view the photo, name, country, known for and description of the author's option.
- Any customer can access the Authors link in the nav bar and gets information about the photo, name, country, known for and description of the author.

7. As a customer I can view the Contact Us option so that I can view the options to fill out my name, email, title and description to submit them of the Contact Us option.
- Any customer can access the Contact link in the nav bar or foot pager and fill out the name, email, title and description to send to the site administrator user.

8. As a customer I can view the Bug Report option so that I can send a bug report and fill out my title, description, browser, os and email.
- Any customer can access the Bug Report link in the nav bar and fill out the title, description, browser, os and email to send to the site administrator user.

**Registration and User Accounts**

9. As a customer I can easily register for an account so that I can have a personal account and view my profile.
- Any customer can click the My Account icon in the nav bar to register for an account. The registration requires filling out the username, email address, password and password confirmation.

10. As a customer I can subscribe to receive a newsletter so that I can fill out my email address and subscribe.
- Any customer can access the Subscribe to receive our newsletter option foot pager and fill out the email address to send to the site administrator user the order to receive the newsletter.

11. As a site user, I can log in or out to access my personal account information.
- Any site user can click the My Account icon in the nav bar to log in for an account. The login requires filling out the username and password. The Sign In option has the Remember me and Forgot password options.

12. As a site user I can recover my password to regain access to my account if I forget it.
- Any site user can click the My Account icon in the nav bar to log in for an account. The Forgot password option requires filling out the email address and confirm clicking the Reset my password option. The site user receives an email to change the password access.

13. As a site user I can receive an email confirmation after registering to confirm my account registration was successful.
- Any customer receives an email confirmation after confirming registering an account in the My Account icon in the nav.

14. As a site user I can have a personalized user profile to view my order history and save my default delivery information.
- Any site user can click the My Account icon in the nav bar to access the My Profile option that shows default delivery information and order history. The default delivery information can be updated and then click on the Update information button.

**Sorting and Searching**

15. As a customer I can sort the list of available products so that I can identify sort by name, author, best and high price.
- Any customer can access directly from the Shop Now link in the Home nav bar where all the books are displayed and can be sorted by name, author, price low to high and price high to low or from the All Products view in the Books dropdown link in the nav bar.

16. As a customer I can search for a product by title, author or keyword so that I can find a specific product I want to purchase. 
- Any customer can access directly the Search bar in the nav bar where the book can be searched by title, author or some keyword.

17. As a customer I can see what I have searched for and the number of results so that I can decide whether the product I want is available.
- Any customer can see the search result of books with the number of books found.

**Purchasing and Check out**

18. As a customer I can select a product when purchasing it so that I can ensure I choose the right product and quantity.
- Any customer can select the book, fill out the quantity and click Add to bag option.

19. As a customer I can add a product to my bag so that I can store into my bag items before I define the total order.
- Any customer can select the book, fill out the quantity and click Add to bag option.

20. As a customer I can view items in my bag to be purchased so that I can identify the total value of my purchase and all items I will receive.
- Any customer can click the shopping bag icon in the nav bar to get a full overview of their Shopping bag. The Keep Shopping button can be clicked if the Shopping bag is empty. If there are items in the bag, the user will see the bag total, delivery, grand total, image, name, sku, price each, subtotal, quantity, total cost and also has the option to change the quantity or remove the item. The customer can keep shopping or proceed to secure checkout.

21. As a customer I can easily adjust the number of individual items in my bag so that I can make changes to my purchase before checkout.
- Any customer can click the shopping bag icon in the nav bar to get a full overview of their Shopping bag. The Keep Shopping button can be clicked if the Shopping bag is empty. If there are items in the bag, the user will see the bag total, delivery, grand total, image, name, sku, price each, subtotal, quantity, total cost and also has the option to change the quantity or remove the item. The customer can keep shopping or proceed to secure checkout.

22. As a site user I can choose default delivery information so that I can check out my purchase.
- Any site user can click the Secure Checkout option in the Shopping bag to complete the order. The details require filling out the full name and email address. The delivery shows default delivery information and the information can be altered. The site user can proceed to purchase by clicking the Complete order button.

23. As a site user I can fill out my default delivery information so that I can save this information to my default delivery information.
- Any site user can click the My Account icon in the nav bar to access the My Profile option that shows default delivery information. The default delivery information can be updated.

24. As a customer I can view an order confirmation after checkout so that I can verify that my order is correct.
- Any customer after Completing the order can view the order confirmation.

25. As a customer I can receive an email confirmation after checkout to keep my purchase warranty.
- Any customer after Completing the order can view the order and receive an email confirmation.

**Admin and Store Management**

26. As a site administrator user I can create, view, update and delete products so that I can add new items, change prices, descriptions, and images, and remove items that are no longer for sale.
- The site administrator user can have disposable the site administration option so that I can add, change and delete books.

27. As a site administrator user I can have disposable the product management option so that I can create new products.
- The site administrator user can click the My Account icon in the nav bar to access the Product management which requires filling out the category, sku, name, author, description, price and image to create a new product.

[Back to content](#contents)

## **Manual Testing**

#### Navigation Bar (Nav-Bar)

* Expected result: The navigation bar should be visible on every page of the site. If the page is rendered on different screens the navigation bar should be proportionally visible.
* Test: Access every page of the site to check if the navigation bar is visible. View the navigation bar on different size screens to check the proportionality of the navigation bar.
* Result: approved.

#### Logo

* Expected result: The user should be redirected to the home page when clicking The Good Reader logo.
* Test: Click The Good Reader logo from all different pages of the site.
* Result: approved.

#### Home Link

* Expected result: The user should be redirected to the Home page when clicking the Home link. When viewing the Home page there are a welcome text, a delivery information text and a Shop Now link option.
* Test: Click the Home link from all different pages of the site in accordance with the expected result.  
* Result: approved.

#### About Link
* Expected result: The user should be redirected to the About page when clicking the About link.
* Test: Click the About link from all different pages of the site.
* Result: approved.

#### Books Link
* Expected result: The dropdown menu should appear displaying the All Books option and the different categories when clicking the Books link.
* Test: Click the Books link from all the different pages of the site.
* Result: approved.

#### Books Link - All Books
* Expected result: The user should be redirected to the All Books page when clicking the All Books link. On the top should appear categories buttons, sort by button and the number of products displayed. The user should choose to sort the books by name, author, and ascending/descending prices. Each book should show an image, author, name and price.
* Test: Click the All Books link from all the different pages of the site in accordance with the expected result. 
* Result: approved.

#### Books Link - Different categories
* Expected result: The user should be redirected to the Books category page when clicking the category link. On the top should appear categories buttons, sort by button, Products Home link and the number of products displayed. Each book should show an image, author, name and price.
* Test: Click the category link from all the different pages of the site and check the result in accordance with the expected result. Repeat the test for all categories.
* Result: approved.

#### Books Detail
* Expected result: The user should be redirected to the Book detail when clicking the specific book. Each book should show the image, author, name,  price and description. The quantity option should show with plus and minus buttons. The Keep shopping and Add to bag buttons should show. The Keep shopping should take the user back to the All Products page. The Add to the bag should take the user to the bag option. 
* Test: Click in the specific book and check the result in accordance with the expected result. Try to enter an invalid quantity input such as letters and check the message Enter a number when the button Add to bag is clicked. 
* Result: approved.

#### Shop Now link
* Expected result: The user should be redirected to the All Books page when clicking the Shop Now link. On the top should appear categories buttons, sort by button and the number of products displayed. Each book should show an image, author, name and price.
* Test: Click the Shop Now link on the Home page and check the result in accordance with the expected result.
* Result: approved.

#### Authors Link
* Expected result: The user should be redirected to the Authors page when clicking the Authors link. Each author should show the photo, name, country, known for and description.
* Test: Click the Authors link from all different pages of the site and check the result in accordance with the expected result.
* Result: approved.

#### Contact Link
* Expected result: The user should be redirected to the Contact Us page when clicking the Contact link. The user fills out the name, email, title and description. The user should click on the Send button. The site administrator user should view the contact data disposable the site administration option so that can be added, changed and delete the contact.
* Test: Click the Contact link from all different pages of the site.
Fill out the name, email, title and description. Click on the Send button. As a site administrator user view the contact data disposable the site administration option and adds, changes and deletes the contact.
* Result: approved.

#### Bug Report Link
* Expected result: The user should be redirected to the Bug Report page when clicking the Bug Report link. The user fills out the title, description, browser, os and email. The user should click on the Send button. The site administrator user should view the bug report data disposable the site administration option so that can be added, changed and delete the bug report.
* Test: Click the Bug Report link from all different pages of the site.
Fill out the title, description, browser, os and email. Click on the Send button. As a site administrator user view the bug report data disposable the site administration option and adds, changes and deletes the bug report.
* Result: approved.

#### Search Field
* Expected result: When entering search criteria in the Search Field the items matching should be displayed. The number of matches should also be presented. If no items match the search criteria it should be shown that there are no products found when searching for that specific criteria. 
* Test: Entered different search criteria to test search functionality in accordance with the expected result. 
* Result: approved.

#### Footer
* Expected result: The footer should be visible on all pages bottom of the site. 
* Test: Check the footer is visible on all pages bottom of the site.
* Result: approved.

#### Footer Social Media Links
* Expected result: The Facebook, Instagram and Twitter icons in the footer linking to the social media accounts should be opened up in new tabs when clicked.
* Test: Click the social media icons in the footer and check the options opened up in new tabs when clicked.
* Result: approved.

#### Newsletter Subscription
* Expected result: The user should be entering an email address and the email address should be visible in the site administrator user Mailchimp account.
* Test: Enter an email address, click on subscribe button and check the successful message. Enter an invalid email address without an @ and check the message asking for an email address valid. Access the mailchimp.com site administrator user account and check the email address shown in the audience all contacts option.
* Result: approved.

#### My Account Link
* Expected result: When clicking the My Account link a dropdown menu should appear, displaying the Register and Login options if the user is logged out or displaying the My Profile and Logout options if the user is logged in or displaying the Product Management, My Profile and Logout options if the site administrator user is logged in.
* Test: Click the My Account link when the user is logged in or not and when the site administrator user is logged in accordance with the expected result.
* Result: approved.

#### Login
* Expected result: Login of the site.      
* Test: Click the Login option on the My Account icon and should be redirected to the Sign-in page. 
The login requires filling out the username and password. The Sign In option has the Remember me and Forgot password options.
If the user has forgotten the password should request to have a password reset by clicking the Forgot Password button and filling out the email address and clicking the Reset my password button. The site user should receive a reset link email to change the password access.
Try entering the incorrect login and should be shown the message The username and/or password you specified are not correct.
Try entering the correct login and should be shown the My Profile e Logout options on the My Account icon.
* Result: approved.

#### 
*
*
*

#### 
*
*
*





## **Code Validation**

#### **HTML**

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML.

***Results:***

All files tested passed with no errors. 

#### **CSS**

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the CSS.

All files tested passed with no errors. 

#### **Python**

The [PEP8 Python Validator Code Institute](https://pep8ci.herokuapp.com/) was used to validate the Python code. 

All files tested passed with no errors. 

#### **JavaScript**

The JavaScript was tested using [https://jshint.com/](https://jshint.com/). 

All files tested passed with no errors. 

[Back to content](#contents)

## **Lighthouse**

The site has been tested with Lighthouse.

![Lighthouse](/static/site_images/lighthouse.png)

[Back to content](#contents)

## **Browser validation**

The site has been tested using the following browsers:

- Chrome
- Edge
- Firefox
- Safari

[Back to content](#contents)

## **User testing**

Many users tested the site on all screen sizes during its development.

[Back to content](#contents)