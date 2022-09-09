class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath.split(".")[-1]
    def filename(self):
        return self.filepath.split("/")[-1].split(".")[0]
    def dirpath(self):
        return "/".join(self.filepath.split(".")[0].split("/")[0:-1:1]) + "/"

# Link: https://www.codewars.com/kata/5844e0890d3bedc5c5000e54

