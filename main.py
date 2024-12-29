from src.processing import filter_by_state, sort_by_date,dictionary_list

if __name__ == "__main__":
    print (sort_by_date(dictionary_list))
    print (filter_by_state(dictionary_list))
