class movie():
    '''The movie class. Has a constructor that initializes the movies title, storyline, poster image, and trailer'''
    def __init__(self, title, story, image, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
