def str2hex(num_str: str) -> int:
    num_str = '0x' + num_str
    return int(num_str, 16)


def get_color_map(base_color: str, num: int, reverse: bool = False) -> list:
    if len(base_color) != 7:
        raise ValueError('Color must be #------')
    r = str2hex(base_color[1:3])
    g = str2hex(base_color[3:5])
    b = str2hex(base_color[5:7])

    color_map = []

    for i in range(num):
        if reverse:
            r_tmp = int((255 - r) * i / num + r)
            g_tmp = int((255 - g) * i / num + g)
            b_tmp = int((255 - b) * i / num + b)
        else:
            r_tmp = int(r * (i + 1) / num)
            g_tmp = int(g * (i + 1) / num)
            b_tmp = int(b * (i + 1) / num)

        r_tmp = '{:02x}'.format(r_tmp)
        g_tmp = '{:02x}'.format(g_tmp)
        b_tmp = '{:02x}'.format(b_tmp)

        color_map.append('#' + r_tmp + g_tmp + b_tmp)

    return color_map


def main():
    print(get_color_map('#0a64b9', 4))


if __name__ == '__main__':
    main()
    
