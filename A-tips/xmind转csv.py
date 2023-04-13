from xmind2testcase.zentao import xmind_to_zentao_csv_file


def main():
    xmind_file = '/Users/edy/Documents/xmind用例/音视频质检M4.xmind'
    print('Start to convert XMind file: %s' % xmind_file)

    zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
    print('Convert XMind file to zentao csv file successfully: %s' % zentao_csv_file)

    print('Finished conversion, Congratulations!')


if __name__ == '__main__':
    main()
