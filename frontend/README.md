# Frontend

The frontend component simulates how SPARCTA will be integrated into the SPARC Portal ecosystem. It includes two primary Vue components: `App.vue` and `SparctaViewer.vue`.

- **`App.vue`**: This is the main component that emulates the user interface of the SPARC Portal. It provides a foundational layout and styling similar to what will be seen in the actual SPARC Portal, ensuring consistency and a smooth integration process.

- **`SparctaViewer.vue`**: This component serves as the TIFF file viewer and annotation tool within the simulation. It is designed to handle the viewing and interaction with TIFF files through the use of OpenSeadragon and Annotorious:
  - **OpenSeadragon**: Employed for displaying Deepzoom images, allowing for efficient and interactive zooming and panning of large TIFF files.
  - **Annotorious**: Utilized for adding and managing annotations on the images. It integrates various plugins to support different types of annotations and annotation tools.

The `SparctaViewer.vue` component is divided into two main sections:
- **The Viewer Container**: This area contains the toolbars and the main canvas where TIFF images are displayed and interacted with.
- **The Annotation Container**: This section maintains the annotation history and provides functionality for managing and reviewing annotations.

As the SPARC Portal is built on Vue, integrating SPARCTA later on should be straightforward due to its compatibility with the Vue ecosystem.

To see how SPARCTA operates and to test its functionalities, you can run the following commands:

```
yarn install
yarn dev
```

These commands will install the necessary dependencies and start the development server, allowing you to interact with the simulated SPARCTA environment.