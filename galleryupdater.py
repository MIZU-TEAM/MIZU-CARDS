import os
import codecs

galleryFile = codecs.open("gallery.md", "w", "utf-8")
mdFile = "# All Cards\n"
directory = os.listdir("./cards/")

images = []

for i in range(0, directory.__len__()):
    if directory[i].endswith(".png") or directory[i].endswith(".gif"):
        images.append(directory[i])


for i in range(0, images.__len__()):
    githubFileName = images[i].replace("+", "%2B")
    if i == 0 or i % 3 == 0:
        mdFile = mdFile + f'\n<img src="https://github.com/MIZU-TEAM/MIZU-CARDS/blob/main/custom-cards/{githubFileName}" width="300">'
    else:
        mdFile = mdFile + f'<img src="https://github.com/MIZU-TEAM/MIZU-CARDS/blob/main/custom-cards/{githubFileName}" width="300">'


galleryFile.write(mdFile)
