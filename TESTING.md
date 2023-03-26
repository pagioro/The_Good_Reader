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


[Back to content](#contents)

## **Manual Testing**

### Header

#### Navigation Bar (Nav-Bar)

* Expected Outcome: The navigation bar should be visible on every site page. The navigation bar should toggle if the page is rendered on smaller screens for a better user experience. 
* Test: Visit every site page to check if the navigation bar is visible. View the navigation bar on different size screens to check the responsiveness of the navigation bar and toggle function. 
* Result: The navigation bar is visible on every site page. The links are toggled for a better user experience when viewed on smaller screens. 
* Verdict: Code functions as intended.

#### Logo

* Expected Outcome: When clicking the logo, the user should be redirected to the home page.
* Test: I tried clicking the logo from all different site pages as a logged-in user or not. 
* Result: Whenever I clicked the logo, I was redirected to the home page.
* Verdict: Code functions as intended.

#### Home Link

* Expected Outcome: The user should be redirected to the Home page when clicking the Home link.
* Test: I tried clicking the Home link from all different pages on the site, both as a logged-in user and not.
* Result: Whenever I clicked the Home link, I was redirected to the home page. 
* Verdict: Code functions as intended.



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