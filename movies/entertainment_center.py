import media
import fresh_tomatoes

#This script displays 6 of my favorite movies on a website 
                     
almost_famous = media.Movie("Almost Famous",
                            "A high-school boy is given the chance to write a story for Rolling Stone Magazine about an up-and-coming rock band as he accompanies it on their concert tour.",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/d/dd/Almost_famous_poster1.jpg/220px-Almost_famous_poster1.jpg",
                            "https://www.youtube.com/watch?v=KgjFYmuXbro")

stuck_in_love = media.Movie("Stuck in Love",
                            "An acclaimed writer, his ex-wife, and their teenaged children come to terms with the complexities of love in all its forms over the course of one tumultuous year.",
                            "http://ia.media-imdb.com/images/M/MV5BMTU1NzI5MDU3OV5BMl5BanBnXkFtZTcwNTE0NDMzOQ@@._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=ORKb_Vqbz9U")

tangled = media.Movie("Tangled",
                      "The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.",
                      "http://img2.wikia.nocookie.net/__cb20110929034113/disney/images/c/ca/Tangled_rapunzel_poster_20.jpg",
                      "https://www.youtube.com/watch?v=pyOyBVXDJ9Q")

hp_gof = media.Movie("Harry Potter and the Goblet of Fire",
                     "Harry finds himself mysteriously selected as an under-aged competitor in a dangerous tournament between three schools of magic.",
                     "http://img3.wikia.nocookie.net/__cb20141215162340/harrypotter/images/b/b5/Harry_Potter_and_the_Goblet_of_Fire_film_.jpg",
                     "https://www.youtube.com/watch?v=7lJ6Suyp1ok")

office_space = media.Movie("Office Space",
                           "Three company workers who hate their jobs and decide to rebel against their greedy boss.",
                           "http://ia.media-imdb.com/images/M/MV5BMjQ0MTE1NDAwNl5BMl5BanBnXkFtZTYwNzMxMDE5._V1_.jpg",
                           "https://www.youtube.com/watch?v=_IwzZYRejZQ")

seven = media.Movie("Seven",
                    "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi.",
                    "http://www.impawards.com/1995/posters/seven_ver1.jpg",
                    "https://www.youtube.com/watch?v=J4YV2_TcCoE")
#order of this list is the order in which they will be shown on the website.                    
movies = [almost_famous, stuck_in_love, tangled, hp_gof, office_space, seven]
#opens the website with proper formatting
fresh_tomatoes.open_movies_page(movies)
