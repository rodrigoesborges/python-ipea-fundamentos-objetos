import json

from my_first_file import reading, recover_list


def save_json(ob):
    with open('my_obj.json', 'w') as f:
        json.dump(ob, f, indent=4)
    print('Saved! You can check my_obj.json')


def load_json():
    with open("my_obj.json", "r") as f:
        ll = json.load(f)
    print(f'A soma da lista lida é {sum(ll):,.0f}')
    return ll


if __name__ == '__main__':
    r = reading()
    l = recover_list(r)
    save_json(l)
    l_lida = load_json()
    print(l_lida)
