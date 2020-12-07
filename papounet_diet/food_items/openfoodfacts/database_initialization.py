from methods import ProcessStore


def main():
    stores = ProcessStore()
    res = stores.download_stores()
    print(res)

if __name__ == "__main__":
    main()