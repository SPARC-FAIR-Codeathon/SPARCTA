<template>
    <div class="container">
        <div id="toolbar" class="toolbar">
            <div 
                v-for="tool in tools" 
                :key="tool.name" 
                @click="tool.action" 
                :title="tool.title" 
                class="toolbar-item"
            >
                <img :src="tool.icon" class="toolbar-icon" />
            </div>
            <input type="file" ref="fileInput" @change="uploadAnnotations" style="display: none;" />
        </div>
        <div id="openseadragon" ref="viewer"></div>

        <div v-if="showModal" class="modal">
            <div class="modal-content">
                <span class="close" @click="closeModal">&times;</span>
                <p>Welcome to SPARCTA! To start annotating, select the annotation type and hold press SHIFT <br/><br/> <span style="font-size: 10px;">(Not the most ideal way but it works for now, we'll implement something easily in the future because of the time constraint).</span></p>
            </div>
        </div>

    </div>
    <div class="annotations-container">
        <p class="annotations-title">Annotation History</p>
        <div id="annotations" ref="annotations" class="annotations-list"></div>
    </div>
</template>

<script>
import OpenSeadragon from 'openseadragon';
import Annotorious from '@recogito/annotorious-openseadragon';
import '@recogito/annotorious-openseadragon/dist/annotorious.min.css';
import SelectorPack from '@recogito/annotorious-selector-pack';
import '@recogito/annotorious-toolbar/';
import '@recogito/annotorious-shape-labels';

export default {
    name: 'SparctViewer',
    props: {
        imageUrl: {
            type: String,
            required: true
        },
        imageType: {
            type: String,
            default: 'png'
        }
    },
    data() {
        return {
            viewer: null,
            anno: null,
            showModal: true,
            tools: [
                { name: 'zoomIn', title: 'Zoom in', icon: '/icon/zoom-in.png', action: this.zoomIn },
                { name: 'zoomOut', title: 'Zoom out', icon: '/icon/zoom-out.png', action: this.zoomOut },
                { name: 'toggleFullScreen', title: 'Toggle fullscreen', icon: '/icon/fullscreen.png', action: this.toggleFullScreen },
                { name: 'downloadAnnotations', title: 'Download annotations', icon: '/icon/downloads.png', action: this.downloadAnnotations },
                { name: 'uploadAnnotations', title: 'Upload annotations', icon: '/icon/upload.png', action: this.triggerFileInput },
                { name: 'rect', title: 'Annotate in rectangle', icon: '/icon/rect.png', action: () => this.setDrawingTool('rect') },
                { name: 'ellipse', title: 'Annotate in ellipse', icon: '/icon/ellipse.png', action: () => this.setDrawingTool('ellipse') },
                { name: 'polygon', title: 'Annotate in polygon', icon: '/icon/polygon.png', action: () => this.setDrawingTool('polygon') },
                { name: 'freehand', title: 'Annotate in freehand', icon: '/icon/freehand.png', action: () => this.setDrawingTool('freehand') },
                { name: 'deleteAllAnnotations', title: 'Delete all annotations', icon: '/icon/remove_all.png', action: this.deleteAllAnnotations }
            ]
        };
    },
    mounted() {
        this.initializeViewer();
    },
    methods: {
        initializeViewer() {
            this.viewer = OpenSeadragon({
                element: this.$refs.viewer,
                prefixUrl: 'https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/images/',
                tileSources: {
                    type: this.imageType == 'dzi' ? 'dzi' : 'image',
                    url: this.imageUrl
                },
                gestureSettingsTouch: {
                    pinchRotate: true
                },
                showNavigationControl: false
            });

            this.anno = Annotorious(this.viewer, {
                locale: 'auto',
                allowEmpty: true,
                widgets: ['COMMENT', 'TAG']
            });

            SelectorPack(this.anno);

            this.anno.on('createAnnotation', (annotation) => {
                console.log('Annotation created:', annotation);
                const annotationsElement = this.$refs.annotations;
                const newAnnotationElement = document.createElement('p');
                newAnnotationElement.innerHTML = `- <span style="color: #8300BF;"><b>SPARC Admin</b></span> added new annotation <b>${annotation.body[0].value}</b>`;
                annotationsElement.appendChild(newAnnotationElement);
            });
        },
        zoomIn() {
            if (this.viewer) {
                this.viewer.viewport.zoomBy(1.2);
                this.viewer.viewport.applyConstraints();
            }
        },
        zoomOut() {
            if (this.viewer) {
                this.viewer.viewport.zoomBy(0.8);
                this.viewer.viewport.applyConstraints();
            }
        },
        toggleFullScreen() {
            if (!document.fullscreenElement) {
                this.$refs.viewer.requestFullscreen();
            } else {
                document.exitFullscreen();
            }
        },
        setDrawingTool(shape) {
            this.anno.setDrawingTool(shape);
        },
        downloadAnnotations() {
            const annotations = this.anno.getAnnotations();
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(annotations));
            const downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", "annotations.json");
            document.body.appendChild(downloadAnchorNode);
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        },
        triggerFileInput() {
            this.$refs.fileInput.click();
        },
        uploadAnnotations(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const annotations = JSON.parse(e.target.result);
                    annotations.forEach(annotation => {
                        this.anno.addAnnotation(annotation);
                        const annotationsElement = this.$refs.annotations;
                        const newAnnotationElement = document.createElement('p');
                        newAnnotationElement.innerHTML = `- <span style="color: #8300BF;"><b>SPARC Admin</b></span> uploaded new annotation <b>${annotation.body[0].value}</b>`;
                        annotationsElement.appendChild(newAnnotationElement);
                    });
                };
                reader.readAsText(file);
            }
        },
        deleteAllAnnotations() {
            this.anno.clearAnnotations();
        },
        closeModal() {
            this.showModal = false;
        }
    }
};
</script>

<style scoped>
.container {
    display: flex;
}

#openseadragon {
    width: 100%;
    height: 600px;
    position: relative;
    border-radius: 10px;
    border: 1px solid #ccc;
}

.toolbar {
    display: flex;
    flex-direction: column;
    margin-right: 10px;
    margin-top: 10px;
}

.toolbar-item {
    cursor: pointer;
    margin-bottom: 5px;
}

.toolbar-icon {
    border: solid 1px #ccc;
    border-radius: 10px;
    padding: 5px;
    width: 25px;
}

.annotations-container {
    padding: 0 45px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.annotations-title {
    color: #24245B;
    font-weight: bold;
}

.annotations-list > p {
    margin: 0;
    padding: 0;
}

.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 500px;
    border-radius: 10px;
    text-align: center;
    position: relative;
}

.close {
    color: #aaa;
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
}

:global(svg.a9s-annotationlayer .a9s-selection-mask) {
    fill: rgba(0, 0, 0, 0.7);
}

:global(svg.a9s-annotationlayer .a9s-selection .a9s-inner, svg.a9s-annotationlayer .a9s-annotation .a9s-inner) {
    stroke-width: 4;
    stroke: #8300BF;
}

:global(svg.a9s-annotationlayer .a9s-handle .a9s-handle-inner) {
    stroke-width: 2;
    fill: #FFB100;
    stroke: #8300BF;
}
</style>
