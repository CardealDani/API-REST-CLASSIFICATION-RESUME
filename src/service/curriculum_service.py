from fastapi import UploadFile
from typing import Dict, List, Optional
from model.curriculum import Curriculum
from model.curriculum_file import CurriculumFile
from database import curriculum_db
from model.review_model import ReviewResponse
from service.exceptions import  ErrorType, Exceptions
from service.review_service import ReviewService

class CurriculumService:

    @classmethod
    async def create_curriculum(self,id_curriculum: int,file:UploadFile) -> Curriculum:
        id_empty = curriculum_db.curriculums.get(id_curriculum)
        if id_empty:
            raise Exceptions(error_type=ErrorType.ID_EMPTY)
        
        create_file = await self.create_curriculum_file(id_curriculum,file)
        new_curriculum = Curriculum(id = id_curriculum,file_name=file.filename)
        curriculum_db.curriculums[id_curriculum] = new_curriculum
        curriculum_db.curriculum_file[id_curriculum] = create_file

        return new_curriculum
    
    @classmethod
    async def create_curriculum_file(self, id_curriculum: int, file: UploadFile) -> CurriculumFile:
        file_content = await file.read()
        if file.content_type == "application/pdf":
            curriculum_file = CurriculumFile(id=id_curriculum, file= file_content)
            return curriculum_file
        raise Exceptions(error_type=ErrorType.FILE_NOT_SUPPORTED)
        
    
    @classmethod
    async def update_curriculum(self, id_curriculum: int, file: UploadFile) -> Curriculum:
        curriculum = self.get_curriculum_by_id(id_curriculum)
        updated_file = await self.create_curriculum_file(id_curriculum, file)

        if isinstance(updated_file, CurriculumFile):
            curriculum_file = self.get_curriculum_file_by_id(id_curriculum)
            curriculum_file.file = updated_file.file
            curriculum.file_name = file.filename
            return curriculum
        
        return updated_file

    @classmethod
    def get_curriculum_by_id(self, id_curriculum: int) -> Optional[Curriculum]:
        curriculum = curriculum_db.curriculums.get(id_curriculum)
        if not curriculum:
            raise Exceptions(error_type=ErrorType.FILE_NOT_FOUND)
        return curriculum
    
    @classmethod
    def get_curriculum_file_by_id(self, id_curriculum: int) -> Optional[CurriculumFile]:
        curriculum_file = curriculum_db.curriculum_file.get(id_curriculum)
        if not curriculum_file:
            raise Exceptions(error_type=ErrorType.FILE_NOT_FOUND)
        return curriculum_file
    
    
    def get_all_curriculum() -> List[Curriculum]:
        return (curriculum_db.curriculums.values())
    
    @classmethod
    def get_analyzer_by_id(self,id_curriculum:int)-> ReviewResponse:
        curriculum_file = self.get_curriculum_file_by_id(id_curriculum)
        review = ReviewService.get_review(curriculum_file.id,curriculum_file.file)
        return review
    
    @classmethod
    def delete_curriculum(self, id_curriculum: int) -> bool:
        curriculum = self.get_curriculum_by_id(id_curriculum)
        if not curriculum:
            raise Exceptions(error_type=ErrorType.FILE_NOT_FOUND)
        
        del curriculum_db.curriculums[id_curriculum]
        del curriculum_db.curriculum_files[id_curriculum]
        return {"message":"sucessfully deleted"}

    