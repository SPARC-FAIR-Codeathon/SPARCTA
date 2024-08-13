
# SPARC Tiff Annotator Backend

The backend part of the project is a Python Flask-based web application designed for managing image annotations and serving deepzoom images generated using TIFF files. The flask web application serves the TIFF viewer on the frontend with dzi files. It uses SQLAlchemy for SQLite database to manage annotations made on TIFF files on the frontend, and serve them to the frontend when requested. This flask web app is meant to serve as a working example of what the SPARC portal backend would be serving to the SPARCTA frontend.

## Project Structure

- **`__init__.py`**: Initializes the Flask application and defines routes for handling image and annotation operations.
- **`app/database.py`**: Sets up the database connection using SQLAlchemy and initializes the database schema.
- **`app/images.py`**: Handles downloading of test dataset into static, and conversion of TIFF files in the test dataset into DZI format using Deep Zoom tools.
- **`app/models.py`**: Defines the database model `Annotation`, representing image and user ids and image associated annotations.
- **`test.db`**: A SQLite database for storing user provided image annotations. 

### Mock dataset

For the purposes of the hackathon, we use the flask app here as a mock backend, with a mock dataset from [Brookes et al. SPARC Consortium (2024)](http://dx.doi.org/10.1111/nmo.13685), identified with ID = 125 in the SPARC portal (this can be changed by modifying TEST_DATASET_ID in `app/images.py`). This dataset is downloaded when the flask app is run, if REMAKE_TEST_DATASET is set to True in `__init__.py` file. All TIFF files in the test dataset are converted to DZI. TIFFs are converted to DZI using openzoom library from DeepZoomTools and Pillow. Only 2D grayscale TIFFs or RGB/RGBA 2D TIFFs are supported, which are converted to 8-bit before conversion into dzi. Parameters for the conversion can be edited in `app/images.py`. A test TIFF file and its corresponding deepzoom (DZI) file is also provided in `/static/test_img/test_img.tif` and `/static/test_img/test_img.dzi` respectively (do not require downloading any dataset). 

### Annotation Database

Annotations are stored in SQLite database and queried using SQLAlchemy. The flask app allows for requesting annotations already stored in the database, adding new annotations to the database, removing previous annotations from the database, and updating existing annotations in the database; all using both POST and GET methods. See [database README](../database/README.md) for details on database organisation.

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

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SPARC-FAIR-Codeathon/2024-team-6.git
    cd 2024-team-6.git
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the database:**
    ```python
    from app.database import init_db
    init_db()
    ```

5. **Run the application:**
    ```bash
    python app/__init__.py
    ```

6. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000`

