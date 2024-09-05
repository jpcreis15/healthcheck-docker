from fastapi import APIRouter, FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

import random
import time
################################################################################

router = APIRouter(
    prefix="/api",
    tags=["healthcheck-docker"]
)

@router.get("/healthz")
async def healthz():
    num = random.random()
    print(num)

    if num > 0.5:
        print("Health - I'm healthy")
        return {'state': 'healthy'}
    else:
        print("Health - I'm stuck....waiting to reboot")
        time.sleep(60)
        return {'state': 'healthy'}

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

# Instrumentator().instrument(app).expose(app)