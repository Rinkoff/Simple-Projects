class Items:

    @staticmethod
    def read_items(file):
        with open(file, "r") as f:
            items = []
            for line in f:
                data = line.strip().split(";")
                items.append(data)
            return items

    @staticmethod
    def create_item(file,item):
        with open(file, "a") as f:
            f.write(f"\n{item[0]};{item[1]};{item[2]};{item[3]};{item[4]}")

    @staticmethod
    def read_item_by_title(file,title):
        with open(file, "r") as f:
            for line in f:
                data = line.strip().split(";")
                if data[0] == title:
                    return data[0], data[1], data[2], int(data[3]), data[4]

    @staticmethod
    def update_items_by_title(file, title, *args, **kwargs):
        items = []
        with open(file, "r") as f:
            for line in f:
                data = line.strip().split(";")
                if data[0] == title:
                    for key, value in kwargs.items():
                        if key == "title":
                            data[0] = value
                        elif key == args[0]:
                            data[1] = value
                        elif key == "genre":
                            data[2] = value
                        elif key == "year":
                            data[3] = value
                        elif key == args[1]:
                            data[4] = value
                item = data[0], data[1], data[2], int(data[3]), data[4]
                items.append(item)

        with open(file, "w") as f:
            for item in items:
                f.write(f"{item[0]};{item[1]};{item[2]};{item[3]};{item[4]}\n")

    @staticmethod
    def delete_item_by_title(file,title):
        items = []
        with open(file, "r") as f:
            for line in f:
                data = line.strip().split(";")
                if data[0] != title:
                    item = data[0], data[1], data[2], int(data[3]), data[4]
                    items.append(item)

        with open(file, "w") as f:
            for item in items:
                f.write(f"{item[0]};{item[1]};{item[2]};{item[3]};{item[4]}\n")


    @staticmethod
    def search_in_items(text,func):
        items = func
        founded = []

        for item in items:
            in_items = list(filter(lambda field: text in field, item))
            if len(in_items) > 0:
                founded.append(item)
        return founded