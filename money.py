# money money money!
# in MSFT stock prices (daily closing)
# find high (and date), low (and date),
# average price, and day with biggest
# one-day *drop*. Restrict to 2022 ONLY.

def get_prices():
    '''Reads file, returns dates and prices
    in two separate lists'''
    l_dates = []
    l_prices = []

    f = open("MSFT.csv", mode="r")
    print(f)
    f.readline() # skip header line
    for s_line in f:
        l_data = s_line.split(",")
        s_date = l_data[0]
        i_year = int(s_date[:4]) # extracts the year
        f_price = float(l_data[4])
        if i_year == 2022: # filter with selection pattern
            # print(s_date, f_price)
            l_dates.append(s_date)
            l_prices.append(f_price)

    f.close()
    return l_dates, l_prices

def biggest_drop(l_prices):
    i_min = 1
    f_min = l_prices[1] - l_prices[0]
    for i_index in range(1, len(l_prices)):
        diff = l_prices[i_index] - l_prices[i_index - 1]
        if diff < f_min:
            i_min = i_index
            f_min = diff
    return i_min, f_min

def main():
    l_dates, l_prices = get_prices()
    f_max = round(max(l_prices), 2)
    f_min = round(min(l_prices), 2)
    f_avg = round(sum(l_prices) / len(l_prices), 2)
    print(f_max, f_min, f_avg)
    i_min, f_min = biggest_drop(l_prices)
    print(l_dates[i_min], l_prices[i_min], f_min)

if __name__ == '__main__':
    main()

