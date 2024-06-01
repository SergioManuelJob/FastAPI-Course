from fastapi import HTTPException, Header

def validate_token(token: str = Header(...)):
    if token != "Bearer":
        raise HTTPException(status_code=401, detail="Token is invalid")