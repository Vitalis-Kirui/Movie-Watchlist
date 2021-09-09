from flask import  render_template,request,redirect,url_for
from app import app
from app.request import get_movies, get_movie, search_movie
from app.models import review
from .forms import ReviewForm

Review = review.Review

#index page view function
@app.route("/")
def index():
    """
    View root page function that returns the index page and its content.
    """
    title = "Vitalis Movie Review Site"
    # message = "Movie Review Site"

    #Getting movie categories
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search', movie_name = search_movie))

    else:
        return render_template("index.html", title=title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)

#Movie page function
@app.route('/movie/<int:id>')
def movie(id):
    """
    Movie page function that returns the movie details page and its content.
    """
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    return render_template("movie.html", title=title, movie=movie, reviews = reviews)

#Search movie by name function
@app.route('/search/<movie_name>')
def search(movie_name):
    """
    View function that returns the search results in a template
    """
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', movies=searched_movies)


@app.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie', id=movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)
