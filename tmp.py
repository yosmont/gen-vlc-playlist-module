from gen_vlc_playlist import Playlist, Videos

if __name__ = "__main__":
    playlist: Playlist = Playlist()
    videos: Videos = Videos()
    playlistFolder: str = ""
    playlistFolderList: dict[str, list[str]] = {
        "test" : ["test/"]
    }
