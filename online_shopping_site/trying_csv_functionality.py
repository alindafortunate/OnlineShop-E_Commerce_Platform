# Working with csv functionality.
import csv

with open(r"marks.csv", "w") as new_file:
    writer = csv.writer(new_file)
    writer.writerow(["Maths", "English", "SST"])
    writer.writerow(["90", 95, 98])
