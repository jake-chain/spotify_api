class Track(object):
    # Construtor da classe
    def __init__(self, track_id, name, artists, album):
        self.__track_id = track_id
        self.__name = name
        self.__artists = artists
        self.__album = album

    """
    Sobrescrita do str
    """

    def __str__(self) -> str:
        return str(self.__dict__)
