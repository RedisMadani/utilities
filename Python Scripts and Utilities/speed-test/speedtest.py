import speedtest
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='internet_speed.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        # Get download and upload speed
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

        # Get ping
        ping = st.results.ping

        # Log the results
        logging.info(f"Download Speed: {download_speed:.2f} Mbps")
        logging.info(f"Upload Speed: {upload_speed:.2f} Mbps")
        logging.info(f"Ping: {ping} ms")

        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping} ms")

    except Exception as e:
        logging.error("Error occurred during the speed test", exc_info=True)
        print("Error occurred during the speed test")
        print(str(e))

if __name__ == "__main__":
    print(f"Starting speed test at {datetime.now()}")
    test_speed()
    print("Speed test completed")
