<template>
  <div id="header">
    <div id="navbar">
      <div
        style="
          display: flex;
          align-items: center;
          justify-content: flex-end;
          padding: 12px;
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="white"
          height="16"
          width="16"
          viewBox="0 0 24 24"
          class="nuxt-icon nuxt-icon--fill tab3 mr-4 mt-4"
          data-v-e840d740=""
        >
          <path
            d="M19 5.6v7.219h-4.181V16.1l-3.889-3.282H5V5.6zm2-2H3v11.218h7.2l3.331 2.81 3.288 2.772v-5.582H21z"
          ></path>
        </svg>
        <p style="font-size: 14px; margin-left: 2px">Contact Us</p>
      </div>
      <div
        style="
          display: flex;
          align-items: center;
          justify-content: flex-end;
          padding: 12px;
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="white"
          height="16"
          width="16"
          viewBox="0 0 24 24"
          class="nuxt-icon nuxt-icon--fill tab3 mr-4 mt-4"
          data-v-e840d740=""
        >
          <circle cx="12" cy="15.824" r=".753"></circle>
          <path
            d="M12 14.256a.75.75 0 0 1-.75-.75v-1c0-.529.419-.818.862-1.124.623-.43 1.138-.83 1.138-1.376A1.21 1.21 0 0 0 12 8.756a1.25 1.25 0 0 0-1.25 1.25.75.75 0 0 1-1.5 0A2.753 2.753 0 0 1 12 7.256a2.72 2.72 0 0 1 2.75 2.75 3.3 3.3 0 0 1-1.786 2.61c-.079.055-.152.1-.214.147v.743a.75.75 0 0 1-.75.75"
          ></path>
          <path
            d="M12 5a7 7 0 1 1-7 7 7.01 7.01 0 0 1 7-7m0-2a9 9 0 1 0 9 9 9 9 0 0 0-9-9"
          ></path>
        </svg>
        <p style="font-size: 14px; margin-left: 2px">Help</p>
      </div>
      <div
        style="
          display: flex;
          align-items: center;
          justify-content: flex-end;
          padding: 12px;
        "
      >
        <svg
          data-v-e840d740=""
          fill="white"
          height="16"
          width="16"
          xmlns="http://www.w3.org/2000/svg"
          xml:space="preserve"
          viewBox="0 0 24 24"
          class="nuxt-icon nuxt-icon--fill tab3 mt-4"
        >
          <path
            d="M8 10c2.8 0 5-2.2 5-5s-2.2-5-5-5-5 2.2-5 5 2.2 5 5 5m0-8c1.7 0 3 1.3 3 3S9.7 8 8 8 5 6.7 5 5s1.3-3 3-3m7.9 16.9c-.5-3.5-3.3-6.3-6.8-6.8-2.1-.3-4.2.2-5.9 1.5S.4 16.7.1 18.9c-.1.5.3 1 .8 1.1H1c.5 0 .9-.4 1-.9.5-3.3 3.5-5.5 6.8-5.1 2.2.3 4.1 1.9 4.8 3.9H5c-.6 0-1 .4-1 1s.4 1 1 1h11.1z"
          ></path>
        </svg>
        <p style="font-size: 14px; margin-left: 2px">SPARC Admin</p>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="white"
          height="12"
          width="12"
          viewBox="0 0 1024 1024"
        >
          <path
            fill="currentColor"
            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z"
          ></path>
        </svg>
      </div>
    </div>
    <div id="menu">
      <img
        src="/icon/sparc.svg"
        alt="SPARC Logo"
        height="60"
        style="margin-right: 10px"
      />
      <p>Data & Models</p>
      <p>SPARC Apps</p>
      <p>Tools & Resources</p>
      <p>News & Events</p>
      <p>About</p>
      <p>Submit to SPARC</p>
    </div>
    <div id="path">
      <p style="font-size: 14px">
        Home > Data & Models > Characterization of projections of longitudinal
        muscle motor neurons in human colon > File >
        SPARC_H2104B_LM_X0.519Y-2.246_ChAT.tif
      </p>
    </div>
  </div>
  <div
    style="margin: 10px 80px; display; flex: flex; flex-direction: column; justify-content: start; align-items: start; "
  >
    <div
      id="tab"
      style="
        padding: 0 5px;
        border: solid #8300bf;
        border-width: 1px 1px 0.125em;
        color: #8300bf;
        font-weight: 500;
        background-color: #f9f2fc;
        width: 100px;
        display: flex;
        flex-direction: row;
        align-items: center;
      "
    >
      <img width="30" height="30" src="/sparc.png" />
      <p style="text-align: left; padding: 0 5px">SPARCTA</p>
    </div>
    <div style="border: 1px solid #dcdfe6; padding: 10px">
      <SparctaViewer imageUrl="/test.dzi" imageType="dzi" />
    </div>
  </div>
  <div
    id="footer"
    style="display: flex; flex-direction: row; justify-content: flex-start"
  >
    <div
      style="
        width: 70%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        margin: 50px 50px;
      "
    >
      <img
        src="/icon/sparc.svg"
        alt="SPARC Logo"
        height="60"
        style="margin-right: 10px"
      />
      <p style="margin: 10 0px; padding: 0; text-align: left">
        The open community platform for bridging the body and the brain through
        neuroscience and systems physiology data, computational and spatial
        modeling, and device design.
      </p>
    </div>
  </div>
</template>

<script>
import SparctaViewer from "./components/SparctaViewer.vue";

export default {
  name: "App",
  components: {
    SparctaViewer,
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: "Asap", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

#menu {
  background-color: white;
  height: 100px;
  display: flex;
  align-items: center; /* Vertically align items */
  justify-content: flex-start; /* Horizontally align items to the right */
  padding: 2px 30px;
  gap: 50px; /* Horizontal gap between children */
  color: #24245b;
  font-weight: 500;
}

#path {
  background-color: #e4e7ed;
  height: 30px;
  display: flex;
  align-items: center; /* Vertically align items */
  justify-content: flex-start; /* Horizontally align items to the right */
  padding: 2px 30px;
  color: #24245b;
}

#navbar {
  background-color: #24245b;
  height: 40px;
  display: flex;
  align-items: center; /* Vertically align items */
  justify-content: flex-end; /* Horizontally align items to the right */
}

#footer {
  background-color: #f8faff;
  height: 200px;
}

#header {
  color: white;
}
</style>
