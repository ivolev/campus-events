from fastapi import FastAPI 

app = FastAPI(title="CampusEvents API")

@app.get("/")
def root():
    return {"status": "ok", "service": "CampusEvents"}

