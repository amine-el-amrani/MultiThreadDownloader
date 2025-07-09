import os
import requests
from concurrent.futures import ThreadPoolExecutor
from security import safe_requests

class MultiThreadDownloader:
    def __init__(self, url, output_file, num_threads=4):
        self.url = url
        self.output_file = output_file
        self.num_threads = num_threads
        self.output_dir = './temp_segments'

    def download_segment(self, start, end, segment_number):
        headers = {'Range': f'bytes={start}-{end}'}
        response = safe_requests.get(self.url, headers=headers, stream=True, timeout=60)
        segment_path = os.path.join(self.output_dir, f'segment_{segment_number}')
        
        with open(segment_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        
        return segment_path

    def reassemble_file(self, segments):
        with open(self.output_file, 'wb') as final_file:
            for segment in segments:
                with open(segment, 'rb') as file:
                    final_file.write(file.read())
                os.remove(segment)

    def download(self):
        os.makedirs(self.output_dir, exist_ok=True)
        response = requests.head(self.url, timeout=60)
        file_size = int(response.headers.get('Content-Length', 0))
        segment_size = file_size // self.num_threads
        
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            for i in range(self.num_threads):
                start = i * segment_size
                end = start + segment_size - 1 if i < self.num_threads - 1 else file_size
                futures.append(executor.submit(self.download_segment, start, end, i))
            
            segments = [future.result() for future in futures]
        
        self.reassemble_file(segments)
