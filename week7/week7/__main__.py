from week7.setting import config as cnf

cnf.DATABASE

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("week7:app", reload=True)