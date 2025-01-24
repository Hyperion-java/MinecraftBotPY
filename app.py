import os
from pytube import YouTube
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)

def progress_callback(stream, chunk, bytes_remaining):
    global pbar
    pbar.update(len(chunk))

def download_video():
    try:
        save_path = os.path.join(os.getcwd(), "videos")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        video_url = input(Fore.BLUE + "Enter the YouTube video URL: ")
        yt = YouTube(video_url, on_progress_callback=progress_callback)
        print(Fore.CYAN + f"Title: {yt.title}")
        print(Fore.CYAN + f"Views: {yt.views}")
        print(Fore.CYAN + f"Duration: {yt.length} seconds")
        stream = yt.streams.filter(res="720p", progressive=True).first()
        if not stream:
            print(Fore.RED + "720p video with audio is not available. Please try another video.")
            return
        filename = yt.title.replace("/", "-").replace("\\", "-")
        save_file = os.path.join(save_path, f"{filename}.mp4")
        global pbar
        file_size = stream.filesize
        pbar = tqdm(total=file_size, unit="B", unit_scale=True, desc="Downloading", colour="green")
        print(Fore.GREEN + "Downloading...")
        stream.download(output_path=save_path, filename=f"{filename}.mp4")
        pbar.close()
        print(Fore.GREEN + f"Download completed! Saved as: {save_file}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    download_video()
