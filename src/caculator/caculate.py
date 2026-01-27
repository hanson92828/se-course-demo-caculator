from fastapi import FastAPI

app = FastAPI()

def add_func(a: float,b: float) -> float:
    return a+b

def subs_func(a: float,b: float) -> float:
    return a-b

def multi_func(a: float,b: float) -> float:
    return a*b
 
''' ------------------------------------- '''
@app.get("/")
def home():
    return {"status": "Online", "message": "這是簡易計算機 API"}

@app.get("/add")
def calculate_add(a: float, b: float):
    # 調用你的 add_func
    result = add_func(a, b)
    return {"operation": "addition", "a": a, "b": b, "result": result}

@app.get("/subs")
def calculate_subs(a: float, b: float):
    # 調用你的 subs_func
    result = subs_func(a, b)
    return {"operation": "subtraction", "a": a, "b": b, "result": result}

@app.get("/mul")
def calculate_multi(a: float, b: float):
    # 調用你的 multi_func
    result = multi_func(a, b)
    return {"operation": "multiplication", "a": a, "b": b, "result": result}