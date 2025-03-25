def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return {number for number in xs if number in ys}