class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.count += 1

        # Update genres list and genre_count dictionary
        if genre not in Song.genres:
            Song.genres.append(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Update artists list and artist_count dictionary
        if artist not in Song.artists:
            Song.artists.append(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
