from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# class Image(Base):
#     __tablename__ = 'images'
#     id = Column(Integer, primary_key=True)
#     image_name = Column(String(255), unique=True, nullable=False)
#     image_url = Column(String(255), unique=True, nullable=False)
#     upload_date = Column(DateTime(timezone=True), server_default=func.now())
#     annotations: Mapped[List["Annotation"]] = relationship(
#         "Annotation", back_populates="image")
#
#     # annotations: Mapped[List["Annotation"]] = relationship(
#     #     back_populates="parent")
#
#     def __init__(self, name=None, url=None):
#         self.image_name = name
#         self.image_url = url
#
#     def __repr__(self):
#         return f'<Image {self.image_name!r}>'


class Annotation(Base):
    __tablename__ = 'annotations'
    id = Column(Integer, primary_key=True)
    # image: Mapped["Image"] = relationship(back_populates="image")
    user_id = Column(Integer)
    image_id = Column(String(1024), unique=False, nullable=False)
    annotation_id = Column(String(64), unique=True, nullable=False)
    annotation = Column(String(1024 * 2), unique=False, nullable=False)
    annotation_created_date = Column(DateTime(timezone=True),
                                     server_default=func.now())
    annotation_updated_date = Column(DateTime(timezone=True),
                                     server_default=func.now(),
                                     onupdate=func.now())

    # image_id = Column(Integer, ForeignKey('images.id'))
    # image: Mapped["Image"] = relationship("Image",
    #                                       back_populates="annotations")
    #
    def __init__(self, user_id, image_id, annotation_id, annotation):
        self.user_id = user_id
        self.image_id = image_id
        self.annotation_id = annotation_id
        self.annotation = annotation

    def __repr__(self):
        return f'<Annotation {self.annotation!r}>'
