def filter_by_state(dict_list: list,state: str = "EXECUTED") -> list:
    tmp_list = [item for item in dict_list if item['state'] == state]
    return tmp_list

def sort_by_date(dict_list: list, descending: bool = True) -> list:
    pass

if __name__ == "__main__":
    pass