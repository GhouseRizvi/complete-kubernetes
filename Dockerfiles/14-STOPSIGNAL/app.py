import signal
import time

def handle_signal(signum, frame):
    print(f"Received signal: {signum}, shutting down gracefully...")
    exit(0)

# Register signal handlers
signal.signal(signal.SIGINT, handle_signal)  # Handling SIGINT
signal.signal(signal.SIGTERM, handle_signal)  # Handling SIGTERM

print("Application is running... Press Ctrl+C to stop.")

# Simulate a long-running process
while True:
    time.sleep(1)
