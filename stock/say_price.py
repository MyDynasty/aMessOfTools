# coding: utf-8
'''

@author: rasca1
'''
import tushare as ts, subprocess, pyttsx3
from asyncio.tasks import sleep


class Stock_reporting:
    def to_chinese(self, number):
        """ convert integer to Chinese numeral """
        chinese_numeral_dict = {
            '0': '零',
            '1': '一',
            '2': '二',
            '3': '三',
            '4': '四',
            '5': '五',
            '6': '六',
            '7': '七',
            '8': '八',
            '9': '九'
        }
        chinese_unit_map = [('', '十', '百', '千'),
                            ('万', '十万', '百万', '千万'),
                            ('亿', '十亿', '百亿', '千亿'),
                            ('兆', '十兆', '百兆', '千兆'),
                            ('吉', '十吉', '百吉', '千吉')]
        chinese_unit_sep = ['万', '亿', '兆', '吉']
        reversed_n_string = reversed(str(number))
        result_lst = []
        unit = 0
        for integer in reversed_n_string:
            if integer is not '0':
                result_lst.append(chinese_unit_map[unit // 4][unit % 4])
                result_lst.append(chinese_numeral_dict[integer])
                unit += 1
            else:
                if result_lst and result_lst[-1] != '零':
                    result_lst.append('零')
                unit += 1

        result_lst.reverse()
        if result_lst[-1] is '零':
            result_lst.pop()
        result_lst = list(''.join(result_lst))
        for unit_sep in chinese_unit_sep:
            flag = result_lst.count(unit_sep)
            while flag > 1:
                result_lst.pop(result_lst.index(unit_sep))
                flag -= 1
        return ''.join(result_lst)

    def say(self, text):
        # res=subprocess.call('say ' + text,shell=True)
        print(text)
        engine = pyttsx3.init();
        engine.say(text);
        engine.runAndWait();

    def mains(self, stock_code):
        df = ts.get_realtime_quotes(stock_code)  # Single stock symbol
        data = str(df[['name', 'pre_close', 'price', 'amount']]).split()
        # print(data)
        money = int(float(data[-1]))
        if int(money) > 5:
            Amount = round(money / 10000, 0) * 10000
        else:
            Amount = money
        tests = '股票 %s 当前价格  %s ,涨跌幅 %s ,成交量  %s' % (
            data[5], data[7], round((float(data[7]) - float(data[6])) / float(data[6]) * 100, 2),
            self.to_chinese(int(Amount)))
        # print(tests)
        self.say(tests)


if __name__ == '__main__':
    itme = Stock_reporting()
    for i in ['600062', '601607']:
        itme.mains(i)
        sleep(5)
