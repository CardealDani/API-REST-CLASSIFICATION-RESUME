from fastapi import FastAPI
from controller.curriculum_controller import CurriculumController as curriculum_controller
app = FastAPI()

app.include_router(curriculum_controller.router)
