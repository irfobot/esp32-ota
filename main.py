from version import VERSION
import time

print("=" * 40)
print(f"  Aplikasi ESP32")
print(f"  Versi : {VERSION}")
print("=" * 40)

counter = 0
while True:
    counter += 1
    print(f"Loop ke-{counter} | Versi {VERSION}")
    time.sleep(3)
