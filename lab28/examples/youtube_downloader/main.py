import os
import shutil
# import re
from pytube import Playlist, YouTube
import threading

class VideoDownloader:
	def __init__(self,url, download_dir) -> None:
		self.url = url
		self.video = YouTube(self.url)

		# if download_dir is None = > use CWD
		if download_dir==None:
			self.download_dir = os.getcwd()
		elif os.path.isdir(download_dir):
			self.download_dir = download_dir
		else:
			raise Exception(f'Error: {download_dir} does not exists!')



	def get_meta_data(self) -> dict():
		return {
			"author": self.video.author,
			"description":self.video.description,
			"keywords": self.video.keywords,
			"length": self.video.length,
			"publish_date":self.video.publish_date,
			"rating":self.video.rating,
			"title":self.video.title,
			"vid_info":self.video.vid_info,
			"views":self.video.views,
			"meta": self.video.metadata
		}

	def download(self, highest_res=False):
		print(f"Downloading: {self.video.title}...")

		if highest_res:
			stream = self.video.streams.get_highest_resolution()
		else:
			stream = self.video.streams.get_lowest_resolution()


		stream.download(self.download_dir)

		# print("Video Download complete!")


	def list_metadata(self):
		print(self.video.metadata.raw_metadata)
		print(self.video.metadata._metadata)


class PlaylistDownloader:
	def __init__(self, url, base_download_dir=None, n=None) -> None:
		self.url = url
		self.playlist = Playlist(self.url)

		# get all video URLs in the playlist
		self.video_urls = self.playlist.video_urls
		# get first n video URLs in the playlist
		if n:
			self.video_urls = self.video_urls[:n]


		# if base_download_dir is None = > use CWD
		if base_download_dir==None:
			self.base_download_dir = os.getcwd()
		elif os.path.isdir(base_download_dir):
			self.base_download_dir = base_download_dir
		else:
			raise Exception(f'Error: {base_download_dir} does not exists!')

		# create a directory to store the playlist videos
		self.playlist_download_dir = os.path.join(
			self.base_download_dir, self.playlist.title)

		try:
			os.mkdir(self.playlist_download_dir)
		except FileExistsError as fe:
			# empty playlist_download_dir
			shutil.rmtree(self.playlist_download_dir)
			os.mkdir(self.playlist_download_dir)


	def list_videos(self):
		for video in self.playlist.videos:
			print(video.title)

	def download(self, highest_res=False):
		# Download each video in the playlist
		for video_url in self.video_urls:
			# Create a YouTube object
			video = VideoDownloader(
				url=video_url,
				download_dir=self.playlist_download_dir)

			video.download(highest_res=highest_res)


	def parallel_download(self, highest_res=False):
		# Download each video in the playlist using separate threads
		threads = []
		for video_url in self.video_urls:
			video = VideoDownloader(
				url=video_url,
				download_dir=self.playlist_download_dir)

			thread = threading.Thread(
				target=video.download,
				kwargs={'highest_res':highest_res})
			thread.start()
			threads.append(thread)

		# Wait for all threads to finish
		for thread in threads:
			thread.join()

		print("Playlist download complete!")



pl1 = PlaylistDownloader(
	url='https://www.youtube.com/watch?v=x7T2XNeWTSI&list=PLHr3FWbW-hj6s13V_lFbwR6_V6PFDiBW4&ab_channel=TheAcademyofWisdom',
	base_download_dir='./downloads/', n=10)

# pl1.list_videos()

pl1.download()
# pl1.parallel_download()
