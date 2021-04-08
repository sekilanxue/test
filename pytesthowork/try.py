import yaml


def get_datas():
    with open("./deomo/data_demo.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas
if __name__ == '__main__':
    get_datas()