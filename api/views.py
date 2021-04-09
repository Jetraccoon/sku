import json

import aiohttp

from api.services import bin_search


async def csv(request):
    sku = request.rel_url.query.get('sku')
    if not sku:
        return aiohttp.web.Response(text='sku required parameter', status=500)
    min_rank = request.rel_url.query.get('min_rank')
    from api.app import sku_list
    location = bin_search(sku_list, sku)
    result = sku_list[location[0]:location[1] + 1]
    if min_rank:
        # for i in range(0, len(result)):
        #     line = result[i].split(',')
        #     if float(line[2]) < float(min_rank):
        #         result.pop(i)
        result = [r for r in result if float(r.split(',')[2]) > float(min_rank)]

    return aiohttp.web.Response(text=json.dumps(result), status=200)
