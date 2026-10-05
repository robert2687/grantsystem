from fastapi import FastAPI

app = FastAPI(
 title="GrantSystem API",
 version="0.1.0"
)

@app.get("/")
def root():
 return {"status": "GrantSystem OK"}

@app.get("/health")
def health():
 return {"status": "healthy"}
