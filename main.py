from fastapi import FastAPI

app = FastAPI(title="Python EKS Application")

@app.get("/")
def home():
    return {"message": "Hello from Python on Amazon EKS"}

@app.get("/health")
def health():
    return {"status": "healthy"}
