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

Here's an additional section for the README document detailing the structure of the `annotation_coordinates` JSON field:

---

## Annotation Coordinates JSON Structure

The `annotation_coordinates` field in the `annotations` table is designed to store spatial data in JSON format. This allows for flexibility in representing various types of annotations, such as polygons, circles, and points. The JSON structure is crucial for defining the shape and location of each annotation.

### JSON Structure Overview

The `annotation_coordinates` field can store different types of geometrical data. The format includes a `type` key that specifies the annotation type, followed by type-specific data. Below are the supported types and their respective structures:

#### 1. Polygon

Represents a polygon annotation. The JSON structure includes:

- **`type`**: Specifies the shape as a polygon, should be `"Polygon"`.
- **`coordinates`**: Contains vertices of the polygon. Each vertex is an array with `[x, y]` coordinates.

Example:
```json
{
  "type": "Polygon",
  "coordinates": [
    [
      [0, 0],
      [0, 1],
      [1, 1],
      [1, 0],
      [0, 0]
    ]
  ]
}
```

#### 2. Circle

Represents a circular annotation. The JSON structure includes:

- **`type`**: Should be `"circle"`.
- **`center`**: An array specifying the `[x, y]` coordinates of the circle's center.
- **`radius`**: The radius of the circle.

Example:
```json
{
  "type": "circle",
  "center": [0, 0],
  "radius": 1
}
```


#### 3. Point

Represents a single point annotation. The JSON structure includes:

- **`type`**: Should be `"point"`.
- **`coordinates`**: An array specifying the `[x, y]` coordinates of the point.

Example:
```json
{
  "type": "point",
  "coordinates": [0, 0]
}
```

### Usage Notes

- **Flexibility**: The JSON structure allows for easy extension if additional types of annotations are needed in the future. Each type can be added with its own specific data format.

### Example JSON Data

Here's an example of a complete JSON object for annotations including different types:

```json
{
  "image": { "image_id": 1 },
  "annotations": [
    {
      "annotation": "test1",
      "annotation_coordinates": {
        "type": "Polygon",
        "coordinates": [
          [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [0, 0]
          ]
        ]
      }
    },
    {
      "annotation": "test2",
      "annotation_coordinates": {
        "type": "circle",
        "center": [0, 0],
        "radius": 1
      }
    },
    {
      "annotation": "test3",
      "annotation_coordinates": { "type": "point", "coordinates": [0, 0] }
    }
  ]
}
```

This example demonstrates how different annotation types (polygon, circle, and point) are represented using the `annotation_coordinates` field.

---


