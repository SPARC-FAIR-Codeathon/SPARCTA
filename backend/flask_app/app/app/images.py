from pathlib import Path
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

STATIC_PATH = Path(__file__).absolute().parent.parent / "static"

STATIC_DATASET_PATH = STATIC_PATH / "dataset"

TEST_IMG_PATH = STATIC_PATH / "test_img/test_img.dzi"

TIFF_DZI_CONVERTER = TiffDziConvert(
    tile_size=128,
    tile_overlap=2,
    tile_format="png",
    image_quality=1,
    resize_filter="bicubic",
)


def download_dataset(dataset_id):
    if STATIC_DATASET_PATH.exists():
        rmtree(STATIC_DATASET_PATH)
    STATIC_DATASET_PATH.mkdir()
    api_tools = New_Dataset_Api(STATIC_DATASET_PATH.absolute())
    api_tools.download_dataset(dataset_id)


def convert_tif_dzi(converter: TiffDziConvert):
    tif_files = itertools.chain(
        STATIC_DATASET_PATH.rglob("*.tif"), STATIC_DATASET_PATH.rglob("*.tiff")
    )
    for tif_file in tif_files:
        converter(tif_file)


def create_test_dataset():
    download_dataset(TEST_DATASET_ID)
    convert_tif_dzi(TIFF_DZI_CONVERTER)


def get_dataset_tif_file(relative_path):
    if relative_path  == "test":
        return TEST_IMG_PATH
    if relative_path[0] == "/":
        relative_path = relative_path[1:]
    tif_path = STATIC_DATASET_PATH / relative_path
    dzi_file = tif_path.parent / f"{tif_path.stem}"
    dzi_file = dzi_file / f"{tif_path.stem}.dzi"
    if dzi_file.exists():
        return dzi_file
    return None
