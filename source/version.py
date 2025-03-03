# LITERAL SOURCE = CHATGPT

import math
import random
import sys

def non_linear_increment(changes):
    """
    Compute a non-linear increment for patch updates.
    Uses a square-root function (with ceiling) so that even many changes 
    result in a moderated increment.
    """
    if changes <= 0:
        return 0
    return int(math.ceil(math.sqrt(changes)))

def ascend_probability(changes, k=0.2):
    """
    Calculate the probability of ascending to a higher version component.
    The probability increases with the number of changes using an exponential decay model.
    
    Args:
        changes (int): Number of changes in the given category.
        k (float): Tuning parameter for sensitivity.
        
    Returns:
        float: A probability between 0 and 1.
    """
    # The probability is 1 - exp(-k * changes)
    return 1 - math.exp(-k * changes)

def next_version(current_version, minor_changes, major_changes, big_changes, k_major=0.2, k_minor=0.2):
    """
    Compute the next version based on the current version and the counts of changes.
    
    The decision hierarchy is:
        1. If there are big changes and a random draw is less than the major ascend probability,
            bump the major version by 1 and reset minor and patch to 0.
        2. Else, if there are major changes and a random draw is less than the minor ascend probability,
            bump the minor version by 1 and reset the patch to 0.
        3. Otherwise, bump the patch version by a non-linear increment based on the number of minor changes.
    
    Args:
        current_version (str): The current version in "X.Y.Z" format.
        minor_changes (int): Count of changes affecting only the patch.
        major_changes (int): Count of changes affecting the minor version.
        big_changes   (int): Count of changes affecting the major version.
        k_major (float): Tuning parameter for the probability of ascending major.
        k_minor (float): Tuning parameter for the probability of ascending minor.
    
    Returns:
        str: The next version as a string in "X.Y.Z" format.
    """
    try:
        major, minor, patch = map(int, current_version.split('.'))
    except ValueError:
        raise ValueError("Invalid version format. Use X.Y.Z where X, Y, Z are integers.")
    
    # Calculate the probability to ascend to a higher version part.
    prob_major = ascend_probability(big_changes, k_major)
    prob_minor = ascend_probability(major_changes, k_minor)
    
    # Decide on version bumping:
    if big_changes > 0 and random.random() < prob_major:
        # Major ascend: bump major and reset minor and patch.
        major += 1
        minor = 0
        patch = 0
    elif major_changes > 0 and random.random() < prob_minor:
        # Minor ascend: bump minor and reset patch.
        minor += 1
        patch = 0
    else:
        # Default: update patch version with a non-linear increment.
        patch += non_linear_increment(minor_changes)
    
    return f"{major}.{minor}.{patch}"

def main():
    current_version = input("Current version: ")
    try:
        minor_changes = int(input("Patch changes: "))
        major_changes = int(input("Minor changes: "))
        big_changes   = int(input("Major changes: "))
    except ValueError:
        print("Change counts must be integers.")
        sys.exit(1)
    
    new_version = next_version(current_version, minor_changes, major_changes, big_changes)
    print("Next version:", new_version)

if __name__ == "__main__":
    main()
