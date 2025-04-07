from temp_test_base.use_cases.tools.date_converter import convert_to_date
from legitindicators import vwap
import csv

def find_vwap_pos(repo, symbol, interval, start_date, end_date):
    start_date_obj = convert_to_date(start_date)
    end_date_obj = convert_to_date(end_date)
    data = repo.get_all_data(symbol, interval, start_date_obj, end_date_obj)
    if data is None:
        return
    
    high = data["high"].tolist()
    low = data["low"].tolist()
    close = data["close"].tolist()
    volume = data["volume"].tolist()

    input_data = []
    for i in range(0, len(data)):
        hlcv = [high[i], low[i], close[i], volume[i]]
        input_data.append(hlcv)

    vwap_result, std_05, std_10, std_15, std_20, std_25 = vwap(input_data)
    if close[-1] < std_05[0][-1] and close[-1] > std_05[1][-1]:
        print(symbol, std_05[1][-1], close[-1], std_05[0][-1])
        with open('temp_test_base/results/vwap_result.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(symbol)