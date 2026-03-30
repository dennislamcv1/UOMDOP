# ── FIXED FUNCTION ────────────────────────────────────────────────────────────

def calculate_avg(movies, score_type):
    """
    Calculates the average score for a given score_type across all movies
    that have a non-None value for that field.

    Parameters:
        movies (list): A list of dictionaries containing all the movie data
        score_type (string): The score key to average (e.g. "imdbRating",
                             "Jumpscare_rating")

    Returns:
        float: Average value rounded to one decimal point
    """
    sum_score = 0
    count = 0                              # FIX 2: track how many movies have a score
    for movie in movies:
        score = get_value(movie, score_type)
        if score:
            sum_score += float(score)      # FIX 1: += (accumulate), not = (overwrite)
            count += 1
    return round(sum_score / count, 1)     # FIX 2: divide by count, not len(movies)


# ── WHAT WAS WRONG ────────────────────────────────────────────────────────────
#
# Bug 1 – assignment instead of accumulation (line inside the if block):
#
#   ORIGINAL:  sum_score = float(movie[score_type])
#   FIXED:     sum_score += float(score)
#
#   The original code *overwrites* sum_score on every iteration, so after the
#   loop it only holds the last movie's score — not the running total.
#   Using += correctly accumulates the sum.
#   (Also switched from movie[score_type] to the already-retrieved `score`
#   variable, which is cleaner and consistent with the get_value() call above.)
#
# Bug 2 – wrong denominator:
#
#   ORIGINAL:  return round(sum_score / len(movies), 1)
#   FIXED:     return round(sum_score / count, 1)
#
#   Not every movie has jumpscare data (get_jumpscares returns (None, None)
#   for unmatched titles). Dividing by the total number of movies instead of
#   the number that actually have a score produces an artificially low average.
#   Tracking `count` separately and dividing by it gives the true average.
