import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import query_comments, create_comments_table

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = os.path.join("/app", "frontend")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/comments")
def get_comments():
    rows = query_comments()
    comments_json = []
    for row in rows:
        comments_json.append({
            "id": row[0],
            "content": row[1],
            "date": row[2]
        })
    return comments_json


if __name__ == "__main__":
    create_comments_table("comments")
    create_comments_table("invalid_comments")
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)




