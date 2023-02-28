
class Song:
    def __init__(self, title, runtime, genre):
        self.title = title
        self.runtime = runtime
        self.genre = genre

    def get_title(self):
        return self.title.title()
    
    def get_runtime(self):
        return self.runtime

    def get_genre(self):
        return self.genre

    def get_record(self):
        return self.record

    def get_artist(self):
        return self.record.artist