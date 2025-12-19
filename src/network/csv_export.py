import io
import csv

def create_csv(data: dict) -> io.StringIO:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Field", "Value"])
    for key, value in data.items():
        writer.writerow([key, value])
    output.seek(0)
    return output
