

import random
import time


def cut():
    text = "«Life is what happens when you're busy making other plans» John Lennon   "
    global split_text, local_str
    split_text = text.split(" ")
    random_int = 0
    len_split_text = len(split_text)
    # print(len_split_text)
    local_list = []
    for i in split_text:

        rand = random.randint(1, 20)
        # print(i)
        if rand <= 10:
            local_list.append(i)
        else:
            local_list.append(i)
            # print(local_list)
            local_str = ""
            for s in local_list:
                local_str += ''.join(s)
                local_str += " "
            print(local_str)
            # print(local_str)

            local_list = []


cut()
