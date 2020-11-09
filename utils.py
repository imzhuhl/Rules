import argparse
import urllib.request as UR


def get_china_ip_list():
    """下载 china ip list
    """
    url = 'https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt'
    resp = UR.urlopen(url)
    context = resp.read()
    with open('./snippet/china_ip_list.txt', 'w') as f:
        f.write(context.decode('utf-8'))
    

def generate_cn_ip_snippet():
    """根据 china ip list txt 文件生成 snippet
    """
    f = open('./snippet/china_ip_list.txt', 'r')
    lines = f.read()
    f.close()
    lines = lines.strip('\n').split('\n')  # str -> list
    rst = [f'IP-CIDR,{line},DIRECT' for line in lines]
    rst = '\n'.join(rst)  # list -> str

    with open('./snippet/china_ip_list_snippet.txt', 'w') as f:
        f.write(rst)


if __name__ == '__main__':
    # get_china_ip_list()
    generate_cn_ip_snippet()
