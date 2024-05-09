from week6.setting import config as cnf

cnf.DATABASE

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("week6:app", reload=True)