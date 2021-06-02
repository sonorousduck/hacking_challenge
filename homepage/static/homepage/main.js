const app = Vue.createApp({

    delimiters: [ '[%', '%]' ],


    data() {
        return {
            placeholder: "Text",
            isAdmin: null,
            isAdminText: "Admin: ",
        }
        


    },

    mounted() {
        this.isAdmin = this.$refs.isAdmin.firstChild.data.toLowerCase();

        console.log(this.isAdmin);
    },






});


const vm = app.mount('#homepage');



