const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isDoneLoading: true,
            locked: true,
            loaded: false,


        }

    },

    created() {


    },

    mounted() {
        this.loaded = true;

    },


    methods: {

    },


});


const vm = app.mount('#challengeBar');
