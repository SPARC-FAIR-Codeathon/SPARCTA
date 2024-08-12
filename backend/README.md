
---

# Image Annotation Backend

This project is a Flask-based web application designed for managing image annotations. It allows users to upload images, view them, and add, update, or delete annotations. The project uses SQLAlchemy for database management and integrates with Deep Zoom for handling large image files.

## Features

- **Upload and View Images**: Upload images and view them in the web interface.
- **Annotations**: Add, update, or delete annotations for the uploaded images.
- **Deep Zoom Integration**: Convert TIFF images to Deep Zoom Image (DZI) format for efficient viewing of large images.
- **Database Management**: Uses SQLAlchemy for ORM and database operations.

## Project Structure

- **`__init__.py`**: Initializes the Flask application and defines routes for handling image and annotation operations.
- **`database.py`**: Sets up the database connection using SQLAlchemy and initializes the database schema.
- **`image.py`**: Handles the downloading, processing, and conversion of image files to the DZI format using Deep Zoom.
- **`models.py`**: Defines the database models for `Image` and `Annotation`, representing images and their associated annotations.

---

### Image Upload and Conversion

The application is designed to handle high-resolution TIFF image files efficiently. Here’s a detailed overview of how the image upload and conversion process works:

1. **Image Upload**:
   - Users can upload TIFF images through the web interface or via API endpoints. TIFF is a flexible format that supports high-quality images and is often used for detailed imagery.
   - Upon upload, the image is stored temporarily on the server while processing begins.

2. **Automatic Conversion**:
   - Once the TIFF file is uploaded, it is automatically converted to the Deep Zoom Image (DZI) format. This conversion is crucial for managing large images effectively.
   - **Deep Zoom Image (DZI)**: DZI is a format designed to allow users to view high-resolution images at different zoom levels without performance issues. It breaks down the image into smaller tiles and levels of detail, facilitating smooth and fast rendering even for very large images.

3. **Storage and Management**:
   - After conversion, the DZI files are organized in a directory structure within the `./static/dataset` folder. This structured storage ensures that images are accessible for rendering and querying.
   - The TIFF files themselves are removed post-conversion to save storage space, leaving only the DZI files and necessary metadata.

4. **Database Integration**:
   - Information about the uploaded images, including their file paths and conversion details, is stored in a SQLite database. This database maintains a record of each image's metadata and allows for efficient retrieval and management.
   - The database schema includes tables for storing image details and annotations, linking them together for comprehensive management.

5. **Error Handling**:
   - If the conversion process encounters any issues (e.g., unsupported image formats or corrupted files), appropriate error messages are generated, and the user is informed of the problem.

By converting TIFF images to DZI format, the application ensures that users can interact with high-resolution images smoothly, leveraging efficient loading and zooming capabilities while maintaining high image quality.

---

## Requirements

To set up the project, you'll need to install the required Python packages. These dependencies are specified in The `requirements.txt` file includes the following packages:


- **`Werkzeug==2.2.2`**: A comprehensive WSGI web application library that Flask depends on for various utilities and functionalities.
- **`flask==2.2.3`**: A lightweight WSGI web application framework that provides the core functionality for the project.
- **`SQLAlchemy==2.0.32`**: A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database interactions.
- **`scikit-image==0.24.0`**: A collection of algorithms for image processing, used for handling and processing image data.
- **`sparc-me==3.0.0`**: A library for interacting with the SPARC dataset API.
- **`Pillow==9.5.0`**: The Python Imaging Library (PIL) fork, used for opening, manipulating, and saving image files.
- **`DeepZoomTools @ git+https://github.com/openzoom/deepzoom.py@master`**: A library for creating Deep Zoom Images (DZI) from high-resolution images, fetched directly from the GitHub repository.

By installing these dependencies, you'll set up the environment needed to run and develop the project. Ensure you have Python 3.7 or later to avoid compatibility issues.

---
