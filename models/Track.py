class Track(object):
    def __init__(self, track_id, name, artists, album):
        self.__track_id = track_id
        self.__name = name
        self.__artists = artists
        self.__album = album

    def __str__(self) -> str:
        return str(self.__dict__)
