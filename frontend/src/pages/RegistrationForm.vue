<template>
    <section class="section">
        <h2 class="title">Вступить в клуб</h2>
        <form action="#" class="form" method="post" @submit.prevent="submit">
            <div class="form__field">
                <FormLabel name="username">Фамилия Имя Отчество</FormLabel>
                <FormInput
                    type="text"
                    name="username"
                    placeholder="Иванов Иван Иванович"
                    required
                    :value="username"
                />
            </div>
            <div class="form__field">
                <FormLabel name="email">Электронная почта</FormLabel>
                <FormInput
                    type="email"
                    name="email"
                    placeholder="Ваша почта"
                    required
                    :value="email"
                />
            </div>
            <div class="form__field">
                <FormLabel name="tel">Телефон</FormLabel>
                <FormInput
                    type="tel"
                    name="tel"
                    placeholder="+78005553535"
                    required
                    :value="tel"
                />
            </div>
            <div class="form__footer">
                <FormButton>Подать заявку</FormButton>
                <p class="form__text">
                    У вас уже есть учетная запись?
                    <a href="#" class="link">Подать заявку</a>
                </p>
            </div>
        </form>
    </section>
</template>

<script>
import FormButton from "@/components/Form/FormButton";
import FormInput from "@/components/Form/FormInput";
import FormLabel from "@/components/Form/FormLabel";

export default {
    name: "RegistrationForm",
    components: {FormLabel, FormInput, FormButton},
    data() {
        return {
            username: '',
            email: '',
            tel: ''
        }
    },
    methods: {
        submit(event) {
            console.log(event);
            // Отправка данных на API
        }
    }
}
</script>

<style>
.form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 32px;
}

.form__field {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}

.form__input {
    border: none;
    outline: none;
    border-bottom: 1px solid #000000;
    padding: 8px 16px;
    width: 550px;
}

.form__label--row {
    display: flex;
    align-items: center;
    gap: 8px;
}

.button {
    background-color: #61892F;
    border: none;
    cursor: pointer;
    width: 320px;
    color: #fff;
    box-shadow: 8px 8px 8px rgba(62, 95, 23, 0.5);
    border-radius: 5px;
    padding: 8px 0 10px;
}

.link {
    color: #61892F;
    text-decoration: none;
}
</style>
