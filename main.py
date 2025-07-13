from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math
from typing import Dict

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







# cats


cats_db = Dict[str, dict] = {}
clubs_db = Dict[str, str] = {}


class Cat(BaseModel):
    name: str
    age: int
    type: str

class LoginRequest(BaseModel):
    name: str

class ClubJoinRequest(BaseModel):
    name: str
    club: str

def verify_cat(token: str):
    if token != "meow":
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")
    
@app.post("/cats/register")
def register_cat(cat: Cat):
    if cat.name in cats_db:
        raise HTTPException(status_code=400, detail="cat already registered, please login.")
    cats_db[cat.name] = cat.dict()
    return {"message": "cat successfully registered", "cat_": cats_db[cat.name]}

@app.post("/cats/login")
def login_cat(login: LoginRequest):
    verify_cat(login.name)
    if login.name not in cats_db:
        raise HTTPException(status_code=404, detail="cat not found, please register first.")
    return {"message": "cat successfully logged in", "cat_": cats_db[login.name], "token": "meow"}

@app.post("/cats/join")
def join_club(join: ClubJoinRequest, token: str):
    verify_cat(token)
    if join.name not in cats_db:
        raise HTTPException(status_code=404, detail="cat not found, please register first.")


    clubs_db[join.name] = join.club
    return {"message": f"cat {join.name} has joined club {join.club}"}

@app.get("/cats/club/{name}")
def get_club(name: str):
    if name not in clubs_db:
        raise HTTPException(status_code=404, detail="cat not found or has not joined any club.")
    return {"cat": name, "club": clubs_db[name]}