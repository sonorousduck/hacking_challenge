const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isDoneLoading: true,
            unlocked: false,


        }

    },

    created() {


    },


    methods: {

    },


});


const vm = app.mount('#challengeBar');
