const app = Vue.createApp({
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isInvisible: true,
        }

    },




    methods: {
        getHints() {
            this.isVisible = !this.isVisible;
        },


    },


});

const vm = app.mount('#formAndHints');

