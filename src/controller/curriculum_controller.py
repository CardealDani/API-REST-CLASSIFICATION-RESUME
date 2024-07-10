from fastapi import APIRouter, File, UploadFile
from typing import List
from model.curriculum import Curriculum
from service.curriculum_service import CurriculumService

class CurriculumController:
    
    router = APIRouter()
    
    @router.post("/curriculums/", response_model=Curriculum)
    async def create_curriculum(id:int, file: UploadFile = File(...))-> Curriculum:
        response =  await CurriculumService.create_curriculum(id_curriculum=id,file=file)
        return response
    
    @router.get("/curriculums/{id_curriculum}", response_model= Curriculum)
    def get_curriculum_by_id(id_curriculum:int):
        curriculum = CurriculumService.get_curriculum_by_id(id_curriculum)
        return curriculum

    @router.get("/curriculums",response_model=List[Curriculum])
    def get_all_curriculum():
        return CurriculumService.get_all_curriculum()

    @router.put("/curriculums/{id_curriculum}", response_model=Curriculum)
    async def update_curriculum(id_curriculum:int, file: UploadFile = File(...)) -> Curriculum:
        response = await CurriculumService.update_curriculum(id_curriculum,file)
        return response
    
    @router.get("/curriculums/{id_curriculum}/review")
    def get_review(id_curriculum:int):
        response = CurriculumService.get_analyzer_by_id(id_curriculum)
        return response

    @router.delete("/curriculums/{id_curriculum}")
    def delete_curriculum(id_curriculum:int):
        delete =  CurriculumService.delete_curriculum(id_curriculum)
        return delete
            
