import os
import shutil

extenstionSet = {
    ".docx": "Documents",
    ".xslx": "Documents",
    ".pdf": "Documents",
    ".csv": "Documents",
    ".txt": "Documents",
    ".log": "Documents",
    ".md": "Documents",
    ".doc": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".mp3": "Musics",
    ".m4a": "Musics",
    ".ogg": "Musics",
    ".wav": "Musics",
    ".jpg": "Pictures",
    ".png": "Pictures",
    ".gif": "Pictures",
    ".tif": "Pictures",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".3gp": "Videos",
    ".mpeg4": "Videos",
    ".exe": "Programs",
    ".msi": "Programs",
    ".apk": "Programs",
    ".bat": "Programs",
    ".jar": "Programs",
    ".py": "Scripts",
    ".sh": "Scripts",
    ".c": "Codes",
    ".cpp": "Codes",
    ".java": "Codes",
    ".html": "Web",
    ".css": "Web",
    ".js": "Web",
    ".php": "Web",
    ".asp": "Web",
    ".aspx": "Web",
    ".jsp": "Web",
    ".xml": "Web",
    ".json": "Web",
}


def Organize(path, extSet):

    if os.path.exists(path):
        for file in os.listdir(path):

            filePath = os.path.join(path, file)

            if os.path.isdir(filePath):
                pass

            filename, fileExtension = os.path.splitext(filePath)

            if fileExtension in extSet:

                relocatingPath = os.path.join(path, extenstionSet[fileExtension])

                if not os.path.exists(relocatingPath):
                    os.makedirs(relocatingPath)

                try:
                    shutil.move(filePath, relocatingPath)
                except OSError as error:
                    CRED = "\033[91m"
                    CEND = "\033[0m"
                    print(CRED + f"Error, does not compute! {error}" + CEND)

        CRED = "\033[92m"
        CEND = "\033[0m"
        print(CRED + "Done!" + CEND)


Organize("C:\\Users\\" + os.environ.get("USERNAME") + "\\Downloads", extenstionSet)
