
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
        }


    },

    mounted() {
        this.isLoaded = true;

    },



    methods: {
        getHints() {
            this.isInvisible = !this.isInvisible;
        },

        validateInput() {
            console.log(this.passcodeInput);
            let formData = new FormData();
            formData.append("passcode", this.passcodeInput);
            // TODO: Instead of taking out of the form, preferably would be to get it straight from Django. Or instead of making a fetch to an overall validation, when it goes to challenges/1/validation, it auto gets its challenge_id from that instead.
            formData.append("challenge_id", document.querySelector('#challenge_id').value);

            fetch(this.validation, {
                method: "POST",

                body: formData,

                headers: {'X-CSRFToken': document.querySelector('#csrf_token').value},

            })
                .then(response => response.json())
                .then(json => {
                    this.correct = json[0]['success'];
                    console.log(this.correct);
    

                    if (this.correct) {
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
                    

                });
        },
    },


});

const vm = app.mount('#formAndHints');

