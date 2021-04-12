def parse_csv():
    with open('./recommends.csv') as f:
        data = f.read()
        data = data.split('\n')
        data.sort()
        return data


def bin_search(sku_list, sku):
    bottom = 0
    top = len(sku_list) - 1
    found = False
    location_first = 0
    location_last = 0
    while (bottom <= top) and not (found):
        middle = int((bottom + top) // 2)
        if (sku_list[middle][:10] == sku):
            found = True
            for I in range(middle, len(sku_list)):
                if not sku_list[I][:10] == sku:
                    location_last = I - 1
                    break
            for I in range(middle, 0, -1):
                if not sku_list[I][:10] == sku:
                    location_first = I + 1
                    break
        else:
            if sku < sku_list[middle][:10]:
                top = middle - 1
            else:
                bottom = middle + 1
    return sku_list[location_first:location_last + 1]
