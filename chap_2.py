#2-1 索引操作实例
# 将已数指定年、月、日的日期打印出来
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
# 一个列表，其中包含1～31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
    + ['st']

# year = input('Year: ')
# month_number = input('Month(1-12): ')
# day_number = input('Day(1-31): ')

#别忘了将表示月和日的数减1，这样才能得到正确的索引
# month_name = months[int(month_number) - 1]
# ordinal = day_number + endings[int(day_number) - 1]
# print(month_name + ' ' + ordinal + ',' + year)

# 2-2 切片操作示例
# # 从类似与 http://wwww.something.com 的URL 中提取域名
# url = input('Please enter the URL: ')
# domain = url[11:-4]
# print('Domain name: ' + domain)

# 序列（字符串）乘法运算示例
#在位于屏幕中央宽度合适的方框内打印一个句子
# sentence = input('Sentence: ')
# screen_width = 80
# text_width = len(sentence)
# box_with = text_width + 6
# left_margin = (screen_width - box_with) // 2
#
# print()
# print(' ' * left_margin + '+' + '-' * (box_with - 2) + '+')
# print(' ' * left_margin + '|' + '-' * text_width     + '+')
# print(' ' * left_margin + '|' +       sentence       + '+')
# print(' ' * left_margin + '|' + '-' * text_width     + '+')
# print(' ' * left_margin + '+' + '-' * (box_with - 2) + '+')
# print()

# 2-4 序列成员的资格示例
# 检查用户名和PIN码
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input('User name: ')
pin = input('PIN code: ')
if [username, pin] in database: print('Access gtanted')
