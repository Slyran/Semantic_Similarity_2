import spacy
nlp = spacy.load('en_core_web_md')

# The description of the movie we want to find a 
# similar movie for, in this case, Planet Hulk
movie_description = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")
similarity_list = []

# Compares each movie description in the file to the
# description of Planet Hulk and saves the similarity
# score in a list
with open("movies.txt") as file:
    for line in file:
        split_line = line.split(":")
        movie = nlp(split_line[1])
        similarity_list.append((split_line[0], (movie_description.similarity(movie), line)))

# Sorts the list by similarity score and prints the
# movie with the highest similarity score
similarity_list.sort(key=lambda x: x[1], reverse=True)
print(similarity_list[0][0])