import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ConvertFileView from "../views/ConvertFileView.vue";
import PickConverterView from "../views/PickConverterView.vue";

import { FileFormats} from "@/constants/file-formats";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/upload/pdf/docx",
      name: "pdf.word",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.PDF,
        fromFormatLabel: "PDF",
        toFormat: FileFormats.WORD,
        toFormatLabel: "Word",
        description: ""
      })
    },
    {
      path: "/upload/pdf/jpg",
      name: "pdf.jpg",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.PDF,
        fromFormatLabel: "PDF",
        toFormat: FileFormats.JPG,
        toFormatLabel: "JPG",
        description: ""
      })
    },
    {
      path: "/upload/pdf/png",
      name: "pdf.png",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.PDF,
        fromFormatLabel: "PDF",
        toFormat: FileFormats.PNG,
        toFormatLabel: "PNG",
        description: ""
      })
    },
    {
      path: "/upload/pdf/jpeg",
      name: "pdf.jpeg",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.PDF,
        fromFormatLabel: "PDF",
        toFormat: FileFormats.JPEG,
        toFormatLabel: "JPEG",
        description: ""
      })
    },
    {
      path: "/upload/pdf/pptx",
      name: "pdf.pptx",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.PDF,
        fromFormatLabel: "PDF",
        toFormat: FileFormats.POWER_POINT,
        toFormatLabel: "Power Point",
        description: ""
      })
    },
    {
      path: "/upload/json/csv",
      name: "json.csv",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.JSON,
        fromFormatLabel: "JSON",
        toFormat: FileFormats.CSV,
        toFormatLabel: "CSV",
        description: ""
      })
    },
    {
      path: "/upload/csv/json",
      name: "csv.json",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.CSV,
        fromFormatLabel: "CSV",
        toFormat: FileFormats.JSON,
        toFormatLabel: "JSON",
        description: ""
      })
    },
    {
      path: "/upload/xml/csv",
      name: "xml.csv",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.XML,
        fromFormatLabel: "XML",
        toFormat: FileFormats.CSV,
        toFormatLabel: "CSV",
        description: ""
      })
    },
    {
      path: "/upload/xml/json",
      name: "xml.json",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.XML,
        fromFormatLabel: "XML",
        toFormat: FileFormats.JSON,
        toFormatLabel: "JSON",
        description: ""
      })
    },
    {
      path: "/upload/json/xml",
      name: "json.xml",
      component: ConvertFileView,
      props: () => ({
        fromFormat: FileFormats.JSON,
        fromFormatLabel: "JSON",
        toFormat: FileFormats.XML,
        toFormatLabel: "XML",
        description: ""
      })
    }
  ],
});

export default router;
