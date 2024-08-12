# Database part of the project

---

# Annotation Table

This document provides an overview of the `annotations` table schema, which is used to store and manage annotations related to images. The table supports various annotation types and includes metadata for tracking and managing these annotations.

## Table Overview

The `annotations` table records detailed information about annotations linked to images. Each entry includes essential metadata, such as creation and update timestamps, and references to the associated image.

## Table Schema

The `annotations` table is defined by the following SQLAlchemy model:

```python
class Annotation(Base):
    __tablename__ = 'annotations'

    id = Column(Integer, primary_key=True)
    user = Column(String(255), nullable=False, default="anonymous")
    annotation = Column(String(1024), nullable=False)
    annotation_coordinates = Column(String(1024), nullable=False)  # JSON
    annotation_created_date = Column(DateTime(timezone=True), server_default=func.now())
    annotation_updated_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    image_id = Column(Integer, ForeignKey('images.id'))
    image = relationship("Image", back_populates="annotations")
```

### Fields

- **`id`**: A unique identifier for each annotation (Primary Key).
- **`user`**: The username or identifier of the person who created the annotation. Defaults to "anonymous".
- **`annotation`**: The text or description of the annotation.
- **`annotation_coordinates`**: A JSON string containing the spatial data defining the annotation's location and shape (e.g., bounding boxes, points, circles).
- **`annotation_created_date`**: Timestamp when the annotation was created. Defaults to the current time.
- **`annotation_updated_date`**: Timestamp when the annotation was last updated. Automatically updated on modification.
- **`image_id`**: Foreign key linking the annotation to a specific image.
- **`image`**: A relationship to the `Image` model, indicating the associated image for the annotation.

## Usage Notes

- The `annotation_coordinates` field is a JSON string that stores spatial data for different types of annotations, including bounding boxes, points, and circles.
- The `user` field helps track the origin of each annotation, with a default value of "anonymous" for unspecified users.
- Timestamps for creation and updates are automatically managed by SQLAlchemy, providing a record of when each annotation was created and last modified.


