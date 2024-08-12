# SPARCTA : SPARC Tiff Annotator

<p align="center">
  <img src="assets/img/SPARCta logo header.png" alt="SPARCTA Header"/>
</p>

# Table of Contents

1.  [Introduction](#introduction)
2.  [Current State](#current-state)
3.  [Our Solution](#our-solution)
4.  [Impact](#impact)
5.  [Architecture](#architecture)
6.  [Using SPARCTA](#using-sparcta)
7.  [Future Directions](#future-directions)
8.  [Reporting Issues](#reporting-issues)
9.  [Team Members](#team-members)


## Introduction

Imagine this: you're exploring the fascinating datasets on the [SPARC portal](https://sparc.science) when you stumble upon a dataset containing some intriguing microscopy images. Curious, you click on the dataset, hoping to quickly browse through some of these images. However, there's a catch: the images are stored in TIFF format, and SPARC doesn’t offer a web-based viewer for these files. But don’t worry: **SPARCTA** is here to save the day!

SPARCTA (SPARC Tiff Annotator) is a web-based viewer for TIFF files that allows users on the SPARC portal to both view and create custom annotations for the TIFF files in SPARC datasets, developed by the Sparctans (Team #6) during the SPARC 2024 Codeathlon. Check out the [Team section](#team-members) for more information on our Team.

## Current State

At present, SPARC portal does not support vieweing TIFF images in their browser, requiring its users to download such files in order to view them. This can be inconvenient, especially when users might want a quick look at the image without needing to download it. The SPARC portal currently uses [BioLucida](https://www.biolucida.net/login) to render image files in browser, but it is currently not available for viewing TIFF images on the SPARC portal. Moreover, BioLucida's web viewer does not allow custom annotations to be made by users who are viewing the image in the web browser, further limiting the ability of the user to explore TIFF images in SPARC datasets.

## Our Solution

In order to tackle these issues, we have developed a web-based viewer for TIFF files with annotation capabilities, called SPARCTA. SPARCTA has the following components and features:
- **TIFF viewer**:
  - Users can freely *preview* TIFF files on the SPARC portal without having to download them.
  - Users can also *zoom* in or out and *pan* across the image, for examining specific features in different parts of the image.
  - SPARCTA also supports a *Full Screen* mode, allowing for detailed examination of the all features presented in the image by the users in one go.
- **Annotations**:
  - Users can create *custom annotations* on top of the image in order to highlight features in the image, tagged by their user name/id.
  - SPARCTA supports *annotation history*, showing the users their previous annotations made in each session.
  - SPARCTA supports *annotations by multiple users* at once, allowing for enhanced collaboration between different users of the SPARC portal.
  - Users can also *save* their annotations for later use in a human-readable format.

SPARCTA directly enhances the FAIRness of TIFF images hosted on the SPARC portal:
- *F*indable: Better exploration of TIFF images on the SPARC portal.
- *A*ccessibility: No need to download TIFF images in order to access them, bringing TIFF images at par with other files such as JPEG images on the SPARC portal.
- *I*nteroperability: SPARCTA stores annotations as json, which can read and interpreted by various other softwares.
- *R*eusability: With custom annotations, SPARCTA allows reusing the same TIFF images by multiple users for exploring many different questions on the same dataset.

## Impact

Currently, images within the SPARC Portal are not capable of being annotated by users. However, with the implementation of SPARCTA, users will be able to annotate images directly in the portal without requiring the download of large image files or the use of customized software. This feature will also enable users to share their thoughts and highlight relevant sections of the images, fostering a collaborative community driven by shared knowledge and understanding.

## Architecture

SPARCTA is essentially built of three components:
- **Frontend**: The frontend for SPARCTA is forked from [SPARC Portal App](https://github.com/nih-sparc/sparc-app-2), with new functionality implemented for viewing TIFF files. In particular, the TIFF files are viewed as Deepzoom images using [OpenSeadragon](https://openseadragon.github.io/docs/) with annotations created using [Annotorious](https://github.com/annotorious/annotorious-openseadragon) plugin for OpenSeadragon. See [frontend README](./frontend/README.md) for details.
- **Database**: Annotations are stored by SPARTCA in a sqlite database. See [database README](./database/README.md) for details.
- **Backend**: For demonstration purposes, the backend for SPARCTA is currently provided by a flask application with both serves the Deepzoom images created from TIFF files to the frontend and stores the annotations received from the frontend in the database. See [backend README](./backend/README.md) for details.

## Using SPARCTA

To experience the current capabilities of the SPARCTA prototype, simply download and run it on your local machine. To do this, follow these setup instructions:

- Launch a Flask server on port 5000 (see [backend README](./backend/README.md))
- Run a React server (see [frontend README](./frontend/README.md))

For detailed guidance on this process, please consult the README files within our frontend and backend directories.

Once you have successfully set up SPARCTA, you can begin testing its features by following these steps:

1. Access the locally installed SPARC Portal to select an image in your web browser.
2. Choose a TIFF image for annotation purposes.
3. Select SPARCTA as your chosen annotation tool.
4. Create one or more annotations within the selected image.
5. Save your annotated work to preserve it for future reference.
6. When you relaunch SPARCTA, your previously created annotations should be visible and ready to use.

## Future Directions

In the future, we will be working towards the following features/removing the following limitations in SPARCTA:
- **Support for multi-dim TIFF**: Currently only 2D grayscale or RGB/RGBA TIFF images are supported, with no support for multi-channel, multi-slice or time-series TIFF images. In the future, we will work towards supporting such images, both the backend for rendering them on the viewer and on the frontend to allow users to explore multi-dimensional TIFF images.
- **Dynamic deepzoom image generation**: Currently, we pre-create the deepzoom copies of each TIFF image, leading to more memory usage. We plan to implement dynamic generation of individual tiles of deepzoom images to alleviate this limitation.
- **Annotation access controls**: Allowing users to control annotation visibility, either keeping them private, making them publicly accessible, or sharing them selectively with other users.
- **Annotation curation**: Allow expert curation of user-/ai-generated annotations in SPARC Portal, where annotations can be accepted or rejected by qualified reviewers.
- **AI-powered Annotation**: Leveraging curated data to train machine learning models and empowering all users to utilize this capability for annotating and exploring new images.

## Reporting Issues

- If you encounter an issue with SPARCTA, kindly report it by creating a new issue in our GitHub repository.
- We also encourage you to share your solution by submitting a pull request if you've managed to resolve the problem yourself.

## Team Members

- [Haries](https://github.com/hariesramdhani) (Lead, Frontend)
- [Archit](https://github.com/bhatnagararchit) (Backend, Documentation)
- [Akram](https://github.com/akram0618) (Database, Backend)
- [Anmol](https://github.com/codemeleon) (Database, Documentation)
