from model.movie import Movie
from model.user import User



def test_add_movie(app):
    new_movie = Movie.random()
    app.ensure_login_as(User.Admin())
    app.add_movie(new_movie)
    assert app.is_added_movie(new_movie)
    app.logout()

