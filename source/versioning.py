# IMPORT MODULES
import random
import math
import sys

# DEFINE LANGUAGE
match sys.argv[1]:
    case "Español":
        question_version = "Introduce la versión actual:                      "
        question_major = "Cambios major:                                    "
        question_minor = "Cambios minor:                                    "
        question_patch = "Cambios patch:                                    "
        line_new = "Nueva versión:                                    "
        line_format = "Usa el formato A.B.C o A.B.C.D"
    case "English" | _:
        question_version = "Enter current version:                            "
        question_major = "Major changes:                                    "
        question_minor = "Minor changes:                                    "
        question_patch = "Patch changes:                                    "
        line_new = "New version:                                      "
        line_format = "Use format A.B.C or A.B.C.D"

# FUNCTIONS
def incrandom(power):
    return round(math.pow(1/random.random(), power))
def major(M, m, p, bound1=0.2):
    chance = random.random()
    if chance >= 1 - bound1:
        return M+1, 0, 0
    else:
        return M, m+1, 0
def minor(M, m, p, bound1=0.03, bound2=0.1, bound3=0.5):
    chance = random.random()
    if chance >= 1 - bound1:
        return M+1, 0, 0
    elif chance >= 1 - bound1 - bound2:
        return M, m+1, 0
    elif chance >= 1 - bound1- bound2 - bound3:
        return M, m, p+incrandom(1.25)
    else:
        return M, m, p+1
def patch3(M, m, p, bound1=0.03, bound2=0.3):
    chance = random.random()
    if chance >= 1 - bound1:
        return M, m+1, 0
    elif chance >= 1 - bound1 - bound2:
        return M, m, p+incrandom(0.75)
    else:
        return M, m, p+1
def patch4(M, m, p, b, bound1=0.02, bound2=0.25, bound3=0.4):
    chance = random.random()
    if chance >= 1 - bound1:
        return M, m+1, 0, 0
    elif chance >= 1 - bound1 - bound2:
        return M, m, p+incrandom(0.5), 0
    elif chance >= 1 - bound1 - bound2 - bound3:
        return M, m, p, b+incrandom(1)
    else:
        return M, m, p, b+incrandom(0.5)

# MAIN PROCESS
def main():
    current = input(question_version).split(".")
    if len(current) == 3:
        vM, vm, vp = int(current[0]), int(current[1]), int(current[2])
        major_changes = int(input(question_major))
        minor_changes = int(input(question_minor))
        patch_changes = int(input(question_patch))
        static_total = major_changes + minor_changes + patch_changes
        for iteration in range(static_total):
            total = major_changes + minor_changes + patch_changes
            select = random.randint(1, total)
            if select <= major_changes:
                vM, vm, vp = major(vM, vm, vp)
                major_changes -= 1
            elif select <= minor_changes + major_changes:
                vM, vm, vp = minor(vM, vm, vp)
                minor_changes -= 1
            else:
                vM, vm, vp = patch3(vM, vm, vp)
                patch_changes -= 1
        print(f"{line_new}{vM}.{vm}.{vp}")
        return True
    elif len(current) == 4:
        vM, vm, vp, vb = int(current[0]), int(current[1]), int(current[2]), int(current[3])
        major_changes = int(input(question_major))
        minor_changes = int(input(question_minor))
        patch_changes = int(input(question_patch))
        static_total = major_changes + minor_changes + patch_changes
        for iteration in range(static_total):
            total = major_changes + minor_changes + patch_changes
            select = random.randint(1, total)
            if select <= major_changes:
                vM, vm, vp = major(vM, vm, vp)
                major_changes -= 1
            elif select <= major_changes + minor_changes:
                vM, vm, vp = minor(vM, vm, vp)
                minor_changes -= 1
            else:
                vM, vm, vp, vb = patch4(vM, vm, vp, vb)
                patch_changes -= 1
        print(f"{line_new}{vM}.{vm}.{vp}.{vb}")
        return True
    else:
        return False

# ENTRY POINT WITH LOOP
if __name__ == "__main__":
    done = False
    while not done:
        done = main()
        if not done:
            print(line_format)