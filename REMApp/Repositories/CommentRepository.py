from abc import ABCMeta, abstractmethod, ABC
from typing import List
from django.contrib.auth.models import Group

from REMApp.dto.CommentDto import MakeCommentDto, ListCommentDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Comment


class Comment_repository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an order for object"""
        raise NotImplementedError

    @abstractmethod
    def make(self, model: MakeCommentDto):
        """Makes a comment"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListCommentDto]:
        """Lists all Comment"""
        raise NotImplementedError

    @abstractmethod
    def get(self, clientId: str):
        """Gets clients details"""
        raise NotImplementedError


class DjangoORMCommentRepository(Comment_repository, ABC):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        comment = Comment.objects.values("propertyId, commentId")
        return [SelectOptionDto(c["time"], c["date"]) for c in comment]

    def make(self, model: MakeCommentDto):
        comment = Comment()
        comment.property_id = model.propertyId
        comment.comment = model.comment

        # Makes comment
        status = Comment.objects.create(model.propertyId, model.comment)
        status.commentTime = model.commentTime
        status.save()

        comment.status = status
        comment = Group.objects.values()
        status.date.add(comment)

        comment.save()

    def list(self) -> List[ListCommentDto]:
        comment = Comment.objects.values("commentId",
                                         "propertyId")

        result: List[ListCommentDto] = []
        for a in comment:
            item = ListCommentDto()
            item.comment_id = a["commentId"]
            item.property_id = a["propertyId"]
            result.append(item)
        return result

    def get(self, commentId: int):
        try:
            comment = Comment.objects.get(id=commentId)
            result = ListCommentDto()
            result.commentId = comment.commentId

            result.commentId = comment.commentId
            result.property_id = comment.property_id
            return comment
        except Comment.DoesNotExist as a:
            message = "comment does not exist"
            print(message)
            raise a
