from abc import ABCMeta, abstractmethod, ABC
from typing import List, Dict

from django.db.models import Q

from REMApp.Repositories import CommentRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.CommentDto import MakeCommentDto, ListCommentDto, DeleteCommentDto


class CommentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """View Options"""
        raise NotImplementedError

    @abstractmethod
    def make(self, model: MakeCommentDto):
        """Makes a comment"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, comment_id: int, model: DeleteCommentDto):
        """Deletes a comment"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListCommentDto]:
        """Lists all Comment"""
        raise NotImplementedError


class DefaultCommentManagementService(CommentManagementService, ABC):
    repository: CommentRepository = None

    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def make(self, model: MakeCommentDto):
        return self.repository.make()

    def delete(self, comment_id: int, model: DeleteCommentDto):
        return self.repository.delete()

    def list(self) -> List[ListCommentDto]:
        return self.repository.list()
