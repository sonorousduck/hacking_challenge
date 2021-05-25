
const app = Vue.createApp({
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            isInvisible: true,
            validation: '../validation/',
            correct: false,
            passcodeInput: '',
        }


    },




    methods: {
        getHints() {
            this.isInvisible = !this.isInvisible;
        },

        validateInput(csrf_token) {
            console.log(csrf_token);
            console.log(this.passcodeInput);
            fetch(this.validation, {
                method: "POST",

                body: JSON.stringify({
                    passcode: this.passcodeInput,
                }),

                headers: {'X-CSRFToken': csrf_token},

            })
                .then(response => response.json())
                .then(json => {
                    this.correct = json;
                    console.log(json);

                });
        },
    },


});

const vm = app.mount('#formAndHints');

