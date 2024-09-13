import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from downloader import MultiThreadDownloader

def test_downloader():
    url = 'https://testfile.org/1.3GBiconpng'  # Example file for testing (1.3 GB)
    output_file = 'downloaded_test_file.bin'

    downloader = MultiThreadDownloader(url, output_file, num_threads=4)
    downloader.download()

    if os.path.exists(output_file):
        print("Test passed: File downloaded successfully.")
    else:
        print("Test failed: File not found.")

if __name__ == '__main__':
    test_downloader()