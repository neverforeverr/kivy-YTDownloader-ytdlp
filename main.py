from yt_dlp import YoutubeDL
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


urlVar = ""


class URLScreen(Screen):
    def contentURL(self):
        global urlVar

        self.__url = self.ids.url.text
        urlVar += self.__url


class MediaDownload(Screen):
    def audio_download(self):
        self.__audioOpt = {"format": "bestaudio", "outtmpl": "%(title)s.mp3"}
        with YoutubeDL(self.__audioOpt) as audio:
            audio.download(urlVar)

    def video_download(self):
        self.__videoOpt = {"format": "best[height=720]", "outtmpl": "%(title)s.mp4"}
        with YoutubeDL(self.__videoOpt) as video:
            video.download(urlVar)


class MainApp(App):
    def build(self):
        __sm = ScreenManager()
        __sm.add_widget(URLScreen(name="url"))
        __sm.add_widget(MediaDownload(name="media"))

        return __sm


if __name__ == "__main__":
    MainApp().run()
