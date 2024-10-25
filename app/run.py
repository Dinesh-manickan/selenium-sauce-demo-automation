from main import main
from update import update_price
from fetch_data import fetch_data
# from logger import Logger


def run_all():
    print("Starting main.py...")
    main()

    print("Starting update.py...")
    update_price()

    print("Starting fetch_data.py...")
    fetch_data()

    # print("Starting Logger.py...")
    # Logger()


print("All scripts have been run successfully!")
if __name__ == "__main__":
    run_all()
