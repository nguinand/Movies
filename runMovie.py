# '''Main class that runs the movie stuff'''
import pageGenerator
import movie
starTrek = movie.movie(
    "Star Trek Into Darkness", "Captain Kirk leads a manhunt to a war-zone. ",
    "http://www.moviedeskback.com/wp-content/uploads/2012/12/Star-Trek-Into-Darkness.jpg",
    "https://www.youtube.com/watch?v=r5gdbUC9mWU")

oblivion = movie.movie(
    "Oblivion", "A veteran assigned to extract Earth's remaining resources.",
    "http://1.bp.blogspot.com/-cMNFRJbgSMQ/UTFMS-TZH7I/AAAAAAAAAJc/_qh0uR6G1Bw/s1600/oblivion+movie.jpg",
    "https://www.youtube.com/watch?time_continue=156&v=XmIIgE7eSak")

inception = movie.movie(
    "Inception", "A thief, who steals corporate secrets through the use of dream-sharing technology. ",
    "http://images2.fanpop.com/image/photos/12300000/Inception-Wallpaper-inception-2010-12396931-1440-900.jpg",
    "https://www.youtube.com/watch?v=d3A3-zSOBT4"
)

interstellar = movie.movie(
    "Interstellar", "A team of explorers travel through a wormhole in space.",
    "https://bfox.files.wordpress.com/2014/11/interstellar-movie.jpg",
    "https://www.youtube.com/watch?v=2LqzF5WauAw"
)

gravity = movie.movie(
    "Gravity", "Two astronauts work together to survive after an accident which leaves them stranded in space.",
    "http://2.bp.blogspot.com/-bDCAq-SUxjc/UfWitIqLKKI/AAAAAAAAADA/4J4z7QN29Z8/s1600/Gravity+poster+(3).jpg",
    "https://www.youtube.com/watch?v=k0ijEEivCbg"
)

movieList = [starTrek, oblivion, inception, interstellar, gravity]
# Calls pageGenerator class that calls the open_movies_page function. movieList array is passed.
pageGenerator.open_movies_page(movieList)
