from src.processing import filter_by_state, sort_by_date,list_of_dictionaries

if __name__ == "__main__":
    print (sort_by_date(list_of_dictionaries))
    print (filter_by_state(list_of_dictionaries))
