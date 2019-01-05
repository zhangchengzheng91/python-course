# 3-1 字符串格式设置显示
# 根据指定的宽度打印格式良好的价格表
width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('fmt=', fmt)
print('=' * width)

print(header_fmt.format('Item', 'Price'))

print('-' * width)

print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots(16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))

print('=' * width)