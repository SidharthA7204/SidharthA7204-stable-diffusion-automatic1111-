import threading
import time
import subprocess
import requests
import os
import signal
import psutil
from pyngrok import ngrok

PORT = 7860
TIMEOUT_SECONDS = 1800

def cleanup():
    try:
        ngrok.kill()
        os.system("pkill ngrok")
    except Exception:
        pass

    for proc in psutil.process_iter(['pid']):
        try:
            for con in proc.connections(kind='inet'):
                if con.laddr.port == PORT:
                    os.kill(proc.pid, signal.SIGKILL)
        except Exception:
            pass

def run_webui():
    cmd = [
        "python", "launch.py",
        "--listen",
        "--port", str(PORT),
        "--enable-insecure-extension-access",
        "--no-download-sd-model",
        "--opt-sdp-attention",
        "--skip-torch-cuda-test"
    ]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def wait_for_server():
    start = time.time()
    while time.time() - start < TIMEOUT_SECONDS:
        try:
            requests.get(f"http://127.0.0.1:{PORT}")
            return True
        except:
            time.sleep(2)
    raise TimeoutError("WebUI startup timed out")

cleanup()
threading.Thread(target=run_webui, daemon=True).start()
wait_for_server()

public_url = ngrok.connect(addr=f"127.0.0.1:{PORT}")
print(f"WebUI Live at: {public_url.public_url}")
