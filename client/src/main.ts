import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import 'primevue/resources/themes/vela-purple/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import "primeflex/primeflex.css";

//#region PrimeVue imports
import PrimeVue from 'primevue/config';
import Menubar from 'primevue/menubar';
import InputText from 'primevue/inputtext';
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import ProgressBar from 'primevue/progressbar';
import Badge from 'primevue/badge';
import Toast from 'primevue/toast';
//#endregion

const app = createApp(App);

app.use(createPinia());
app.use(PrimeVue);
app.use(router);

//#region PrimeVue components
app.component('MenuBar', Menubar);
app.component('InputText', InputText);
app.component('FileUpload', FileUpload);
app.component('Button', Button);
app.component('Badge', Badge);
app.component('ProgressBar', ProgressBar);
app.component('Toast', Toast);
//#endregion
app.mount("#app");
