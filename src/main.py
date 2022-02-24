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

from Contributor import Contributor
from Project import Project


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
    allContributors = []
    allProjects = []

    input_file = open(file_location, "r")
    numContributors = 0
    seenContributors = 0
    numProjects = 0
    currentContributor = None
    currentProject = None
    currentContSkills = 0
    currentProjectSkills = 0
    count = 0
    for line in input_file:
        # Do Something
        count+=1
        if count == 1:
            splitLine = line.split(" ")
            numContributors = int(splitLine[0])
            numProjects = int(splitLine[1])
        elif seenContributors < numContributors:
            if currentContSkills == 0:
                splitLine = line.split(" ")
                currentContributor = Contributor(splitLine[0], int(splitLine[1]))
                currentContSkills = int(splitLine[1])
                currentContSeenSkills = 0
            else:
                splitLine = line.split(" ")
                currentContributor.add_skill(splitLine[0], int(splitLine[1]))
                currentContSeenSkills += 1
                if currentContSeenSkills == currentContSkills:
                    # Seen all skills
                    allContributors.append(currentContributor)
                    currentContSkills = 0
                    seenContributors += 1
        else:
            if currentProjectSkills == 0:
                splitLine = line.split(" ")
                currentProject = Project(splitLine[0], int(splitLine[1]), int(splitLine[2]), int(splitLine[3]), int(splitLine[4]))
                currentProjectSkills = int(splitLine[4])
                currentProjectSeenSkills = 0
            else:
                splitLine = line.split(" ")
                currentProject.add_role(splitLine[0], int(splitLine[1]))
                currentProjectSeenSkills += 1
                if currentProjectSeenSkills == currentProjectSkills:
                    # Seen all project
                    allProjects.append(currentProject)
                    currentProjectSkills = 0
    input_file.close()


    ### DO THE WORK
    for aProject in allProjects:
        for aRole in aProject.get_roles():
            required_skill = aProject.get_skill_for_role(aRole)
            for aContributor in allContributors:
                if aContributor.get_skill_level(aRole) >= required_skill and not aProject.is_contributor_assigned(aContributor.get_name()):
                    aProject.add_contributor(aContributor.get_name(), aRole)
                    break

    completedProjectCount = 0
    ### PRINT
    output_file = open(output_location, "w")
    # Write to file here
    for aProject in allProjects:
        if aProject.is_completed():
            completedProjectCount += 1
    output_file.write(f"{completedProjectCount}\n")
    for aProject in allProjects:
        if aProject.is_completed():
            output_file.write(f"{aProject.get_name()}\n")
            output_file.write(f"{aProject.get_ordered_roles()}\n")
    output_file.close()


# When run from the terminal
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
