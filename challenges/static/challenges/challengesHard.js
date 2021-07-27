const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isLoaded: false,
            progressBarHidden: true,
            progressBarPercent: 10,
            progressBarText: "Deleting...",
            progressInterval: null,
            clicked: false,
        }

    },

    mounted() {
        this.isLoaded = true;

    },

    watch: {
        progressBarPercent(val) {
             if (this.progressBarPercent >= 100) {
                 this.progressBarPercent = 100;
                 clearInterval(this.progressInterval);
             }
        },
    },


    methods: {

        startTimer() {
            this.progressInterval = setInterval(() => (this.progressBarPercent += 88), 1000);
        },

        beginDeletion() {
            this.progressBarHidden = false;
            if (this.clicked === false) { 
                this.startTimer(); 
                this.clicked = true;
            }

        },

    },


});


const vm = app.mount('#completedContainer');
