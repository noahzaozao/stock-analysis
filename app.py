from flask import Flask
from flask_pymongo import PyMongo
import json
import tushare as ts

import sys
sys.path.append('.')

from config import config


app = Flask(__name__)
app.config.from_object(config['dev'])
mongo = PyMongo(app)


@app.route('/api/fetch')
def api_fetch():
    # 获取沪深上市公司基本情况
    df = ts.get_stock_basics()
    mongo.db.stocks.insert(json.loads(df.T.to_json()).values())
    return 'Fetch complete'


@app.route('/api/list')
def api_list():
    """
    :return:
    code,代码
    name,名称
    industry,所属行业
    area,地区
    pe,市盈率
    outstanding,流通股本(亿)
    totals,总股本(亿)
    totalAssets,总资产(万)
    liquidAssets,流动资产
    fixedAssets,固定资产
    reserved,公积金
    reservedPerShare,每股公积金
    esp,每股收益
    bvps,每股净资
    pb,市净率
    timeToMarket,上市日期
    undp,未分利润
    perundp, 每股未分配
    rev,收入同比(%)
    profit,利润同比(%)
    gpr,毛利率(%)
    npr,净利润率(%)
    holders,股东人数
    """
    stocks = mongo.db.stocks.find()
    stocks_data = []
    for stock in stocks:
        print(stock)
        stocks_data.append({
            '_id': str(stock.pop('_id')),
            'name': stock.pop('name'),
            'industry': stock.pop('industry'),
            'area': stock.pop('area'),
            'pe': stock.pop('pe'),
            'outstanding': stock.pop('outstanding'),
            'totals': stock.pop('totals'),
            'totalAssets': stock.pop('totalAssets'),
            'liquidAssets': stock.pop('liquidAssets'),
            'fixedAssets': stock.pop('fixedAssets'),
            'reserved': stock.pop('reserved'),
            'reservedPerShare': stock.pop('reservedPerShare'),
            'esp': stock.pop('esp'),
            'bvps': stock.pop('bvps'),
            'pb': stock.pop('pb'),
            'timeToMarket': stock.pop('timeToMarket'),
            'undp': stock.pop('undp'),
            'perundp': stock.pop('perundp'),
            'rev': stock.pop('rev'),
            'profit': stock.pop('profit'),
            'gpr': stock.pop('gpr'),
            'npr': stock.pop('npr'),
            'holders': stock.pop('holders'),
        })
    return {
        'data': json.dumps(stocks_data)
    }


if __name__ == '__main__':
    app.run(debug=True, port=8000)
