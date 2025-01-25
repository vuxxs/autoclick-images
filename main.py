import os
import time
import pyautogui
from typing import List, Tuple
from dotenv import load_dotenv

load_dotenv()

CONFIDENCE = float(os.getenv("CONFIDENCE", 0.8))
LOOP_DELAY = int(os.getenv("LOOP_DELAY", 5))
MAX_INACTIVITY = int(os.getenv("MAX_INACTIVITY", 30))


def get_image_files(directory: str = "./images") -> Tuple[List, List]:
    """
    Scans the specified directory for PNG and JPG files.
    Returns a list of numbered and non-numbered filenames.
    """
    valid_extensions = (".png", ".jpg")
    files = [f for f in os.listdir(directory) if f.endswith(valid_extensions)]

    numbered_files = []
    other_files = []

    for file in files:
        name, _ = os.path.splitext(file)
        if name.isdigit():
            numbered_files.append(file)
        else:
            other_files.append(file)

    numbered_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

    return numbered_files, other_files


def find_and_click(
    image_path: str, directory: str = "./images", move_x: int = 100, move_y: int = 100
) -> bool:
    """
    Searches for an image in the specified directory. If found, clicks it, moves the mouse, and waits.
    If not found, it does nothing.
    """
    full_path = os.path.join(directory, image_path)
    try:
        location = pyautogui.locateCenterOnScreen(full_path, confidence=CONFIDENCE)
        if location:
            print(f"Found {image_path} at {location}. Clicking...")
            pyautogui.click(location)
            pyautogui.moveTo(location.x + move_x, location.y + move_y)
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print(f"Error finding or clicking {image_path}: {e}")
        return False


def main() -> None:
    print("Starting script. Press Ctrl+C to stop.")
    try:
        announce_io_activation = True
        while True:
            numbered_files, other_files = get_image_files()

            last_action_time = time.time()
            restart_required = False

            if numbered_files:
                if announce_io_activation:
                    print("In-order mode activated.")
                    announce_io_activation = False
                for file in numbered_files:
                    if find_and_click(file):
                        last_action_time = time.time()
                    if time.time() - last_action_time > MAX_INACTIVITY:
                        restart_required = True
                        break
            else:
                if not announce_io_activation:
                    announce_io_activation = True
                    print("In-order mode deactivated.")

                print("Clicking all available images.")

                for file in other_files:
                    if find_and_click(file):
                        last_action_time = time.time()
                    if time.time() - last_action_time > MAX_INACTIVITY:
                        restart_required = True
                        break

            if restart_required:
                print(f"No activity for {MAX_INACTIVITY} seconds, restarting loop...")
                time.sleep(LOOP_DELAY)

    except KeyboardInterrupt:
        print("Script stopped by user.")


if __name__ == "__main__":
    main()
