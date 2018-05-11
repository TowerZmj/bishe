import numpy as np
import matplotlib.pyplot as plt
from random import randint


def draw_users_brows_columnar(user_id_list, users_tensor, user_count=10):
    length = len(user_id_list)
    random_index_list = [randint(0, length) for _ in range(user_count)]
    pic_user_id_list = list()
    for index in random_index_list:
        pic_user_id_list.append(str(user_id_list[index]))
    click_list = list()
    add_to_cart_list = list()
    purchase_list = list()
    add_to_fav_list = list()
    for user_id in pic_user_id_list:
        user_id = int(user_id)
        user_tensor = users_tensor[user_id]
        click_count = np.sum(user_tensor.tensor[:, 0])
        click_list.append(click_count)
        add_to_cart_count = np.sum(user_tensor.tensor[:, 1])
        add_to_cart_list.append(add_to_cart_count)
        purchase_count = np.sum(user_tensor.tensor[:, 2])
        purchase_list.append(purchase_count)
        add_to_fav_count = np.sum(user_tensor.tensor[:, 3])
        add_to_fav_list.append(add_to_fav_count)

    x = np.arange(0, 2*user_count, 2) + 1
    total_width, n = 1.6, 4
    width = total_width / n

    plt.bar(x, click_list, width=width, label='click', fc='y')
    x = x + width
    plt.bar(x, add_to_cart_list, width=width, label='add-to-cart', tick_label=pic_user_id_list, fc='r')
    x = x + width
    plt.bar(x, purchase_list, width=width, label='purchase', fc='g')
    x = x + width
    plt.bar(x, add_to_fav_list, width=width, label='add-to-fav', fc='b')
    plt.legend()
    plt.show()


def draw_users_dirty_columnar(user_id_list, users_tensor, user_count=10):
    length = len(user_id_list)
    random_index_list = [randint(0, length-1) for _ in range(user_count)]
    pic_user_id_list = list()
    for index in random_index_list:
        pic_user_id_list.append(str(user_id_list[index]))

    other_count_list = list()
    one_click_count_list = list()
    for user_id in pic_user_id_list:
        user_id = int(user_id)
        user_tensor = users_tensor[user_id]
        tensor = user_tensor.tensor
        total_count = tensor.shape[0]
        one_click_list = user_tensor.is_one_click()
        one_click_count = len(one_click_list)
        one_click_count_list.append(one_click_count)
        other_count = total_count - one_click_count
        other_count_list.append(other_count)
    x = np.arange(user_count) + 1
    plt.bar(x, one_click_count_list, label='one_click', fc='y')
    plt.bar(x, other_count_list, bottom=one_click_count_list, label='other', tick_label=pic_user_id_list, fc='r')
    plt.legend()
    plt.show()



