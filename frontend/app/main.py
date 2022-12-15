from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # used for basic testing
    return {"Hello": "World"}

# get the information stored about a specific run of DataPanels
@app.get("/datapanels/{project_id}/{run_id}")
def read_datapanels_run(run_id: int):
    return {"item_id": run_id}

# post information about a specific run of DataPanels 
@app.post("/datapanels/{project_id}/{run_id}")
def post_datpanels_run(run_id: int, project_id: int, json_obj: str = None):
    return {"project_id": project_id, "run_id": run_id, "q": json_obj}