const app = Vue.createApp({
    delimiters: [ '[%', '%]' ],

    data() {
        return {
            hideChangeForm: false,            
            isLoaded: false,

        }


    },

    mounted() {
        this.isLoaded = true;

    },


    methods: {
        showForm() {
            this.hideChangeForm = !this.hideChangeForm;

        }

        

    },







});

const vm = app.mount('#adminPage');
