import requests
from lxml import etree


def req(url):

    data = requests.get(url)

    return data


def parse(data):

    tree = etree.HTML(data.text)
    xpath_div = tree.xpath('//div[@class="article block untagged mb15 typs_hot"] '
                           '| //div[@class="article block untagged mb15 typs_long"]')

    data = ''
    for div in xpath_div:

        content = div.xpath('.//div[@class="content"]/span/text()')
        content = dis(content)
        author = div.xpath('.//h2/text()')
        author = dis(author)
        funny_count = div.xpath('.//i[@class="number"]/text()')[0]
        repost_count = div.xpath('.//i[@class="number"]/text()')[1]

        head = '作者:'+ author[0] + '\n好笑数:' + funny_count + '\n评论数:' + repost_count
        content = head + '\n' + ''.join(content) + '\n\n'

        data += content
        
    return data


def dis(in_list):

    out_list = [x.strip() for x in in_list if x.strip() != '']

    return out_list


def save(data):

    with open('qsbk.txt','a') as f:
        f.write(data)


def get_page(data):
    tree = etree.HTML(data.text)
    current_page = tree.xpath('//ul[@class="pagination"]/li/span[@class="current"]/text()')
    current_page = dis(current_page)

    return current_page[0]


def main():

    with open('qsbk.txt','w') as f:
        f.write('')

    url = 'https://www.qiushibaike.com/text/page/1/'
    n = eval(input("你想看几页:"))
    for i in range(n):
        req_data = req(url)
        page = get_page(req_data)
        parse_data = parse(req_data)
        save(parse_data)
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(int(page)+1)


main()
