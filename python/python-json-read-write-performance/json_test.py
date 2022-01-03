import timeit
import json

class CheckTime:
    def __init__(self):
        self.path = "data"
        self.filename = "github"
        self.filepath = f"{self.path}/{self.filename}"
        self.extension = ".json"
        self.data1 = None
        self.data2 = None

    def json_r(self):
        with open(f'{self.filepath}{self.extension}', "r") as json_file:
            self.data1 = json.load(json_file)
        
    def json_w_dump(self):
        with open(f'{self.filepath}_w_dump{self.extension}', "w") as json_file:
            data = self.data1
            json.dump(data, json_file)

    def json_w_dumps(self):
        with open(f'{self.filepath}_w_dumps{self.extension}', "w") as json_file:
            data = json.dumps(self.data1)
            json_file.write(data)

    def json_rb(self):
        with open(f'{self.filepath}{self.extension}', "rb") as json_file:
            self.data2 = json.load(json_file)
        
    def json_wb_dumps(self):
        with open(f'{self.filepath}_wb_dumps{self.extension}', "wb") as json_file:
            data = json.dumps(self.data2).encode('utf-8')
            json_file.write(data)

    def get_time(self):
        print(__class__.__name__)
        repeat_count = 100

        print("===============================")

        def test_json_r():
            self.json_r()
        json_r_time = timeit.Timer(stmt=test_json_r).repeat(number=repeat_count)
        print(f"json_r = {sum(json_r_time)/len(json_r_time)} sec")

        def test_json_w_dump():
            self.json_w_dump()
        json_w_dump_time = timeit.Timer(stmt=test_json_w_dump).repeat(number=repeat_count)
        print(f"json_w_dump = {sum(json_w_dump_time)/len(json_w_dump_time)} sec")

        def test_json_w_dumps():
            self.json_w_dumps()
        json_w_dumps_time = timeit.Timer(stmt=test_json_w_dumps).repeat(number=repeat_count)
        print(f"json_w_dumps = {sum(json_w_dumps_time)/len(json_w_dumps_time)} sec")

        print("===============================")

        def test_json_rb():
            self.json_rb()
        json_rb_time = timeit.Timer(stmt=test_json_rb).repeat(number=repeat_count)

        print(f"json_rb = {sum(json_rb_time)/len(json_rb_time)} sec")

        def test_json_wb_dumps():
            self.json_wb_dumps()
        json_wb_dumps_time = timeit.Timer(stmt=test_json_wb_dumps).repeat(number=repeat_count)

        print(f"json_wb_dumps = {sum(json_wb_dumps_time)/len(json_wb_dumps_time)} sec")


checkTime = CheckTime()
checkTime.get_time()
