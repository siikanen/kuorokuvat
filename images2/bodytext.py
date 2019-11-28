import os

outfile="bodytext"
filenames=os.listdir(".")

fileoperations=input("Do you want to enable fileoperations? [y/N]")

def fixFilename(filenames):
    for name in filenames:
        if " " in name[0:4]:
            print(name)
            os.rename(name, "0" + name)

filenames.clear()
filenames=os.listdir(".")
filenames.sort()

with open(outfile, 'w') as f:
    for name in filenames:
        if ".py" in name or name == outfile:
            continue
        originalname=name
        name = name.split(" ", 1)
        text = name[1][:-4]
        newname = name[0] + "." + name[1].split(".", 1)[1]

        if fileoperations == "y" or fileoperations == "Y":
            os.rename(originalname, newname)
            print(f"Renaming {originalname} to {newname}")

        f.write('<section data-transition="fade" data-background-color="fff" data-background-image="images2/' + newname + ' data-background-opacity="1" data-background-size="contain" >\n')
        f.write('<aside class="notes">' + text + ' </aside>\n')
        f.write("</section>\n\n")


        print("Desc text would be", text, "\nFilename would be",  newname)
        print()
