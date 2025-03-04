import gdown
import tarfile
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Download and extract a tar file from Google Drive.")
parser.add_argument("--url", required=True, help="Google Drive URL to download the file")
args = parser.parse_args()

url = args.url
destination = "."

output = f'{destination}/download.tgz'
gdown.download(url, output, quiet=False)

# Open and extract
# with tarfile.open(output, "r:gz") as tar:
#     tar.extractall(destination)

if os.path.exists(output):
    os.remove(output)