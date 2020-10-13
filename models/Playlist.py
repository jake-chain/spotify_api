class Playlist(object):
    # Construtor da classe
    def __init__(self, playlists_id, name, tracks=None):
        if tracks is None:
            tracks = {}
        self.__playlists_id = playlists_id
        self.__name = name
        self.__tracks = tracks

    """
    Métodos de GET
    """

    def get_tracks(self):
        return self.__tracks

    """
    Métodos de SET
    """

    def set_tracks(self, tracks=None):
        if tracks is None:
            tracks = {}
        self.__tracks = tracks

    def add_track(self, track):
        self.__tracks[track.track_id] = track

    """
    Sobrescrita do str
    """

    def __str__(self) -> str:
        return str(self.__dict__)
