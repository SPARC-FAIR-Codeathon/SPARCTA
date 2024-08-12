# SPARCTA : SPARC Tiff Annotator

<p align="center">
  <img src="assets/img/SPARCta logo header.png" alt="SPARCTA Header"/>
</p>

# Table of Contents

1.  [Introduction](#introduction)
2.  [Problem Definition](#problem-definition)
3.  [Solution](#solution)
4.  [Impact](#impact)
5.  [Architecture](#architecture)
6.  [Using SPARCTA](#using-sparcta)
7.  [FAIR Practices](#fair-practices)
8.  [Future Directions](#future-directions)
9.  [Reporting Issues](#reporting-issues)
10. [Team Members:](#team-members:)


## Introduction

Imagine this: you're exploring the fascinating datasets on the [SPARC portal](https://sparc.science) when you stumble upon a dataset containing some intriguing microscopy images. Curious, you click on the dataset, hoping to quickly browse through some of these images. However, there's a catch: the images are stored in TIFF format, and SPARC doesn’t offer a web-based viewer for these files. But don’t worry: **SPARCTA** is here to save the day!

SPARCTA (SPARC Tiff Annotator) is a web-based viewer for TIFF files that allows users on the SPARC portal to both view and create custom annotations for the TIFF files in SPARC datasets, developed by the Sparctans (Team #6) during the SPARC 2024 Codeathlon. Check out the [Team section](#team-members) for more information on our Team.

## Current State

At present, SPARC portal does not support vieweing TIFF images in their browser, requiring its users to download such files in order to view them. This can be inconvenient, especially when users might want a quick look at the image without needing to download it. The SPARC portal currently uses [BioLucida](https://www.biolucida.net/login) to render image files in browser, but it is currently not available for viewing TIFF images on the SPARC portal. Moreover, BioLucida's web viewer does not allow custom annotations to be made by users who are viewing the image in the web browser, further limiting the ability of the user to explore TIFF images in SPARC datasets.

## SPARCTA: The Tiff Viewer for SPARC Portal

In order to tackle these issues, we have developed a web-based viewer for TIFF files with annotation capabilities, called SPARCTA. SPARCTA has the following components and features:
- **TIFF**:
  - Users can freely *preview* TIFF files on the SPARC portal without having to download them.
  - Users can also *zoom* in or out and *pan* across the image, for examining specific features in different parts of the image.
  - SPARCTA also supports a *Full Screen* mode, allowing for detailed examination of the all features presented in the image by the users in one go.
- **Annotations**:
  - Users can create *custom annotations* on top of the image in order to highlight features in the image, tagged by their user name/id.
  - SPARCTA supports *annotations by multiple users* at once, allowing for enhanced collaboration between different users of the SPARC portal.
  - Users can also *save* their annotations for later use in a human-readable format.

SPARCTA directly enhances the FAIRness of TIFF images hosted on the SPARC portal, by:
- *F*indable: Better exploration of TIFF images on the SPARC portal.
- *A*ccessibility: No need to download TIFF images in order to access them, bringing TIFF images at par with other files such as JPEG images on the SPARC portal.
- *I*nteroperability: SPARCTA stores annotations as json, which can read and interpreted by various other softwares.
- *R*eusability: With custom annotations, SPARCTA allows reusing the same TIFF images by multiple users for exploring many different questions on the same dataset.

## Impact

Currently, images within the SPARC Portal are not capable of being annotated by users. However, with the implementation of SPARCTA, users will be able to annotate images directly in the portal without requiring the download of large image files or the use of customized software. This feature will also enable users to share their thoughts and highlight relevant sections of the images, fostering a collaborative community driven by shared knowledge and understanding.

## Architecture

SPARCTA is essentially built of three components:
- **Frontend**: The frontend for SPARCTA is forked from 

## Using SPARCTA

To experience the current capabilities of the SPARCTA prototype, simply download and run it on your local machine. To do this, follow these setup instructions:

- Launch a Flask server on port 5000 (see ./backend/README.md)
- Run a React server (see ./frontend/README.md)

For detailed guidance on this process, please consult the README files within our frontend and backend directories.

Once you have successfully set up SPARCTA, you can begin testing its features by following these steps:

1. Access the locally installed SPARC Portal to select an image in your web browser.
2. Choose a TIFF image for annotation purposes.
3. Select SPARCTA as your chosen annotation tool.
4. Create one or more annotations within the selected image.
5. Save your annotated work to preserve it for future reference.
6. When you relaunch SPARCTA, your previously created annotations should be visible and ready to use.

## Future Directions

We will be working on the following features in SPARCTA:

- Allowing users to control annotation visibility, either keeping them private, making them publicly accessible, or sharing them selectively with other users.
- Expert curation in SPARC Portal, where annotations can be accepted or rejected by qualified reviewers.
- Leveraging curated data to train machine learning models and empowering all users to utilize this capability for annotating and exploring new images.

## Reporting Issues

- If you encounter an issue with SPARCTA, kindly report it by creating a new issue in our GitHub repository.
- We also encourage you to share your solution by submitting a pull request if you've managed to resolve the problem yourself.

## Team Members

- [Haries](https://github.com/hariesramdhani) (Lead, Frontend)
- [Archit](https://github.com/bhatnagararchit) (Backend)
- [Sruthi]() (Documentation, Backend-support)
- [Akram](https://github.com/akram0618) (Database)
- [Anmol](https://github.com/codemeleon) (Database)
