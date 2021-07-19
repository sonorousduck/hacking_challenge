const app = Vue.createApp({

    delimiters: [ '[%', '%]' ],


    data() {
        return {
            placeholder: "Text",
            isAdmin: false,
            isAdminText: "Admin: ",
            isNotLoaded: true,
            completedChallenges: null,
            numChallenges: null,
            percentComplete: null,
        }
        


    },

    mounted() {
        if (this.$refs.admin.firstChild.data.toLowerCase() === 'false') {
            this.isAdmin = false;
            this.isAdminText = "User";
        } else {
            this.isAdmin = true;
            this.isAdminText = "Admin";
        }
        this.isNotLoaded = false;

        this.completedChallenges = this.$refs.completedChallenges.firstChild.data;
        this.numChallenges = this.$refs.numChallenges.firstChild.data;
        this.percentComplete = '' + ((this.completedChallenges / this.numChallenges) * 100).toFixed(2) + '%';

    },


});


const vm = app.mount('#homepage');



