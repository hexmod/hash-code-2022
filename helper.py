import datetime
import importlib
import os
import pkgutil
import sys
import time
import zipfile

# Add the src folder to the path to allow the submission to import
# files in the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
# Import the entry point for our submission
import main as hashCodeImp


DATA_LOCATION = ".\\data"
OUTPUT_LOCATION = ".\\output"


def run():
    now = datetime.datetime.now()
    print("Hash Code Runner - Welcome to Hash Code", now.year)
    repl()


def repl():
    while True:
        print("Please choose an option:")
        data_files = get_data_files()
        (action, param) = get_action(data_files)
        refresh_source()

        if action == "singleFile":
            run_for_file(get_file_path(param), OUTPUT_LOCATION)
        elif action == "allFiles":
            for a_file in data_files:
                run_for_file(get_file_path(a_file), OUTPUT_LOCATION)
        elif action == "zip":
            zip_project(OUTPUT_LOCATION)
        elif action == "allFilesAndZip":
            for a_file in data_files:
                run_for_file(get_file_path(a_file), OUTPUT_LOCATION)
            zip_project(OUTPUT_LOCATION)


def get_file_path(a_file):
    return os.path.join(DATA_LOCATION, a_file)


def refresh_source():
    # Reload our source in case we have made any changes
    importlib.reload(hashCodeImp)
    for _, name, _ in pkgutil.iter_modules(['src']):
        if name in sys.modules:
            importlib.reload(sys.modules[name])


def get_data_files():
    data_files = []
    for file_name in os.listdir(DATA_LOCATION):
        if file_name != "readme.txt" and os.path.isfile(os.path.join(DATA_LOCATION, file_name)):
            data_files.append(file_name)
    return data_files


def get_action(data_files):
    options = [("doNothing", None)]
    count = 1
    for a_file in data_files:
        print("[" + str(count) + "]", a_file)
        options.append(("singleFile", a_file))
        count += 1

    print("[" + str(count) + "]", "Run for all Files")
    options.append(("allFiles", None))
    count += 1

    print("[" + str(count) + "]", "Zip source")
    options.append(("zip", None))
    count += 1

    print("[" + str(count) + "]", "Run for all files and zip source")
    options.append(("allFilesAndZip", None))

    user_choice = input()
    return options[convert_input_to_option(user_choice, len(options))]


def convert_input_to_option(input, upper_bound):
    try:
        option_num = int(input)
        if option_num > 0 and option_num < upper_bound:
            return option_num
        else:
            return 0
    except ValueError:
        return 0  # Do Nothing


def run_for_file(file_location, output_location):
    print("Running hash code entry against", file_location)
    print("-----------------")
    print()
    start = time.time_ns()

    hashCodeImp.run(file_location, output_location)

    print()
    print("-----------------")
    end = time.time_ns()
    print("Ran in:", (end - start) / 1000000000, "seconds")
    print()


def zip_project(output_location):
    print("Zipping project and saving to", output_location)
    now = datetime.datetime.now()

    zip_name = OUTPUT_LOCATION + "\\hashCode" + str(now.year) + ".zip"
    zipf = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    # Add our Pipfile, so any deps can be downloaded
    zipf.write(".\\Pipfile")
    zipf.write(".\\Pipfile.lock")
    for root, dirs, files in os.walk(".\\src"):
        for file in files:
            filename = os.path.join(root, file)
            # Ignore the top level init file, as this is only needed by the code runner
            if filename != ".\\src\\__init__.py":
                zipf.write(filename, filename.replace(".\\src\\", ".\\"))
    zipf.close()
    print()


# When run from the terminal
if __name__ == '__main__':
    run()
