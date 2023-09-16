<template>
    <input
        :type="type"
        :name="name"
        :id="name"
        :required="required"
        :placeholder="placeholder"
        :value="value"
        @input="$emit('input', $event.target.value)"
        class="form__input"
    >
</template>

<script>
export default {
    name: "FormInput",
    emits: ['update:modelValue'],
    props: {
        type: {
            type: String,
            default: 'text'
        },
        name: {
            type: String,
            required: true
        },
        required: {
            type: Boolean,
            default: false
        },
        placeholder: {
            type: String,
            default: ''
        },
        value: {
            type: [String, Boolean, Number],
            required: true
        }
    }
}
</script>

<style>
    .form__input {
        border: none;
        outline: none;
        border-bottom: 1px solid #000000;
        padding: 8px 16px;
        width: 100%;
    }

    @media (min-width: 576px) {
        .form__input {
            width: 550px;
        }
    }
</style>
