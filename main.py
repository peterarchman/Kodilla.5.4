class MovieLibrary:
    def __init__(self, title, year, genre, number_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_plays = number_of_plays

        self.current_number_of_plays = 0

    def play(self):
        self.current_number_of_plays += 1

    def __str__(self):
        return f"{self.title}({self.year})"



class SeriesLibrary(MovieLibrary):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number}, E{self.episode_number}"

movie1 = MovieLibrary(title = "The Code" ,year = "1994", genre = "comedy", number_of_plays = 0 )

series1 = SeriesLibrary(title = "Vikings", year = "2019", genre = "comedy", number_of_plays = 5, episode_number = 3, season_number = 2)


movie_list = [movie1]
series_list = [series1]

my_movie_series_list = movie_list + series_list