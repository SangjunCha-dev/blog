import orjson  # pip install orjson
import timeit

class CheckTime:
    def __init__(self):
        self.path = "data"
        self.filename = "github"
        self.filepath = f"{self.path}/{self.filename}"
        self.extension = ".json"
        self.data1 = None
        self.data2 = None

    def orjson_r(self):
        with open(f'{self.filepath}{self.extension}', "r") as json_file:
            self.data1 = orjson.loads(json_file.read())
        
    def orjson_w_dumps(self):
        with open(f'{self.filepath}_w_dumps{self.extension}', "w") as json_file:
            data = orjson.dumps(self.data1).decode('utf-8')
            json_file.write(data)

    def orjson_rb(self):
        with open(f'{self.filepath}{self.extension}', "rb") as json_file:
            self.data2 = orjson.loads(json_file.read())
        
    def orjson_wb_dumps(self):
        with open(f'{self.filepath}_wb_dumps{self.extension}', "wb") as json_file:
            data = orjson.dumps(self.data2)
            json_file.write(data)

    def get_time(self):
        print(__class__.__name__)
        repeat_count = 100

        print("===============================")

        def test_orjson_r():
            self.orjson_r()
        orjson_r_time = timeit.Timer(stmt=test_orjson_r).repeat(number=repeat_count)
        print(f"orjson_r = {sum(orjson_r_time)/len(orjson_r_time)} sec")

        def test_orjson_w_dumps():
            self.orjson_w_dumps()
        orjson_w_dumps_time = timeit.Timer(stmt=test_orjson_w_dumps).repeat(number=repeat_count)
        print(f"orjson_w_dumps = {sum(orjson_w_dumps_time)/len(orjson_w_dumps_time)} sec")

        print("===============================")

        def test_orjson_rb():
            self.orjson_rb()
        orjson_rb_time = timeit.Timer(stmt=test_orjson_rb).repeat(number=repeat_count)

        print(f"orjson_rb = {sum(orjson_rb_time)/len(orjson_rb_time)} sec")

        def test_orjson_wb_dumps():
            self.orjson_wb_dumps()
        orjson_wb_dumps_time = timeit.Timer(stmt=test_orjson_wb_dumps).repeat(number=repeat_count)

        print(f"orjson_wb_dumps = {sum(orjson_wb_dumps_time)/len(orjson_wb_dumps_time)} sec")


checkTime = CheckTime()
checkTime.get_time()
