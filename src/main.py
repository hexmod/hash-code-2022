###############################
##
# HASH CODE ENTRY
##
# Usage: python main.py <path_to_source_file> <output_location>
##
###############################
import os
import sys
import pickle

# Import additional files by saving them in this folder and importing
# them relative to this file. e.g: from myFile import my_function


def do_with_cache(input_file_location, identifier, param):
    #
    # Sample method. This method will first check if the result
    # is cached and use that if avaliable. Else it will do the
    # work and then cache the results
    #
    input_file_name = os.path.basename(input_file_location).split(".")[0]
    cache_file = os.path.join(
        ".\\cache", input_file_name + "_" + identifier + ".pkl")

    if os.path.isfile(cache_file):
        print(f"Using Cache for {identifier}")
        with open(cache_file, "rb") as f:
            res = pickle.load(f)
    else:
        # Do the work here
        res = "Something..."
        with open(cache_file, "wb") as f:
            pickle.dump(res, f)

    return res


def run(file_location, output_location):
    print("Running Hash Code Entry")
    # Hash Code here :)

    # ----- SAMPLE: Read the input file -----
    # input_file = open(file_location, "r")
    # for line in input_file:
    #     # Do Something
    # input_file.close()
    # ---------------------------------------

    # ----- SAMPLE: Write out results -----
    # output_file = open(output_location, "w")
    # # Write to file here
    # output_file.write(f"{"Something"}\n")
    # output_file.close()
    # ------------------------------------


# When run from the terminal
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
