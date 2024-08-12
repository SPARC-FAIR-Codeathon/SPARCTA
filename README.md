# SPARCTA : SPARC Tiff Annotator

<p align="center">
  <img src="assets/img/SPARCta logo header.png" alt="SPARCTA Header"/>
</p>

## Introduction

## Problem Definition

- In the current version of SPARC Portal Users are unable to view TIFF images directly in the browser; they must download them first. This can be inconvenient, especially when users might want a quick look at the image without needing to download it.
- Please mention about BioLucida Viewer and its limitation (Please help research)
- Please highlight on the annotation limitation
- Please highlight on the importance collaboration (Other people from the same group if they're given an access they can see the annotated tiff files to, allowing collaboration)

## Solution

(Please rephrase in a way that we're offering them a solution) SPARCTA will allow the user to perform the following task:

- **Preview**: Users can preview TIFF image without having to download it first
- **Annotation**: Users can annotate microscopy images and save their annotations.
- **Comments**: Users can leave comments directly on the image.
- **Full Screen Mode**: Users can go into full screen mode and this allows for detailed examination by expanding the image to full screen.
- **Zoom and Pan**: Users can zoom in, zoom out, pan across the image, crop it, and save the final result.
- **Image Adjustments**: Users can adjust the brightness, saturation, and other settings of the image.

## Impact

Currently, images within the SPARC Portal are not capable of being annotated by users. However, with the implementation of SPARCTA, users will be able to annotate images directly in the portal without requiring the download of large image files or the use of customized software. This feature will also enable users to share their thoughts and highlight relevant sections of the images, fostering a collaborative community driven by shared knowledge and understanding.

## Architecture

## Using SPARCTA

To experience the current capabilities of the SPARCATA prototype, simply download and run it on your local machine. To do this, follow these setup instructions:

- Launch a Flask server on port 5000
- Run a React server

For detailed guidance on this process, please consult the README files within our frontend and backend directories.

Once you have successfully set up SPARCATA, you can begin testing its features by following these steps:

1. Access the locally installed SPARC Portal to select an image in your web browser.
2. Choose a TIFF image for annotation purposes.
3. Select SPARCATA as your chosen annotation tool.
4. Create one or more annotations within the selected image.
5. Save your annotated work to preserve it for future reference.
6. When you relaunch SPARCATA, your previously created annotations should be visible and ready to use.

## FAIR Practices

The SPARC codeathon focuses on ensuring that our code and data are FAIR, and we're extending this commitment to our development process. We've evaluated SPARCTA against the FAIR Principles for research software and will provide further details in a separate document.

## Future Directions

We will be working on the following features in SPARCTA:

- Allowing users to control annotation visibility, either keeping them private, making them publicly accessible, or sharing them selectively with other users.
- Expert curation in SPARC Portal, where annotations can be accepted or rejected by qualified reviewers.
- Leveraging curated data to train machine learning models and empowering all users to utilize this capability for annotating and exploring new images.

## Reporting Issues

- If you encounter an issue with SPARCTA, kindly report it by creating a new issue in our GitHub repository.
- We also encourage you to share your solution by submitting a pull request if you've managed to resolve the problem yourself.

## Team Members:

- Haries (Lead, Frontend)
- Archit (Backend)
- Sruthi (Documentation, Backend-support)
- Akram (Database)
- Anmol (Database)
