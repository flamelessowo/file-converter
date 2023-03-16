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
      path: "/upload/pdf/word",
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

  ],
});

export default router;
