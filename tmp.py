from gen_vlc_playlist import Playlist, Videos
import os

if __name__ = "__main__":
    videos: Videos = Videos()
    playlistFolder: str = ""
    playlistFolderList: dict[str, list[str]] = {
        "test" : ["test/"]
    }
    for name, folderList in playlistFolder.items():
        playlist: Playlist = Playlist()
        files: list[str] = []
        for folderpath in folderList:
            os.chdir(folderpath)
            files += videos.get_videos_with_subdir()
