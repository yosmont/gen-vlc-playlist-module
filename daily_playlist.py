from gen_vlc_playlist import Videos, Playlist
import os, random, shutil
import xml.etree.ElementTree as xml
from zipfile import ZipFile

class DailyPlaylistConfig:
    def __init__(self) -> None:
        self.playlistDuration: int = 24 # the playlist length in hour 
        self.trackDuration: int = 5 # a prediction of the mean duration of a track
        self.trackListSize: int = (self.playlistDuration * 60) / self.trackDuration # how many track put in the playlist 
        self.srcDir: str = "" # path to the folder for get_videos (absolute path ending with '/')
        self.destDir: str = "" # path to the work folder & final result folder (both use the same folder) (absolute path ending with '/')
        self.trackDirName: str = "tracks" # folder name for where to put the track list files
        self.trackDir: str = self.destDir + self.trackDirName + '/' # absolute path ending with '/' to the trackDir
        self.playlistName: str = "daily.xspf" # playlist file name
        self.zipName: str = "daily.zip" # zip file name

if __name__ == "__main__":
    conf: DailyPlaylistConfig = DailyPlaylistConfig()
    shutil.rmtree(conf.destDir)
    os.mkdir(conf.destDir)
    vid: Videos = Videos()
    os.chdir(conf.srcDir)
    srcFiles: list[str] = random.shuffle(vid.get_videos_with_subdir())[:conf.trackListSize]
    os.mkdir(conf.trackDir)
    for f in srcFiles:
        shutil.copy(f, conf.trackDir)
    os.chdir(conf.trackDir)
    dailyFiles: list[str] = vid.edit_paths(vid.abspath_to_relpath(vid.get_videos(), conf.destDir))
    dailylist: Playlist = Playlist()
    for f in vid.edit_paths(vid.abspath_to_relpath(dailyFiles, conf.destDir)):
        dailylist.add_track(f)
    with open(conf.destDir + self.playlistName, 'w') as mf:
        mf.write(xml.to_string(dailylist.get_playlist()).decode('utf-8'))
    # shutil.make_archive(conf.destDir)
    with ZipFile(conf.destDir + conf.zipName, 'w') as zip:
        for f in dailyFiles:
            zip.write(f, conf.trackDirName + '/' + os.path.basename(f))
            os.remove(f)
        zip.write(conf.destDir + conf.playlistName, conf.playlistName)
        os.remove(conf.destDir + conf.playlistName)
