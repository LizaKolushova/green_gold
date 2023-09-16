<template>
    <label
        :for="name"
        class="form__label"
        :class="{'form__label--row': row}"
    >
        <slot></slot>
    </label>
</template>

<script>
export default {
    name: "FormLabel",
    props: {
        name: {
            type: String,
            default: ''
        },
        row: {
            type: Boolean,
            default: false
        }
    }
}
</script>

<style>
    .form__label--row {
        display: flex;
        align-items: center;
        gap: 8px;
    }
</style>
