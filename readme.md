&cmd /k workon apis
workon apis
python manage.py runserver 0.0.0.0:8000
localhost:8000



https://github.com/jazzband/django-auditlog/blob/master/docs/source/usage.rst
https://django-auditlog.readthedocs.io/en/latest/usage.html

pip install django-auditlog
manage.py migrate


path /Users/salvadorortiz/apis/lib/python3.8/site-packages/auditlog/ for JSONField conflict

from jsonfield import JSONField
field = JSONField(max_length=200)





Summary
This challenge is designed to put your skills to the test by designing and building a good RESTful API to manage a small movie rental.

Time frame
    Max 7 days.

Requirements
    (X) 1. Only users with admin role are allowed to perform the following actions:
        Add a movie
        Modify a movie
        Remove a movie
        Delete a movie
    (X) 2. Movies must have a title, description, at least one image, stock, rental price, sale price and availability.
    (X) 3. Availability is a field of movies, which may only be modified by an admin role.
    (X) 4. Save a log of the title, rental price and sale price updates for a movie.
    ( ) 5. Users can rent and buy a movie. For renting functionality you must keep track when the user have to return the movie and apply a monetary penalty if there is a delay.
    ( ) 6. Keep a log of all rentals and purchases (who bought, how many, when).
    (X) 7. Users can like movies.
    (X) As an admin I’m able to see all movies and filtering by availability/unavailability.
    (X) As an user I’m able to see only the available movies for renting or buying.
    (X) The list must be sortable by title (default), and by popularity (likes).
    (X) The list must have pagination functionality.
    (X) Search through the movies by name.
Security requirements
    ( ) 1. Add login/logout functionality.Preferably JWT.
    (X) 2. Only admins can add/modify/remove movies.
    ( ) 3. Only logged in users can rent and buy movies.
    (X) 4. Only logged in users can like movies.
    (X) 5. Everyone (authenticated or not) can get the list of movies.
    (X) 6. Everyone (authenticated or not) can get the detail of a movie.
    ( ) 7. Publish your work using heroku andsharethe link with us.
Extra credit
    ( ) 1. Recovery and forgot password functionality (send email).
    ( ) 2. Confirming account (send email)
    ( ) 3. Build a small frontend app and connecting to the API.
    ( ) 4. As an user with admin role I want to be able to change the role of any user.
    ( ) 5. Unit test, at least 80% of coverage.
    ( ) 6. Include a dockerfile for production deployments.
Keep in mind
    ( ) 1. You are free to use any package, library and weapons for the battle as long as you can justify their use.
    ( ) 2. You may use any kind of database you like.
    ( ) 3. Provide a database dump so we can replicate the database locally.
    ( ) 4. POSTMAN will be used to evaluate the API. It would be great if you can provide us with a collection to test your API.
    ( ) 5. Follow best RESTful API practices. Take a look on this guidehttps://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
    ( ) 6. Use git and do small commits to facilitate the evaluation of progress.
    ( ) 7. Include areadme.mdfile with instructions on how to setup your project locally to test it. (This is super important, if we cannot install it and run it easily we cannot evaluate it).
    ( ) 8. Upload your solutionto your Github or Gitlab accountand share a link with your evaluator.
    ( ) 9. The test has been designed with enough time to do a good job, so don’t cut any corners, take your time and watch for quality. We evaluatecode readability, comments, formatting, performance and re-usability.
