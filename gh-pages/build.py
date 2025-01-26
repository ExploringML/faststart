# gh-pages/build.py
import httpx
import time
from pathlib import Path
import subprocess
import signal
import sys
from shutil import copytree, rmtree

def wait_for_server(url, timeout=5):
    start = time.time()
    while time.time() - start < timeout:
        try:
            httpx.get(url)
            return True
        except:
            time.sleep(0.1)
    return False

# Get directories
gh_pages_dir = Path(__file__).parent
src_dir = gh_pages_dir / 'src'
docs_dir = gh_pages_dir.parent / 'docs' # Changed to root docs folder

# Clean and recreate docs directory with same structure
if docs_dir.exists():
    rmtree(docs_dir)
docs_dir.mkdir(exist_ok=True)
(docs_dir / 'public').mkdir(exist_ok=True)

# Start the FastHTML server from src directory
server = subprocess.Popen(
    [sys.executable, "main.py"],
    cwd=str(src_dir)
)

try:
    # Wait for server to start
    if not wait_for_server("http://localhost:5001"):
        print("Server failed to start")
        sys.exit(1)

    # Fetch the page
    response = httpx.get("http://localhost:5001")
    
    # Save the HTML
    (docs_dir / 'index.html').write_text(response.text)
    
    # Copy static assets maintaining structure
    if (src_dir / 'public').exists():
        for item in (src_dir / 'public').glob('*'):
            if item.is_file():
                dest = docs_dir / 'public' / item.name
                dest.write_bytes(item.read_bytes())
            else:
                copytree(item, docs_dir / 'public' / item.name)

finally:
    server.send_signal(signal.SIGTERM)
    server.wait()
