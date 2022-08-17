import random
import time


def cut():
    text = "To be or not to be  "
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
    # while True:
    #
    #     # print("split_text", split_text)
    #     rand = random.randint(1, 3)
    #     exit_str = split_text[0:rand]
    #     try:
    #         while rand > 0:
    #             del split_text[0]
    #             rand = rand - 1
    #         print(len(split_text))
    #         print("print(split_text)",split_text)
    #
    #         split_text = split_text
    #
    #     except (ValueError, IndexError,Exception) as e:
    #         print(len(split_text))
    #         print(split_text)
    #
    #         if len(split_text) >= 1:
    #             print(split_text)
    #
    #         print(e)
    #         break
    #     # print(split_text)
    #
    #     print(exit_str)
    #



cut()
