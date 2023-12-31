import datetime
import time

from selenium.common.exceptions import TimeoutException

from aviso import Aviso
from res.string import strings
from settings import Settings


def main():
    _settings = Settings()
    settings = _settings.get_settings()
    lan = settings['language']
    wmr_fast = Aviso(_settings)
    driver = wmr_fast.log_in()
    print(f'{datetime.datetime.now()} sleep {5} seconds')
    time.sleep(5)
    is_video_tasks_available = True
    is_website_tasks_available = False
    while True:
        try:
            if is_video_tasks_available or is_website_tasks_available:
                if is_video_tasks_available:
                    is_video_tasks_available = wmr_fast.watch_videos(driver)['is_tasks_available']
                if is_website_tasks_available:
                    is_website_tasks_available = wmr_fast.view_websites(driver)['is_tasks_available']
            else:
                print(f"{datetime.datetime.now()} {strings['nothing_watch_or_view'][lan]}")
                is_video_tasks_available = True
                is_website_tasks_available = True
                time.sleep(3600)
        except KeyboardInterrupt:
            if input('PRESS ENTER TO CONTINUE OR ENTER STOP TO CLOSE').lower() == 'stop':
                quit()
            else:
                continue
        except TimeoutException:
            print(f"{datetime.datetime.now()} Error with network. Sleep 1 minute")
            time.sleep(60)
            continue
        except Exception as e:
            print(e)
            time.sleep(15)
            continue


if __name__ == "__main__":
    main()
