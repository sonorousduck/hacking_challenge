const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isLoaded: false,
            progressBarHidden: true,
            progressBarPercent: 0,
            progressBarText: "Deleting...",
            progressInterval: null,
            clicked: false,
            disabled: false,
            csrf_token: null,
        }

    },

    mounted() {
        this.isLoaded = true;
        this.csrf_token = this.get_token();
    },

    watch: {
        progressBarPercent(val) {
             if (this.progressBarPercent >= 100) {
                 this.progressBarPercent = 100;
                 this.updateDatabase();
                 clearInterval(this.progressInterval);
 

                 setInterval(function() {window.location.replace('https://www.youtube.com/watch?v=dQw4w9WgXcQ')}, 3500);
             }
        },
    },


    methods: {
        
        get_token() {
            if (!document.cookie) {
                return null;
            }

            const xsrfCookies = document.cookie.split(';')
                .map(c => c.trim())
                .filter(c => c.startsWith('csrftoken='));

            if (xsrfCookies.length === 0) {
                return null;
            }
            return xsrfCookies[0].split('=')[1];
        },


        updateDatabase() {
            const requestOptions = {
                method: "POST",
                headers: {'Content-Type': 'application/json', 'Config': 'True', 'X-CSRFToken': this.get_token(),},
                
            };

            fetch('deleteServer/', requestOptions)
                .then(response => response.json())
                .then(json => {
                });

        },
        


        startTimer() {
            this.progressInterval = setInterval(() => (this.progressBarPercent += 1), 45);
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
