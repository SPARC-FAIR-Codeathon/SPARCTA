from pathlib import Path, PurePosixPath
from shutil import rmtree
import io
import os
import itertools

from PIL import Image
from skimage import img_as_ubyte
from skimage.io import imread

from sparc_me import Dataset_Api
import deepzoom


class New_Dataset_Api(Dataset_Api):
    """Dataset_Api modified to allow saving the dataset to any given path

    Adds new attribute root_path, which is the path at which downloaded 
    datasets is to be stored. Modifies _mkdir and _parse functions to ensure
    that paths are pointed correctly.
    """
    def __init__(self, root_path=""):
        self.root_path = Path(root_path)
        super().__init__()

    def _mkdir(self, paths):
        print(self.root_path)
        for path in paths:
            savepath = self.root_path
            fileStrList = path.split("/")
            i = len(fileStrList)
            relative_path = ""
            for r in fileStrList[0 : i - 1]:
                relative_path += r + "/"
            savepath = savepath / relative_path
            folder = os.path.exists(savepath)
            if not folder:
                os.makedirs(savepath)

    def _parse(self, html_queue):
        while True:
            res = html_queue.get()
            if res is None:
                print("finish downloading dataset!")
                break
            with io.BytesIO(res["content"]) as io_file:
                with open(self.root_path / res["filepath"], "wb") as file:
                    file.write(io_file.getvalue())


class TiffDziConvert:
    """TIFF to DZI converter

    Creates instances that can convert TIFF files into DZI files,
    using deepZoom.ImageCreator.

    All init arguments are passed to deepZoom.ImageCreator.

    Any instance takes one argument, the path to the TIFF file, as 
    input. TIFF file is rescaled to 8-bit depth before conversion to 
    DZI, since deepZoom.ImageCreator only supports png or jpeg. If 
    TIFF is 3 (4) channel, it is assumed to be RGB (RGBA).

    DZI file (with the same name as the input TIFF file) and its tiles 
    are stored in a new folder of the same name as the input TIFF file,
    in the same folder as the TIFF file.
    """
    def __init__(self, *args, **kwargs):
        self.creator = deepzoom.ImageCreator(*args, **kwargs)

    def __call__(self, source):
        source = Path(source).absolute()
        # Read tiff file, convert to RGB if multichannel
        source_img = img_as_ubyte(imread(source))
        if len(source_img.shape) == 2:
            source_img = Image.fromarray(source_img, mode="L")
        elif len(source_img.shape) == 3:
            source_img = Image.fromarray(
                source_img, mode="RGBA" if source_img.shape[-1] == 4 else "RGB"
            )
        else:
            return None  # Image cannot be converted, giving up
        # Create new folder in source folder to store the dzi file
        destination = source.parent / source.stem
        if destination.exists():
            rmtree(destination)
        destination.mkdir()
        destination = destination / f"{source.stem}.dzi"
        # Convert to dzi
        self.creator.create(source_img, destination)
        return destination


TEST_DATASET_ID = 125
"""ID for test dataset"""

STATIC_PATH = Path(__file__).absolute().parent.parent / "static"
"""Path to static folder"""

STATIC_DATASET_PATH = STATIC_PATH / "dataset"
"""Path where test dataset is stored when downloaded"""

TEST_IMG_PATH = STATIC_PATH / "test_img/test_img.dzi"
"""Path to test img, always present"""

TIFF_DZI_CONVERTER = TiffDziConvert(
    tile_size=128,
    tile_overlap=2,
    tile_format="png",
    image_quality=1,
    resize_filter="bicubic",
)
"""Default TIFF to DZI converter"""


def download_dataset(dataset_id):
    """Downloads dataset from SPARC with id as dataset_id.
    Dataset is downloaded at STATIC_DATASET_PATH. If the 
    path already exists, it is overwritten.

    :param dataset_id: ID of SPARC dataset to download
    """
    if STATIC_DATASET_PATH.exists():
        rmtree(STATIC_DATASET_PATH)
    STATIC_DATASET_PATH.mkdir()
    api_tools = New_Dataset_Api(STATIC_DATASET_PATH.absolute())
    api_tools.download_dataset(dataset_id)


def convert_tif_dzi(converter: TiffDziConvert):
    """Converts all TIFFs at dataset at STATIC_DATASET_PATH into 
    DZI, using given converter.

    :param converter: TIFF to DZI converter
    """
    tif_files = itertools.chain(
        STATIC_DATASET_PATH.rglob("*.tif"), STATIC_DATASET_PATH.rglob("*.tiff")
    )
    for tif_file in tif_files:
        converter(tif_file)


def create_test_dataset():
    """Downloads test dataset (TEST_DATASET_ID) and converts all
    TIFF files in the dataset into DZI using TIFF_DZI_CONVERTER
    """
    download_dataset(TEST_DATASET_ID)
    convert_tif_dzi(TIFF_DZI_CONVERTER)


def _get_dataset_tif_file(relative_path):
    """Returns absolute path to DZI file, given relative path from url
    to corresponding TIFF file

    :param relative_path: url relative path to TIFF file
    :return: If DZI file exists, returns the path to it. If it doesn't, 
    returns None.
    """
    if relative_path  == "test":
        return TEST_IMG_PATH
    if relative_path[0] == "/":
        relative_path = relative_path[1:]
    tif_path = STATIC_DATASET_PATH / relative_path
    dzi_file = tif_path.parent / f"{tif_path.stem}"
    dzi_file = dzi_file / f"{tif_path.stem}.dzi"
    if dzi_file.exists():
        return dzi_file
    
def get_dataset_tif_file(relative_path):
    """Returns url path to DZI file relative to STATIC_PATH.parent, given 
    relative path from url to corresponding TIFF file

    :param relative_path: url relative path to TIFF file
    :return: If DZI file exists, returns the url relative path to it. If 
    it doesn't, returns None.
    """
    dzi_file = _get_dataset_tif_file(relative_path)
    if dzi_file is not None:        
        # Relative to static
        relative_path = Path(os.path.relpath(dzi_file.parent,STATIC_PATH.parent))
        relative_path = relative_path/dzi_file.name
        return '/' + str(PurePosixPath(relative_path))
    return None
