import sys
from temp_test_base.repository.tw.twrepo_all_stock import TWRepoAllStock
from temp_test_base.use_cases.list_pairs import list_pairs
from temp_test_base.use_cases.find_vwap_pos import find_vwap_pos

def find_vwap():
    repo = TWRepoAllStock()
    pairs = list_pairs(repo)
    for pair in pairs: 
        symbol = find_vwap_pos(repo, pair, "1d", "20200323000000", "20250406000000")


if __name__ == "__main__":
    if sys.argv[1] == "vwap":
        find_vwap()