# MultiThreadDownloader

MultiThreadDownloader is a Python script that allows you to download files in segments using multithreading. 
This approach speeds up the download process by leveraging multiple threads to download different parts of a file simultaneously.

## Features

- Download files in parallel using multiple threads.
- Automatically reassemble downloaded file segments.
- Supports custom configuration of the number of threads.

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:amine-el-amrani/MultiThreadDownloader.git
cd MultiThreadDownloader
```

### 2. Create a Virtual Environment

```bash
Python3 -m venv venv
```

### 3. Create a Virtual Environment

```bash
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

```bash
from src.downloader import MultiThreadDownloader

url = 'http://example.com/largefile.zip'
output_file = 'largefile.zip'

downloader = MultiThreadDownloader(url, output_file, num_threads=4)
downloader.download()
```

## Testing

### 1. Prepare the Environment

Ensure that the virtual environment is activated and dependencies are installed.

### 2. Run the Test Script

Execute the test script to verify functionality:

```bash
python tests/test_downloader.py
```

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.