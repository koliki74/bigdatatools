"""
HASVITHA KOLIKINENI
ASSIGNMENT 3 SUBMISSION
BIG DATA TOOLS AND TECHNIQUES
"""

import matplotlib.pyplot as plt

# This class creates plots and shows them to the user.
# This class can also save the images as png files to the users computer but it will do that only if the user wants to.


class DataProcessor:
    def __init__(self, neo_data):
        self.neo_data = neo_data
        self.dates = list(self.neo_data["near_earth_objects"].keys())
        self.counts = [
            len(self.neo_data["near_earth_objects"][date]) for date in self.dates
        ]

    def generate_line_chart(self, save):
        # Generates a line chart
        plt.figure(figsize=(10, 6))
        plt.plot(self.dates, self.counts, marker="o", linestyle="-", color="b")
        plt.title("NEO Counts Over the Current Week")
        plt.xlabel("Date")
        plt.ylabel("Number of NEOs Detected")
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save:
            plt.savefig("line_chart.png")
        plt.show()
        plt.close()  # Ensure plt.close() is called to free up memory

    def generate_bar_chart(self, save):
        # Generates a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(self.dates, self.counts, color="skyblue")
        plt.title("NEO Counts Over the Current Week")
        plt.xlabel("Date")
        plt.ylabel("Number of NEOs Detected")
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save:
            plt.savefig("bar_chart.png")
        plt.show()
        plt.close()

    def generate_pie_chart(self, save):
        # Generates a pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(self.counts, labels=self.dates, autopct="%1.1f%%", startangle=140)
        plt.title("Distribution of NEO Detections Over the Current Week")
        if save:
            plt.savefig("pie_chart.png")
        plt.show()
        plt.close()
