from app.utils import print_transactions

if __name__ == "__main__":
    data_to_print = print_transactions()
    for item in data_to_print:
        print(item)
