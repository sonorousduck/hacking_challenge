const app = Vue.createApp({
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isInvisible: true,
            validation: '../validation/',
            correct: false,
            passcodeInput: '',
            isIncorrectHidden: true,
            isCorrectHidden: true,
            isLoaded: null,
            isAssignmentClosed: false,
            isAssignmentClosedHidden: true,
            locked: null,
        }


    },

    mounted() {
        this.isLoaded = true;
        if (document.querySelector('#backend').textContent === 'true') {
            this.locked = false;
        } else {
            this.locked = true;
        }
    },


    methods: {
        getHints() {
            this.isInvisible = !this.isInvisible;
        },

        validateInput() {
            let formData = new FormData();
            formData.append("passcode", this.passcodeInput);
            formData.append("challenge_id", document.querySelector('#challenge_id').value);

            fetch(this.validation, {
                method: "POST",

                body: formData,

                headers: {'X-CSRFToken': document.querySelector('#csrf_token').value},

            })
                .then(response => response.json())
                .then(json => {
                    if (json[0]['success'] === "Assignment is closed") {
                        this.isAssignmentClosed = true;
                        this.correct = false;
                    } else {
                    
                        this.correct = json[0]['success'];
                    }
                    
                    if (this.isAssignmentClosed) {
                        this.isAssignmentClosedHidden = false;

                        setTimeout(() => {
                            this.isAssignmentClosedHidden = true;
                        }, 5000);
                    }

                    else {

                        if (this.correct) {
                            this.locked = false;
                            this.isCorrectHidden = false;
                            
                            setTimeout(() => {
                                this.isCorrectHidden = true; 
                            }, 5000);
                        }

                        else if (!this.correct) { 
                            this.isIncorrectHidden = false;
                            
                            setTimeout(() => {
                                this.isIncorrectHidden = true; 
                            }, 5000);

                        }
                    } 

                });
        },
    },


});

const vm = app.mount('#formAndHints');

