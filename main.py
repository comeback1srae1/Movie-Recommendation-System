from flask import Flask, request, render_template
from model import movie_df, recommendate_movie

app = Flask(__name__)


@app.route('/select-movie')
def select_movie():
    return render_template('index.html', movies=zip(movie_df['movieId'], movie_df['title']))


@app.route('/give-recommendations', methods=['POST'])
def give_recommendation():
    watched_movies = request.form.getlist('watched_movies')
    watched_movies = [int(i) for i in watched_movies]
    watched_movies = movie_df[movie_df["movieId"].isin(watched_movies)]

    recommendations = recommendate_movie(watched_movies)

    return render_template('recommendations.html', recommendations=recommendations)


def main():
    app.run()


if __name__ == '__main__':
    main()
