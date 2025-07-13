from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def default():
    return {"message": "welcome to apicat!"}


#https://www.geeksforgeeks.org/dsa/check-for-prime-number/
@app.get("/isPrime_sixMethod/{number}")
def is_prime_six_method(number: int):
    if number < 2:
        return {"is_prime": False}
    if number == 2 or number == 3:
        return {"is_prime": True}
    if number % 2 == 0 or number % 3 == 0:
        return {"is_prime": False}
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return {"is_prime": False}
        i += 6
    
    return {"is_prime": True}

#https://www.geeksforgeeks.org/dsa/check-for-prime-number/
@app.get("/isPrime_bruteForceSqrt/{number}")
def is_prime_bruteForceSqrt(number: int):
    if number < 2:
        return {"is_prime": False}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

#https://www.geeksforgeeks.org/dsa/check-for-prime-number/
@app.get("/isPrime_bruteForce/{number}")
def is_prime_bruteForce(number: int):
    if number < 2:
        return {"is_prime": False}
    for i in range(2, number):
        if number % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}


#https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended/
def gcd_euclid(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd_euclid(b % a, a)

#https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended/
@app.get("/gcd_eulerBasic/{a}/{b}")
def gcd_euler_basic(a: int, b: int):
    if a == 0 and b == 0:
        raise HTTPException(status_code=400, detail="Illegal paramaters: both a and b cannot be zero.")
    return {"gcd": abs(gcd_euclid(a, b))}

def gcd_extendedEuclid(a: int, b: int, x, y) -> int:
    if a == 0:
        x[0] = 0
        y[0] = 1
        return b
    
    x1 = [0]
    y1 = [0]
    gcd = gcd_extendedEuclid(b % a, a, x1, y1)

    x[0] = y1[0] - (b // a) * x1[0]
    y[0] = x1[0]
    return gcd


#https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended/
@app.get("/gcd_eulerExtended/{a}/{b}")
def gcd_euler_extended(a: int, b: int):
    if a == 0 and b == 0:
        raise HTTPException(status_code=400, detail="Illegal paramaters: both a and b cannot be zero.")
    
    x = [0]
    y = [0]
    gcd = gcd_extendedEuclid(a, b, x, y)
    
    return {"gcd": abs(gcd)}


class CatNode(BaseModel):
    category: str
    children: list[str] = []

@app.get("/cats/cats")
def get_cats():
    return CatNode(
        category="all",
        children=[
            "domestic",
            "wild",
        ]
    )

@app.get("/cats/domestic")
def get_domestic_cats():
    return CatNode(
        category="domestic",
        children=[
            "shorthair",
            "longhair",
        ]
    )

@app.get("/cats/wild")
def get_wild_cats():
    return CatNode(
        category="wild",
        children=[
            "lion",
            "tiger",
            "leopard",
        ]
    )
@app.get("/cats/domestic/domestic_shorthair")
def get_domestic_shorthair_cats():
    return CatNode(
        category="domestic shorthair",
        children=[
            "american shorthair",
            "british shorthair",
            "manx",
        ]
    )
@app.get("/cats/domestic/domestic_longhair")
def get_domestic_longhair_cats():
    return CatNode(
        category="domestic longhair",
        children=[
            "persian",
            "maine coon",
        ]
    )

@app.get("/cats/wild/lion")
def get_wild_lion_cats():
    return CatNode(
        category="lion",
        children=[
            "masai lion",
        ]
    )

@app.get("/cats/wild/tiger")
def get_wild_tiger_cats():
    return CatNode(
        category="tiger",
        children=[
            "sumatran tiger",
            "malayan tiger",
            "south china tiger",
        ]
    )

@app.get("/cats/wild/leopard")
def get_wild_leopard_cats():
    return CatNode(
        category="leopard",
        children=[
            "amur leopard",
            "sri lankan leopard",
        ]
    )

@app.get("/cats/domestic/shorthair/american_shorthair")
def get_domestic_american_shorthair_cats():
    return CatNode(
        category="american shorthair",
        children=[]
    )

@app.get("/cats/domestic/shorthair/british_shorthair")
def get_domestic_british_shorthair_cats():
    return CatNode(
        category="british shorthair",
        children=[]
    )

@app.get("/cats/domestic/shorthair/manx")
def get_domestic_manx_cats():
    return CatNode(
        category="manx",
        children=[]
    )

@app.get("/cats/domestic/longhair/persian")
def get_domestic_persian_cats():
    return CatNode(
        category="persian",
        children=[]
    )
@app.get("/cats/domestic/longhair/maine_coon")
def get_domestic_maine_coon_cats():
    return CatNode(
        category="maine coon",
        children=[]
    )

@app.get("/cats/wild/lion/masai_lion")
def get_wild_masai_lion_cats():
    return CatNode(
        category="masai lion",
        children=[]
    )

@app.get("/cats/tiger/sumatran_tiger")
def get_wild_sumatran_tiger():
    return CatNode(
        category="sumatran_tiger",
        children=[]
    )

@app.get("/cats/wild/tiger/malayan_tiger")
def get_wild_malayan_tiger():
    return CatNode(
        category="malayan tiger",
        children=[]
    )

@app.get("/cats/wild/tiger/south_china_tiger")
def get_wild_south_china_tiger():
    return CatNode(
        category="south china tiger",
        children=[]
    )

@app.get("/cats/wild/leopard/amur_leopard")
def get_wild_amur_leopard():
    return CatNode(
        category="amur leopard",
        children=[]
    )

@app.get("/cats/wild/leopard/sri_lankan_leopard")
def get_wild_sri_lankan_leopard():
    return CatNode(
        category="sri lankan leopard",
        children=[]
    )