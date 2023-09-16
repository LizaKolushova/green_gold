<template>
    <section class="section">
        <h2 class="title">Войти</h2>
        <form action="#" class="form" method="post" @submit.prevent="submit">
            <div class="form__field">
                <FormLabel name="email">Электронная почта</FormLabel>
                <FormInput
                    type="email"
                    name="email"
                    placeholder="Ваша почта"
                    required
                    v-model="email"
                />
            </div>
            <div class="form__field">
                <FormLabel name="password">Пароль</FormLabel>
                <FormInput
                    type="password"
                    name="password"
                    placeholder="Ваш пароль"
                    required
                    v-model="password"
                />
            </div>
            <div class="form__field">
                <FormLabel
                    name="save"
                    row
                >
                    <FormCheckbox
                        type="checkbox"
                        name="save"
                        v-model="save"
                    />
                    Запомнить меня
                </FormLabel>
            </div>
            <div class="form__footer">
                <FormButton>Войти</FormButton>
                <p class="form__text">
                    У вас еще нет учетной записи?
                    <a href="#" class="link">Вступить в клуб</a>
                </p>
                <a href="#" class="link">Забыли пароль?</a>
            </div>
        </form>
        {{email}}
        {{password}}
        {{save}}
    </section>
</template>

<script>
import FormButton from "@/components/Form/FormButton";
import FormInput from "@/components/Form/FormInput";
import FormLabel from "@/components/Form/FormLabel";
import FormCheckbox from "@/components/Form/FormCheckbox";

export default {
    name: "LoginForm",
    components: {FormCheckbox, FormLabel, FormInput, FormButton},
    data() {
        return {
            email: 'email',
            password: '',
            save: false
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
    .title {
        margin-bottom: 25px;
    }

    .form {
        display: flex;
        flex-direction: column;
        gap: 32px;
    }

    @media (min-width: 576px) {
        .form {
            align-items: center;
        }
    }

    .form__field {
        display: flex;
        flex-direction: column;
        gap: 8px;
        align-items: flex-start;
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
