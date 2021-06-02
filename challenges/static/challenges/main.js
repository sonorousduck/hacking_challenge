const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            someText: "This is a test",
            challengesFromDatabase: null,
            databaseChallengesLocation: 'getChallenges',
            isLocked: false,
            navigation: 'navigateToChallenge',

        }

    },

    created() {


    },


    methods: {

        goToChallenge(event) {
            fetch(this.navigation, {challenge: 'event.currentTarget.id'})



        },


    },


});


const vm = app.mount('#challenges');
