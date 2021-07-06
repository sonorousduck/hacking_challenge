const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            testString: "testing",

        }

    },

    created() {


    },


    methods: {

    },


});


const vm = app.mount('#mainContainer');
