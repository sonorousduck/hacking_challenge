const app = Vue.createApp({

    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isInvisible: true,
            passwordIsInvisible: true,
            isLoaded: false,
        }
    },

    mounted() {
        this.isLoaded = true;   

    },

    methods: {
        changeText() {
            this.isInvisible = !this.isInvisible;
        },

        changePassword() {
            this.passwordIsInvisible = !this.passwordIsInvisible;
        },


    }




});

const vm = app.mount('#changePopup')
