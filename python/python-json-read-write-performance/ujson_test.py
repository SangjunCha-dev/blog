import ujson  # pip install ujson
import timeit

class CheckTime:
    def __init__(self):
        self.path = "data"
        self.filename = "github"
        self.filepath = f"{self.path}/{self.filename}"
        self.extension = ".json"
        self.data1 = None
        self.data2 = None

    def ujson_r(self):
        with open(f'{self.filepath}{self.extension}', "r") as json_file:
            self.data1 = ujson.loads(json_file.read())
        
    def ujson_w_dumps(self):
        with open(f'{self.filepath}_w_dumps{self.extension}', "w") as json_file:
            data = ujson.dumps(self.data1)
            json_file.write(data)

    def ujson_rb(self):
        with open(f'{self.filepath}{self.extension}', "rb") as json_file:
            self.data2 = ujson.load(json_file)
        
    def ujson_wb_dumps(self):
        with open(f'{self.filepath}_wb_dumps{self.extension}', "wb") as json_file:
            data = ujson.dumps(self.data2).encode('utf-8')
            json_file.write(data)

    def get_time(self):
        print(__class__.__name__)
        repeat_count = 100

        print("===============================")

        def test_ujson_r():
            self.ujson_r()
        ujson_r_time = timeit.Timer(stmt=test_ujson_r).repeat(number=repeat_count)
        print(f"ujson_r = {sum(ujson_r_time)/len(ujson_r_time)} sec")

        def test_ujson_w_dumps():
            self.ujson_w_dumps()
        ujson_w_dumps_time = timeit.Timer(stmt=test_ujson_w_dumps).repeat(number=repeat_count)
        print(f"ujson_w_dumps = {sum(ujson_w_dumps_time)/len(ujson_w_dumps_time)} sec")

        print("===============================")

        def test_ujson_rb():
            self.ujson_rb()
        ujson_rb_time = timeit.Timer(stmt=test_ujson_rb).repeat(number=repeat_count)

        print(f"ujson_rb = {sum(ujson_rb_time)/len(ujson_rb_time)} sec")

        def test_ujson_wb_dumps():
            self.ujson_wb_dumps()
        ujson_wb_dumps_time = timeit.Timer(stmt=test_ujson_wb_dumps).repeat(number=repeat_count)

        print(f"ujson_wb_dumps = {sum(ujson_wb_dumps_time)/len(ujson_wb_dumps_time)} sec")


checkTime = CheckTime()
checkTime.get_time()
