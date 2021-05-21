const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            someText: "This is a test",
            challengesFromDatabase: null,
            databaseChallengesLocation: 'getChallenges/'

        }

    },

    created() {
        this.challengesFromDatabase = this.getChallenges();


    },


    methods: {
        getChallenges() {
            fetch(this.databaseChallengesLocation)
                .then(response => response.json())
                .then(json => {
                    this.challengesFromDatabase = json;
                });
        },

    },


});


const vm = app.mount('#challenges');
