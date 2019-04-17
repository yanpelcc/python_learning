import datetime

try:
    open('balance_sheet.txt','r')
except:
    with open('balance_sheet.txt', 'w') as f:
        f.write('结算日期 资产/万 负债/万 净资产/万\n')
        f.write('{} 0 0 0\n'.format(datetime.datetime.now().date()))

try:
    open('flow_bill.txt', 'r')
except:
    with open('flow_bill.txt', 'w+') as f:
        f.write('交易对象 收入/万 支出/万 应收账款/万 应出账款/万 交易日期\n')

function = input("1.查账；2.记账\n请选择服务：")

if int(function) == 2:
    with open('balance_sheet.txt', 'r') as f:
        x = f.readlines()
        data = x[-1]
        data_list = data.split()
        assets = eval(data_list[1])
        debt = eval(data_list[2])
        n_assets = eval(data_list[3])

    print("记账模式")
    object = input("交易对象：")
    income = input("收入/万：")
    expend = input("支出/万：")
    ar = input("应收账款/万：")
    ap = input("应出账款/万：")

    assets = assets + int(income) - int(expend)
    debt = debt + int(ap) - int(ar)
    n_assets = assets - int(debt)

    with open('balance_sheet.txt', 'a') as f:
        f.write('{} {} {} {}\n'.format(datetime.datetime.now().date(),assets,debt,n_assets))

    with open('flow_bill.txt', 'a') as f:
        f.write('{} {} {} {} {} {}\n'.format(object,income,expend,ar,ap,datetime.datetime.now().date()))

    print("交易已记录\n当前资产状况：\n最新资产：%d\n最新负债：%d\n最新净资产：%d" % (assets,debt,n_assets))

if int(function) == 1:
    function_2 = input('查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易来\n3.查询最近资产负债状况\n请选择服务：')

    if int(function_2) == 1:
        print("最近十笔交易")
        with open('flow_bill.txt', 'r') as f:
            x = f.readlines()
            print(x[0])
            for i in range(-1,-11,-1):
                try:
                    if x[i] == x[0]:
                        break
                    else:
                        print(x[i])
                except:
                    break

    if int(function_2) == 2:
        count = 0
        object = input('请输入公司名：')
        with open('flow_bill.txt', 'r') as f:
            data = f.readlines()
            for i in data:
                if object in i:
                    count += 1
            print('与{}共有{}笔交易'.format(object,count))
            for i in data[1:]:
                if object in i:
                    bill = i.split()
                    print('交易时间：{}\n收入：{}\n支出：{}\n应收账款：{}\n应出账款：{}'.format(bill[5],bill[1],bill[2],bill[3],bill[4]))

    if int(function_2) == 3:
        with open('balance_sheet.txt','r') as f:
            data = f.readlines()
            l_assent = data[-1].split()
            print('最新资产：{}\n最新负债：{}\n最新净资产：{}\n最后更新时间：{}'.format(l_assent[1],l_assent[2],l_assent[3],l_assent[0]))

