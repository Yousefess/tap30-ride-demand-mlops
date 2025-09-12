import os
from pathlib import Path

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.config_reader import read_config

config_path = "config/config.yaml"
web_config = read_config(config_path)["web"]

model_dir = web_config["model_output_dir"]
model_name = web_config["model_name"]

model = joblib.load(Path(model_dir) / model_name)

app = FastAPI()


class DemandRequest(BaseModel):
    hour_of_day: int = Field(ge=0, le=23, description="Hour of day (0-23)")
    day: int = Field(ge=0, description="Day number")
    row: int = Field(ge=0, le=7, description="Row index (0-7)")
    col: int = Field(ge=0, le=7, description="Column index (0-7)")


class DemandResponse(BaseModel):
    demand: int


@app.post("/predict", response_model=DemandResponse)
def predict_demand(request: DemandRequest):
    features = pd.DataFrame(
        [
            {
                "hour_of_day": request.hour_of_day,
                "day": request.day,
                "row": request.row,
                "col": request.col,
            }
        ]
    )

    prediction = model.predict(features)[0]
    return {"demand": round(prediction)}


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=os.environ.get("WEB_HOST", web_config["host"]),
        port=int(os.environ.get("WEB_PORT", web_config["port"])),
        reload=True,
    )
