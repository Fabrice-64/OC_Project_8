from methods import ProcessStore, ProcessCategory, ProcesProduct


def main():
    stores = ProcessStore()
    stores.store_full_process()

    categories = ProcessCategory()
    categories.category.full_process()
    

if __name__ == "__main__":
    main()