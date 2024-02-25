import csv
import requests
import matplotlib.pyplot as plt
import random
from bs4 import BeautifulSoup


def generate_housing_prices(num_records):
    dataset = []
    for _ in range(num_records):
        price = random.randint(500000, 5000000)  # Random price between 500,000 NPR and 5,000,000 NPR
        dataset.append([price])
    return dataset

def save_data_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Price (NPR)'])
        writer.writerows(data)


def read_data_from_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            data.append([int(value) for value in row])
    return data

def plot_data(datasets):
    for idx, data in enumerate(datasets):
        plt.plot(data, marker='o', linestyle='-', label=f'Dataset {idx+1}')
    plt.title('Scraped Data Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')
   # plt.legend()
   # plt.grid(True)
    plt.show()

def main():
    num_records = 50  # Adjust the number of records as needed
    
    housing_prices = generate_housing_prices(num_records)
    # Save scraped datasets to CSV files
    for idx, dataset in enumerate(housing_prices):
        save_data_to_csv(housing_prices, f'scraped_data_{idx+1}.csv')

    # Read datasets from the CSV files
    datasets_from_csv = []
    for idx in range(len(housing_prices)):
        dataset = read_data_from_csv(f'scraped_data_{idx+1}.csv')
        datasets_from_csv.append(dataset)

    # Plot the datasets
    plot_data(datasets_from_csv)

if __name__ == "__main__":
    main()
